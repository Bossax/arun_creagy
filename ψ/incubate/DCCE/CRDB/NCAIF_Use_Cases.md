---
status: current
tags:
  - NCAIF
  - use-cases
created: 2026-02-26
last_updated: 2026-03-04
project:
  - DCCE_CRDB
type:
  - artifact
---
# NCAIF Use Cases (Draft) — consultation + stakeholder interviews

## Purpose

Translate interview/workshop observations into **concrete NCAIF user journeys** and **data system requirements** that can guide:

- Phase 1 NCAIF “flagship products”
- CDM prioritization (which entities/relationships must exist first)
- Data governance phasing (what governance is required *just-in-time* to ship Phase 1)

## Source material

- Workshop notes: [`src/02_Meeting/2026-02-19 - Data provider consultation workshop.md`](src/02_Meeting/2026-02-19%20-%20Data%20provider%20consultation%20workshop.md:1)
- Stakeholder interview summaries:
  - DLA: [`src/01_Projects/2025-11_DCCE-CRDB/sources/Interview result/Interview Summary - DLA.md`](src/01_Projects/2025-11_DCCE-CRDB/sources/Interview%20result/Interview%20Summary%20-%20DLA.md:1)
  - MSDHS: [`src/01_Projects/2025-11_DCCE-CRDB/sources/Interview result/Interview Summary - MSDHS.md`](src/01_Projects/2025-11_DCCE-CRDB/sources/Interview%20result/Interview%20Summary%20-%20MSDHS.md:1)
  - NSO: [`src/01_Projects/2025-11_DCCE-CRDB/sources/Interview result/Interview Summary - NSO.md`](src/01_Projects/2025-11_DCCE-CRDB/sources/Interview%20result/Interview%20Summary%20-%20NSO.md:1)
  - OTP: [`src/01_Projects/2025-11_DCCE-CRDB/sources/Interview result/Interview Summary - OTP.md`](src/01_Projects/2025-11_DCCE-CRDB/sources/Interview%20result/Interview%20Summary%20-%20OTP.md:1)
  - DDPM: [`src/01_Projects/2025-11_DCCE-CRDB/sources/Interview result/Interview Summary DDPM.md`](src/01_Projects/2025-11_DCCE-CRDB/sources/Interview%20result/Interview%20Summary%20DDPM.md:1)
  - NESDC: [`src/01_Projects/2025-11_DCCE-CRDB/sources/Interview result/Interview Summary - NESDC.md`](src/01_Projects/2025-11_DCCE-CRDB/sources/Interview%20result/Interview%20Summary%20-%20NESDC.md:1)
  - NXPO: [`src/01_Projects/2025-11_DCCE-CRDB/sources/Interview result/Interview Summary - NXPO.md`](src/01_Projects/2025-11_DCCE-CRDB/sources/Interview%20result/Interview%20Summary%20-%20NXPO.md:1)
  - Thai Bankers' Association (TBA): [`src/01_Projects/2025-11_DCCE-CRDB/sources/Interview result/Interview Summary - Thai Bankers' Association.md`](src/01_Projects/2025-11_DCCE-CRDB/sources/Interview%20result/Interview%20Summary%20-%20Thai%20Bankers'%20Association.md:1)

Additional internal requirements signal:

- DCCE internal Focus Group Discussion #1 (FGD1): [`src/01_Projects/2025-11_DCCE-CRDB/output/FGD 1 result.md`](src/01_Projects/2025-11_DCCE-CRDB/output/FGD%201%20result.md:1)

## 👁️ Observations (raw → implications)

### FGD1 internal feedback: usability, language, workflow, and QA/QC

Key FGD1 signals to carry into FGD2 decisions (summarized from Table 2 in [`src/01_Projects/2025-11_DCCE-CRDB/output/FGD 1 result.md`](/01_Projects/2025-11_DCCE-CRDB/output/FGD%201%20result.md)):

- **Terminology mismatch / missing definitions** across agencies → Phase 1 must ship a **glossary + definitions authority** (even if minimal).
- **Language too technical** for public/local users → Phase 1 needs **plain-language explanations** and “how to read this” guidance.
- **Data latency / incomplete data / format mismatch** → Phase 1 must label **timeliness, completeness, and constraints**; design for imperfect inputs.
- **Lack of central QA/QC SOP** and unclear responsibility → Phase 1 governance must define **minimum QA/QC checkpoints + accountable roles**.
- **Need 3 information levels** (policy / practitioners / public) → Phase 1 IA/UX should be able to **present the same content at 3 depths**.
- **Two-way communication desired** (FAQ/chatbot) → Phase 1 should include at least a **feedback channel** and an FAQ pattern (chatbot can be roadmap).
- **Want preview-before-link/download** → Phase 1 catalog must include **dataset preview** (schema + sample + limitations).
- **PR workflow bottleneck** (need internal review before publishing; PR waits for platform updates) → Phase 1 publishing should include a **staging/review workflow** (draft → review → publish), or at minimum an agreed operating procedure.

### ⏲️ Data timeliness and “event reality”

- **DDPM** event impact data is aggregated from **LAO**, with ~**1 week lead time** post-event.
- Variables observed: where, when, affected population, affected key assets (quantities). Economic damage estimation is inconsistent and depends on LAO reference cost inventories.

Implications:
- Phase 1 cannot assume real-time “loss & damage” numbers; it should support a **post-event assessment workflow** and clearly label timeliness/uncertainty.
- A **standard event-impact schema** and a **reference-cost registry** become governance priorities.

Additional interview signals:
- Disaster declaration is triggered when **LAO capacity is exceeded** (not merely hazard occurrence) → event concepts must include *operational threshold/context* (DDPM).
- Local reporting is **incentivized by relief disbursement**; late/incorrect data entry is common → Phase 1 should plan for **screening/validation** and transparent caveats (DDPM).

### 🗺️ Spatial units and boundary confusion
- Administrative units are used for emergency response; LAO boundaries relate to service delivery.
- Community boundaries are not yet available (in progress by DPT); question raised about census-tract equivalents.

Implications:
- NCAIF needs an explicit **“spatial reference” layer**: authoritative boundary datasets, versioning, and usage guidance (which unit for which workflow).
- CDM must handle **multiple boundary systems** and crosswalks.

Additional interview signals:
- Users need resolution aligned with **budget holders** (municipality / LAO) and **service delivery** boundaries (DLA, MSDHS).
- NSO’s **Enumeration Area (EA)** concept provides an option for consistent small-area baselines where appropriate (NSO).

### Multi-hazard and cascading impacts literacy gap

- Reported misunderstanding of **multi-hazards** and **cascading impacts**.

Implications:
- NCAIF should include interpretive guidance (not only data): explanations, examples, and “how to read this map/dashboard.”
- “Cascading impacts” should be a named concept in the glossary and supported as a tagging/relationship pattern.

Additional interview signals:
- Local implementers often blur **“disaster” vs “climate change”** → the portal should explicitly offer *plain-language pathways* and examples (MSDHS).

### Health impacts: heat morbidity/mortality
- Heat-related morbidity/mortality: “not really has the database.”
- Attribution of cause of mortality is difficult.

Implications:
- Phase 1 should treat heat-health as a **data gap + roadmap item** (inventory data owners, feasibility, privacy/legal constraints), not a full KPI product.

Additional interview signals:

- MSDHS needs 2–5 year **habitability/relocation timelines** (forecast) more than just historic stats → Phase 2+ requirement for projections + scenario communication (MSDHS).

### 🙎Candidate data partners / co-producers
- **LLD**: administrative data can reach **tambon** level.
- **GISTDA**: province/tambon layers; multi-layer datasets that could support loss & damage estimation.
- **MSDHS (พม)**: disabled population point data.
- **DDPM**: risk-based early warning.
- **DGA**: Digital Government Act context (status unclear).

Implications:
- Phase 1 should prioritize “connectable” datasets with clear stewardship and boundary compatibility.
- Data governance must include data-sharing/legal readiness (especially for sensitive population data).

Additional interview signals:
- NSO will **link** to source data rather than duplicate if already in the government data catalog → NCAIF can work as a catalog + linking hub, not a data warehouse (NSO).
- OTP needs **authoritative long-term projections** accepted across ministries, to avoid re-litigating forecasts annually (OTP).

### Data discovery and metadata pain
- Staff waste time searching multiple websites and lack data dictionaries/technical metadata (MSDHS).

Implications:
- The Phase 1 “Data Catalog” is not optional. It must expose **minimum metadata**, human-readable definitions, and contact/owner pathways.
- Governance gates should require a **limitations statement** (what is missing, what is uncertain, and what can’t be inferred).

Additional internal (FGD1) requirements for the catalog experience:

- **Preview** before connecting/downloading (schema/snippet + owner/contact + update cadence)
- **Audience tiering**: policy vs practitioners vs public

### Budgeting and policy constraints

- LAOs may be forced to drain accumulated funds for emergency response, leaving no resources for proactive resilience (DLA).
- Adaptation engineering costs inflate under long-horizon uncertainty; budgets often rejected (OTP).

Implications:

- NCAIF must support “**budget justification**” outputs (simple one-pagers, exportable evidence packages) rather than only exploratory maps.
- Phase 1 products should be designed as **decision-support packaging** (printable/exportable, with metadata/caveats).

### Privacy / legal / accountability constraints

- Individual-level social welfare data exists but requires careful handling; sharing during crises occurs but is sensitive (MSDHS).
- Statistics Act constraints and hierarchy-of-law conflicts can block inter-agency data requests without MOUs (NSO).

Implications:

- Define a Phase 1 stance for **aggregation rules** and **access pathways**.
- Treat “sensitive data onboarding” as a governance work package with explicit approvals.

Additional interview signals:

- Publishing/predictive-data risk: agencies fear legal/social backlash if a forecast is “wrong” → Phase 1 must be explicit about **uncertainty communication**, **limitations statements**, and **accountability protections** (NXPO).

Additional internal (FGD1) requirement:

- Make “what we can/can’t publish” explicit so comms/PR can operate safely (supports a staged publishing workflow).
---
## 🔨Use cases (draft)

### UC-01 — Post-event impact & Loss/Damage assessment (DDPM + LAO)

**Primary user**: DCCE analyst + DDPM focal point
**Trigger**: A flood/drought/heat event occurs; agencies need consolidated, comparable post-event reporting.

**User journey (minimum)**
1. Select event (where/when; hazard type).
2. Review affected population + affected assets (quantities) + data freshness.
3. Compare impacts across provinces/districts using consistent boundary units.
4. Export a standardized report (tables + maps) with caveats.
5. If publishing externally, route through a **reviewable publishing state** (draft → review → publish) or capture the operating rule.

**Notes from interviews**
- Treat “disaster” as an **operational state**: LAO capacity exceeded triggers declaration (DDPM).
- Expect **lag and noise** in early reports; include validation flags and update history (DDPM).

**Data needs**
- Event registry (ID, hazard type, start/end time, affected areas)
- Administrative boundaries (authoritative, versioned)
- Impact observations (population, assets, damages)
- Reference cost inventories (per LAO / harmonized)

**Key gaps / governance needs**
- Standard schema for impact reporting
- Reference-cost governance (definitions, version control)
- Metadata on timeliness + uncertainty

**Typology tags (actionable climate information)**
- Use: Plan; Motivate & communicate; Fund
- Information: Detailed data & results; Data improvement & guidance

---
### UC-02 — Risk context for early warning, pre-positioning, and preparedness (DDPM)

**Primary user**: Disaster management planner / operations support

**Goal**: Combine hazard context + exposure/vulnerability layers to support early warning interpretation and resource staging.

**User journey (minimum)**
1. Select hazard type + time window.
2. See authoritative boundary-aligned layers + known limitations.
3. Overlay vulnerable groups / critical assets (as permitted).
4. Export a briefing pack for decision-makers.

**NCAIF product shape (Phase 1 feasible)**
- “Risk context” map + briefing export
- Explicit **interpretive guidance** for multi-hazard + cascading impacts

**Governance needs**
- Boundary governance (what units are valid for operational use)
- Publishing caveats + timeliness labeling
- Minimum QA/QC + validation flags for known failure modes (late reports, wrong categories, revision history)

**Typology tags (actionable climate information)**
- Use: Plan; Take action
- Information: Detailed data & results; Data improvement & guidance

---
### UC-03 — Provincial risk profile for policy and planning (NCAIF flagship) 


**Primary user**: Policy maker / provincial planner
**Goal**: Obtain a curated, readable “one-pager” + map set describing priority hazards, exposure, vulnerable groups, and adaptation context.
**Data needs**
- Hazard layers (current and projected) 
- Socio-economic and vulnerable group indicators (e.g., disability point data where allowed)
- Critical infrastructure / key assets

**Governance needs**
- Minimum metadata standard for “published” indicators
- Simple quality flags and update cadence

**FGD1 alignment notes**

- Present the profile at **3 depths** (executive/policy → implementers → public) with consistent definitions.

**Typology tags (actionable climate information)**
- Use: Understand; Motivate & communicate; Plan
- Information: Broad trends & patterns; Detailed data & results

<!--note: this is the spatial climate risk map of DCCE (version 2 just released)--> 
<!--todo: assess the gaps by interviewing actual users-->

### UC-03b — Municipality/LAO budget justification pack (DLA)

**Primary user**: Municipality/LAO planner + DLA advisor
**Goal**: Produce an evidence pack that links local risk exposure to budget justification (including alignment with national planning/reporting systems).

**User journey (minimum)**
1. Select LAO/municipality.
2. View risk layers + affected assets/people (bounded by provenance/quality).
3. Pull standard indicator snippets and assumptions.
4. Export a one-page justification aligned with planning systems (e.g., e-MENSCR links where applicable).

**Governance needs**
- Canonical boundary + crosswalk guidance (admin vs LAO) <!--note: it's the single, most trusted source for defining geographical or administrative limits within a system-->
- Minimum published metadata + “limitations statement”

**FGD1 alignment notes**

- Ensure outputs are understandable to non-technical audiences and can be used offline (printable/exportable).

**Typology tags (actionable climate information)**
- Use: Fund; Plan
- Information: Detailed data & results; Data improvement & guidance

<!--note:  This use case seems to be answered by ADPC's data platform developed under #UNDP-BTR project --> 
### UC-04 — Vulnerable group mapping & service targeting (MSDHS + DCCE)

**Primary user**: Social protection planner
**Goal**: Identify high-risk areas with concentrations of vulnerable groups.

**Constraints**
- Potentially sensitive personal data → requires classification policy, aggregation rules, and clear access control.

**Interview-driven details**
- Need subgroup breakdown (children, elderly, disability categories, gender/equality needs) at municipality/sub-district resolution (MSDHS).
- Operational sharing can happen during crises, but must have clear accountability and access rules (MSDHS).

**Typology tags (actionable climate information)**
- Use: Plan; Take action
- Information: Detailed data & results; Data improvement & guidance

### UC-05 — Heat-health surveillance roadmap (gap → plan)

**Primary user**: Public health / DCCE coordination
**Goal**: Establish what’s needed to measure heat morbidity/mortality credibly.

**Phase 1 deliverable**
- Data gap register + candidate owners + feasibility notes (privacy, attribution limitations)

**Typology tags (actionable climate information)**
- Use: Understand; Plan
- Information: Data improvement & guidance

### UC-06 — Cascading impacts explainer and analysis entry point

**Primary user**: Mixed (policy + analysts)

**Goal**: Reduce misunderstanding by providing:

- A curated explainer (examples: flood → transport disruption → supply chain impacts)
- A way to tag/link datasets and narratives by cascading pathways

**FGD1 alignment notes**

- Make the explainer usable as PR content (clear definitions + ready-to-share visuals), with a review workflow.

**Typology tags (actionable climate information)**
- Use: Understand; Motivate & communicate
- Information: Broad trends & patterns; Data improvement & guidance

### UC-07 — Infrastructure disruption & critical corridor exposure (OTP)

**Primary user**: Infrastructure planner / transport resilience analyst
**Goal**: Understand how hazards translate into disruption risk for transport corridors and critical assets.

**Notes from interviews**
- OTP models at very high resolution (km markers, poles); standard national maps are too coarse (OTP).

**Phase 1 stance**
- Start with a **catalog + showcase** of sectoral exposure datasets and methods; do not promise nationwide high-resolution modeling.

**Governance needs**
- Provenance + model assumptions
- Cost/uncertainty communication for budget allocators

**Typology tags (actionable climate information)**
- Use: Plan; Fund
- Information: Detailed data & results; Data improvement & guidance

### UC-08 — Statistical baselines and thematic tagging (NSO)

**Primary user**: Data cataloger / national statistics integrator
**Goal**: Provide consistent baselines and discoverability via tagging frameworks (FDES/GSBPM-style QA).

**Phase 1 stance**
- Treat NSO outputs as baseline references; link rather than duplicate where possible.

**Governance needs**
- Metadata completeness requirements
- Privacy-preserving aggregation guidelines

**Typology tags (actionable climate information)**
- Use: Understand; Inform
- Information: Data improvement & guidance

---

### UC-09 — “True” economic Loss & Damage estimation (NESDC)

**Primary user**: NESDC policy analyst / macroeconomic forecaster; DCCE analyst supporting national planning

**Goal**: Close the gap between **relief payouts** and **true economic loss** (direct + business interruption) so national planning and evaluation can use comparable, decision-ready values.

**User journey (minimum)**
1. Select event or time period (where/when; hazard type).
2. Pull baseline economic context (agriculture yields, establishments, tourism accounts, etc.).
3. Estimate direct losses (assets) + **indirect losses** (opportunity/business interruption) with transparent assumptions.
4. Produce an exportable brief: “relief vs true loss” with uncertainty and caveats.

**Notes from interviews**
- DDPM statistics describe compensation payouts, not economic loss; indirect losses are hardest to measure and often excluded due to lack of data (NESDC).

**Data needs**
- Event/impact schema (aligned with UC-01)
- Economic baseline datasets (sectoral accounts, crop yields, establishments)
- Assumption registry (methods, coefficients) + versioning

**Key gaps / governance needs**
- “Economic L&D” methodology guardrails (assumptions, uncertainty handling)
- Clear provenance for any damage/loss coefficients

**Typology tags (actionable climate information)**
- Use: Fund; Plan; Motivate & communicate
- Information: Detailed data & results; Data improvement & guidance

---

### UC-10 — Baseline verification / “single source of truth” (NXPO)

**Primary user**: Policy integrator / standards convenor; DCCE central data + governance roles

**Goal**: Reduce fragmentation by defining how DCCE (and partners) will:

- declare/endorse baseline datasets (what is “official enough”)
- publish uncertainty and limitations safely
- operate a **clearinghouse model** (linking to authoritative sources) where full central hosting is unrealistic

**User journey (minimum)**
1. Identify a high-demand variable (e.g., flood hazard baseline; population baseline).
2. Compare competing sources; record differences, methods, and intended use constraints.
3. Publish a DCCE-endorsed “recommended baseline” and usage guidance.
4. Maintain an audit trail of changes (versions + rationale).

**Notes from interviews**
- Verification is the core missing function: multiple agencies produce different numbers; nobody wants liability (NXPO).
- Suggests a Climate-ADAPT-style clearinghouse and locked/automated publishing to reduce personal liability (NXPO).

**Data needs**
- Metadata + provenance + versioning for endorsed baselines
- Limitation/uncertainty statements as first-class fields

**Key gaps / governance needs**
- Decision-rights model for endorsements (who can declare a baseline “recommended”)
- Accountability and safe-publishing workflow

**Typology tags (actionable climate information)**
- Use: Understand; Plan
- Information: Data improvement & guidance

---

### UC-11 — Financial sector physical risk analysis & climate stress testing (TBA)

**Primary user**: Bank risk analyst; regulator-facing reporting teams; (secondary) DCCE providing foundational datasets

**Goal**: Support portfolio-level analysis by providing (or enabling access to) foundational datasets + consistent guidance on uncertainty interpretation.

**User journey (minimum)**
1. Select portfolio assets and geocode/align to a spatial reference.
2. Select hazard scenario (historic + probabilistic + projected).
3. Estimate exposure and losses (depth/duration where applicable) using consistent damage functions.
4. Produce a stress-testing output with uncertainty-safe interpretation notes.

**Notes from interviews**
- Asset-level granularity is required; index maps are insufficient (TBA).
- Analysts often misread probabilistic maps deterministically → need standardized uncertainty guidance (TBA).
- Damage functions and ISIC/sector mapping are major gaps (TBA).

**Phase 1 stance**
- DCCE should not promise to build bank-grade models; Phase 1 can deliver a **catalog + endorsed foundational layers** + uncertainty guidance, and register partner datasets (e.g., HII/GISTDA).

**Data needs**
- Authoritative spatial references (boundaries/crosswalks)
- Hazard layers with probability semantics
- Damage-function registry (even if placeholder + roadmap)
- Sector taxonomy crosswalks (ISIC ↔ domestic sectors)

**Key gaps / governance needs**
- Uncertainty communication standard for published hazard layers
- Provenance and update cadence for foundational datasets

**Typology tags (actionable climate information)**
- Use: Plan; Fund
- Information: Detailed data & results; Data improvement & guidance

## Cross-cutting “must decide” items for FGD2
- Which boundary system is canonical for Phase 1 reporting (and how to crosswalk others)
- Whether Phase 1 includes *any* persona-based navigation (hybrid NCAIF)
- Minimum published metadata set for NCAIF datasets/products
- Approach to sensitive datasets (classification + aggregation + legal/accountability pathway)

Additional “must decide” items (added from March 2026 interviews):

- “Clearinghouse vs repository” stance for Phase 1 (link-first vs host-first)
- Who (role/title) can endorse a “recommended baseline” and publish it with accountability protections
- Uncertainty interpretation standard for probabilistic layers (to avoid deterministic misuse)

Additional cross-cutting items (pulled from FGD1 internal feedback):

- **Terminology authority + glossary scope** for Phase 1 (what gets defined, who maintains it)
- **3-level information architecture** stance (policy vs practitioners vs public)
- **Two-way communication minimum** for Phase 1 (feedback channel, FAQ; chatbot as roadmap)
- **Dataset preview standard** for Phase 1 catalog (schema + sample + owner + update cadence)
- **Publishing workflow** stance (draft/review/publish) and who signs off
- **QA/QC minimum SOP** and role clarity (input validation, output publishing checks)

Additional (from interviews):
- Minimum **granularity stance** for Phase 1 (province vs district vs sub-district vs municipality/LAO vs EA)
- “Printable / exportable” pack requirement for budget and executive workflows
- Whether NCAIF will primarily **link** to authoritative sources (catalog-first) vs host data
