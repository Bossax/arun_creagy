# CRDB Enhancement Concept Note — Thaiwater Data Governance Lessons

## 1. Purpose

Use the Hydroinformatics Institute (Thaiwater) data governance framework as a benchmark to sharpen CRDB Phase 1 deliverables (NCAIF, CDM, inventories, governance) within the existing TOR. This is a concept note for human review, not an implementation plan.

## 2. TOR anchor (what we must deliver)

Key clauses from [`CRDB - TOR.md`](ψ/incubate/DCCE/CRDB/inbox_source/CRDB - TOR.md):

- **5.2 – NCAIF & data management structure**: benchmark foreign platforms; describe DCCE structure; produce a Draft NCAIF and Draft Data Management Structure (sources, responsible agencies, mechanisms, link to CCE Center), refined via FGDs and public hearing.
- **5.3 – Inventories & MVD**: build information product and baseline data inventories with rich metadata; design a Minimum Viable Dataset (MVD) and Loss & Damage reporting form, test on ≥3 events; perform gap analysis; provide policy and technical recommendations.
- **5.5 – Knowledge sets**: review key studies (≥10) and synthesize into accessible formats and media.

Phase 1 decisions in [`phase1_decision_log.md`](ψ/incubate/DCCE/CRDB/output/phase1_decision_log.md) lock:

- MVP‑3 (recommended dataset registry) + MVP‑2 (disaster data ingestion + Loss & Damage groundwork) as Phase 1 core.
- Hybrid sitemap (workflow‑pattern‑first) and **catalog‑first** architecture.
- Publishing rails: open / G2G / internal.
- Governance gates G1–G5 (classification, metadata+preview, baseline endorsement, boundary/crosswalk, event schema with timeliness & flags).

The Thaiwater-inspired enhancements below are framed to sit inside this TOR + decision envelope.

## 3. In-scope enhancement themes (Thaiwater → CRDB)

### 3.1 Reference standards layer

**Concept**

Create an explicit “reference information” layer that NCAIF and the CDM both depend on, mirroring Thaiwater’s units/codes appendices.

**Content**

- Boundary systems and crosswalks (admin, LAO/municipality, EA) and their governance.
- Agency codes for key partners (NSO, DDPM, RID, etc.).
- Canonical indicators and units.
- Standardized update-frequency / interval vocabulary.

**TOR fit**
- Required implicitly by 5.3.4–5.3.5 (metadata-rich inventories) and 5.2.3 (data management structure).
- Strengthens governance gate G4 (boundary+crosswalk) and supports G1–G3。

>[!verdict] My verdict
>This is legit. The reference layer applies to common attributes shared across any types of dataset. The attributes are usually for space, time, institutional orientations, datum (scientific), and tags/ names of common entities. 

### 3.2 Observation envelope & MVD semantics

**Concept**

Adopt a generic “observation envelope” pattern (metadata + observation payload) in the CDM, inspired by Thaiwater’s rainfall and station schemas.

**Use in CRDB**

- Loss & Damage reporting form (5.3.6–5.3.7).
- Any recurring hazard/impact metrics appearing in inventories and knowledge sets.

Envelope fields (conceptual): provider, document time, dataset type, measure time, create/update time, location/entity, variable, value, unit, qualityFlag, qualityControlLevel.

**TOR fit**

- In scope as conceptual schema + templates supporting MVD and forms.
- Out of scope only if interpreted as requiring a full production database / ETL system (which we avoid in Phase 1).

>[!verdict] My verdict
>- Loss and Damage schema will need to be design down to "logical level" similar to "rainfall" data dictionary schema. However, we cannot adopt observation data's schemas as is since loss and damage data is not the same as earth observation data. 
> - Forms will be designed after because the design has to depend on 1. DDPM practice of data collection and reporting 2. The process of importing DDPM relevant data fields into DCCE's data system


### 3.3 Exchange posture & publishing rails

**Concept**

Make CRDB’s exchange posture explicit, using Thaiwater’s online/offline logic but staying within the catalog‑first, link‑first stance.

**Use in CRDB**
- In the data management structure and inventories, state that CRDB Phase 1:
  - Links to existing APIs or file services where they already exist (risk map, data.go.th, DDPM, NSO).
  - Supports file/template-based exchange (CSV, Excel) for MVD and manual ingestion.
  - Routes everything through the three rails: open / G2G / internal-only.

**TOR fit**

- Directly supports 5.2.3 (mechanisms), 5.3.4–5.3.5 (formats), and 5.3.9 (technical recommendations).
- Does not require building new APIs; it clarifies and disciplines how data flows conceptually.

### 3.4 Data Quality Framework (QC levels & flags)

