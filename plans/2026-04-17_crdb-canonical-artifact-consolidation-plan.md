# CRDB canonical artifact consolidation plan

## Goal

Replace fragmented, overlapping, and misleading CRDB planning artifacts with a smaller canonical set that reflects integrated execution across CDM, NCAIF, data governance, MVD, and validation streams.

This plan assumes superseded artifacts will be moved into project archive locations under [`ψ/incubate/DCCE/CRDB/archive/`](ψ/incubate/DCCE/CRDB/archive/).

## Problem statement

The current active set mixes at least three different concerns in overlapping ways:

- navigation/orientation via [`ψ/incubate/DCCE/CRDB/output/CRDB-Workstreams-Index.md`](ψ/incubate/DCCE/CRDB/output/CRDB-Workstreams-Index.md)
- execution sequencing via [`ψ/incubate/DCCE/CRDB/output/2026-04-08_CRDB-Stakeholder-Engagement-Plan.md`](ψ/incubate/DCCE/CRDB/output/2026-04-08_CRDB-Stakeholder-Engagement-Plan.md)
- track-specific architecture and governance anchors such as [`ψ/incubate/DCCE/CRDB/output/National Climate Adaptation Information Framework.md`](ψ/incubate/DCCE/CRDB/output/National%20Climate%20Adaptation%20Information%20Framework.md), [`ψ/incubate/DCCE/CRDB/output/Conceptual Data Model for climate risk and adaptation data system.md`](ψ/incubate/DCCE/CRDB/output/Conceptual%20Data%20Model%20for%20climate%20risk%20and%20adaptation%20data%20system.md), and [`ψ/incubate/DCCE/CRDB/output/2026-03-05-Feature-Driven Data Governance Strategy v3.md`](ψ/incubate/DCCE/CRDB/output/2026-03-05-Feature-Driven%20Data%20Governance%20Strategy%20v3.md)

The result is that the label “stakeholder engagement” now understates the real scope of the execution spine, while “workstreams” still reflects an older fragmentation model.

## Planning principles

1. Keep one canonical artifact per planning function.
2. Separate execution control from domain architecture.
3. Make validation and engagement one track inside integrated execution, not the umbrella frame.
4. Preserve history by moving superseded files to archive rather than deleting them.
5. Update PM ledgers so the new canon becomes traceable from trigger to deliverable.

## Proposed canonical artifact set

### A. Core execution artifact

Create one new top-level execution artifact:

- [`ψ/incubate/DCCE/CRDB/output/2026-04-17_CRDB-Integrated-Execution-Plan.md`](ψ/incubate/DCCE/CRDB/output/2026-04-17_CRDB-Integrated-Execution-Plan.md)

Purpose:

- replace the misleading frame in [`ψ/incubate/DCCE/CRDB/output/2026-04-08_CRDB-Stakeholder-Engagement-Plan.md`](ψ/incubate/DCCE/CRDB/output/2026-04-08_CRDB-Stakeholder-Engagement-Plan.md)
- define the integrated execution spine across:
  - CDM operationalization
  - NCAIF service and content architecture
  - data governance and publishing rails
  - MVD and Loss and Damage operationalization
  - validation streams such as IT discussion, workshop, and FGD3

Recommended sections:

1. why the old framing is insufficient
2. integrated execution tracks
3. priority stack
4. decisions already locked
5. unresolved decisions
6. stream-by-stream validation role
7. outputs required before IT meeting, workshop, and FGD3
8. done criteria

### B. Canonical navigation artifact

Replace the current workstream index with a navigation artifact that matches the new integrated model:

- [`ψ/incubate/DCCE/CRDB/output/CRDB-Execution-Architecture-Index.md`](ψ/incubate/DCCE/CRDB/output/CRDB-Execution-Architecture-Index.md)

Purpose:

- supersede [`ψ/incubate/DCCE/CRDB/output/CRDB-Workstreams-Index.md`](ψ/incubate/DCCE/CRDB/output/CRDB-Workstreams-Index.md)
- index the canonical artifact family by function instead of by older stream labels

Recommended sections:

1. execution control artifacts
2. architecture anchors
3. governance and data standards anchors
4. MVD and Loss and Damage anchors
5. validation and workshop artifacts
6. evidence and PM ledgers

### C. Domain consolidation artifacts

Create a small set of new synthesis artifacts where current material is fragmented:

1. [`ψ/incubate/DCCE/CRDB/output/2026-04-17_CRDB-CDM-Operationalization-Plan.md`](ψ/incubate/DCCE/CRDB/output/2026-04-17_CRDB-CDM-Operationalization-Plan.md)
   - translates the CDM into priority subject areas, boundary choices, ownership questions, and implementation use in NCAIF and MVD

2. [`ψ/incubate/DCCE/CRDB/output/2026-04-17_CRDB-NCAIF-Service-Architecture-Plan.md`](ψ/incubate/DCCE/CRDB/output/2026-04-17_CRDB-NCAIF-Service-Architecture-Plan.md)
   - consolidates workflow patterns, page/service structure, content tiers, and service-bundle logic

3. [`ψ/incubate/DCCE/CRDB/output/2026-04-17_CRDB-Governance-and-Data-Standards-Plan.md`](ψ/incubate/DCCE/CRDB/output/2026-04-17_CRDB-Governance-and-Data-Standards-Plan.md)
   - consolidates rails, gates, QC logic, reference standards, role mapping, and Thaiwater-derived implications

4. [`ψ/incubate/DCCE/CRDB/output/2026-04-17_CRDB-MVD-and-Loss-Damage-Operational-Plan.md`](ψ/incubate/DCCE/CRDB/output/2026-04-17_CRDB-MVD-and-Loss-Damage-Operational-Plan.md)
   - isolates the MVD thread so it stops disappearing inside broader stakeholder or governance notes

These should be synthesis-and-direction artifacts, not repetitions of raw evidence notes.

## Proposed supersession map

### Direct supersession

1. Supersede [`ψ/incubate/DCCE/CRDB/output/2026-04-08_CRDB-Stakeholder-Engagement-Plan.md`](ψ/incubate/DCCE/CRDB/output/2026-04-08_CRDB-Stakeholder-Engagement-Plan.md)
   - replacement: [`ψ/incubate/DCCE/CRDB/output/2026-04-17_CRDB-Integrated-Execution-Plan.md`](ψ/incubate/DCCE/CRDB/output/2026-04-17_CRDB-Integrated-Execution-Plan.md)
   - archive destination: [`ψ/incubate/DCCE/CRDB/archive/2026-04-08_CRDB-Stakeholder-Engagement-Plan.md`](ψ/incubate/DCCE/CRDB/archive/2026-04-08_CRDB-Stakeholder-Engagement-Plan.md)

2. Supersede [`ψ/incubate/DCCE/CRDB/output/CRDB-Workstreams-Index.md`](ψ/incubate/DCCE/CRDB/output/CRDB-Workstreams-Index.md)
   - replacement: [`ψ/incubate/DCCE/CRDB/output/CRDB-Execution-Architecture-Index.md`](ψ/incubate/DCCE/CRDB/output/CRDB-Execution-Architecture-Index.md)
   - archive destination: [`ψ/incubate/DCCE/CRDB/archive/CRDB-Workstreams-Index.md`](ψ/incubate/DCCE/CRDB/archive/CRDB-Workstreams-Index.md)

### Partial absorption into new domain artifacts

The following stay as evidence or prior anchors, but their planning role is reduced because new syntheses will absorb their forward-looking sections:

- [`ψ/incubate/DCCE/CRDB/output/2026-03-05-Feature-Driven Data Governance Strategy v3.md`](ψ/incubate/DCCE/CRDB/output/2026-03-05-Feature-Driven%20Data%20Governance%20Strategy%20v3.md)
- [`ψ/incubate/DCCE/CRDB/output/NCAIF — Workflow patterns + MVP v3.md`](ψ/incubate/DCCE/CRDB/output/NCAIF%20%E2%80%94%20Workflow%20patterns%20%2B%20MVP%20v3.md)
- [`ψ/incubate/DCCE/CRDB/output/2026-04-08_CRDB-Thaiwater-Enhancement-Concept-Note.md`](ψ/incubate/DCCE/CRDB/output/2026-04-08_CRDB-Thaiwater-Enhancement-Concept-Note.md)
- [`ψ/incubate/DCCE/CRDB/inbox_note/2026-04-09-enhancement-plan-based-on-Thaiwater-data-architecture.md`](ψ/incubate/DCCE/CRDB/inbox_note/2026-04-09-enhancement-plan-based-on-Thaiwater-data-architecture.md)

These should not necessarily be archived immediately. Instead, the new canonical artifacts should cite them as source anchors and later mark them as absorbed or historical if the user wants a second cleanup pass.

## Naming conventions

### New canonical planning artifacts

Use this pattern:

- `YYYY-MM-DD_CRDB_<Function>-Plan.md` for dated execution syntheses
- `CRDB-<Function>-Index.md` for durable navigation artifacts

Preferred terms:

- use `Integrated-Execution`
- use `Execution-Architecture`
- use `Operationalization`
- use `Governance-and-Data-Standards`
- use `MVD-and-Loss-Damage`

Avoid these in new canonical names when they are too narrow or misleading:

- `Stakeholder-Engagement`
- `Workstreams`
- `brainstorming`

## Archive move rules

1. Move only files that are clearly replaced by a new canonical artifact.
2. Keep filenames unchanged when moving to archive so references remain intelligible.
3. Add a short supersession note at the top of each archived file if content editing is part of implementation.
4. Add a short “supersedes” and “superseded by” note in each new canonical artifact.
5. Do not archive raw evidence anchors that still serve as evidence inputs.

## Required ledger and navigation updates

### Deliverable map

Update [`ψ/incubate/DCCE/CRDB/CRDB-Deliverable-Map.md`](ψ/incubate/DCCE/CRDB/CRDB-Deliverable-Map.md) to:

- add new D-rows for the new canonical artifacts
- mark D-019 and D-020 as superseded or partially superseded once replacements exist
- add archive references for moved files

### Trigger log

Update [`ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md) to:

- add a new trigger for reframing execution from stakeholder-only to integrated execution
- connect this trigger to T-015 and T-016 as downstream refinement

### Evidence registry

Update [`ψ/incubate/DCCE/CRDB/CRDB-Evidence-Registry.md`](ψ/incubate/DCCE/CRDB/CRDB-Evidence-Registry.md) to:

- register the new consolidated planning artifacts as active synthesis artifacts if they become evidence-bearing
- preserve older files as prior anchors or source notes rather than active planning surfaces

### Navigation index

Update or replace [`ψ/incubate/DCCE/CRDB/output/CRDB-Workstreams-Index.md`](ψ/incubate/DCCE/CRDB/output/CRDB-Workstreams-Index.md) so the entry point reflects integrated execution, not obsolete stream names.

## Implementation sequence

1. Draft the new canonical execution artifact first.
2. Draft the new navigation index second.
3. Draft the four domain synthesis artifacts.
4. Move directly superseded files into archive.
5. Update deliverable, trigger, and evidence ledgers.
6. Do one link-integrity pass across all new and archived references.

## Suggested scope boundary for the first implementation pass

### In scope

- creating the new canonical artifact family
- moving clearly superseded planning files to archive
- updating core ledgers and index/navigation files

### Out of scope for the same pass

- rewriting all historic strategy notes
- cleaning every older chapter-writing artifact
- de-duplicating all interim-report support material

## Review questions for approval

1. Is the proposed canonical set too large, or is the four-domain split acceptable?
2. Should the MVD and Loss and Damage plan remain separate, or be merged into the governance and data standards plan?
3. Should older planning anchors such as [`ψ/incubate/DCCE/CRDB/output/2026-03-05-Feature-Driven Data Governance Strategy v3.md`](ψ/incubate/DCCE/CRDB/output/2026-03-05-Feature-Driven%20Data%20Governance%20Strategy%20v3.md) stay active as anchors, or be archived in a later cleanup phase?
