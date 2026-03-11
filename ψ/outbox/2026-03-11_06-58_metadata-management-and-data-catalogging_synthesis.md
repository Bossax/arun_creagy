# Metadata management & data catalogging — synthesis (global inbox + project notes)

**Created**: 2026-03-11 06:58 (GMT+7)
**Scope**: Metadata management + data catalogging for DCCE climate data ecosystem work (CRDB / CRI / BTR). Source intake limited to **10 files total**, max **4 per folder**.

## Source set (10 files)

### Global inbox (4)
- [`ψ/inbox/Metadata in Data Governance.md`](../inbox/Metadata%20in%20Data%20Governance.md:1)
- [`ψ/inbox/What is a Data Catalog Definition, Features & Why it Matters in 2025.md`](../inbox/What%20is%20a%20Data%20Catalog%20Definition,%20Features%20&%20Why%20it%20Matters%20in%202025.md:1)
- [`ψ/inbox/What is Metadata Management Importance & Benefits 2025.md`](../inbox/What%20is%20Metadata%20Management%20Importance%20&%20Benefits%202025.md:1)
- [`ψ/inbox/6 Types of Metadata Explained Examples & Key Uses 2024.md`](../inbox/6%20Types%20of%20Metadata%20Explained%20Examples%20&%20Key%20Uses%202024.md:1)

### CRDB project inbox (3)
- [`ψ/incubate/DCCE/CRDB/inbox/writing_notes/Data System Artifact Guide.md`](../incubate/DCCE/CRDB/inbox/writing_notes/Data%20System%20Artifact%20Guide.md:1)
- [`ψ/incubate/DCCE/CRDB/inbox/writing_notes/Steering MVP directions.md`](../incubate/DCCE/CRDB/inbox/writing_notes/Steering%20MVP%20directions.md:1)
- [`ψ/incubate/DCCE/CRDB/inbox/active/dcce-crdb_knowledge_digest.md`](../incubate/DCCE/CRDB/inbox/active/dcce-crdb_knowledge_digest.md:1)

### CRI project inbox (2)
- [`ψ/incubate/DCCE/CRI/inbox/writing_notes/Critique of CRI Phase 2.md`](../incubate/DCCE/CRI/inbox/writing_notes/Critique%20of%20CRI%20Phase%202.md:1)
- [`ψ/incubate/DCCE/CRI/inbox/active/Process-based indicators for urban resilience - consensus.ai.md`](../incubate/DCCE/CRI/inbox/active/Process-based%20indicators%20for%20urban%20resilience%20-%20consensus.ai.md:1)

### BTR project inbox (1)
- [`ψ/incubate/UNDP/BTR/inbox/writing_notes/Data Reference Sheet dependency on ADPC database schema.md`](../incubate/UNDP/BTR/inbox/writing_notes/Data%20Reference%20Sheet%20dependency%20on%20ADPC%20database%20schema.md:1)

---

## 1) What “metadata management” is in governance terms (not tool terms)

From a governance lens, **metadata is the control surface** that makes policies executable on real data assets.

Key idea: policy (definition / usage / security / lineage) is abstract until it is attached to **specific datasets and fields** through metadata.

Practical stewardship responsibilities (condensed):
- define and document entities/attributes and their meaning
- identify relationships (business + technical)
- certify accuracy/completeness/timeliness *as a governed claim* (not a belief)
- record lineage/heritage and revision history

Anchors: [`ψ/inbox/Metadata in Data Governance.md`](../inbox/Metadata%20in%20Data%20Governance.md:9)

---

## 2) Data catalogging: what it is *for* (in this ecosystem)

Within CRDB/NCAIF, a catalog is not “a website list of datasets.” It is the **inventory + context layer** that enables:

1) discovery (“find what exists”)  
2) understanding (“what does it mean and how was it produced”)  
3) governance (“who owns it, what are the rules, what is publishable”)  
4) safe reuse (“what breaks if we change it; what downstream depends on it”)  

