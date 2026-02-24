# Lesson: Environment Agnosticism is Active Work

**Context**: Failed `/recap` script execution due to path issues and `date` command failure on Windows during a `/rrr` retrospective.
**Observation**: Static paths (e.g., `~/.claude/...`) and Unix-specific commands (`date +%...`) are brittle in a Windows-hosted VS Code environment, causing avoidable errors and context switching.
**Insight**: Cross-platform compatibility isn't just a "nice to have"—it's a requirement for fluid agent operation. We cannot assume a POSIX environment.
**Action**:
1.  Prefer relative paths or dynamic discovery for scripts.
2.  Use language-native time/date functions (Node/Python) instead of shell commands when precision format is needed.
3.  Proactively check OS context before issuing shell commands.

**Tags**: #engineering #cross-platform #agent-efficiency #windows #tooling
