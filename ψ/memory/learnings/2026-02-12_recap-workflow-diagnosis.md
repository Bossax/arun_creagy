## Context
During a session focused on fixing the `/recap` skill, a user's feedback highlighted that the recap output did not explicitly state the focus of the previous session. This led to a diagnosis of the recap workflow and a subsequent implementation of improvements.

## Problem
The `recap-rich.ts` script lacked robust mechanisms to:
1. Consistently resolve paths containing the `ψ` character, leading to potential file access issues.
2. Reliably identify and present the focus of the last session, especially when no explicit focus file was being tracked by the script itself.
3. Use local time for date derivations, which could lead to discrepancies with user's local context.
4. Deterministically select the latest retrospective file, potentially showing an older session due to file system ordering.

## Solution
Implemented several changes to `recap-rich.ts`:
1. Introduced `resolvePsiPath` function to provide a fallback mechanism for `ψ` paths to `psi` paths.
2. Updated all relevant path references (`focusFile`, `scheduleFile`, `tracksDir`, `retroDir`, `handoffDir`) to use `resolvePsiPath`.
3. Modified date derivation for `month` to use local time (`now.getFullYear()`, `now.getMonth()`, `now.getDate()`).
4. Enhanced the 