# CRDB Claim Register

## Purpose

This ledger tracks **reusable project claims**: intermediate statements that connect evidence to decisions and deliverables. It formalizes the "claim" object type defined in [`plans/2026-03-27-crdb-oracle-project-work-cycle-architecture-plan.md`](plans/2026-03-27-crdb-oracle-project-work-cycle-architecture-plan.md) for the CRDB context.

## Usage and maintenance

- Capture claims that are **actually used** in deliverables, meeting narratives, or decision logs.
- Keep wording **exact and quotable**; this is the canonical formulation for reuse.
- When evidence or stance changes, add a **new claim ID** rather than silently rewriting an old claim.
- Use the **Status** field to mark whether a claim is active, revised, or retired.
 - Link the claim’s first appearance (when known) in the neutral staging timeline: [`CRDB-Project-History-Timeline.md`](ψ/incubate/DCCE/CRDB/output/CRDB-Project-History-Timeline.md)

## Claim table

| Claim ID | Claim (exact wording) | Supporting evidence | Opposing / limiting evidence | Confidence | Related decisions | Related deliverables | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| C-001 | DCCE should act as architect and librarian for national climate adaptation information, not as a heavy platform builder in Phase 1. | E-002 (CDM conceptual model), E-003 (NCAIF narrative), E-015 (execution gaps note), E-020 (progress-meeting decisions) | Org-structure and platform-dependency uncertainties in E-023 and E-024 | High | Phase 1 architecture and MVP stance in [`phase1_decision_log.md`](ψ/incubate/DCCE/CRDB/output/phase1_decision_log.md) | D-001 (management evidence pack), D-002 (interim report narrative), future governance notes | Active | Central framing for CRDB scope control and expectation management; informs how project-management tooling must behave (advisor, not platform). |
| C-002 | Baseline endorsement is a core trust mechanism and must be explicitly governed, not left as an implied technical property of datasets. | E-002 (CDM), E-008 (NCAIF use cases), E-011 (stakeholder needs v2), E-015 (execution gaps), E-018 (Pack A risk-map extraction) | Limited concrete examples of baseline disputes; pending future workshops | Medium-high | Governance gates and endorsement authority decisions in [`phase1_decision_log.md`](ψ/incubate/DCCE/CRDB/output/phase1_decision_log.md) | Future baseline registry schema, governance role-mapping notes, management packs | Active | Drives the need for clear publishing rails, endorsement panels, and change logging. |
| C-003 | A catalog-first, workflow-pattern-first architecture is safer for Phase 1 than a platform-first build, given evidence, dependencies, and governance capacity. | E-003 (NCAIF narrative), E-008 (use cases), E-011 (stakeholder needs), E-019 (UX benchmark), E-020 (progress-meeting decisions) | Future DCCE Digital Tech initiatives may eventually justify some platform features; not yet confirmed for this phase | High | Architecture and sitemap stance in [`phase1_decision_log.md`](ψ/incubate/DCCE/CRDB/output/phase1_decision_log.md) | D-001, D-002, NCAIF sitemap and MVP materials | Active | Anchors the project-management ecosystem against over-scoping automation or opaque orchestration. |

| C-004 | If CRDB delivers only a website surface without a conceptual data model (mental model), the system will become static and quickly lose usefulness; therefore CDM and data/logic traceability must be treated as the backbone, with the website as a presentation layer. | E-021 (Dir Toey progress meeting summary), E-004 (Section 1 CDM/MVP evidence analysis), E-002 (CDM) | Potential future platform build by Digital Tech group may shift implementation, but does not remove CDM need (E-024) | High | Architecture stance and MVP constraints in [`phase1_decision_log.md`](ψ/incubate/DCCE/CRDB/output/phase1_decision_log.md) | D-001 (management evidence pack), D-004 (governance role mapping), D-006 (workshop package), future CDM deliverables | Active | This claim is quotable and sponsor-facing; use it to justify why CRDB spends effort on CDM, catalog, and governance rails. |

| C-005 | The April 30 CRDB workshop should act as a "bridge" (baton pass) from the earlier TMD/WMO baseline meeting to the late-May NFCS validation workshop: **build on** baseline outputs and shift from dataset identification to synthesis via active breakouts. | E-025 (workshop strategy note), E-021 (Dir Toey workshop logistics + morning/afternoon split) | Risks: stakeholder fatigue if the bridge narrative is not explicit; limited time; coordination uncertainty with parallel initiatives (E-024) | Medium-high | Workshop positioning and Phase 1 stance in [`phase1_decision_log.md`](ψ/incubate/DCCE/CRDB/output/phase1_decision_log.md) | D-006 (workshop invite + logistics package), D-001 (management evidence pack) | Active | Use as a facilitation design constraint: “build, don’t repeat” + “breakouts produce missing outputs.” |

## Practical reading order

1. Use this file when drafting narrative or governance notes that make **strong normative statements**.
2. For each claim:
   - trace back to evidence via IDs in [`CRDB-Evidence-Registry.md`](ψ/incubate/DCCE/CRDB/output/CRDB-Evidence-Registry.md)
   - cross-check decisions in [`phase1_decision_log.md`](ψ/incubate/DCCE/CRDB/output/phase1_decision_log.md)
   - see where the claim surfaces in the deliverable map via [`CRDB-Deliverable-Map.md`](ψ/incubate/DCCE/CRDB/CRDB-Deliverable-Map.md)