Modern catalogs tend to include (minimum viable): inventory, metadata storage, search, lineage, governance fields, collaboration/annotations, and quality/freshness signals.

Anchors: [`ψ/inbox/What is a Data Catalog Definition, Features & Why it Matters in 2025.md`](../inbox/What%20is%20a%20Data%20Catalog%20Definition,%20Features%20&%20Why%20it%20Matters%20in%202025.md:13)

---

## 3) Metadata types: use-case framing that prevents “metadata = schema only”

Using a “types → use cases” frame helps keep the catalog from becoming a static dictionary.

Six-type frame (high signal):
- **Technical**: structure + file/system properties
- **Governance**: classification, permissions, compliance, ownership
- **Operational**: pipeline/log/processing history and lineage signals
- **Collaboration**: discussions, tickets, annotations, decisions around an asset
- **Quality**: tests, freshness, completeness, verification flags
- **Usage**: access patterns, popularity, top consumers

Anchor: [`ψ/inbox/6 Types of Metadata Explained Examples & Key Uses 2024.md`](../inbox/6%20Types%20of%20Metadata%20Explained%20Examples%20&%20Key%20Uses%202024.md:13)

This maps cleanly to CRDB Phase 1 gates (see Section 5).

---

## 4) “Active metadata” vs “passive metadata”: the leverage point

Passive metadata: manually curated, static, brittle.

Active metadata: continuously captured/enriched from operations (queries, pipelines, quality checks), enabling automation (classification suggestions, lineage graphs, quality alerts, access workflows).

Two implementation implications:
- **Don’t over-index on tooling before defining minimum governance fields.** Tooling should automate the already-defined model.
- **Start with a policy-relevant subset**, then expand to active signals.

Anchors: [`ψ/inbox/What is Metadata Management Importance & Benefits 2025.md`](../inbox/What%20is%20Metadata%20Management%20Importance%20&%20Benefits%202025.md:63)

---

## 5) CRDB-specific synthesis: Phase 1 governance = “publish safely”

CRDB framing positions the system as **architect/librarian** (catalog + governance + conceptual modeling), not a full platform build. Governance is therefore about shipping **safe, usable, endorsed artifacts**.

From the CRDB digest, Phase 1 governance gates relevant to metadata/catalogging:
- **G1 Data classification**: Open / GDX / internal + privacy handling
- **G2 Minimum metadata + preview**: owner, cadence, spatial unit, limitations, access path
- **G3 Endorsement registry**: recommended baselines (authority, rationale, version history)
- **G4 Boundary + crosswalk governance**: canonical boundary + crosswalk ownership
- **G5 Event/impact schema governance**: timeliness, validation flags, revision history

Anchor: [`ψ/incubate/DCCE/CRDB/inbox/active/dcce-crdb_knowledge_digest.md`](../incubate/DCCE/CRDB/inbox/active/dcce-crdb_knowledge_digest.md:35)

### 5.1 Catalog-first + link-first (don’t duplicate rails)

Steering principle: **link to authoritative sources**, endorse and contextualize; avoid rehosting.

Implication: the catalog needs strong **provenance + access-path metadata** (where the asset lives; how to get it; what constraints apply), plus an explicit endorsement model.

Anchor: [`ψ/incubate/DCCE/CRDB/inbox/writing_notes/Steering MVP directions.md`](../incubate/DCCE/CRDB/inbox/writing_notes/Steering%20MVP%20directions.md:98)

### 5.2 Minimal artifacts set (catalog ≠ dictionary only)

The artifact guide partitions:
- baseline data inventory (catalog as structured spreadsheet; raw dataset registry)
- information product inventory (catalog of analytical products + lineage)
- technical data dictionaries (deep field-level for risk datasets)
- business glossary (term authority linked to NCAIF)

And explicitly notes: Risk datasets need more technical metadata (e.g., resolution/CRS), while some M&E datasets only need business metadata (existence + owner + description) for discovery.

