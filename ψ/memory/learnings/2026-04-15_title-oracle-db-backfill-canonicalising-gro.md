---
title: ---
tags: [oracle-db, backfill, canonicalisation, notebooklm, writing_th, crdb, multi-stage-reports, supersede-metadata]
created: 2026-04-15
source: ψ/memory/learnings/2026-04-11_oracle-db-backfill-group6-7-canonicalisation.md
---

# ---

---
title: Oracle DB backfill — canonicalising Groups 6–7 before Phase 2.2
created: 2026-04-11
type: learning
concepts:
  - oracle-db
  - backfill
  - canonicalisation
  - notebooklm
  - writing_th
  - crdb
  - multi-stage-reports
  - supersede-metadata
source: rrr: Arun_Creagy
---

# Oracle DB backfill — canonicalising Groups 6–7 before Phase 2.2

## Pattern

Before running a new backfill wave into Oracle DB from an existing learning corpus, first canonicalise dense learning clusters so that the DB receives a small number of stable, cross‑project patterns instead of many overlapping local notes.

In this session, two merge groups were finalised:

1. **Group 6 — writing-th Option C skill design**
   - Elevated [`ψ/memory/learnings/2026-03-28_lesson-writing-th-option-c-skill-redesign-oracle.md`](ψ/memory/learnings/2026-03-28_lesson-writing-th-option-c-skill-redesign-oracle.md) as the canonical design note for writing_th Option C.
   - Marked related notes (`writing_th` MCP handshake, CRDB edit-session learn-back, RRR Option C retrospective) as `status: superseded` with `superseded_by` pointing to the canonical.
   - Ensured the canonical explicitly encodes: MCP-first retrieval via MCP tools, minimal intake, outline-stop before drafting, diff-based learn-back via `/writing-th-learn`, and strict `oracle_learn()` materialisation guardrails.

2. **Group 7 — CRDB interim vs final report structure & revision cycle**
   - Elevated [`ψ/memory/learnings/2026-04-09_for-multi-stage-reports-separate-final-report-str.md`](ψ/memory/learnings/2026-04-09_for-multi-stage-reports-separate-final-report-str.md) as the general multi-stage report pattern (not CRDB-specific).
   - Marked earlier CRDB notes on Chapter 2 scope, progress-first Section 1, and rewrite planning as `status: superseded` with `superseded_by` pointing to the multi-stage canonical.
   - Treated revision-cycle logic as its own pattern in [`ψ/memory/learnings/2026-04-09_when-an-interim-report-is-explicitly-scheduled-for.md`](ψ/memory/learnings/2026-04-09_when-an-interim-report-is-explicitly-scheduled-for.md), already present in Oracle DB.

## Group 6–7 mapping to indexing-map

- **Indexing-map Group 6** → represented here by the writing_th Option C architecture pattern and its canonical note at [`ψ/memory/learnings/2026-03-28_lesson-writing-th-option-c-skill-redesign-oracle.md`](ψ/memory/learnings/2026-03-28_lesson-writing-th-option-c-skill-redesign-oracle.md).
- **Indexing-map Group 7** → represented here by the multi-stage report structure and revision-cycle pattern, with CRDB as the main worked example and canonicalised in [`ψ/memory/learnings/2026-04-09_for-multi-stage-reports-separate-final-report-str.md`](ψ/memory/learnings/2026-04-09_for-multi-stage-reports-separate-final-report-str.md) plus the revision-cycle note.
- This file is the **joint canonical** for Groups 6–7 when projecting the corpus into Oracle DB and when recording backfill rows in [`ψ/memory/logs/info/backfill-index.md`](ψ/memory/logs/info/backfill-index.md).

## Why it works

- **Reduces duplication in Oracle DB**: Only canonical patterns (Option C architecture, multi-stage report structure, revision gate) are backfilled, avoiding a DB full of near-duplicates.
- **Keeps history without clutter**: Superseded notes remain as provenance, but their metadata makes it clear which learning should be treated as current when querying or backfilling.
- **Aligns corpus and DB**: The canonical notes match what Oracle DB already knows from log-based backfill, making it easier to reason about which concepts are “live” in both the markdown vault and the DB.

## How to apply

1. When encountering a dense set of related learnings, choose one canonical note that states the cross‑project rule or architecture and promotes project-specific details to examples.
2. Mark all older or narrower notes as `status: superseded` and add a `superseded_by` pointer to the canonical file path.
3. Backfill only the canonical note into Oracle DB via `arra_learn()` (or confirm an existing `oracle_learn()` entry) and record the canonical Oracle ID alongside the source file path in [`ψ/memory/logs/info/backfill-index.md`](ψ/memory/logs/info/backfill-index.md).
4. For future selection, filter learnings by `status != superseded` when proposing candidates for backfill.

## Confidence

High. The pattern is already applied to Groups 3–7 and aligns with the existing Oracle DB snapshot and backfill index, preserving history while keeping the DB projection small and curated.


---
*Added via Oracle Learn*