**Concept**

Formalize a cross-domain Data Quality Framework, inspired by Thaiwater’s QC levels and flags, tied to existing governance gates.

**Use in CRDB**

- Define 2–3 QC levels (e.g. ingestion checks, agency‑validated, cross‑domain review).
- Define a small, general QC flag vocabulary (e.g. Removed, Suspect, Estimated, Missing), adapted to multi-hazard, multi-sector context.
- Require these in:
  - Loss & Damage MVD and reporting forms.
  - Key baseline indicators in the registry.
  - Any numbers that appear in NCAIF decision‑support products.

**TOR fit**

- Fits 5.3.1–5.3.2 (documenting limitations) and 5.3.6–5.3.8 (MVD quality + gap analysis).
- Implements governance gate G5 (event schema with timeliness/flags) in a clear, reusable way.

>[!verdict] My verdict
>Agree. We should have QC frameworks starting with key products and services.
>
Need to think further since the baseline data inventory (data catalog in data architecture term) from TOR 5.3.5 will contain many many datasets which we are not be able to set quality standards for every dataset groups

### 3.5 Governance control flows & repository

**Concept**

Move from generic governance “principles” to concrete flows and an indexed repository, echoing Thaiwater’s governance body/steward and standard‑revision flows.

**Use in CRDB**
- Flows:
  - Dataset onboarding → classification & sensitivity → metadata/QC check → rail assignment → baseline endorsement (where applicable) → publication.
  - Schema/indicator revision → proposal → review (central team + stewards) → approval (endorsement panel) → update of NCAIF and inventories.
- Roles (aligned with `phase1_decision_log.md`):
  - DCCE central data team as interim governance body.
  - Data stewards in key partner agencies.
  - Baseline endorsement panel (central + source‑agency co‑signature).
- Repository index:
  - Single note indexing TOR, decision log, governance notes, QC framework, inventories, and PM ledgers as governance evidence.

>[!verdict] My verdict
>- Ownership of data domains of the CDM and the domains of NCAIF platform needs to be decided too. 

**TOR fit**

- Squarely in 5.2.3 (data management structure) and 5.3.9 (policy/technical recommendations).
- Also supports clarity and traceability for 7.x deliverables.

### 3.6 NCAIF information architecture slots

**Concept**

Reflect these elements in NCAIF’s sitemap and content structure, as Thaiwater surfaces reference, standards, QC, and governance sections.

**Use in CRDB**

- Add NCAIF slots for:
  - Data standards and governance (reference codes, QC, governance flows, rails).
  - “How to read this data” pages for key maps/indices (units, baselines, QC meaning, appropriate use context).

**TOR fit**

- Fully in scope under 5.2.1–5.2.3 as part of the Draft NCAIF; also supports dissemination and knowledge sets (5.4, 5.5).

>[!verdict] My verdict
>- Since NCAIF is more like an information website mixed with many tiers of data products and services, the Data standards and governance in the same manner as Thaiwater.net (basically technical) should be inside data catalog page (people who visit this page mostly have technical background to understand data standards)

## 4. Out-of-scope but useful future options

Clearly beyond the current contract, but worth recording as Phase 2+ directions (for 5.3.9 recommendations):

- A live, Thaiwater‑level API platform with standardized JSON schemas and secured exchange for all CRDB domains.
- Automated, system‑side QC engines beyond manual checks and simple scripts.
- A central physical data warehouse / lakehouse implementation; current TOR only requires conceptual/logical architecture and inventories.

## 5. Schematic workflow (concept)

High-level flow, Thaiwater-inspired but TOR-bounded:

1. **Sources & evidence**: external systems (risk maps, NFCS, statistics, DDPM, sectoral systems) and studies (5.5.1–5.5.2).
2. **CDM + observation envelopes**: conceptual entities and relationships for climate, hazard, exposure, vulnerability, impact, response; standard envelope for any observation/record.
3. **Inventories & baseline registry**: products and datasets recorded with reference codes, metadata, QC level, and publishing rail; MVD and Loss & Damage forms as structured special cases.
4. **Governance flows & rails**: dataset and schema changes move through defined flows with clear decision points and documented evidence; rails govern where and how data is published.
5. **NCAIF & knowledge products**: NCAIF pages and 5.5 knowledge sets draw from the registry and CDM, exposing QC and limitations to users in a Thaiwater-like, standards-aware way.

This keeps CRDB aligned with Thaiwater’s governance strengths while staying within the scope, objectives, and Phase 1 decisions already agreed with DCCE.



>[!verdict] My verdict
In overall, also connect the governance of use cases and data and information product and services development with data governance and standards too
