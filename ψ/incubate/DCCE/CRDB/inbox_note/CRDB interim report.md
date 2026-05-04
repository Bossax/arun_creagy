# CRDB Interim Report — Working Outline (TOR 7.2)

The interim report must include these topics per [[CRDB - TOR]]:
- **Results of Clauses 5.2.1 to 5.2.5**
- **Results of Clauses 5.3.1 to 5.3.2**
- **Progress on Clauses 5.5.1 to 5.5.2**

## Chapter 1 — Develop the National Climate Adaptation Information Framework (TOR 5.2)

**Evidence to carry into this chapter**
- Three-platform benchmark review from the inception report, with T-PLAT lessons summarized in [`ψ/incubate/DCCE/CRDB/output/2026-03-13-Three-Platform Review and T-PLAT Lessons.md`](ψ/incubate/DCCE/CRDB/output/2026-03-13-Three-Platform%20Review%20and%20T-PLAT%20Lessons.md)
- DCCE website content review 
- FGD1 and FGD2 results (validation + change requests)
- Draft NCAIF CDM, sitemap vNext, and MVPs
- Use cases from interviews
- Governance rails: [[ψ/incubate/DCCE/CRDB/output/2026-03-05-Feature-Driven Data Governance Strategy v3]]
- Pack A evidence from the spatial risk-map report (risk‑map product definition + limitations)

**Sub‑sections (working)**
1.1 TOR intent and sponsor expectations
1.2 Methodology: deriving user demand and design criteria
1.3 Methodology: why the project needed a conceptual data model (CDM)
1.4 Standards and literature alignment (IPCC, WMO, UNFCCC, ISO)
1.5 Predecessor review: three climate adaptation platforms from the inception report, with T-PLAT focus and lesson summary
1.6 Brief review: DCCE web structure and content gap, with NCAIF hosted inside the DCCE website
1.7 Product-reality diagnosis: spatial risk map constraints (factual only; applications deferred)
1.8 UX/IA diagnosis: design principles that shape sitemap decisions
1.9 Architectural interpretation: CDM as hidden organizing logic
1.10 Service translation: workflow patterns and MVPs
1.11 Consultation and revision loop
1.12 Current Phase 1 position

### Draft — Chapter 1 (TOR 5.2)

#### 1.1 TOR intent and sponsor expectations

The TOR requested a **National Climate Adaptation Information Framework** plus a **data management structure**, not only a web redesign. This chapter therefore reports progress on a coherent framework, the underlying management logic, and the mechanisms for safe publishing and revision. (TOR reference: [`ψ/incubate/DCCE/CRDB/inbox_source/CRDB - TOR.md`](ψ/incubate/DCCE/CRDB/inbox_source/CRDB%20-%20TOR.md))

#### 1.2 Methodology: deriving user demand and design criteria

