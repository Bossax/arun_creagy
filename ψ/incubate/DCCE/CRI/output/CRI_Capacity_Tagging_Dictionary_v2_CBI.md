---
type: knowledge_artifact
status: stub
version: 2.0-draft
created: 2026-04-08
last_updated: 2026-04-08
project:
  - DCCE_CRI
title: CRI Phase 2 Capacity Tagging Dictionary v2 – CBI-integrated variant
tags:
  - cri
  - capacity_tagging
  - phase2
  - v2_dictionary
  - cbi_integration
---

# CRI Phase 2 Capacity Tagging Dictionary v2 – CBI-integrated variant (Stub)

## Purpose

This file defines the **CBI-integrated variant** of the v2 capacity tagging dictionary. It is a **structural stub** for combining:

- the canonical v2 indicator concepts defined in `CRI_Capacity_Tagging_Dictionary_v2.md`, and
- the Climate Budget Integration (CBI) framing and indicators described in CRI CBI method notes.

The aim is to support a **single tagging dictionary** that can be filtered or projected into both:

- CRI capacity profiling views; and
- CBI-aligned budgeting and expenditure views.

## Relationship to other artifacts

- **v1.1 dictionary:** `CRI_Capacity_Tagging_Dictionary.md` remains the historical source of the initial indicator list and tagging rules.
- **Canonical v2 dictionary:** `CRI_Capacity_Tagging_Dictionary_v2.md` is the primary home for indicator concepts. This CBI-integrated file wraps that schema with CBI-specific fields; it does **not** introduce new indicator concepts on its own.
- **CBI method notes and bridging documents:**
  - `CRI_CBI_Bridging_Method_Note.md`
  - `CRI_CBI_method_reconstruction.md`
  - `CRI_CBI_indicator_crosswalk.md` (technical mapping table; see separate file)
- **NotebookLM v2 workflow:** CBI-related indicator ideas extracted via NotebookLM (under `output/notebooklm_capacity_dictionary_v2/`) will be surfaced here after they are canonicalised in the v2 dictionary.

## Planned structure and initial populated subset

The CBI-integrated dictionary extends each v2 indicator row with additional CBI-aligned attributes. At minimum, the fields are:

- All v2 fields from `CRI_Capacity_Tagging_Dictionary_v2.md`:
  - `canonical_indicator_concept`
  - `baseline_proxy`
  - `target_process_metric`
  - `capacity_category`
  - `aspect_or_dimension`
  - `governance_function`
  - `data_richness_confidence_0_3`
  - `supporting_evidence`
- Plus CBI-specific fields:
  - `cbi_indicator_code` – Reference code used in the CBI framework.
  - `cbi_indicator_label` – Short label used in CBI documentation.
  - `cbi_dimension` – Relevant CBI dimension or pillar.
  - `cbi_mapping_type` – Nature of the mapping (e.g. `baseline_proxy`, `composite`, `partial_overlap`, `adjacency_only`, `no_clear_match`).
  - `cbi_notes` – Brief explanation of the mapping logic, assumptions, or caveats.

For this subtask, we provide a **lightly populated** subset of indicator rows to demonstrate the CBI-integrated structure for key financial, governance, and data/knowledge capacities.

### Table (initial populated subset)

