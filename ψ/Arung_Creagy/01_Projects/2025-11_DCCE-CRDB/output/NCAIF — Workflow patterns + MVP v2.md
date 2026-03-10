---
status: current
tags:
  - NCAIF
  - workflow
  - MVP
  - FGD2
created: 2026-03-06
last_updated: 2026-03-06
project:
  - DCCE_CRDB
type:
  - artifact
source_material:
  - src/01_Projects/2025-11_DCCE-CRDB/output/NCAIF_Use_Cases.md
  - src/01_Projects/2025-11_DCCE-CRDB/notes/Steering MVP directions.md
  - src/01_Projects/2025-11_DCCE-CRDB/output/NCAIF — Workflow patterns + MVP draft (from stakeholder use cases).md
---

# NCAIF — Workflow patterns + MVP v2 (literacy-grounded)

## Purpose

Refine the MVP shortlist for FGD2 so that Phase 1 deliverables are **safe and usable** in Thailand’s observed **mixed climate + data literacy** context.

This v2 keeps the original workflow-pattern logic (P1–P4) but updates the MVP design with:

- a **tiered dissemination strategy** (prescriptive Tier 1 vs advanced Tier 2)
- a **catalog-first, link-first stance** (avoid duplicating national infrastructure)
- a **publishing safety posture** (limitations + review gates are “product requirements”)

Primary inputs:

- Use cases + constraints: [`NCAIF_Use_Cases.md`](src/01_Projects/2025-11_DCCE-CRDB/output/NCAIF_Use_Cases.md)
- MVP steering principles (grounded in interviews): [`Steering MVP directions.md`](src/01_Projects/2025-11_DCCE-CRDB/notes/Steering%20MVP%20directions.md)
- Prior v1 (preserved): [`NCAIF — Workflow patterns + MVP draft (from stakeholder use cases).md`](src/01_Projects/2025-11_DCCE-CRDB/output/NCAIF%20%E2%80%94%20Workflow%20patterns%20%2B%20MVP%20draft%20(from%20stakeholder%20use%20cases).md)

---

## 0) Design constraints (what interviews force us to do)

### C0.1 Mixed literacy → Tiered product strategy

**Tier 1 (default audience)**

- Policymakers, LAO staff, general internal staff.
- Needs **prescriptive answers**, not “choose your own adventure analysis.”
- Needs **export-first** artifacts for budgeting and communication.

**Tier 2 (advanced audience)**

- Banks, NESDC macro analysts, technical analysts.
- Needs probabilistic semantics, richer metadata, and deeper access.

Grounding signals (examples):

- LAO budget users need digestible evidence packs (DLA).
- MSDHS has no data science capacity; needs clear metadata + how-to-read guidance (MSDHS).
- TBA needs probabilistic/asset-level semantics but misuse risk is high (TBA).

### C0.2 Accountability fear → “safe publishing” must be built-in

For any public-facing output, the MVP must include:

- limitations + uncertainty statements
- clear ownership / sign-off roles
- draft → review → publish states (or an explicit operating rule)

Grounding: NXPO’s “accountability culture” around forecasts (NXPO) + FGD1 PR bottleneck.

### C0.3 Data reality (post-event) → quarantine + revision

Post-event impact data is **lagged, noisy, and revisable**; the system must model:

- validation flags
- revision history
- separation of “relief payouts” vs “estimated true loss”

Grounding: DDPM one-way reporting chain + late/incorrect reporting; NESDC “true loss vs relief” gap.

---

## A) Workflow patterns (v2: unchanged set, clarified intent)

### Pattern P1 — Curated briefing pack service (policy / budget / comms)

**Core need**: exportable, decision-ready packaging.

**v2 clarification**: treat “pack generation” as a **curated service** (operator model) for Tier 1; the public does not configure analysis.

Primary use cases: UC-03, UC-03b, UC-07 (Phase 1 stance), UC-09.

---

### Pattern P2 — Event → impact → loss/damage (post-event assessment)

**Core need**: standardize reporting with timeliness + quality flags.

**v2 clarification**: treat the pipeline as **ingest → screen/quarantine → revise**, not a clean real-time feed.

Primary use cases: UC-01, UC-02 (as briefing), UC-09.

---

### Pattern P3 — Recommended baseline endorsement (clearinghouse)

**Core need**: resolve “competing numbers” and publish “recommended for use” guidance without rehosting everything.

Primary use cases: UC-08, UC-10 (+ cross-cutting).

---

### Pattern P4 — Uncertainty-safe analysis for advanced users

**Core need**: probabilistic layers are required by advanced users; misuse risk is high.

Primary use cases: UC-11; supports UC-07 and improves correctness across the portfolio.

---



## B) MVP candidates (v2)

### MVP-1 — Curated Briefing Pack Service (Tier-1, export-first)

**Primary pattern**: P1

**What it is (v2)**

- A **standard pack library** (templates) + a **curated generation workflow** operated by DCCE central data team.
- Outputs are “locked” and publishable only when they include mandatory caveats.

**Tier 1 deliverables (Phase 1)**

