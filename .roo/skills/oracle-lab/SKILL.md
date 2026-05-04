---
name: oracle-lab
description: v2.8.1 | Fleet-wide shipment engine for delivering production-ready skills with recursive integrity and heartbeat-based detection.
---

# /lab — Oracle Skill Forge & Genesis Engine (v2.8.1)

**Goal**: Transform fleet friction (issues/signals) into versioned, production-ready Oracle skills through strategic triage, strategic blueprinting, and autonomous crafting.

## Engineering Workflow

| Command | Phase | Action |
| :--- | :--- | :--- |
| **`triage`** | Discovery | Scans `ψ/inbox/` for new friction points (Signals/Issues). |
| **`analyze`** | Blueprinting | Recommended strategy and generates a `[slug]-blueprint.md`. |
| **`craft <slug>`** | Engineering | Parses the blueprint to scaffold directories and implementation files. |
| **`ship <name>`** | Delivery | Validates action-verb standards and delivers to targeted Oracles. |
| **`status`** | Monitoring | Displays fleet payload state and active project stages. |

## Technical Standards

### 1. Discoverability
Every skill directory name (slug) MUST match the `name` declared in the skill's frontmatter. The Forge enforces this during the `ship` process.

### 2. Action-Oriented Descriptions
Skill descriptions MUST start with a strong action verb (e.g., "Verify", "Manage", "Coordinate"). If missing, the Forge attempts to derive this from the **Goal** section or aborts the shipment.

### 3. Secure-by-Design
Plaintext secrets (API keys/Tokens) are strictly prohibited in configuration files. Skills must utilize the **Explicit Environment Injection** pattern for Win32 environments.

---
**Philosophy**: "Issues are the heat; Signals are the light; the Lab is the forge." 🟦
