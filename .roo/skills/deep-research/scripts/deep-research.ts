#!/usr/bin/env bun
/**
 * Deep Research Automation Script
 *
 * Workflow:
 * 1. Create new Gemini tab
 * 2. Select Deep Research mode
 * 3. Send research prompt
 * 4. Click "Start research" button
 */

const MQTT_HOST = "localhost";
const MQTT_PORT = "1883";
const MQTT_TOPIC_CMD = "claude/browser/command";
const MQTT_TOPIC_RSP = "claude/browser/response";
const MQTT_TOPIC_ANSWER = "claude/browser/answer";

// Get topic from arguments
const topic = Bun.argv.slice(2).join(" ");

if (!topic) {
  console.log("Usage: deep-research.ts <topic>");
  console.log("Example: deep-research.ts compare yeast S-33 vs T-58");
  process.exit(1);
}

console.log(`\n🔬 Deep Research: ${topic}\n`);
console.log(`MQTT: host=${MQTT_HOST} port=${MQTT_PORT}`);
console.log(`MQTT: cmd_topic=${MQTT_TOPIC_CMD} rsp_topic=${MQTT_TOPIC_RSP} answer_topic=${MQTT_TOPIC_ANSWER}\n`);

// Helper to publish MQTT command
async function mqttPub(payload: object): Promise<void> {
  const msg = JSON.stringify(payload);
  const proc = Bun.spawn([
    "mosquitto_pub", "-h", MQTT_HOST, "-p", MQTT_PORT,
    "-t", MQTT_TOPIC_CMD, "-m", msg
  ]);
  await proc.exited;
}

// Helper to subscribe and wait for response
async function mqttSubOnce(timeoutSec: number = 10): Promise<string | null> {
  const proc = Bun.spawn([
    "mosquitto_sub", "-h", MQTT_HOST, "-p", MQTT_PORT,
    "-t", MQTT_TOPIC_RSP, "-C", "1", "-W", String(timeoutSec)
  ], { stdout: "pipe" });

  const output = await new Response(proc.stdout).text();
  await proc.exited;
  return output.trim() || null;
}

type RespMsg = { topic: string; raw: string; data: any };

const responseQueue: RespMsg[] = [];
const responseWaiters: { match: (m: RespMsg) => boolean; resolve: (m: RespMsg | null) => void }[] = [];

function enqueueResponse(msg: RespMsg) {
  responseQueue.push(msg);
  // Resolve any waiters that match
  for (let i = responseWaiters.length - 1; i >= 0; i--) {
    const w = responseWaiters[i];
    if (w.match(msg)) {
      responseWaiters.splice(i, 1);
      w.resolve(msg);
    }
  }
}

function parseLine(line: string): RespMsg | null {
  const trimmed = line.trim();
  if (!trimmed) return null;
  const firstSpace = trimmed.indexOf(' ');
  if (firstSpace === -1) {
    return { topic: MQTT_TOPIC_RSP, raw: trimmed, data: safeJson(trimmed) };
  }
  const topic = trimmed.slice(0, firstSpace);
  const payload = trimmed.slice(firstSpace + 1);
  return { topic, raw: payload, data: safeJson(payload) };
}

function safeJson(text: string) {
  try { return JSON.parse(text); } catch { return text; }
}

function startSubscriber() {
  const proc = Bun.spawn([
    "mosquitto_sub", "-h", MQTT_HOST, "-p", MQTT_PORT,
    "-t", MQTT_TOPIC_RSP,
    "-t", MQTT_TOPIC_ANSWER,
    "-v"
  ], { stdout: "pipe" });

  const stdout = proc.stdout;
  if (!stdout) {
    console.log('⚠️ Subscriber stdout not available');
    return;
  }

  let buffer = "";
  const decoder = new TextDecoder();

  (async () => {
    const reader = stdout.getReader();
    try {
      while (true) {
        const { value, done } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split(/\r?\n/);
        buffer = lines.pop() || "";
        for (const line of lines) {
          const msg = parseLine(line);
          if (msg) enqueueResponse(msg);
        }
      }
    } catch (err) {
      console.log('⚠️ Subscriber read error:', err?.message || err);
    }
    console.log('⚠️ Response subscriber ended unexpectedly');
  })();
}

async function waitForResponse(match: (m: RespMsg) => boolean, timeoutMs: number): Promise<RespMsg | null> {
  // Check queue first
  for (const msg of responseQueue) {
    if (match(msg)) return msg;
  }
  return await new Promise((resolve) => {
    const timer = setTimeout(() => {
      // remove waiter if still pending
      const idx = responseWaiters.findIndex(w => w.resolve === resolve);
      if (idx >= 0) responseWaiters.splice(idx, 1);
      resolve(null);
    }, timeoutMs);
    responseWaiters.push({
      match,
      resolve: (m) => {
        clearTimeout(timer);
        resolve(m);
      }
    });
  });
}

