---
type: knowledge_artifact
status: draft
version: 2.0-draft
created: 2026-04-08
last_updated: 2026-04-08
project:
  - DCCE_CRI
title: CRI Phase 2 Capacity Tagging Dictionary v2 (Canonical)
tags:
  - cri
  - capacity_tagging
  - phase2
  - v2_dictionary
---

# CRI Phase 2 Capacity Tagging Dictionary v2 (Canonical)

## Purpose

This file defines the **canonical v2 tagging dictionary** for CRI Phase 2. It refactors and extends the v1.1 dictionary in `CRI_Capacity_Tagging_Dictionary.md` into a more explicit schema focused on **indicator concepts** and their **Baseline vs Target** measurement stance.

The v2 dictionary:

- Preserves the conceptual content and two-speed measurement stance defined in the v1.1 dictionary (`CRI_Capacity_Tagging_Dictionary.md`).
- Integrates new indicator concepts and refinements emerging from the NotebookLM v2 synthesis workflow under `output/notebooklm_capacity_dictionary_v2/` (including the M1/F1/A1 extraction batches defined in `02_pilot_execution_packet.md`).
- Makes the structure of each indicator concept explicit, separating the concept label, Baseline proxy, Target process metric (if defined), capacity tags, governance function, and confidence score.

This v2 artifact is the **living reference** for all subsequent CRI Phase 2 tagging work in Track B.

## Relationship to v1.1 dictionary

The v1.1 dictionary in `CRI_Capacity_Tagging_Dictionary.md` remains the historical record of how Phase 2 tagging was first operationalised. It:

- Introduced the **two-speed measurement stance** (Baseline vs Target).
- Defined an initial long-list of indicator concepts in a wide table.
- Established the **0–3 data-richness/confidence scale** applied to Baseline proxies.

The v2 dictionary keeps these rules but reorganises the content so that each **canonical indicator concept** is represented as a structured row (or block) with clearly named fields. When individual v1.1 rows are migrated into v2 (Track B4–B5), the v1.1 file will be treated as an input source, not edited retroactively.

## Relationship to NotebookLM v2 synthesis

The NotebookLM v2 workflow under `output/notebooklm_capacity_dictionary_v2/` provides a structured extraction and synthesis of indicator ideas and capacity concepts from external frameworks and internal notes.

Within that workflow:

- Batches **M1/F1/A1** are treated as a sufficient extraction set for Phase 2, with later batches (M2/F2/A2) as optional gap-filling.
- The NotebookLM register tracks which sources and prompt sessions gave rise to candidate indicator concepts.

This v2 dictionary is the **landing zone** for canonicalising those candidate concepts. Later tasks (B4–B5) will:

- Map selected NotebookLM concepts into v2 `canonical_indicator_concept` entries.
- Record supporting evidence back to the NotebookLM register (e.g. batch IDs, row references) using the `supporting_evidence` field defined below.

## Schema for v2 indicator concepts

Each row in the v2 dictionary represents a single **canonical indicator concept** with the following fields:

- `canonical_indicator_concept` – Short, human-readable label used locally in v2 to name the indicator concept.
- `baseline_proxy` – Description of the Baseline measurement using secondary/admin data (proxy, stock, or binary indicator), consistent with the practicality stance.
- `target_process_metric` – Description of the Target process-quality metric (event- or process-log based). May be `n/a` where not yet defined.
- `capacity_category` – Capacity classification: `Coping`, `Adaptive`, or `Transformative`.
- `aspect_or_dimension` – Structural lens for the indicator (e.g. `asset`, `process`, `output`, or `not_explicit`).
- `governance_function` – Primary governance function or role (e.g. `planning`, `coordination`, `finance`, `data_governance`, etc.).
- `data_richness_confidence_0_3` – Estimated data-richness/confidence score (0–3) for the **Baseline proxy**, using the existing scale from v1.1.
- `supporting_evidence` – Brief references to evidence and provenance (e.g. `P1/M1/F1/A1 row IDs`, internal note IDs, or literature shorthand).

### Data-richness / confidence scale (Baseline proxy)

The v2 dictionary reuses the v1.1 **0–3 data-richness/confidence scale** for Baseline proxies:

- **0** – Not realistically measurable via existing secondary/admin data without event-level logs or new primary collection.
- **1** – Partially measurable or highly inconsistent; requires substantial interpretation or proxying.
- **2** – Measurable with reasonable effort via existing reports/registries/web presence; still needs normalization and QA.
- **3** – Measurable via structured, regularly reported fields in known pipelines (high repeatability).

## Table structure (initial v1.1-mapped rows)

The canonical v2 dictionary is represented as a markdown table with the schema above. This section now contains the **first pass of populated rows**, migrated from the v1.1 nominal indicator long-list in `CRI_Capacity_Tagging_Dictionary.md`.

