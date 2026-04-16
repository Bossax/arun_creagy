---
title: ---
tags: []
created: 2026-04-15
source: ψ/memory/learnings/2026-03-27_oracle-learn-file-materialization-guardrail.md
---

# ---

---
title: Guardrail — Verify oracle_learn() materializes a repo-local learning file
created: 2026-03-27
status: superseded
superseded_by: 2026-04-09_guardrail-after-every-oraclelearn-call-immedi.md
---

> This learning has been superseded by [`2026-04-09_guardrail-after-every-oraclelearn-call-immedi.md`](ψ/memory/learnings/2026-04-09_guardrail-after-every-oraclelearn-call-immedi.md); kept for historical context and example incidents.

# Guardrail — Verify `oracle_learn()` materializes a repo-local learning file

**Date**: 2026-03-27 (Asia/Bangkok)

## Problem

Sometimes an MCP call (e.g., `oracle_learn()`) reports success and returns a target path under `ψ/memory/learnings/…`, but the corresponding markdown file is not present on disk immediately after (observed as `ENOENT` when trying to read it).

## Guardrail (operational implementation)

After every `oracle_learn()` call:

1) **Capture** the returned `file` path from the tool response.
2) **Verify existence** in the working tree by reading the file at that path.
   - If read succeeds: stop (file exists).
   - If read returns `ENOENT`: continue to step 3.
3) **Create the missing file** at the exact returned path and paste the learning content into it (use `apply_patch`, not shell redirection).
4) **Re-read** the created file to confirm it is now on disk.
5) Optionally, run `git status` to ensure it is staged/tracked as expected.

## Notes

- This guardrail is tool-agnostic: it works whether `oracle_learn()` was called directly or indirectly (e.g., via an “important” info logging flow).
- It does not fix the underlying MCP issue; it prevents “invisible” learnings.

## Example (local evidence)

- Repo-local learning created after a missing-file incident: [`ψ/memory/learnings/2026-03-27_director-toey-suggested-we-talk-to.md`](ψ/memory/learnings/2026-03-27_director-toey-suggested-we-talk-to.md)
- Repo-local learning created after a missing-file incident: [`ψ/memory/learnings/2026-03-27_dcce-has-a-planned-internal-reorganization-march.md`](ψ/memory/learnings/2026-03-27_dcce-has-a-planned-internal-reorganization-march.md)

---
*Added via Oracle Learn*
