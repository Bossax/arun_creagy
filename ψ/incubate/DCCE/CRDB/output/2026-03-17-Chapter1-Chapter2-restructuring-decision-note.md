# Chapter 1 and Chapter 2 restructuring decision note

Anchor file:
- [`ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim Report Writing Plan.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim%20Report%20Writing%20Plan.md)

Working draft for testing structural moves:
- [`ψ/incubate/DCCE/CRDB/output/2026-03-13-CRDB-Interim-Report-Section-1.6-1.12-Draft-th-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-13-CRDB-Interim-Report-Section-1.6-1.12-Draft-th-v2.md)

Reference draft to preserve:
- [`ψ/incubate/DCCE/CRDB/output/2026-03-13-CRDB-Interim-Report-Section-1.6-1.12-Draft-th-edited.md`](ψ/incubate/DCCE/CRDB/output/2026-03-13-CRDB-Interim-Report-Section-1.6-1.12-Draft-th-edited.md)

## Decision summary

### 1. Section 2.8 should not remain a report subsection

The current idea of a Chapter 2 subsection labeled as progress-status plus evidence gaps is better treated as a **pre-drafting analysis step** rather than a report section.

Reason:
- it is mainly for internal writing control;
- it helps the team prepare synthesis before prose drafting;
- if left inside the report structure, it risks turning the interim report into a meta-commentary about drafting readiness instead of a report on project progress.

