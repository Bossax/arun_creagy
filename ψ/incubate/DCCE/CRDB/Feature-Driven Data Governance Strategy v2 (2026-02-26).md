---
status: current
tags:
  - data-governance
  - implementation
  - NCAIF
created: 2026-02-26
last_updated: 2026-02-26
project:
  - DCCE_CRDB
type:
  - strategy
version: "v2"
supersedes:
  - src/01_Projects/2025-11_DCCE-CRDB/output/Feature-Driven Data Governance Strategy (archived 2026-02-26).md
---
# DCCE-CRDB Data Governance Implementation Strategy (v2): Feature-Driven, Value-First Approach

This strategy keeps the original guiding principle (“govern what you need, just-in-time to deliver the next valuable feature”) but updates the roadmap based on:

- Practicality constraints and delivery sequencing implied by Phase 1
- Interview/workshop signals about **event data reality**, **boundary complexity**, and **climate-literacy gaps**

Primary input for this v2 update:

- Workshop/interview notes: [`src/02_Meeting/2026-02-19 - Data provider consultation workshop.md`](src/02_Meeting/2026-02-19%20-%20Data%20provider%20consultation%20workshop.md:1)
- Use-case extraction: [`src/01_Projects/2025-11_DCCE-CRDB/output/NCAIF_Use_Cases.md`](src/01_Projects/2025-11_DCCE-CRDB/output/NCAIF_Use_Cases.md:1)

## 1. Guiding principle & rationale (unchanged)

**Guiding Principle:** “Govern what you need, just in time, to deliver the next valuable feature.”

**Why it fits DCCE**

- Budget cycles are project-driven → Phase 1 must show value early.
- Data literacy is developing → governance must teach by doing.
- Incentives follow utility → governance must visibly improve products.

## 2. NCAIF design stance for Phase 1 (clarification)

Phase 1 should deliver a **thematic taxonomy (Option 1)** as the stable backbone, but introduce a **light user-journey entry layer** to reduce cognitive load and improve usability.

Reference designs:

- Thematic draft: [`src/01_Projects/2025-11_DCCE-CRDB/output/Artifact v1/NCAIF_Draft_Option1.md`](src/01_Projects/2025-11_DCCE-CRDB/output/Artifact%20v1/NCAIF_Draft_Option1.md:1)
- User-journey draft: [`src/01_Projects/2025-11_DCCE-CRDB/output/Artifact v1/NCAIF_Draft_Option2.md`](src/01_Projects/2025-11_DCCE-CRDB/output/Artifact%20v1/NCAIF_Draft_Option2.md:1)

**Practical framing**

- Phase 1 navigation: “Start here (persona)” → “Browse data/resources (thematic)”
- Phase 1 content: prioritize a few **flagship products** rather than a broad portal.

Update (based on interview signals):

- Persona layer should explicitly prioritize:
  - **Policy makers / planners**
  - **Disaster management planners (DDPM / operations support)**
  - **Local leaders / LAO planners**
  - (Secondary: researchers, communities/citizens)
- UX must make foundational governance *visible* (boundary guidance, limitations statements, access rules), not hidden in policy docs.

## 3. Refined implementation roadmap

### Phase 1 (Months 1–6): High-visibility MVP + targeted governance

**Action (products): Phase 1 flagship set**
1. **Provincial Risk Profiles** (curated, readable outputs) <!--note: essentially Spatial Risk Map version 2-->
2. **Hazard + vulnerability map viewer** (limited set of authoritative layers) <!--note: This is the task that ADPC is working on-->
3. **Post-event impact view** (DDPM/LAO-style reporting, clearly labeled timeliness) <!--note: value-add is standardization + boundary crosswalk + caveats + export packs-->
4. **Risk assessment data catalog (MVP)** — aligned with WP4 requirements in: <!--note: under this project-->
   - [`src/01_Projects/2025-11_DCCE-CRDB/output/CRDB - TOR.md`](src/01_Projects/2025-11_DCCE-CRDB/output/CRDB%20-%20TOR.md:1)
   - [`src/01_Projects/2025-11_DCCE-CRDB/output/CRDB - Implementation Plan.md`](src/01_Projects/2025-11_DCCE-CRDB/output/CRDB%20-%20Implementation%20Plan.md:1)
