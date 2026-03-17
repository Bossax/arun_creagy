---
color: var(--mk-color-green)
status: In Progress
start date: 2026-01-05T00:00:00.000Z
last_updated: 2026-03-06
type: task
project:
  - DCCE_CRDB
due date:
---
# National Climate Adaptation Information Framework (NCAIF)

**Role of this document**: lock the **preliminary NCAIF design** for FGD2 (structure + how it serves prioritized workflows + where MVPs sit).

Primary inputs:

- Use-case inventory: [`NCAIF_Use_Cases.md`](src/01_Projects/2025-11_DCCE-CRDB/output/NCAIF_Use_Cases.md:1)
- Workflow patterns + MVPs (v2; literacy-grounded): [`NCAIF — Workflow patterns + MVP v2.md`](src/01_Projects/2025-11_DCCE-CRDB/output/NCAIF%20%E2%80%94%20Workflow%20patterns%20%2B%20MVP%20v2.md:1)
- (v1 preserved for history): [`NCAIF — Workflow patterns + MVP draft (from stakeholder use cases).md`](src/01_Projects/2025-11_DCCE-CRDB/output/NCAIF%20%E2%80%94%20Workflow%20patterns%20%2B%20MVP%20draft%20%28from%20stakeholder%20use%20cases%29.md:1)
- Sitemap alternatives (to select): [`NCAIF_Sitemap_Options.md`](src/01_Projects/2025-11_DCCE-CRDB/output/Artifact%20v1/NCAIF_Sitemap_Options.md:1)
- Governance phasing (v3): [`Feature-Driven Data Governance Strategy v3 (2026-03-05).md`](01_Projects/2025-11_DCCE-CRDB/output/Feature-Driven%20Data%20Governance%20Strategy%20v3%20%282026-03-05%29.md)

---

## 1) Purpose

Help non-technical stakeholders navigate the climate adaptation domain **and** support a small set of high-value workflows in Phase 1–2.

This means NCAIF must do two things at once:

1) Provide a stable **business taxonomy** (thematic backbone), and
2) Provide workflow entry points that surface **MVPs** clearly.

---

## 2) Focused workflows and MVPs (what Phase 1 must visibly support)

From stakeholder use cases, we prioritize cross-cutting workflow patterns (P1–P4) and map them to MVPs:

### Workflow pattern → MVP mapping

- **P1 — Curated briefing pack (policy/decision/budget)** → **MVP-1** Briefing Pack Generator
- **P2 — Event → impact → loss/damage post-event assessment** → **MVP-2** Post-event reporting pack
- **P3 — Finding and agreeing on the official dataset (clearinghouse)** → **MVP-3** Recommended Dataset Registry
- **P4 — Uncertainty-safe risk analysis for advanced users** → **MVP-4** Uncertainty guidance pack + publishing standard

These MVPs must be **explicitly placed** in the sitemap (not implied).

**v2 refinement (literacy-grounded):**

- Phase 1 must assume **mixed literacy** and implement a **Tier 1 vs Tier 2** stance.
- Tier 1 should be **prescriptive and export-first** (curated packs), rather than self-service analysis.
- Tier 2 enables advanced users (banks, NESDC) with uncertainty semantics and deeper metadata.

---

## 3) Sitemap alternatives (2–3 options)

For FGD2, we present three viable alternatives:

1) **Option 1 — Thematic-based**
2) **Option 2 — User-journey-based**
3) **Option 3 — Hybrid (Workflow-pattern-first)**

Details live in: [`NCAIF_Sitemap_Options.md`](01_Projects/2025-11_DCCE-CRDB/output/Artifact%20v1/NCAIF_Sitemap_Options.md)

**FGD2 selection question:** Which option best balances usability + Phase 1 feasibility + stakeholder expectations?

---

## 4) Use case inventory (stakeholder engagement → system requirements)

The complete inventory (with implications and “must decide” items) is maintained in:

- [`NCAIF_Use_Cases.md`](src/01_Projects/2025-11_DCCE-CRDB/output/NCAIF_Use_Cases.md:1)

For FGD2, the key is not to re-list everything, but to show:

