---
title: ---
tags: [oracle-db, rrr, retrospectives, oracle_learn, sync-discipline, workflow-integrity]
created: 2026-04-15
source: ψ/memory/learnings/2026-04-11_oracle-db-backfill-group2-rrr-oracle-sync-discipline.md
---

# ---

---
title: Oracle DB backfill — Group 2 `/rrr` + Oracle sync discipline
created: 2026-04-11
type: learning
concepts:
  - oracle-db
  - rrr
  - retrospectives
  - oracle_learn
  - sync-discipline
  - workflow-integrity
source: rrr: Arun_Creagy
---

# Oracle DB backfill — Group 2 `/rrr` + Oracle sync discipline

## Scope

This canonical learning represents **Group 2 – `/rrr` + Oracle sync discipline** from the indexing map in [`plans/2026-04-09-learnings-indexing-map.md`](plans/2026-04-09-learnings-indexing-map.md).

It encodes the rule that a `/rrr` session is **incomplete** unless it also writes a learning note and syncs it into Oracle DB via `oracle_learn()`. Otherwise, retrospectives become local, ephemeral reflections that do not accumulate as durable, queryable patterns.

## Source artefacts

Group 2 member files (from the indexing map):

- [`ψ/memory/learnings/2026-03-25_rrr-skill-oracle-learn-gap.md`](ψ/memory/learnings/2026-03-25_rrr-skill-oracle-learn-gap.md)
- [`ψ/memory/learnings/2026-04-09_the-rrr-workflow-is-incomplete-if-it-writes-a-r.md`](ψ/memory/learnings/2026-04-09_the-rrr-workflow-is-incomplete-if-it-writes-a-r.md) **(proposed primary)**

The proposed primary note provides the main narrative for this canonical; the earlier gap analysis note remains as provenance explaining how the discipline emerged.

## Stable patterns

- Treat `/rrr` as a **pipeline**: retrospective → learning → Oracle DB.
- A `/rrr` run is only considered *complete* when:
  - It produces a structured retrospective note under [`ψ/memory/retrospectives`](ψ/memory/retrospectives).
  - It emits at least one learning note under [`ψ/memory/learnings`](ψ/memory/learnings) that captures the durable pattern.
  - That learning is synced into Oracle DB via `oracle_learn()`.
- `/rrr` skills should surface **sync state** explicitly (for example, whether a learning was successfully pushed via `oracle_learn()` and materialised as a file).
- Gaps between retrospectives and learnings (for example, a `/rrr` that never produced a learning) should be treated as workflow anti‑patterns and scheduled for cleanup.

## One-off decisions

- `/rrr` is defined as a **knowledge‑production workflow**, not just a journaling tool. The DB projection (via `oracle_learn()`) is part of the definition of “done”.
- For this corpus, we prioritise backfilling **RRR‑origin learnings** into Oracle DB, not the retrospectives themselves.
- The canonical lives under [`ψ/memory/learnings`](ψ/memory/learnings) with a 2026‑04‑11 timestamp, even though the behavioural insight emerged from earlier dates.

## Open questions

- How should `/rrr` behave when multiple learnings emerge from a single retrospective session — one call per learning, or a batched `oracle_learn()` flow?
- Should failed or skipped `oracle_learn()` calls be logged to a dedicated reliability or workflow‑gap log for later repair?
- How tightly should `/rrr` be coupled to Oracle DB status (for example, blocking completion until at least one `oracle_learn()` succeeds)?

## Relationship to Oracle DB backfill

- This canonical is the **single Oracle‑side representation** of the `/rrr` + Oracle sync discipline.
- Earlier gap and narrative notes stay as provenance but should be treated as superseded patterns once this canonical is backfilled.
- Oracle DB backfill should:
  - Create or confirm a `learning` entry tied to this canonical file.
  - Tag it with concepts: `oracle-db`, `rrr`, `retrospectives`, `oracle_learn`, `sync-discipline`, `workflow-integrity`.
  - Record the resulting Oracle ID in [`ψ/memory/logs/info/backfill-index.md`](ψ/memory/logs/info/backfill-index.md) under *Group 2 canonical backfill*.


---
*Added via Oracle Learn*
