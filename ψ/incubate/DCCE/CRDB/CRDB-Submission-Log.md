# CRDB Submission Log

## Purpose

This ledger records **external submissions and key internal freeze points** for CRDB deliverables. It implements the "submission creates a freeze point" rule from [`plans/2026-03-27-crdb-oracle-project-work-cycle-architecture-plan.md`](plans/2026-03-27-crdb-oracle-project-work-cycle-architecture-plan.md).

## Usage and maintenance

- Add one row **per submission or freeze event**.
- Treat the **Submission ID** as the canonical handle when referring to a specific sent or frozen state.
- Prefer sorting the table **by Date (ascending)** for historical reconstruction. Submission IDs may therefore appear out of numeric order if earlier IDs were already referenced elsewhere.
- Use this file together with:
  - [`CRDB-Deliverable-Map.md`](ψ/incubate/DCCE/CRDB/CRDB-Deliverable-Map.md) for deliverable context
  - [`CRDB-Trigger-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md) for the trigger that led to submission or revision
  - [`CRDB-Change-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Change-Log.md) for narrative about direction changes
  - the neutral staging timeline for reconstruction/backfill: [`CRDB-Project-History-Timeline.md`](ψ/incubate/DCCE/CRDB/archive/CRDB-Project-History-Timeline.md)

## Submission table

| Submission ID | Date | Channel / recipient | Deliverable ID | Submitted artifact | Version label | Trigger(s) | Decision basis | Evidence basis | Notes |
|---|---|---|---|---|---|---|---|---|---|
| S-004 | 2026-01-07 | Internal freeze (submitted-by-claim; no preserved send artifact) | D-008 | [`260106_DCCE_Climate risk database_inception report_vfinal.pdf`](ψ/incubate/DCCE/CRDB/inbox_source/260106_DCCE_Climate%20risk%20database_inception%20report_vfinal.pdf) (plus MD mirror) | Inception report vfinal (frozen snapshot) | T-006, T-007 | Deliverable schedule in [`CRDB - TOR.md`](ψ/incubate/DCCE/CRDB/inbox_source/CRDB%20-%20TOR.md); project plan milestone in [`CRDB - Implementation Plan.md`](ψ/incubate/DCCE/CRDB/output/CRDB%20-%20Implementation%20Plan.md) | Repo statements asserting submission/approval: [`CRDB - Work Status Brief.md`](ψ/incubate/DCCE/CRDB/archive/CRDB%20-%20Work%20Status%20Brief.md); timeline anchoring: [`CRDB-Project-History-Timeline.md`](ψ/incubate/DCCE/CRDB/archive/CRDB-Project-History-Timeline.md) | Logged to preserve an auditable Jan-7 inception freeze point, but explicitly marked as **inferred from in-repo statements** (still evidence-backed) rather than a preserved submission package (email/cover note). |
| S-003 | 2026-03-18 | Internal (drafting cutoff / freeze point) | D-014 | [`2026-03-18_02-03_crdb-interim-report-23mar-submission-wrap.md`](ψ/inbox/handoff/2026-03-18_02-03_crdb-interim-report-23mar-submission-wrap.md) | Drafting cutoff for 23-Mar cycle | T-013 | Interim report writing baseline in [`2026-03-12-Interim Report Writing Plan.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim%20Report%20Writing%20Plan.md); Phase 1 stance in [`phase1_decision_log.md`](ψ/incubate/DCCE/CRDB/archive/phase1_decision_log.md) | Working draft set referenced in the handoff (Chapter 3, appendices, interviews, FGD summary) | Creates an internal “ship-as-is” boundary: the 23-Mar submission package is prepared without reopening major structural rewriting. |
| S-002 | 2026-03-23 | DCCE (interim report submission package — first submission snapshot) | D-002 (see Notes) | [`2026-03-23_interim-report-1st-submission.md`](ψ/incubate/DCCE/CRDB/inbox_source/2026-03-23_interim-report-1st-submission.md) | Interim report (23-Mar first submission snapshot) | T-013, T-012 | Interim report writing baseline in [`2026-03-12-Interim Report Writing Plan.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim%20Report%20Writing%20Plan.md); Phase 1 stance in [`phase1_decision_log.md`](ψ/incubate/DCCE/CRDB/archive/phase1_decision_log.md) | Interim report snapshot artifact itself (plus its embedded references) | This is the **23-Mar** snapshot referenced by the cutoff handoff. The deliverable map currently tracks the **27-Mar** submitted snapshot as D-002; add a separate deliverable ID for the 23-Mar snapshot later if you want clean one-to-one mapping. |
| S-001 | 2026-03-27 | DCCE (formal interim report submission) | D-002 | [`2026-03-27-CRDB-interim-report-v3-edited.md`](ψ/incubate/DCCE/CRDB/inbox_source/2026-03-27-CRDB-interim-report-v3-edited.md) | Interim report v3 (edited snapshot) | T-001, T-003 | Phase 1 decisions in [`phase1_decision_log.md`](ψ/incubate/DCCE/CRDB/archive/phase1_decision_log.md); progress-meeting stance in [`2026-03-24_CRDB-Progress-Meeting-Decisions.md`](ψ/incubate/DCCE/CRDB/output/2026-03-24_CRDB-Progress-Meeting-Decisions.md) | E-004, E-008, E-011, E-020, E-021, E-022 | Creates the canonical freeze point for later diff/compare tasks and for aligning future narrative revisions. |

## Practical reading order

1. Scan this file to understand **what was submitted when**.
2. Follow **Deliverable ID** to [`CRDB-Deliverable-Map.md`](ψ/incubate/DCCE/CRDB/CRDB-Deliverable-Map.md).
3. Follow **Trigger(s)** to [`CRDB-Trigger-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md).
4. Use **Decision basis** and **Evidence basis** links for audit and explanation.