function logPayload(step: string, payload: object): void {
  console.log(`   ↪ ${step} payload: ${JSON.stringify(payload)}`);
}

async function logResponse(step: string, match: { id?: string; action?: string; topic?: string } = {}, timeoutSec: number = 8): Promise<void> {
  console.log(`   ↪ ${step} waiting for response (timeout=${timeoutSec}s)`);
  const res = await waitForResponse((m) => {
    if (match.topic && m.topic !== match.topic) return false;
    if (match.id && m.data?.id !== match.id) return false;
    if (match.action && m.data?.action !== match.action) return false;
    return true;
  }, timeoutSec * 1000);
  if (!res) {
    console.log(`   ⚠️ No response received for ${step}`);
    return;
  }
  console.log(`   ↪ ${step} response: ${typeof res.data === 'string' ? res.data : JSON.stringify(res.data)}`);
}

async function pollForResponse(maxSeconds: number = 180, intervalMs: number = 4000): Promise<void> {
  const start = Date.now();
  let lastState: string | null = null;
  while ((Date.now() - start) / 1000 < maxSeconds) {
    // Query state
    const statePayload = {
      id: `state-${ts()}`,
      action: "get_state",
      ts: ts()
    };
    logPayload("get_state", statePayload);
    await mqttPub(statePayload);
    const stateRes = await waitForResponse((m) => m.data?.id === statePayload.id, 6000);
    if (stateRes) {
      const stateText = typeof stateRes.data === 'string' ? stateRes.data : JSON.stringify(stateRes.data);
      console.log(`   ↪ get_state response: ${stateText}`);
      lastState = stateText;
    } else {
      console.log("   ⚠️ No response received for get_state");
    }

    // Try fetching latest response
    const getRespPayload = {
      id: `getresp-${ts()}`,
      action: "get_response",
      ts: ts()
    };
    logPayload("get_response", getRespPayload);
    await mqttPub(getRespPayload);
    const resp = await waitForResponse((m) => m.data?.id === getRespPayload.id || m.topic === MQTT_TOPIC_ANSWER, 6000);
    if (resp) {
      const respText = typeof resp.data === 'string' ? resp.data : JSON.stringify(resp.data);
      console.log(`   ↪ get_response response: ${respText}`);
      // Heuristic: if response contains "answer" and non-empty, stop polling
      if (respText.includes('"answer"') && respText.match(/"answer"\s*:\s*".{10,}/)) {
        console.log("   ✅ Detected response text. Stopping poll.");
        return;
      }
    } else {
      console.log("   ⚠️ No response received for get_response");
    }

    await Bun.sleep(intervalMs);
  }

  console.log("   ⚠️ Polling timed out without confirmed response. You can check Gemini tab manually.");
}

const ts = () => Date.now();

// Start persistent subscriber to avoid missing responses
startSubscriber();

// Step 1: Create new Gemini tab
console.log("1️⃣ Creating new Gemini tab...");
const createTabPayload = {
  id: `newtab-${ts()}`,
  action: "create_tab",
  url: "https://gemini.google.com/app",
  ts: ts()
};
logPayload("create_tab", createTabPayload);
await mqttPub(createTabPayload);
await logResponse("create_tab", { id: createTabPayload.id }, 8);
await Bun.sleep(6000);
console.log("   ✓ Tab created");

// Step 2: Select Deep Research mode
console.log("2️⃣ Selecting Deep Research mode...");
const selectModePayload = {
  id: `mode-${ts()}`,
  action: "select_mode",
  mode: "Deep Research",
  ts: ts()
};
logPayload("select_mode", selectModePayload);
await mqttPub(selectModePayload);
await logResponse("select_mode", { id: selectModePayload.id }, 12);
await Bun.sleep(6000);
console.log("   ✓ Deep Research selected");

// Step 3: Send research prompt
console.log("3️⃣ Sending research prompt...");
const chatPayload = {
  id: `chat-${ts()}`,
  action: "chat",
  text: topic,
  ts: ts()
};
logPayload("chat", chatPayload);
await mqttPub(chatPayload);
await logResponse("chat", { id: chatPayload.id }, 12);
await Bun.sleep(6000);
console.log("   ✓ Prompt sent");

// Step 4: Click "Start research" button
console.log("4️⃣ Starting research...");
const clickPayload = {
  id: `click-${ts()}`,
  action: "clickText",
  text: "Start research",
  ts: ts()
};
logPayload("clickText(Start research)", clickPayload);
await mqttPub(clickPayload);
await logResponse("clickText(Start research)", { id: clickPayload.id }, 12);
console.log("   ✓ Research started!");

// Step 5: Poll for results and auto-fetch
console.log("5️⃣ Polling for Deep Research results...");
await pollForResponse(240, 5000);

console.log("\n🎉 Deep Research is running! Check your Gemini tab.\n");
