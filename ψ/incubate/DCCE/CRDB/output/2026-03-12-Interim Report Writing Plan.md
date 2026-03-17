# Interim Report Writing Plan — CRDB (TOR 7.2)

supersede [[CRDB interim report]]
## Objective
Deliver the interim report by **23 Mar 10:00** (billing constraint), aligned to TOR 7.2 and the post‑FGD2 synthesis requirements, **with a progress‑first narrative that updates sponsor understanding from TOR‑era assumptions to current evidence and decisions**.

## Storytelling strategy (progress‑first)

**Goal:** evolve sponsor understanding from **TOR assumptions → current evidence → architectural interpretation → validated Phase 1 direction**, so conclusions are earned rather than abrupt.

1) **Start from the TOR intent** (what the sponsor asked for at contract start).
2) **Show what changed and why** (evidence, constraints, FGD1/FGD2 signals, Pack A realities, current DCCE website limitations, Pack C UX guidance).
3) **Explain the hidden logic**: show why **CDM** is needed as the back-end organizing logic and management structure, not as a detached technical artifact.
4) **Then land on visible Phase 1 expressions**: show how **workflow patterns and MVPs** translate that logic into user-facing services, while making clear what is real now, what is groundwork, and what remains future-facing.

## Inputs (fixed evidence)
- TOR mapping and interim report requirements: [`ψ/incubate/DCCE/CRDB/inbox_source/CRDB - TOR.md`](ψ/incubate/DCCE/CRDB/inbox_source/CRDB%20-%20TOR.md)
- FGD2 synthesis and validation signals: [`ψ/incubate/DCCE/CRDB/inbox_source/2026-03-11_FGD2_action_summary.md`](ψ/incubate/DCCE/CRDB/inbox_source/2026-03-11_FGD2_action_summary.md) and log files. 
- Website content gap baseline: [`ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Summary.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Summary.md)
- Pack A evidence (risk‑map product + limitations): [`ψ/inbox/2026-03-12 - รายงานฐานข้อมูลความเสี่ยงเชิงพื้นที่จากการเปลี่ยนแปลงสภาพภูมิอากาศไทยฉบับสมบูรณ์  -notebooklm extraction.md`](ψ/inbox/2026-03-12%20-%20รายงานฐานข้อมูลความเสี่ยงเชิงพื้นที่จากการเปลี่ยนแปลงสภาพภูมิอากาศไทยฉบับสมบูรณ์%20%20-notebooklm%20extraction.md)
- Pack A/B/C decision matrix (sitemap decisions + constraints): [`ψ/incubate/DCCE/CRDB/output/2026-03-12 - NCAIF_Pack_ABC_Decision_Matrix.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12%20-%20NCAIF_Pack_ABC_Decision_Matrix.md)
- Pack C UI/UX analysis (navigation + page archetype rules): [`ψ/incubate/DCCE/CRDB/output/2026-03-12 - NCAIF_Pack_C_UI_Analysis.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12%20-%20NCAIF_Pack_C_UI_Analysis.md)
- Three-platform benchmark review + T-PLAT lessons: [`ψ/incubate/DCCE/CRDB/output/2026-03-13-Three-Platform Review and T-PLAT Lessons.md`](ψ/incubate/DCCE/CRDB/output/2026-03-13-Three-Platform%20Review%20and%20T-PLAT%20Lessons.md)
- Section 1 synthesis note: [`ψ/incubate/DCCE/CRDB/output/2026-03-12_crdb-section1-cdm-mvp-evidence-analysis.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12_crdb-section1-cdm-mvp-evidence-analysis.md)
- UX benchmark source with citations: [`ψ/incubate/DCCE/CRDB/inbox_source/2026-03-12 - User Experience Design Principles for National Climate Change Adaptation Information Services.md`](ψ/incubate/DCCE/CRDB/inbox_source/2026-03-12%20-%20User%20Experience%20Design%20Principles%20for%20National%20Climate%20Change%20Adaptation%20Information%20Services.md)
- Sitemap [[ψ/incubate/DCCE/CRDB/output/National Climate Adaptation Information Framework|National Climate Adaptation Information Framework]] in  "Refined NCAIF sitemap — March 2026 (Pack A/B/C aligned)"

