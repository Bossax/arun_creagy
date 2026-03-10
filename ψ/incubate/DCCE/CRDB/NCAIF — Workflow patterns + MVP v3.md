---
status: current
tags:
  - NCAIF
  - workflow
  - MVP
  - FGD2
version: 3
created: 2026-03-09
last_updated: 2026-03-09
project:
  - DCCE_CRDB
type:
  - artifact
source_material:
  - src/01_Projects/2025-11_DCCE-CRDB/output/NCAIF_Use_Cases.md
  - src/01_Projects/2025-11_DCCE-CRDB/notes/Steering MVP directions.md
  - src/01_Projects/2025-11_DCCE-CRDB/output/NCAIF — Workflow patterns + MVP v2.md
  - src/01_Projects/2025-11_DCCE-CRDB/output/CRDB - TOR.md
  - src/01_Projects/2025-11_DCCE-CRDB/output/CRDB - Implementation Plan.md
---

# NCAIF — Workflow patterns + MVP v3 (procedural steps clarified)

## Purpose

Clarify that **workflow patterns** describe the **general procedural steps** data users take to achieve a use case, while **MVPs** are the **self‑contained entities** (products + rules + artifacts) that help users complete those steps. This v3 keeps the P1–P4 logic, but makes the workflow‑vs‑MVP distinction explicit and reframes **MVP‑2** as groundwork for DDPM data ingestion and Loss & Damage governance.

### Definitions (v3)

- **Workflow patterns**: the repeatable **procedural steps** users follow when they use data to do something (use cases). They are not products; they are the “how.”
- **MVPs**: the **self‑contained entities** (outputs + process + governance) that make those steps achievable. MVPs map closely to patterns, but express **deliverable products** and governance gates.

In practice, MVPs are **not so different** from workflow patterns; each MVP operationalizes a pattern so the steps can be executed safely and consistently.

---

## 0) Design constraints (continuity from v2 + new framing)

### C0.1 Mixed literacy → Tiered product strategy

**Tier 1 (default audience)**

- Policymakers, LAO staff, general internal staff.
- Needs **prescriptive answers**, not “choose your own adventure analysis.”
- Needs **export‑first** artifacts for budgeting and communication.

**Tier 2 (advanced audience)**

- Banks, NESDC macro analysts, technical analysts.
- Needs probabilistic semantics, richer metadata, and deeper access.

### C0.2 Accountability fear → “safe publishing” must be built‑in

For any public‑facing output, the MVP must include:

- limitations + uncertainty statements
- clear ownership / sign‑off roles
- draft → review → publish states (or an explicit operating rule)

### C0.3 Post‑event data reality → quarantine + revision

Post‑event impact data is **lagged, noisy, and revisable**; the system must model:

- validation flags
- revision history
- separation of “relief payouts” vs “estimated true loss”

### C0.4 MVP‑2 as groundwork for future development

MVP‑2 should be framed as the **groundwork for future development**: a deliberate effort to **ingest disaster‑related data from DDPM into DCCE’s boundary**, even if ingestion is not automatic. This creates the **data pipeline foundation** for tailoring disaster information products and establishing **data governance for the Disaster + Loss & Damage domain** in the CDM.

This aligns with the **Minimum Viable Dataset (MVD)** and the **Loss & Damage logical data model** in:

- [ψ/writing/2025-11_DCCE-CRDB/output/CRDB - TOR.md](ψ/writing/2025-11_DCCE-CRDB/output/CRDB%20-%20TOR.md)
- [ψ/writing/2025-11_DCCE-CRDB/output/CRDB - Implementation Plan.md](ψ/writing/2025-11_DCCE-CRDB/output/CRDB%20-%20Implementation%20Plan.md)

---

## A) Workflow patterns (procedural steps emphasized)

### Pattern P1 — Curated briefing pack (policy / budget / comms)

**Core need**: exportable, decision‑ready packaging.

**Procedural steps (general):**

1) Select area + time horizon.
2) Pull recommended baselines (hazard, exposure, vulnerability).
3) Generate a short briefing pack with assumptions/limitations.
4) Route through review → publish gate.

**Primary use cases**: UC‑03, UC‑03b, UC‑07, UC‑09.

---

### Pattern P2 — Event → impact → loss/damage (post‑event assessment)

**Core need**: standardize reporting with timeliness + quality flags.

**Procedural steps (general):**

1) Ingest DDPM event data into DCCE’s boundary (even if manual or batch).
2) Apply validation flags, revisions, and provenance logging.
3) Enrich with baseline exposure layers.
4) Produce a standardized post‑event report with explicit caveats.

