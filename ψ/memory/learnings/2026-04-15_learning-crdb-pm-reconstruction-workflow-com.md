---
title: # Learning — CRDB PM reconstruction + workflow compliance
tags: []
created: 2026-04-15
source: ψ/memory/learnings/2026-03-27_rrr-crdb-pm-history-spine-ledgers-and-compliance-gap.md
---

# # Learning — CRDB PM reconstruction + workflow compliance

# Learning — CRDB PM reconstruction + workflow compliance

## Pattern
When reconstructing a project’s history, use a **timeline-first staging surface** (neutral, chronological) and then backfill canonical ledgers in this order:
1) **Trigger Log** = history spine (must render correctly and sort chronologically)
2) **Deliverable Map** = artifacts implied/created by triggers
3) **Submission Log** = all freeze points (internal cutoffs) + formal submissions/snapshots

## Operational rules
- Spine surfaces must be **chronologically readable** even if IDs are not sequential.
- Keep “backfill notes” out of tables; keep tables strictly row data.
- Prefer evidence-first linking: reference Evidence Registry IDs when available.

## Reliability rule (process)
If the user invokes `/rrr`, complete the chain end-to-end:
- write retrospective → write learning → oracle sync → git add/commit.

This prevents “silent loss” of session meaning and aligns with “Nothing is Deleted”.

---
*Added via Oracle Learn*
