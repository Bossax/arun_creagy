---
title: ---
tags: [oracle-db, pm-ledgers, execution-spine, project-management, crdb, backfill]
created: 2026-04-15
source: ψ/memory/learnings/2026-04-11_oracle-db-phase2.2-pm-ledgers-and-execution-spine-backfill.md
---

# ---

---
title: Oracle DB Phase 2.2 — PM ledgers and execution-spine patterns for backfill
created: 2026-04-11
type: learning
concepts:
  - oracle-db
  - pm-ledgers
  - execution-spine
  - project-management
  - crdb
  - backfill
source: rrr: Arun_Creagy
---

# Oracle DB Phase 2.2 — PM ledgers and execution-spine patterns for backfill

Scope: oracle DB backfill – Phase 2.2 batch of project-management ledger and execution-spine patterns, distilled into a single canonical learning.

## Source artefacts

- [`ψ/memory/learnings/2026-03-27_project-management-ecosystem-facade.md`](ψ/memory/learnings/2026-03-27_project-management-ecosystem-facade.md)
- [`ψ/memory/learnings/2026-03-30_crdb-pm-backfill-definition-and-event-scope.md`](ψ/memory/learnings/2026-03-30_crdb-pm-backfill-definition-and-event-scope.md)
- [`ψ/memory/learnings/2026-04-08_crdb-three-stream-execution-spine-history-ledgers.md`](ψ/memory/learnings/2026-04-08_crdb-three-stream-execution-spine-history-ledgers.md)

These notes are part of the “project-management & PM ledgers (cross-project)” category in [`plans/2026-04-09-learnings-indexing-map.md`](plans/2026-04-09-learnings-indexing-map.md). This canonical learning expresses the cross-project patterns they share.

## Stable patterns

### 1. Ledgers index reality; they do not absorb it

- Canonical ledgers (Trigger Log, Deliverable Map, Submission Log, Claim Register, Change Log) are **navigation surfaces and contracts**, not replacement storage.
- Each ledger row should:
  - point to existing artifacts (notes, evidence, decisions, submissions),
  - record enough context that a reader can reconstruct *why* an entry exists,
  - avoid duplicating full narrative content that already lives in dedicated output files.
- A project-management facade built on these ledgers should behave as a transparent dispatcher: reading ledgers, surfacing inferred state and options, and never silently writing to core artifacts.

### 2. Define “backfill complete” as an explicit ledger checklist

- For artifact-first PM ecosystems, “backfill” is only complete when **all** relevant ledgers are populated:
  - Trigger Log is chronologically readable and linked to evidence/decisions.
  - Deliverable Map covers high-leverage deliverables and links to triggers and anchors.
  - Submission Log includes external submissions **and** internal freezes/cutoffs.
  - Claim Register captures reusable claims that justify decisions and sponsor narratives.
  - Change Log captures major direction shifts in plain language.
- If only some ledgers are populated, name that state explicitly (“spine backfilled” vs “ledgers backfilled”) instead of claiming the entire system is up to date.

### 3. Encode execution spines across all ledgers

- When a planning artifact defines a **three-stream execution spine** (e.g. “IT discussion → consultation workshop → FGD3”), materialise it consistently across:
  - Trigger Log (where the spine is adopted and linked to evidence),
  - Change Log (what changed in direction and why),
  - Deliverable Map (the plan or spine note as a first-class deliverable with dependencies),
  - Claim Register (a reusable claim summarising the rationale).
- This keeps the execution spine aligned with interim report narratives and TOR interpretations, and preserves both events *and* reasoning.

### 4. Keep PM maintenance event-scoped

- Instead of “fix everything” passes, choose one concrete event (e.g. a specific workshop or submission) and run a full maintenance cycle:
  - state-sensing → update Trigger/Deliverable/Claim/Submission/Change as needed → refresh one executable artifact.
- This avoids scope creep into high-agency automation and keeps each maintenance run inspectable and reversible.

### 5. Use test branches for structural PM changes

- When introducing or refactoring PM ledgers or facades, perform changes on a dedicated test branch (e.g. `test/project-management-ecosystem`).
- Merge only after the schema and contracts have been exercised with real data and reviewed.

## One-off decisions and local choices

- CRDB-specific ledger filenames and IDs (e.g. `T-015`, `D-020`, `C-011`) are examples; other projects should reuse the pattern, not these identifiers.
- The `test/project-management-ecosystem` branch name is illustrative; any clearly scoped test branch name is acceptable as long as it is treated as a staging area for structural PM work.

## Open questions / future refinement

- Clarify how PM-ledger patterns should appear in Oracle DB search results (e.g. tag taxonomy for `pm-ledgers`, `execution-spine`, `backfill`).
- Decide what minimum ledger coverage is required before a project is considered “Oracle-ready” for PM patterns (e.g. at least Trigger/Deliverable/Change in sync).

## Relationship to Oracle DB backfill

- This note is the **Phase 2.2 canonical** for PM ledger and execution-spine patterns.
- Future Oracle DB backfill should:
  - use this file as the primary PM-ledger pattern entry,
  - reference CRDB-specific learnings as provenance/examples from this canonical,
  - log the Oracle ID for this pattern under `Source type = learning` in [`ψ/memory/logs/info/backfill-index.md`](ψ/memory/logs/info/backfill-index.md).


---
*Added via Oracle Learn*
