---
title: Skill development — separate Oracle memory access (MCP) from integration APIs (HTTP)
tags: [skill-dev, architecture, mcp, http, oracle-v2, workflow]
created: 2026-03-11
source: rrr: Arun_Creagy
---

# Skill development — separate Oracle memory access (MCP) from integration APIs (HTTP)

## Problem
When building a new skill, it’s easy to mix up two valid access layers:

- **MCP tools**: the agent-native way to retrieve and write memory (search, learn, reflect).
- **HTTP APIs**: useful for UIs, dashboards, and external integrations.

If a skill uses HTTP endpoints for “memory retrieval,” it creates fragile plumbing, duplicates responsibility, and makes the skill drift away from the Oracle architecture.

## Pattern

1) **Memory retrieval must be MCP-first**
- Skill handshake should explicitly call MCP tools to retrieve resonance + learnings.

2) **Runners are formatting-only**
- A TypeScript runner can exist, but it must not query Oracle DB or call MCP.
- Use it only to transform external inputs (e.g., convert a pasted bibliography table into normalized reference entries).

3) **Keep stable rules in resonance; keep evolving behavior in learnings**
- Resonance: canonical “how we write” and “how we cite.”
- Learnings: session-grounded examples and refinements.

4) **Prefer append-only updates; supersede rarely**
- Append-only preserves history and supports “Nothing is Deleted.”
- Supersede only when you intentionally publish a new canonical spec.

## Example application
The `/writing_th` skill should retrieve `writing-style.md` and `citation-style.md` via MCP tools, then generate an outline and stop; after approval, it should call `oracle_learn` to store a reusable pattern.

## Confidence
High. This separation reduces tool thrash and keeps skills aligned with Oracle’s design.


---
*Added via Oracle Learn*
