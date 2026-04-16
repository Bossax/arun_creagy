---
title: # Lessons Learned: /rrr Tool Usage
tags: [read_file, cross-platform, LF/CRLF, pulse-data, retrospective]
created: 2026-04-15
source: C:\Users\sitth\OracleWorkspace\Arun_Creagy\ψ\memory\learnings\2026-02-12_rrr_tool_usage.md
---

# # Lessons Learned: /rrr Tool Usage

# Lessons Learned: /rrr Tool Usage

- **Understanding `read_file` modes**: When reading files, especially non-code files or when the entire content is needed, prefer `mode=\'slice\'` without `anchor_line` or use a direct `cat` command to avoid errors related to `indentation` mode. `indentation` mode is best suited for extracting semantic code blocks when a specific line of interest is known.
- **Cross-platform compatibility**: Be mindful of line ending differences (LF vs CRLF) when working in a cross-platform environment, as indicated by git warnings. This can impact file integrity and diffs.
- **Importance of pulse data**: Even with minimal initial data, the pulse context provides a baseline for tracking project activity and growth over time, which is valuable for retrospectives and understanding project momentum.

---
*Added via Oracle Learn*
