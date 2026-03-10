---
type: knowledge_artifact
status: current
version: 1.1
created: 2026-02-19
last_updated: 2026-02-27
project:
  - DCCE_CRI
title: CRI Phase 2 Capacity Tagging Dictionary
sticker: emoji//1f351
---

# CRI Phase 2 Capacity Tagging Dictionary

## Purpose

Provide a transparent, literature-backed tagging dictionary for classifying municipal indicators into Coping, Adaptive, and Transformative capacity tiers.

>[!important] This dictionary now explicitly supports a **two-speed measurement stance**:
> - **Baseline (deliverable now):** rely on **secondary/admin data first**, using proxy/stock/binary indicators when process-quality signals are not available.
> - **Target (upgrade path):** prioritize **process indicators** tied to administrative events (plan revisions, procurement cycles, coordination cadence) when/where event logs can be accessed later.

This aligns the dictionary with the practicality strategy in [`CRI_Urban_Resilience_Frameworks_Analysis.md`](CRI_Urban_Resilience_Frameworks_Analysis.md).

## Scope
1. Municipal urban resilience and governance indicators
2. Administrative/statistical data as the baseline measurement regime
3. Process metrics as the target measurement regime (when event/process logs become feasible)
4. Supports CRI Phase 2 capacity profiling

## Sources used
1. External / evidence anchors:
	- [[Case studies of urban resilience indicators]]
	- [[Process-based indicators for urban resilience - consensus.ai]]
2. Internal alignment reference:
3. Practicality stance and “two-speed” approach: [[CRI_Urban_Resilience_Frameworks_Analysis]]
## Tagging rules (v1.1)
1. **Two-tier measurement is mandatory:** every conceptual indicator should have a Baseline proxy (secondary-data measurable) and an optional Target process metric (event-log measurable).
2. **Baseline-first (practicality):** if process quality is not measurable, use the best available proxy/stock/binary indicator and label it explicitly as **Baseline proxy**.
3. **Process remains the north star:** keep process-quality definitions in the dictionary as **Target** so the measurement roadmap stays coherent.
4. Use **mandate-aligned naming** where possible (indicator names reflect legal duties or official KPIs) to reduce political contestability.
5. Allow **readiness modifiers** (e.g., feasibility or governance-readiness factors) as cross-cutting tags rather than core capacity indicators.
6. If a single indicator spans multiple functions, assign the **primary governance function** and document secondary linkages in notes.
7. Record a **data-richness/confidence score (0–3)** for the Baseline proxy to make missingness and measurement strength explicit.

## Capacity tier definitions (operational)
- **Coping:** Immediate response and stabilization capacity; short-term emergency management and relief.
- **Adaptive:** Medium-term adjustment and learning; planning, resource allocation, and iterative improvement.
- **Transformative:** Structural reform and system change; cross-sector integration, governance redesign, and long-term strategic shifts.

## Nominal indicator long-list (v1.1)

### Data-richness / confidence scale (Baseline proxy)

This score is a **pre-data-inventory estimate** of how feasible it is to measure the Baseline proxy using typical secondary/admin sources.
- **0** = Not realistically measurable via existing secondary/admin data without event-level logs or new primary collection.
- **1** = Partially measurable or highly inconsistent; requires substantial interpretation/proxying.
- **2** = Measurable with reasonable effort via existing reports/registries/web presence; still needs normalization/QA.
- **3** = Measurable via structured, regularly reported fields in known pipelines (high repeatability).


