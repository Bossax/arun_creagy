---
title: Oracle skills updates: preserve Windows/Git Bash fixes via sync branch + PR (no force push)
tags: [oracle-skills, update, git, windows, git-bash, workflow]
created: 2026-03-04
---

# Oracle skills updates: preserve Windows/Git Bash fixes via sync branch + PR (no force push)

## Problem
Updating Oracle skills from upstream can overwrite local Windows/Git Bash adaptations that live in the installed skills directory (commonly `~/.roo/skills`). Direct reinstall is risky when the installed skills are also the patched source you run.

## Pattern (safe, repeatable)
Treat the installed skills directory as a **patch-carrying fork**:

- `origin` = your repo that mirrors what is installed (example: `Bossax/my-oracle-skills`)
- `upstream` = the mother-oracle source (example: `Soul-Brews-Studio/oracle-skills-cli`)

When a new upstream tag is released:

```bash
cd ~/.roo/skills

git fetch upstream --tags
git checkout -b sync/<tag>
git merge <tag> --allow-unrelated-histories
git push -u origin sync/<tag>
```

Then open a PR `sync/<tag> → master`, review that Windows/Git Bash fixes remain, merge, and reinstall skills from your fork.

## Why it works
- Preserves local patches (Nothing is Deleted)
- Avoids `git push --force`
- Makes upstream updates reviewable (PR diff)
- Handles first-time alignment with `--allow-unrelated-histories` (expected when histories started independently)

## Verification
After reinstall, verify with:

```bash
oracle-skills list -g | head -5
```


---
*Added via Oracle Learn*