- Working outline: [`ψ/incubate/DCCE/CRDB/inbox_note/CRDB interim report.md`](ψ/incubate/DCCE/CRDB/inbox_note/CRDB%20interim%20report.md)
- Task 5.5 scope: [`ψ/incubate/DCCE/CRDB/output/2026-03-12-Task 5.5 Scope.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-Task%205.5%20Scope.md)

## Section 1 positioning logic: CDM and MVPs

- **CDM** should be positioned in the interim report as the **hidden organizing logic** that explains why DCCE cannot move directly from scattered assets to a usable national adaptation information service. It is the conceptual layer that connects content types, data relationships, governance roles, and publishing rules behind the interface.
- **MVPs** should be positioned as **visible Phase 1 service expressions** of workflow patterns, not as the whole story and not yet as final-report-scale product claims.
- In other words: **CDM explains why the structure must change; MVPs show how the revised structure becomes useful in practice.**
- The interim report should therefore treat CDM and MVPs as **evidence-backed explanatory devices for project progress**, not as abrupt action-oriented conclusions.

## Section 1 methodology logic: how we got here

- The Section 1 story must explicitly explain **how sponsor understanding evolved** from TOR intent to current NCAIF architecture.
- The methodology sequence is:
  1. **Interview and workshop evidence** → derive user demand, pain points, workflow needs, and publishing constraints.
  2. **Benchmark and literature review** → derive why a conceptual data blueprint is necessary, and why standards alignment matters.
  3. **Three-platform review + T-PLAT lessons** → revisit the inception-report benchmark set, then focus on T-PLAT as the nearest predecessor and summarize what it got right, what it could not do, and why NCAIF must move beyond a static portal model.
  4. **Current DCCE website and risk-map review** → establish the evidence base of current assets and product reality; detailed landscape description can sit in Section 2, while Section 1 retains only the analytical implications needed for the architecture argument.
  5. **Synthesis into CDM + NCAIF + workflow patterns/MVPs** → turn evidence into a bounded Phase 1 architecture.

## Section 1 evidence map (subsection-by-subsection)

| Subsection | Core claim to establish | Main evidence | How CDM should be positioned | How MVPs should be positioned |
|---|---|---|---|---|
| **1.1 TOR intent recap** | The sponsor originally asked for a national adaptation information framework plus management structure, not merely a website facelift | [`ψ/incubate/DCCE/CRDB/inbox_source/CRDB - TOR.md`](ψ/incubate/DCCE/CRDB/inbox_source/CRDB%20-%20TOR.md) | CDM is introduced as the kind of conceptual management logic implicitly required by TOR 5.2.3 | MVPs are not yet the focus; they appear later as practical Phase 1 expressions |
| **1.2 User-demand derivation** | NCAIF structure and MVP choices come from observed stakeholder demand, not arbitrary design taste | [`ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md) and interview-derived artifacts in the same project space | CDM is justified as the shared conceptual structure needed to serve recurring use cases, data pain points, boundary confusion, and governance constraints | MVPs are derived from recurring workflow needs seen in interviews and focus groups |
| **1.3 Why a conceptual data blueprint is needed** | The project needed a business-facing data blueprint before any logical or physical build because TOR asks for management structure, inventories, and future dataset design | [`ψ/incubate/DCCE/CRDB/output/Conceptual Data Model for climate risk and adaptation data system.md`](ψ/incubate/DCCE/CRDB/output/Conceptual%20Data%20Model%20for%20climate%20risk%20and%20adaptation%20data%20system.md), [`ψ/incubate/DCCE/CRDB/inbox_source/What is Conceptual Data Modeling Purpose & Examples.md`](ψ/incubate/DCCE/CRDB/inbox_source/What%20is%20Conceptual%20Data%20Modeling%20Purpose%20%26%20Examples.md), and [`ψ/incubate/DCCE/CRDB/inbox_source/Conceptual vs Logical vs Physical Data Models.md`](ψ/incubate/DCCE/CRDB/inbox_source/Conceptual%20vs%20Logical%20vs%20Physical%20Data%20Models.md) | CDM is framed as the translation layer between business requirements and future system implementation | MVPs remain downstream products that depend on this shared blueprint |
| **1.4 Standards and literature alignment** | CDM entity names and relationships were not invented ad hoc; they were aligned to IPCC, WMO, UNFCCC, and ISO logic | [`ψ/incubate/DCCE/CRDB/inbox_note/Technical Interoperability and Data Modeling in Disaster Risk Reduction - A Comparative Analysis of IPCC, Sendai, and Global Standards.md`](ψ/incubate/DCCE/CRDB/inbox_note/Technical%20Interoperability%20and%20Data%20Modeling%20in%20Disaster%20Risk%20Reduction%20-%20A%20Comparative%20Analysis%20of%20IPCC,%20Sendai,%20and%20Global%20Standards.md), [`ψ/incubate/DCCE/CRDB/output/National Climate Adaptation Information Framework.md`](ψ/incubate/DCCE/CRDB/output/National%20Climate%20Adaptation%20Information%20Framework.md), and supporting data-model notes in project inbox_source | CDM is positioned as standards-aligned conceptual infrastructure, especially for hazard, exposure, vulnerability, event, attribution, and adaptation-cycle logic | MVPs inherit standards discipline indirectly through the CDM and publishing rules |
| **1.5 Predecessor review: three-platform benchmark + T-PLAT lessons** | Section 1.5 should revisit the three climate adaptation platforms reviewed in the inception report while focusing on T-PLAT as the nearest predecessor and summarizing its lessons for the current draft | [`ψ/incubate/DCCE/CRDB/inbox_source/260106_DCCE_Climate risk database_inception report_vfinal.pdf`](ψ/incubate/DCCE/CRDB/inbox_source/260106_DCCE_Climate%20risk%20database_inception%20report_vfinal.pdf), [`ψ/incubate/DCCE/CRDB/inbox_source/T-PLAT analysis.md`](ψ/incubate/DCCE/CRDB/inbox_source/T-PLAT%20analysis.md), [`ψ/incubate/DCCE/CRDB/inbox_source/Learnings from T-PLAT - Benchmarking CDM.md`](ψ/incubate/DCCE/CRDB/inbox_source/Learnings%20from%20T-PLAT%20-%20Benchmarking%20CDM.md), and [`ψ/incubate/DCCE/CRDB/output/2026-03-13-Three-Platform Review and T-PLAT Lessons.md`](ψ/incubate/DCCE/CRDB/output/2026-03-13-Three-Platform%20Review%20and%20T-PLAT%20Lessons.md) | CDM is only foreshadowed here as the structural step beyond portal-first precedent; the subsection stays primarily on benchmark and predecessor lessons | MVP implications stay light here; visible service lessons from T-PLAT are carried forward to later sections |
| **1.6 Current-state implications from the current website and product landscape** | Section 1.6 should retain only the analytical implications drawn from the DCCE website review and the spatial risk-map product review: the current landscape contains real assets, but they remain fragmented, bounded, and insufficient as a coherent national service without reorganization | [`ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Summary.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Summary.md), [`ψ/inbox/2026-03-12 - รายงานฐานข้อมูลความเสี่ยงเชิงพื้นที่จากการเปลี่ยนแปลงสภาพภูมิอากาศไทยฉบับสมบูรณ์  -notebooklm extraction.md`](ψ/inbox/2026-03-12%20-%20รายงานฐานข้อมูลความเสี่ยงเชิงพื้นที่จากการเปลี่ยนแปลงสภาพภูมิอากาศไทยฉบับสมบูรณ์%20%20-notebooklm%20extraction.md), and the v2 working draft in [`ψ/incubate/DCCE/CRDB/output/2026-03-13-CRDB-Interim-Report-Section-1.6-1.12-Draft-th-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-13-CRDB-Interim-Report-Section-1.6-1.12-Draft-th-v2.md) | CDM is not argued in full here; this subsection now establishes only the analytical problem that later architectural sections must resolve | MVP discussion stays deferred; descriptive landscape material is expected to be developed later in Chapter 2 |
| **1.7 UX and IA diagnosis** | Usability requires strong information scent, shallow navigation, matrix pathways, progressive disclosure, and separation of tools from catalogs | [`ψ/incubate/DCCE/CRDB/inbox_source/2026-03-12 - User Experience Design Principles for National Climate Change Adaptation Information Services.md`](ψ/incubate/DCCE/CRDB/inbox_source/2026-03-12%20-%20User%20Experience%20Design%20Principles%20for%20National%20Climate%20Change%20Adaptation%20Information%20Services.md), especially its arguments on information scent, matrix taxonomy, and decoupled architecture | CDM is not a screen; it is the structural logic that allows separated front-end experiences to remain connected | MVPs are the visible pathways that embody these principles for policy users, local implementers, and technical analysts |
| **1.8 Architectural interpretation** | The project therefore needs a hidden organizing layer between fragmented content and user-facing services | Current NCAIF structure in [`ψ/incubate/DCCE/CRDB/output/National Climate Adaptation Information Framework.md`](ψ/incubate/DCCE/CRDB/output/National%20Climate%20Adaptation%20Information%20Framework.md), plus Pack A and Pack C evidence, synthesized in [`ψ/incubate/DCCE/CRDB/output/2026-03-12_crdb-section1-cdm-mvp-evidence-analysis.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12_crdb-section1-cdm-mvp-evidence-analysis.md) | CDM becomes the explanation for why NCAIF can connect products, data, methods, and governance without collapsing into one menu tree | MVPs become service wrappers placed on top of the information structure, not substitutes for the architecture |
| **1.9 Service translation** | Phase 1 must show a small number of usable service expressions rather than promise full system completion | [`ψ/incubate/DCCE/CRDB/output/NCAIF — Workflow patterns + MVP v3.md`](ψ/incubate/DCCE/CRDB/output/NCAIF%20%E2%80%94%20Workflow%20patterns%20%2B%20MVP%20v3.md), [`ψ/memory/logs/info/2026-03-09_20-18_mvp-vs-workflow-patterns-and-mvp2-groundwork.md`](ψ/memory/logs/info/2026-03-09_20-18_mvp-vs-workflow-patterns-and-mvp2-groundwork.md), and [`ψ/memory/logs/info/2026-03-11_16-59_fgd2-sitemap-focus-platform-framing.md`](ψ/memory/logs/info/2026-03-11_16-59_fgd2-sitemap-focus-platform-framing.md) | CDM remains central as the logic underneath all service pathways | MVPs are the limited, credible, Phase 1-visible expressions of that logic |
| **1.10 Consultation and revision loop** | FGD1 and FGD2 shifted sponsor understanding from website-centric expectations toward architecture, workflow, and governance awareness | [`ψ/memory/logs/info/2026-03-11_16-59_fgd2-sitemap-focus-platform-framing.md`](ψ/memory/logs/info/2026-03-11_16-59_fgd2-sitemap-focus-platform-framing.md), [`ψ/memory/logs/info/2026-03-11_17-12_fgd2-sitemap-needs-more-detail-and-remains-flexible.md`](ψ/memory/logs/info/2026-03-11_17-12_fgd2-sitemap-needs-more-detail-and-remains-flexible.md), [`ψ/incubate/DCCE/CRDB/inbox_source/2026-03-11_FGD2_action_summary.md`](ψ/incubate/DCCE/CRDB/inbox_source/2026-03-11_FGD2_action_summary.md) | CDM is what decision-makers learned sits behind the sitemap and makes change manageable | MVPs are what make the sitemap feel practical and explainable to decision-makers |
| **1.11 Current Phase 1 position** | The refined NCAIF structure is now a bounded, evidence-backed Phase 1 architecture | [`ψ/incubate/DCCE/CRDB/output/National Climate Adaptation Information Framework.md`](ψ/incubate/DCCE/CRDB/output/National%20Climate%20Adaptation%20Information%20Framework.md), [`ψ/incubate/DCCE/CRDB/output/2026-03-12 - NCAIF_Pack_ABC_Decision_Matrix.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12%20-%20NCAIF_Pack_ABC_Decision_Matrix.md) | CDM is the hidden architecture that keeps this bounded structure coherent and extensible | MVPs identify what Phase 1 visibly supports now, what stays documentation-light, and what remains groundwork |

