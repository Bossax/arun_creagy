# Handoff: CRI Phase 2 Capacity Tagging v2 + CBI Crosswalk (Track B)

**Date**: 2026-04-08 16:22 (GMT+7)
**Context**: CRI Phase 2 capacity-tagging Track B has implemented v2 dictionary scaffolding and a first-pass CBI integration for key concepts; evidence wiring (B8) and profile-first demonstrator remain.

## What We Did
- Locked NotebookLM extraction status for the CRI capacity dictionary v2 workflow by updating the execution packet so that M1/F1/A1 are treated as the sufficient extraction set for this phase.
- Created and structured the canonical v2 capacity tagging dictionary:
  - [`ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary_v2.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary_v2.md)
- Migrated a representative slice of v1.1 long-list indicators into the v2 schema (plan revision cycle, coordination, finance, data/knowledge, community engagement, etc.), including capacity category, asset/process/output dimension, governance function, and data-richness scores.
- Integrated key NotebookLM-derived clusters into the v2 dictionary (risk-informed planning, coordination, financial mechanisms, community engagement/social support, emergency HR capacity, climate innovation/ICT, infrastructure robustness, risk assessment capabilities, progress in implementation).
- Implemented a first-pass CRI–CBI indicator crosswalk mapping v2 concepts to CBI codes with mapping types and confidence scores:
  - [`ψ/incubate/DCCE/CRI/output/CRI_CBI_indicator_crosswalk.md`](ψ/incubate/DCCE/CRI/output/CRI_CBI_indicator_crosswalk.md)
- Created and populated a CBI-integrated v2 dictionary variant, keyed by v2 concepts and annotated with linked CBI indicators, mapping types, and usage notes:
  - [`ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary_v2_CBI.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary_v2_CBI.md)
- Captured a retrospective and learning on subtask discipline for this workflow:
  - [`ψ/memory/retrospectives/2026-04/08/16.19_rrr_cri-capacity-v2-cbi-crosswalk.md`](ψ/memory/retrospectives/2026-04/08/16.19_rrr_cri-capacity-v2-cbi-crosswalk.md)
  - [`ψ/memory/learnings/2026-04-08_cri-capacity-v2-cbi-crosswalk-subtasking.md`](ψ/memory/learnings/2026-04-08_cri-capacity-v2-cbi-crosswalk-subtasking.md)

## Pending
- [ ] Track B8: Minimal QC and evidence wiring for the v2 dictionary and CBI bridge:
  - [ ] Register v2, v2_CBI, and the crosswalk in [`ψ/incubate/DCCE/CRI/output/CRI_AI_sources_index.md`](ψ/incubate/DCCE/CRI/output/CRI_AI_sources_index.md).
  - [ ] Add/update evidence entries in [`ψ/incubate/DCCE/CRI/output/CRI-Evidence-Registry.md`](ψ/incubate/DCCE/CRI/output/CRI-Evidence-Registry.md) and [`ψ/incubate/DCCE/CRI/output/CRI-Evidence-Coverage-Map.md`](ψ/incubate/DCCE/CRI/output/CRI-Evidence-Coverage-Map.md) for the v2 dictionary, CBI crosswalk, and CBI-integrated variant.
- [ ] Extend the CRI–CBI crosswalk beyond the initial subset (finance, planning, governance, communication, data/knowledge) to cover additional v2 concepts such as:
  - Governance readiness modifier
  - Formal coordination mechanism
  - Data interoperability score
  - Service delivery timeliness and case throughput
- [ ] Extend the CBI-integrated dictionary variant to mirror more of the canonical v2 concept list, including clearer treatment of CBI-only constructs that should remain narrative or adjacency-only.
- [ ] Return to Phase 2 immediate priorities (from [`ψ/incubate/DCCE/CRI/output/2026-04-07_cri-phase2-next-steps.md`](ψ/incubate/DCCE/CRI/output/2026-04-07_cri-phase2-next-steps.md)) once Track B is fully wired:
  - Operationalise the Administrative Gap protocol in Phase 1 data.
  - Build at least one profile-first provincial demonstrator using the v2 dictionary + CBI bridge.

## Next Session
- [ ] Implement Track B8 (evidence wiring):
  - [ ] Update AI sources index with v2 dictionary, v2_CBI, crosswalk, and NotebookLM v2 plan/packet/register.
  - [ ] Append evidence entries and coverage map references for v2 + CBI artifacts.
- [ ] Decide the minimal additional v2 concepts to prioritise in the next crosswalk expansion pass and document them as a short target list before editing.
- [ ] Sketch a mini-plan for the first provincial profile-first demonstrator (which province, which indicators, minimum outputs) based on the updated v2 tagging contract.

## Key Files
- Dictionary v1.1 and observations (baseline):  
  - [`ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary.md)  
  - [`ψ/incubate/DCCE/CRI/inbox_note/CRI_Capacity_Tagging_Dictionary_Observations.md`](ψ/incubate/DCCE/CRI/inbox_note/CRI_Capacity_Tagging_Dictionary_Observations.md)
- v2 dictionary and variants:  
  - [`ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary_v2.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary_v2.md)  
  - [`ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary_v2_CBI.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary_v2_CBI.md)
- CBI integration artifacts:  
  - [`ψ/incubate/DCCE/CRI/output/CRI_CBI_indicator_crosswalk.md`](ψ/incubate/DCCE/CRI/output/CRI_CBI_indicator_crosswalk.md)  
  - [`ψ/incubate/DCCE/CRI/output/CRI_CBI_method_reconstruction.md`](ψ/incubate/DCCE/CRI/output/CRI_CBI_method_reconstruction.md)  
  - [`ψ/incubate/DCCE/CRI/output/CRI_CBI_Bridging_Method_Note.md`](ψ/incubate/DCCE/CRI/output/CRI_CBI_Bridging_Method_Note.md)
- NotebookLM v2 pipeline (frozen extraction model):  
  - [`ψ/incubate/DCCE/CRI/output/notebooklm_capacity_dictionary_v2/00_query_plan.md`](ψ/incubate/DCCE/CRI/output/notebooklm_capacity_dictionary_v2/00_query_plan.md)  
  - [`ψ/incubate/DCCE/CRI/output/notebooklm_capacity_dictionary_v2/02_pilot_execution_packet.md`](ψ/incubate/DCCE/CRI/output/notebooklm_capacity_dictionary_v2/02_pilot_execution_packet.md)  
  - [`ψ/incubate/DCCE/CRI/output/notebooklm_capacity_dictionary_v2/synthesis/indicator_concept_register.md`](ψ/incubate/DCCE/CRI/output/notebooklm_capacity_dictionary_v2/synthesis/indicator_concept_register.md)

