# Mandate: System Rules (win32/PowerShell)

These rules ensure technical consistency and path compliance across the Windows/PowerShell environment.

## 1. Environment & Commands
- **Default Shell**: `powershell.exe -NoProfile`. 
- **The Brain (ψ)**: Use PowerShell for all path operations involving the `ψ` character.
- **Path Syntax**: 
  - **Tool Parameters**: Forward slashes (`/`) (e.g., `read_file(file_path="ψ/memory/...")`).
  - **Shell Commands**: Backslashes (`\`) (e.g., `ls ψ\memory`).
- **PowerShell Pipelines**: Always use explicit mapping (`$_.FullName`).

## 2. Technical Integrity
- **Absolute Paths**: Always resolve `ψ/` paths to their absolute host path when calling external CLIs.
- **Atomic Execution**: Maximum of two independent operations per `run_shell_command`.
- **Sorting**: Replace `ls -t` with `Get-ChildItem | Sort-Object LastWriteTime -Descending`.