- which use cases collapse into the 3–4 workflow patterns, and
- which MVPs serve multiple use cases (leverage).

---

## 5) Prioritized workflows + logic of MVP derivation (the “why these MVPs” section)

**Logic (pattern-first):**

1) We observed repeated needs across agencies: exportable decision packs, post-event reporting, dataset disputes, and probabilistic layer misinterpretation.
2) We distilled these into workflow patterns P1–P4.
3) We selected MVPs that serve multiple patterns/use cases with minimal platform dependency:
   - MVP-1 and MVP-3 can start as documentation/templates + catalog entries
   - MVP-2 can start as a schema + pilot with historic events
   - MVP-4 can start as a publishing standard + worked examples

Reference: [`NCAIF — Workflow patterns + MVP draft (from stakeholder use cases).md`](src/01_Projects/2025-11_DCCE-CRDB/output/NCAIF%20%E2%80%94%20Workflow%20patterns%20%2B%20MVP%20draft%20%28from%20stakeholder%20use%20cases%29.md:1)

Updated reference (v2): [`NCAIF — Workflow patterns + MVP v2.md`](src/01_Projects/2025-11_DCCE-CRDB/output/NCAIF%20%E2%80%94%20Workflow%20patterns%20%2B%20MVP%20v2.md:1)

**Alignment check (how v2 MVP design enhances use cases)**

- UC-03 / UC-03b (policy + LAO budgets): v2 makes packs prescriptive and export-first (Tier 1) and avoids requiring users to interpret probabilistic layers.
- UC-01 / UC-09 (post-event + true loss): v2 frames event/impact as quarantine + revision with flags, enabling gradual improvement without pretending the data is clean.
- UC-10 / UC-08 (baseline verification + statistical baselines): v2 makes “recommended baselines” a first-class artifact with endorsement authority + audit trail.
- UC-11 (banks): v2 keeps advanced uncertainty semantics but moves it into a governed Tier 2, reducing misuse risk.

---

## 6) Demonstration user journeys (FGD2-ready)

These are the three journeys requested for the deck demo. Each journey should map to a single MVP “moment.”

### Journey A — DCCE Communication & Engagement team (public-facing, safe publishing)

**Goal:** publish a climate risk briefing without misinterpretation or PDPA risk.

1) Start at **Recommended Baselines (MVP-3)** → choose authoritative datasets.
2) Check **Uncertainty guidance (MVP-4)** → apply required wording for probabilistic layers.
3) Generate **briefing pack (MVP-1)** → export 1–2 page pack with limitations statement.
4) Route through **draft → review → publish** gate (governance requirement).

### Journey B — Adaptation measure development team (planning + project design)

**Goal:** justify an adaptation project with consistent evidence.

1) Select area (province/LAO).
2) Pull baselines (MVP-3) + interpret safely (MVP-4).
3) Produce a **budget justification / planning pack (MVP-1)**.

### Journey C — International cooperation / reporting & compliance team

**Goal:** respond to external reporting requests with auditable sourcing.

1) Use **catalog + recommended baselines (MVP-3)** to cite sources and versions.
2) Attach limitations/uncertainty statements (MVP-4 standard).
3) Export standardized pack (MVP-1) for communication/reporting.

---

## 7) Governance dependencies (Phase 1 “must exist”)

Aligned to governance v3:

- data classification decisions (Internal vs GDX vs Open Data)
- minimum metadata + preview standard
- recommended baseline endorsement authority + audit trail
- boundary governance + crosswalk ownership
- event/impact schema governance (for MVP-2)

Reference: [`Feature-Driven Data Governance Strategy v3 (2026-03-05).md`](src/01_Projects/2025-11_DCCE-CRDB/output/Feature-Driven%20Data%20Governance%20Strategy%20v3%20(2026-03-05).md:1)

---

# Draft Data Structure (Sitemap) -superseded
2026-03-11 Sitemap presented in FGD2 (seed to preserve)

## Option 1: Thematic-based (ทางเลือกที่ 1: อิงตามหมวดหมู่ข้อมูล)

