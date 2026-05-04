# NCAIF Refinement Decision Matrix — Packs A, B, C 

## Purpose

Reconcile the three evidence packs for NCAIF refinement into explicit design decisions before revising the sitemap and interim-report insert.

- **Pack A** = product reality and constraints from [`ψ/inbox/2026-03-12 - รายงานฐานข้อมูลความเสี่ยงเชิงพื้นที่จากการเปลี่ยนแปลงสภาพภูมิอากาศไทยฉบับสมบูรณ์  -notebooklm extraction.md`](ψ/inbox/2026-03-12-รายงานฐานข้อมูลความเสี่ยงเชิงพื้นที่จากการเปลี่ยนแปลงสภาพภูมิอากาศไทยฉบับสมบูรณ์-notebooklm%20extraction.md)
- **Pack B** = TOR and interim-report framing from [`ψ/incubate/DCCE/CRDB/CRDB - TOR.md`](ψ/incubate/DCCE/CRDB/CRDB%20-%20TOR.md), [`ψ/incubate/DCCE/CRDB/Task 5.5 Scope.md`](ψ/incubate/DCCE/CRDB/Task%205.5%20Scope.md), and [`ψ/incubate/DCCE/CRDB/Interim Report Writing Plan.md`](ψ/incubate/DCCE/CRDB/Interim%20Report%20Writing%20Plan.md)
- **Pack C** = UI benchmark principles from [`ψ/incubate/DCCE/CRDB/inbox_source/2026-03-12 - User Experience Design Principles for National Climate Change Adaptation Information Services.md`](ψ/incubate/DCCE/CRDB/inbox_source/2026-03-12%20-%20User%20Experience%20Design%20Principles%20for%20National%20Climate%20Change%20Adaptation%20Information%20Services.md)

## Decision rules

- **Keep** = preserve the current direction largely as-is
- **Revise** = keep the concept but change label, placement, or framing
- **Add** = introduce a new page, wrapper, or rule not explicit enough before
- **Defer** = valid idea, but not Phase 1
- **Link out** = expose through contextual links rather than first-class ownership or deep build

## Matrix

Citation note: in the **Pack C signal** column, Pack C-derived claims are supported by the deep-research note’s cited sources on information scent, transaction-log navigation, matrix taxonomy, tool-versus-catalog separation, progressive disclosure, narrative onboarding, and retention. The most reused citation anchors are: Climate-ADAPT for matrix taxonomy and multi-entry structure (Climate-ADAPT, n.d.); the World Bank CCKP for the combination of authoritative data with narrative profiles (World Bank, n.d.); information-scent and navigation studies for hierarchy depth and click-path friction ("The scent of a site," n.d.; "Exploring User Navigation," n.d.; "Finding Unexpected Navigation Behaviour," n.d.); behavioral and usability sources for progressive disclosure and adoption (Userflow, n.d.; The Decision Lab, n.d.); and climate-service platform guidance for user-interface platforms and feedback loops (World Meteorological Organization, n.d.; Statsig, n.d.; Quantum Metric, n.d.). Pack A and Pack B claims remain anchored to their respective source notes listed above.