### Section 1 evidence synthesis notes

- The **interview and use-case evidence** shows how user demand and preferences were actually derived: through stakeholder interviews, workshop signals, and internal focus-group feedback about usability, pain points, data discovery, publishing constraints, resolution needs, and decision-support requirements. This is the empirical basis for both NCAIF IA and MVP derivation.
- The **conceptual-modeling and standards evidence** shows why the project needed a CDM in the first place: TOR asks for management structure, baseline categorization, and future dataset design, while literature and standards explain that a conceptual model is the bridge from business requirements to implementation.
- The **three-platform benchmark review plus T-PLAT lesson summary** explains the predecessor logic and its limits. NCAIF does not start from zero; it inherits lessons from the inception-report benchmark set and especially from T-PLAT, but must move beyond a static portal and document library toward a more relational and service-oriented architecture.
- The **website gap evidence** should be framed briefly and concretely: NCAIF is to be hosted inside the DCCE website, not positioned as a replacement for it, and the scattered existing content should be treated as foundational material to reorganize, connect, and upgrade.
- The **risk-map report evidence** should remain factual in its own subsection: DCCE already has one substantial product domain, but it is bounded in scale, interpretation, and suitable uses. Applications to CDM, NCAIF, and MVP design should be interpreted later rather than folded into the product-reality subsection itself.
- The **UX benchmark evidence** shows that the front-end must separate catalogs from tools, use shallow and narrative pathways, and maintain progressive disclosure and information scent. This provides the rationale for why NCAIF cannot simply mirror DCCE's bureaucratic site structure or expose raw backend complexity directly.
- The consolidated read across these method streams is captured in [`ψ/incubate/DCCE/CRDB/output/2026-03-12_crdb-section1-cdm-mvp-evidence-analysis.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12_crdb-section1-cdm-mvp-evidence-analysis.md).
- Therefore, **Section 1 should argue that CDM is the hidden logic that reconciles fragmented content, product reality, and usable interface design, while MVPs are the limited Phase 1 expressions through which this logic becomes visible to users.**

## Section 2 positioning logic: current data product landscape and interview synthesis

- For the **interim report**, Section 2 should be narrower than a full baseline-inventory chapter.
- Its main role is to explain the **current data product landscape** and synthesize interview findings around four practical questions:
  1. what data products and systems already exist,
  2. what data stakeholders generate or manage,
  3. how they collect and update those data,
  4. what datasets they still need and what use cases they are trying to support.
- Section 2 should therefore function as a **landscape review + interview synthesis**, not as a completed national inventory chapter.
- To preserve the line of logic in Section 1, the more descriptive current-state material from Chapter 1 sections **1.6** and **1.7** may be relocated into Section 2, while Section 1 retains only the analytical results that are necessary for the architecture argument.
- In effect:
  - **Section 1** = why the structure had to change and what the architecture means
  - **Section 2** = what current products, data practices, unmet needs, and use cases that architecture must respond to

## Section 2 evidence map (subsection-by-subsection)

| Subsection | Core claim to establish | Main evidence | Link to Chapter 1 |
|---|---|---|---|
| **2.1 TOR intent recap** | TOR 5.3.1-5.3.2 requires a review of the current product and data landscape, not merely a technical list | [`ψ/incubate/DCCE/CRDB/inbox_source/CRDB - TOR.md`](ψ/incubate/DCCE/CRDB/inbox_source/CRDB%20-%20TOR.md), [`ψ/incubate/DCCE/CRDB/output/CRDB - Implementation Plan.md`](ψ/incubate/DCCE/CRDB/output/CRDB%20-%20Implementation%20Plan.md) | Keeps Section 2 grounded in TOR rather than repeating Section 1 architecture logic |
| **2.2 Current data product landscape** | DCCE and partner agencies already have multiple products, portals, dashboards, reports, and systems, but they are fragmented | [`ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter2-current-data-product-landscape-table.md`](ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter2-current-data-product-landscape-table.md), [`ψ/incubate/DCCE/CRDB/output/FGD 1 result.md`](ψ/incubate/DCCE/CRDB/output/FGD%201%20result.md), [`ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Summary.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Summary.md), and Pack A evidence in [`ψ/inbox/2026-03-12 - รายงานฐานข้อมูลความเสี่ยงเชิงพื้นที่จากการเปลี่ยนแปลงสภาพภูมิอากาศไทยฉบับสมบูรณ์  -notebooklm extraction.md`](ψ/inbox/2026-03-12%20-%20รายงานฐานข้อมูลความเสี่ยงเชิงพื้นที่จากการเปลี่ยนแปลงสภาพภูมิอากาศไทยฉบับสมบูรณ์%20%20-notebooklm%20extraction.md) | Absorbs the descriptive current-state material that would otherwise overload Section 1.6-1.7 |
| **2.3 Stakeholder-generated data and collection practice** | Agencies generate or manage different kinds of data through different mechanisms such as surveys, reporting chains, registries, modeling, and external data integration | [`ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter2-interview-comparison-matrix.md`](ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter2-interview-comparison-matrix.md) plus supporting interview summaries in [`ψ/incubate/DCCE/CRDB/output/Interview summary notes`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes) | Extends Section 1.2 interview evidence into operational data practice rather than design criteria |
| **2.4 Update frequency, scale, and operational constraints** | Data usefulness depends on update cadence, spatial granularity, quality controls, and access constraints | [`ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter2-interview-comparison-matrix.md`](ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter2-interview-comparison-matrix.md), with operational detail anchored in DDPM, NSO, MSDHS, OTP, DLA, DGA, TBA, and NESDC interview summaries | Prevents Section 1 from carrying too much descriptive operational detail |
| **2.5 Expressed dataset needs** | Stakeholders consistently report unmet needs around projections, baselines, metadata, granularity, economic loss data, vulnerability data, and safe access pathways | [`ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter2-stakeholder-needs-synthesis.md`](ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter2-stakeholder-needs-synthesis.md), [`ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter2-interview-comparison-matrix.md`](ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter2-interview-comparison-matrix.md), and [`ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md) | Supplies the concrete demand-side evidence that later supports prioritization, without repeating Section 1 MVP framing |
| **2.6 Use cases of climate risk and impact information** | Climate risk and impact information is used across emergency response, local planning, budgeting, social protection, macroeconomic planning, infrastructure resilience, and financial risk analysis | [`ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter2-use-case-clustering.md`](ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter2-use-case-clustering.md), [`ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md), and the interview summaries in [`ψ/incubate/DCCE/CRDB/output/Interview summary notes`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes) | Connects the product landscape to why the architecture matters, without replacing Section 1.10 |
| **2.7 Synthesis and progress implications** | The current landscape shows both existing assets and major coordination gaps; the project's immediate value lies in organizing and clarifying this landscape | the full evidence package above, especially [`ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter1-to-Chapter2-handoff-analysis.md`](ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter1-to-Chapter2-handoff-analysis.md), plus [`ψ/incubate/DCCE/CRDB/output/CRDB - Project Status (Current).md`](ψ/incubate/DCCE/CRDB/output/CRDB%20-%20Project%20Status%20(Current).md) | Hands the argument back to later report sections while avoiding a second architecture chapter |

