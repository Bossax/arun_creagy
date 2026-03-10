---
status: current
last_updated: 2026-03-05
---
# NCAIF Sitemap and Key Content Options

> Purpose of this file: provide **2–3 sitemap alternatives** for selection, and make **MVP placement explicit**.
> 
> MVP references (from workflow patterns/MVP draft):
> - **MVP-1** Briefing Pack Generator (export-first)
> - **MVP-2** Event + Impact schema + Post-event reporting pack
> - **MVP-3** Recommended Dataset Registry (clearinghouse + endorsement)
> - **MVP-4** Uncertainty guidance pack + probabilistic-layer publishing standard
> 
> Cross-cutting modules expected in *all* options:
> - **Data Catalog (MVP)** with preview + limitations + steward/contact
> - **Spatial reference + boundaries** (canonical boundaries + crosswalk guidance)
> - **Publishing workflow** (draft → review → publish) for anything external

## Option 1: Thematic-Based Sitemap [[NCAIF_Draft_Option1]]

This sitemap organizes content around key climate change themes, providing a clear and straightforward navigation structure for users seeking specific information.

*   **Home**
    *   National Climate Risk Overview
    *   Latest Updates and News
    *   Featured Content
*   **Climate Risks & Impacts**
    *   By Hazard
        *   Floods
        *   Droughts
        *   Sea Level Rise
        *   Extreme Heat
    *   By Sector
        *   Agriculture
        *   Water Resources
        *   Public Health
        *   Tourism
        *   Infrastructure
    *   Provincial Risk Profiles
*   **Adaptation Planning**
    *   National Adaptation Plan (NAP)
    *   Adaptation Options Library
        *   Nature-Based Solutions
        *   Engineering Solutions
        *   Policy & Governance
    *   Case Studies & Best Practices
    *   Decision Support Tools
*   **Data & Resources**
    *   Data Catalog
    *   Map Viewer
    *   Publications & Reports
    *   Glossary
*   **About NCAIF**
    *   Mission & Vision
    *   Partners
    *   Contact Us

**Where the MVPs live (explicit placement)**

- **MVP-1 (Briefing packs):** under **Climate Risks & Impacts → Provincial Risk Profiles** and **Adaptation Planning → Decision Support Tools** (exportable packs)
- **MVP-2 (Post-event reporting):** add a new item under **Climate Risks & Impacts**:
  - **Post-event impact assessment** (standard report view + quality flags + revision history)
- **MVP-3 (Recommended Dataset Registry):** under **Data & Resources → Data Catalog** as a prominent “Recommended baselines” section
- **MVP-4 (Uncertainty guidance):** under **Data & Resources**:
  - **How to interpret probabilistic layers** (standard wording + examples of misuse)

---

## Option 2: User-Journey-Based Sitemap [[NCAIF_Draft_Option2]]

This sitemap is designed to guide different user personas through their specific information needs and decision-making journeys, providing a more tailored and actionable user experience.

*   **Home**
    *   I am a... (Policy Maker/Planner; Disaster Management; Local Leader/LAO; secondary: Researcher; Community)
    *   Quick Links: Map Viewer, Data Catalog (MVP), Glossary, Spatial Reference, Export/Printable packs
    *   Current Climate Alerts (with “event reality” framing: freshness + limitations)
*   **For Policy Makers & Planners**
    *   **Understand the Risks:**
        *   National & Provincial Risk Assessments
        *   Future Climate Scenarios
    *   **Develop a Plan:**
        *   NAP Guidance & Resources
        *   Adaptation Option Appraisal Tools
        *   Financing & Investment
    *   **Monitor & Evaluate:**
        *   M&E Framework
        *   National Progress Dashboard
*   **For Researchers & Academia**
    *   **Access Data:**
        *   Open Data Portal (API Access)
        *   Climate Model Projections
        *   Socio-Economic Data
    *   **Collaborate:**
        *   Research Network Directory
        *   Call for Proposals
    *   **Publish:**
        *   Journal of Climate Adaptation
        *   Working Paper Series
*   **For Local Leaders / LAO planners**
    *   **What's Happening in My Area?:**
        *   Local Risk Maps
        *   Community Vulnerability Assessments
    *   **What Can We Do?:**
        *   Community-Based Adaptation Toolkit
        *   Funding Opportunities for Local Projects
        *   Local Success Stories
*   **Explore Our Work**
    *   Projects & Initiatives
    *   News & Events
    *   About Us

*   **For Disaster Management (DDPM / operations support)**
    *   Prepare & pre-position (risk context dashboard + briefing exports)
    *   Post-event impact assessment (standard report view + quality flags + versioned updates)
    *   Governance dependencies (event schema, boundaries, publishing gates)

**Where the MVPs live (explicit placement)**
- **MVP-1 (Briefing packs):**
  - Home → Quick Links (“Briefing packs”)
  - For Policy Makers & Planners → Understand the Risks / Develop a Plan (downloadable packs)
  - For Disaster Management → Prepare & pre-position (briefing exports)
- **MVP-2 (Post-event reporting):**
  - For Disaster Management → Post-event impact assessment
  - (Optional cross-link) For Policy Makers & Planners → Monitor & Evaluate (event summary packs)
- **MVP-3 (Recommended Dataset Registry):**
  - Home → Quick Links (“Recommended baselines”)
  - For Researchers & Academia → Access Data (recommended baselines + provenance)
- **MVP-4 (Uncertainty guidance):**
  - Home → Quick Links (“How to read probabilistic maps”) and within each hazard/scenario page

---

## Option 3: Hybrid (Workflow-pattern-first) — “Start with what you need to do”

This option is designed to satisfy both:

1) users who think in **workflows** ("I need a briefing pack", "I need post-event reporting"), and
2) users who want to **browse thematically** (NCAIF stages / domains).

### Top-level navigation

* **Home**
  * "I need to…" (workflow entry)
  * "Browse topics" (thematic entry)
  * Quick Links: Data Catalog (MVP), Recommended Baselines, Spatial Reference, Glossary

* **Do (Workflow entry)**
  * **W1 — Generate a briefing pack (MVP-1)**
    * Provincial risk profile pack <!--note: translate the spatial risk map into communication packs with highlighted exposed and vulnerable entities -->
    * LAO/municipality budget justification pack <!--comment:  unavailable data-->
    * Corridor/infrastructure exposure pack <!--comment: unavailable data-->
    * Export templates + assumptions + limitations (3-depth wording) 
  * **W2 — Post-event assessment (MVP-2)**
    * Event registry + impact observation template
    * Standard post-event report + revision history + validation flags
  * **W3 — Find the official dataset (MVP-3)**
    * Search candidates → compare differences → endorse “recommended baseline” → keep history
  * **W4 — Use probabilistic layers safely (MVP-4)**
    * Required metadata fields + interpretation standard + examples of common misuse

* **Browse (Thematic entry)**
  * Stage 1: Meteorology & Climate
  * Stage 2: Risk & Impact Assessment
  * Stage 3: Loss & Damage
  * Stage 4: Adaptation Measures
  * Stage 5: Results & M&E

* **Data & Governance (visible, not hidden)**
  * Data Catalog (preview + owner + cadence + limitations)
  * Spatial reference (canonical boundaries + crosswalk guidance)
  * Publishing workflow (draft → review → publish)
  * Data classification + access paths (Open Data via data.go.th; Non-open via GDX)

**Why this option works for FGD2**

- It makes **workflow patterns** concrete for discussion (what do we ship first?), while keeping the thematic “NCAIF stages” as a stable backbone.
