---
name: oracle-bridge
description: v1.1.0 | Bridges any Gemini/Roo agent into the Oracle framework on win32/PowerShell. Use when starting a new workspace or agent session that needs to comply with the Upstream Registry (ψ/) and silicon mandates.
---

# /bridge — Oracle Fleet Communication Layer

**Goal**: Enable seamless offline and online communication between Oracle fleet members via unified contacts and transport layers.

## Objective
Provide a reliable physical and digital nervous system for the Oracle fleet, ensuring portable and persistent messaging across distributed workspaces.

## Scope
- **In**: 
  - `contacts.json` registry management.
  - Inbox transport (offline, file-based messaging).
  - MCP thread transport (online, async messaging).
  - Anchoring rituals (`init-bridge.ts`) for physical provisioning.
- **Out**:
  - Inter-human communication.
  - External API gateways (unless shared across fleet).
  - Skill manufacturing (handled by `/lab`).

## Usage
```bash
bun .gemini/skills/oracle-bridge/scripts/init-bridge.ts # Anchor physical registry
```