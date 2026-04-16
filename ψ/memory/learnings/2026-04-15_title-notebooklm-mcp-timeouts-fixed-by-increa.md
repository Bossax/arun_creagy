---
title: ---
tags: []
created: 2026-04-15
source: ψ/memory/learnings/2026-03-04_notebooklm-mcp-timeouts-fixed-by-increasing-serv.md
---

# ---

---
title: NotebookLM MCP timeouts fixed by increasing server env timeouts + disabling stealth
tags: [notebooklm, mcp, timeout, playwright, troubleshooting]
created: 2026-03-04
source: rrr: Knowledge_System
status: current
---

# NotebookLM MCP timeouts fixed by increasing server env timeouts + disabling stealth

## Pattern

If `mcp--notebooklm--ask_question` repeatedly fails with `MCP error -32001: Request timed out` while `mcp--notebooklm--get_health` shows `authenticated: true`, treat it as a latency-budget problem (Notebook load + UI automation slower than the client wait window).

## Fix

- Set NotebookLM MCP server env in `/.roo/mcp.json` (example values):
  - `BROWSER_TIMEOUT=180000`
  - `STEALTH_ENABLED=false`
  - `TYPING_WPM_MIN=400`
- Restart VS Code or restart the `notebooklm` MCP server so the env is applied.

## Notes

Disabling stealth reduces random delays and human-like typing overhead, improving reliability for time-sensitive automation flows.

---
*Added via oracle_learn(); canonical troubleshooting note for NotebookLM MCP timeouts*

---
*Added via Oracle Learn*
