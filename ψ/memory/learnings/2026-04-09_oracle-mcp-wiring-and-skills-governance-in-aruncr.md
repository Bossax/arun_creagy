---
title: Oracle MCP wiring and skills governance in Arun_Creagy
tags: [oracle, mcp, docker, bun, skills-governance, configuration]
created: 2026-04-09
source: rrr: Arun_Creagy
---

# Oracle MCP wiring and skills governance in Arun_Creagy

Oracle MCP wiring and skills governance in Arun_Creagy

Pattern
- Run the Oracle MCP entrypoint (src/index.ts) inside the same Bun Docker container that hosts the HTTP engine, using docker exec -i <container> bun src/index.ts, so both HTTP and MCP share the same Linux runtime, Bun version, /vault mapping, database, and vector index.
- Treat .roo/mcp.json as code, not just config: validate JSON, avoid docker run src/index.ts patterns that treat TypeScript paths as images, and explicitly wire args, cwd, and env to match docker-compose.
- Keep a clear separation between oracle-skills installed for agents (Claude Code, Codex) under ~/.claude and ~/.codex, and Roo’s own skill trees under ~/.roo and .roo/, since oracle-skills-cli updates the agent skills but does not modify Roo’s internal skills.

Why it matters
- Prevents divergence between HTTP and MCP behavior by eliminating split runtimes (Windows vs Linux) and ensuring both entrypoints see the same filesystem and database.
- Reduces downtime from subtle MCP misconfigurations and makes it easier to debug connection errors by having a single, explicit command for how MCP is started.
- Clarifies the blast radius of global oracle-skills updates and avoids confusion about which parts of the system have changed after running the installer.

Tags
- oracle
- mcp
- docker
- bun
- skills-governance
- configuration

---
*Added via Oracle Learn*
