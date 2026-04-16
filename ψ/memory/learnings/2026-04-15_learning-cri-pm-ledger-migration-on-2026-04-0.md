---
title: # Learning — CRI PM Ledger Migration
tags: []
created: 2026-04-15
source: ψ/memory/learnings/2026-04-02_cri-pm-ledger-migration.md
---

# # Learning — CRI PM Ledger Migration

# Learning — CRI PM Ledger Migration

On 2026-04-02 we migrated the CRI project from an evidence-spine-only setup into a full ledger-based project-management ecosystem parallel to CRDB. The key pattern was to treat the ledgers (triggers, deliverables, claims, submissions, changes) plus the evidence registry as the canonical project state, and to demote the hub and plan into navigation and operating surfaces rather than state stores.

Three concrete lessons emerged:

1. **Ledger-first requires artifact-first.** The ledgers only became trustworthy once every row was grounded in real artifacts: Public Hearing 1 transcripts and notes, hypothesis memos, and SES-framing notes. Designing the structure without tying it to actual files would have produced a beautiful but hollow system.
2. **Selective backfill beats exhaustive reconstruction.** Instead of trying to encode every CRI note as a trigger or change, we chose a small number of pivots that clearly changed direction (Phase 1/2 interface, LAO incentives, SES framing). This kept the history legible and avoided false precision.
3. **Explicit uncertainty is a feature, not a flaw.** For submissions and some historical decisions, the evidence base is incomplete. Rather than inventing submission rows or overconfident links, we logged the absence of verified events and marked downstream fields as "to be linked". This preserves integrity while leaving space for future clarification.

This migration confirms that the CRDB-style PM ecosystem is portable: the same form can be applied to CRI with different content, as long as we stay disciplined about evidence, selective backfill, and explicit uncertainty.

---
*Added via Oracle Learn*