| Indicator (concept)                      | Baseline proxy (secondary/admin data first)                                                                          | Baseline data-richness / confidence (0–3) | Target (process-quality metric)                                               | Capacity tier  | Governance function           | Evidence anchor                                                                                 | Notes / upgrade path                                                                                               |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ----------------------------------------: | ----------------------------------------------------------------------------- | -------------- | ----------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Plan revision cycle                      | Plan exists + last revised year (or last published version)                                                          |                                         2 | Months since last update of climate/DRM plan; update cadence over N years     | Adaptive       | Planning                      | City Resilience Framework – Resilient Cities Network                                            | If revision timestamps are absent, treat “exists” as Baseline and keep cadence as Target for roadmap.              |
| After-action review completion rate      | AAR mechanism exists (policy/guideline/template) + count of drills/exercises reported (if any)                       |                                         0 | % of major events with AAR completed within timeframe                         | Adaptive       | Learning / accountability     | Feldmeyer et al. 2019. Indicators for Monitoring Urban Climate Change Resilience and Adaptation | Baseline likely collapses to “exists”; keep as a Target indicator to drive future event-log requirements.          |
| Cross-department coordination meetings   | Formal coordination body exists (committee/taskforce) + publicized meeting minutes (if available)                    |                                         1 | # formal inter-agency coordination meetings per year (with attendance/agenda) | Adaptive       | Coordination                  | Institutionalizing Urban Resilience – Urban.org                                                 | If only existence is known, baseline is binary; upgrade requires meeting logs.                                     |
| Emergency budget disbursement timeliness | Emergency fund/reserve exists; annual allocation size; emergency spending line items (if available)                  |                                         1 | Average days to disburse emergency funds after event                          | Coping         | Finance / response            | Goonesekera & Olazabal 2022. Climate adaptation indicators and metrics                          | Upgrade requires disbursement timestamps (event date, approval date, payment date).                                |
| Emergency procurement cycle time         | Emergency procurement policy exists; procurement budget allocated; procurement “fast track” clause exists            |                                         0 | Days from request to award for emergency procurement                          | Coping         | Procurement / response        | Kenney & Gerst 2021. Synthesis of indicators, datasets, and frameworks                          | Without transaction timestamps, keep as Target only; baseline is policy existence.                                 |
| Climate budget tagging coverage          | Climate budget tagging policy exists; # items tagged (if counts exist)                                               |                                         1 | % of municipal budget items tagged as climate-related                         | Adaptive       | Finance / accountability      | Climate Change Expenditure Tagging – NICCDIES                                                   | Baseline can start with “policy exists”; upgrade requires consistent tagging field + denominator.                  |
| Service delivery timeliness              | Service coverage proxies (service availability, staffing levels, complaint counts)                                   |                                         0 | Median processing time for core municipal services                            | Adaptive       | Service delivery              | Serdar et al. 2021. Urban Transportation Networks Resilience                                    | If only service coverage exists, interpret as capacity context; upgrade requires case management timestamps.       |
| Case throughput rate                     | Aggregate resolved-case totals (if reported) + staffing levels (if reported)                                         |                                         0 | Resolved cases per staff per period (department-level)                        | Adaptive       | Operations                    | Serdar et al. 2021. Urban Transportation Networks Resilience                                    | Throughput is highly diagnostic but log-intensive; baseline may not be possible without structured case systems.   |
| Governance readiness modifier            | Composite proxy from verifiable items (strategy exists, org unit exists, budget allocated, basic data systems exist) |                                         2 | Feasibility-adjusted readiness score with explicit rubric and documentation   | Transformative | Institutional feasibility     | Integrative Decision-Making Framework for Sustainable Urban Development (MDPI 2026)             | Keep as cross-cutting modifier; ensure rubric is published for defensibility.                                      |
| Formal coordination mechanism            | CRO/taskforce exists; mandate documented; membership list exists                                                     |                                         2 | Activation frequency + outputs (meetings/year, joint projects/year)           | Transformative | Governance reform             | Institutionalizing Urban Resilience – Urban.org                                                 | Baseline captures structure; upgrade captures lived functionality.                                                 |
| Performance dashboard coverage           | Public dashboard exists (URL) and shows KPIs                                                                         |                                         2 | Dashboard includes context + equity sections; update cadence measured         | Transformative | Transparency / accountability | 8 Local Government Public Dashboard Examples – Envisio                                          | Baseline is observable via web/portal; upgrade requires content rubric + update logs.                              |
| Data interoperability score              | Metadata standard exists; data catalog exists; interoperability policy exists                                        |                                         1 | % datasets compliant with metadata standard                                   | Transformative | Data governance               | Prioritizing Core Data Sets for Smart City Governance: Evidence (MDPI)                          | Baseline is policy/structure; upgrade requires dataset registry + compliance checks.                               |
| Policy integration score                 | Climate integrated in key sector plan(s) (binary per sector)                                                         |                                         1 | Share of sector plans integrating climate resilience                          | Adaptive       | Policy integration            | Kauffman & Hill 2021. Climate Change, Adaptation Planning and Institutional Integration         | Baseline can be checklist-style; upgrade requires plan inventory + consistent scoring rubric.                      |
| Community engagement frequency           | Participation mechanism exists; engagement activities documented in annual report                                    |                                         1 | # engagements/year with attendance + feedback loop evidence                   | Transformative | Inclusion / legitimacy        | Inclusive engagement for equitable resilience: community case study insights                    | Baseline may be “reported engagements”; upgrade requires consistent event logs and minimum documentation standard. |

## Notes on use

- Use this dictionary for **baseline-first tagging** of LPA and other administrative indicators, while preserving target process metrics as the roadmap.
- For every indicator used in scoring/profiling, state explicitly whether you are using the **Baseline proxy** or the **Target process metric**.
- Always carry the **data-richness/confidence score (0–3)** alongside the Baseline proxy to avoid implying false precision.
- Where Baseline proxies are binary/stock indicators, treat results as **profiles + gap diagnostics**, not definitive measures of process quality (consistent with the stance in [`CRI_Urban_Resilience_Frameworks_Analysis.md`](CRI_Urban_Resilience_Frameworks_Analysis.md:1)).
- Observations + further refinement ideas are tracked separately in [`CRI_Capacity_Tagging_Dictionary_Observations.md`](../notes/CRI_Capacity_Tagging_Dictionary_Observations.md:1).
