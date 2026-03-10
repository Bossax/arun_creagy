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
### National Climate Adaptation Information Framework (NCAIF)

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

## Appendix — Thematic backbone (business taxonomy)

>[!note] Structure (Refined from Inception Report Benchmarking):
**NCAIF**
├── Stage 1: Meteorology & Climate (Deep Modeling)
│   ├── Climate Variables (Temperature, Precipitation, Wind) -> Aligned with "Essential Climate Variables" (KlimAdapt)
│   ├── Climate Projections (GCMs, RCPs, Scenarios) -> Integrated with Copernicus-style explorers
│   └── Climate Indices (SPI, ENSO, IOD)
├── Stage 2: Risk & Impact Assessment (IVRA Core)
│   ├── Hazards (Flood, Drought, Heat Wave, Storm, SLR) -> Aligned with ADPC/BTR Hazard List
│   ├── Exposure (Population, Infrastructure, Agriculture, Coastal Assets) -> From DCCE Risk MAP
│   ├── Vulnerability & Sensitivity (Sectoral Factors) -> Refined via NAP 6 Sectors
│   ├── Adaptive Capacity (Local vs. Institutional)
│   └── Impacts (Economic Loss, Casualties, Disruption) -> Linked to Sendai Targets A-G
├── Stage 3: Loss & Damage (MVD Area)
│   ├── Event Metadata (Type, Location, Duration)
│   ├── Impact Metrics (Physical Damage, Economic Loss)
│   └── Response & Recovery (Emergency Measures)
├── Stage 4: Adaptation Measures (Shallow Modeling)
│   ├── Measure Types (NbS, Structural, Policy)
│   └── Sectoral Alignment (NAP 6: Water, Ag, Tourism, Health, Nature, Settlement)
└── Stage 5: Results & M&E (External Integration)
    └── Integration Points for CU Framework (BTR WP-4)

**Artifact Type:** Hierarchical knowledge structure, Business Glossary