| canonical_indicator_concept            | baseline_proxy                                                                                                       | target_process_metric                                                         | capacity_category | aspect_or_dimension | governance_function         | data_richness_confidence_0_3 | supporting_evidence                                |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------- | ------------------- | --------------------------- | ---------------------------- | -------------------------------------------------- |
| Plan revision cycle                    | Plan exists + last revised year (or last published version)                                                          | Months since last update of climate/DRM plan; update cadence over N years     | Adaptive          | process             | planning                    | 2                            | v1.1 row: Plan revision cycle                      |
| After-action review completion rate    | AAR mechanism exists (policy/guideline/template) + count of drills/exercises reported (if any)                       | % of major events with AAR completed within timeframe                         | Adaptive          | process             | learning_accountability     | 0                            | v1.1 row: After-action review completion rate      |
| Cross-department coordination meetings | Formal coordination body exists (committee/taskforce) + publicized meeting minutes (if available)                    | # formal inter-agency coordination meetings per year (with attendance/agenda) | Adaptive          | process             | coordination                | 1                            | v1.1 row: Cross-department coordination meetings   |
| Emergency budget disbursement timeline | Emergency fund/reserve exists; annual allocation size; emergency spending line items (if available)                  | Average days to disburse emergency funds after event                          | Coping            | process             | finance_response            | 1                            | v1.1 row: Emergency budget disbursement timeliness |
| Emergency procurement cycle time       | Emergency procurement policy exists; procurement budget allocated; procurement “fast track” clause exists            | Days from request to award for emergency procurement                          | Coping            | process             | procurement_response        | 0                            | v1.1 row: Emergency procurement cycle time         |
| Climate budget tagging coverage        | Climate budget tagging policy exists; # items tagged (if counts exist)                                               | % of municipal budget items tagged as climate-related                         | Adaptive          | process             | finance_accountability      | 1                            | v1.1 row: Climate budget tagging coverage          |
| Service delivery timeliness            | Service coverage proxies (service availability, staffing levels, complaint counts)                                   | Median processing time for core municipal services                            | Adaptive          | output              | service_delivery            | 0                            | v1.1 row: Service delivery timeliness              |
| Case throughput rate                   | Aggregate resolved-case totals (if reported) + staffing levels (if reported)                                         | Resolved cases per staff per period (department-level)                        | Adaptive          | output              | operations                  | 0                            | v1.1 row: Case throughput rate                     |
| Governance readiness modifier          | Composite proxy from verifiable items (strategy exists, org unit exists, budget allocated, basic data systems exist) | Feasibility-adjusted readiness score with explicit rubric and documentation   | Transformative    | not_explicit        | institutional_feasibility   | 2                            | v1.1 row: Governance readiness modifier            |
| Formal coordination mechanism          | CRO/taskforce exists; mandate documented; membership list exists                                                     | Activation frequency + outputs (meetings/year, joint projects/year)           | Transformative    | process             | governance_reform           | 2                            | v1.1 row: Formal coordination mechanism            |
| Performance dashboard coverage         | Public dashboard exists (URL) and shows KPIs                                                                         | Dashboard includes context + equity sections; update cadence measured         | Transformative    | asset               | transparency_accountability | 2                            | v1.1 row: Performance dashboard coverage           |
| Data interoperability score            | Metadata standard exists; data catalog exists; interoperability policy exists                                        | % datasets compliant with metadata standard                                   | Transformative    | asset               | data_governance             | 1                            | v1.1 row: Data interoperability score              |
| Policy integration score               | Climate integrated in key sector plan(s) (binary per sector)                                                         | Share of sector plans integrating climate resilience                          | Adaptive          | process             | policy_integration          | 1                            | v1.1 row: Policy integration score                 |
| Community engagement frequency         | Participation mechanism exists; engagement activities documented in annual report                                    | # engagements/year with attendance + feedback loop evidence                   | Transformative    | process             | inclusion_legitimacy        | 1                            | v1.1 row: Community engagement frequency           |

## Usage

- Treat this file as the **living, canonical tagging dictionary** for CRI Phase 2 once populated.
- Ground new entries in both:
  - the v1.1 dictionary (`CRI_Capacity_Tagging_Dictionary.md`), and
  - the NotebookLM v2 synthesis register under `output/notebooklm_capacity_dictionary_v2/`.
- Maintain the **two-speed stance** (Baseline vs Target) and the **0–3 confidence scores** as described in the v1.1 dictionary and in `CRI Phase 2 Methodology.md`.
- When later subtasks begin populating rows, ensure each indicator concept records at least:
  - a clear Baseline proxy definition;
  - a Target process metric definition or explicit `n/a`;
  - one capacity category and one primary governance function; and
  - a reasoned confidence score backed by visible supporting evidence.

## NotebookLM-derived clusters (initial integration — B5)

The following rows capture a first pass of **NotebookLM-derived indicator concept clusters** from `notebooklm_capacity_dictionary_v2/synthesis/indicator_concept_register.md`. They use the same schema as the main table above but are presented separately for clarity during integration.

