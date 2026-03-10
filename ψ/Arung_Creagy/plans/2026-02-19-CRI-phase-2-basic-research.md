---
created: 2026-02-19
project: DCCE_CRI
tags:
status: archived
type: "plan "
---
# Session Plan: 19 Feb 2026 - CRI Phase 2 basic research

## Objective

*  Research more case studies and literature to sharpen the tagging dictionary to be backed by good practices and literature 

## Hypothesis
* We could reduce subjectivity of the tagging or categorization process by defining a long-list of nominal indicator names 

## Tasks

*   [ ] draft research questions for ai research tools
*   [ ] wait for the user to point to the sources
*   [ ] find common patterns and finalize the tagging dictionary backed by literature and case studies

## Research prompts (management science + urban resilience governance)

### Set A — Google Deep Research (case studies via general internet search)

1. Find **municipal or city-level urban resilience case studies** that operationalize governance capacity (planning, coordination, finance, service delivery). Extract indicator names, definitions, data types, and evidence; map each to Coping/Adaptive/Transformative.
2. Identify **Southeast Asia or comparable middle-income city** case studies using administrative data for municipal resilience/adaptation measurement; extract indicators, data sources, and limitations.
3. Locate case studies that report **process metrics** (e.g., planning update frequency, inter-agency coordination mechanisms, budget disbursement timeliness) and document how they were measured.
4. Find city resilience programs or initiatives with **performance dashboards** or KPI sets; extract the governance-related indicators and any classification logic.

### Set B — Consensus.ai (literature review focus)

1. Synthesize literature on **local-government governance capacity** or **institutional/implementation capacity** for climate adaptation or DRM. Extract process-oriented indicators (frequency, timeliness, coordination, learning loops) with definitions and data sources.
2. Identify municipal adaptation or urban resilience **indicator frameworks** that provide a taxonomy or tagging logic; list nominal indicator long-lists and decision rules for classification.
3. Find management-science literature on **organizational performance, coordination costs, bureaucratic friction, and public administration performance** that provides measurable proxy indicators applicable at the municipal level.
4. Compare how different frameworks distinguish **process vs stock** indicators and how they justify the classification.

### Hypotheses to test (Consensus.ai)

H1. **Governance-readiness modifiers** (e.g., GRI-style feasibility factors) reduce the gap between technical option ranking and implementability in municipal resilience planning.

H2. **Performance dashboards** with contextual narratives and equity sections improve decision-use and accountability for municipal resilience programs.

H3. **Climate budget tagging** at local-government level increases transparency and alignment between adaptation priorities and actual expenditures.

H4. **Formal coordination mechanisms** (CRO roles, inter-agency working groups) measurably reduce coordination costs and improve cross-sector resilience delivery.

### Management-science keywords to include

- implementation capacity, organizational performance, institutional capacity
- coordination costs, bureaucratic friction, inter-agency coordination
- process metrics, service delivery performance, learning/feedback loops
- public administration, municipal performance management

## Search query templates

- urban resilience index AND municipal AND governance AND indicators
- local government adaptive capacity AND indicator framework AND process metrics
- city resilience governance capacity framework case study
- municipal climate adaptation indicators administrative data
- disaster risk management local government performance indicators
- public administration performance AND municipal AND climate adaptation
- coordination costs AND local government AND resilience

## Inclusion criteria

- Municipal or city-level focus on urban resilience or climate adaptation
- Provides operational indicators or explicit measurement rules
- Governance or institutional capacity emphasized
- Empirical case study or validated framework

## Exclusion criteria

- National-only indices with no municipal breakdown
- Purely conceptual papers without indicators or measurement detail
- Sector-only engineering metrics without governance link

## Extraction schema (per source)

- Citation, region/city, year
- Framework name + goal
- Indicator name (nominal), definition, data type, unit
- Capacity tier mapping (Coping/Adaptive/Transformative)
- Governance function (planning, finance, coordination, service delivery)
- Process vs stock classification
- Evidence type + limitations
---
## Draft tagging dictionary (v0.1)

### Tagging rules (draft)

1. Prefer **process indicators** tied to administrative events (plan revisions, procurement cycles, coordination meetings).
2. Use **mandate-aligned naming** where possible (indicator names reflect legal duties or official KPIs).
3. Allow **readiness modifiers** (e.g., GRI-style feasibility scores) as cross-cutting tags rather than core capacity indicators.
4. Distinguish **process vs stock** explicitly to reduce subjectivity; treat stock indicators as supporting context only.

### Nominal indicator long-list (draft)

| Indicator (nominal) | Definition / signal | Capacity tier | Governance function | Process vs stock | Evidence anchor |
|---|---|---|---|---|---|
| Plan revision cycle | Months since last update of climate/DRM plan | Adaptive | Planning | Process | Planning frequency as resilience metric |
| After-action review completion rate | % of major events with completed after-action reports within set timeframe | Adaptive | Learning / accountability | Process | Learning loops / feedback |
| Cross-department coordination meetings | Number of formal inter-agency coordination meetings per year | Adaptive | Coordination | Process | Coordination cost / alignment |
| Emergency budget disbursement timeliness | Average days to disburse emergency funds after event | Coping | Finance / response | Process | Budget operations timeliness |
| Emergency procurement cycle time | Average days from request to contract award for response projects | Coping | Procurement / response | Process | Bureaucratic friction |
| Climate budget tagging coverage | % of municipal budget items tagged as climate-related | Adaptive | Finance / accountability | Process | CCET / tagging systems |
| Service delivery timeliness | Median processing time for core municipal services | Adaptive | Service delivery | Process | Public administration performance |
| Case throughput rate | Resolved cases per staff per period in key departments | Adaptive | Operations | Process | Performance management proxy |
| Governance readiness score | Feasibility-adjusted score for institutional capacity to deliver options | Transformative | Institutional feasibility | Modifier | GRI / readiness concept |
| Formal coordination mechanism | Existence + activation frequency of CRO or inter-agency taskforce | Transformative | Governance reform | Process | CRO / de-siloing practices |
| Performance dashboard coverage | Public KPI dashboard with context + equity sections | Transformative | Transparency / accountability | Process | Dashboard governance practice |
| Data interoperability score | % of datasets compliant with shared metadata standards | Transformative | Data governance | Process | Metadata / interoperability barriers |
| Policy integration score | Share of sector plans explicitly integrating climate resilience | Adaptive | Policy integration | Process | Cross-sector alignment |
| Community engagement frequency | Number of documented participatory engagements per year | Transformative | Inclusion / legitimacy | Process | Participation / equity emphasis |

## Expected Outcome

* Refined tagging dictionary with long-lists of nominal indicator names and description