| canonical_indicator_concept                       | baseline_proxy                                                                                                                                                       | target_process_metric                                                                                                                                                                    | capacity_category | aspect_or_dimension | governance_function         | data_richness_confidence_0_3 | supporting_evidence                                                                                                                                        | cbi_indicator_code | cbi_indicator_label           | cbi_dimension            | cbi_mapping_type | cbi_notes                                                                                                                                                                                               |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ------------------- | --------------------------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ----------------------------- | ------------------------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Financial mechanisms and resource allocation      | Presence of dedicated climate/adaptation budget lines or funds and documented allocations to resilience, adaptation, and retrofit projects                           | Percentage of municipal capital and operating budget allocated to climate-resilient and adaptation-related investments using explicit and transparent eligibility criteria               | Adaptive          | asset               | finance                     | 1                            | register cluster: Financial mechanisms and resource allocation (P1-03; P2-12; P3-04; P3-12; M1-01; M1-03; M1-08; M1-12; F1-03; F1-13; A1-04; A1-07; A1-10) | TA2                | Climate Resilience Investment | Transformative / Asset   | baseline_proxy   | Use TA2 as the main quantitative baseline proxy for long-term climate resilience investment flows under this concept; treat AA2 and CA2 as complementary diagnostics rather than separate core proxies. |
| Climate budget tagging coverage                   | Climate budget tagging policy exists; # items tagged (if counts exist)                                                                                               | % of municipal budget items tagged as climate-related                                                                                                                                    | Adaptive          | process             | finance_accountability      | 1                            | v1.1 row: Climate budget tagging coverage                                                                                                                  | TA2                | Climate Resilience Investment | Transformative / Asset   | adjacency_only   | TA2 assumes some form of climate-related budget classification that should be underpinned by tagging coverage; do not treat TA2 as a direct measure of tagging performance.                             |
| Risk-informed and climate-integrated planning     | Existence of a formally adopted climate or DRM plan that includes documented climate/disaster risk assessment and cross-references key sector and land-use plans     | Proportion of strategic plans and major land-use or investment decisions that explicitly document the use of climate risk assessment outputs                                             | Adaptive          | process             | planning                    | 1                            | register cluster: Risk-informed and climate-integrated planning (P1-01; P1-11; P3-01; P3-05; M1-04; M1-14; F1-01; A1-08)                                   | AP1                | Climate Adaptation Plan       | Adaptive / Process       | baseline_proxy   | Use AP1 (plan existence) as the primary baseline proxy for this concept; complement with AP2 to assess integration depth where available.                                                               |
| Policy integration score                          | Climate integrated in key sector plan(s) (binary per sector)                                                                                                         | Share of sector plans integrating climate resilience                                                                                                                                     | Adaptive          | process             | policy_integration          | 1                            | v1.1 row: Policy integration score                                                                                                                         | AP2                | Climate Data Integration      | Adaptive / Process       | baseline_proxy   | Treat AP2’s 1–5 scale as the main CBI-aligned baseline proxy for how far climate information is integrated into development planning, approximating this concept.                                       |
| Community engagement and social support           | Existence of structured participation mechanisms and documented engagement activities, including community organisations and social support networks                 | Number and diversity of community engagement events per year with evidence of attendance, feedback loops, and actions taken to strengthen social support and inclusion                   | Transformative    | not_explicit        | inclusion_legitimacy        | 1                            | register cluster: Community engagement and social support (P1-04; P2-04; M1-06; M1-08; M1-10; M1-13; M1-20; F1-13)                                         | AP3                | Community Participation       | Adaptive / Process       | baseline_proxy   | Use AP3’s participation-level scale as a strong process-quality baseline proxy for this concept; note that social support network depth remains only partially covered.                                 |
| Emergency and human resource capacity             | Counts of staff in emergency, health, and DRM roles per population, plus existence of documented emergency response procedures and early warning coverage indicators | Proportion of relevant staff trained annually in emergency response and proportion of population covered by effective, people-centred multi-hazard early warning systems                 | Coping            | asset               | human_resources_response    | 1                            | register cluster: Emergency and human resource capacity (P1-10; P2-09; P2-11; M1-08; M1-09; M1-10; M1-19; F1-07; F1-10; A1-06)                             | CA4                | Emergency Medical Personnel   | Coping / Asset           | baseline_proxy   | Use CA4 as the primary quantitative baseline proxy on staffing; combine with qualitative information on training and EWS coverage during analysis, not as separate indicators.                          |
| Climate innovation and communication technology   | Existence of digital platforms, open data portals, and smart-city infrastructure used for climate risk communication, transparency, and participation                | Usage and reliability of digital climate services (e.g. population reach via digital early warning, update frequency, and uptime of climate information platforms and open data portals) | Transformative    | asset               | digital_innovation          | 1                            | register cluster: Climate innovation and communication technology (P1-13; P2-05; P2-08; P3-09; M1-08; M1-10; M1-19; F1-04; F1-05; A1-09; A1-11; A1-12)     | CP4                | Risk Communication Channels   | Coping / Process         | partial_overlap  | CP4 measures diversity of communication channels and thus partially covers the communication side of this concept; indicators of digital platform performance remain to be defined as Target metrics.   |
| Climate innovation and communication technology   | Existence of digital platforms, open data portals, and smart-city infrastructure used for climate risk communication, transparency, and participation                | Usage and reliability of digital climate services (e.g. population reach via digital early warning, update frequency, and uptime of climate information platforms and open data portals) | Transformative    | asset               | digital_innovation          | 1                            | register cluster: Climate innovation and communication technology (P1-13; P2-05; P2-08; P3-09; M1-08; M1-10; M1-19; F1-04; F1-05; A1-09; A1-11; A1-12)     | TP3                | Climate Innovation Adoption   | Transformative / Process | baseline_proxy   | Use TP3 as the main CBI baseline proxy for innovation and technology adoption under this concept; it highlights the presence of climate-related innovation projects rather than platform coverage.      |
| Risk assessment and urban diagnostic capabilities | Existence of citywide climate and disaster risk assessments, exposure maps, and diagnostic studies covering multiple hazards and sectors                             | Frequency, granularity, and update cadence of risk assessments and diagnostics, and documented integration of their outputs into planning and investment decisions                       | Adaptive          | process             | risk_assessment             | 2                            | register cluster: Risk assessment and urban diagnostic capabilities (M1-04; M1-17; F1-12; F1-14)                                                           | AP2                | Climate Data Integration      | Adaptive / Process       | partial_overlap  | AP2 signals the presence and use of climate and risk information in development planning; treat this as a partial proxy, to be sharpened once explicit CBI-style risk assessment indicators are added.  |
| Performance dashboard coverage                    | Public dashboard exists (URL) and shows KPIs                                                                                                                         | Dashboard includes context + equity sections; update cadence measured                                                                                                                    | Transformative    | asset               | transparency_accountability | 2                            | v1.1 row: Performance dashboard coverage                                                                                                                   | AP4                | Public Climate Literacy       | Adaptive / Process       | adjacency_only   | AP4 provides an adjacent signal on public awareness and climate literacy; it should not be treated as a direct proxy for dashboard coverage but can be used narratively alongside this concept.         |

> **Note:** This subset is intentionally small and pattern-focused. Later Track B passes should extend it to additional v2 concepts and CBI indicators, following the same schema and mapping vocabulary.

## Usage (once populated)

- Use this file when a **single table** is needed that aligns CRI Phase 2 capacity indicators with the CBI budgeting and expenditure framing.
- Maintain the v2 canonical fields as the primary reference, while treating CBI fields as **projections** into the budgeting domain.
- Keep this file in sync with:
  - `CRI_Capacity_Tagging_Dictionary_v2.md` (for indicator concepts and capacity tagging), and
  - `CRI_CBI_indicator_crosswalk.md` (for technical mapping and traceability).
