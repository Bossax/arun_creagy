---
name: oracle-bridge
description: v1.0.0 | Infrastructure-as-Code (IaC) engine for Oracle environment anchoring on win32/PowerShell.
---

# /bridge — Oracle Infrastructure Anchor

**Goal**: Establish a drift-free local environment for Oracle agents by standardizing shell behavior, brain structure, and MCP configuration.

## Objective
Provide a reliable "Silicon Anchor" that ensures portable and persistent agent environments, guaranteeing compliance with the Upstream Registry (ψ/) and Silicon Mandates across distributed workspaces.

## Scope
- **In**: 
  - `ψ/` brain structure integrity (7-pillar verification).
  - `docker-compose.yml` physical anchor drift detection.
  - MCP settings management (surgical merge of fleet standards).
  - Silicon Mandate injection (`.gemini/`, `.roo/`).
- **Out**:
  - Inter-agent communication or message transport.
  - `contacts.json` registry management.
  - External network interaction.

## Usage
```bash
bun .gemini/skills/oracle-bridge/scripts/init-bridge.ts --cwd=<path> # Anchor local infrastructure
```