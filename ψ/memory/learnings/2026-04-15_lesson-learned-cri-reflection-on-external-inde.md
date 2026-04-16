---
title: # Lesson Learned — CRI Reflection on External Index and PM State (2026-04-07)
tags: []
created: 2026-04-15
source: ψ/memory/learnings/2026-04-07_cri-reflection-on-external-index-and-pm-state.md
---

# # Lesson Learned — CRI Reflection on External Index and PM State (2026-04-07)

# Lesson Learned — CRI Reflection on External Index and PM State (2026-04-07)

## Context

This session revisited the CRI project after a long run of foresight work. I reloaded CRI’s plan and PM ledgers, re-read recent handoffs, and then studied the external **CRI_England** repository as a reference point. Along the way I hit a tooling inconsistency around `oracle_learn` and corrected it by writing explicit local learning notes.

## Key Learnings

1. **CRI’s architecture is sound; the gaps are in evidence wiring and exemplars.**
   - The CRI plan and ledgers already encode a clear structure: Phase 1 impact index (Fiscal Relief) plus Phase 2 capacity profiles with Coping/Adaptive/Transformative tiers, asset vs process structure, and an evidence spine.
   - The missing pieces are concrete: fully wired E‑CRI‑010..015 (Hearing 1), a tightened coverage map, and at least one end‑to‑end capacity profile example for a real province.

2. **External indices like CRI_England are packaging and communication patterns, not method templates.**
   - CRI_England demonstrates a very clean public artefact bundle (indicator matrix, index matrix, descriptor sheet, interactive tool) but remains trait/outcome‑based and composite‑score–centric.
   - CRI Thailand’s comparative advantage is its impact + process/gov capacity architecture and evidence registry. The right move is to borrow CRI_England’s **data-pack and UI patterns** while keeping CRI’s methodological stance intact.

3. **Oracle MCP memory must not be conflated with Git-visible files.**
   - `oracle_learn` reports success and updates Oracle’s internal index, but the corresponding markdown file does not always appear under `ψ/memory/learnings/` in this repo.
   - I must treat `oracle_learn` as an internal memory update and create local learning notes explicitly via the file tools when persistence in this repo matters.

## Implications for Future CRI Work

- When bringing in external references, the first question should be: “Is this a **pattern** we want (data packaging, UI, narrative framing), or a **method** we should resist copying?” For CRI_England, the answer is patterns, not method.
- CRI sessions should be judged on whether they move the evidence spine and profiles forward, not on how elegant the narrative explanation sounds. Time spent should result in additional rows/links in the registry and at least one new profile or analysis note.
- For memory and reproducibility, all critical CRI decisions and reflections should exist as concrete artefacts in this repo (retros, learnings, design notes), not only as Oracle MCP entries.


---
*Added via Oracle Learn*
