# CRDB Section 1 analysis — CDM, NCAIF structure, and risk-map evidence

## Purpose

This note analyzes how **CDM** should be positioned in the interim report when read together with:

- the current NCAIF information structure in [`ψ/incubate/DCCE/CRDB/output/National Climate Adaptation Information Framework.md`](ψ/incubate/DCCE/CRDB/output/National%20Climate%20Adaptation%20Information%20Framework.md)
- the DCCE website gap analysis in [`ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Summary.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Summary.md)
- the spatial risk-map report extraction in [`ψ/inbox/2026-03-12 - รายงานฐานข้อมูลความเสี่ยงเชิงพื้นที่จากการเปลี่ยนแปลงสภาพภูมิอากาศไทยฉบับสมบูรณ์  -notebooklm extraction.md`](ψ/inbox/2026-03-12%20-%20รายงานฐานข้อมูลความเสี่ยงเชิงพื้นที่จากการเปลี่ยนแปลงสภาพภูมิอากาศไทยฉบับสมบูรณ์%20%20-notebooklm%20extraction.md)
- the UX benchmark source in [`ψ/incubate/DCCE/CRDB/inbox_source/2026-03-12 - User Experience Design Principles for National Climate Change Adaptation Information Services.md`](ψ/incubate/DCCE/CRDB/inbox_source/2026-03-12%20-%20User%20Experience%20Design%20Principles%20for%20National%20Climate%20Change%20Adaptation%20Information%20Services.md)

## Core reading

The current story should not present CDM as a detached technical deliverable. It should present CDM as the **architectural explanation** for why DCCE must move beyond a fragmented website and beyond one standalone risk-map product if it wants to satisfy the intent of TOR 5.2.

## Missing methodological layer that must be made explicit

The missing piece is not more architecture detail. It is the explanation of **how the project got to the current architecture**.

Section 1 should explicitly state that the current NCAIF logic emerged from four methodological streams:

1. **Stakeholder interviews and workshops** to derive user demand, workflow needs, pain points, publishing constraints, and metadata expectations.
2. **Conceptual data modeling and interoperability literature** to justify why a shared blueprint was needed before building inventories, services, or logical datasets.
3. **Standards review** to align entity logic and naming with IPCC, WMO, UNFCCC, and ISO.
4. **Predecessor and current-system review** through T-PLAT, the DCCE web estate, and the new spatial risk-map report.

Without this layer, CDM and MVPs look like design preferences. With this layer, they become evidence-based project outputs.

## How user demand and preference were actually derived

The strongest evidence is in [`ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md).

That document shows that user demand was not guessed. It was synthesized from:
- stakeholder interviews
- workshop notes
- FGD1 signals on usability, language, workflow, QA/QC, preview needs, review workflows, and audience tiering
- cross-agency constraints on spatial units, timeliness, data discovery, privacy, budget justification, and publication risk

This gives the project a clear methodological claim:

- **workflow patterns** were distilled from repeated user journeys and operational tasks
- **MVPs** were derived from repeated service needs that cut across multiple use cases
- **information architecture choices** were shaped by observed confusion, search friction, publishing bottlenecks, and mixed literacy levels

So the report should say that NCAIF structure and MVP prioritization are grounded in stakeholder demand synthesis, not only benchmark inspiration.

## Why the project knew it needed CDM

The strongest internal statement is in [`ψ/incubate/DCCE/CRDB/output/Conceptual Data Model for climate risk and adaptation data system.md`](ψ/incubate/DCCE/CRDB/output/Conceptual%20Data%20Model%20for%20climate%20risk%20and%20adaptation%20data%20system.md), which explicitly maps TOR requirements to the need for conceptual modeling.

Its logic is straightforward:

- TOR 5.2.3 asks for a **data management structure**
- TOR 5.3.5 asks for baseline data inventory categories aligned to a risk framework
- TOR 5.3.6 asks for a future logical dataset structure for Loss and Damage
- TOR 5.3.8 asks for supply-vs-demand gap analysis

These tasks require a prior understanding of **what entities exist, how they relate, and what business rules matter**. That is the role of a conceptual data model.

This is reinforced by the background notes in [`ψ/incubate/DCCE/CRDB/inbox_source/What is Conceptual Data Modeling Purpose & Examples.md`](ψ/incubate/DCCE/CRDB/inbox_source/What%20is%20Conceptual%20Data%20Modeling%20Purpose%20%26%20Examples.md) and [`ψ/incubate/DCCE/CRDB/inbox_source/Conceptual vs Logical vs Physical Data Models.md`](ψ/incubate/DCCE/CRDB/inbox_source/Conceptual%20vs%20Logical%20vs%20Physical%20Data%20Models.md), both of which support the business-facing role of CDM as a bridge between requirements and implementation.

## Why the current CDM looks the way it does

The current CDM is not arbitrary. It was shaped by standards review and interoperability problems.

Key evidence:

- [`ψ/incubate/DCCE/CRDB/inbox_note/Technical Interoperability and Data Modeling in Disaster Risk Reduction - A Comparative Analysis of IPCC, Sendai, and Global Standards.md`](ψ/incubate/DCCE/CRDB/inbox_note/Technical%20Interoperability%20and%20Data%20Modeling%20in%20Disaster%20Risk%20Reduction%20-%20A%20Comparative%20Analysis%20of%20IPCC,%20Sendai,%20and%20Global%20Standards.md)
- [`ψ/incubate/DCCE/CRDB/output/National Climate Adaptation Information Framework.md`](ψ/incubate/DCCE/CRDB/output/National%20Climate%20Adaptation%20Information%20Framework.md)

These sources explain why the entity logic had to align with:

- **IPCC** for hazard, exposure, vulnerability, impact, and iterative adaptation framing
- **WMO** for hazardous-event logic and UUID-based event identity
- **UNFCCC** for adaptation and reporting structure
- **ISO** for vulnerability logic and adaptation-cycle management

This is why the CDM uses constructs such as:

- `CLIMATE_DRIVER`
- `HAZARDOUS_EVENT`
- `SPATIAL_UNIT`
- `VULNERABILITY_DEFINITION`
- `ATTRIBUTION_LINK`

The report should explain these as responses to methodological needs, not just modeling creativity.

## T-PLAT as predecessor, not just benchmark

The T-PLAT materials are not decorative background. They explain why NCAIF must go beyond a portal model.

Most important sources:

- [`ψ/incubate/DCCE/CRDB/inbox_source/T-PLAT analysis.md`](ψ/incubate/DCCE/CRDB/inbox_source/T-PLAT%20analysis.md)
- [`ψ/incubate/DCCE/CRDB/inbox_source/Learnings from T-PLAT - Benchmarking CDM.md`](ψ/incubate/DCCE/CRDB/inbox_source/Learnings%20from%20T-PLAT%20-%20Benchmarking%20CDM.md)
- [`ψ/incubate/DCCE/CRDB/inbox_source/T-PLAT - Thailand Climate Change Adaptation Information Platform.md`](ψ/incubate/DCCE/CRDB/inbox_source/T-PLAT%20-%20Thailand%20Climate%20Change%20Adaptation%20Information%20Platform.md)

The T-PLAT review contributes two critical arguments:

1. T-PLAT provides a useful precedent for sector organization, governance coordination, and science-to-action ambition.
2. T-PLAT also reveals why a document-heavy or portal-like model is insufficient for actionable, interoperable, multi-stakeholder climate services.

This matters because it strengthens the case for both:

- **CDM** as the hidden relational structure that T-PLAT lacked
- **MVPs** as a safeguard against drifting back into a static library model

## What the current evidence says

### 1. The current DCCE web estate has content, but not a usable adaptation information service