User demand and design requirements were derived from stakeholder interviews, workshop notes, and internal focus-group signals. These inputs were synthesized into repeatable user journeys, priority workflows, and governance constraints that now shape the NCAIF architecture and the MVP shortlist. The evidence base is consolidated in [`ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md) and supported by internal feedback captured in [`ψ/incubate/DCCE/CRDB/output/FGD 1 result.md`](ψ/incubate/DCCE/CRDB/output/FGD%201%20result.md). Key findings include: demand for decision-ready summaries, a need for clear boundary guidance, preview-before-download expectations, and a staged publishing workflow.

#### 1.3 Methodology: why the project needed a conceptual data model (CDM)

The TOR requires a data management structure and future dataset design; these tasks require a conceptual blueprint that defines **entities, relationships, and business rules** before any logical or physical build. The CDM bridges stakeholder needs to implementation and prevents ad hoc structures. This rationale is documented in [`ψ/incubate/DCCE/CRDB/output/Conceptual Data Model for climate risk and adaptation data system.md`](ψ/incubate/DCCE/CRDB/output/Conceptual%20Data%20Model%20for%20climate%20risk%20and%20adaptation%20data%20system.md) with supporting conceptual-model references in [`ψ/incubate/DCCE/CRDB/inbox_source/What is Conceptual Data Modeling Purpose & Examples.md`](ψ/incubate/DCCE/CRDB/inbox_source/What%20is%20Conceptual%20Data%20Modeling%20Purpose%20%26%20Examples.md) and [`ψ/incubate/DCCE/CRDB/inbox_source/Conceptual vs Logical vs Physical Data Models.md`](ψ/incubate/DCCE/CRDB/inbox_source/Conceptual%20vs%20Logical%20vs%20Physical%20Data%20Models.md).

#### 1.4 Standards and literature alignment (IPCC, WMO, UNFCCC, ISO)

The CDM entity logic was aligned to international standards to avoid semantic drift and to ensure future reporting interoperability. This alignment draws on the technical interoperability review in [`ψ/incubate/DCCE/CRDB/inbox_note/Technical Interoperability and Data Modeling in Disaster Risk Reduction - A Comparative Analysis of IPCC, Sendai, and Global Standards.md`](ψ/incubate/DCCE/CRDB/inbox_note/Technical%20Interoperability%20and%20Data%20Modeling%20in%20Disaster%20Risk%20Reduction%20-%20A%20Comparative%20Analysis%20of%20IPCC,%20Sendai,%20and%20Global%20Standards.md) and the standards alignment section in [`ψ/incubate/DCCE/CRDB/output/National Climate Adaptation Information Framework.md`](ψ/incubate/DCCE/CRDB/output/National%20Climate%20Adaptation%20Information%20Framework.md). This work ensures consistent treatment of hazard, exposure, vulnerability, event attribution, and adaptation-cycle logic.

#### 1.5 Predecessor review: three-platform benchmark with T-PLAT focus

- Use [`ψ/incubate/DCCE/CRDB/output/2026-03-13-Three-Platform Review and T-PLAT Lessons.md`](ψ/incubate/DCCE/CRDB/output/2026-03-13-Three-Platform%20Review%20and%20T-PLAT%20Lessons.md) to briefly recap the three climate adaptation platforms reviewed in the inception report.
- Keep T-PLAT as the main national predecessor for this subsection and summarize what it validates, what it could not sustain, and what lessons carry forward.
- Do not turn this subsection into CDM or MVP argumentation yet; keep it as benchmark/predecessor framing for later sections.

#### 1.6 Brief review: DCCE web structure and content gap

This section should stay brief and factual: NCAIF is hosted inside the DCCE website, not positioned as a replacement for it. The gap analysis in [`ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Summary.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Summary.md) and insert evidence in [`ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Report_Insert.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Report_Insert.md) should be used to show how scattered existing DCCE content can become foundational NCAIF content once reorganized, linked, and clarified.

#### 1.7 Product-reality diagnosis: spatial risk map constraints

The spatial risk-map report is the most mature product domain currently available. This subsection should remain factual about the three product layers (model/indices, user-facing maps, backend services) and the explicit boundary conditions (provincial scale, relative index, static socio-economic assumptions), using [`ψ/inbox/2026-03-12 - รายงานฐานข้อมูลความเสี่ยงเชิงพื้นที่จากการเปลี่ยนแปลงสภาพภูมิอากาศไทยฉบับสมบูรณ์  -notebooklm extraction.md`](ψ/inbox/2026-03-12-รายงานฐานข้อมูลความเสี่ยงเชิงพื้นที่จากการเปลี่ยนแปลงสภาพภูมิอากาศไทยฉบับสมบูรณ์-notebooklm%20extraction.md) as the anchor. Applications to CDM, NCAIF, and MVPs should be deferred to later sections.

#### 1.8 UX/IA diagnosis: design principles that shape sitemap decisions

UX evidence shows that the platform must separate tools from catalogs, keep navigation shallow, and use narrative pathways with progressive disclosure. These principles are documented in [`ψ/incubate/DCCE/CRDB/inbox_source/2026-03-12 - User Experience Design Principles for National Climate Change Adaptation Information Services.md`](ψ/incubate/DCCE/CRDB/inbox_source/2026-03-12%20-%20User%20Experience%20Design%20Principles%20for%20National%20Climate%20Change%20Adaptation%20Information%20Services.md) and operationalized in [`ψ/incubate/DCCE/CRDB/output/2026-03-12 - NCAIF_Pack_C_UI_Analysis.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12%20-%20NCAIF_Pack_C_UI_Analysis.md). These constraints explain why the NCAIF sitemap is not a mirror of DCCE’s internal structure.

#### 1.9 Architectural interpretation: CDM as hidden organizing logic

The CDM is the hidden logic that reconciles fragmented content, product reality, and interface usability. It connects data entities, governance roles, and publishing rules so the sitemap can remain legible while still being scientifically valid and extensible. The synthesis of this argument is captured in [`ψ/incubate/DCCE/CRDB/output/2026-03-12_crdb-section1-cdm-mvp-evidence-analysis.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12_crdb-section1-cdm-mvp-evidence-analysis.md) and supported by the NCAIF/CDM architecture overview in [`ψ/incubate/DCCE/CRDB/output/NCAIF_CDM_Architecture_Diagram.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_CDM_Architecture_Diagram.md).

