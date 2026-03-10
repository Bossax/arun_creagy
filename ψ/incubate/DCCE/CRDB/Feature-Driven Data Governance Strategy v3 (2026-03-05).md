---
status: current
tags:
  - data-governance
  - implementation
  - NCAIF
  - DGA
created: 2026-03-05
last_updated: 2026-03-05
project:
  - DCCE_CRDB
type:
  - strategy
version: "v3"
supersedes:
  - src/01_Projects/2025-11_DCCE-CRDB/output/Feature-Driven Data Governance Strategy v2 (2026-02-26).md
inputs:
  - src/01_Projects/2025-11_DCCE-CRDB/output/NCAIF_Use_Cases.md
  - src/01_Projects/2025-11_DCCE-CRDB/output/NCAIF — Workflow patterns + MVP draft (from stakeholder use cases).md
  - src/01_Projects/2025-11_DCCE-CRDB/sources/Interview result/Interview Summary - DGA.md
  - src/01_Projects/2025-11_DCCE-CRDB/output/FGD2_Slide_Deck_Guide.md
---

# DCCE-CRDB Data Governance Implementation Strategy (v3): Feature-Driven + **Leverage National Infrastructure (DGA-first)**

This version preserves the core principle from v2:

> **Guiding principle:** “Govern what you need, just in time, to deliver the next valuable feature.”

and adds a new, explicit constraint and opportunity from the DGA interview:

> **New stance (v3):** *Do not build redundant government data infrastructure.* Treat DGA’s platforms and standards as “default rails” for publishing and sharing.

Primary user-facing driver remains the NCAIF product set (MVPs) described in:
- [`NCAIF_Use_Cases.md`](src/01_Projects/2025-11_DCCE-CRDB/output/NCAIF_Use_Cases.md:1)
- [`NCAIF — Workflow patterns + MVP draft (from stakeholder use cases).md`](src/01_Projects/2025-11_DCCE-CRDB/output/NCAIF%20%E2%80%94%20Workflow%20patterns%20%2B%20MVP%20draft%20%28from%20stakeholder%20use%20cases%29.md:1)

---

## 0) What changed from v2 (summary)

### Added (from DGA interview)

- **National platforms as default pathways**:
  - Open data → **data.go.th** (harvested from agency catalogs)
  - Non-open G2G sharing → **GDX** (permissioned 1:1 provider-consumer)
- **Data classification as a first-class governance activity** (internal vs GDX vs Open Data), and a service DGA can help implement.
- **Architecture choice affects DCCE’s Digital Government Readiness KPI**; DCCE should consult DGA before committing to “separate climate hub vs integrated agency catalog.”
- **PDPA is often a roadblock-by-interpretation**; DGA helps agencies design masking/anonymization so analytical open data can be published safely.

### Kept (from v2)

- Feature-driven governance roadmap (Phase 1 → Phase 2 → Phase 3)
- Publishing gates, limitations statements, boundary governance, event schema governance

---

## 1) The “Rails” model (how data moves, without redundant builds)

Use these rails as the default operating model for Phase 1–2.

### Rail A — Open Data (public)

- **Where it lives**: agency-owned dataset + metadata in an **Agency Catalog** (typically CKAN).
- **How it becomes searchable nationally**: harvested into **data.go.th** (central portal).
- **DCCE governance role**: define the Phase 1 “minimum publishable metadata” + limitations/uncertainty standard.

### Rail B — Non-open data (G2G)
- **Where it moves**: via **GDX** (government-to-government only).
- **How it’s granted**: provider-controlled, permissioned, field-level access, based on legal mandate and agreement.
- **DCCE governance role**:
  - define the request templates and internal approval path
  - classify datasets (what can be open vs GDX vs strictly internal)

### Rail C — Internal-only data (restricted)
- **Where it lives**: inside DCCE systems until governance/legal readiness exists.
- **DCCE governance role**: aggregation rules + access controls + auditable handling.

**Implication:** Phase 1 NCAIF can be a **catalog + clearinghouse** even if data physically remains distributed; hosting is not required to deliver value.

---
## 2) Updated Phase 1 focus: MVP-first, with DGA-enabled gates

### Phase 1 Flagship MVPs (6 months)

Keep the v2 “flagship set” but formalize the MVP framing:

1) **MVP-1 — Briefing pack generator** (export-first) <!--comment:  out of project scope. Task 5.5-->
2) **MVP-3 — Recommended dataset registry** (“Which dataset should I use?”) <!--comment: in project scope. Task 5.3-->
3) **MVP-4 — Uncertainty guidance pack** (publishing standard) <!--comment: out of project scope. require serious research-->
4) **MVP-2 — Post-event reporting pack** (schema + pilot, medium feasibility) <!--comment:  in project scope. Task 5.3-->

