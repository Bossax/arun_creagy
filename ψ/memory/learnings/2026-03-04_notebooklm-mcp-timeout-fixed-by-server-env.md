title: NotebookLM MCP timeouts fixed by increasing server env timeouts + disabling stealth
tags:
  - notebooklm
  - mcp
  - troubleshooting
created: 2026-03-04
status: superseded
superseded_by: 2026-03-04_notebooklm-mcp-timeouts-fixed-by-increasing-serv.md
---

> This troubleshooting note has been superseded by [`2026-03-04_notebooklm-mcp-timeouts-fixed-by-increasing-serv.md`](ψ/memory/learnings/2026-03-04_notebooklm-mcp-timeouts-fixed-by-increasing-serv.md); kept for earlier wording and additional notes.

# NotebookLM MCP timeouts fixed by increasing server env timeouts + disabling stealth

## Pattern

If [`mcp--notebooklm--ask_question`](mcp--notebooklm--ask_question:1) repeatedly fails with `MCP error -32001: Request timed out` even though [`mcp--notebooklm--get_health`](mcp--notebooklm--get_health:1) reports `authenticated: true`, treat it primarily as a **latency budget** issue (Notebook loading + UI automation slower than the client wait window).

## Fix

1) Add/adjust NotebookLM MCP `env` in [`/.roo/mcp.json`](.roo/mcp.json:1), e.g.

- `BROWSER_TIMEOUT=180000`
- `STEALTH_ENABLED=false`
- `TYPING_WPM_MIN=400`

2) Restart VS Code (or restart the `notebooklm` MCP server) so the MCP server process is recreated with the new environment.

## Notes

- Disabling stealth reduces random delays and human-like typing overhead, improving reliability for time-sensitive flows.
- If timeouts persist, check for profile locks / background `notebooklm-mcp` processes holding the automation profile directory.