1) 3–5 standard pack templates (1–2 pages each):
   - provincial risk profile (UC-03)
   - LAO/municipality budget justification pack (UC-03b)
   - post-event situation brief (lightweight output from MVP-2)
   - (optional) macro L&D summary framing (UC-09) as a narrative with explicit gaps
2) A minimum “pack must include” checklist:
   - provenance links (where data lives)
   - timeliness label
   - limitations/uncertainty statement
   - owner/contact

**Tier 2 expansion (Phase 2+)**

- Self-service pack generation for trained internal analysts (not public).

**Grounding signals**

- Budget justifications are required for LAO and are often constrained; exportable evidence is essential (DLA).
- Budget allocators reject “uncertain” costs; the pack must include “how to read uncertainty” in plain language (OTP).

**Success metric**

- Reduced ad-hoc requests; consistent reuse of standard packs.

---

### MVP-2 — Event + Impact Quarantine Gateway (revision + flags; L&D-ready)

**Primary pattern**: P2

**What it is (v2)**

- A standardized **event + impact schema** plus a reporting pack that makes “data reality” visible:
	  - lag/noise
	  - wrong categories
	  - revisions over time
	  - separation between “reported relief payouts” and “estimated loss”

**Tier 1 deliverables (Phase 1)**

1) Minimal event registry fields (ID, hazard type, start/end, affected admin units, declaration context).
2) Impact observation template with:
   - freshness timestamp
   - validation flags
   - revision history fields
3) Output: a standard post-event report export (tables + maps) with caveats.

**Tier 2 expansion (Phase 2+)**

- Methods registry for “estimated true loss” (proxy values, econometric coefficients), versioned and auditable.

**Grounding signals**
- One-way DDPM reporting chain cannot be ground-truthed centrally; quality flags must exist (DDPM).
- NESDC needs “true loss” and currently cannot obtain it reliably (NESDC).

**Success metric**

- Comparable post-event reporting across provinces/events with explicit uncertainty.

---

### MVP-3 — Recommended Baseline Registry (endorsement + audit trail; catalog-first)

**Primary pattern**: P3

**What it is (v2)**

- A small authoritative list of **recommended baselines** that answers: “Which dataset should I use for X?”
- Each baseline entry is metadata + link + guidance (not necessarily data hosting).

**Tier 1 deliverables (Phase 1)**

1) “Recommended baselines” list for 5–10 high-demand topics (start with floods + core socio-economic baselines).
2) For each entry:
   - owner/steward
   - coverage (area/time)
   - update cycle
   - access pathway (open / internal / GDX)
   - intended use + not-for-use
   - limitations/uncertainty statement
   - version history (superseded baselines retained)

**Tier 2 expansion (Phase 2+)**

- Workflow to compare competing datasets and record structured “differences and rationale.”

**Grounding signals**

- NSO links rather than duplicates where possible; tagging + metadata are the core value (NSO).
- NXPO’s verification gap: nobody wants liability for declaring “truth”; endorsement + caveats are required (NXPO).

**Success metric**

- Reduced disputes over baselines; faster decision workflows.

---

### MVP-4 — Uncertainty + Publishing Standard (tiered guidance)

**Primary pattern**: P4 (also a safety gate for P1–P3)

**What it is (v2)**

- A lightweight standard required before probabilistic/projection layers (and derived products) can be published.

**Tier 1 deliverables (Phase 1)**

1) “How to read this” plain-language guidance blocks (policy/practitioner/public versions).
2) Minimum metadata fields for probabilistic layers (return period semantics, exceedance probability, scenario/time horizon).
3) A worked misuse example (“100-year flood does not mean it happens everywhere in one year”).

**Tier 2 expansion (Phase 2+)**

- Technical annex standard for analysts (full methodology, validation notes, model provenance).

**Grounding signals**

- Analysts often treat probabilistic layers deterministically; this creates inflated impacts (TBA).
- Publishing predictive information triggers fear of blame; standards + disclaimers reduce risk (NXPO).

**Success metric**

- Fewer misinterpretations; consistent language in packs and catalog entries.

---



## C) Pattern × MVP mapping (v2)

| Pattern \ MVP | MVP-1 Curated packs | MVP-2 Event/impact gateway | MVP-3 Baseline registry | MVP-4 Uncertainty + publishing |
|---|---:|---:|---:|---:|
| P1 Curated briefing pack service | **Primary** | Support (as inputs) | Support | Support (mandatory caveats) |
| P2 Event → impact → loss/damage | Support (export) | **Primary** | Support (baseline overlays) | Support |
| P3 Baseline endorsement | Support (uses recommended list) | Support | **Primary** | Support |
| P4 Uncertainty-safe analysis | Support (pack interpretation) | Support | Support | **Primary** |

---

## D) What must be decided in FGD2 (to make v2 shippable)

1) **Tiering stance**: what is Tier 1 vs Tier 2 in Phase 1?
2) **Operator model** for Tier 1 packs: who generates and who can publish?
3) **Endorsement authority**: which role/title can publish “recommended baselines”?
4) **Minimum publishing gate**: limitations + uncertainty + review workflow (or explicit alternative).
5) **Boundary/crosswalk ownership**: which unit is canonical per flagship output.

