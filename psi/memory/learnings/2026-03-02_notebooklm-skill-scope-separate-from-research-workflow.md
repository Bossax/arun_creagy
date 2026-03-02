---
created: 2026-03-02
type: learning
tags:
  - notebooklm
  - skills
  - workflow
  - scope
---

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

