# CRI Claim Register

## Purpose

This ledger tracks **reusable project claims** for the CRI project: intermediate statements that connect evidence to decisions and deliverables (for example, assertions about how the CRI Impact Index should be interpreted, or how Phase 2 capacity profiles should behave). It mirrors the claim object pattern from [`ψ/incubate/DCCE/CRDB/CRDB-Claim-Register.md`](ψ/incubate/DCCE/CRDB/CRDB-Claim-Register.md) but is scoped to **DCCE / CRI**.

## Usage and maintenance

- Capture claims that are **actually used** in CRI deliverables, public hearing narratives, decision notes, or implementation guidance.
- Keep wording **exact and quotable**; this is the canonical formulation for reuse across CRI outputs.
- When evidence or stance changes, add a **new claim ID** rather than silently rewriting an old claim.
- Use the **Status** field to mark whether a claim is active, revised, or retired.
- Where possible, link the claim’s first appearance (when known) in any CRI-neutral staging timeline or history note introduced later.



## Practical reading order

1. Use this file when drafting CRI narrative or governance notes that make **strong normative statements**.
2. For each claim, once populated:
   - trace back to evidence via IDs in [`output/CRI-Evidence-Registry.md`](ψ/incubate/DCCE/CRI/output/CRI-Evidence-Registry.md)
   - cross-check decisions in CRI decision / change logs
   - see where the claim surfaces in the deliverable map via [`CRI-Deliverable-Map.md`](ψ/incubate/DCCE/CRI/CRI-Deliverable-Map.md)



> [!pattern]
> Claims should be grounded in artifacts registered in the CRI evidence registry and coverage map. Avoid speculative or purely aspirational statements.

## Claim table

| Claim ID   | Claim (exact wording) | Supporting evidence | Opposing / limiting evidence | Confidence | Related decisions | Related deliverables | Status | Notes |
|-----------|------------------------|---------------------|------------------------------|------------|-------------------|----------------------|--------|-------|
| C-CRI-001 | The CRI should be presented primarily as a **multi-dimensional profile** (impact, capacity tiers, data-richness/confidence), not as a single 1–76 ranking. | E-CRI-012, E-CRI-013 | (none recorded yet; future feedback from Hearing 2 or DCCE steering may refine) | Medium | (to be linked once CRI Phase 2 methodology revisions are frozen) | D-CRI-002, D-CRI-003 (once mapped) | Draft | Synthesised from Hearing 1 discussion where stakeholders requested profiles, breakdowns by capacity type, and radar/profile-style visualisations rather than a single rank.
| C-CRI-002 | **Capacity profiles in Phase 2 are baseline indicators of structural readiness, not performance audits**, and must be framed as support for capacity-building and access to funding, not as a tool to penalise local authorities. | E-CRI-012, E-CRI-013, E-CRI-015 | (none recorded yet; watch for future concerns from local authorities or MOI/DLA) | Medium | (to be linked once capacity-profile governance note is formalised) | D-CRI-003, D-CRI-005 (once mapped) | Draft | Grounded in Hearing 1 concerns about audit risk and the clarification that capacity scores should signal where support and investment are needed, not serve as compliance scores.
| C-CRI-003 | The **Fiscal Relief component of the Impact Index is a proxy for fiscal vulnerability and budgetary strain, not a full measure of economic loss**, and low recorded relief should not be interpreted on its own as evidence of low climate risk. | E-CRI-013, E-CRI-014 | (none recorded yet; potential challenge if future analyses compare Fiscal Relief directly with modelled losses) | Medium | (to be linked once Phase 1 methodology is updated) | (to be linked to Phase 1 methodology and communication packs) | Draft | Derived from Hearing 1 questions on "real damage" vs relief, and the methodology note’s recommendation to treat Fiscal Relief as a policy- and eligibility-limited proxy rather than total loss.
| C-CRI-004 | For publication in Phase 2, **district-level (amphoe/khet) should be treated as the default spatial resolution** for CRI outputs, with tambon- or village-level detail only where data quality and form design support safe use, and aggregation rules prioritise interpretability and auditability. | E-CRI-012, E-CRI-014 | (none recorded yet; final resolution contract with DCCE may adjust) | Medium | (to be linked once spatial-resolution contract is agreed) | D-CRI-004 (once mapped) | Draft | Reflects Hearing 1 discussions on trade-offs between province, district and tambon resolution, and the methodology implication to prioritise robust district-level outputs while planning for future upgrades.