Anchor: [`ψ/incubate/DCCE/CRDB/inbox/writing_notes/Data System Artifact Guide.md`](../incubate/DCCE/CRDB/inbox/writing_notes/Data%20System%20Artifact%20Guide.md:38)

---

## 6) CRI-specific synthesis: why metadata matters for defensible indices

CRI notes add a measurement nuance that is directly relevant to metadata governance:

**Binary “existence” indicators produce a Potemkin index** if you cannot show process, timeliness, and revision cycles.

This implies the catalog must treat “governance process” attributes as first-class metadata:
- revision frequency / last-updated timestamps
- timeliness of disbursement/procurement cycles
- coordination evidence (meeting cadence, after-action reviews)

Anchor: [`ψ/incubate/DCCE/CRI/inbox/writing_notes/Critique of CRI Phase 2.md`](../incubate/DCCE/CRI/inbox/writing_notes/Critique%20of%20CRI%20Phase%202.md:25)

The process-indicator research note supports:
- explicit taxonomy & tagging logic
- mandate/KPI-aligned classification rules to reduce subjectivity
- management-science proxies (timeliness, throughput, friction)

Anchor: [`ψ/incubate/DCCE/CRI/inbox/active/Process-based indicators for urban resilience - consensus.ai.md`](../incubate/DCCE/CRI/inbox/active/Process-based%20indicators%20for%20urban%20resilience%20-%20consensus.ai.md:47)

---

## 7) BTR-specific synthesis: DRS as “metadata contract” and drift risk

The BTR note frames the Data Reference Sheet (DRS) as the **user manual / metadata layer** for ADPC’s physical schema.

Key governance point: if schema changes, the DRS becomes obsolete unless there is a mechanism to keep it synchronized.

Implication for catalogging: treat schema ↔ documentation alignment as a governed lifecycle process (versioning + change control + “pending schema” placeholders).

Anchor: [`ψ/incubate/UNDP/BTR/inbox/writing_notes/Data Reference Sheet dependency on ADPC database schema.md`](../incubate/UNDP/BTR/inbox/writing_notes/Data%20Reference%20Sheet%20dependency%20on%20ADPC%20database%20schema.md:21)

---

## 8) A minimal “Phase 1 metadata model” proposal (for reading later)

This is framed as fields to capture in a baseline inventory spreadsheet or lightweight catalog, aligned to CRDB governance gates.

### 8.1 Asset identity & discovery
- Asset name (TH/EN)
- Asset type: dataset | indicator | map layer | document | model output
- Domain (NCAIF domain)
- Keywords/tags

### 8.2 Provenance & access path
- Owning agency / steward / contact
- Source system (data.go.th / GDX / internal / external)
- Access method (URL, API, request workflow)
- License / usage constraints

### 8.3 Technical minimum (for geospatial/risk datasets)
- Spatial unit / boundary version
- Resolution / scale
- CRS / format
- Temporal coverage + update cadence

### 8.4 Governance & safety
- Classification: Open | GDX | Internal
- Sensitivity/PII flag (Y/N + rationale)
- Limitations statement (required for publishing)
- Draft → review → publish status + approver roles

### 8.5 Quality + operational signals (start manual, evolve to active)
- Freshness label / last updated
- Validation flags / revision history
- Lineage summary (upstream sources, key transformations)

### 8.6 Endorsement registry fields (recommended baselines)
- Endorsed? (Y/N)
- Endorsing authority
- Version + effective dates
- Rationale (why this baseline)
- Compatibility notes (what it can/can’t be compared with)

---

## 9) What to do next (suggested next reading path)

If the next session continues this topic, the highest-leverage next step is to translate Section 8 into:
- a **catalog template** (spreadsheet or md schema), and
- a **decision log** for Phase 1 gates (which fields are required, by rail, and who approves).

Primary project anchor for that: [`ψ/incubate/DCCE/CRDB/inbox/active/dcce-crdb_knowledge_digest.md`](../incubate/DCCE/CRDB/inbox/active/dcce-crdb_knowledge_digest.md:87)

