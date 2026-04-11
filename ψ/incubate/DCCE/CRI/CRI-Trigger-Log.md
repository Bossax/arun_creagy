# CRI Trigger Log

## Purpose

This ledger records **project-relevant triggers** that cause the CRI project to reconsider direction, priorities, methodology, or implementation posture. It mirrors the trigger-layer pattern from [`ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md) but is scoped specifically to **DCCE / CRI**.

Use this as the **canonical index of why something changed** for CRI.

## Usage and maintenance

- Append new rows; do **not** delete old entries.
- Prefer **one row per meaningful trigger**, even if several artifacts or conversations are involved.
- When a trigger is fully processed, update the **Status** field instead of editing the description.
- Link to:
  - evidence via [`output/CRI-Evidence-Registry.md`](ψ/incubate/DCCE/CRI/CRI-Evidence-Registry.md) and the coverage map [`output/CRI-Evidence-Coverage-Map.md`](ψ/incubate/DCCE/CRI/CRI-Evidence-Coverage-Map.md)
  - decisions and stances in CRI decision / design notes (to be anchored in later steps)
  - deliverables via the CRI deliverable map: [`CRI-Deliverable-Map.md`](ψ/incubate/DCCE/CRI/CRI-Deliverable-Map.md)
  - any neutral staging timeline for CRI, when introduced later in the migration


## Practical reading order

1. Scan the **latest rows** (bottom of table) to see what has recently shifted for CRI.
2. Follow links into evidence via [`output/CRI-Evidence-Registry.md`](ψ/incubate/DCCE/CRI/CRI-Evidence-Registry.md) and the coverage map.
3. Review affected decisions in CRI decision / design notes (once established).
4. Check downstream impact on deliverables in [`CRI-Deliverable-Map.md`](ψ/incubate/DCCE/CRI/CRI-Deliverable-Map.md).


> [!pattern]
> The trigger log is **artifact-first and append-first**: log the trigger as soon as it becomes operationally important (e.g., a public hearing, sponsor instruction, or TOR interpretation), then gradually enrich links to evidence, decisions, and deliverables. Avoid speculative entries without at least one concrete artifact.

## Trigger table


| Trigger ID | Date       | Origin / source                                                              | Trigger type                   | Impact zone                                                       | Urgency | Linked evidence                                                  | Linked decisions                                              | Linked deliverables                                          | Status | Notes |
| ---------- | ---------- | ---------------------------------------------------------------------------- | ------------------------------ | ----------------------------------------------------------------- | ------- | ---------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------ | ------ | ----- |
| T-CRI-000  | 2025-10-17 | `inbox_note/Hypothesis_Climate-Resilience-Index_V4.md`                       | Internal framing / pivot       | Phase 1/2 interface; impact vs resilience split; spatial strategy | Medium  | E-CRI-001                                                        | (to be linked once Phase 1/2 interface notes are anchored)    | (to be mapped; likely Phase 1/2 methodology revisions)       | Logged | Internal decision to treat Phase 1 Impact Index as a complementary benchmark to spatial risk maps, pivot away from heavy new impact modelling in Phase 2, and focus on dasymetric mapping plus a new municipal-level Climate Resilience Index. Recorded here as a backfilled trigger from historical notes. |
| T-CRI-000A | 2025-10-29 | `inbox_note/Hypothesis_Climate-Resilience-Index_V3.md`                       | Internal hypothesis refinement | LAO data incentives; dual-track CRI framing                       | Low     | (to be linked once relevant evidence rows are added)             | (to be linked once data-governance / incentive notes exist)   | (to be mapped; candidate CRI data-architecture deliverables) | Logged | Refinement of project direction emphasising LAO-reported indicators (LPA, Sustainable City) and co-creation, signalling a shift toward using existing administrative systems as the backbone for Phase 2 capacity profiling rather than building standalone CRI data-entry tools. |
| T-CRI-000B | 2026-02-02 | `inbox_note/CRI pivoting to social-ecological system and context focused.md` | Internal conceptual pivot      | Conceptual framing; SES-based capacity design; indicator strategy | Medium  | (to be linked once SES framing synthesis is added to registry)   | (to be linked once CRI conceptual framing notes are anchored) | (to be mapped; future SES/capacity profile deliverables)     | Logged | Conceptual decision to frame CRI as a social-ecological, process-based resilience tool (with emphasis on governance, information, agency, and process indicators) rather than an asset-based readiness index, including explicit rejection of ND-GAIN-style "readiness" terminology. Backfilled from evergreen note. |
| T-CRI-001  | 2026-03-11 | CRI Phase 2 Public Hearing 1 (hybrid public consultation)                    | Public hearing signal          | Methodology framing; capacity-profile design; governance          | High    | E-CRI-010, E-CRI-011, E-CRI-012, E-CRI-013, E-CRI-014, E-CRI-015 | (to be linked once CRI decision / design anchors are created) | D-CRI-002, D-CRI-003, D-CRI-004                              | Logged | First formal Phase 2 methodology and implementation consultation; anchors the shift toward capacity profiles, profile-over-ranking stance, data-richness overlay, and multi-channel CRI use-cases. |
| T-CRI-002  | 2026-04-10 | `ψ/inbox/handoff/2026-04-10_15-10_cri-v3-structure-locked.md` + v3 governance freeze work | Governance / methodology freeze | Phase 2 governance lens; indicator-vetting preparation; evidence wiring | High | E-CRI-016, E-CRI-017, E-CRI-018 | (to be linked once governance-v3 claims / design anchors are added) | D-CRI-006, D-CRI-007 | Logged | Locked the Institutional Readiness governance lens as the canonical v3 framing for Phase 2, froze the six-pillar governance structure, hardened concept definitions through the concept-check workflow, and created a compact concept-summary surface for the first indicator-vetting pass. |

