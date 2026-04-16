---
title: # Learning — MVPs: pattern composition + functional orthogonality
tags: []
created: 2026-04-15
source: ψ/memory/learnings/2026-03-04_mvp-orthogonality-pattern-composition.md
---

# # Learning — MVPs: pattern composition + functional orthogonality

# Learning — MVPs: pattern composition + functional orthogonality

**Date**: 2026-03-04
**Context**: Distilling NCAIF stakeholder use cases into workflow patterns and MVP candidates for FGD2 alignment.

## Pattern

1) A single **MVP can serve multiple workflow patterns**.

2) To prevent scope creep, each MVP should still have:

- **One primary pattern** it is optimized for.
- **Secondary pattern support** via reuse/composition (consuming shared primitives), not by adding bespoke branches.

3) MVP set design should aim for **functional orthogonality**:

- Each MVP owns a distinct capability boundary (e.g., packaging/exports vs event-impact schema vs baseline endorsement vs uncertainty standard).
- Shared governance rules (e.g., limitations/uncertainty statements) should be defined once (as a standard) and referenced/consumed elsewhere, rather than duplicated.

## Why it matters

- Keeps the Phase 1 product shortlist small and coherent.
- Reduces redundancy and future refactoring.
- Makes it easier to communicate tradeoffs in workshops: “this MVP enables these patterns” without implying “it does everything.”

## Example (NCAIF)

- “Event + Impact schema + post-event reporting” is appropriately **single-pattern-primary** (post-event assessment), while its outputs can still be embedded downstream in briefing packs.

## Where used

- Workflow/MVP artifact: [`src/01_Projects/2025-11_DCCE-CRDB/output/NCAIF — Workflow patterns + MVP draft (from stakeholder use cases).md`](src/01_Projects/2025-11_DCCE-CRDB/output/NCAIF%20%E2%80%94%20Workflow%20patterns%20%2B%20MVP%20draft%20(from%20stakeholder%20use%20cases).md:1)

---
*Added via Oracle Learn*
