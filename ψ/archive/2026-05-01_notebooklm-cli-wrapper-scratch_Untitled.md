# ARCHIVED SCRATCH NOTE — NOT EXECUTABLE

This file is archived to preserve history.

## Why this exists

This contains an example of a **Gemini CLI-style MCP wrapper command** that is **not runnable** in this workspace.

- Evidence: this note itself records the PowerShell error that `use_mcp_tool` is not recognized.
- The actual MCP configuration for this repo is in [`.roo/mcp.json`](.roo/mcp.json:1) (NotebookLM server runs via `npx notebooklm-mcp@latest`, not a `use_mcp_tool` cmdlet).

## Original scratch content (verbatim)

```shell
pwsh -NoProfile -Command "use_mcp_tool -ServerName notebooklm -ToolName get_health -Arguments '{}'"
```

**use_mcp_tool: **The term 'use_mcp_tool' is not recognized as a name of a cmdlet, function, script file, or executable program.****
****Check the spelling of the name, or if a path was included, verify that the path is correct and try again.****

notebooklm://notebooks

No description

Returns `Unknown`
