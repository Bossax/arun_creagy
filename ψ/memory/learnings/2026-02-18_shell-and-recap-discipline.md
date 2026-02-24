# Shell and recap discipline – 2026-02-18

## Context

This learning captures a serious failure pattern around recap / RRR workflows and command execution in this repository.

- **Fact for this project**: the interactive shell used in VS Code is **always Git Bash**.
- Despite this, previous sessions behaved as if `cmd.exe` were the operative environment for commands, leading to repeated failures.
- Failing commands were retried many times (10+ API calls) without halting, without clear communication of the blocker, and without switching strategy.
- Result: the session failed; no useful progress on the requested recap/rrr work, and unnecessary consumption of the user's resources.

The failure context is described in the 2026-02-18 retrospective stored under `psi/memory/retrospectives/`.

## Key lessons

1. **Treat Git Bash as the canonical shell here.**
   - For this Knowledge_System workspace, assume that commands the user runs in VS Code land in **Git Bash**, not in `cmd.exe`.
   - Any assistant reasoning about shell behavior must start from this fact.

2. **Do not blindly repeat failing command patterns.**
   - If a command (or class of similar commands) fails twice, that is a hard signal to stop using that pattern in the current session.
   - After two similar failures, the assistant must:
     - Stop issuing that style of command.
     - Analyze why it failed.
     - Switch to an alternative approach (file-based tools, higher-level APIs, or explicit user guidance).

3. **Communicate blockers explicitly and early.**
   - When command execution fails repeatedly, the assistant must clearly state:
     - What was attempted.
     - What failed and how often.
     - What change in strategy will be adopted next.
   - Remaining silent while commands continue to fail is unacceptable; it wastes the user’s time and resources.

4. **Recap and RRR should be file-first, not shell-first.**
   - This repo already contains structured retrospectives and learnings under `psi/memory/retrospectives/` and `psi/memory/learnings/`.
   - For recap / RRR workflows, the default behavior must be:
     - Read existing retrospectives and learnings directly from these directories.
     - Summarize context and propose next actions using those files.
   - External shell-driven recap scripts are optional and must never be treated as the only or primary path.

## Operational rules for future sessions

1. **Assume Git Bash when reasoning about user-side shell behavior.**
   - When discussing or planning shell commands that the *user* will run in VS Code, assume Git Bash semantics (Unix-like tooling, `bash` syntax) unless the user explicitly says otherwise for a given session.

2. **Prefer tools and file reads over shell commands for assistant actions.**
   - For tasks that can be done via file listing/reading/editing tools, those tools should be preferred over shell commands.
   - Shell invocations should be reserved for cases where they genuinely add value and are clearly safe in a Git Bash context.

3. **Circuit breaker for failing commands.**
   - After two similar command execution failures, treat that pathway as unsafe in the current session.
   - Do not retry variations blindly; instead, change strategy and explain that decision.

4. **Recap / RRR workflow (high level).**
   - **Recap:**
     - Identify the latest retrospective under `psi/memory/retrospectives/`.
     - Read and summarize focus, outcomes, blockers, and pending work.
     - Optionally integrate recent learnings from `psi/memory/learnings/`.
   - **RRR:**
     - At session end, create a new retrospective file under `psi/memory/retrospectives/YYYY-MM/DD/HH.MM_topic.md`.
     - Include sections such as: Session Summary, Timeline, Files Modified, Key Learnings, Blockers & Resolutions, Honest Feedback.

## How to use this file

For any future work touching recap/rrr or shell commands in this repository:

- Recall this learning as the canonical memory about **Git Bash as the shell** and about avoiding repeated failing commands.
- Enforce the “two failures → stop and switch strategy” rule.
- Default to a file-first recap / RRR workflow using the existing memory directories.