Decision:
- remove Section 2.8 from the report-facing Chapter 2 outline;
- treat it as part of the pre-drafting analysis package linked from the anchor plan in [`ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim Report Writing Plan.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim%20Report%20Writing%20Plan.md).

### 2. Chapter 1 sections 1.6 and 1.7 should be split into descriptive material vs analytical result

The current content in Section 1.6 and Section 1.7 contains two different layers:

1. **descriptive current-state material**
   - what the DCCE website currently contains;
   - what the spatial risk-map product is;
   - what it shows, at what scale, and with what limitations.

2. **analytical implication for the architecture**
   - why fragmentation matters;
   - why a reorganizing layer is required;
   - why product reality constrains what Phase 1 can honestly claim.

Decision:
- move the **descriptive landscape material** into Chapter 2;
- keep the **analytical implications** in Chapter 1.

This preserves the logic of Chapter 1 as an argument about why NCAIF architecture had to change, while making Chapter 2 the proper home for the current product landscape review.

## Revised Chapter 1 to Chapter 2 division of labor

### What stays in Chapter 1

Chapter 1 should remain the architecture-and-interpretation chapter.

Keep in Chapter 1:
- TOR intent and sponsor expectation logic
- methodology from interviews, workshops, benchmarks, and standards
- benchmark and predecessor lessons
- the **implications** of DCCE web fragmentation
- the **implications** of the spatial risk-map product's actual scope and limits
- UX and information architecture reasoning
- CDM interpretation
- workflow-pattern and MVP translation
- FGD1 and FGD2 as framework-refinement evidence
- the resulting bounded Phase 1 position
- the explanation of the latest locked NCAIF design choices, especially stable backbone, flexible elements, and the logic of the navigation/access model

For Section 1.6 and Section 1.7 specifically, keep only:
- the conclusion that the existing DCCE landscape is fragmented and requires reorganization;
- the conclusion that the risk map is real but bounded, and cannot be over-claimed as a complete platform proof;
- any bridging sentences needed to connect these realities to [`chapter 1.9`](ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim%20Report%20Writing%20Plan.md), [`chapter 1.10`](ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim%20Report%20Writing%20Plan.md), and [`chapter 1.12`](ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim%20Report%20Writing%20Plan.md).

In the revised structure, the explanation of current NCAIF design choices should sit mainly in the later architecture-facing subsection that explains:
- why the stable backbone is locked,
- why Policy Maker Center is the most visible access anchor,
- why the platform uses a hybrid navigation model,
- why tools/catalog access must remain secondary to the narrative surface,
- and why detailed sitemap lists should move to an appendix rather than dominate Chapter 1 prose.

### What moves to Chapter 2

Chapter 2 should become the current landscape and interview-synthesis chapter.

Move into Chapter 2:
- fuller description of the current DCCE website and related product landscape
- fuller description of the spatial risk-map product as a current information product
- interview-based description of what agencies already produce or manage
- how agencies collect data and how often they update it
- what datasets they say they need
- what they are trying to use climate risk and impact information for

This makes Chapter 2 the place where the report says:
- what exists now;
- who produces what;
- how it is produced;
- what is still missing;
- what users need the information for.

This also means Chapter 2 should **not** become the place where the report re-explains the locked NCAIF design logic. That explanatory burden remains in Chapter 1.

## Practical rule to avoid repetition

When drafting:

- if a paragraph is mainly answering **what currently exists** or **how an existing product works**, it belongs in Chapter 2;
- if a paragraph is mainly answering **why those realities imply the need for a new organizing architecture**, it belongs in Chapter 1.

## Recommended pre-drafting analysis artifacts

These should be prepared before chapter drafting begins.

### A. Interview comparison matrix

Purpose:
- create one structured comparison view across all interview summaries.

Suggested fields:
- agency
- role in the ecosystem
- products or systems currently maintained
- data generated or managed
- collection method
- update frequency
- spatial scale
- key constraints
- expressed dataset needs
- use cases

### B. Current data product landscape table

Purpose:
- produce a concise landscape view of existing visible products and systems across DCCE and partner agencies.

Suggested fields:
- product or system name
- owner agency
- product type
- intended audience
- main content or function
- current status
- scale or scope
- limitation relevant to the interim report

### C. Stakeholder-needs synthesis note

Purpose:
- group dataset needs into reusable themes instead of repeating each interview separately.

Suggested need clusters:
- long-term projections
- authoritative baselines
- metadata and data dictionaries
- finer spatial granularity
- true economic loss and damage
- vulnerability and resilience indicators
- access and publishing pathways

### D. Use-case clustering note

Purpose:
- synthesize practical uses of climate risk and impact information into a small set of report-ready clusters.

Suggested clusters:
- disaster response and post-event assessment
- local planning and budget justification
- social protection and vulnerable-group targeting
- macroeconomic planning and national evaluation
- infrastructure resilience planning
- financial-sector risk analysis

### E. Chapter 1 to Chapter 2 handoff note

Purpose:
- explicitly list which descriptive paragraphs move from Chapter 1 to Chapter 2 and which analytical claims remain in Chapter 1.

Minimum contents:
- keep/move decisions for current [`section 1.6`](ψ/incubate/DCCE/CRDB/output/2026-03-13-CRDB-Interim-Report-Section-1.6-1.12-Draft-th-edited.md) paragraphs
- keep/move decisions for current [`section 1.7`](ψ/incubate/DCCE/CRDB/output/2026-03-13-CRDB-Interim-Report-Section-1.6-1.12-Draft-th-edited.md) paragraphs
- transitional sentences needed between the two chapters

## Implementation recommendation for drafting order

1. finalize the Chapter 1 to Chapter 2 split in this decision note
2. build the interview comparison matrix
3. build the current data product landscape table
4. build the stakeholder-needs synthesis note
5. build the use-case clustering note
6. revise the v2 Chapter 1 draft based on the approved split
7. only then begin prose drafting of Chapter 2

8. after the Chapter 1 v3 merge, run one more consistency pass against Chapter 2 to confirm that the architecture explanation in Chapter 1 and the landscape explanation in Chapter 2 do not overlap excessively

## Current status

At this point:
- the anchor plan file has been updated in [`ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim Report Writing Plan.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim%20Report%20Writing%20Plan.md)
- a v2 test copy exists in [`ψ/incubate/DCCE/CRDB/output/2026-03-13-CRDB-Interim-Report-Section-1.6-1.12-Draft-th-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-13-CRDB-Interim-Report-Section-1.6-1.12-Draft-th-v2.md)
- the remaining pre-drafting work should now focus on producing the analysis artifacts rather than drafting Chapter 2 prose directly
