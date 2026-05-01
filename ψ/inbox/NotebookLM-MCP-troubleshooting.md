## 2026-04-22 — AS-3 continuation timeout/auth recovery pattern
- **Symptom**: NotebookLM MCP flow encountered timeout/auth friction during AS-3 continuation.
- **Recovery pattern that worked**: re-authenticate, resume in continuation mode (same extraction packet scope), and re-run the pending batch without changing extraction schema.
- **Verification signal**: downstream pipeline closed normally (flatten/QC 57 rows → register 57 entries → mismatch crosswalk 22 grouped entries), indicating recovery did not corrupt packet lineage.

## 2026-05-01 — Browser context closes immediately (launchPersistentContext)
- **Symptom**: `mcp--notebooklm--ask_question` fails immediately with `browserType.launchPersistentContext: Target page, context or browser has been closed`.
- **Observed behavior**: Chrome launches headless, then is closed/killed; Playwright reports context/browser closed. Error includes process exitCode=21.
- **Scope**: blocks even minimal “test query” (not prompt-length related).
- **Environment**: Windows 11; NotebookLM MCP health reports `authenticated=true`.
- **Next checks to try (in order)**:
  1. Run [`mcp--notebooklm--get_health`](ψ/inbox/NotebookLM-MCP-troubleshooting.md:1) again to confirm state.
  2. Try a new session (omit `session_id`) to see if a stale session is causing crash.
  3. If still failing, apply controlled re-auth workflow (re_auth) per [`notebooklm-rules`](.roo/skills/notebooklm-rules/SKILL.md:58).

## 2026-05-01 — Cleanup (preserve library) was partial due to locked local profile
- **Action**: Ran `cleanup_data(confirm=true, preserve_library=true)` after preview.
- **Result**: `status = partial`.
- **Deleted**:
  - `C:/Users/sitth/AppData/Roaming/notebooklm-mcp`
- **Failed (locked / could not delete)**:
  - `C:/Users/sitth/AppData/Local/notebooklm-mcp`
  - `C:/Users/sitth/AppData/Local/notebooklm-mcp/Data/chrome_profile`
- **Hypothesis**: a background `chrome.exe` / Chromium process (or another lock) is still holding the profile directory.
- **Next step**: close all Chrome/Chromium processes (Task Manager), then rerun cleanup + auth.

## 2026-05-01 — Query 1 (corpus-wide) timed out

- **Operation**: [`mcp--notebooklm--ask_question()`](mcp--notebooklm--ask_question:1)
- **Parameters**:
  - `notebook_id = urban-resilience-infrastructur`
  - `session_id = 6085058f`
- **Error**: `MCP error -32001: Request timed out` (tool-reported timeout: 60000ms)
- **Planned mitigation**: rerun with `browser_options.timeout_ms = 360000` (6 minutes) and keep response bounded.

## 2026-05-01 — Query 1 (corpus-wide) timed out again (timeout override ignored)

- **Operation**: [`mcp--notebooklm--ask_question()`](mcp--notebooklm--ask_question:1)
- **Parameters**:
  - `notebook_id = urban-resilience-infrastructur`
  - `session_id = 6085058f`
  - `browser_options.timeout_ms = 360000` (requested)
- **Error**: `MCP error -32001: Request timed out` (tool-reported timeout still: 60000ms)
- **Interpretation (hypothesis)**: upstream caller / adapter is enforcing a hard 60s timeout regardless of `browser_options.timeout_ms`.

## 2026-05-01 — Query 1 timed out again even with visible browser + fast typing settings

- **Operation**: [`mcp--notebooklm--ask_question()`](mcp--notebooklm--ask_question:1)
- **Parameters (as requested by user)**:
  - `notebook_id = urban-resilience-infrastructur`
  - `session_id = 6085058f`
  - `show_browser = true`
  - `browser_options.show = true`
  - `browser_options.headless = false`
  - `browser_options.timeout_ms = 360000` (requested)
  - `browser_options.stealth.human_typing = true`
  - `browser_options.stealth.typing_wpm_min = 500`
  - `browser_options.stealth.typing_wpm_max = 700`
- **Error**: `MCP error -32001: Request timed out` (tool-reported timeout still: 60000ms)

Interpretation:
- The browser session can continue running/rendering, but the **MCP call channel** is being terminated at ~60s by an upstream timeout (likely the host/tool-call wrapper), so no response is returned to the client even if the page is still loading/processing.
