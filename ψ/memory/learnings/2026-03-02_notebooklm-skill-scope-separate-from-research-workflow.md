created: 2026-03-02
type: learning
status: superseded
superseded_by: 2026-02-27_notebooklm-atomic-note-template-must-follow-session-tasks.md
tags:
  - notebooklm
  - skills
  - workflow
  - scope
---

> This learning has been superseded by [`2026-02-27_notebooklm-atomic-note-template-must-follow-session-tasks.md`](ψ/memory/learnings/2026-02-27_notebooklm-atomic-note-template-must-follow-session-tasks.md); kept for detailed discussion of NotebookLM skill vs workflow responsibilities.

# Keep NotebookLM skill scope minimal; keep research workflow in workflow docs / session plan

When integrating NotebookLM MCP into a Roo skill, keep the skill narrowly scoped and deterministic:

- **Skill responsibilities (do):**
  - Feed a user-authored prompt to a NotebookLM notebook.
  - Archive the response into atomic note `.md` files in a predictable location.

- **Workflow responsibilities (do elsewhere):**
  - Translating research questions into AI research tool prompts.
  - Running external research tools and screening literature.
  - Selecting which sources to upload to NotebookLM.

This separation prevents scope creep, keeps skills composable, and preserves flexibility across different session styles.

References: [`../../.roo/skills/notebookLM-research/SKILL.md`](../../.roo/skills/notebookLM-research/SKILL.md:1), [`src/00_Meta/00_WORKFLOW.md`](src/00_Meta/00_WORKFLOW.md:1)

---
*Added via /rrr*


---
*Added via Oracle Learn*