## Pre-drafting analysis tasks for Section 2 (not report content)

These should be completed **before** drafting Section 2 and should **not** appear as a subsection in the report:

1. Interview comparison matrix
   - agency, role, products/systems, data generated or managed, collection method, update frequency, scale, expressed needs, use cases
2. Current data product landscape table
   - visible systems, owners, purpose, audience, and current status
3. Stakeholder-needs synthesis note
   - grouped by projections, baselines, metadata, granularity, economic loss, vulnerability, and access/publishing constraints
4. Use-case clustering note
   - grouped by emergency response, local planning and budgeting, social protection, macroeconomic planning, infrastructure resilience, and financial risk analysis
5. Chapter 1 to Chapter 2 handoff note
   - what descriptive material moves to Section 2 and what analytical conclusions remain in Section 1

## Section 2 source-to-artifact mapping and reuse rules

This mapping should remain embedded in the anchor writing plan rather than split into a separate note.

### Reuse rules

1. **Descriptive current-state material** belongs in the Section 2 analysis artifacts and later Chapter 2 prose.
2. **Architectural interpretation** remains in Chapter 1, except where a short bridge sentence is needed.
3. When evidence is uneven, record it as `explicit`, `implied`, or `not yet specified` rather than forcing false precision.
4. The current data product landscape must combine:
   - DCCE website-content findings from [`ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Summary.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Summary.md)
   - Pack A risk-map product evidence from [`ψ/inbox/2026-03-12 - รายงานฐานข้อมูลความเสี่ยงเชิงพื้นที่จากการเปลี่ยนแปลงสภาพภูมิอากาศไทยฉบับสมบูรณ์  -notebooklm extraction.md`](ψ/inbox/2026-03-12%20-%20รายงานฐานข้อมูลความเสี่ยงเชิงพื้นที่จากการเปลี่ยนแปลงสภาพภูมิอากาศไทยฉบับสมบูรณ์%20%20-notebooklm%20extraction.md)
   - agency product and system references from [`ψ/incubate/DCCE/CRDB/output/FGD 1 result.md`](ψ/incubate/DCCE/CRDB/output/FGD%201%20result.md) and [`ψ/incubate/DCCE/CRDB/output/Interview summary notes`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes)
5. The Chapter 1 to Chapter 2 handoff analysis must compare [`ψ/incubate/DCCE/CRDB/output/2026-03-13-CRDB-Interim-Report-Section-1.6-1.12-Draft-th-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-13-CRDB-Interim-Report-Section-1.6-1.12-Draft-th-v2.md) against [`ψ/incubate/DCCE/CRDB/output/2026-03-17-CRDB-Interim-Report-Chapter-1-Draft-v3.md`](ψ/incubate/DCCE/CRDB/output/2026-03-17-CRDB-Interim-Report-Chapter-1-Draft-v3.md), guided by [`ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter1-Chapter2-restructuring-decision-note.md`](ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter1-Chapter2-restructuring-decision-note.md).

### Source-to-artifact mapping

