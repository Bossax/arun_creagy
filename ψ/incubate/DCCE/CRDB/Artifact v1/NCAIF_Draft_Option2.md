---
status: current
---
# National Climate Adaptation Information Framework (NCAIF) - Option 2: User-Journey-Based

This artifact outlines the key content and structure for a user-journey-based NCAIF, designed to provide a tailored experience for different user groups.

This version is refined using stakeholder signals about:

- boundary complexity and the need for a “spatial reference” layer
- event-data reality (lag/uncertainty) and post-event reporting workflows
- climate literacy gaps (need for interpretive guidance)
- granularity needs (municipality/sub-district/EA vs province)
- sensitive data handling (classification/aggregation/access pathways)

## 1. Home

The homepage will be designed to quickly direct users to the information that is most relevant to their needs.

### 1.1 Persona entry (“I am a…”) — Phase 1 priority ordering

Primary (Phase 1)

1. **Policy Maker / Planner**
2. **Disaster Management Planner (DDPM / operations support)**
3. **Local Leader / LAO planner**

Secondary (Phase 1)

4. **Researcher / Academia**
5. **Community member / Citizen**

### 1.2 Quick links (always visible)

- **Map Viewer (authoritative layers)**
- **Data Catalog (MVP)**
- **Glossary (plain-language definitions)**
- **Spatial Reference (boundaries + crosswalk guidance)**
- **Export / Printable briefing packs**

### 1.3 Alerts and “event reality” framing

- **Current alerts** can be displayed, but Phase 1 must avoid implying real-time loss & damage.
- For events, show:
  - `data_freshness` / update timestamp
  - known limitations
  - which agency owns the dataset
  - whether this is *warning*, *situation update*, or *post-event assessment*

## 2. For Policy Makers & Planners

This section will provide the information and tools that policy makers and planners need to develop and implement effective adaptation strategies.

*   **Understand the Risks**:
    *   **National & Provincial Risk Assessments**: Comprehensive reports and data on climate risks at both the national and sub-national levels.
    *   **Future Climate Scenarios (Phase 1: curated; Phase 2+: deeper)**: Long-term projections with clear assumptions and acceptance status (cross-ministry).
*   **Develop a Plan**:
    *   **NAP Guidance & Resources**: A toolkit of resources to support the development of National Adaptation Plans.
    *   **Adaptation Option Appraisal Tools**: Tools to help users evaluate and compare different adaptation options.
    *   **Financing & Investment**: Information on funding opportunities and investment frameworks for adaptation projects.
*   **Monitor & Evaluate**:
    *   **M&E Framework**: The national framework for monitoring and evaluating adaptation progress.
    *   **National Progress Dashboard**: A dashboard visualizing key indicators of adaptation progress.

### Phase 1 features (policy/planner)

- **Provincial Risk Profile (flagship)**
  - “one-pager” executive summary + map set
  - includes *limitations statement* and data lineage
- **Budget justification exports**
  - evidence pack aligned to planning/reporting workflows (e.g., e-MENSCR alignment where relevant)
- **Granularity selector with guidance**
  - province vs district vs sub-district vs municipality/LAO (when available)
  - warns about boundary mismatch and crosswalk caveats

### Guidance / literacy scaffolding

- “How to read this” modules:
  - multi-hazard vs single hazard
  - cascading impacts examples
  - what an indicator can/cannot claim

## 3. For Researchers & Academia

This section will provide the data and collaborative tools that researchers need to advance the science of climate adaptation.

*   **Access Data**:
    *   **Open Data Portal (API Access)**: A portal for accessing a wide range of climate-related data via APIs.
    *   **Climate Model Projections**: Access to raw and processed climate model data.
    *   **Socio-Economic Data**: A repository of socio-economic data relevant to vulnerability and adaptation assessment.
*   **Collaborate**:
    *   **Research Network Directory**: A directory of researchers and institutions working on climate adaptation in Thailand.
    *   **Call for Proposals**: Information on research funding opportunities.
*   **Publish**:
    *   **Journal of Climate Adaptation**: A platform for publishing research on climate adaptation.
    *   **Working Paper Series**: A series of working papers on cutting-edge research topics.

## 4. For Communities & Local Leaders

This section will provide practical information and resources to help communities and local leaders build resilience to climate change.

### 4.1 For Local Leaders / LAO planners (Phase 1 primary)

**What’s happening in my area?**

- **Local risk maps (guided)**
  - boundary-aware search (LAO/municipality/sub-district)
  - includes “which boundary is this?” helper + crosswalk notes
- **Post-event situation view (where feasible)**
  - clear lead time and update cadence

**What can we do?**

- **Printable one-page packs** for meetings and budget justification
- **Links to standards / guidelines** (e.g., DLA climate guideline books)

### 4.2 For Communities / Citizens (Phase 1 secondary)

- Plain-language maps + explainers
- “What this means” summaries; avoid technical jargon

## 5. For Disaster Management (DDPM / operations support) (Phase 1 primary)

This section supports early warning interpretation and post-event reporting workflows.

**Prepare and pre-position**

- Risk context dashboard (hazard + exposure/vulnerability layers) with explicit caveats
- Briefing export (PDF/slide-ready)

**Post-event impact assessment**

- Standard event-impact report view (tables + maps)
- Data quality / validation flags (late/incorrect submissions)
- Versioned updates (what changed since last refresh)

**Governance dependencies**

- Event-impact schema governance (standard fields)
- Boundary governance (authoritative units + crosswalk)
- Publishing gates for sensitive data

## 6. Cross-cutting foundations (must be explicit in the UX)

These are not “back-office” topics; they must be visible in the NCAIF experience.

1. **Spatial Reference**: boundary datasets + versioning + guidance
2. **Data Catalog**: minimum metadata + owner pathways + limitations
3. **Glossary**: plain-language definitions + mapping to external terminology
4. **Sensitivity & access**: classification + aggregation rules + access requests
5. **Exportability**: printable briefing packs for decision and budgeting workflows
