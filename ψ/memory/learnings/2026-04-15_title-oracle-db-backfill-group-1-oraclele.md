---
title: ---
tags: [oracle-db, oracle_learn, guardrail, durable-capture, workflow-integrity, backfill]
created: 2026-04-15
source: ψ/memory/learnings/2026-04-11_oracle-db-backfill-group1-oraclelearn-materialisation-guardrail.md
---

# ---

---
title: Oracle DB backfill — Group 1 `oracle_learn` materialisation guardrail
created: 2026-04-11
type: learning
concepts:
  - oracle-db
  - oracle_learn
  - guardrail
  - durable-capture
  - workflow-integrity
  - backfill
source: rrr: Arun_Creagy
---

# Oracle DB backfill — Group 1 `oracle_learn` materialisation guardrail

## Scope

This canonical learning represents **Group 1 – `oracle_learn` materialisation guardrail** from the indexing map in [`plans/2026-04-09-learnings-indexing-map.md`](plans/2026-04-09-learnings-indexing-map.md).

It consolidates the guardrail that **after every `oracle_learn()` call, the materialised markdown file must exist on disk and be treated as a first‑class artefact**. Any missing file (`ENOENT`) is treated as a serious integrity failure that must be corrected immediately.

## Source artefacts

Group 1 member files (from the indexing map):

- [`ψ/memory/learnings/2026-03-27_guardrail-after-every-oraclelearn-call-treat.md`](ψ/memory/learnings/2026-03-27_guardrail-after-every-oraclelearn-call-treat.md)
- [`ψ/memory/learnings/2026-03-27_oracle-learn-file-materialization-guardrail.md`](ψ/memory/learnings/2026-03-27_oracle-learn-file-materialization-guardrail.md)
- [`ψ/memory/learnings/2026-04-07_oracle-learn-file-sync-anomaly.md`](ψ/memory/learnings/2026-04-07_oracle-learn-file-sync-anomaly.md)
- [`ψ/memory/learnings/2026-04-09_guardrail-after-every-oraclelearn-call-immedi.md`](ψ/memory/learnings/2026-04-09_guardrail-after-every-oraclelearn-call-immedi.md) **(proposed primary)**

The narrative anchor for this canonical is the consolidated guardrail in the proposed primary note, with the earlier anomaly and guardrail notes retained as provenance and detailed incident records.

## Stable patterns

- Treat the `file` / `source_file` path returned by `oracle_learn()` as a **claim that must be verified** in the filesystem.
- Immediately after each `oracle_learn()` call, check that the referenced markdown file exists at the expected path under the vault (`ψ/…`).
- If the file is missing (for example a read returns `ENOENT`), treat this as a **serious workflow integrity failure** because it breaks durable capture and creates false confidence in non‑existent artefacts.
- On missing file:
  - Immediately materialise the learning markdown at the exact path with the learning content.
  - Commit the file to Git in the next human‑driven commit.
  - Log the incident as a reliability issue, so that future investigations can track environment or MCP bugs.
- Assume that in the hybrid Windows + Docker + Git Bash environment, `oracle_learn()` may succeed in Oracle’s internal DB while failing to create a Git‑visible file unless this explicit check‑and‑create discipline is enforced.

## One-off decisions

- `oracle_learn()` is treated as **DB‑first**: the DB record may exist even if the markdown file does not. The guardrail is responsible for re‑materialising missing files and keeping the Git view consistent.
- ENOENT after `oracle_learn()` is treated as a **red‑flag incident**, not a recoverable edge case to be silently ignored.
- The canonical path for the guardrail learning lives under [`ψ/memory/learnings`](ψ/memory/learnings) with a 2026‑04‑11 date stamp to align with the Oracle DB backfill wave.

## Open questions

- How much of this guardrail can be automated inside the MCP server (for example, post‑`oracle_learn()` hooks) versus enforced as a client‑side discipline in skills and workflows?
- Should ENOENT incidents be tracked in a dedicated reliability log (for example under [`ψ/memory/logs`](ψ/memory/logs)) with their own patterns and metrics?
- Do we need additional integrity checks that cross‑reference Oracle DB entries against the filesystem on a scheduled basis?

## Relationship to Oracle DB backfill

- This canonical note is the **single source of truth** for the `oracle_learn` materialisation guardrail in Oracle DB.
- Earlier notes remain in the filesystem as provenance and detailed incident records but should be treated as **superseded** learnings once this canonical is backfilled.
- Oracle DB backfill should:
  - Create or confirm a single `learning` entry keyed to this canonical file.
  - Tag the entry with concepts: `oracle-db`, `oracle_learn`, `guardrail`, `durable-capture`, `workflow-integrity`, `backfill`.
  - Record the resulting Oracle ID in [`ψ/memory/logs/info/backfill-index.md`](ψ/memory/logs/info/backfill-index.md) under *Group 1 canonical backfill*.


---
*Added via Oracle Learn*