5. **Glossary + boundary guidance** (to reduce semantic/boundary fragmentation) <!--note: address semantic issues-->
6. **Exportable / printable briefing packs** (budget and executive workflows)

**Governance integration (minimum set required to ship Phase 1)**
1. **“Champion” data stewards (1–2 people)**
	- Own Phase 1 onboarding and publishing rules.
2. **Lightweight catalog, but with publishing gates**
	- Minimum metadata fields: `Asset name`, `Description`, `Owner/Steward`, `Source`, `Spatial unit`, `Update cadence`, `Sensitivity/classification`, `Known limitations`.
3. **Boundary dataset governance (critical)**
	- Declare “canonical boundary set(s)” for Phase 1 reporting
	- Record versions and crosswalk approach (admin vs LAO vs future community boundaries)
4. **Event/impact schema governance (critical)** <!--note: part of Loss and Damage Minimum Viable Dataset? could be. we could integrate standardized event records-->
	- Standardize fields for “where/when/affected population/assets”
	- Explicitly store `lead_time` / `data_freshness` to avoid misleading “real-time” claims
5. **Sensitive data policy path (explicit)**
	- Apply classification policy early; define aggregation rules
	- Open question to decide with stakeholders: whether DCCE needs formal legal/accountability arrangements to access sensitive individual-level data.

Strengthening additions (from interviews):

6. **Limitations statement as a publishing gate (required)**
  - Every “published” indicator/product must include: what it measures, what it does not, freshness, known biases, and safe interpretation notes.
7. **Granularity stance (required)**
  - Define Phase 1 stance on which spatial levels are supported for which workflows (province vs district vs sub-district vs municipality/LAO vs EA).
8. **Data screening / validation (minimum)**
  - For post-event reporting, define minimal screening rules and visible quality flags (late/incorrect category entries are expected).

**Desired outcome**
- A small set of visible, used products that proves the value of governed data.

### Phase 2 (Months 7–18): Expand value chains + build capacity (revised for practicality)

**Action (products)**

- Expand toward a deeper “policy maker & planner journey” (dashboards, progress views), but only after Phase 1 datasets are stable.
- Add more agencies/datasets incrementally (co-producers such as OPT/DDPM), using a repeatable onboarding playbook.

**Governance integration (what changes from Phase 1)**

- **Scale stewardship**: add more data stewards as each new feature requires.
- **Foundational data quality**: apply the quality framework only to Phase 2 “published KPIs.”
- **Capacity building (realistic sequencing)**:
  - If the live portal is not available until a later budget cycle, use **prototype dashboards + dataset onboarding exercises** as the teaching vehicle (not “live portal training”).
- **Pilot DSC function**: create a working group from active stewards to resolve cross-domain issues.

### Phase 3 (Months 19+): Formalize governance + ecosystem integration

**Action**

- Once products have adoption and stewardship maturity, formalize DGC/DSC and scale quality enforcement.

## 4. “Projectized execution” recommendation (new)

Because delivery is project-based, governance work should be packaged into repeatable **work packages** with tangible outputs:

- WP-A: Dataset onboarding (metadata sheet + steward assignment + boundary alignment + publishing decision)
- WP-B: Product release (flagship product spec + data contracts + caveats)
- WP-C: Quality checks (minimal validation rules + limitations statement)
- WP-D: Legal / sharing readiness (classification decision + access pathway)

This framing makes governance fundable, schedulable, and auditable within project cycles.

## 5. Link to alternative strategy

- [`src/01_Projects/2025-11_DCCE-CRDB/output/Alternative_Strategy_Compliance-First.md`](src/01_Projects/2025-11_DCCE-CRDB/output/Alternative_Strategy_Compliance-First.md:1)
