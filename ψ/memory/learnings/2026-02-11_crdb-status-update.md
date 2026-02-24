# Lessons Learned: Cross-Platform CLI and Pulse Data

## Cross-Platform CLI Nuances
When executing CLI commands, especially system utilities like `date` and `time`, it is crucial to account for operating system differences. Unix-like systems often use `date "+%H:%M %Z (%A %d %B %Y)"` for formatted output, whereas Windows `cmd.exe` requires `date /t` and `time /t` for basic date and time display. Failing to adapt to these platform-specific syntaxes can lead to command execution errors. Always consult the `SYSTEM INFORMATION` provided in the environment details and, if unsure, test commands or craft them to be more robust across different shell environments.

## Value of Pulse Data in Retrospectives
The `pulse` data (from `psi/data/pulse/project.json` and `psi/data/pulse/heartbeat.json`) provides significant contextual enrichment for session retrospectives. This data, when available, allows for insights into: 
*   Total sessions in a project.
*   Average messages per session.
*   Session categorization (e.g., short, medium, long).
*   Activity on the current branch.
*   Developer streak (days of consecutive work).
*   Week-over-week activity changes.

Its absence during a retrospective generation noticeably limits the depth of the "AI Diary" and "Session Summary" sections, as it prevents a data-driven narrative about project momentum and personal engagement. For comprehensive self-reflection and performance tracking, ensuring the availability and integration of pulse data is highly beneficial.