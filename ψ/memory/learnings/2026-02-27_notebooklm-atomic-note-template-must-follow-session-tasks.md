created: 2026-02-27
type: learning
tags:
  - notebooklm
  - literature-review
  - extraction
  - koi
---

# NotebookLM atomic-note templates and minimal skill scope

## Atomic-note template design

NotebookLM extraction works best when atomic-note format is designed backward from the next synthesis task.

When using NotebookLM to extract “atomic notes”, the note format should be **fixed and derived from the session plan’s subsequent tasks** (e.g., framework curation fields, data requirements, methods, use-of-results, and chronological context). If the format is left open-ended, extraction outputs become inconsistent and hard to recombine into comparative tables, timelines, and KO&I evidence indices.

In practice:

- Start from the target report sections (what you will write later).
- Define the atomic-note schema to directly populate those sections.
- Require citations/quotes for definitions and “applied to real cities” evidence.

## Skill scope

NotebookLM MCP skills should stay **narrowly scoped and deterministic**, while the broader research workflow lives in plans and workflow docs.

- **Skill responsibilities (do):**
  - Feed a user-authored prompt to a NotebookLM notebook.
  - Archive the response into atomic-note `.md` files in a predictable location, using the agreed template that is designed from the session’s next synthesis tasks.
- **Workflow responsibilities (do elsewhere):**
  - Translating research questions into AI research tool prompts.
  - Running external research tools and screening literature.
  - Selecting which sources to upload to NotebookLM and how they map into the atomic-note schema.

This separation keeps NotebookLM skills composable, reusable across session styles, and prevents scope creep into general “research orchestration”.

## Sources

- [`2026-02-26_notebooklm-extraction-works-best-when-atomic-note.md`](ψ/memory/learnings/2026-02-26_notebooklm-extraction-works-best-when-atomic-note.md)
- [`2026-03-02_notebooklm-skill-scope-separate-from-research-workflow.md`](ψ/memory/learnings/2026-03-02_notebooklm-skill-scope-separate-from-research-workflow.md)
- [`2026-03-02_keep-notebooklm-mcp-skills-narrowly-scoped-feed-p.md`](ψ/memory/learnings/2026-03-02_keep-notebooklm-mcp-skills-narrowly-scoped-feed-p.md)

---
*Added via Oracle Learn*
