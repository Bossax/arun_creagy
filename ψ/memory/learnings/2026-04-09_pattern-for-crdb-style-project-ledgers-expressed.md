---
title: Pattern: For CRDB-style project ledgers expressed as Markdown tables (Evidence R
tags: [markdown, table-editing, project-management, ledgers, evidence-trigger-change, crdb, thaiwater, architecture]
created: 2026-04-09
source: rrr: Arun_Creagy
project: github.com/sitth/oracle-arun-creagy
---

# Pattern: For CRDB-style project ledgers expressed as Markdown tables (Evidence R

Pattern: For CRDB-style project ledgers expressed as Markdown tables (Evidence Registry, Trigger Log, Change Log, Deliverable Map), treat table editing as an architectural concern, not a one-off patching problem. Always follow Evidence → Trigger → Change ordering, and always use deterministic block-level table replacement instead of line-based diffs.

Key points:
- Evidence-first: register new benchmark artifacts/notes as E-ids in the Evidence Registry; demote old decision logs to historical/retired when they no longer represent live stance.
- Trigger-after-evidence: add T-ids in the Trigger Log that tie E-ids to concrete impact zones and future D-* deliverables; make supersession of old anchors explicit.
- Change-after-trigger: only create CH-ids in the Change Log once design commitments and D-* deliverables exist; link CH-ids back to T-ids and D-ids.
- Table editing: never use apply_patch or line-level diffs on core PM tables. Use a markdown-table-edit skill + deterministic script (e.g. replace-md-table.ts) or full-file write to replace the entire table block under a heading anchor.

Benefits:
- Prevents subtle table corruption and patch failures.
- Keeps PM stance explicit and layered (evidence, triggers, changes, deliverables).
- Ensures historical decision logs remain traceable but do not silently govern current work.


---
*Added via Oracle Learn*
