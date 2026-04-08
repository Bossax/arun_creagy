type: technical_mapping
status: partial_mapping
version: 0.2-draft
created: 2026-04-08
last_updated: 2026-04-08
project:
  - DCCE_CRI
title: CRI–CBI Indicator Crosswalk (Schema Stub)
tags:
  - cri
  - cbi
  - indicator_crosswalk
  - mapping_table
---

# CRI–CBI Indicator Crosswalk (Schema Stub)

## Purpose

This file defines the **technical mapping table** between:

- canonical v2 indicator concepts in `CRI_Capacity_Tagging_Dictionary_v2.md`, and
- CBI indicator codes and dimensions used in CRI–CBI integration work.

In this subtask (B2–B3), the crosswalk is a **schema-only stub**. It establishes the header and field definitions so that later subtasks (B4–B8) can populate mappings in a structured, traceable way.

## Relationship to other artifacts

- `CRI_Capacity_Tagging_Dictionary_v2.md` – source of canonical indicator concepts and capacity/governance tags.
- `CRI_Capacity_Tagging_Dictionary_v2_CBI.md` – integrated dictionary that combines CRI v2 fields with CBI-specific fields for day-to-day use.
- `CRI_Capacity_Tagging_Dictionary.md` – v1.1 dictionary; remains an upstream reference for how indicators were first framed.
- `CRI_CBI_Bridging_Method_Note.md` and `CRI_CBI_method_reconstruction.md` – narrative descriptions of the CBI integration logic that this table will operationalise.
- `output/notebooklm_capacity_dictionary_v2/` – NotebookLM extraction and synthesis workspace that may provide candidate mappings or clarifications.

## Table schema (initial populated subset)

The crosswalk is implemented as a markdown table with the following columns:

- `cri_canonical_indicator_concept` – Reference to the v2 canonical concept label.
- `cri_capacity_category` – Coping / Adaptive / Transformative.
- `cri_governance_function` – Primary governance function tag from the v2 dictionary.
- `cbi_indicator_code` – Code used for the corresponding CBI indicator (if any).
- `cbi_indicator_label` – Short label or description of the CBI indicator.
- `cbi_dimension` – Relevant CBI dimension or pillar.
- `mapping_type` – Nature of the mapping (e.g. `direct`, `derived`, `composite`, `one_to_many`, `many_to_one`, `no_match`).
- `mapping_confidence_0_3` – Qualitative confidence score (0–3) for the mapping itself (separate from data-richness of the indicator).
- `notes` – Short free-text notes on assumptions, caveats, or decisions.

### Header

| cri_canonical_indicator_concept                   | cri_capacity_category | cri_governance_function     | cbi_indicator_code | cbi_indicator_label           | cbi_dimension            | mapping_type    | mapping_confidence_0_3 | notes                                                                                                                                                                                          |
| ------------------------------------------------- | --------------------- | --------------------------- | ------------------ | ----------------------------- | ------------------------ | --------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Financial mechanisms and resource allocation      | Adaptive              | finance                     | TA2                | Climate Resilience Investment | Transformative / Asset   | baseline_proxy  | 3                      | TA2 provides a direct budget-based baseline proxy for long-term climate resilience investment within this concept; alignment improves once climate budget tagging is formalised.               |
| Financial mechanisms and resource allocation      | Adaptive              | finance                     | AA2                | Recovery Budget               | Adaptive / Asset         | baseline_proxy  | 2                      | AA2 complements TA2 by capturing post-disaster recovery budget per capita; together they approximate the broader financial mechanisms and resource allocation concept.                         |
| Financial mechanisms and resource allocation      | Adaptive              | finance                     | CA2                | Emergency Disaster Fund       | Coping / Asset           | partial_overlap | 2                      | CA2 focuses on emergency response funds, covering only one slice of the wider financial mechanisms and resource allocation concept.                                                            |
| Climate budget tagging coverage                   | Adaptive              | finance_accountability      | TA2                | Climate Resilience Investment | Transformative / Asset   | adjacency_only  | 1                      | TA2 uses a climate-related project classification that would typically be enabled by budget tagging, but it does not itself measure tagging coverage; treat this as an adjacency-only linkage. |
| Emergency budget disbursement timeline            | Coping                | finance_response            | CA2                | Emergency Disaster Fund       | Coping / Asset           | partial_overlap | 2                      | CA2 measures emergency fund levels, which are a necessary but not sufficient condition for timely disbursement captured in this concept.                                                       |
| Risk-informed and climate-integrated planning     | Adaptive              | planning                    | AP1                | Climate Adaptation Plan       | Adaptive / Process       | baseline_proxy  | 3                      | Existence of an approved provincial climate adaptation plan is treated as a strong baseline proxy for risk-informed and climate-integrated planning capacity.                                  |
| Risk-informed and climate-integrated planning     | Adaptive              | planning                    | AP2                | Climate Data Integration      | Adaptive / Process       | composite       | 2                      | AP2’s 1–5 scale captures the quality of climate data integration into development plans and can be used as a composite proxy for this concept when interpreted alongside AP1.                  |
| Policy integration score                          | Adaptive              | policy_integration          | AP2                | Climate Data Integration      | Adaptive / Process       | baseline_proxy  | 2                      | AP2 directly reflects the degree to which climate information is integrated into provincial development planning, aligning with policy integration under this concept.                         |
| Community engagement and social support           | Transformative        | inclusion_legitimacy        | AP3                | Community Participation       | Adaptive / Process       | baseline_proxy  | 3                      | AP3’s participation ladder provides a strong process-quality proxy for community engagement and social support capacities.                                                                     |
| Emergency and human resource capacity             | Coping                | human_resources_response    | CA4                | Emergency Medical Personnel   | Coping / Asset           | baseline_proxy  | 2                      | CA4 measures emergency health personnel per population and is used as a baseline proxy for broader emergency and human resource capacity.                                                      |
| Climate innovation and communication technology   | Transformative        | digital_innovation          | CP4                | Risk Communication Channels   | Coping / Process         | partial_overlap | 2                      | CP4 captures diversity of risk communication channels and serves as a partial proxy for digital communication aspects of this concept.                                                         |
| Climate innovation and communication technology   | Transformative        | digital_innovation          | TP3                | Climate Innovation Adoption   | Transformative / Process | baseline_proxy  | 2                      | TP3 counts climate-related innovation projects and is used as a baseline proxy for innovation and technology adoption capacities.                                                              |
| Risk assessment and urban diagnostic capabilities | Adaptive              | risk_assessment             | AP2                | Climate Data Integration      | Adaptive / Process       | partial_overlap | 2                      | AP2 implies use of climate and risk information in planning; when supported by separate risk assessment evidence it can partially proxy diagnostic capabilities.                               |
| Performance dashboard coverage                    | Transformative        | transparency_accountability | AP4                | Public Climate Literacy       | Adaptive / Process       | adjacency_only  | 1                      | AP4 reflects public awareness and literacy rather than dashboards; it is treated only as an adjacent signal for transparency and communication capacity.                                       |

> **Note:** This is a first-pass, non-exhaustive crosswalk focusing on fiscal/budget, governance/institutional, and data/knowledge capacities. Mappings and confidence scores are expected to be refined and extended in later Track B subtasks.

## Usage (once populated)

When populated in later subtasks, this table will:

- Provide a **machine- and human-readable bridge** between CRI v2 capacity indicators and CBI indicator codes.
- Support filtering and aggregation of CRI-tagged indicators into CBI reporting structures.
- Preserve traceability by keeping mapping decisions, confidence, and notes in one place.

Until then, treat this file as a **design artefact** documenting the intended crosswalk schema.
