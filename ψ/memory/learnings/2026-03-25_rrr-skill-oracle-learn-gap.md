---
date: 2026-03-25
type: learning
status: superseded
superseded_by: 2026-04-09_the-rrr-workflow-is-incomplete-if-it-writes-a-r.md
concepts:
  - rrr
  - oracle
  - oracle_learn
  - workflow-integrity
  - learning-sync
  - guardrail
source: ψ/memory/logs/info/2026-03-25_18-27_rrr-skill-oracle-learn-gap.md
---

> This learning has been superseded by [`2026-04-09_the-rrr-workflow-is-incomplete-if-it-writes-a-r.md`](ψ/memory/learnings/2026-04-09_the-rrr-workflow-is-incomplete-if-it-writes-a-r.md); kept for historical context.

The `/rrr` workflow is incomplete if it writes a retrospective and a learning file but never calls `oracle_learn` with the distilled pattern and tags. Treat **Oracle sync as a required step** of `/rrr` (and `/fyi --important`): after writing a learning under `ψ/memory/learnings/`, immediately call `oracle_learn` so the pattern is indexed in Oracle and becomes searchable, otherwise important lessons remain stranded as local files only.