The website gap analysis shows that the current DCCE site is **administration-first and portal-of-portals**, with fragmented tools, dispersed reports, and no consistent adaptation-cycle narrative or policy-maker front door. See [`ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Summary.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Summary.md).

Implication:

- the problem is not absence of content alone
- the problem is absence of an organizing logic that can connect content, products, user journeys, and governance

That is exactly the narrative slot where **CDM** belongs.

### 2. The risk-map report provides a real product domain, but only a bounded one

The risk-map extraction shows a three-layer product reality:

1. a **data model and indices** layer
2. a **user-facing map/dashboard** layer
3. a **backend database and tools** layer

It also makes the boundary conditions explicit:

- strongest reporting scale is **provincial**
- the risk index is **relative**, not a direct financial-loss measure
- socio-economic variables in future projections are effectively **held static**
- public-facing use is strongest for hotspot identification and broad prioritization, not fine-grained local design

See [`ψ/inbox/2026-03-12 - รายงานฐานข้อมูลความเสี่ยงเชิงพื้นที่จากการเปลี่ยนแปลงสภาพภูมิอากาศไทยฉบับสมบูรณ์  -notebooklm extraction.md`](ψ/inbox/2026-03-12%20-%20รายงานฐานข้อมูลความเสี่ยงเชิงพื้นที่จากการเปลี่ยนแปลงสภาพภูมิอากาศไทยฉบับสมบูรณ์%20%20-notebooklm%20extraction.md).

Implication:

- the risk-map product is the most mature current evidence for NCAIF-facing value
- but it does **not** equal the whole NCAIF
- and it does **not** remove the need for a broader conceptual model that can relate climate data, risk components, methods, outputs, and governance

Therefore the risk-map evidence strengthens CDM rather than replacing it.

### 3. The UX benchmark clarifies that interface value and backend structure must be distinct but linked

The UX benchmark source argues that climate information platforms should behave as **dynamic User Interface Platforms**, not static repositories, and that they require:

- strong information scent
- shallow top-level navigation
- matrix-style entry routes
- progressive disclosure
- front-end separation of tools and catalogs with backend integration
- narrative pathways that connect data to decision-making

See [`ψ/incubate/DCCE/CRDB/inbox_source/2026-03-12 - User Experience Design Principles for National Climate Change Adaptation Information Services.md`](ψ/incubate/DCCE/CRDB/inbox_source/2026-03-12%20-%20User%20Experience%20Design%20Principles%20for%20National%20Climate%20Change%20Adaptation%20Information%20Services.md), especially its arguments on information scent, matrix taxonomy, decoupled architecture, and narrative-driven IA.

Implication:

- CDM should **not** be pushed into the user-facing surface as if users must navigate the model itself
- but the interface will fail unless a hidden structural layer keeps tools, catalogs, explainers, methods, and governance connected coherently

This again gives CDM a strong explanatory role.

## Analysis of the current CDM design in this context

### The current CDM is directionally correct, but its story needs reframing

The current NCAIF design already assumes that a single national adaptation service must connect multiple kinds of things:

- climate and hazard information
- risk and area profiles
- adaptation measures and implementation content
- data services and catalogs
- methods, standards, and caveats

See [`ψ/incubate/DCCE/CRDB/output/National Climate Adaptation Information Framework.md`](ψ/incubate/DCCE/CRDB/output/National%20Climate%20Adaptation%20Information%20Framework.md).

This means the CDM should not be described narrowly as a database schema for storing scientific variables. It should be described as the **conceptual management structure** that allows these different product and content types to coexist as one national information service.

### What the CDM must do now

Given the current evidence, the CDM must support at least five structural jobs:

1. **Absorb the risk-map domain correctly**
   - hazards, exposure, vulnerability, adaptive capacity, scenarios, time slices, spatial scale, methods, and caveats

2. **Bridge product types**
   - public dashboards
   - expert drill-down tools
   - data services and downloads
   - explanatory and methodological pages

3. **Support NCAIF navigation logic without becoming the navigation itself**
   - the sitemap should present user-oriented pathways
   - the CDM should keep the relationships behind those pathways coherent

4. **Make governance visible but not overwhelming**
   - provenance, limitations, ownership, and publishing conditions must be supported structurally

5. **Support phased growth**
   - Phase 1 can expose only the product domains that are real and usable now
   - later phases can add richer implementation, knowledge-set, and event-based domains

### What the CDM should not be asked to do in the interim-report story

- It should not be narrated as a promise of full software implementation.
- It should not be treated as if all future domains are equally mature today.
- It should not be mistaken for the front-end experience.

## Positioning of MVPs relative to CDM

The logs and workflow documents suggest a stable distinction:

- **workflow patterns** = the repeatable steps users take
- **MVPs** = the visible, bounded service expressions that help users complete those steps

See [`ψ/incubate/DCCE/CRDB/output/NCAIF — Workflow patterns + MVP v3.md`](ψ/incubate/DCCE/CRDB/output/NCAIF%20%E2%80%94%20Workflow%20patterns%20%2B%20MVP%20v3.md) and [`ψ/memory/logs/info/2026-03-09_20-18_mvp-vs-workflow-patterns-and-mvp2-groundwork.md`](ψ/memory/logs/info/2026-03-09_20-18_mvp-vs-workflow-patterns-and-mvp2-groundwork.md).

In this framing:

- **CDM** is the hidden coherence layer
- **MVPs** are the visible service wrappers

This means the interim report should keep CDM narratively prior to MVPs.

### Practical implication for Phase 1 MVPs

- **MVP-3** is important because the fragmented website and tool landscape need a trustworthy dataset and product discovery logic.
- **MVP-1** matters because Pack C and the gap analysis both show the need for decision-ready, narrative, low-friction outputs.
- **MVP-4** matters because the risk-map product requires caveats, interpretation standards, and staged transparency.
- **MVP-2** should remain clearly framed as groundwork and not confused with the existing spatial risk-map product.

## Recommended Section 1 story

Section 1 should read like this:

1. DCCE asked for a national adaptation information framework and management structure.
2. Stakeholder interviews and workshops revealed what users actually need, where current systems fail, and what kinds of outputs are decision-relevant.
3. Literature and standards review showed that these needs require a conceptual data blueprint aligned with IPCC, WMO, UNFCCC, and ISO logic.
4. T-PLAT review showed the value of a national adaptation portal, but also the limitations of a static or weakly structured portal model.
5. Existing DCCE web content and tools are real but fragmented.
6. The new spatial risk-map report gives DCCE one strong product domain, but with clear scale and interpretation boundaries.
7. UX evidence shows that a usable national service cannot simply expose raw portals, reports, and methods in one undifferentiated structure.
8. Therefore the project needs a hidden organizing layer: **CDM as conceptual management structure**.
9. NCAIF becomes the user-facing expression of that structure.
10. MVPs become the bounded Phase 1 service expressions that make the structure useful without over-claiming platform maturity.

## Bottom line

The latest evidence does **not** weaken the need for CDM. It clarifies its proper role.

The correct storytelling is:

- the **website gap** tells us why a new structure is needed
- the **risk-map report** tells us what product reality is already available and where its boundaries lie
- the **UX benchmark** tells us how the interface should behave
- the **CDM** explains how those realities can be integrated coherently
- the **MVPs** show what Phase 1 can visibly deliver on top of that logic
