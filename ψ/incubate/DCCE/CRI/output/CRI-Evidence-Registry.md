---
type: registry
status: draft
project:
  - DCCE_CRI
title: CRI Evidence Registry
description: Central register of evidence artifacts backing CRI Phase 1 and Phase 2 methodology and decisions
---

# CRI Evidence Registry

This registry records the **evidence backbone for the Climate Risk Index (CRI)** project. It follows the evidence registry pattern established in the CRDB project, but is scoped specifically to **DCCE / CRI** under `ψ/incubate/DCCE/CRI/`.

Each row links a concrete artifact (source, note, synthesis, or output) to its role in CRI Phase 1 and Phase 2 design and implementation. Over time, this table should become the **single authoritative map** of which evidence backs which methodology sections, design decisions, and implementation choices.

## Table

| id        | title                                                      | path                                                                                       | type         | phase   | status   | dimensions                                      | notes |
| --------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------ | ------- | -------- | ----------------------------------------------- | ----- |
| E-CRI-001 | CRI Phase 1 Methodology                                    | ψ/incubate/DCCE/CRI/output/CRI Phase 1 Methodology.md                                      | output       | Phase 1 | current  | impact; data_richness; fiscal_relief            | Anchor for Impact Index / Fiscal Relief framing and hybrid data model. |
| E-CRI-002 | Climate Risk Index (CRI) Pilot Methodology                 | ψ/incubate/DCCE/CRI/inbox_source/Climate Risk Index (CRI) Pilot Methodology.md            | source       | Phase 1 | current  | impact; methodology; historical_baseline        | Pilot methodology reference for Phase 1 evolution and gap analysis. |
| E-CRI-003 | CRI – Resilience Measurement & Indicator Design (Synthesis) | ψ/incubate/DCCE/CRI/output/CRI_resilience_measurement_synthesis.md                        | AI_synthesis | Phase 2 | current  | capacity; SES; governance; data_richness        | Synthesizes evidence for Phase 2 capacity profiling and indicator design. |

> [!note]
> - **id** should be a stable identifier (`E-CRI-###`) used in methodology notes, the coverage map, and decision logs.
> - **path** is always recorded relative to the repo root (`c:/Users/sitth/OracleWorkspace/Arun_Creagy`).
> - **type** distinguishes raw sources, internal notes, curated outputs, and AI-assisted syntheses.
> - **dimensions** should reference CRI-relevant concepts such as `impact`, `capacity`, `data_richness`, `SES`, `governance`, etc.

