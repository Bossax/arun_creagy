---
query: Thai report writing task in memory; redesign writing-th skill to align with Oracle way
target: Arun_Creagy
mode: smart
timestamp: 2026-03-28 11:57 GMT+7
---

# Trace: Thai report writing task; redesign writing-th to align with Oracle way

**Target**: Arun_Creagy
**Mode**: smart (Oracle first, then repo search)
**Time**: 2026-03-28 11:57 GMT+7

## Oracle Results
- None returned.
  - Note: Oracle MCP vector search unavailable; query ran in FTS-only mode.

## Files Found

### Current spec / candidate sources
- Draft skill spec in inbox (appears to be the working spec to migrate into a project-local skill):
	- [`ψ/inbox/writing-th.md`](ψ/inbox/writing-th.md)

- Learning-only companion skill already present as project-local skill:
	- [`​.roo/skills/writing-th-learn/SKILL.md`](.roo/skills/writing-th-learn/SKILL.md)

- Archived older skill spec (useful as history; do not delete):
	- [`ψ/archive/writing-th SKILL.md`](ψ/archive/writing-th%20SKILL.md)

### Architecture decisions + retrospectives that define “Oracle way”

- MCP-first architecture correction for writing skill design:
  - [`ψ/memory/retrospectives/2026-03/11/15.18_writing_th-skill-architecture.md`](ψ/memory/retrospectives/2026-03/11/15.18_writing_th-skill-architecture.md)

- Writing-th learn-back split (drafting vs learning) and intended `/rrr` integration pattern:
  - [`ψ/memory/retrospectives/2026-03/24/09.36_writing-th-learn-crdb-edit-session.md`](ψ/memory/retrospectives/2026-03/24/09.36_writing-th-learn-crdb-edit-session.md)

### Stable resonance constraints (should remain the canonical long-lived “voice”)

- Thai writing style guidance:
  - [`ψ/memory/resonance/writing-style-th.md`](ψ/memory/resonance/writing-style-th.md)

- Thai citation style guidance:
  - [`ψ/memory/resonance/citation-style-th.md`](ψ/memory/resonance/citation-style-th.md)

### Related plans / handoffs that motivated the workflow

- Example of “Thai report style” usage context in a plan:
  - [`plans/2026-03-23-forward-cce-interview-prep-and-progress-report-plan.md`](plans/2026-03-23-forward-cce-interview-prep-and-progress-report-plan.md)

## Git History

- Not searched in this trace run.

## GitHub Issues/PRs

- Not searched in this trace run.

## Cross-Repo Matches

- Not searched in this trace run.

## Oracle Memory

- Located relevant retrospectives and resonance notes inside this workspace under `ψ/`.

## Summary

Key alignment requirements inferred from files above:

1) **MCP-first retrieval is mandatory**
   - The writing skill must retrieve resonance + learnings via MCP tool calls (not via HTTP APIs, and not from a runner script).
   - Runner scripts (if any) must be formatting-only.

2) **Outline-first is a control boundary**
   - The skill should stop after producing an outline and wait for explicit user confirmation before drafting.

3) **Separate drafting vs learning (do not collapse into one skill)**
   - `/writing-th` should focus on planning + outlining + drafting.
   - `/writing-th-learn` should do the draft-vs-edited comparison and persist learnings.
   - `/rrr` integration should trigger `/writing-th-learn` rather than duplicating its logic.

4) **Resonance vs learnings separation**
   - Stable constraints live in resonance files.
   - Session-specific patterns and improvements live in learnings and are discoverable by search.

Primary deliverable for the redesign work:

- Add a project-local skill at [`​.roo/skills/writing-th/SKILL.md`](.roo/skills/writing-th/SKILL.md) that codifies the MCP handshake, outline stop, and calls out integration with [`​.roo/skills/writing-th-learn/SKILL.md`](.roo/skills/writing-th-learn/SKILL.md).