- **Data repository by content category (คลังข้อมูลตามหมวดหมู่เนื้อหา)**
  - Science and Climate Conditions (วิทยาศาสตร์และสภาวะภูมิอากาศ)
  - Risks and Impacts (ความเสี่ยงและผลกระทบ)
  - Loss and Damage (ความสูญเสียและความเสียหาย)
  - Adaptation and Risk Management (การปรับตัวและจัดการความเสี่ยง)

---

## Option 2: User-journey-based (ทางเลือกที่ 2: อิงตามกลุ่มผู้ใช้งาน)

- **Data Management Center for Policy Makers (ศูนย์บริหารจัดการข้อมูลสำหรับผู้กำหนดนโยบาย)**
  - Summary of risks by area and sector (สรุปภาพรวมความเสี่ยงรายพื้นที่และภาคส่วน) — **MVP-1**
  - Indicators (ตัวชี้วัด)
    - Disaster indicators / extreme event (ตัวชี้วัดด้านภัยพิบัติ) — **MVP-2**
  - Status of national adaptation measures (สถานะมาตรการปรับตัวระดับชาติ)
  - Data services for strategic planning (บริการข้อมูลเพื่อการวางแผนยุทธศาสตร์)
    - Standard reference dataset registry (บัญชีชุดข้อมูลอ้างอิงมาตรฐาน) — **MVP-3**
    - Hazard and vulnerability data overlay tool (เครื่องมือซ้อนทับข้อมูลภัยและความเปราะบาง)
    - Spatial risk database (ฐานข้อมูลความเสี่ยงเชิงพื้นที่)
    - Data methodology and standards (ระเบียบวิธีและมาตรฐานข้อมูล) — **MVP-4**

---

# Sitemap vNext (interim report refinement) - superseded 2026-03-12 10:50

## 1. Design rules

- Preserve the **Option 1 topics** as the visible content taxonomy.
- Keep the **Policy Maker block** intact because it is the anchor expected by leadership.
- Use the **adaptation cycle as the backbone** of the user-journey map.
- Embed technical assets (recommended baselines, spatial references, standards) **inside relevant pages** rather than placing them at the top level.

## 2. Top-level navigation

1) Home
2) Data Management Center for Policy Makers
3) Adaptation Information by Cycle
4) Risk and Area Profiles
5) Adaptation Measures and Implementation
6) Knowledge, Tools, and Data Services
7) News, Updates, and About

## Drill-down sitemap (2–3 levels)
#### 1) Home
- National climate adaptation overview
- Key climate risks and adaptation priorities
- Featured maps and insight cards
- Latest updates
- Quick entry by need
	- Understand risks
	- Plan adaptation action
	- Monitor adaptation progress
	- Access data services

#### 2) Center for Policy Makers
- Summary of risks by area and sector — **MVP-1**
	- National summary
	- Provincial profiles
	- Sector summaries
	- Executive briefing pack export
- Indicators
	- Disaster indicators and extreme events — **MVP-2**
	- Risk indicators
	- Adaptation progress indicators
	- M&E indicators
- Status of national adaptation measures
	- National adaptation plan progress
	- Priority measures by sector
	- Implementation progress snapshots
- Data services for strategic planning
	- Hazard and vulnerability overlay tool
	- Spatial risk database
	- Scenario and planning support pages
	- Data methodology and standards — **MVP-4**

#### 3) Adaptation Information by Cycle

This is the primary user-journey backbone derived from Option 1 topics.

- Climate science
	- Climate drivers and trends
	- Historical observations
	- Future climate scenarios
	- Hazard overview pages
- Risks and impacts
	- Exposure and vulnerability
	- Risk assessments by sector
	- Risk assessments by area
	- Cascading impacts and cross-sector effects
- Loss and damage
	- Event overviews
	- Post-event impact pages — **MVP-2**
	- Damage and loss summaries  — **MVP-2**
	- Revision and update notes
- Adaptation planning
	- Adaptation planning guidance
	- Priority options and response pathways
	- Planning case examples
	- Budget justification packs — **MVP-1**
- Adaptation implementation
	- Ongoing projects and interventions
	- Who is doing what
	- Local and sector implementation examples
	- Implementation challenges and lessons
- Results and monitoring
	- Monitoring and evaluation framework
	- Outcome and progress dashboards
	- Adaptation stories
	- Adaptation projects
	- Reporting resources

