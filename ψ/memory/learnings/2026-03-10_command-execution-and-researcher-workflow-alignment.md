---
type: learning-index
created: 2026-03-10
tags:
  - knowledge-ops
  - workflow
  - migration
  - command-execution
  - researcher-workflow
---

# Learning Index — split for searchability

This note was split into smaller atomic notes so search works better and each idea can evolve independently.

## Split into
- Command execution reliability (hybrid shell): [`2026-03-10_command-execution-reliability-hybrid-shell.md`](ψ/memory/learnings/2026-03-10_command-execution-reliability-hybrid-shell.md:1)
- Research workflow alignment (Sensing → Forge → Harvest → Rhythm): [`2026-03-10_research-workflow-alignment_sensing-forge-harvest-rhythm.md`](ψ/memory/learnings/2026-03-10_research-workflow-alignment_sensing-forge-harvest-rhythm.md:1)
- Knowledge migration playbook (repeatable refactors): [`2026-03-10_knowledge-migration_playbook.md`](ψ/memory/learnings/2026-03-10_knowledge-migration_playbook.md:1)

## Archived bundle (kept for history)

### Pattern
When operating in a hybrid Windows environment (Git Bash + Unicode paths + tools that sometimes truncate/partially execute), long inline shell commands are a primary source of errors. Reliability improves sharply when migration work is expressed as small, rerunnable scripts with built-in verification and logging.

### What happened
- Inline shell attempts failed unpredictably (quoting, heredocs, command splitting, timezone output, and environment differences).
- The work succeeded once we moved to script-based operations:
  - move operations performed via Python `shutil.move`
  - collision handling via `__dupN`
  - explicit destinations created before moving
  - links updated via a targeted replace tool
  - provenance captured in [`ψ/archive/migration-log.md`](ψ/archive/migration-log.md:1)

### Reusable playbook
1) **Plan as a migration**, not as “file cleanup.”
2) **One responsibility per script** (move notes, move outputs, move assets, update links, cleanup).
3) Always:
   - log every move
   - avoid overwrites
   - validate with counts + spot-check samples

### Workflow alignment (Boss preference)
- Sensing phase: dump into inbox; don’t interrupt deep work to structure.
- Forge phase: keep project context in incubate hubs + `plan.md`.
- Harvest: extract atomic notes from project outputs and retro lessons.
- Rhythm: wrap sessions with rrr/recap, carry forward decisions.

### Confidence
- High: script-first migration approach improves reliability.
- High: inbox triage queues match capture-first workflow.
- Medium: best “embed update” strategy depends on note system conventions (Obsidian paths vs markdown links).


---
*Added via Oracle Learn*