**Primary use cases**: UC‑01, UC‑02, UC‑09.

---

### Pattern P3 — Recommended baseline endorsement (clearinghouse)

**Core need**: resolve “competing numbers” and publish “recommended for use” guidance without rehosting everything.

**Procedural steps (general):**

1) Find candidate datasets via catalog.
2) Compare coverage, method, limitations, and update cycles.
3) Endorse a recommended baseline for specific uses.
4) Publish recommendation + version history.

**Primary use cases**: UC‑08, UC‑10.

---

### Pattern P4 — Uncertainty‑safe analysis for advanced users

**Core need**: probabilistic layers are required by advanced users; misuse risk is high.

**Procedural steps (general):**

1) Select scenario + probability semantics.
2) Align assets to spatial reference and apply crosswalks.
3) Compute exposure/impact summaries.
4) Publish outputs with required uncertainty guidance.

**Primary use cases**: UC‑11; supports UC‑07.

---

## B) MVP candidates (v3)

### MVP‑1 — Curated Briefing Pack Service (Tier‑1, export‑first)

**Primary pattern**: P1

**What it is**

- A standard pack library (templates) + curated generation workflow operated by DCCE central data team.
- Outputs are “locked” and publishable only when mandatory caveats are included.

**Tier 1 deliverables (Phase 1)**

1) 3–5 standard pack templates (1–2 pages each).
2) “Pack must include” checklist (provenance, timeliness, limitations, owner).

---

### MVP‑2 — Disaster Data Ingestion + L&D Groundwork Gateway

**Primary pattern**: P2

**What it is**

- A **structured ingestion and quarantine gateway** for DDPM disaster data into DCCE’s boundary.
- Not necessarily automated; emphasizes **traceable intake**, validation flags, and revision history.
- Establishes **data governance for Disaster + Loss & Damage** as a CDM domain and sets the foundation for the **MVD / L&D logical model**.

**Phase 1 deliverables (groundwork)**

1) Minimal event registry + impact observation template aligned to MVD/L&D schema.
2) Intake and validation rules (timeliness labels, revision tracking, “relief vs estimated loss” separation).
3) A standard post‑event report export with caveats.

**Explicit linkage**

- Minimum Viable Dataset (MVD) requirements in [ψ/writing/2025-11_DCCE-CRDB/output/CRDB - TOR.md](ψ/writing/2025-11_DCCE-CRDB/output/CRDB%20-%20TOR.md).
- Loss & Damage logical model framing in [ψ/writing/2025-11_DCCE-CRDB/output/CRDB - Implementation Plan.md](ψ/writing/2025-11_DCCE-CRDB/output/CRDB%20-%20Implementation%20Plan.md).

---

### MVP‑3 — Recommended Baseline Registry (endorsement + audit trail)

**Primary pattern**: P3

**What it is**

- A small authoritative list of recommended baselines with metadata, usage guidance, and version history.
- Catalog‑first, link‑first: value is the endorsement decision, not re‑hosting.

---

### MVP‑4 — Uncertainty + Publishing Standard (tiered guidance)

**Primary pattern**: P4

**What it is**

- A lightweight standard required before probabilistic/projection layers can be published.
- Includes plain‑language guidance, minimum metadata fields, and a misuse example.

---

## C) Pattern × MVP mapping (v3)

| Pattern \ MVP | MVP‑1 Curated packs | MVP‑2 Disaster ingestion + L&D groundwork | MVP‑3 Baseline registry | MVP‑4 Uncertainty + publishing |
|---|---:|---:|---:|---:|
| P1 Curated briefing pack | **Primary** | Support (post‑event briefs) | Support | Support (mandatory caveats) |
| P2 Event → impact → loss/damage | Support (export) | **Primary** | Support (baseline overlays) | Support |
| P3 Baseline endorsement | Support | Support | **Primary** | Support |
| P4 Uncertainty‑safe analysis | Support | Support | Support | **Primary** |

---

## D) Decisions for FGD2 (updated)

1) Tiering stance: what is Tier 1 vs Tier 2 in Phase 1?
2) Operator model for Tier 1 packs: who generates and who can publish?
3) Endorsement authority: which role/title can publish “recommended baselines”?
4) Minimum publishing gate: limitations + uncertainty + review workflow (or explicit alternative).
5) Boundary/crosswalk ownership: which unit is canonical per flagship output.
6) MVP‑2 pipeline scope: what is in‑boundary ingestion vs out‑of‑scope automation for Phase 1?