#### 4) Risk and Area Profiles

- Provincial risk profiles — **MVP-1**
- Area-based summaries
- Sector-based risk pages
- Cross-area comparison views
- Printable briefing packs — **MVP-1**

#### 5) Adaptation Measures and Implementation
- Adaptation options library
	- Nature-based solutions
	- Infrastructure and engineering
	- Governance and policy measures
	- Community-based approaches
- Good practices and case studies
- National and local implementation status
- Implementation support resources

#### 6) Knowledge, Tools, and Data Services

Technical support is present but embedded rather than the platform’s identity.
- Data catalog and discovery — **MVP-3**
	- Browse datasets by theme
	- Browse datasets by sector
	- Browse datasets by area
	- Dataset pages with steward, cadence, access condition, and usage notes
- Strategic planning data services
	- Standard reference datasets embedded in relevant pages — **MVP-3**
	- Overlay and map services
	- Download and request services
- Methodology and standards — **MVP-4**
	- How risk is defined
	- How adaptation is categorized
	- Indicator methods
	- How to interpret climate projections and uncertainty
- Glossary and learning resources

#### 7) News, Updates, and About

- News and events
- Recent publications
- About the platform
- Partner agencies
- Contact and feedback

---

##  3. Assessment of the NCAIF navigation structure

### Strengths
- **Usable for non‑technical decision‑makers** through the Policy Maker Center.
- **Clear adaptation‑cycle storyline** that aligns with IPCC, UNFCCC, and ISO logic.
- **Balanced public‑facing structure** that is not just a data catalog.
- **Extensible backbone** with flexible subtopics to grow over time without redesign.
- **Phase 1 pragmatism**: technical functions are embedded within user pages rather than dominating navigation.

### Limitations and risks
- **Duplication risk** across policy‑maker pages, cycle pages, and risk‑area profiles if editorial governance is weak.
- **Overlap in implementation content** between the cycle branch and the dedicated implementation section.
- **Loss and damage may dominate** if not consistently framed as part of the broader risk chain.
- **Analytical concepts remain implicit** (exposure, vulnerability, adaptive capacity, residual risk).
- **Support/enabling conditions** are under‑surfaced relative to assessment and planning content.



## 4. Alternative sitemap designs (same core, different emphasis)

### Alternative A — Policy and program cycle‑first
**Idea**: Present the same content as a public‑sector program cycle (diagnose → plan → finance → implement → evaluate). This keeps the adaptation‑cycle logic in the background while foregrounding planning and implementation decisions.

**Top‑level navigation (illustrative)**
1) Home
2) Policy Maker Center
3) Diagnose and Assess
4) Plan and Prioritize
5) Finance and Enable
6) Implement and Coordinate
7) Evaluate and Report
8) Knowledge, Tools, and Data Services
9) News and About

**Trade‑offs vs vNext**
- **Better** when the primary audience is senior planners and program managers.
- **More legible** for UNFCCC reporting logic and ISO management cycles.
- **Less visible** as a climate‑risk architecture unless strong cross‑links remain.

### Alternative B — User‑group‑first
**Idea**: Present the platform by user groups (policy, technical analysts, local implementers), with adaptation‑cycle tags in the background. This emphasizes service usability and audience‑specific navigation.

**Top‑level navigation (illustrative)**
1) Home
2) For Policy Makers
3) For Technical Analysts
4) For Local Implementers
5) National Adaptation Cycle
6) Knowledge, Tools, and Data Services
7) News and About

**Trade‑offs vs vNext**
- **Better** when usability for multiple audiences is the dominant goal.
- **Aligned** with WMO climate services thinking (service delivery by user community).
- **Less explicit** as an adaptation‑cycle storyline, requiring strong taxonomy/metadata to preserve standards alignment.

---


# Locked decision 2026-03-13
## a) Stable vs flexible sitemap rules

### a-1) Stable backbone (do not change without leadership review)
- adaptation cycle structure
- policy maker block
- core topic families
	- climate conditions
	- risks and impacts
	- loss and damage
	- adaptation planning
	- adaptation implementation
	- results and monitoring
- existence of data services, methodology, glossary, and updates sections

