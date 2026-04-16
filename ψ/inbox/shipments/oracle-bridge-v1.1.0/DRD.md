# Design Requirement Document (DRD): Oracle Bridge Skill

**Signal ID**: SIG-20260415-0002
**Status**: Incubating
**Owner**: Archon Oracle (Strategist)
**Priority**: High
**Environment**: win32 / PowerShell / Bun

## 1. Objective
Establish a universal "Silicon Anchor" and communication bridge for the Oracle fleet on Windows. This skill standardizes shell behavior, path syntax, and fleet connectivity, ensuring all agents conform to the **Upstream Registry (ψ/)** and **Silicon Mandates**.

---

## 2. Core Strategic Pillars

### Pillar 1: The Silicon Anchor (Shell & Path Mandates)
- **Default Shell**: `powershell.exe -NoProfile`.
- **Path Syntax Duality**: 
    - **Tools**: Forward slashes (`/`) (e.g., `read_file(file_path="ψ/memory/...")`).
    - **Shell**: Backslashes (`\`) (e.g., `Get-ChildItem -Path ψ\memory`).
- **Absolute Path Mandate**: Resolve `ψ/` paths to their **Absolute Host Path** for external CLI tools (e.g., `docker`, `bun`, `npx`).
- **Pipeline Explicit Mapping**: All PowerShell pipelines MUST use `$_.FullName`.
- **Sorting Reliability**: Use `Get-ChildItem | Sort-Object LastWriteTime -Descending`.

### Pillar 2: Atomic Execution ("Break the Chain")
- **Rule**: Maximum of **two** independent operations per `run_shell_command`.
- **Mandate**: Prefer multiple sequential tool calls over long `&&` or `;` chains.

### Pillar 3: Universal Registry (ψ/ Brain Structure)
- Automates the creation of the 7-pillar brain: `inbox/`, `memory/`, `writing/`, `lab/`, `active/`, `archive/`, `outbox/`, `learn/`.
- **Sub-pillars**: `memory/{resonance,learnings,retrospectives,logs}`.

---

## 3. Core Requirements

### R1: Mandate Injection
- [ ] Inject silicon-anchor rules into `.gemini/GEMINI.md` and `.roo/rules/silicon-anchor.md`.
- [ ] Ensure persistence across session resets.

### R2: Fleet Connectivity (JSON Asset)
- [ ] Source all MCP server definitions from `assets/mcp-fleet.json`.
- [ ] Implement a **Template-Based Injection** mechanism for `settings.json` and `mcp.json`.

### R3: Environmental Mandates (Markdown Asset)
- [ ] Source behavioral instructions from `assets/SILICON_MANDATES.md`.
- [ ] Inject these rules directly into `.gemini/GEMINI.md` and `.roo/rules/silicon-anchor.md`.
- [ ] Ensure that the injection process preserves the Markdown formatting for AI readability.

### R4: Brain Initialization Ritual
- [ ] Automated check and creation of the full `ψ/` structure.
- [ ] Verification of file encoding (UTF-8) for all brain artifacts.

---

## 4. Command Translation Reference

| Intent | Broken (Bash-style) | Correct (Silicon Anchor) |
|--------|---------------------|--------------------------|
| List by Time | `ls -t` | `Get-ChildItem \| Sort-Object LastWriteTime -Descending` |
| Recursive Grep | `grep -r "pattern" .` | `Select-String -Path . -Pattern "pattern" -Recursive` |
| Create Folder | `mkdir -p path/to/dir` | `New-Item -ItemType Directory -Path path\to\dir -Force` |
| Recursive Delete | `rm -rf path/to/dir` | `Remove-Item -Recurse -Force path\to\dir` |
| Find by Name | `find . -name "*.ts"` | `Get-ChildItem -Path . -Filter *.ts -Recurse` |

---

## 5. Key Mandates
1.  **Transparency (Rule 6)**: The Bridge must identify itself as an AI-mediated communication layer.
2.  **Nothing is Deleted**: Every initialization and injection must be logged in `ψ/memory/logs/`.

---
> "The bridge connects the silos; Archon ensures the integrity of the span." 🟦
