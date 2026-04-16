---
title: # Learning — Markdown Table Editing and Thaiwater PM Ledger Alignment
tags: []
created: 2026-04-15
source: ψ/memory/learnings/2026-04-09_markdown-table-edit-and-thaiwater-ledger-alignment.md
---

# # Learning — Markdown Table Editing and Thaiwater PM Ledger Alignment

# Learning — Markdown Table Editing and Thaiwater PM Ledger Alignment

**Date**: 2026-04-09  
**Project**: CRDB (DCCE)  
**Context**: Integrating Thaiwater data governance as an external benchmark and updating CRDB PM ledgers.

## What happened

- The Thaiwater data governance analysis note was completed and accepted as a canonical external benchmark for CRDB data standards and governance.
- The existing PM ledgers (Evidence Registry, Trigger Log) needed to be updated to reflect this benchmark without corrupting complex Markdown tables.
- Line-based patching (`apply_patch`) against large tables repeatedly failed due to minor representation differences and tool artefacts (e.g. phantom `| |` cells).
- A dedicated `markdown-table-edit` skill and a Bun-based replacement script were designed and implemented to enforce block-level, deterministic table editing.
- The Evidence Registry and Trigger Log were regenerated via block replacement, demoting the Phase 1 decision log to historical status and introducing new Thaiwater evidence (E-026–E-028) and trigger T-016.

## Key insight

For PM ledgers expressed as Markdown tables, **table editing is an architectural concern**, not a convenience detail. The system must treat tables as **block-level structures** with dedicated tooling (skills + scripts) rather than ad-hoc line diffs. At the same time, Evidence → Trigger → Change ordering must be respected so that new benchmarks are introduced first as evidence, then as triggers, and only then as formal changes when deliverables exist.

## Pattern

1. **Evidence-first:**
   - Register new benchmark artifacts and notes in the Evidence Registry as E-ids.
   - Demote historical decision logs to “historical / retired” when they are no longer the live stance.

2. **Trigger-after-evidence:**
   - Add a Trigger Log row (T-id) that ties the new E-ids to a specific impact zone and future deliverables.
   - Make it explicit when a trigger supersedes an older decision log as an active anchor.

3. **Change-after-trigger (only when design is real):**
   - Log a Change Log entry (CH-id) only once concrete D-* deliverables and design commitments exist.
   - Link CH-id to both the triggers and the new deliverables.

4. **Table editing via block replacement only:**
   - Never use `apply_patch` or line-level diffs on core PM tables.
   - Use a skill like `markdown-table-edit` that:
     - Checks for generators first.
     - Reads the table block under a heading anchor.
     - Builds the full new table in memory.
     - Replaces the block via full-file write or a deterministic script (`replace-md-table.ts`).

## Why it matters

This pattern protects both **data integrity** (no broken tables, no silent misalignment) and **conceptual integrity** (clear separation between evidence discovery, trigger recognition, and formal change). It prevents historical decision logs from quietly staying in power once a new benchmark is adopted, and it gives the PM facade a reliable way to propose and execute ledger updates without fighting fragile patch tools.

## Where to reuse

- Any project that uses Markdown table ledgers for triggers, changes, deliverables, or evidence (e.g. CRI, NFCS) should adopt the same `markdown-table-edit` + block replacement approach.
- Any time a new external benchmark or synthesis note emerges (like Thaiwater), follow Evidence → Trigger → Change ordering and avoid reusing old decision logs as live stance.


---
*Added via Oracle Learn*
