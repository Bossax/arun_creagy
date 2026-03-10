# DCCE_CRDB — Project Knowledge Digest (Onboarding)

## 1) Project Purpose & Scope (What this is)
- The project delivers **conceptual + logical architecture**, not a software build. Physical schemas are **out of scope** (except for data products). This is explicit in [`CRDB - Implementation Plan.md`](ψ/writing/2025-11_DCCE-CRDB/output/CRDB%20-%20Implementation%20Plan.md:24).
- **NCAIF** is now defined as the **Enterprise Data Model (EDM)**: a business taxonomy + glossary and a logical blueprint for organizing climate adaptation knowledge. [`CRDB - Implementation Plan.md`](ψ/writing/2025-11_DCCE-CRDB/output/CRDB%20-%20Implementation%20Plan.md:61)
- **CRDB role vs ADPC role**: CRDB is *Architect/Librarian* (catalog + governance + conceptual modeling). ADPC (UNDP‑BTR Task 2) is *Builder/Curator* (physical risk platform + visualization). [`CRDB - Implementation Plan.md`](ψ/writing/2025-11_DCCE-CRDB/output/CRDB%20-%20Implementation%20Plan.md:32)
- **IVRA‑first** (Identification, Vulnerability & Risk Assessment) is the primary architecture focus; M&E is external integration. [`CRDB - Implementation Plan.md`](ψ/writing/2025-11_DCCE-CRDB/output/CRDB%20-%20Implementation%20Plan.md:56)

## 2) NCAIF (Enterprise Data Model) — Core Design
Source: [`National Climate Adaptation Information Framework.md`](ψ/writing/2025-11_DCCE-CRDB/output/National%20Climate%20Adaptation%20Information%20Framework.md:11)

### 2.1 Purpose
- Provide **stable business taxonomy** + **workflow entry points** to surface MVPs.
- Tiered UX for mixed literacy: **Tier 1** is prescriptive and export‑first; **Tier 2** is advanced, analytic.

### 2.2 Workflow Patterns → MVPs (P1–P4)
- **P1 Curated briefing pack** → **MVP‑1 Briefing Pack Generator** (export‑first)
- **P2 Event → impact → loss/damage** → **MVP‑2 Post‑event reporting pack**
- **P3 Recommended baselines** → **MVP‑3 Recommended Dataset Registry**
- **P4 Uncertainty‑safe risk analysis** → **MVP‑4 Uncertainty guidance + publishing standard**

### 2.3 Sitemap Options (FGD2 decision)
- **Option 1**: Thematic‑based
- **Option 2**: User‑journey‑based
- **Option 3**: Hybrid (workflow‑pattern‑first)

## 3) Governance Rails (v3) — DGA‑First
Source: [`Feature-Driven Data Governance Strategy v3 (2026-03-05).md`](ψ/writing/2025-11_DCCE-CRDB/output/Feature-Driven%20Data%20Governance%20Strategy%20v3%20(2026-03-05).md:24)

### 3.1 Rails Model
- **Rail A Open Data** → data.go.th (harvested from agency catalogs)
- **Rail B Non‑open G2G** → GDX
- **Rail C Internal‑only** → DCCE systems

### 3.2 Phase 1 Governance Gates (Minimum to Ship Safely)
- **G1 Data classification**: Internal / GDX / Open Data + privacy handling
- **G2 Minimum metadata + preview**: owner, cadence, spatial unit, limitations, access path
- **G3 Recommended baseline endorsement registry**: who endorses what, why, and version history
- **G4 Boundary + crosswalk governance**: canonical boundary + crosswalk ownership
- **G5 Event/impact schema governance**: timeliness, validation flags, revision history

## 4) CDM Highlights (IVRA) — Conceptual Logic
Source: [`Conceptual Data Model for climate risk and adaptation data system.md`](ψ/writing/2025-11_DCCE-CRDB/output/Conceptual%20Data%20Model%20for%20climate%20risk%20and%20adaptation%20data%20system.md:10)

Key structural choices:
- **CLIMATE_DRIVER vs HAZARDOUS_EVENT**: separate continuous drivers from discrete events.
- **ATTRIBUTION_LINK**: enables slow‑onset attribution without “fake events.”
- **Vulnerability strategy pattern**: supports both curve‑based risk (CLIMADA) and index‑based risk (CRI) via a flexible vulnerability definition layer.

