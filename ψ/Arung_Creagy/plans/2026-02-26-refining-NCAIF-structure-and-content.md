---
project: DCCE_CRDB
status: archived
created: 2026-02-26
tags:
type: plan
---
# Session Plan: Refining NCAIF structure and content (redo)

## Objective

- Refine NCAIF structure to reflect real user journeys, climate literacy constraints, and Phase 1 flagship products.
- Align CDM/NCAIF priorities with interview-derived gaps and governance needs.

## Interview insights (gaps + use-case seeds)

Short synthesis of what the NCAIF/CDM must address, based on stakeholder interviews in `src/01_Projects/2025-11_DCCE-CRDB/sources/Interview result/`:

- **Data discovery + metadata pain** (datasets hard to find/interpret) → Phase 1 must include a **catalog with minimum metadata + limitations**.
- **Granularity mismatch** (province too coarse; budget holders are often municipality/LAO; small-area baselines like EA may matter) → NCAIF must make **spatial unit selection + boundary crosswalks** explicit.
- **Event reality** (lag/noise; operational definition of “disaster”; incentives drive reporting) → Phase 1 should be **post-event workflow-first**, with freshness and quality flags.
- **Climate literacy gaps** (multi-hazard/cascading impacts; disaster vs climate confusion) → NCAIF must include **interpretive guidance**.
- **Sensitive data constraints** (privacy/legal/accountability) → publishable outputs need **classification + aggregation rules + access pathways**.

## Hypothesis

- Hybrid NCAIF design: thematic taxonomy + policymaker user journey.
- CDM/NCAIF should translate external terminology into DCCE’s glossary and data model.
- FGD2 should drive agreement on:
  - Data model design principles (analysis workflow-first)
  - Key domain entities
  - NCAIF design principles (persona-first entry with thematic backbone)
  - NCAIF structure + Phase 1 flagship products
  - Practicality given climate literacy constraints
  - Data governance phasing plan

## Tasks

- [x] Understand the workflow [[00_WORKFLOW]]

Extract

- [x] Review interview summaries in `src/01_Projects/2025-11_DCCE-CRDB/sources/Interview result` and extract gaps + use cases for NCAIF/CDM/FGD2 alignment.
- [x] Extract use cases for policymaker/user-journey design (municipality-level, vulnerable groups, infrastructure exposure, loss & damage).

Document

- [x] Create or update a use-case artifact to document these insights for NCAIF user-journey design.

Synthesize

- [x] Update [[Data Governance Strategy - version tracker]] (v2) to expand Phase 1; ingest inline comments and interview insights.

Design

- [x] Update NCAIF structure and Phase 1 flagship products using interview gaps + use cases.
- [x] Draft/update the FGD2 plan (decision agenda) in the notes folder.

## Expected Outcome

- Refined data governance + data system implementation plan grounded in interview evidence.
- Updated NCAIF structure + use-case artifact.
- Draft FGD2 decision plan.