### a-2) Flexible elements (can evolve by section owners)
- specific sectors
- hazard subtopics
- named tools and dashboards
- case studies and featured stories
- agency collections
- indicator sets

## b) Standards alignment of the NCAIF sitemap 
2026-03-12 15:50

>[!key] Sitemap change process (short form)
>1) **Minor content change** (new subpage, label revision, case study) → section owner approval
>2) **Structural extension** (new subtopic under a cycle branch, new sector page) → CRDB/NCAIF coordination review
>3) **Backbone change** (top-level navigation or cycle structure change) → DCCE leadership review


This section verifies whether the proposed sitemap structure aligns with major international standards and frameworks (IPCC, WMO, UNFCCC, ISO). The assessment is framed for Phase 1, where the NCAIF is a **conceptual and logical architecture**, not a full software build.

### IPCC (risk framing and iterative adaptation)

**What IPCC emphasizes**
- Climate risk as a function of **hazard, exposure, vulnerability**, producing **impacts** and **residual risk**.
- **Iterative risk management**: assess risk → plan/implement adaptation → monitor and adjust.

**Mapping to NCAIF vNext**
- **Climate and climate conditions** → hazard and climate signal base.
- **Risks and impacts** → exposure/vulnerability patterns and sector/area risk assessments.
- **Loss and damage** → realized impacts and residual risk evidence.
- **Adaptation planning / implementation / results & monitoring** → iterative adaptation and review.
- **Risk and area profiles** → applied, decision‑ready synthesis of risk evidence.

**Gaps / cautions**
- Exposure, vulnerability, adaptive capacity, and residual risk are **implicit**, not consistently named in the sitemap.
- Loss and damage is policy‑important, but should be narrated as part of the risk chain to avoid siloing.

### WMO / climate services (observations → services → users)

**What WMO emphasizes**
- Observations/monitoring, prediction/projection, and **user‑oriented climate services**.
- Service delivery and co‑production principles.

**Mapping to NCAIF vNext**
- **Climate and climate conditions** → observations, trends, scenarios.
- **Knowledge, Tools, and Data Services** → catalog, maps, downloads, guidance.
- **Policy Maker Center** → tailored service layer for decision‑makers.
- **Risk and area profiles** → localized service outputs.

**Gaps / cautions**
- The platform reads more as **adaptation information** than a full climate services architecture.
- Co‑production and service performance are not explicit in navigation (can be added in About/Methodology later).

### UNFCCC (NAP and adaptation reporting logic)

**What UNFCCC emphasizes**
- Hazards and climate context
- Impacts and vulnerabilities
- Adaptation priorities and plans
- Implementation progress
- Monitoring and evaluation
- Support/needs and institutional context

**Mapping to NCAIF vNext**
- **Climate and climate conditions** → hazard context.
- **Risks and impacts** → vulnerability and impact evidence.
- **Adaptation planning** → priorities and planning guidance.
- **Adaptation implementation** → action tracking and status.
- **Results and monitoring** → M&E and reporting outputs.
- **Policy Maker Center** → summaries, indicators, and national status for reporting.

**Gaps / cautions**
- Support dimensions (finance, capacity, technology, institutions) are not foregrounded.
- Reporting provenance and legal constraints are embedded, but not explicitly surfaced as a reporting hub.

### ISO 14090 / 14091 (adaptation management cycle)
**What ISO emphasizes**

- Context establishment, climate risk assessment, option appraisal, implementation, and monitoring/review.
- Clear traceability of methods, assumptions, responsibilities, and review cycles.

**Mapping to NCAIF vNext**

- **Climate and climate conditions + Risks and impacts + Loss and damage** → context and risk assessment.
- **Adaptation planning** → option identification and appraisal.
- **Adaptation implementation** → execution.
- **Results and monitoring** → review and improvement.
- **Methodology and standards** → auditability and process discipline.

**Gaps / cautions**

- ISO traceability depends on page‑level metadata and governance practices, not the sitemap alone.

## c) Landing page access model (Policy Maker Center placement + main entry paths)

This section explains how the **Center for Policy Makers** should appear on the landing page and how users access each main section from the homepage.

