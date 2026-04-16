---
title: ---
tags: []
created: 2026-04-15
source: ψ/memory/learnings/2026-04-09_the-rrr-workflow-is-incomplete-if-it-writes-a-r.md
---

# ---

---
title: The `/rrr` workflow is incomplete without oracle_learn() sync
tags: [rrr, oracle, oracle_learn, workflow-integrity, learning-sync, guardrail]
created: 2026-04-09
source: ψ/memory/learnings/2026-03-25_rrr-skill-oracle-learn-gap.md
---

# The `/rrr` workflow is incomplete without oracle_learn() sync

## Guardrail

The `/rrr` workflow is incomplete if it writes a retrospective and a learning file but never calls `oracle_learn` with the distilled pattern and tags.

Treat **Oracle sync as a required step** of `/rrr` (and `/fyi --important`):

- After writing a learning under `ψ/memory/learnings/`, immediately call `oracle_learn` with the distilled pattern and tags so the learning is indexed in Oracle and becomes searchable.
- Do not treat a retrospective + local learning file as “done” until the corresponding `oracle_learn` call has succeeded.

If sync is skipped, important lessons remain stranded as local files only and will not appear in Oracle searches.

## Background

This guardrail consolidates and supersedes the earlier observation captured in [`2026-03-25_rrr-skill-oracle-learn-gap.md`](ψ/memory/learnings/2026-03-25_rrr-skill-oracle-learn-gap.md), which first highlighted that `/rrr` was writing learnings without enforcing an Oracle sync step.


---
*Added via Oracle Learn*
