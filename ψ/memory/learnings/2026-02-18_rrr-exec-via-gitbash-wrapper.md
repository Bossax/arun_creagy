# Lesson Learned: Run /rrr bash steps via a Git Bash wrapper (Windows tool-runner mismatch)

**Date**: 2026-02-18  
**Category**: Workflow / Tooling  
**Tags**: #rrr #recap #gitbash #windows #cli

## Context

The repository is used interactively in VS Code with **Git Bash**.

However, the assistant tool-runner (`execute_command`) can route commands through a non-Git-Bash environment (observed as a WSL relay error when invoking `bash -lc`). This caused `/rrr` runs to silently skip the SKILL-required bash steps.

## Problem

The `/rrr` SKILL.md requires bash commands (gather + pulse update):

- `date "+%H:%M %Z (%A %d %B %Y)"`
- `git log --oneline -10 && git diff --stat HEAD~5`
- `bash tools/pulse.sh`

When the tool-runner cannot reliably execute `bash`, the agent drifts into “file-only RRR”, which violates the skill contract and prevents pulse data (streak, sessions) from updating.

## Solution

Add a repo-local wrapper that runs **Git for Windows bash.exe** explicitly:

- [`tools/gitbash.ts`](tools/gitbash.ts:1) — a Bun script that spawns:
  - `C:/Program Files/Git/usr/bin/bash.exe -lc "..."`

Then implement `/rrr` bash steps through the wrapper:

- [`tools/rrr_gather.sh`](tools/rrr_gather.sh:1) — gather + optional pulse context display
- Pulse update: run `bash tools/pulse.sh` via the wrapper

## Operational rule (RRR contract)

When `/rrr` is invoked in this repo, the assistant must:

1. Run gather commands using [`tools/gitbash.ts`](tools/gitbash.ts:1)
2. Write retrospective + learning files
3. Run `bash tools/pulse.sh` using [`tools/gitbash.ts`](tools/gitbash.ts:1)
4. Commit `psi/memory/retrospectives/` and `psi/memory/learnings/` (and pulse files if desired)

This preserves SKILL.md compliance while remaining robust to Windows tool-runner shell ambiguity.