| Artifact | Direct purpose | Main sources | Extraction focus | Feeds Chapter 2 subsections |
|---|---|---|---|---|
| Interview comparison matrix | Create one normalized comparison view across agencies | interview summaries in [`ψ/incubate/DCCE/CRDB/output/Interview summary notes`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes) | agency role, products/systems, data managed, collection/update practice, spatial scale, constraints, unmet needs, use cases | 2.3, 2.4, 2.5, 2.6 |
| Current data product landscape table | Consolidate what products, systems, and content assets already exist | [`ψ/incubate/DCCE/CRDB/output/FGD 1 result.md`](ψ/incubate/DCCE/CRDB/output/FGD%201%20result.md), [`ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Summary.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Summary.md), Pack A extraction in [`ψ/inbox/2026-03-12 - รายงานฐานข้อมูลความเสี่ยงเชิงพื้นที่จากการเปลี่ยนแปลงสภาพภูมิอากาศไทยฉบับสมบูรณ์  -notebooklm extraction.md`](ψ/inbox/2026-03-12%20-%20รายงานฐานข้อมูลความเสี่ยงเชิงพื้นที่จากการเปลี่ยนแปลงสภาพภูมิอากาศไทยฉบับสมบูรณ์%20%20-notebooklm%20extraction.md), interview product mentions | website asset groups, risk-map product structure, current system status, intended audiences, scope, limitations | 2.2, 2.7 |
| Stakeholder-needs synthesis note | Group recurring unmet-data requests into report-ready themes | interview summaries, [`ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md), FGD1 comments in [`ψ/incubate/DCCE/CRDB/output/FGD 1 result.md`](ψ/incubate/DCCE/CRDB/output/FGD%201%20result.md) | projections, baselines, metadata, granularity, economic loss, vulnerability, governance/access | 2.5, 2.7 |
| Use-case clustering note | Cluster scattered use cases into a small set of practical groups | [`ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md), interview summaries | emergency response, local planning/budgeting, social protection, macro planning, infrastructure resilience, financial risk analysis | 2.6, 2.7 |
| Chapter 1 to Chapter 2 handoff analysis note | Separate what stays analytical in Chapter 1 from what moves as descriptive landscape material into Chapter 2 | [`ψ/incubate/DCCE/CRDB/output/2026-03-13-CRDB-Interim-Report-Section-1.6-1.12-Draft-th-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-13-CRDB-Interim-Report-Section-1.6-1.12-Draft-th-v2.md), [`ψ/incubate/DCCE/CRDB/output/2026-03-17-CRDB-Interim-Report-Chapter-1-Draft-v3.md`](ψ/incubate/DCCE/CRDB/output/2026-03-17-CRDB-Interim-Report-Chapter-1-Draft-v3.md), [`ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter1-Chapter2-restructuring-decision-note.md`](ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter1-Chapter2-restructuring-decision-note.md), Pack A extraction, website gap summary | keep/move/bridge decisions, especially for website-description and risk-map-description material | 2.2, 2.7 and Chapter 1/2 consistency |

### Normalization conventions for the Section 2 evidence package

- **Update frequency**
  - `continuous/system-driven`
  - `event-driven`
  - `monthly`
  - `annual or periodic`
  - `project-based / ad hoc`
  - `not explicitly stated`

- **Spatial scale**
  - `national`
  - `provincial`
  - `district`
  - `sub-district / municipality / LAO`
  - `asset-level / point-level`
  - `mixed-scale`

- **Evidence confidence**
  - `explicit in source`
  - `inferred from workflow description`
  - `not yet specified`

## Required TOR coverage (Interim Report)

1. **Results of TOR 5.2.1–5.2.5** (Draft NCAIF + management structure progress)
2. **Results of TOR 5.3.1–5.3.2** (baseline data + product landscape assessment)
3. **Progress on TOR 5.5.1–5.5.2** (knowledge set review + significant study shortlist)

## Section outline + evidence map

### Section 0 — Executive Summary (2–3 pages)
- **Sponsor‑orientation**: what the TOR expected vs what evidence now shows
- What changed since inception report (why the understanding evolved)
- FGD2 validation highlights (confirming or revising assumptions)
- Pack A integration: risk‑map product reality + limitations (boundary of Phase‑1 claims)
- Why the project now distinguishes **interface value** (NCAIF), **hidden organizing logic** (CDM), and **Phase 1 service expressions** (workflow patterns + MVPs)

### Section 1 — NCAIF development, management structure, and sitemap refinement (TOR 5.2)
- **1.1 TOR intent recap**: what “NCAIF + management structure” was expected to deliver at project start
- **1.2 Methodology: deriving user demand and design criteria** from stakeholder interviews, workshop evidence, and internal focus-group findings
- **1.3 Methodology: why the project needed a CDM** based on conceptual-modeling logic, TOR requirements, and literature on risk-data architecture
- **1.4 Methodology: standards and benchmark alignment** using IPCC, WMO, UNFCCC, ISO, and related literature to shape the entity logic and adaptation-cycle structure
- **1.5 Predecessor review**: review the three climate adaptation platforms from the inception report, while focusing on T-PLAT and summarizing lessons from T-PLAT for the current draft
- **1.6 Current-state implications from the website and product landscape**: merge the analytical results of the DCCE website review and the spatial risk-map review, while moving fuller descriptive landscape material to Section 2
- **1.7 UX/IA diagnosis**: Pack C principles → why the presentation layer must separate tools, catalogs, explainers, and guided pathways
- **1.8 Architectural interpretation**: CDM as the hidden logic and management structure that reconciles fragmented content, product types, metadata, governance, and cross-linking
- **1.9 Service translation**: workflow patterns + MVPs as the visible Phase 1 expressions of that logic, showing how users actually encounter value without over-claiming full platform buildout
- **1.10 Locked design choices and navigation model**: explain the stable backbone, flexible elements, policy-maker-centered access model, and the separation between narrative surface and technical support layer using the latest locked NCAIF decisions
- **1.11 Current Phase 1 position**: refined NCAIF structure and boundary statements (supported by Pack A/B/C evidence and explicit scope control)

### Section 2 — Information Product & Baseline Data Inventory (TOR 5.3.1–5.3.2)
- **TOR intent recap**: expected baseline inventory outputs
- **2.1 TOR intent and purpose of the landscape review**
- **2.2 Current data product landscape**: what products, systems, dashboards, reports, and portals already exist across DCCE and partner agencies
- **2.3 Stakeholder-generated data and collection/update practice**: what data agencies generate or manage, how they collect it, and how often they update it
- **2.4 Operational constraints of current data**: scale, cadence, quality, access, and governance limitations affecting usability
- **2.5 Expressed dataset needs**: what stakeholders still need in usable form
- **2.6 Use cases of climate risk and impact information**: what agencies are trying to do with these data in practice
- **2.7 Synthesis and progress implications**: what the landscape review implies for the interim report and next drafting stages

