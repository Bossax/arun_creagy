---
title: # Lesson — writing-th Option C skill redesign (Oracle-aligned)
tags: []
created: 2026-04-15
source: ψ/memory/learnings/2026-03-28_lesson-writing-th-option-c-skill-redesign-oracle.md
---

# # Lesson — writing-th Option C skill redesign (Oracle-aligned)

# Lesson — writing-th Option C skill redesign (Oracle-aligned)

## Pattern

When the user wants Thai drafting that can closely mimic a specific “example report” style **without losing** the Oracle’s stable voice and safety rules, use a layered style system:

1) Example report (session reference) is PRIMARY for terminology + section flow.
2) Write a timestamped Session Style Pack Summary into the writing plan (append-only).
3) Apply resonance as safety rails (citations, hedging, no hallucinated sources).
4) Store evolving improvements as learnings; promote stable rules to resonance only after repetition or explicit approval.

## Execution / learning separation

- [`/writing-th`](.roo/skills/writing-th/SKILL.md) handles the **Option C handshake before drafting**:
  - MCP-first retrieval via tools like `oracle_concepts()` and `oracle_search()` to pull style and citation patterns from resonance notes (for example, `ψ/memory/resonance/writing-style.md` and `ψ/memory/resonance/citation-style.md`).
  - Minimal intake: ask only for missing: mode (`--report`/`--article`), topic/objective, audience, length, constraints, and sources.
  - Outline-stop: always produce a numbered Thai outline first and **stop for human confirmation** before any drafting.
  - Drafting: after approval, generate Thai-first text that follows the outline and applies the layered style system and safety rails.

- [`/writing-th-learn`](.roo/skills/writing-th-learn/SKILL.md) handles the **diff-based learn-back loop**:
  - Take the draft, the edited version, and any human-written edit-pattern analysis notes as inputs.
  - Distil "rules of writing" and structural patterns (not paragraphs of report text) into a learning note under `ψ/memory/learnings/` with clear session context.
  - Call `oracle_learn()` with these distilled patterns and tags so they become reusable, cross-session Oracle learnings, keeping promotion of long-lived rules into resonance explicit and append-only.

## Operational guardrail

`oracle_learn()` may report success but the file can be missing on disk.

- Verify and materialize per: [`ψ/memory/learnings/2026-03-27_oracle-learn-file-materialization-guardrail.md`](ψ/memory/learnings/2026-03-27_oracle-learn-file-materialization-guardrail.md)

---
*Added via Oracle Learn*
