# Lesson Learned — Recap Local Skill Fix

On Windows with Bun, `ls -t` executed through Bun’s `$` can produce a non-time-ordered list; use `bash -lc` to ensure correct recency ordering when selecting the latest retrospective or handoff. Keep project-specific skills under `.roo/skill/` to avoid conflicts with upstream skill repositories and make ownership explicit.

---
*Added via Oracle Learn*