### Phase 1 governance capabilities (minimum set to ship safely)

#### G1 — Data classification + publishing path (DGA-aligned)

For each dataset/product used in an MVP, record:
- classification: **Internal / GDX / Open Data**
- intended uses + prohibited uses
- privacy handling (mask/anonymize/aggregate)
- publication rail: data.go.th / GDX / internal

> DGA can support this through their **Data Classification Service** and DGF consulting.

#### G2 — Catalog metadata + preview standard (Phase 1 baseline)

Minimum metadata fields (v2) stay, but v3 adds explicit national alignment:
- `Asset name`, `Description`, `Owner/Steward`, `Source`, `Spatial unit`, `Update cadence`, `Sensitivity/classification`, `Known limitations`
- `Access pathway`: Open Data URL (data.go.th/agency catalog) **or** GDX route **or** internal request point
- `Legal basis / mandate (if GDX)` (short text)

#### G3 — “Recommended baseline” endorsement (clearinghouse)

Build a small registry that answers:
- Which dataset is recommended for X?
- For what purpose, at what scale, with what caveats?
- Who endorses it (role/title)?
- What was superseded (history kept)?

This is the governance engine behind **MVP-3**.

#### G4 — Boundary + crosswalk governance
Keep v2’s boundary emphasis. v3 adds an operational policy:

- Phase 1 must explicitly designate **canonical boundaries** for reporting and publishing.
- Crosswalks must be treated as governed assets (owner + version + limitations).

#### G5 — Event/impact schema governance (post-event reality)

Continue v2: timeliness/freshness is mandatory metadata; validation flags exist; revision history is visible.

---

## 3) Work packages (make governance fundable + schedulable)

This keeps v2’s “projectized execution,” updated to include DGA rails.

### WP-A — Dataset onboarding (rail decision + metadata)

**Outputs**
- dataset registered in an agency catalog (or referenced link + metadata)
- classification decision (Internal/GDX/Open)
- limitations + uncertainty text
- steward/contact + update cadence

**DGA leverage**
- if Open Data: align metadata/tags so harvesting to data.go.th is clean
- if Non-open: design the GDX request + provider/consumer agreement workflow

### WP-B — Product release (MVP packaging)

**Outputs**
- a briefing pack template / post-event template / endorsed baseline page
- publishing workflow: draft → review → publish

### WP-C — Safe publishing gates (minimum QA/QC)

**Outputs**
- a “minimum QA/QC” checklist for each product type
- required limitations statement

### WP-D — Legal / sharing readiness

**Outputs**
- PDPA-safe anonymization/masking guidance per dataset class
- GDX pathway feasibility notes and dependencies

---

## 4) Phase 2–3 (unchanged in principle; updated in institutional integration)

### Phase 2 (Months 7–18): expand value chains + build capacity

- scale stewardship as new features/datasets are onboarded
- expand the recommended baseline registry (more topics)
- formalize repeatable GDX request workflows for priority non-open datasets

### Phase 3 (Months 19+): formalize governance + ecosystem integration

- formalize decision bodies (DGC/DSC) once adoption exists
- align DCCE governance artifacts with DGF expectations and audit readiness

---

## 5) FGD2 “must decide” items (to lock preliminary design)

1) **Catalog-first vs host-first** stance for Phase 1
2) Which datasets/products are Phase 1 flagship (choose 2–4 MVPs)
3) Canonical boundary set(s) + crosswalk ownership
4) Endorsement authority (role/title) for “recommended baselines”
5) Publishing rail decisions (Open vs GDX vs internal) and classification ownership
6) Architecture choice: integrate into existing DCCE agency catalog vs separate climate hub (KPI implications; consult DGA)

---

## References

- DGA interview summary: [`Interview Summary - DGA.md`](src/01_Projects/2025-11_DCCE-CRDB/sources/Interview result/Interview Summary - DGA.md:1)
- v2 strategy (superseded): [`Feature-Driven Data Governance Strategy v2 (2026-02-26).md`](src/01_Projects/2025-11_DCCE-CRDB/output/Feature-Driven%20Data%20Governance%20Strategy%20v2%20(2026-02-26).md:1)
- v2 strategy (superseded): [`Feature-Driven Data Governance Strategy v2 (2026-02-26).md`](src/01_Projects/2025-11_DCCE-CRDB/output/Feature-Driven%20Data%20Governance%20Strategy%20v2%20%282026-02-26%29.md:1)
