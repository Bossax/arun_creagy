---
title: # NotebookLM MCP auth recovery + atomic extraction + commit boundary discipline
tags: []
created: 2026-04-15
source: ψ/memory/learnings/2026-03-30_notebooklm-mcp-auth-atomic-extraction-and-commit-boundaries.md
---

# # NotebookLM MCP auth recovery + atomic extraction + commit boundary discipline

# NotebookLM MCP auth recovery + atomic extraction + commit boundary discipline

## Context
NotebookLM MCP access intermittently failed (auth drift + timeouts). At the same time, the repo contained multiple concurrent streams of work (WMO-NFCS quote extraction + CRDB narrative packaging + tooling/config diffs), making it easy to create messy commits.

## Pattern
When MCP services are flaky and the workspace is “multi-stream”, reliability comes from two disciplines:

1) **Stabilize the toolchain** (auth + smaller queries)
2) **Stabilize the repo history** (commit boundaries that match intent)

## What worked
### A) MCP auth recovery (fastest reliable path)
- Check health/auth.
- Run cleanup with `preserve_library=true`.
- Ensure all Chrome/Chromium instances are closed if cleanup partially fails.
- Re-run auth; verify authenticated state.

### B) Timeout mitigation for NotebookLM extraction
- Prefer **atomic prompts** (single theme, hard length limit).
- If timeouts persist: reduce to 3–5 quotes, 120–200 words total, then iterate.

### C) Commit boundary discipline
- Decide boundaries explicitly (e.g., “WMO-NFCS only” vs “CRDB narrative” vs “tooling/config”).
- Stage only the intended paths; leave everything else uncommitted.

## Why this matters
- Extraction quality improves because you can keep iterating without fighting the tool.
- Repo history stays legible, which is essential when narrative decisions must be justified later.


---
*Added via Oracle Learn*
