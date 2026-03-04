---
title: Oracle skills updates: preserve Windows/Git Bash fixes by treating `~/.roo/skill
tags: [oracle-skills, update, git, windows, git-bash, workflow]
created: 2026-03-04
source: rrr: Knowledge_System
---

# Oracle skills updates: preserve Windows/Git Bash fixes by treating `~/.roo/skill

Oracle skills updates: preserve Windows/Git Bash fixes by treating `~/.roo/skills` as a patch-carrying fork (`origin`) and `Soul-Brews-Studio/oracle-skills-cli` as `upstream`. For each upstream release tag, create `sync/<tag>` branch, merge `<tag>` with `--allow-unrelated-histories` (expected if histories started independently), push branch, review/merge via PR, then reinstall from your fork. Avoid `git push --force` to honor 'Nothing is Deleted'. Verify with `oracle-skills list -g | head -5`.

---
*Added via Oracle Learn*
