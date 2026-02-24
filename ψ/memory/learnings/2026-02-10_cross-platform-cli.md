# Lesson Learned: Cross-Platform CLI Robustness on Windows

**Date**: 2026-02-10
**Category**: Development Environment
**Tags**: #windows #powershell #cli #cross-platform

## Context
While executing standard maintenance tasks (retrospectives) in a Windows 11 environment, initial attempts to use Unix-style commands (e.g., `date`, `mkdir -p`) failed or behaved unexpectedly in the default `cmd.exe` shell.

## Problem
Many AI-generated or skill-defined scripts assume a POSIX-compliant environment. On Windows, `date` is an interactive command that waits for user input to change the system date, and `mkdir -p` is not supported by `cmd.exe`.

## Solution
Leverage PowerShell directly for system-level operations within the `execute_command` tool. PowerShell provides more consistent behavior and powerful formatting options that bridge the gap between Unix and Windows CLI paradigms.

**Example: Robust Date Formatting**
```powershell
powershell -Command "Get-Date -Format 'HH:mm K (dddd dd MMMM yyyy)'"
```

**Example: Robust Directory Creation**
```powershell
powershell -Command "New-Item -ItemType Directory -Force -Path 'path/to/dir'"
```

## Lessons Learned
1. **Shell Awareness**: Always verify the active shell and OS before issuing CLI commands.
2. **Explicit Fallbacks**: Skill instructions should ideally provide both POSIX and PowerShell variants of common operations.
3. **Avoid Interactive Commands**: Avoid commands like `date` in `cmd.exe` that might hang the terminal session waiting for input.
