# Learning — Data Architecture Core Concepts (Mesh, Canonical Model, Medallion)

**Date**: 2026-03-10 (GMT+7)
**Context**: CRDB/NCAIF learning session — align governance + modeling language.

## 1) Data mesh (what it is)
Data mesh is a *responsibility architecture* that decentralizes data ownership to **domains**, while keeping **shared governance** centralized.

From [`ψ/inbox/Data Mesh Architecture Explained - AWS.md`](ψ/inbox/Data Mesh Architecture Explained - AWS.md:9): a mesh “unites disparate data sources” through centrally managed sharing and governance guidelines, while business functions retain control over access and formats.

### The 4 principles
From [`…Data Mesh Architecture Explained - AWS.md`](ψ/inbox/Data Mesh Architecture Explained - AWS.md:77):

1. **Distributed domain-driven architecture** — domain teams host/serve their datasets.
2. **Data as a product** — products must be discoverable, addressable, trustworthy (SLOs), self-describing.
3. **Self-serve data infrastructure** — platform team provides common tooling so domains don’t reinvent pipelines.
4. **Federated governance** — leadership defines global standards; domains apply locally with autonomy.

### Governance split (operating model)
- **Governance council**: sets policies (classification, standards, naming, minimum metadata).
- **Platform team**: runs catalog/access/logging/quality tooling; encodes policy into “paved roads.”
- **Domain teams**: publish data products + metadata; own SLAs; respond to consumers.

## 2) Conceptual / logical / physical modeling (where canonical fits)
From [`ψ/incubate/DCCE/CRDB/inbox/active/Conceptual vs Logical vs Physical Data Models.md`](ψ/incubate/DCCE/CRDB/inbox/active/Conceptual vs Logical vs Physical Data Models.md:32):

- **Conceptual model**: aligns stakeholders on core entities + relationships (business meaning).
- **Logical model**: adds attributes, keys, normalization (still tech-agnostic).
- **Physical model**: implements in a specific platform (tables, columns, indexes, constraints).

## 3) Canonical data model (CDM)
A canonical data model is a **shared representation** of core entities/relationships used for **integration**.

Purpose:
- Reduce pairwise mappings from O(n²) to O(n): each system maps to/from the canonical form.

Practical note:
- Canonical models require **versioning discipline** (deprecation windows, compatibility rules) to avoid breaking integrations.

## 4) Medallion architecture
Medallion architecture layers data by quality/lifecycle:

- **Bronze**: raw/landing, append-only, replayable.
- **Silver**: cleaned, conformed, validated, deduped.
- **Gold**: curated business-ready serving tables / aggregates.

Relation to mesh:
- Medallion is about *processing and quality progression*.
- Mesh is about *ownership and governance*.
- They can coexist: each **domain** can operate its own bronze/silver/gold inside the mesh.

## 5) Implications for CRDB/NCAIF
- Use mesh framing to define **domains** and “data product cards” (owner, SLA, metadata, access policy).
- Use conceptual models to lock down **meaning**, then evolve logical/physical layers safely.
- Use canonical model selectively for cross-domain or cross-system integration where reuse outweighs rigidity.
- Use medallion layering to keep ingestion and transformation disciplined without losing raw provenance.


---
*Added via Oracle Learn*