| Topic | Current / candidate design element                      | Pack A signal                                                                                      | Pack B signal                                            | Pack C signal                                                                                | Decision       | Implication for sitemap                                                                                   |
| ----- | ------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------- | --------------------------------------------------------------------------------------------------------- |
| 1     | Adaptation-cycle backbone                               | Compatible with the risk-map product as long as pages do not over-promise sub-provincial analytics | Supports NCAIF narrative and interim-report framing      | Strong narrative workflow improves information scent and reduces cognitive load              | **Keep**       | Maintain adaptation cycle as the core organizing logic                                                    |
| 2     | Policy Maker Center as prominent entry                  | Risk-map outputs can support decision-ready summaries at provincial level                          | Interim report needs decision-ready framing              | Benchmark supports short top-level lists, strong landing pages, and actionable entry points  | **Keep**       | Preserve a dedicated policy-maker landing area near the top of the sitemap                                |
| 3     | Risk and Area Profiles as a major section               | Strongly supported by Pack A; this is where the product is most real                               | Fits TOR 5.2 and interim-report story                    | Benchmark supports geography-based entry and guided discovery                                | **Keep**       | Retain this as a first-class section                                                                      |
| 4     | Public-facing risk map as a flagship feature            | Supported, but only at provincial scale with explicit caveats                                      | Allowed as NCAIF-facing output if framed correctly       | Tools should be task-oriented and not mixed with raw catalog UX                              | **Revise**     | Present as guided provincial dashboard with explanation, not as free-form expert analytics                |
| 5     | Climate science page under adaptation-cycle navigation  | Supported by Pack A with scenarios, hazards, and time slices                                       | Useful for Chapter 1 and Chapter 3 narrative             | Benchmark favors clear information scent and progressive disclosure                          | **Keep**       | Maintain climate and hazard explainers as core early-stage pages                                          |
| 6     | Data catalog and tools grouped into one strand          | Backend integration is real, but user needs are distinct                                           | Task 5.5 is content/knowledge, not tool engineering      | Strongly argues for front-end separation of data catalog and tools, with backend integration | **Revise**     | Separate tool discovery from raw data discovery while linking them contextually                           |
| 7     | Create-your-own risk maps as visible Phase-1 promise    | Mentioned in Pack A, but advanced and likely specialist-facing                                     | Outside defensible minimum scope for current Phase 1     | Benchmark warns against overwhelming mixed-literacy users                                    | **Defer**      | Keep out of major public navigation; mention as future or specialist capability                           |
| 8     | Advanced drill-down on E, S, AC components              | Technically plausible for analysts, but risky as a broad public promise                            | Not essential for interim-report proof                   | Progressive disclosure supports hiding complexity until needed                               | **Revise**     | Treat as secondary analyst feature under guided access, not default public homepage content               |
| 9     | Download center for underlying data                     | Supported in Pack A                                                                                | Consistent with inventory and discovery work             | Catalog/tool separation implies this belongs in a data-service environment                   | **Keep**       | Provide as contextual bridge from tools to data catalog or download area                                  |
| 10    | Methodology and standards as top-level headline section | Necessary for trust, but not the primary public identity                                           | Needed for defensible interim-report language            | Benchmark favors progressive disclosure rather than forcing methodology upfront              | **Revise**     | Keep in Knowledge/Methods support layer, not as a dominant homepage promise                               |
| 11    | Limitations and uncertainty guidance                    | Pack A makes this mandatory                                                                        | Pack B requires defensible scope language                | Benchmark stresses algorithmic transparency with progressive disclosure                      | **Add**        | Add explicit caveat blocks and interpretation pages tied to risk-map and climate pages                    |
| 12    | Province profile pages                                  | Strongly supported by Pack A                                                                       | Needed for interim-report usable outputs                 | Geography-first entry improves discoverability                                               | **Add**        | Introduce province/area profile wrappers around the existing risk-map product                             |
| 13    | Cross-area comparison views                             | Supported only at provincial comparison level                                                      | Useful for policy makers if carefully framed             | Fits matrix navigation and decision-oriented tasks                                           | **Revise**     | Keep comparisons at province level only and clearly label them as relative comparisons                    |
| 14    | Adaptation Measures Library                             | Supported by Pack B as a content-layer need; sources exist but are dispersed                       | Strong fit with Task 5.5 knowledge outputs               | Benchmark favors narrative onboarding and curated exemplars                                  | **Add** %%No%% | Create a curated measures-and-good-practice section, likely as a content library rather than raw registry |
| 15    | Loss and Damage explainer / node                        | Pack A does not weaken it; it sits adjacent to risk interpretation                                 | Interim-report and TOR framing both support its presence | Narrative pathways support a dedicated explainer                                             | **Add**        | Keep as a distinct explainer or sub-section under the adaptation-cycle flow                               |
| 16    | Adaptation M&E content as major standalone branch       | Dependency exists, but product is being built by another team                                      | Must stay inside scope and not duplicate parallel work   | Benchmark supports linking related systems instead of overstuffing one portal                | **Link out**   | Reference and connect to Adaptation M&E outputs without making them the core NCAIF identity               |
| 17    | Hazard-exposure overlay tool as core NCAIF feature      | Still under development elsewhere                                                                  | Should not be over-claimed in current scope              | Avoid promising unusable or unfinished tools                                                 | **Link out**   | Mention as connected service or future integration, not flagship Phase-1 feature                          |
| 18    | Climate data from TMD, GISTDA, and others               | Pack A confirms DCCE is not the only source                                                        | Fits NCAIF as integration and translation layer          | Matrix taxonomy supports multiple entry vectors and linked discovery                         | **Keep**       | Explicitly frame climate science pages as curated multi-agency knowledge, not DCCE-only ownership         |
| 19    | Deep hierarchical menus with many sub-items             | No product need for this                                                                           | Not required for TOR                                     | Benchmark explicitly warns against deep hierarchies and weak information scent               | **Defer**      | Keep top-level navigation short and use exemplars plus lateral links                                      |
| 20    | Narrative case studies and briefing packs               | Supported as packaging around existing evidence                                                    | Strong Task 5.5 and interim-report fit                   | Narrative engineering and peak-end rule strongly support these                               | **Add**        | Add briefing packs, story-based case pages, and export-ready narratives as first-class content wrappers   |