#### 1.10 Service translation: workflow patterns and MVPs

Workflow patterns describe repeatable user steps; MVPs are the limited, visible Phase 1 service expressions of those patterns. This translation is anchored in [`ψ/incubate/DCCE/CRDB/output/NCAIF — Workflow patterns + MVP v3.md`](ψ/incubate/DCCE/CRDB/output/NCAIF%20%E2%80%94%20Workflow%20patterns%20%2B%20MVP%20v3.md), with MVP‑2 explicitly framed as groundwork for DDPM ingestion and Loss & Damage governance rather than a fully automated pipeline.

#### 1.11 Consultation and revision loop

FGD1 and FGD2 feedback shifted sponsor understanding from a “website-first” expectation to an architecture‑and‑governance‑first stance. The revisions are documented in [`ψ/incubate/DCCE/CRDB/inbox_source/2026-03-11_FGD2_action_summary.md`](ψ/incubate/DCCE/CRDB/inbox_source/2026-03-11_FGD2_action_summary.md) and supported by the internal synthesis logs in [`ψ/memory/logs/info/2026-03-11_16-59_fgd2-sitemap-focus-platform-framing.md`](ψ/memory/logs/info/2026-03-11_16-59_fgd2-sitemap-focus-platform-framing.md) and [`ψ/memory/logs/info/2026-03-11_17-12_fgd2-sitemap-needs-more-detail-and-remains-flexible.md`](ψ/memory/logs/info/2026-03-11_17-12_fgd2-sitemap-needs-more-detail-and-remains-flexible.md).

#### 1.12 Current Phase 1 position

The refined NCAIF structure is now a bounded Phase 1 architecture aligned to product reality, usability constraints, and governance gates. The current stance is recorded in [`ψ/incubate/DCCE/CRDB/output/National Climate Adaptation Information Framework.md`](ψ/incubate/DCCE/CRDB/output/National%20Climate%20Adaptation%20Information%20Framework.md) and validated through the Pack A/B/C synthesis in [`ψ/incubate/DCCE/CRDB/output/2026-03-12 - NCAIF_Pack_ABC_Decision_Matrix.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12%20-%20NCAIF_Pack_ABC_Decision_Matrix.md).

## Chapter 2 — Develop Information Product & Baseline Data Inventory (TOR 5.3.1–5.3.2)

**Evidence to carry into this chapter**
- ADPC climate analytics platform dataset list: [[ADPC Climate Hazard and Exposure Visualization Platform]]
- Indicator list from [[Spatial climate risk map DCCE v2]] (noting processed/siloed limitation)
- Review of [[Development of National Climate Risk Index - Thailand]] (data sources)
- [[ψ/incubate/DCCE/CRI/inbox/active/Climate Risk Index (CRI) Pilot Methodology ]]
- CDM risk/impact subject area to define boundaries
- Interview results (datasets owned + pain points + use cases)

**Sub‑sections (working)**
2.1 Current dataset landscape and boundary definition
2.2 Baseline data candidates and gaps
2.3 Use‑case evidence from interviews (who needs what)

## Chapter 3 — Develop Knowledge Sets on Climate Risks & Impacts (TOR 5.5.1–5.5.2 progress)

**Purpose**
Show progress on 10‑year review + selection of significant studies and how the knowledge sets will feed NCAIF content.

**Evidence to carry into this chapter**
- Task 5.5 scope note: [[2026-03-12-Task 5.5 Scope]]
- Draft list of significant studies (to be completed)
- Article + infographic plan mapped to NCAIF sitemap nodes

**Sub‑sections (working)**
3.1 Review method and selection criteria
3.2 Shortlist of significant studies (progress)
3.3 Draft knowledge‑set structure (articles + infographics) mapped to NCAIF

## Interim‑report inserts (to draft)

- “What FGD2 validated / changed” (1–2 pages)
- Sitemap vNext drill‑down + sitemap change process (Pack A integration)
- Phase‑1 content gap update (what is missing vs what is available)
- Task 5.5 scope + progress snapshot

## Appendix candidates

- Pack A evidence summary (risk‑map product + limitations)
- Gap analysis insert (from [`DCCE_Website_Content_Gap_Report_Insert.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Report_Insert.md))
- FGD2 minutes/excerpts
