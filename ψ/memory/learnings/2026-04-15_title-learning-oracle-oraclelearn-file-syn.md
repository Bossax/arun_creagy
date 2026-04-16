---
title: ---
tags: []
created: 2026-04-15
source: ψ/memory/learnings/2026-04-07_oracle-learn-file-sync-anomaly.md
---

# ---

---
title: Learning — Oracle oracle_learn File Sync Anomaly
created: 2026-04-07
status: superseded
superseded_by: 2026-04-09_guardrail-after-every-oraclelearn-call-immedi.md
---

> This anomaly note has been superseded at the guardrail level by [`2026-04-09_guardrail-after-every-oraclelearn-call-immedi.md`](ψ/memory/learnings/2026-04-09_guardrail-after-every-oraclelearn-call-immedi.md), but is kept for detailed environment/context evidence.

# Learning — Oracle `oracle_learn` File Sync Anomaly (2026-04-07)

## Context

- Environment: Arun_Creagy repo running locally at `c:/Users/sitth/OracleWorkspace/Arun_Creagy`.
- Oracle engine is started via docker-compose:
  - `./engine:/app`
  - `./Arun_Creagy:/vault`
  - `ORACLE_REPO_ROOT=/vault`
- In theory, container `/vault` and this repo root are the **same** filesystem.

## Observed Issue

- Calls to `oracle_learn` report success with a `file` path under `ψ/memory/learnings/` (for example, `ψ/memory/learnings/2026-04-07_using-the-criengland-data-repository-as-a-referen.md`).
- The corresponding markdown file **does not appear** under this repo’s `ψ/memory/learnings/` directory when inspected via Roo’s file tools.
- This has occurred across multiple sessions: `oracle_learn` indicates a document was added, but no new file is visible in the local workspace.

## Likely Explanation

- Oracle’s internal DB/index is being updated, so `oracle_search` and `oracle_stats` see the learning.
- The markdown file backing that document is either:
  - Not being written to disk under `/vault` at all, or
  - Written to a location that Roo’s file tools are not reading, despite the `/vault` mount.
- This repo is being run **locally**, whereas Oracle’s original deployment assumptions were GitHub/ghq-based. The Docker + Windows + Git Bash stack may introduce subtle path/permission differences between how the Oracle engine writes files and how Roo reads them.

## Impact

- It is unsafe to assume a successful `oracle_learn` call has created a markdown file in this Git repo.
- Saying “learning file X now exists in `ψ/memory/learnings/`” based solely on the MCP response is incorrect in this environment.

## Current Workaround / Discipline

- Treat `oracle_learn` as **updating Oracle’s internal memory/index only**.
- For anything that must exist as a Git-visible file here:
  - Always create or update it explicitly under `ψ/memory/learnings/` using Roo’s file tools (`apply_patch`, etc.).
  - Do not rely on `oracle_learn` side effects to create the markdown file.

## Next Steps (for future debugging)

- When convenient, inspect the Oracle engine container directly to see where `oracle_learn` writes files and compare that to `/vault/ψ/memory/learnings/`.
- Consider adding explicit logging inside the Oracle engine to print the **absolute path** of any file written by `oracle_learn`.
- Until resolved, keep a strict separation in the mental model:
  - Oracle MCP memory ≠ Git workspace files, even though they share the `/vault` mount.


---
*Added via Oracle Learn*
