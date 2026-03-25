# Handoff: CRI — Data analysis tasks and evidence spine

**Date**: 2026-03-25 12:32
**Context**: CRI project structure now mirrors the CRDB pattern (Hub + plan + evidence registry + coverage map). Public Hearing 1 has been ingested as cleaned transcripts, a summary note, and three curated hearing notes. Legacy management surfaces (Implementation Plan, Working Status Brief, AI sources index) have been archived as evidence-only and superseded by the Hub, plan, methodologies, and evidence system.

## What We Did
- Mirrored the CRDB project pattern into CRI at `ψ/incubate/DCCE/CRI` (Hub, plan, inbox_source/inbox_note/output, archive).
- Created the CRI evidence spine:
  - Registry: `ψ/incubate/DCCE/CRI/output/CRI-Evidence-Registry.md`
  - Coverage map: `ψ/incubate/DCCE/CRI/output/CRI-Evidence-Coverage-Map.md`
- Ingested CRI Public Hearing 1 as first-class evidence:
  - Cleaned transcripts for Part 1 and Part 2 in `inbox_source/`.
  - Summary note in `ψ/incubate/DCCE/CRI/inbox_note/2026-03-CRI_Phase2_Public_Hearing1_summary.md`.
  - Three curated notes in `output/` (decisions & signals, methodology implications, implementation/governance signals).
- Retired legacy management surfaces as active dashboards and marked them `status: archived` with `superseded_by` pointers:
  - `ψ/incubate/DCCE/CRI/output/CRI_Implementation Plan.md`
  - `ψ/incubate/DCCE/CRI/output/CRI_Working Status Brief.md`
  - `ψ/incubate/DCCE/CRI/output/CRI_AI_sources_index.md`
- Updated Hub and plan to anchor onto the methodologies, evidence registry/coverage map, and hearing notes instead of the retired surfaces.

## Pending
- [ ] Finalize E-CRI-010..015 entries in `ψ/incubate/DCCE/CRI/output/CRI-Evidence-Registry.md` for:
  - Part 1 cleaned transcript
  - Part 2 cleaned transcript
  - Hearing 1 summary note
  - Hearing 1 decisions & design signals
  - Hearing 1 methodology implications
  - Hearing 1 implementation & governance signals
- [ ] Extend `ψ/incubate/DCCE/CRI/output/CRI-Evidence-Coverage-Map.md` so each dimension (Impact Index, Capacity Profiles, Data Richness, SES framing, Governance/Implementation) explicitly references E-CRI-010..015 and states what each artifact contributes.
- [ ] Decide and encode the **Transformative capacity** stance (where it is measured and how light/heavy it is) in `ψ/incubate/DCCE/CRI/output/CRI Phase 2 Methodology.md`, pointing to hearing evidence.
- [ ] Decide and encode the **spatial resolution contract** for CRI Phase 2 (province/district/tambon or hybrid) in the methodology and implementation docs, using hearing evidence and data-availability constraints.
- [ ] Tighten method-level references so Phase 1/2 methodologies explicitly cite the new hearing notes (by title or E-CRI ids) in the sections on: Fiscal Relief framing, two-speed measurement, capacity tiers, profiling vs ranking, and data-richness/confidence overlay.
- [ ] For each major CRI synthesis note (`CRI_resilience_measurement_synthesis.md`, `CRI_capacity_concepts_synthesis.md`, `CRI_loss_and_damage_estimation_synthesis.md`), ensure there is a corresponding registry entry with clear dimensions and that those entries are referenced in the coverage map.

## Next Session (Data analysis focus)
- [ ] Populate and review the E-CRI-010..015 rows in `ψ/incubate/DCCE/CRI/output/CRI-Evidence-Registry.md` to make Hearing 1 fully visible in the evidence spine.
- [ ] Work through `ψ/incubate/DCCE/CRI/output/CRI-Evidence-Coverage-Map.md` dimension by dimension and:
  - Add bullets that reference relevant registry ids (including hearing artifacts and key syntheses).
  - Mark obvious gaps where no current evidence exists for a dimension (e.g., Transformative capacity, certain governance metrics, specific spatial resolutions).
- [ ] From the registry + coverage map, extract a **data analysis to-do list**:
  - Which indicators need data-quality checks (e.g., relief series zeros vs hazard masks)?
  - Which proxy layers need to be assembled or audited (e.g., urban exposure, process-based capacity indicators)?
  - Which admin datasets require exploratory analysis before they can be safely used in Phase 2.
- [ ] Start one narrow data-analysis task (e.g., testing the Administrative Gap protocol for a small subset of provinces) and capture the results in a short note under `ψ/incubate/DCCE/CRI/output/` linked into the evidence registry.

## Key Files
- Hub and plan:
  - `ψ/incubate/DCCE/CRI/Hub.md`
  - `ψ/incubate/DCCE/CRI/plan.md`
- Evidence spine:
  - `ψ/incubate/DCCE/CRI/output/CRI-Evidence-Registry.md`
  - `ψ/incubate/DCCE/CRI/output/CRI-Evidence-Coverage-Map.md`
- Hearing 1 artifacts:
  - `ψ/incubate/DCCE/CRI/inbox_source/2026-03-CRI_Public_Hearing_Phase2_Framework_Part1_transcript_clean.md`
  - `ψ/incubate/DCCE/CRI/inbox_source/2026-03-CRI_Public_Hearing_Phase2_Framework_Part2_transcript_clean.md`
  - `ψ/incubate/DCCE/CRI/inbox_note/2026-03-CRI_Phase2_Public_Hearing1_summary.md`
  - `ψ/incubate/DCCE/CRI/output/CRI_Phase2_Public_Hearing1_decisions_and_signals.md`
  - `ψ/incubate/DCCE/CRI/output/CRI_Public_Hearing1_Methodology_Implications.md`
  - `ψ/incubate/DCCE/CRI/output/CRI_Public_Hearing1_Implementation_Governance_Signals.md`
- Legacy management surfaces (now archived as evidence):
  - `ψ/incubate/DCCE/CRI/output/CRI_Implementation Plan.md`
  - `ψ/incubate/DCCE/CRI/output/CRI_Working Status Brief.md`
  - `ψ/incubate/DCCE/CRI/output/CRI_AI_sources_index.md`