## 5) Use‑Case Signals & Constraints (FGD1 + Interviews)
Source: [`NCAIF_Use_Cases.md`](ψ/writing/2025-11_DCCE-CRDB/output/NCAIF_Use_Cases.md:13)

### 5.1 Constraints (Phase 1 reality)
- Data latency is normal → must label **timeliness** and support revision history.
- Boundary mismatch → must define **canonical boundary** + **crosswalks**.
- Literacy variation → must tier content and provide **plain‑language guidance**.
- Sensitive data → must define **classification + publishing rails**.

### 5.2 Implications for Product Design
- Exportable **budget‑justification packs** are required (not just exploratory maps).
- Catalog must include **preview before download**, metadata, and owner contact.
- Publishing should include **draft → review → publish** flow (or explicit SOP).

## 6) Milestones (Historical anchors)
Source: [`CRDB - Work Status Brief.md`](ψ/writing/2025-11_DCCE-CRDB/output/CRDB%20-%20Work%20Status%20Brief.md:10)

- **FGD2** (internal validation) and **Interim Report** were priority milestones.
- **ADPC data coordination** is a dependency for baseline inventory completeness.

## 7) Open Decisions (FGD2‑critical)
Sources: [`National Climate Adaptation Information Framework.md`](ψ/writing/2025-11_DCCE-CRDB/output/National%20Climate%20Adaptation%20Information%20Framework.md:57), [`Feature-Driven Data Governance Strategy v3 (2026-03-05).md`](ψ/writing/2025-11_DCCE-CRDB/output/Feature-Driven%20Data%20Governance%20Strategy%20v3%20(2026-03-05).md:185), [`FGD2_Slide_Deck_Guide.md`](ψ/writing/2025-11_DCCE-CRDB/output/FGD2_Slide_Deck_Guide.md:229)

1) **Phase 1 MVP priority** (which 2–4 MVPs)
2) **Sitemap option** (thematic vs user‑journey vs hybrid)
3) **Catalog‑first vs host‑first** stance
4) **Canonical boundary** + crosswalk ownership
5) **Endorsement authority** for recommended baselines
6) **Publishing rails** decisions (Open vs GDX vs internal)

## 8) Key Risks & Watchpoints
Source: [`CRDB - Work Status Brief.md`](ψ/writing/2025-11_DCCE-CRDB/output/CRDB%20-%20Work%20Status%20Brief.md:33)

- **ADPC data availability** delays can empty baseline inventory.
- **Stakeholder engagement** quality affects validation of use cases and MVPs.
- **Complexity creep**: NCAIF must remain legible for non-technical stakeholders.

## 9) Immediate Next Actions (Onboarding‑Ready)
1) **Confirm Phase 1 MVP shortlist** and the **sitemap choice** (use FGD2 prompts).
2) **Draft the recommended baseline registry schema** (owner, purpose, scale, limitations, versioning).
3) **Define canonical boundary** and crosswalk governance owner(s).
4) **Stand up a minimal catalog template** (business glossary + technical metadata split).

---

## Reference Index (Primary Artifacts)
- [`CRDB - Implementation Plan.md`](ψ/writing/2025-11_DCCE-CRDB/output/CRDB%20-%20Implementation%20Plan.md:1)
- [`CRDB - Work Status Brief.md`](ψ/writing/2025-11_DCCE-CRDB/output/CRDB%20-%20Work%20Status%20Brief.md:1)
- [`National Climate Adaptation Information Framework.md`](ψ/writing/2025-11_DCCE-CRDB/output/National%20Climate%20Adaptation%20Information%20Framework.md:1)
- [`Feature-Driven Data Governance Strategy v3 (2026-03-05).md`](ψ/writing/2025-11_DCCE-CRDB/output/Feature-Driven%20Data%20Governance%20Strategy%20v3%20(2026-03-05).md:1)
- [`NCAIF_Use_Cases.md`](ψ/writing/2025-11_DCCE-CRDB/output/NCAIF_Use_Cases.md:1)
- [`Conceptual Data Model for climate risk and adaptation data system.md`](ψ/writing/2025-11_DCCE-CRDB/output/Conceptual%20Data%20Model%20for%20climate%20risk%20and%20adaptation%20data%20system.md:1)
- [`FGD2_Slide_Deck_Guide.md`](ψ/writing/2025-11_DCCE-CRDB/output/FGD2_Slide_Deck_Guide.md:1)

