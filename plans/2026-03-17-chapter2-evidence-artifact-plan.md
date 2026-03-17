# Plan — Chapter 2 evidence-artifact package for interim report drafting

## Objective

Create the analysis artifacts that will serve as the evidence base for drafting Chapter 2 of the CRDB interim report, then update the Section 2 evidence table in [`ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim Report Writing Plan.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim%20Report%20Writing%20Plan.md) so the plan reflects the stronger evidence base.

## Planning constraints

- Chapter 2 must remain a **current data product landscape + interview synthesis** chapter, not a full national inventory and not a second architecture chapter.
- The **current data product landscape table** must explicitly include:
  - DCCE website content analysis from [`ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Summary.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Summary.md)
  - risk-map product content and limitations currently carried in Chapter 1 related materials
  - Pack A product evidence from [`ψ/inbox/2026-03-12 - รายงานฐานข้อมูลความเสี่ยงเชิงพื้นที่จากการเปลี่ยนแปลงสภาพภูมิอากาศไทยฉบับสมบูรณ์  -notebooklm extraction.md`](ψ/inbox/2026-03-12%20-%20รายงานฐานข้อมูลความเสี่ยงเชิงพื้นที่จากการเปลี่ยนแปลงสภาพภูมิอากาศไทยฉบับสมบูรณ์%20%20-notebooklm%20extraction.md), especially its three-part product structure, scale and temporal coverage, index limitations, backend-service description, and usage caveats
- The **Chapter 1 → Chapter 2 handoff analysis** must compare:
  - [`ψ/incubate/DCCE/CRDB/output/2026-03-13-CRDB-Interim-Report-Section-1.6-1.12-Draft-th-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-13-CRDB-Interim-Report-Section-1.6-1.12-Draft-th-v2.md)
  - [`ψ/incubate/DCCE/CRDB/output/2026-03-17-CRDB-Interim-Report-Chapter-1-Draft-v3.md`](ψ/incubate/DCCE/CRDB/output/2026-03-17-CRDB-Interim-Report-Chapter-1-Draft-v3.md)
- The artifacts must strengthen the Section 2 evidence base without causing Chapter 2 to repeat the Chapter 1 architecture argument.

## Deliverables

1. Interview comparison matrix
2. Current data product landscape table
3. Stakeholder-needs synthesis note
4. Use-case clustering note
5. Chapter 1 → Chapter 2 handoff analysis note
6. Updated Section 2 evidence table in [`ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim Report Writing Plan.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim%20Report%20Writing%20Plan.md)

## Execution plan

### Step 1 — Lock the source set

Read and inventory the core source materials that will feed the evidence package:

- interview summaries in [`ψ/incubate/DCCE/CRDB/output/Interview summary notes`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes)
- current product references in [`ψ/incubate/DCCE/CRDB/output/FGD 1 result.md`](ψ/incubate/DCCE/CRDB/output/FGD%201%20result.md)
- DCCE website analysis in [`ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Summary.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Summary.md)
- risk-map product evidence in [`ψ/inbox/2026-03-12 - รายงานฐานข้อมูลความเสี่ยงเชิงพื้นที่จากการเปลี่ยนแปลงสภาพภูมิอากาศไทยฉบับสมบูรณ์  -notebooklm extraction.md`](ψ/inbox/2026-03-12%20-%20รายงานฐานข้อมูลความเสี่ยงเชิงพื้นที่จากการเปลี่ยนแปลงสภาพภูมิอากาศไทยฉบับสมบูรณ์%20%20-notebooklm%20extraction.md)
- Chapter 2 framing in [`ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter2-reframed-writing-plan-and-outline.md`](ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter2-reframed-writing-plan-and-outline.md)
- restructuring rules in [`ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter1-Chapter2-restructuring-decision-note.md`](ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter1-Chapter2-restructuring-decision-note.md)

Output of this step:
- a source-to-artifact mapping table showing which source files feed which artifact
- a short note on reuse rules: descriptive material goes to Chapter 2 artifacts, analytical implications stay tied to Chapter 1

### Step 2 — Run the Chapter 1 split analysis

Compare [`ψ/incubate/DCCE/CRDB/output/2026-03-13-CRDB-Interim-Report-Section-1.6-1.12-Draft-th-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-13-CRDB-Interim-Report-Section-1.6-1.12-Draft-th-v2.md) against [`ψ/incubate/DCCE/CRDB/output/2026-03-17-CRDB-Interim-Report-Chapter-1-Draft-v3.md`](ψ/incubate/DCCE/CRDB/output/2026-03-17-CRDB-Interim-Report-Chapter-1-Draft-v3.md) and classify content into three buckets:

- **Keep in Chapter 1**
  - analytical implications of fragmentation
  - analytical implications of risk-map scope limits
  - UX and information-architecture reasoning
  - architecture, CDM, MVP, and design-choice interpretation
- **Move into Chapter 2**
  - fuller description of DCCE website content and current assets
  - fuller description of the spatial risk-map product
  - product-level statements about what exists, what it shows, scale, audience, and limitations
- **Bridge between chapters**
  - short transition sentences that let Chapter 1 point to the descriptive landscape review in Chapter 2 without repeating it

Output of this step:
- a paragraph-level handoff analysis note with `keep`, `move`, and `bridge` sections

### Step 3 — Define artifact templates before population

Create a fixed structure for each artifact so data extraction is consistent.