| canonical_indicator_concept                              | baseline_proxy                                                                                                                                                       | target_process_metric                                                                                                                                                                    | capacity_category | aspect_or_dimension | governance_function       | data_richness_confidence_0_3 | supporting_evidence                                                                                                                                                                         |
| -------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ------------------- | ------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Risk-informed and climate-integrated planning            | Existence of a formally adopted climate or DRM plan that includes documented climate/disaster risk assessment and cross-references key sector and land-use plans     | Proportion of strategic plans and major land-use or investment decisions that explicitly document the use of climate risk assessment outputs                                             | Adaptive          | process             | planning                  | 1                            | register cluster: Risk-informed and climate-integrated planning (P1-01; P1-11; P3-01; P3-05; M1-04; M1-14; F1-01; A1-08)                                                                    |
| Coordination and multi-stakeholder collaboration         | Existence of formal coordination mechanisms (committees, taskforces, working groups) with documented mandates and membership including multiple stakeholder groups   | Number of multi-stakeholder coordination meetings and joint initiatives per year with documented agendas, attendance, and follow-up actions                                              | Adaptive          | process             | coordination              | 1                            | register cluster: Coordination and multi-stakeholder collaboration (P1-02; P1-12; P2-05; P3-05; M1-03; M1-10; M1-13; M1-15; F1-06; F1-11; A1-05)                                            |
| Financial mechanisms and resource allocation             | Presence of dedicated climate/adaptation budget lines or funds and documented allocations to resilience, adaptation, and retrofit projects                           | Percentage of municipal capital and operating budget allocated to climate-resilient and adaptation-related investments using explicit and transparent eligibility criteria               | Adaptive          | asset               | finance                   | 1                            | register cluster: Financial mechanisms and resource allocation (P1-03; P2-12; P3-04; P3-12; M1-01; M1-03; M1-08; M1-12; F1-03; F1-13; A1-04; A1-07; A1-10)                                  |
| Community engagement and social support                  | Existence of structured participation mechanisms and documented engagement activities, including community organisations and social support networks                 | Number and diversity of community engagement events per year with evidence of attendance, feedback loops, and actions taken to strengthen social support and inclusion                   | Transformative    | not_explicit        | inclusion_legitimacy      | 1                            | register cluster: Community engagement and social support (P1-04; P2-04; M1-06; M1-08; M1-10; M1-13; M1-20; F1-13)                                                                          |
| Emergency and human resource capacity                    | Counts of staff in emergency, health, and DRM roles per population, plus existence of documented emergency response procedures and early warning coverage indicators | Proportion of relevant staff trained annually in emergency response and proportion of population covered by effective, people-centred multi-hazard early warning systems                 | Coping            | asset               | human_resources_response  | 1                            | register cluster: Emergency and human resource capacity (P1-10; P2-09; P2-11; M1-08; M1-09; M1-10; M1-19; F1-07; F1-10; A1-06)                                                              |
| Climate innovation and communication technology          | Existence of digital platforms, open data portals, and smart-city infrastructure used for climate risk communication, transparency, and participation                | Usage and reliability of digital climate services (e.g. population reach via digital early warning, update frequency, and uptime of climate information platforms and open data portals) | Transformative    | asset               | digital_innovation        | 1                            | register cluster: Climate innovation and communication technology (P1-13; P2-05; P2-08; P3-09; M1-08; M1-10; M1-19; F1-04; F1-05; A1-09; A1-11; A1-12)                                      |
| Critical infrastructure and strategic service robustness | Inventory of critical infrastructure assets and strategic services and presence of key protective infrastructure (e.g. cooling centres, flood defences, backups)     | Share of critical services with documented resilience measures, redundancy, continuity plans, and acceptable downtime thresholds following extreme events                                | Absorptive        | output              | infrastructure_resilience | 1                            | register cluster: Critical infrastructure and strategic service robustness (P2-04; P3-04; P3-05; P3-06; M1-04; M1-05; M1-07; M1-09; M1-11; M1-17; F1-15; F1-16; F1-17; F1-18; A1-02; A1-03) |
| Risk assessment and urban diagnostic capabilities        | Existence of citywide climate and disaster risk assessments, exposure maps, and diagnostic studies covering multiple hazards and sectors                             | Frequency, granularity, and update cadence of risk assessments and diagnostics, and documented integration of their outputs into planning and investment decisions                       | Adaptive          | process             | risk_assessment           | 2                            | register cluster: Risk assessment and urban diagnostic capabilities (M1-04; M1-17; F1-12; F1-14)                                                                                            |
| Progress in implementation                               | Project registers or reports that track planned resilience and adaptation projects with basic implementation status (e.g. planned, started, completed)               | Percentage of planned resilience and adaptation actions completed on schedule with documented outcomes, lessons learned, and adjustments to future plans                                 | Adaptive          | output              | implementation_management | 1                            | register cluster: Progress in Implementation (A1-01)                                                                                                                                        |
