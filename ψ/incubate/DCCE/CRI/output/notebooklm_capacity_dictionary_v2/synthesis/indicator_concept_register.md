---
type: knowledge_artifact
status: integration_in_progress
created: 2026-04-08
updated: 2026-04-08
project:
  - DCCE_CRI
title: Indicator Concept Register — NotebookLM Capacity Dictionary v2
---

# Indicator Concept Register — NotebookLM Capacity Dictionary v2

This is the local synthesis register for the refreshed v2 pipeline.

## Boundary reminder

- Do not paste raw NotebookLM dumps directly into this register.
- Update this file only after raw responses have been saved under [`responses/`](ψ/incubate/DCCE/CRI/output/notebooklm_capacity_dictionary_v2/responses/).
- Harmonisation, de-duplication, local canonical label choice, QC, and register maintenance happen here, not in NotebookLM.

## Current state

- Pilot-only harmonisation completed (P1, P2-pilot, P3-pilot).
- **Batch M1 (Methodological)** integrated 2026-04-08.
- **Batch F1 (Frameworks)** integrated 2026-04-08.

## Intake queue

- [x] Local Pass 1 raw pilot rows available in [`responses/2026-04-08_pilot_pass1_local_raw_rows.json`](ψ/incubate/DCCE/CRI/output/notebooklm_capacity_dictionary_v2/responses/2026-04-08_pilot_pass1_local_raw_rows.json)
- [x] NotebookLM Pass 2 raw pilot response (Note: Superseded by M1 for methodological core)
- [x] NotebookLM Pass 3 raw pilot response
- [x] Batch M1 (Methodological) saved verbatim in [`responses/2026-04-08_batch_M1_methodological_notebooklm_raw.md`](ψ/incubate/DCCE/CRI/output/notebooklm_capacity_dictionary_v2/responses/2026-04-08_batch_M1_methodological_notebooklm_raw.md)
- [x] Batch F1 (Frameworks) saved verbatim in [`responses/2026-04-08_batch_F1_framework_notebooklm_raw.md`](ψ/incubate/DCCE/CRI/output/notebooklm_capacity_dictionary_v2/responses/2026-04-08_batch_F1_framework_notebooklm_raw.md)
- [x] Batch A1 (Adjacency) saved verbatim in [`responses/2026-04-08_batch_A1_adjacency_notebooklm_raw.md`](ψ/incubate/DCCE/CRI/output/notebooklm_capacity_dictionary_v2/responses/2026-04-08_batch_A1_adjacency_notebooklm_raw.md)

## Traceability convention

 - `P1-xx`: Pilot Pass 1 (Local Paste)
 - `M1-xx`: Batch M1 (Methodological Core) - refer to row index in raw response.
 - `F1-xx`: Batch F1 (Framework Core) - refer to row index in raw response.
 - `A1-xx`: Batch A1 (Adjacency/Operational) - refer to row index in raw response.
 - `P2-xx` / `P3-xx`: Pilot-phase NotebookLM runs (being phased out by M/F/A batches).

## Pilot + Batch M1/F1/A1 integrated register

