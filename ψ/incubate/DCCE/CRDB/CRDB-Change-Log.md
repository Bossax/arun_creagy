# CRDB Change Log

## Purpose

This ledger records **human-readable summaries of major direction shifts** in the CRDB project: what changed, why, and what it affected. It complements the more granular trigger, decision, and submission ledgers.

It is designed to answer, in plain language:

- what changed,
- why it changed,
- who or what triggered it, and
- which artifacts and stances were affected.

## Usage and maintenance

- Add an entry when the **project direction, governance stance, or key deliverable trajectory** changes.
- Each entry should reference:
  - trigger(s) from [`CRDB-Trigger-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md)
  - decisions from [`phase1_decision_log.md`](ψ/incubate/DCCE/CRDB/output/phase1_decision_log.md)
  - deliverables from [`CRDB-Deliverable-Map.md`](ψ/incubate/DCCE/CRDB/CRDB-Deliverable-Map.md)
- Use **append-only** updates; do not delete historical change notes.
 - When reconstructing history, treat the neutral staging timeline as the chronological entry point: [`CRDB-Project-History-Timeline.md`](ψ/incubate/DCCE/CRDB/output/CRDB-Project-History-Timeline.md)

## Change log

| Change ID | Date | Change summary | Trigger(s) | Affected decisions | Affected deliverables | Impact description | Notes |
|---|---|---|---|---|---|---|---|
| CH-001 | 2026-03-24 | Locked Phase 1 stance around catalog-first architecture, workflow-pattern-first sitemap, and MVP-3 + MVP-2 as the core deliverables; clarified governance gates and endorsement approach. | T-001 | Phase 1 decisions as recorded in [`phase1_decision_log.md`](ψ/incubate/DCCE/CRDB/output/phase1_decision_log.md) | D-001 (management evidence pack), D-002 (interim report narrative), future governance notes (D-004) | Consolidated previous assumptions into a confirmed decision set, tightening scope and expectations for interim report drafting and governance design. | Acts as the main reference for "what changed at the March 24 progress meeting"; later changes should reference this entry when revisiting decisions. |
| CH-002 | 2026-03-27 | Created the first CRDB project-management anchors: trigger log, deliverable map, claim register, submission log, change log, project-management module specs, and a controlled facade contract. | T-001, T-002, T-003 | None new; these artifacts operationalize existing decisions without changing them. | D-003 (this deliverable map), D-005 (submission log), project-management module and facade specs | Shifted project-management practice from ad-hoc reasoning to explicit, artifact-centered ledgers, while preserving a low-agency, advisory posture for any automation. | This change introduces the scaffolding for Option B (controlled facade) without enabling autonomous orchestration. |

## Practical reading order

1. Review this file to understand **major phases and turning points**.
2. For each row:
   - inspect underlying triggers → [`CRDB-Trigger-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md)
   - confirm decision details → [`phase1_decision_log.md`](ψ/incubate/DCCE/CRDB/output/phase1_decision_log.md)
   - assess deliverable impact → [`CRDB-Deliverable-Map.md`](ψ/incubate/DCCE/CRDB/CRDB-Deliverable-Map.md)
