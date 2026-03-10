---
created: 2026-03-04
project:
tags:
  - oracle
status: To-do
type: "plan "
---
# Session Plan: Oracle skills fork sync
## Context
- Current upstream tag: v2.0.7
- Local skills repo: `~/.roo/skills`
- Origin (your fork/snapshot): https://github.com/Bossax/my-oracle-skills
- Upstream (mother-oracle): https://github.com/Soul-Brews-Studio/oracle-skills-cli
- Sync branch already pushed: `sync/v2.0.7`
- PR link: https://github.com/Bossax/my-oracle-skills/pull/new/sync/v2.0.7

## Goal
Preserve Windows/Git Bash customizations while syncing to upstream v2.0.7, then reinstall skills from your fork.

## Step 1 — Open PR (GitHub)
1) Open the PR link above.
2) Review the diff for Windows/Git Bash fixes and ensure they remain.
3) Merge the PR into `master`.

## Step 2 — Update local master from origin
```bash
cd ~/.roo/skills
git checkout master
git pull origin master
```

## Step 3 — Install skills from your fork
### Option A (after PR merge, install from master)
```bash
~/.bun/bin/bunx --bun oracle-skills@github:Bossax/my-oracle-skills#master install -g -y
```

### Option B (install directly from sync branch before merge)
```bash
~/.bun/bin/bunx --bun oracle-skills@github:Bossax/my-oracle-skills#sync/v2.0.7 install -g -y
```

## Step 4 — Verify
```bash
oracle-skills list -g | head -5
```

## Notes
- This keeps your local Windows/Git Bash fixes in your fork and makes upstream updates reviewable.
- If future upstream tags add conflicts, resolve them in a new `sync/<tag>` branch and repeat the PR flow.