## Emerging architecture stance

### Stable backbone to preserve

1. Adaptation-cycle backbone
2. Policy Maker Center / decision-ready landing area
3. Risk and Area Profiles
4. Climate and hazard explainers
5. Knowledge and service layers that support trust and reuse

### Elements to revise

1. Separate **tools** from **data catalog** in front-end navigation
2. Reframe advanced analytics as secondary or specialist-facing
3. Move methodology and standards into support layers with progressive disclosure
4. Keep cross-area comparison explicitly relative and provincial-scale

### New content wrappers required for Phase 1
1. Province or area profile pages
2. Risk-map interpretation and limitations pages
3. Loss and Damage explainer
4. Briefing packs and narrative case studies

### Items to defer or avoid over-claiming
1. Create-your-own risk maps as mainstream user feature
2. Sub-provincial or fine-grained area planning claims
3. Full integration of unfinished external tools
4. Deep, catalog-like menu exposure to non-technical users
5. Adaptation Measures Library %% This is outside the scope. We can provide guideline how to do it but we are not doing it%%

### Items to link out
1. Adaptation M&E platform outputs
2. Hazard-exposure overlay tool under external development %%will be integrated into DCCE IT system%%
3. External climate data provider services where direct duplication is unnecessary

## Consequence for the next step
The refined NCAIF structure should now be written as a **hybrid architecture**. This synthesis is justified by Pack A product reality, Pack B TOR containment, and Pack C’s presentation logic around narrative onboarding, shallow navigation, and task-oriented pathways. On the Pack C side, the strongest supporting precedents are matrix-style climate portals such as Climate-ADAPT, narrative workflow design such as the U.S. Climate Resilience Toolkit, and the World Bank’s combination of data collections with country-profile packaging (Climate-ADAPT, n.d.; U.S. Climate Resilience Toolkit, n.d.; World Bank, n.d.).
- **narrative and decision-oriented on the surface**
- **catalog-linked and method-transparent underneath** 
- **strictly limited by provincial-scale risk-map reality**
- **strengthened by Task 5.5 as the explanatory content layer**

## What this means for the interim-report insert

The insert should say the post-FGD2 refinement did **not** abandon the original sitemap direction. Instead, it deepened it in four ways, based on the combined reading of product constraints, TOR scope, and Pack C usability guidance. The usability side is best supported by cited evidence on information scent, matrix taxonomy, narrative case-based onboarding, and staged transparency ("The scent of a site," n.d.; Climate-ADAPT, n.d.; U.S. Climate Resilience Toolkit, n.d.; World Bank, n.d.; World Meteorological Organization, n.d.).

1. clarified which existing products are real and Phase-1 ready
2. added the missing content wrappers and explainers needed for usability
3. separated data-discovery and tool-discovery logic to reduce cognitive overload
4. tightened scope to avoid promising advanced features beyond TOR and current product maturity
