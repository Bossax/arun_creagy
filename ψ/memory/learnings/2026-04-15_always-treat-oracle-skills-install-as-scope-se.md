---
title: - Always treat `oracle-skills install` as scope-sensitive; running it from a rep
tags: []
created: 2026-04-15
source: ψ/memory/learnings/2026-03-25_local-skills-standup-recap-reset.md
---

# - Always treat `oracle-skills install` as scope-sensitive; running it from a rep

- Always treat `oracle-skills install` as scope-sensitive; running it from a repo root can populate `.roo/skills` inside the project.
- For this hybrid Windows/Git Bash/Bun environment, wrap `ls -t` with `bash -lc` to get deterministic “latest retrospective” ordering.
- Keep local skill overrides minimal: a small local `SKILL.md` that points to the local script is safer than duplicating upstream logic.

---
*Added via Oracle Learn*
