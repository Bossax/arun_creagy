# RRR utilities fix – recap of changes

> STATUS: Partially superseded
>
> For the **current, canonical behavior** of recap and `/rrr` in this repo, prefer:
> - [`2026-02-18_rrr-exec-via-gitbash-wrapper.md`](psi/memory/learnings/2026-02-18_rrr-exec-via-gitbash-wrapper.md:1)
> - [`2026-02-18_rrr-recap-rrr-session-wrap-up.md`](psi/memory/learnings/2026-02-18_rrr-recap-rrr-session-wrap-up.md:1)
>
> This note remains as historical context for an earlier iteration of the workflow.

## Context

This learning note is paired with the retrospective:

- [`11.38_rrr-recap-rrr-workflow-fix.md`](psi/memory/retrospectives/2026-02/18/11.38_rrr-recap-rrr-workflow-fix.md:1)

In that session, the goal was to bring the `/rrr` workflow back into alignment with its SKILL.MD by:

- Ensuring the pulse utility maintains the JSON schema expected by `/rrr` in `psi/data/pulse/project.json` and `psi/data/pulse/heartbeat.json`.
- Tracking per-branch session counts so `/rrr` summaries can talk about branch-level activity.
- Encoding the Git Bash environment and recap/RRR discipline in project-local memory.

## Key changes

1. **Pulse schema alignment**
   - [`pulse.sh`](tools/pulse.sh:1) now guarantees that `project.json` contains:
     - `projectName`
     - `createdAt`
     - `updatedAt`
     - `totalSessions`
     - `avgMessagesPerSession`
     - `sizes`
     - `branches`
   - `createdAt` is set on first run, and `updatedAt` is updated on each pulse run using the latest session timestamp.
   - `totalSessions` increments only when the latest session timestamp changes, preventing double-counting.

2. **Branch-level tracking**
   - A small helper in [`pulse.sh`](tools/pulse.sh:38) uses `git rev-parse --abbrev-ref HEAD` to detect the current branch (best-effort; falls back to `"unknown"`).
   - On each run, `branches[<branch>]` is incremented, so `/rrr` can surface how many sessions have been associated with each branch.

3. **Environment and discipline encoded in memory**
   - The fact that this workspace uses **Git Bash in VS Code** is now written explicitly into:
     - [`2026-02-18_shell-and-recap-discipline.md`](psi/memory/learnings/2026-02-18_shell-and-recap-discipline.md:1)
   - That file also records the rule that repeating failing command patterns more than twice is not acceptable; future sessions must stop, explain, and switch strategy.

## Lessons learned

1. **RRR tooling is part of the contract.**
   - The `/rrr` SKILL.MD defines expectations around pulse data; utilities like [`pulse.sh`](tools/pulse.sh:1) must be treated as part of that contract and kept in sync.

2. **Environment facts belong in memory files.**
   - The shell environment (Git Bash here) and behavioral guardrails (e.g. "no repeated failing commands") must be written into `psi/memory/learnings/`, not left implicit.

3. **File-first RRR is safer than shell-first RRR.**
   - Retrospectives and learnings are written as markdown under `psi/memory/`; shell scripts like `pulse.sh` should be small, testable utilities rather than the primary driver of the workflow.

## How to use this going forward

When running `/rrr` in this repository:

1. Let the assistant handle **files**:
   - Creating/updating retrospectives under `psi/memory/retrospectives/`.
   - Creating/updating learnings under `psi/memory/learnings/`.

2. Run **Git Bash commands** yourself when needed:
   - From the workspace root:
     - `bash tools/pulse.sh` to refresh pulse data after a retro.
     - `git add psi/memory/retrospectives psi/memory/learnings psi/data/pulse` and commit with an `rrr:` message.

3. Treat this file and [`2026-02-18_shell-and-recap-discipline.md`](psi/memory/learnings/2026-02-18_shell-and-recap-discipline.md:1) as the canonical references for RRR utilities and environment assumptions in `Knowledge_System`.

