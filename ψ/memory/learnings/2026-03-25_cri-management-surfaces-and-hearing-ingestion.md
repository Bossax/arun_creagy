# Learning — CRI management surfaces & hearing ingestion

**Date**: 2026-03-25

## Context

During this session, I aligned the CRI project structure with the CRDB pattern (Hub + plan + evidence registry + coverage map) and ingested the CRI Phase 2 Public Hearing 1 into a small set of typed artifacts (cleaned transcripts, summary note, decisions/signals, methodology implications, implementation/governance signals). I also retired older management surfaces (Implementation Plan, Working Status Brief, AI sources index) by marking them as archived and pointing to the live plan + Hub + evidence system.

## What I learned

1. **One evidence spine beats many dashboards.** Once a project has a proper evidence registry and coverage map, older management surfaces (implementation plans, AI source indices, working briefs) should be treated as historical evidence, not parallel control layers. The Hub + plan + methodologies + registry + coverage map form a coherent spine; everything else should either feed into that spine or be explicitly archived with `superseded_by` pointers.

2. **Consultations need a canonical artifact set.** For hearings and workshops, the minimum viable evidence pack is: (a) cleaned transcripts as source, (b) one summary note, and (c) a few curated interpretation notes (decisions/signals, methodology implications, implementation/governance signals). When these are registered in the evidence registry and referenced from the plan and methods, the event becomes part of the knowledge base instead of a one-off meeting.

3. **AI-output indices are scaffolding, not destinations.** Early in a project it is natural to build a bespoke “AI sources index” to keep track of synthetic notes. Once an evidence registry exists, that index should be folded into it and the index file archived. This keeps the number of “where is the truth?” surfaces small while preserving the index as a trace of how AI was used.

## How to apply this next time

- When extending CRI or starting a new project, treat the evidence registry and coverage map as the only authoritative lists of evidence; use Hub and plan to point at them, and avoid spinning up new parallel dashboards unless there is a clear, time-bounded reason.
- For every major consultation or public hearing, immediately generate the canonical artifact set (transcripts, summary, decisions/signals, implications notes) and register them with E-IDs in the evidence registry, instead of letting meeting notes live as loose inbox items.
- When using AI to produce research syntheses, plan from the beginning that those syntheses will be moved into the evidence registry and thematic notes, and that any intermediate “AI index” documents will be archived rather than kept as live management surfaces.

## Tags

- project_hygiene
- evidence_registry
- consultation_ingestion
- management_surfaces
- cri