### Section 3 — Knowledge Sets (TOR 5.5 progress)
- **TOR intent recap**: expected knowledge‑set progression
- Review method and shortlist criteria (progress transparency)
- Shortlist status across 6 NAP sectors (what is ready vs pending)
- Draft article + infographic plan mapped to NCAIF (how outputs will be used in later phases; not the core proof of interim completion)

## Interim‑report inserts (appendix or stand‑alone)

1. **What FGD2 validated / changed** (1–2 pages)
2. **Sitemap vNext drill‑down + sitemap change process** (integrate Pack A caveats)
3. **Phase‑1 content gap update** (what to explain vs what already exists)
4. **Task 5.5 scope + progress snapshot**
5. **Section 1 evidence synthesis**: DCCE website gaps + Pack A product reality + Pack C UX logic, interpreted through CDM and MVP positioning

## Writing schedule (tight‑loop)

- **Now → 14 Mar:** finalize outline + evidence map; draft Exec Summary + Section 1 skeleton
- **Tone/framing checkpoint:** before drafting the merged [`Section 1.6`](ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim%20Report%20Writing%20Plan.md), confirm that Chapter 1 keeps only the analytical implications of the current landscape while the fuller descriptive material is deferred to Chapter 2
- **Pre-drafting analysis checkpoint for Section 2:** complete the comparison matrix, product landscape table, stakeholder-needs synthesis, use-case clustering, and Chapter 1 to Chapter 2 handoff note before drafting Section 2
- **15–18 Mar:** complete Sections 2–3 drafts; populate inserts
- **19–20 Mar:** consolidate appendices; align formatting with TOR
- **21–22 Mar:** internal review + QA; prepare submission pack
- **23 Mar 10:00:** submit interim report

## Living checklist (writing vs design)

- [ ] Executive Summary (draft + revise)
- [ ] Section 1: NCAIF development (TOR 5.2) — move from current-state evidence to CDM logic to workflow/MVP translation, then to refined sitemap and management-structure implications
- [ ] Section 1 framing checkpoint: use the merged [`Section 1.6`](ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim%20Report%20Writing%20Plan.md) to carry only analytical implications, with fuller descriptive landscape material relocated to Section 2 drafting inputs
- [ ] Section 1 design checkpoint: ensure the latest locked NCAIF design choices are explained in prose without dumping appendix-level sitemap detail
- [ ] Section 2 pre-drafting analysis package: comparison matrix, product landscape table, stakeholder-needs synthesis, use-case clustering, and Chapter 1 to Chapter 2 handoff note
- [ ] Section 2: inventory progress (TOR 5.3)
- [ ] Section 3: Task 5.5 progress (TOR 5.5)
- [ ] Insert: FGD2 validated/changed
- [ ] Insert: Sitemap vNext drill‑down + change process
- [ ] Insert: Phase‑1 content gap update
- [ ] Insert: Task 5.5 scope + progress
- [ ] Insert: Section 1 evidence synthesis (website + Pack A + Pack C through CDM/MVP lens)
- [ ] Appendices (risk‑map evidence, gap summary, interview signals)

## Thai appendix outline — CDM, use cases, and sitemap

Purpose:
- prepare three stand-alone appendix sections that carry the full supporting detail which would be too heavy for the main report body
- keep the main report readable while preserving the technical and structural basis behind the draft

Drafting mode:
- Thai formal report prose
- appendix style: more detailed than the main chapters, but still readable as a report section rather than as raw notes

### Appendix Section A — Detailed Conceptual Data Model (CDM)

Objective:
- explain the full CDM in enough detail for review, future system design, and traceability back to the project logic

Proposed structure:

1. **วัตถุประสงค์ของภาคผนวกส่วนนี้**
   - อธิบายว่าเหตุใดจึงต้องแสดงรายละเอียดของ CDM แยกจากเนื้อหาหลัก
   - เชื่อมว่า CDM เป็นโครงสร้างกลางของการจัดระเบียบข้อมูลสำหรับ NCAIF

2. **ภาพรวมของขอบเขตข้อมูลหลักของ CDM**
   - ขอบเขตข้อมูลด้านสภาพภูมิอากาศและตัวขับการเปลี่ยนแปลง
   - ขอบเขตข้อมูลด้านการประเมินความเสี่ยงและผลกระทบ
   - ขอบเขตข้อมูลด้านการประเมินความยืดหยุ่น
   - ขอบเขตข้อมูลด้านการวางแผนและดำเนินการปรับตัว

3. **รายละเอียดของแต่ละ subject area**
   - subject area 1: physical climate
   - subject area 2: risk and impact assessment
   - subject area 3: resilience assessment
   - subject area 4: adaptation planning

4. **รายละเอียดของ sub-domains / entities ภายใน subject area 2**
   - hazard modeling
   - vulnerability and exposure
   - risk assessment outputs
   - impact / loss and damage

5. **ตรรกะการเชื่อมโยงข้อมูลระหว่าง subject areas**
   - การเชื่อมจาก climate drivers ไปสู่ hazard map
   - การเชื่อมจาก exposed assets / vulnerability ไปสู่ risk assessment
   - การเชื่อมจาก risk outputs ไปสู่ adaptation planning และ intervention results

6. **หลักการออกแบบสำคัญของ CDM**
   - determinant neutrality
   - recursive aggregation
   - attribution logic
   - polymorphic vulnerability
   - spatial multi-tenancy
   - model agnosticism
   - projections as first-class citizens
   - intervention feedback loop

7. **ความหมายเชิงการใช้งานของ CDM ต่อ NCAIF และการพัฒนาระบบในระยะต่อไป**

Primary sources:
- [`ψ/incubate/DCCE/CRDB/output/2026-02-26-Detailed_CDM_Design.md`](ψ/incubate/DCCE/CRDB/output/2026-02-26-Detailed_CDM_Design.md)
- [`ψ/incubate/DCCE/CRDB/output/Conceptual Data Model for climate risk and adaptation data system.md`](ψ/incubate/DCCE/CRDB/output/Conceptual%20Data%20Model%20for%20climate%20risk%20and%20adaptation%20data%20system.md)

### Appendix Section B — Detailed Use Cases and User Journeys

Objective:
- document the full set of use cases, user journeys, and governance implications that informed the platform and product decisions

Proposed structure:

1. **วัตถุประสงค์ของภาคผนวกส่วนนี้**
   - อธิบายว่า use cases เป็นฐานของการออกแบบบริการและผลิตภัณฑ์ขั้นต่ำ