### Placement rule for the Policy Maker Center
- **Always visible in the top navigation bar** (as a primary menu item).
- **Featured as the first and largest entry card** on the landing page.
- **Included as the primary call‑to‑action button** in the hero banner.

This ensures leadership sees their entry point immediately, without scrolling or searching.

### Suggested landing page layout
#### 1) Top navigation bar (global)
- Home
- Data Management Center for Policy Makers
- Adaptation Information by Cycle
- Risk and Area Profiles
- Adaptation Measures and Implementation
- Knowledge, Tools, and Data Services
- News, Updates, and About

#### 2) Hero band (top of the page)
**Title + short explanation + 2–3 primary buttons**

- **[Go to Policy Maker Center]** → Data Management Center for Policy Makers
- [Explore by Adaptation Cycle] → Adaptation Information by Cycle
- [Find My Area Profile] → Risk and Area Profiles

#### 3) Primary entry cards (largest visual block)
1) **Policy Maker Center** (highlighted, first position)
2) **Adaptation Information by Cycle**
3) **Risk and Area Profiles**
4) **Adaptation Measures and Implementation**

Each card links directly to the corresponding main page.

#### 4) Secondary discovery rows
- **Adaptation cycle band** (visual flow with clickable steps)
- **Explore by area band** (map selector + provincial profiles)
- **Measures and practice band** (options library, case studies, implementation support)
- **Tools and data band** (catalog, maps/overlays, methods/standards)

### Access map (conceptual)
- **Policy Maker Center** is reachable via:
  - top nav
  - hero button
  - first entry card
- **Adaptation Information by Cycle** is reachable via:
  - top nav
  - hero button
  - second entry card
  - cycle band
- **Risk and Area Profiles** is reachable via:
  - top nav
  - hero button
  - third entry card
  - area band
- **Adaptation Measures and Implementation** is reachable via:
  - top nav
  - fourth entry card
  - measures band
- **Knowledge, Tools, and Data Services** is reachable via:
  - top nav
  - tools and data band

---

## d) Refined NCAIF sitemap — March 2026 (Pack A/B/C aligned)
**2026-03-12 17: 50**

This section updates the NCAIF structure to reflect the Pack A/B/C decision matrix and the latest scope constraints. It preserves the adaptation-cycle backbone and the Policy Maker Center, while reframing tools and catalog access to match Phase 1 reality and Pack C usability guidance.

### 1. Top-level navigation
The top-level list stays shallow, with narrative and decision-ready entry points. Items marked as “tools” or “catalog” are separated in the second level to avoid mixed-mode confusion.

1) **Home**
2) **Data Management Center for Policy Makers**
3) **Adaptation Information by Cycle**
4) **Risk and Area Profiles**
5) **Adaptation Measures Guidance & Implementation Examples** (Phase 1 guidance and exemplars, not a complete registry)
6) **Knowledge, Tools, and Data Services** (tools and data catalog separated in sub-navigation)
7) **News, Updates, and About**

Key scope cautions:
- Adaptation Measures is positioned as **guidance + curated examples** in Phase 1 (not a fully built searchable library).
- Hazard–exposure overlay is treated as an **integration point with the broader DCCE IT system**, not a flagship Phase‑1 feature.
- Risk maps and comparisons are **provincial‑scale** with explicit caveats; advanced drill‑downs are not surfaced as public promises.

### 2. Second-level (2nd-level) structure

**1) Home**
- What NCAIF helps users do (short value statement)
- Quick entry by need (Understand risks / Plan adaptation / Monitor progress / Access tools & data)
- Featured provincial map cards + briefing packs
- Latest updates and announcements

**2) Data Management Center for Policy Makers**
- Decision‑ready summaries
  - National summary
  - Provincial profiles (dashboard + briefing pack export)
  - Sector summaries
- Indicators (risk, disaster, adaptation progress)
- Status of national adaptation measures (high‑level progress snapshots)
- Strategic planning services (links, not deep builds)
  - Provincial risk dashboard (guided, not free‑form analytics)
  - Data services for planning (link to tools & catalog)
  - Hazard–exposure overlay integration (link out to DCCE IT system)

