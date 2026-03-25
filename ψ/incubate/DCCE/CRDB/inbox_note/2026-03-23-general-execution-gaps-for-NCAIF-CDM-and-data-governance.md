# General execution gaps for NCAIF, CDM, and data governance

This note captures the **project-level execution gaps** that still need to be closed to move the CRDB work from validated concept into operational execution.

It is intentionally independent from any single stakeholder interview. Interview-specific analysis for the Head of CCE belongs in [`2026-03-23-17200-prep-for-HEAD-CCE-interview.md`](ψ/incubate/DCCE/CRDB/inbox_note/2026-03-23-17200-prep-for-HEAD-CCE-interview.md).

## 1. NCAIF execution gaps

| Gap                                                                                                                                                 | Why it matters now                                                                                                 | What still needs clarification                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Visible service scope is still broader than named operational ownership**                                                                         | FGD2 validated the sitemap direction, but execution still requires named content and service owners                | Which unit owns each part of the public-facing service surface, and which functions are only contributors                                          |
| **Adaptation-cycle content is agreed conceptually, but not yet assigned by function**                                                               | The framework covers risk, planning, implementation, and M&E, but execution requires someone to curate each branch | Which teams are responsible for climate and risk knowledge, implementation knowledge, M&E content, and cross-linking across the cycle              |
| **Detailed topic governance is not yet anchored to business ownership**                                                                             | Stakeholders want the sitemap to remain flexible, but flexibility without a change owner causes drift              | Who approves new topics, retires outdated pages, and keeps topic pages aligned with actual datasets and reports                                    |
| **Catalog-first is agreed, but the relationship between website pages, thematic information pages, and catalog records is not yet operationalized** | The system can fail if users encounter fragmented portals and duplicate content again                              | Whether NCAIF should act mainly as a curated front door into existing assets, a publishing surface for selected assets, or a mixture of both       |
| **Service tiers are implied but not explicitly assigned**                                                                                           | Different users need public explainers, technical references, and internal coordination views                      | Which outputs should exist at which level, and who is responsible for maintaining summary pages, technical notes, and internal stewardship records |

## 2. CDM execution gaps

| Gap | Why it matters now | What still needs clarification |
|---|---|---|
| **CDM is accepted as hidden logic, but the adoption path is still abstract** | FGD2 discussion shows the model still needs institutional adoption after the project | Whether the CDM is only a reference model or the structure that future cataloging, integration, and product design must explicitly follow |
| **Priority subject areas for first implementation are not yet confirmed at project level** | Not every domain can be instantiated at once | Which domains should be prioritized first for operational use: climate trends, hazards, impacts, vulnerability, adaptation knowledge, uncertainty, or others |
| **Boundary between hosted data, referenced data, and curated knowledge is still blurry** | A catalog-first architecture only works when this boundary is explicit | For each major topic, whether the system should host data, mirror data, link to source agencies, or publish only interpretation and guidance |
| **The model needs named domain authorities for definitions and semantics** | Without this, metadata, interoperability, and baseline endorsement will be inconsistent | Which units or agencies define or co-define core concepts such as hazard, impact, vulnerability, adaptation measures, and uncertainty language |

## 3. Data-governance execution gaps

| Gap | Why it matters now | What still needs clarification |
|---|---|---|
| **Owner vs steward vs custodian roles are not yet operationally assigned** | Governance cannot move from paper to practice without real role mapping | Which roles sit with thematic units, central catalog teams, digital teams, and source agencies |
| **Recommended-baseline endorsement needs a decision-rights model** | The most visible Phase 1 value proposition is the trusted baseline registry | Who can propose, review, endorse, publish, and supersede recommended datasets for specific uses |
| **Minimum metadata is known in principle, but not yet institutionalized by topic** | The catalog depends on fields like owner, cadence, limitations, intended use, and access path | What minimum metadata must exist before a climate dataset or information product is surfaced to users |
| **Publishing rails need topic-specific interpretation** | Open, GDX, and internal-only rules vary by dataset class | Which datasets can be open, which need controlled government exchange, and which should stay internal |
| **Methodology and uncertainty communication remain under-owned** | BTR and CRDB both depend on trustworthy interpretation, not just files | Who is responsible for methodology notes, uncertainty disclaimers, intended-use guidance, and safe-use warnings |
| **Operating continuity under staff turnover is still a risk** | Governance was explicitly justified in FGD2 as continuity protection | What recurring process can realistically be maintained for update review, contact maintenance, dataset change logging, and supersession history |

## 4. Cross-cutting project-level implication

Across NCAIF, CDM, and data governance, the core unresolved issue is not only technical design. The main project-level gap is the absence of an agreed operating model that connects:

1. thematic ownership
2. catalog and metadata stewardship
3. baseline endorsement and supersession
4. publication and access-control decisions
5. methodology and uncertainty communication

Until those functions are assigned to real teams and recurring processes, the CRDB outputs remain conceptually coherent but only partially executable.