2. **วิธีสังเคราะห์กรณีการใช้งาน**
   - มาจากการสัมภาษณ์ stakeholder และ workshop signals อย่างไร

3. **การจัดกลุ่ม use cases หลัก**
   - post-event impact and loss/damage assessment
   - risk context for preparedness
   - provincial risk profile
   - municipality / LAO budget justification pack
   - vulnerable group mapping
   - heat-health roadmap
   - cascading impacts explainer
   - infrastructure disruption and corridor exposure
   - statistical baselines and tagging
   - true economic loss and damage estimation
   - baseline verification / single source of truth
   - financial-sector physical risk analysis

4. **รายละเอียดราย use case**
   - primary user
   - trigger / policy question
   - user journey
   - minimum data needs
   - governance needs
   - Phase 1 stance

5. **ข้อสังเกตข้าม use cases**
   - granularity needs
   - metadata needs
   - publishing constraints
   - uncertainty handling
   - printable / exportable products

6. **ความเชื่อมโยงจาก use cases ไปสู่ MVPs และโครงสร้างข้อมูล**

Primary sources:
- [`ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md)
- [`ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter2-use-case-clustering.md`](ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter2-use-case-clustering.md)

### Appendix Section C — Detailed Sitemap and Information Architecture

Objective:
- place the full sitemap and the detailed navigation logic in an appendix so the main report can explain structure without becoming a menu inventory

Proposed structure:

1. **วัตถุประสงค์ของภาคผนวกส่วนนี้**
   - อธิบายว่าเนื้อหานี้แสดงรายละเอียดเชิงโครงสร้างของแพลตฟอร์มที่ถูกย่อไว้ในบทหลัก

2. **หลักการออกแบบ sitemap**
   - adaptation-cycle backbone
   - Policy Maker Center
   - hybrid access model
   - separation between narrative surface and technical support layer
   - shallow top-level navigation
   - progressive disclosure

3. **sitemap ระดับบนทั้งหมด**
   - top-level sections
   - entry routes
   - stable backbone elements

4. **รายละเอียดระดับรองของแต่ละหมวด**
   - climate conditions
   - risks and impacts
   - loss and damage
   - adaptation planning
   - adaptation implementation
   - results and monitoring
   - Policy Maker Center
   - risk and area profiles
   - knowledge, tools, and data services

5. **รายละเอียดของ key page types / products**
   - briefing packs
   - area profiles
   - dashboards
   - catalogs and download pages
   - methods / standards / glossary pages

6. **องค์ประกอบที่คงเสถียรภาพ กับองค์ประกอบที่ปรับเปลี่ยนได้**

7. **ข้อกำกับในการเปลี่ยนแปลง sitemap ในระยะต่อไป**

Primary sources:
- [`ψ/incubate/DCCE/CRDB/output/National Climate Adaptation Information Framework.md`](ψ/incubate/DCCE/CRDB/output/National%20Climate%20Adaptation%20Information%20Framework.md)
- [`ψ/incubate/DCCE/CRDB/output/2026-03-12 - NCAIF_Pack_ABC_Decision_Matrix.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12%20-%20NCAIF_Pack_ABC_Decision_Matrix.md)
- [`ψ/incubate/DCCE/CRDB/output/2026-03-12 - NCAIF_Pack_C_UI_Analysis.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12%20-%20NCAIF_Pack_C_UI_Analysis.md)

Drafting rule for all three appendix sections:
- include every detail necessary for technical and managerial review
- keep the prose report-like, not bullet-dump only
- allow lists and tables where detail density is high

## Thai drafting outline for Chapter 2 draft

Mode: `--report`

Target length:
- fuller Chapter 2 draft
- approximately 7–9 pages in Thai report prose

Drafting objective:
- produce a sponsor-facing Thai draft of Chapter 2 that follows the anchor plan
- keep the chapter descriptive and evidence-led
- synthesize current products, data practices, unmet needs, and practical use cases without repeating the Chapter 1 architecture argument

Primary drafting sources:
- [`ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter2-current-data-product-landscape-table.md`](ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter2-current-data-product-landscape-table.md)
- [`ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter2-interview-comparison-matrix.md`](ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter2-interview-comparison-matrix.md)
- [`ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter2-stakeholder-needs-synthesis.md`](ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter2-stakeholder-needs-synthesis.md)
- [`ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter2-use-case-clustering.md`](ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter2-use-case-clustering.md)
- [`ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter1-to-Chapter2-handoff-analysis.md`](ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter1-to-Chapter2-handoff-analysis.md)
- [`ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Summary.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Summary.md)
- [`ψ/inbox/2026-03-12 - รายงานฐานข้อมูลความเสี่ยงเชิงพื้นที่จากการเปลี่ยนแปลงสภาพภูมิอากาศไทยฉบับสมบูรณ์  -notebooklm extraction.md`](ψ/inbox/2026-03-12%20-%20รายงานฐานข้อมูลความเสี่ยงเชิงพื้นที่จากการเปลี่ยนแปลงสภาพภูมิอากาศไทยฉบับสมบูรณ์%20%20-notebooklm%20extraction.md)

Numbered outline:

1. **บทนำของหมวด 2**
   - เปิดด้วยเจตนารมณ์ของ TOR 5.3.1–5.3.2 ในฐานะการทบทวนภูมิทัศน์ผลิตภัณฑ์ข้อมูลและฐานข้อมูลในระยะปัจจุบัน
   - วางกรอบว่าเนื้อหาในหมวดนี้มุ่งอธิบายสิ่งที่มีอยู่จริง วิธีที่หน่วยงานต่าง ๆ ใช้และจัดการข้อมูล สิ่งที่ยังขาด และกรณีการใช้งานหลัก
   - ย้ำว่าเป็นการทบทวนเชิงสังเคราะห์สำหรับรายงานความก้าวหน้า ไม่ใช่การอ้างว่าการจัดทำ baseline inventory เสร็จสมบูรณ์แล้ว

2. **2.1 เจตนารมณ์ของ TOR และวัตถุประสงค์ของการทบทวนภูมิทัศน์ผลิตภัณฑ์ข้อมูลในระยะปัจจุบัน**
   - อธิบายว่าเหตุผลของหมวดนี้คือทำให้เห็นสถานะปัจจุบันของผลิตภัณฑ์ข้อมูลและระบบข้อมูลที่มีอยู่
   - เชื่อมว่าหมวดนี้รองรับงานตาม TOR 5.3 โดยไม่ซ้ำกับบทสถาปัตยกรรมใน Chapter 1