**3) Adaptation Information by Cycle**
- Climate science and hazards (trends, observations, scenarios)
- Risks and impacts (sector + area risk summaries)
- Loss and damage (event overview + interpretation)
- Adaptation planning (guidance + planning packs)
- Adaptation implementation (examples and lessons)
- Results and monitoring (progress framing; link out to Adaptation M&E system)

**4) Risk and Area Profiles**
- Provincial risk profiles (core Phase‑1 product)
- Area summaries and sector risk pages
- Cross‑area comparisons (provincial‑scale only; explicitly relative)
- Briefing packs and narrative summaries
- Interpretation and limitations (required companion pages)

**5) Adaptation Measures Guidance & Implementation Examples**
- Adaptation measures guidance (what to consider, how to assess)
- Curated exemplars by sector and context
- Good practices and case studies
- Implementation support resources (templates and planning aids)
- Links to external registries or programs (when relevant)

**6) Knowledge, Tools, and Data Services**
- **Interactive tools / dashboards**
  - Provincial risk map (guided)
  - Scenario exploration (limited, explanatory)
  - Other task‑oriented tools (as they become available)
- **Data catalog / download / APIs**
  - Browse datasets by theme/sector/area
  - Dataset detail pages (steward, cadence, access)
  - Download/request workflow
- **Methods, limitations, and standards**
  - Risk interpretation and caveats
  - Uncertainty guidance
  - Methodology references
- **Glossary and learning resources**

**7) News, Updates, and About**
- News and events
- Publications
- About the platform
- Partner agencies
- Contact and feedback

### 3. Page-type rules (page archetypes)

- **Landing / Hub page**
  - Purpose: orient users quickly and provide 2–4 clear entry routes.
  - Always include: short value statement, primary calls‑to‑action, featured map or briefing pack.
- **Explainer / Concept page**
  - Purpose: translate technical concepts into decision‑ready language.
  - Always include: plain‑language summary, key visual, link to methods/limitations.
- **Area (province) profile page**
  - Purpose: deliver provincial‑scale risk summaries for decision use.
  - Always include: key indicators, map view, comparison cue, and **provincial‑scale caveat**.
- **Sector knowledge page**
  - Purpose: show sector‑specific risk drivers and response options.
  - Always include: sector summary, cross‑links to measures guidance and case examples.
- **Tool entry page (interactive)**
  - Purpose: task‑oriented access to dashboards/maps.
  - Always include: task framing, expected outputs, data provenance, and limitations.
- **Data catalog / download page**
  - Purpose: provide authoritative dataset discovery and access.
  - Always include: steward, update cadence, access condition, usage notes, and links to related tools.
- **Methodology / limitations page**
  - Purpose: ensure transparency without overwhelming first contact.
  - Always include: interpretation guidance, uncertainty notes, and links back to related pages.
- **Case study / briefing pack page**
  - Purpose: translate evidence into narrative, decision‑ready outputs.
  - Always include: context, evidence summary, actions taken, and key lessons.

Phase‑1 specificity:
- **Adaptation Measures** pages are **explanatory and exemplar‑based**, not a comprehensive library.
- **Risk maps** are provincial‑scale only and must carry clear caveats about resolution, uncertainty, and proper use.

### 4. Sitemap change process

**Stable backbone (rare change)**
- Adaptation‑cycle structure
- Policy Maker Center as a top‑level anchor
- Risk and Area Profiles as a first‑class section

**Flexible elements (frequent change)**
- Case studies, briefing packs, and exemplars
- Named tools and dashboards
- Sector subpages and featured hazards
- External links to related systems (e.g., Adaptation M&E, hazard‑exposure overlay)

**Change types**
1) **Minor content change** (new subpage, label refinement, new case study) → section owner approval
2) **Structural extension** (new subtopic under a cycle branch, new sector page) → CRDB/NCAIF coordination review
3) **Backbone change** (top‑level navigation or cycle‑structure change) → DCCE leadership review

**Governance rule**
- Major sitemap decisions must cite Pack A product constraints, Pack B TOR scope (Task 5.5), Pack C usability guidance, and the decision matrix evidence.
- Interim‑report decisions are the **initial governance record** for this refined structure and should be treated as the baseline for subsequent revisions.
