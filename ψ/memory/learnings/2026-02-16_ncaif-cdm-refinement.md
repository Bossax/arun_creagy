# Lessons Learned from NCAIF and CDM Refinement

*   Always verify `read_file` parameters, especially `anchor_line`, to avoid repeated errors.
*   Prioritize `read_file` to obtain exact content for `apply_diff` `SEARCH` blocks to ensure successful and precise modifications.
*   For multi-artifact design tasks, maintain a clear internal mental model or external notes to track dependencies and ensure all relevant files are addressed systematically.