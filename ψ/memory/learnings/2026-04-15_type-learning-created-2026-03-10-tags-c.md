---
title: ---
tags: []
created: 2026-04-15
source: ψ/memory/learnings/2026-03-10_command-execution-reliability-hybrid-shell.md
---

# ---

---
type: learning
created: 2026-03-10
tags:
  - command-execution
  - reliability
  - windows
  - git-bash
  - automation
---

# Command execution reliability in a hybrid shell environment

## Problem
Complex inline shell commands (heredocs, quoting, loops, pipes) become fragile when:
- shells differ (`cmd.exe` vs Git Bash vs WSL)
- paths contain Unicode (`ψ/`)
- output truncation hides partial failures

## Failure modes observed
- **Shell mismatch**: commands that assume Bash executed under a different shell.
- **Heredoc/quoting breakage**: multi-line strings interpreted incorrectly.
- **Silent partial execution**: a move step fails, next steps proceed.

## Fix pattern
Prefer small, rerunnable scripts over one-liners.

Examples in this repo:
- [`tools/migrate_active_to_inbox.py`](tools/migrate_active_to_inbox.py:1)
- [`tools/migrate_writing_notes_to_inbox.py`](tools/migrate_writing_notes_to_inbox.py:1)
- [`tools/migrate_writing_output_to_incubate.py`](tools/migrate_writing_output_to_incubate.py:1)

## Verification checklist (do after every step)
1) Count source + destination files.
2) Spot-check 3–5 moved items.
3) If assets/links involved, open one representative markdown file and confirm embeds still resolve.

---
*Added via Oracle Learn*
