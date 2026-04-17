# CRDB Project History Timeline (staging)

## Purpose

This file is a **neutral, chronological staging timeline** used to reconstruct CRDB project history *before* backfilling the canonical project-management ledgers.

It is intentionally:

- **append-only** (new rows; do not delete),
- **link-first** (always link to source artifacts; do not rewrite content),
- **ledger-feeding** (each event points to the Trigger/Change/Submission/Deliverable/Claim ledgers where applicable).

Canonical ledgers (targets):

- [`ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md)
- [`ψ/incubate/DCCE/CRDB/CRDB-Change-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Change-Log.md)
- [`ψ/incubate/DCCE/CRDB/CRDB-Submission-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Submission-Log.md)
- [`ψ/incubate/DCCE/CRDB/CRDB-Deliverable-Map.md`](ψ/incubate/DCCE/CRDB/CRDB-Deliverable-Map.md)
- [`ψ/incubate/DCCE/CRDB/CRDB-Claim-Register.md`](ψ/incubate/DCCE/CRDB/CRDB-Claim-Register.md)

Orientation anchors:

- [`ψ/incubate/DCCE/CRDB/Hub.md`](ψ/incubate/DCCE/CRDB/archive/Hub.md)
- [`ψ/incubate/DCCE/CRDB/plan.md`](ψ/incubate/DCCE/CRDB/plan.md)

## How to use

1) Add an event here first.
2) If the event corresponds to a trigger, change, submission, deliverable, or claim, then:
   - create/update the relevant ledger entry (T-*, CH-*, S-*, D-*, C-*), and
   - reference that ID back in this timeline row.

## Shared event schema (fields)

| Field | Meaning |
|---|---|
| `event_id` | Timeline-only ID (H-*) used for chronological reconstruction |
| `date` | `YYYY-MM-DD` (ICT unless stated) |
| `phase` | One of the canonical phases below |
| `event_type` | `decision` / `meeting` / `trigger_logged` / `submission` / `deliverable_created` / `change_logged` / `pm_system_update` / `workshop_stream` |
| `workstreams` | Comma-separated: `Interim_Report`, `Governance`, `NCAIF`, `CDM`, `Workshop`, `PM_Ecosystem`, `Architecture` |
| `summary` | One-line description |
| `primary_sources` | Links to the most authoritative artifacts for the event |
| `ledger_refs` | Links/IDs into T-*, CH-*, S-*, D-*, C-* where applicable |
| `status` | `logged` / `open` / `in_progress` / `superseded` |
| `notes` | Anything needed for later backfill |

## Canonical phases

1) Inception and TOR grounding
2) CDM and NCAIF framing
3) FGD1/FGD2 preparation and execution
4) Interim report v1–v3 drafting cycle
5) Interim submission and post-submission edits
6) Progress meetings and sponsor decisions
7) Late-April workshop stream
8) PM ecosystem and facade build-out

---

## Timeline — Pass 1 (anchors only)

### Phase 2 — CDM and NCAIF framing

| event_id | date | phase | event_type | workstreams | summary | primary_sources | ledger_refs | status | notes |
|---|---|---|---|---|---|---|---|---|---|
| H-008 | 2025-12-08 | 2 | deliverable_created | Governance, Architecture | TOR translation/restructure captured as a stable constraint reference (scope, deliverables, meetings). | [`ψ/incubate/DCCE/CRDB/inbox_source/CRDB - TOR.md`](ψ/incubate/DCCE/CRDB/inbox_source/CRDB%20-%20TOR.md) | T-006 | logged | Use as authoritative clause anchor when debating “in scope/out of scope.” |
| H-009 | 2026-01-05 | 2 | deliverable_created | NCAIF, Architecture | NCAIF framework established as the organizing “front door” structure (early anchor). | [`ψ/incubate/DCCE/CRDB/output/National Climate Adaptation Information Framework.md`](ψ/incubate/DCCE/CRDB/output/National%20Climate%20Adaptation%20Information%20Framework.md) | T-008, E-003 | logged | Later sitemap decisions should reference this as the early direction anchor. |
| H-010 | 2026-01-06 | 2 | deliverable_created | Governance, Architecture | Inception report grounds the early project shape: NCAIF framing, governance emphasis, and internal FGD cadence proposed. | [`ψ/incubate/DCCE/CRDB/inbox_source/260106_DCCE_Climate risk database_inception report_vfinal.pdf`](ψ/incubate/DCCE/CRDB/inbox_source/260106_DCCE_Climate%20risk%20database_inception%20report_vfinal.pdf), [`ψ/incubate/DCCE/CRDB/inbox_source/260106_DCCE_Climate risk database_inception report_vfinal.md`](ψ/incubate/DCCE/CRDB/inbox_source/260106_DCCE_Climate%20risk%20database_inception%20report_vfinal.md) | T-007 | logged | Includes proposed internal focus groups (first window: 2026-01-19..23). |
| H-011 | 2026-01-09 | 2 | deliverable_created | CDM, Architecture | CDM anchor created as cross-cutting conceptual structure for interoperability and later “catalog-first/link-first” stance. | [`ψ/incubate/DCCE/CRDB/output/Conceptual Data Model for climate risk and adaptation data system.md`](ψ/incubate/DCCE/CRDB/output/Conceptual%20Data%20Model%20for%20climate%20risk%20and%20adaptation%20data%20system.md) | T-009, E-002 | logged | Serves as the conceptual glue for later linking hazards/exposure/vulnerability/impacts/adaptation across agencies. |

### Phase 3 — FGD1/FGD2 preparation and execution

| event_id | date | phase | event_type | workstreams | summary | primary_sources | ledger_refs | status | notes |
|---|---|---|---|---|---|---|---|---|---|
| H-012 | 2026-02-26 | 3 | deliverable_created | Governance, NCAIF | FGD2 decision pack + governance strategy revision created (Phase 1 practicality framing). | [`ψ/inbox/handoff/2026-02-26_14-19_ncaif-fgd2-handoff-2026-02-26.md`](ψ/inbox/handoff/2026-02-26_14-19_ncaif-fgd2-handoff-2026-02-26.md), [`ψ/memory/retrospectives/2026-02/26/14.10_ncaif-refinement-and-fgd2-plan.md`](ψ/memory/retrospectives/2026-02/26/14.10_ncaif-refinement-and-fgd2-plan.md) | T-010 | logged | Governance reframed as “safe publishing prerequisites” for Phase 1 flagship products; decision prompts D1–D5. |
| H-013 | 2026-03-09 | 3 | decision | NCAIF, Governance, Architecture | MVP v3 framing aligned (workflow patterns vs MVPs) and MVP-2 reframed as DDPM→DCCE ingestion + L&D groundwork. | [`ψ/inbox/handoff/2026-03-09_22-31_forward-dcce-crdb-mvp-v3-alignment.md`](ψ/inbox/handoff/2026-03-09_22-31_forward-dcce-crdb-mvp-v3-alignment.md) | T-014 | logged | Feeds directly into the confirmed Phase 1 decision log (2026-03-10 confirmation). |
| H-014 | 2026-03-11 | 3 | meeting | Governance, NCAIF, Workshop | FGD2 captured as action summary + minutes/transcript; becomes the canonical “what stakeholders asked for” anchor. | [`ψ/incubate/DCCE/CRDB/inbox_source/2026-03-11_FGD2_action_summary.md`](ψ/incubate/DCCE/CRDB/inbox_source/2026-03-11_FGD2_action_summary.md), [`ψ/incubate/DCCE/CRDB/inbox_source/2026-03-11-FGD2-Meeting-Minute.md`](ψ/incubate/DCCE/CRDB/inbox_source/2026-03-11-FGD2-Meeting-Minute.md), [`ψ/incubate/DCCE/CRDB/inbox_source/2026-03-11_FGD2_transcript_clean.md`](ψ/incubate/DCCE/CRDB/inbox_source/2026-03-11_FGD2_transcript_clean.md) | T-011, E-016 | logged | Later: extract explicit “decision candidates” into CH rows once confirmed. |

### Phase 4 — Interim report v1–v3 drafting cycle

| event_id | date | phase | event_type | workstreams | summary | primary_sources | ledger_refs | status | notes |
|---|---|---|---|---|---|---|---|---|---|
| H-015 | 2026-03-12 | 4 | deliverable_created | Interim_Report, Architecture | Interim report drafting baseline stabilized (evidence-linked) with a writing plan + CDM/MVP rationale. | [`ψ/inbox/handoff/2026-03-12_17-47_crdb-interim-report-drafting-handoff.md`](ψ/inbox/handoff/2026-03-12_17-47_crdb-interim-report-drafting-handoff.md), [`ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim Report Writing Plan.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim%20Report%20Writing%20Plan.md), [`ψ/incubate/DCCE/CRDB/output/2026-03-12_crdb-section1-cdm-mvp-evidence-analysis.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12_crdb-section1-cdm-mvp-evidence-analysis.md) | T-012, E-004 | logged | Repositions CDM as hidden organizing logic and MVPs as bounded Phase 1 expressions. |
| H-016 | 2026-03-18 | 4 | decision | Interim_Report | Interim report drafting cutoff for 23-Mar deadline: ship as-is, carry known rough edges into late-April workshop stream. | [`ψ/inbox/handoff/2026-03-18_02-03_crdb-interim-report-23mar-submission-wrap.md`](ψ/inbox/handoff/2026-03-18_02-03_crdb-interim-report-23mar-submission-wrap.md) | T-013 | logged | Use as “why deferred” anchor when later improving narrative or evidence packaging. |

### Phase 5 — Interim submission and post-submission edits

| event_id | date | phase | event_type | workstreams | summary | primary_sources | ledger_refs | status | notes |
|---|---|---|---|---|---|---|---|---|---|
| H-001 | 2026-03-27 | 5 | submission | Interim_Report | Interim report edited snapshot submitted (freeze point created). | [`ψ/incubate/DCCE/CRDB/inbox_source/2026-03-27-CRDB-interim-report-v3-edited.md`](ψ/incubate/DCCE/CRDB/inbox_source/2026-03-27-CRDB-interim-report-v3-edited.md), [`ψ/incubate/DCCE/CRDB/plan.md`](ψ/incubate/DCCE/CRDB/plan.md) | S-001, D-002, T-003 | logged | Later: diff/compare vs working drafts and record deltas as change events. |

### Phase 6 — Progress meetings and sponsor decisions

| event_id | date | phase | event_type | workstreams | summary | primary_sources | ledger_refs | status | notes |
|---|---|---|---|---|---|---|---|---|---|
| H-002 | 2026-03-24 | 6 | decision | Governance, Architecture, Interim_Report | Internal progress-meeting decision synthesis produced (stance used to position sponsor meeting). | [`ψ/incubate/DCCE/CRDB/output/2026-03-24_CRDB-Progress-Meeting-Decisions.md`](ψ/incubate/DCCE/CRDB/output/2026-03-24_CRDB-Progress-Meeting-Decisions.md), [`ψ/incubate/DCCE/CRDB/plan.md`](ψ/incubate/DCCE/CRDB/plan.md) | T-001, CH-001 | logged | Treat as “pre-meeting stance” artifact; distinct from sponsor outcomes. |
| H-003 | 2026-03-27 | 6 | meeting | Governance, Workshop, Architecture | Sponsor progress meeting (Dir Toey) captured as verbatim/human summary; becomes canonical outcome anchor. | [`ψ/incubate/DCCE/CRDB/output/2026-03-27_progress-meeting-summary_dir-toey.md`](ψ/incubate/DCCE/CRDB/output/2026-03-27_progress-meeting-summary_dir-toey.md), [`ψ/incubate/DCCE/CRDB/Hub.md`](ψ/incubate/DCCE/CRDB/archive/Hub.md) | T-004 | open | Later: extract explicit “decision candidates” into CH rows once confirmed. |
| H-004 | 2026-03-27 | 6 | trigger_logged | Governance | Sponsor context watchpoints logged: DCCE org restructure + Digital Tech consultant scope uncertainty. | [`ψ/memory/logs/info/2026-03-27_09-24_dcce-org-restructure-cdm-data-governance-must-align.md`](ψ/memory/logs/info/2026-03-27_09-24_dcce-org-restructure-cdm-data-governance-must-align.md), [`ψ/memory/logs/info/2026-03-27_09-22_dcce-digital-tech-group-consultant-scope-unclear.md`](ψ/memory/logs/info/2026-03-27_09-22_dcce-digital-tech-group-consultant-scope-unclear.md) | T-002 | open | Later: translate into concrete governance role-mapping deliverable (D-004). |

### Phase 7 — Late-April workshop stream

| event_id | date | phase | event_type | workstreams | summary | primary_sources | ledger_refs | status | notes |
|---|---|---|---|---|---|---|---|---|---|
| H-005 | 2026-03-27 | 7 | workshop_stream | Workshop | “Bridge / baton pass” workshop strategy note recorded to shape April 30 design. | [`ψ/incubate/DCCE/CRDB/inbox_source/2026-03-27-my-idea-about-April-workshop.md`](ψ/incubate/DCCE/CRDB/inbox_source/2026-03-27-my-idea-about-April-workshop.md), [`ψ/incubate/DCCE/CRDB/plan.md`](ψ/incubate/DCCE/CRDB/plan.md) | T-005, C-005, D-006 | open | Later: convert into an actionable workshop package deliverable (D-006) and change-log entry if it materially shifts direction. |

### Phase 8 — PM ecosystem and facade build-out

| event_id | date | phase | event_type | workstreams | summary | primary_sources | ledger_refs | status | notes |
|---|---|---|---|---|---|---|---|---|---|
| H-006 | 2026-03-27 | 8 | pm_system_update | PM_Ecosystem | PM ecosystem ledgers + facade contract created and anchored in plan. | [`ψ/inbox/handoff/2026-03-27_13-12_crdb-project-management-ecosystem-test-session.md`](ψ/inbox/handoff/2026-03-27_13-12_crdb-project-management-ecosystem-test-session.md), [`ψ/incubate/DCCE/CRDB/plan.md`](ψ/incubate/DCCE/CRDB/plan.md) | CH-002, D-003, D-005 | logged | Note: handoff lists ledgers “under output” but canonical paths are currently under `ψ/incubate/DCCE/CRDB/`. Keep canonical; fix references later if needed. |
| H-007 | 2026-03-27 | 8 | pm_system_update | PM_Ecosystem | Handoff created to test the PM ecosystem with a manual facade pass. | [`ψ/inbox/handoff/2026-03-27_13-12_crdb-project-management-ecosystem-test-session.md`](ψ/inbox/handoff/2026-03-27_13-12_crdb-project-management-ecosystem-test-session.md) | (handoff) | logged | This is a coordination event; may later become a trigger if it changes priorities. |

---

## Backfill queue (not yet encoded)

These are known streams/milestones that should become timeline rows in later passes.

### Phase 3 — FGD1/FGD2

- FGD2 action summary + transcript + meeting minutes (see references in [`ψ/incubate/DCCE/CRDB/plan.md`](ψ/incubate/DCCE/CRDB/plan.md)).

### Phase 4 — Interim report drafting cycle

- Writing plan anchor: [`ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim Report Writing Plan.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim%20Report%20Writing%20Plan.md)
- Draft progression under [`ψ/incubate/DCCE/CRDB/output/`](ψ/incubate/DCCE/CRDB/output/)
- Submission wrap milestone (23-Mar): [`ψ/inbox/handoff/2026-03-18_02-03_crdb-interim-report-23mar-submission-wrap.md`](ψ/inbox/handoff/2026-03-18_02-03_crdb-interim-report-23mar-submission-wrap.md)

### Phase 2 — CDM and NCAIF framing

- CDM and NCAIF anchor artifacts (see [`ψ/incubate/DCCE/CRDB/Hub.md`](ψ/incubate/DCCE/CRDB/archive/Hub.md)).