#### 3A. Interview comparison matrix

Recommended columns:

- agency
- ecosystem role
- products or systems currently maintained
- data generated or managed
- collection method
- update frequency
- spatial scale
- quality or access constraints
- expressed dataset needs
- principal use cases
- source note

#### 3B. Current data product landscape table

Recommended columns:

- product or content group
- owner agency
- product type
- audience
- main content or function
- current status
- scale or scope
- key limitation for interim-report framing
- source basis
- chapter placement note

Required row groups:

- DCCE website content groups from [`ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Summary.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Summary.md)
- spatial risk-map product components and boundaries from Pack A evidence, including:
  - `Data Model & Indices`
  - `User-facing Maps`
  - `Backend Database & Tools`
  - provincial display scope
  - future roadmap claims that must be clearly separated from current-state claims
  - interpretation caveats such as relative-index logic, static socio-economic assumptions, and non-suitability for sub-provincial decisions
- major agency-owned products visible in [`ψ/incubate/DCCE/CRDB/output/FGD 1 result.md`](ψ/incubate/DCCE/CRDB/output/FGD%201%20result.md) and interview summaries

#### 3C. Stakeholder-needs synthesis note

Required clusters:

- long-term projections
- authoritative baselines
- metadata and data dictionaries
- finer spatial granularity
- economic loss and damage
- vulnerability and resilience indicators
- access and publishing pathways

For each cluster, record:

- recurring need statement
- agencies expressing the need
- likely Chapter 2 subsection usage
- confidence or completeness note

#### 3D. Use-case clustering note

Required clusters:

- disaster response and post-event assessment
- local planning and budgeting
- social protection and vulnerable-group targeting
- macroeconomic planning and national evaluation
- infrastructure resilience planning
- financial-sector risk analysis

For each cluster, record:

- use-case summary
- representative agencies
- data types required
- why the use case matters for Chapter 2 synthesis

#### 3E. Chapter 1 → Chapter 2 handoff analysis note

Required sections:

- `Material retained in Chapter 1`
- `Material moved into Chapter 2`
- `Transitional bridge sentences needed`
- `Implications for the current data product landscape table`

### Step 4 — Populate the evidence artifacts

Populate in this order so each later artifact reuses earlier work:

1. interview comparison matrix
2. current data product landscape table
3. stakeholder-needs synthesis note
4. use-case clustering note
5. Chapter 1 → Chapter 2 handoff analysis note

Population rules:

- normalize uneven interview evidence instead of forcing false precision
- when update frequency is unclear, label it as inferred or not yet explicit
- treat website content findings and risk-map evidence as part of the same current-landscape story, but keep architecture interpretation out of the table itself
- avoid agency-by-agency prose; extract reusable synthesis material

### Step 5 — Validate against Section 2 needs

Check the full package against the Section 2 evidence map in [`ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim Report Writing Plan.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim%20Report%20Writing%20Plan.md).

Validation questions:

- Do the artifacts support subsections 2.2 through 2.7 directly?
- Is the current data product landscape now consolidated enough for Chapter 2 drafting?
- Are stakeholder needs and use cases clustered enough to avoid repetitive writing?
- Does the handoff note clearly prevent overlap between Chapter 1 and Chapter 2?
- Are remaining evidence gaps explicitly logged rather than hidden?

Output of this step:
- a short validation note listing strong evidence, weak evidence, and caveats that Chapter 2 drafting must respect

### Step 6 — Update the anchor plan

After the artifact package is complete, update the Section 2 evidence table and related evidence-strength notes in [`ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim Report Writing Plan.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim%20Report%20Writing%20Plan.md).

Update goals:

- replace references to missing comparison artifacts with references to completed artifacts
- strengthen the evidence description for Section 2 subsections where the new package materially improves coverage
- preserve honest caveats where evidence remains uneven, especially for update frequency and product comparability

## Recommended file set for implementation

Create or update the following markdown files under [`ψ/incubate/DCCE/CRDB/output`](ψ/incubate/DCCE/CRDB/output):

- `2026-03-17-Chapter2-source-to-artifact-mapping.md`
- `2026-03-17-Chapter2-interview-comparison-matrix.md`
- `2026-03-17-Chapter2-current-data-product-landscape-table.md`
- `2026-03-17-Chapter2-stakeholder-needs-synthesis.md`
- `2026-03-17-Chapter2-use-case-clustering.md`
- `2026-03-17-Chapter1-to-Chapter2-handoff-analysis.md`

Then update:

- [`ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim Report Writing Plan.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim%20Report%20Writing%20Plan.md)

## Acceptance criteria

The plan is complete when:

- every Chapter 2 analysis artifact has a defined template and source basis
- the current data product landscape table includes DCCE website content findings and risk-map content migrated from Chapter 1 materials
- the handoff analysis is grounded in a direct comparison between [`2026-03-13-CRDB-Interim-Report-Section-1.6-1.12-Draft-th-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-13-CRDB-Interim-Report-Section-1.6-1.12-Draft-th-v2.md) and [`2026-03-17-CRDB-Interim-Report-Chapter-1-Draft-v3.md`](ψ/incubate/DCCE/CRDB/output/2026-03-17-CRDB-Interim-Report-Chapter-1-Draft-v3.md)
- the evidence package is validated against Section 2 needs before prose drafting begins
- the anchor writing plan is updated to reflect the stronger evidence base
