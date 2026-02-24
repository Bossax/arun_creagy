# Lesson Learned: Stable /recap and /rrr behavior on Windows with Git Bash

**Date**: 2026-02-18  
**Source**: rrr: recap-rrr-workflow-session  
**Tags**: #rrr #recap #gitbash #pulse #windows

## Context

This session wrapped up a multi-session effort to repair recap and `/rrr` behavior in the `Knowledge_System` repo. The environment is Windows 11 with VS Code using Git Bash as the interactive shell, while the assistant’s tool-runner may route commands differently (including through a WSL relay). Earlier sessions revealed problems with pulse streaks staying at 0, last-session dates appearing stale, and `/rrr` silently skipping SKILL-defined shell commands.

## Key Learnings

1. **Derive pulse from retrospectives, not from script invocations.**  
   - [`tools/pulse.sh`](tools/pulse.sh:1) now scans `psi/memory/retrospectives/` to count sessions, determine the first and latest session timestamps, and compute streaks as consecutive days with retrospectives.
   - This immediately fixed `streak.days` and `totalSessions`, making them trustworthy inputs for `/rrr` narratives.

2. **Encapsulate Git Bash execution in a dedicated wrapper.**  
   - [`tools/gitbash.ts`](tools/gitbash.ts:1) launches the confirmed Git-for-Windows `bash.exe` and runs arbitrary bash commands via `-lc`.
   - `/rrr` gather steps (`date`, `git log`, `git diff`, pulse inspection) and `bash tools/pulse.sh` can now be executed through this wrapper without path mangling or WSL errors.

3. **Recap must clearly distinguish retrospectives from handoffs.**  
   - Recap now treats the latest retrospective as the authoritative indicator of “last session” and displays the latest handoff in a separate, clearly labeled section.
   - This avoids the earlier confusion where an older handoff date appeared to contradict evidence of more recent work.

## Application

For future `/recap` and `/rrr` runs in this repository:

- Use [`tools/gitbash.ts`](tools/gitbash.ts:1) as the standard entry point whenever SKILL.md specifies bash commands.
- Expect pulse metrics to be accurate snapshots of actual retrospectives, and use them confidently in summaries (e.g., “Session #N of M (K-day streak)”).
- Treat handoff files as optional guidance, not as the canonical record of the last session.

