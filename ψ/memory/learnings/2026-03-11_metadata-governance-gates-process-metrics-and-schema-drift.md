# Metadata governance: gates + process metrics + schema drift

**Date**: 2026-03-11

## Learning

For climate data ecosystems (CRDB/CRI/BTR), “metadata management” is not a documentation task; it is the **execution layer** that makes governance policies real on assets.

Three complementary requirements recur across projects:

1) **Governance gates (publish safety)**: define a minimal set of metadata required to publish or endorse any dataset/product (classification, owner, cadence, spatial unit/boundary version, limitations statement, access path, review workflow). This is the catalog’s baseline purpose.

2) **Process/timeliness metadata (defensibility)**: for governance and resilience measurement, static “existence” facts (plan exists) are weak. Metadata must capture time-sensitive and process-oriented signals (last updated, revision frequency, disbursement timeliness, validation flags, revision history) to avoid creating authoritative-looking but non-actionable (or misleading) outputs.

3) **Schema↔documentation coupling (drift control)**: when a physical schema exists (e.g., ADPC platform), reference sheets/dictionaries are “metadata contracts.” If schema changes without versioning and update discipline, documentation becomes obsolete. Therefore, metadata models must be versioned and explicitly track alignment (or “pending schema” placeholders).

## Implication

Treat “metadata fields” as product requirements and map them directly to:
- publishing rails (Open/GDX/Internal)
- endorsement workflows
- boundary/crosswalk governance
- revision history and timeliness labeling

## Pointers

- CRDB gates and governance rails: [`ψ/incubate/DCCE/CRDB/inbox/active/dcce-crdb_knowledge_digest.md`](../../incubate/DCCE/CRDB/inbox/active/dcce-crdb_knowledge_digest.md:35)
- CRI process-metric critique: [`ψ/incubate/DCCE/CRI/inbox/writing_notes/Critique of CRI Phase 2.md`](../../incubate/DCCE/CRI/inbox/writing_notes/Critique%20of%20CRI%20Phase%202.md:25)
- BTR DRS dependency / drift risk: [`ψ/incubate/UNDP/BTR/inbox/writing_notes/Data Reference Sheet dependency on ADPC database schema.md`](../../incubate/UNDP/BTR/inbox/writing_notes/Data%20Reference%20Sheet%20dependency%20on%20ADPC%20database%20schema.md:21)

