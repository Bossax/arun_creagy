---
title: # Learning — CRI Phase 1 Data Pipeline & Execution Discipline
tags: []
created: 2026-04-15
source: ψ/memory/learnings/2026-04-02_cri-phase1-data-pipeline-discipline.md
---

# # Learning — CRI Phase 1 Data Pipeline & Execution Discipline

# Learning — CRI Phase 1 Data Pipeline & Execution Discipline

**Date**: 2026-04-02
**Type**: info
**Status**: raw
**Significance**: important

## Pattern

For CRI Phase 1, the safest and most efficient pattern is:

1. **Pilot-first, minimal change**
   - Reuse the CRI pilot datasets (DDPM, OAE relief, NESDC GPP, DOPA population, pilot Excel) as the spine.
   - Request updated extracts from the same agencies, but do not invent new data families unless necessary.
   - Introduce new spatial layers only for dasymetric mapping and gap detection.

2. **Pipeline as explicit processes, not ad-hoc steps**
   - Encode the work as a small set of processes (P1–P8): inventory → clean → build impact variables → prepare denominators → construct exposure proxies → constrained redistribution → gap flags → evidence + freeze.
   - Keep these processes documented in the CRI project output, not in global plans.

3. **Execution discipline in Code mode**
   - Default to concrete actions (file moves, edits, commands) with minimal narration when instructions are clear.
   - Avoid describing desired state without using tools to create it.
   - Translate SKILL shell snippets (like `/rrr`) into discrete `execute_command` + file edits instead of copying heredocs that are fragile in the hybrid shell.

## Why it matters

This pattern keeps CRI Phase 1 honest about its lineage (pilot-first), minimizes unnecessary refactoring, and makes the data pipeline auditable. At the same time, it respects the workspace’s hybrid shell constraints and the brain structure that expects assistant outputs to live under `ψ/incubate/DCCE/CRI/output/` and `ψ/memory/…`, not at the top level.

## Next use

When starting any CRI Phase 1–related session:
- Load the CRI Phase 1 pipeline plan, workflow, and checklist from `ψ/incubate/DCCE/CRI/output/`.
- Treat the 8 processes as the canonical todo for data work.
- Enforce the “do, don’t just describe” rule for filesystem and git operations.

Logged via /rrr

---
*Added via Oracle Learn*
