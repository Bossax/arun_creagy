---
title: # Learning — Project Management Ecosystem Facade Discipline (CRDB)
tags: []
created: 2026-04-15
source: ψ/memory/learnings/2026-03-27_project-management-ecosystem-facade.md
---

# # Learning — Project Management Ecosystem Facade Discipline (CRDB)

# Learning — Project Management Ecosystem Facade Discipline (CRDB)

**Date**: 2026-03-27

## Context
While implementing the CRDB project-management ecosystem, I needed to choose between a powerful orchestrator and a controlled facade. We opted for Option B: a thin, low-agency facade sitting on top of explicit ledgers (Trigger Log, Deliverable Map, Claim Register, Submission Log, Change Log) and a modules spec (state sensing, trigger capture, deliverable trace).

## Pattern / Learning
- Canonical ledgers should index and point to existing artifacts (notes, evidence, decisions, submissions), not absorb them. They are navigation surfaces and contracts, not replacement storage.
- A project-manager facade is safest when it behaves like a transparent dispatcher: it reads ledgers, reports inferred state, lists which modules it calls or recommends, and proposes edits as explicit options. It never silently writes to core artifacts.
- The facade’s output should always include: inferred state, modules invoked/recommended, artifacts read, proposed artifact writes, and decisions left to the human. This structure enforces legibility and keeps human judgment in the loop.
- Running this kind of structural change on a dedicated test branch (e.g. `test/project-management-ecosystem`) gives room to evolve schemas and contracts without putting main at risk.

## When to Apply
Use this pattern whenever upgrading project management for a complex, evidence-heavy project:
- start by defining ledgers that index reality,
- then define modules that operate purely via those ledgers,
- only then add a controlled facade that surfaces state and options without hidden orchestration,
- and test everything on an isolated branch before merging.

## Tags
project-management, crdb, ledgers, facade, governance, retrospective, option-b

---
*Added via Oracle Learn*
