---
title: writing_th skill — MCP-first retrieval + outline-stop + learn-back
tags: [writing_th, skill, mcp, workflow, thai-writing]
created: 2026-03-11
source: rrr: Arun_Creagy
---

# writing_th skill — MCP-first retrieval + outline-stop + learn-back

## Pattern
For a writing skill that must mirror a specific human voice (Thai-first) and use a non-hardcoded citation style, the skill must enforce a handshake that pulls from the Oracle brain before generating.

**Handshake sequence:**

1) **Retrieve (MCP only)**
- Call MCP tools (e.g., `oracle_concepts`, `oracle_search`) to retrieve writing patterns and citation patterns.
- Prefer canonical, stable constraints in resonance:
  - `ψ/memory/resonance/writing-style.md`
  - `ψ/memory/resonance/citation-style.md`
- Use learnings tagged `writing_th` for evolving examples.

2) **Intake (minimal)**
- Ask only for missing: mode (`--report`/`--article`), topic/objective, audience, length, constraints, and sources.

3) **Outline-first stop**
- Always produce a numbered Thai outline first.
- Stop and wait for confirmation before drafting.

4) **Draft with constraints**
- Thai-first.
- English only when unavoidable.
- No quote marks for emphasis; use **bold**.
- Avoid parenthetical English glosses.

5) **Learn-back**
- After approval, call `oracle_learn` to save a new learning pattern: what worked, what structure was used, and a short excerpt.
- If stable style rules changed, append-only update resonance notes.

## Why it works
- Ensures the writing is grounded in “your Oracle memory” rather than generic LLM defaults.
- The outline stop preserves human control (External Brain, Not Command).
- The learn-back loop makes improvement incremental and auditable.

## Confidence
High. This pattern aligns with how Oracle v2 is intended to access and evolve memory.

