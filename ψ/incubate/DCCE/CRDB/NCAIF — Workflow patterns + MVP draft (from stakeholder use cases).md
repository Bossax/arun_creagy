---
status: archived
tags:
  - NCAIF
  - workflow
  - MVP
  - FGD2
created: 2026-03-04
last_updated: 2026-03-04
project:
  - DCCE_CRDB
type:
  - artifact
source_material:
  - src/01_Projects/2025-11_DCCE-CRDB/output/NCAIF_Use_Cases.md
  - src/03_Evergreens/Typology of actionable climate information .md
---


## Purpose

Distill the growing list of use cases into:

1) **3–4 repeatable workflow patterns** (cross-cutting user journeys)
2) **2–4 MVP candidates** that can serve many use cases

This supports internal alignment and FGD2 discussions (what can be delivered in 1–2 years).

Primary input: updated use cases in [`src/01_Projects/2025-11_DCCE-CRDB/output/NCAIF_Use_Cases.md`](src/01_Projects/2025-11_DCCE-CRDB/output/NCAIF_Use_Cases.md:1)

Typology reference: [`src/03_Evergreens/Typology of actionable climate information .md`](obsidian://open?vault=src&file=03_Evergreens%2FTypology%20of%20actionable%20climate%20information%20)

---

## A) Workflow patterns (cross-cutting)

### Pattern P1 — “Curated briefing pack” (policy / decision / budget)

**Why it exists**

- Users repeatedly need **exportable, decision-ready packaging** (not only interactive maps).

**Primary actors**

- Policy makers / planners (UC-03)
- LAO / budget holders (UC-03b)
- Infrastructure planners (UC-07)
- NESDC macro team (UC-09)

**Canonical steps**
1. Choose area (province / LAO / corridor) + time horizon.
2. Pull “recommended baselines” (hazard + exposure + vulnerability) with metadata.
3. Generate a **1–2 page pack** (maps + numbers + assumptions + limitations).
4. Route through publish/review workflow if external.

**Key data inputs**
- Boundary + crosswalk (admin vs LAO vs EA)
- Hazard layers (historic + probabilistic + projected)
- Exposure & vulnerability indicators
- Interpretation text + limitations statements

**Outputs**
- Printable / shareable PDF/slide + machine-readable export (tables)

**Typology mapping**
- Use: Plan; Fund; Motivate & communicate
- Information: Broad trends & patterns + Detailed data & results + Data improvement & guidance

**Use cases covered**
- UC-03, UC-03b, UC-07, UC-09

---

### Pattern P2 — “Event → impact → loss/damage” post-event assessment

**Why it exists**

- DDPM event impact data has lag/noise; multiple users need **standardization** and **truth vs relief** clarity.

**Primary actors**

- DDPM + LAO reporting chain (UC-01)
- NESDC L&D framing + economic impact analysis (UC-09)
- NSO exposure overlays for affected areas (UC-08)

**Canonical steps**
1. Create/select event record (where/when/hazard; operational declaration context).
2. Ingest “impact observations” (people/assets/damages) with freshness + validation flags.
3. Enrich with baseline exposure layers (population, establishments, agriculture).
4. Produce standardized report + export; revise as data updates.

**Key data inputs**
- Event registry + schema
- Impact observation schema + reference costs
- Boundary/version governance
- Validation flags + revision history

**Outputs**
- Post-event impact report (tables/maps)
- Loss & damage summary (relief vs estimated true loss, if feasible)

**Typology mapping**
- Use: Plan; Fund; Take action
- Information: Detailed data & results + Data improvement & guidance

**Use cases covered**
- UC-01, UC-09, UC-08

---

### Pattern P3 — “Finding and agreeing on the official dataset” (clearinghouse)

**What this pattern solves**

Different agencies often publish different numbers for the same thing (for example: population, hazard maps, economic indicators). Nobody wants to take the risk of saying “this one is correct”.

This pattern describes how NCAIF helps DCCE and partners:

- find all relevant datasets,
- compare them, and
- clearly say which one is **recommended for use** (and under what conditions), without copying all data into one central database.


**Who is involved**

- DCCE “central data” / governance team.
- NXPO and other policy integrators.
- Data‑producing agencies (e.g. NSO) and downstream users.


**Typical steps**
1. **Search for candidates** — Use the data catalog to find all datasets for one topic (for example: “population baseline” or “flood hazard map”).
2. **Compare and understand differences** — For each dataset, record in simple language: where it comes from (agency/method), what area/time it covers, how often it is updated, and known limitations/caveats.
3. **Agree on a recommended dataset** — For each topic, DCCE (with partners) chooses one dataset as “recommended for this purpose”, and writes: when it should be used, when it should **not** be used, and how to interpret it safely (especially uncertainty).
4. **Publish the decision and keep history** — Add the recommendation to a small “official baseline list” that is easy to browse in the catalog/portal, versioned (old recommendations are kept, not deleted), and linked back to the original data provider.


**What data this pattern needs**

- Metadata and preview for each candidate dataset: owner, coverage, update cycle, access URL, basic quality notes, and known issues.
- A simple registry of “recommended baselines” with version history.


**What comes out**
- A public (or internal) page that answers: “Which dataset should I use for X?”, “Who owns it?”, and “What are the limitations?”
- Clear separation between: **where the data lives** (source agency), and **who recommends it for which purpose** (DCCE + partners).


**How this supports the typology**

- Use: Understand; Plan
- Information: Data improvement & guidance

**Use cases covered**
- UC-10, UC-08, cross-cutting for most other UCs

---

### Pattern P4 — “Uncertainty-safe risk analysis for advanced users”

**Why it exists**
- Advanced users (banks, some planners) require probabilistic data; misuse risk is high.

**Primary actors**
- Financial sector analysts (UC-11)
- Technical analysts in agencies (supporting UC-07, UC-02)

**Canonical steps**
1. Select scenario + probability semantics (return periods, exceedance probabilities).
2. Align assets to a spatial reference (geocoding/crosswalk).
3. Compute exposure + (optionally) loss using damage functions.
4. Generate uncertainty-safe interpretation notes for outputs.

**Key data inputs**
- Probabilistic hazard layers with explicit semantics
- Asset registries / geocoding
- Damage-function library (even a roadmap)

**Outputs**
- Portfolio/asset exposure and loss summary (with uncertainty guidance)

**Typology mapping**
- Use: Plan; Fund
- Information: Detailed data & results + Data improvement & guidance

**Use cases covered**
- UC-11 (and enables better quality for other UCs)

---

## B) MVP candidates (2–4) aligned to the patterns

### MVP-1 — NCAIF “Briefing Pack Generator” (export-first)

**Serves patterns**: P1 (direct), supports P2/P4 (as export packaging) <!--comment: out of project scope-->

**What it is**
- A small set of standardized, exportable templates (PDF/slide + table export) for:
  - provincial risk profile  
  - LAO budget justification
  - corridor/infrastructure exposure summary
  - macro L&D summary (as feasible)

**Phase 1 feasibility**
- High: can start with limited datasets and strong caveats.

**Minimum required datasets**
- Canonical boundaries + crosswalk guidance
- Core hazard layers + baseline exposure/vulnerability indicators

**Governance prerequisites**
- Limitations statement required
- Draft → review → publish (if public)
- “3-depth” wording for audiences (policy/practitioner/public)

**Success metric**
- Reduced ad-hoc requests; increased reuse of standard packs.

---

### MVP-2 — Event + Impact schema + Post-event reporting pack (L&D-ready)

**Serves patterns**: P2

**What it is**
- A standardized event/impact record model + exports:
  - consistent “where/when/what/affected”
  - freshness and revision history
  - validation flags

**Phase 1 feasibility**
- Medium: depends on DDPM/LAO reporting flow, but can start as a schema + cataloged example + pilot with historic events.

**Minimum required datasets**
- Boundaries
- Event registry stub
- Impact observation template

**Governance prerequisites**
- Data quality screening rules (minimal)
- Explicit timeliness/uncertainty labeling

**Success metric**
- Comparable post-event reports across provinces/events; clarity on relief vs impact.

---

### MVP-3 — Baseline “Recommended Dataset Registry” (clearinghouse + endorsement)

**Serves patterns**: P3

**What it is**
- A small authoritative list of “recommended baselines” with:
  - provenance, version, intended use
  - uncertainty semantics
  - limitations statement
  - steward/contact

**Phase 1 feasibility**
- High as a documentation + metadata deliverable; can be implemented in the spreadsheet catalog and later moved to a portal.

**Minimum required datasets**
- None beyond metadata; links to authoritative sources are acceptable.

**Governance prerequisites**
- Decision-rights: who can endorse
- Audit trail: superseded baselines retained

**Success metric**
- Reduced “competing numbers” and repeated disputes over baselines.

---

### MVP-4 — Uncertainty guidance pack + “probabilistic layer standard”

**Serves patterns**: P4 (and reduces misuse risk across the portfolio)

**What it is**
- A lightweight standard for publishing probabilistic layers:
  - required metadata fields
  - how to interpret (what it does/does not mean)
  - examples of common misuse

**Phase 1 feasibility**
- High (documentation + governance gate), even before full tooling exists.

**Minimum required datasets**
- Existing probabilistic flood maps (even if linked) + one worked example.

**Governance prerequisites**
- Limitations/uncertainty statement is mandatory for publication.

**Success metric**
- Fewer misinterpretations; more consistent downstream analysis.

---

## C) Notes for integrating into FGD2 decision prompts

Decisions these MVPs force explicitly:

- Canonical boundaries + crosswalk owner
- Catalog-first / clearinghouse stance
- Endorsement authority (role/title)
- Minimum uncertainty/limitations standard for any published layer

These align with the “must decide” list in [`src/01_Projects/2025-11_DCCE-CRDB/output/NCAIF_Use_Cases.md`](src/01_Projects/2025-11_DCCE-CRDB/output/NCAIF_Use_Cases.md:303)