3. **2.2 ภาพรวมของผลิตภัณฑ์ข้อมูลและระบบข้อมูลที่มีอยู่ในปัจจุบัน**
   - เริ่มจากภูมิทัศน์ของ DCCE website และระบบที่เกี่ยวข้อง ว่ามีทรัพย์สินข้อมูลจริงจำนวนมาก แต่กระจัดกระจายตามภารกิจและโครงการ
   - อธิบายระบบแผนที่ความเสี่ยงเชิงพื้นที่ในฐานะผลิตภัณฑ์ข้อมูลที่ก้าวหน้าที่สุดในปัจจุบัน โดยแจกแจง 3 ชั้นของผลิตภัณฑ์
   - ขยายไปยังผลิตภัณฑ์และระบบของหน่วยงานคู่สนทนา เช่น พอร์ทัลข้อมูลภัยพิบัติ ระบบสถิติ ศูนย์ข้อมูลเปิด ระบบข้อมูลภาคขนส่ง และเครื่องมือวิเคราะห์ของภาคการเงิน
   - ปิดด้วยข้อสังเกตว่าภูมิทัศน์ปัจจุบันมีสินทรัพย์จริงจำนวนมาก แต่ยังไม่เชื่อมเป็นภาพรวมเดียว

4. **2.3 ลักษณะข้อมูลที่ผู้มีส่วนเกี่ยวข้องเป็นผู้ผลิตหรือดูแล และวิธีการได้มาของข้อมูล**
   - จัดกลุ่มหน่วยงานตามลักษณะการทำงาน ไม่เรียงรายหน่วยงานแบบรายตัว
   - กลุ่มผู้ผลิตข้อมูลปฐมภูมิและข้อมูลธุรการ
   - กลุ่มผู้ประสานข้อมูลและโครงสร้างพื้นฐานข้อมูล
   - กลุ่มผู้ใช้ข้อมูลเชิงนโยบายและเชิงวิเคราะห์
   - อธิบายความแตกต่างของวิธีได้มาของข้อมูล เช่น สำรวจ รายงานตามสายงาน ทะเบียน การเชื่อม API การวิเคราะห์เชิงแบบจำลอง และการดึงจากแหล่งภายนอก

5. **2.4 ความถี่การปรับปรุงข้อมูล ระดับพื้นที่ และข้อจำกัดในการใช้งานจริง**
   - สังเคราะห์เรื่อง cadence การอัปเดตว่าบางระบบเป็น event-driven บางระบบเป็น periodic survey บางระบบเป็นโครงการเฉพาะกิจ
   - อธิบายความต่างด้านระดับพื้นที่ ตั้งแต่ระดับประเทศ จังหวัด อำเภอ ตำบล เทศบาล ไปจนถึงระดับทรัพย์สินหรือจุดเฉพาะ
   - ชี้ข้อจำกัดหลัก เช่น ความไม่ครบถ้วน ความล่าช้า การไม่มี metadata ความไม่สอดคล้องของนิยาม การจำกัดสิทธิ์เข้าถึง และความเสี่ยงในการตีความผิดเกินขอบเขตข้อมูล

6. **2.5 ความต้องการข้อมูลที่หน่วยงานต่าง ๆ ยังขาดอยู่**
   - จัดความต้องการออกเป็นกลุ่มหลักตาม synthesis note
   - ข้อมูลคาดการณ์ระยะยาวและ scenario ที่เชื่อถือได้
   - baseline และตัวชี้วัดมาตรฐานกลาง
   - metadata และ data dictionary
   - ข้อมูลที่ละเอียดสอดคล้องกับระดับการตัดสินใจ
   - ข้อมูลความสูญเสียและความเสียหายทางเศรษฐกิจที่แท้จริง
   - ข้อมูลความเปราะบางและขีดความสามารถในการปรับตัว
   - เส้นทางการเข้าถึงและการเผยแพร่ข้อมูลที่ปลอดภัยและชัดเจน

7. **2.6 กรณีการใช้งานของข้อมูลความเสี่ยงและผลกระทบจากการเปลี่ยนแปลงสภาพภูมิอากาศ**
   - จัด use cases เป็นกลุ่มสังเคราะห์ ไม่เล่าแบบหน่วยงานต่อหน่วยงาน
   - การตอบสนองภัยพิบัติและการประเมินหลังเหตุการณ์
   - การวางแผนท้องถิ่นและการของบประมาณ
   - การคุ้มครองกลุ่มเปราะบางและการจัดบริการสังคม
   - การวางแผนเศรษฐกิจมหภาคและการประเมินระดับชาติ
   - การวางแผนความยืดหยุ่นของโครงสร้างพื้นฐาน
   - การวิเคราะห์ความเสี่ยงของภาคการเงิน
   - ปิดด้วยข้อสังเกตว่า use cases เหล่านี้สะท้อนว่าความต้องการข้อมูลไม่ได้มีเพียงเพื่อการสื่อสาร แต่เพื่อการตัดสินใจจริงในหลายบริบท

8. **2.7 ข้อสังเกตเชิงสังเคราะห์จากการทบทวนภูมิทัศน์ผลิตภัณฑ์ข้อมูลและผลการสัมภาษณ์**
   - สรุปว่าไทยมีผลิตภัณฑ์ข้อมูลและระบบข้อมูลอยู่แล้วจำนวนมาก
   - แต่ข้อมูลและระบบเหล่านี้ยังแยกส่วนกันทั้งในเชิงสถาบัน มาตรฐาน คำอธิบาย และการค้นพบ
   - ชี้ว่าความท้าทายสำคัญไม่ใช่การเริ่มจากศูนย์ แต่คือการจัดระเบียบ เชื่อมโยง อธิบายข้อจำกัด และทำให้ผู้ใช้เลือกใช้ได้อย่างมั่นใจ
   - ส่งต่อเหตุผลอย่างนุ่มนวลไปสู่หมวดถัดไปของรายงานโดยไม่ย้อนกลับไปแบกภาระเชิงสถาปัตยกรรมของ Chapter 1

9. **หลักการเขียนตลอดทั้งหมวด**
   - ใช้ภาษารายงานทางการ อ่านเป็นฉบับส่งผู้ว่าจ้าง
   - เปิดแต่ละหัวข้อด้วยข้อค้นพบเชิงปฏิบัติ ไม่เปิดด้วยกระบวนการวิเคราะห์ภายใน
   - รักษาแนวเขียนแบบสังเคราะห์ ไม่ทำให้เนื้อหาแตกเป็นบันทึกสัมภาษณ์รายหน่วยงาน
   - กล่าวถึงข้อจำกัดของข้อมูลอย่างตรงไปตรงมา แต่ไม่ทำให้น้ำเสียงกลายเป็นบันทึกปัญหาภายในทีม
