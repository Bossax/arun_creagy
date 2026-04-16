---
title: ---
tags: [oracle-db, notebooklm, atomic-notes, skill-scope, research-workflow, templates]
created: 2026-04-15
source: ψ/memory/learnings/2026-04-11_oracle-db-backfill-group3-notebooklm-atomic-templates-scope.md
---

# ---

---
title: Oracle DB backfill — Group 3 NotebookLM atomic-note templates & narrow skill scope
created: 2026-04-11
type: learning
concepts:
  - oracle-db
  - notebooklm
  - atomic-notes
  - skill-scope
  - research-workflow
  - templates
source: rrr: Arun_Creagy
---

# Oracle DB backfill — Group 3 NotebookLM atomic-note templates & narrow skill scope

## Scope

This canonical learning represents **Group 3 – NotebookLM atomic-note templates & narrow skill scope** from the indexing map in [`plans/2026-04-09-learnings-indexing-map.md`](plans/2026-04-09-learnings-indexing-map.md).

It captures the design rule that **NotebookLM atomic-note templates must be designed backwards from downstream tasks**, and that NotebookLM MCP skills should remain *narrowly scoped* (prompt feeding + archiving) while the actual research workflow logic lives in plans and local tooling.

## Source artefacts

Group 3 member files (from the indexing map):

- [`ψ/memory/learnings/2026-02-26_notebooklm-extraction-works-best-when-atomic-note.md`](ψ/memory/learnings/2026-02-26_notebooklm-extraction-works-best-when-atomic-note.md)
- [`ψ/memory/learnings/2026-02-27_notebooklm-atomic-note-template-must-follow-session-tasks.md`](ψ/memory/learnings/2026-02-27_notebooklm-atomic-note-template-must-follow-session-tasks.md) **(proposed primary)**
- [`ψ/memory/learnings/2026-03-02_notebooklm-skill-scope-separate-from-research-workflow.md`](ψ/memory/learnings/2026-03-02_notebooklm-skill-scope-separate-from-research-workflow.md)
- [`ψ/memory/learnings/2026-03-02_keep-notebooklm-mcp-skills-narrowly-scoped-feed-p.md`](ψ/memory/learnings/2026-03-02_keep-notebooklm-mcp-skills-narrowly-scoped-feed-p.md)

The proposed primary provides the clearest articulation of the template design rule; the other notes contribute detail on skill scope and why to keep NotebookLM roles narrow.

## Stable patterns

- Design atomic‑note templates **backwards from downstream outputs** (reports, databases, tagging schemes), not forwards from arbitrary headings.
- Each atomic note should map to a small, well‑defined task or concept, so that extraction results are reusable across projects.
- NotebookLM MCP skills should:
  - Focus on feeding prompts, managing sources, and archiving outputs.
  - Avoid embedding full research‑workflow logic (planning, decision trees, multi‑step orchestration).
- Research workflows (branching, prioritisation, project‑specific constraints) should live in local plans and tools under [`plans`](plans) and `ψ/incubate`, not inside NotebookLM skills.
- When the scope of a NotebookLM skill drifts wider than “prompt feeding + archiving”, split it into smaller, narrower skills.

## One-off decisions

- Template examples are allowed to reference CRI/CRDB projects, but the canonical pattern is **cross‑project** and should be worded generically.
- Atomic notes are preferred over large, multi‑topic synthesis notes when the goal is to populate Oracle DB or other knowledge systems.
- This canonical is dated 2026‑04‑11 to line up with the backfill wave even though the underlying experiments span February–March.

## Open questions

- How granular should atomic notes become before the overhead of managing them outweighs the benefits of reuse?
- What is the best way to represent NotebookLM atomic‑note templates inside Oracle DB (for example, as patterns, templates, or both)?
- Should there be a dedicated registry of approved atomic‑note templates for common research patterns?

## Relationship to Oracle DB backfill

- Oracle DB should contain **one canonical learning** for this group, tied to this file, rather than separate records for each early experiment.
- Earlier notes stay in the markdown corpus as provenance but can be marked as superseded once this canonical is backfilled.
- Oracle DB backfill should:
  - Create or confirm a `learning` entry for this canonical file.
  - Tag it with concepts: `oracle-db`, `notebooklm`, `atomic-notes`, `skill-scope`, `research-workflow`, `templates`.
  - Record the Oracle ID in [`ψ/memory/logs/info/backfill-index.md`](ψ/memory/logs/info/backfill-index.md) under *Group 3 canonical backfill*.


---
*Added via Oracle Learn*