| canonical_indicator_concept                                 | supporting_raw_rows                                                                                            | provisional_capacity_category                                                                      | provisional_aspect                                                                                                                                                             | provisional_dimension                    | notes                                                                                                                                                                                                                                                           |
| ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Risk-informed and climate-integrated planning               | P1-01; P1-11; P3-01; P3-05; M1-04; M1-14; F1-01; A1-08                                                         | Adaptive / Institutional / Functional / Integrated                                                 | planning; climate information integration; risk-informed land-use planning; adoption of plans; integrated planning                                                             | process (explicit in M1-14)              | M1-14 reinforces integrated planning as a "process-oriented capability". F1-01 (GCRI) identifies comprehensive climate planning as an indicator of institutional governance. A1-08 adds comprehensive climate planning frameworks.                              |
| Coordination and multi-stakeholder collaboration            | P1-02; P1-12; P2-05; P3-05; M1-03; M1-10; M1-13; M1-15; F1-06; F1-11; A1-05                                    | Adaptive / Transformative / Functional / Inclusive / Strategic Management / Global integration     | coordination; community participation; collaboration of multi-stakeholders; interdependencies; empowerment of actors; international networks                                   | process                                  | M1-03 (governance input), M1-13 (inclusive/collective ownership), and M1-15 (empowerment of actors) significantly strengthen this cluster. F1-06 (GCRI) adds global integration (international networks). A1-05 adds dedicated cross-government climate bodies. |
| Financial mechanisms and resource allocation                | P1-03; P2-12; P3-04; P3-12; M1-01; M1-03; M1-08; M1-12; F1-03; F1-13; A1-04; A1-07; A1-10                      | Adaptive / Financial / Resourceful / Inputs / Institutional governance                             | finance/accountability; financial capacities; resource distribution; input indicators; investing in ability to organize resources; sustainable procurement                     | asset                                    | M1-01/03/12 confirm "inputs" and "resourceful" as core capacity category framings. F1-03 links sustainable procurement. A1-04/07 focus on allocation and retrofit financing. A1-10 reinforces sustainable procurement policies.                                 |
| Community engagement and social support                     | P1-04; P2-04; M1-06; M1-08; M1-10; M1-13; M1-20; F1-13                                                         | Transformative / Absorptive / Social / Inclusive / Organizational                                  | inclusion/legitimacy; community support; social networks; social capital; collective identity; stakeholder aspects                                                             | not explicit                             | M1-20 provides a detailed definition of "social capital" as an investment into networks. F1-13 (Brito) integrates social and stakeholder aspects into the organizational dimension.                                                                             |
| Emergency and human resource capacity                       | P1-10; P2-09; P2-11; M1-08; M1-09; M1-10; M1-19; F1-07; F1-10; A1-06                                           | Coping Capacity / Human/Health / Adaptive / Absorptive / Transformative / Organisational resources | emergency medical personnel; skills, knowledge, health, education; human resources; formal procedures; emergency responsiveness; early warning systems                         | asset (explicit in M1-19)                | M1-19 explicitly maps organisational resources as "assets". F1-07/10 focus on emergency responsiveness. A1-06 adds integrated, people-centred early warning systems.                                                                                            |
| Climate innovation and communication technology             | P1-13; P2-05; P2-08; P3-09; M1-08; M1-10; M1-19; F1-04; F1-05; A1-09; A1-11; A1-12                             | Transformative / Technological resources / Technology and innovation                               | innovation/technology; communication technology; technological resources and assets; smart city development; digital governance; climate transparency                          | asset (explicit in M1-19)                | M1-19 confirms technological infrastructure as an asset. F1-04/05 link smart city and e-government. A1-09/11/12 reinforce transparency and digital governance as key innovation aspects.                                                                        |
| Critical infrastructure and strategic service robustness    | P2-04; P3-04; P3-05; P3-06; M1-04; M1-05; M1-07; M1-09; M1-11; M1-17; F1-15; F1-16; F1-17; F1-18; A1-02; A1-03 | Absorptive / Functional / Physical / Infrastructure and ecosystems                                 | protective infrastructure; service management; interdependencies; cool points built; mobility and communications; infrastructure criticality; robustness; autonomy; redundancy | output (explicit in M1-04, M1-05, M1-07) | M1 provides explicit "output" indicators for infrastructure. F1-16/17/18 focus on physical resilience. A1-02/03 provide operational metrics for cooling points and green/blue infrastructure delivery.                                                          |
| Service delivery performance — urban solid waste collection | P3-02; F1-17                                                                                                   | not explicit / physical                                                                            | health and contamination risks; environmental quality; critical waste asset functionality                                                                                      | output                                   | Framework-specific candidate row. F1-17 links waste assets specifically to the physical resilience dimension.                                                                                                                                                   |
| Institutional mandate and governance readiness              | P2-01; P3-11; M1-08; M1-10; M1-15; F1-02                                                                       | Authority to adapt / Institutional governance / Strategic management                               | mandate; legal and policy systems; strategic management; efficiency; transparency                                                                                              | not explicit                             | M1-15 links "strategic management" to the broader governance theme. F1-02 (GCRI) adds "climate transparency" (CDP reporting) as a governance indicator.                                                                                                         |
| Risk assessment and urban diagnostic capabilities           | M1-04; M1-17; F1-12; F1-14                                                                                     | Functional / Spatial / Capabilities and Processes                                                  | risk mapping; diagnostic & risk assessment; spatial exposure                                                                                                                   | process (explicit in F1-12)              | F1-12 (WGS) explicitly classifies risk assessment under "Capabilities & Processes". F1-14 (Brito) links risk mapping to the "spatial" dimension.                                                                                                                |
| Progress in Implementation                                  | A1-01                                                                                                          | Implementation progress                                                                            | implemented projects; progress reporting                                                                                                                                       | output (explicit in A1-01)               | A1-01 explicitly identifies project implementation progress as an "output" indicator.                                                                                                                                                                           |

## Framing evidence retained but not yet collapsed

- `M1-01`: Five categories of indicators: targets, inputs, outputs, outcomes, impacts.
- `M1-02`: Five most used dimensions: social, economic, environmental, infrastructure, governance.
- `M1-08, M1-09, M1-10`: Systematic list of indicators for adaptive, absorptive, and transformative capacity (Zeng et al., 2022).
- `M1-11, M1-12, M1-13, M1-14`: Resilience attributes: Flexible, Resourceful, Inclusive, Integrated.
- `M1-15, M1-16, M1-17, M1-18`: Rockefeller Foundation framework dimensions (González Castillo et al., 2022).
- `F1-13, F1-14, F1-15, F1-16`: Brito et al. (2026) 4-dimension typology: Organizational, Spatial, Functional, Physical.
- `P1-05` to `P1-07`: CBI material triads (Coping/Adaptive/Transformative).
- `P1-08, P1-09`: Asset/Process local dimension statements.

## Integration Notes (2026-04-08)

1. **Batch M1 Verification:** The run successfully restricted itself to the three methodological sources. No substitution reported.
2. **Batch F1 Verification:** Successful extraction from the three targeted urban resilience framework sources. 18 rows extracted.
3. **Dimension Discipline:** M1 and F1 rows with explicit "output" or "asset" wording were integrated and used to strengthen provisional dimension assignments. F1-07, F1-08, F1-09 (WGS) use "output KPIs" explicitly.
4. **Register Expansion:** F1 added significant depth to "Infrastructure", "Governance transparency", and "Risk assessment" clusters.
5. **Supersession:** Pilot P2 (methodological) is now effectively superseded by M1. Pilot P3 (frameworks) is now superseded by F1.
