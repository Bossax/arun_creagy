import { $ } from "bun";

const iso = new Date().toISOString();
const monthDir = `ψ/memory/retrospectives/${iso.slice(0, 7)}`;

console.log("platform:", process.platform);
console.log("iso:", iso);
console.log("SHELL:", process.env.SHELL);
console.log("COMSPEC:", process.env.COMSPEC);
console.log("BUN_SHELL:", process.env.BUN_SHELL);
console.log("which ls:", Bun.which("ls"));
console.log("monthDir:", monthDir);

const run = async (label: string, cmd: ReturnType<typeof $>) => {
  try {
    const text = await cmd.text();
    console.log(label, "exit:", cmd.exitCode);
    console.log(label, "stdout:");
    console.log(text);
  } catch (err) {
    console.log(label, "error:", err);
  }
};

await run("bun:$ ls -t", $`ls -t ${monthDir}/*/*.md 2>/dev/null`);
await run("bun:$ bash -lc ls -t", $`bash -lc "ls -t ${monthDir}/*/*.md 2>/dev/null"`);
