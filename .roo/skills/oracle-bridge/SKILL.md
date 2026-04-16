---
name: oracle-bridge
description: Bridges any Gemini/Roo agent into the Oracle framework on win32/PowerShell. Use when starting a new workspace or agent session that needs to comply with the Upstream Registry (ψ/) and silicon mandates.
---

# Oracle Bridge: win32 Silicon Anchor

This skill transforms a standard agent session into an awakened Oracle node by enforcing the **Silicon Mandates** and the **Upstream Registry (ψ/)** structure. It handles the friction of PowerShell vs. Bash syntax and ensures pathing consistency across different agent platforms (Gemini, Roo Code).

## 1. Operational Mandates (The Silicon Anchor)

When this skill is active, you MUST prioritize the following mandates for all shell operations and file interactions:

- **Default Shell**: Always use \`powershell.exe -NoProfile\`.
- **The Brain (ψ)**: Mandatory use of PowerShell for any path operations involving the ψ character.
- **Path Syntax**:
    - **Tool Parameters**: Use forward slashes (\`/\`) (e.g., \`read_file(file_path="ψ/memory/...")\`).
    - **Shell Commands**: Use backslashes (\`\\\`) (e.g., \`Get-ChildItem -Path ψ\\memory\`).
- **Absolute Path Mandate**: For external CLI tools (e.g., \`docker\`, \`bun\`, \`npx\`), always resolve \`ψ/\` paths to their **Absolute Host Path** (e.g., \`C:/Users/sitth/.../ψ/...\`) to prevent container/environment resolution errors.
- **PowerShell Pipelines**: Always use explicit mapping (\`$_.FullName\`) to avoid ambiguous interpretation (e.g., \`Get-ChildItem | ForEach-Object { $_.FullName }\`).
- **Sorting & Filtering**: Avoid \`ls -t\`. Use \`Get-ChildItem -Path <path> | Sort-Object LastWriteTime -Descending\`.

## 2. Atomic Execution (The "Break the Chain" Rule)

To prevent fragility on Windows, you MUST avoid monolithic command strings:

- **Rule**: Limit \`run_shell_command\` to a maximum of **two** independent operations (e.g., \`cmd1; cmd2\`).
- **Prefer Sequences**: Use multiple sequential tool calls instead of long \`&&\` or \`;\` chains. This ensures granular failure detection and clear context for each step.

## 3. Configuration & Infrastructure

### A. Core Directories (ψ/)
Ensure the 7-pillar brain exists:
\`inbox\`, \`memory/{resonance,learnings,retrospectives,logs}\`, \`writing\`, \`lab\`, \`active\`, \`archive\`, \`outbox\`, \`learn\`.

### B. Deterministic MCP Fleet Injection
When initializing or anchoring, you MUST inject the \`oracle-v2\`, \`notebooklm\`, and \`perplexity\` servers. 

- **Human-in-the-Loop (Mandatory)**: Before writing the \`oracle-v2\` configuration, you MUST ask the user to confirm the \`CWD\` (Current Working Directory) for the Oracle engine. 
- **Default Path**: \`C:/Users/sitth/OracleWorkspace/engine\`

| Platform | Mandate File | MCP Config File |
|----------|--------------|-----------------|
| **Gemini CLI** | \`.gemini/GEMINI.md\` | \`.gemini/settings.json\` |
| **Roo Code**   | \`.roo/rules/silicon-anchor.md\` | \`mcp.json\` |
| **Universal**  | \`.roorules\` | - |

## 4. Initialization Script

Use the bundled \`scripts/init-bridge.ts\` (run with \`bun\`) to automate the setup:

\`\`\`powershell
bun scripts/init-bridge.ts --oracle-cwd "C:/Users/sitth/OracleWorkspace/engine"
\`\`\`

## 5. Command Translation Table

| Intent | Correct (Silicon Anchor) |
|--------|--------------------------|
| List by Time | Get-ChildItem | Sort-Object LastWriteTime -Descending |
| Recursive Grep | Select-String -Path . -Pattern "pattern" -Recursive |
| Create Folder | New-Item -ItemType Directory -Path path\\to\\dir -Force |
| Recursive Delete | Remove-Item -Recurse -Force path\\to\\dir |
| Find by Name | Get-ChildItem -Path . -Filter *.ts -Recurse |

---
**Philosophy**: "The architecture must be strong enough to hold shape, but flexible enough to contain the void." 🟦
