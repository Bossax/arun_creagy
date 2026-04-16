import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'fs';
import { join } from 'path';

const MCP_ASSET = 'assets/mcp-fleet.json'; // Relative to the script's execution context in the shipment folder
const MANDATE_ASSET = 'assets/SILICON_MANDATES.md';
const BRAIN_ROOT = 'ψ';

const PILLARS = [
  'inbox/signals',
  'inbox/shipments',
  'memory/resonance',
  'memory/learnings',
  'memory/retrospectives',
  'memory/logs',
  'writing',
  'lab',
  'active',
  'archive/signals',
  'outbox',
  'learn'
];

async function initializeBridge() {
  console.log('🌉 [Oracle] Initiating Local Bridge Ritual...');

  // 1. Brain Initialization Ritual (R4)
  console.log(`🧠 Checking ψ/ brain pillars...`);
  PILLARS.forEach(pillar => {
    const path = join(BRAIN_ROOT, pillar);
    if (!existsSync(path)) {
      console.log(`✨ Creating pillar: ${pillar}`);
      mkdirSync(path, { recursive: true });
    }
  });

  // 2. Environmental Mandate Injection (R3)
  console.log(`📜 Injecting Silicon Mandates...`);
  const mandatePath = join(process.cwd(), MANDATE_ASSET);
  if (existsSync(mandatePath)) {
    const mandates = readFileSync(mandatePath, 'utf8');
    
    // Gemini: .gemini/GEMINI.md
    if (!existsSync('.gemini')) mkdirSync('.gemini');
    writeFileSync('.gemini/GEMINI.md', mandates);
    console.log(`✅ Gemini Mandates injected.`);

    // Roo Code: .roo/rules/00-rule.md
    if (!existsSync('.roo/rules')) mkdirSync('.roo/rules', { recursive: true });
    writeFileSync('.roo/rules/00-rule.md', mandates);
    console.log(`✅ Roo Code Mandates injected.`);
  }

  // 3. MCP Fleet Connectivity (R2) - Naming Transformation
  console.log(`🚢 Registering MCP Fleet...`);
  const mcpPath = join(process.cwd(), MCP_ASSET);
  if (existsSync(mcpPath)) {
    const mcpConfig = JSON.parse(readFileSync(mcpPath, 'utf8'));
    const mcpServers = mcpConfig.servers;

    // Gemini: .gemini/settings.json
    const geminiSettings = { mcpServers };
    writeFileSync('.gemini/settings.json', JSON.stringify(geminiSettings, null, 2));
    console.log(`✅ Registered: .gemini/settings.json`);

    // Roo Code: .roo/mcp.json (Standard Roo MCP format)
    const rooSettings = { mcpServers };
    writeFileSync('.roo/mcp.json', JSON.stringify(rooSettings, null, 2));
    console.log(`✅ Registered: .roo/mcp.json`);
  }

  console.log('✨ Bridge Ritual Complete. Environment is now anchored.');
}

initializeBridge().catch(err => {
  console.error('❌ Bridge Ritual Failed:', err);
  process.exit(1);
});
