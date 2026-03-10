# Next Session Plan — Knowledge Ops Migration + Workflow Alignment

References handoff: [`ψ/inbox/handoff/2026-03-10_12-06_knowledge-ops-migration-workflow-alignment.md`](ψ/inbox/handoff/2026-03-10_12-06_knowledge-ops-migration-workflow-alignment.md:1)

## What We Accomplished
- Reorganized knowledge workflow boundaries: capture → [`ψ/inbox/`](ψ/inbox/:1), forge → [`ψ/incubate/`](ψ/incubate/:1), harvest → [`ψ/memory/learnings/`](ψ/memory/learnings/:1), rhythm → [`ψ/memory/retrospectives/`](ψ/memory/retrospectives/:1)
- Migrated legacy `active/` + `writing/` contents via repeatable scripts with a provenance log in [`ψ/archive/migration-log.md`](ψ/archive/migration-log.md:1)
- Preserved embed integrity by moving shared images to [`ψ/incubate/_shared_assets/pic/`](ψ/incubate/_shared_assets/pic/:1) and rewriting `![[pic/...]]` links with [`tools/update_pic_links.py`](tools/update_pic_links.py:1)
- Split bundled learning into atomic notes for improved search: see [`ψ/memory/learnings/2026-03-10_command-execution-and-researcher-workflow-alignment.md`](ψ/memory/learnings/2026-03-10_command-execution-and-researcher-workflow-alignment.md:1)

## Pending Items (Carry Forward)
- [ ] Triage + route: process [`ψ/inbox/_triage_from_active/`](ψ/inbox/_triage_from_active/:1) and [`ψ/inbox/_triage_from_writing_notes/`](ψ/inbox/_triage_from_writing_notes/:1) into the correct project incubate hubs
- [ ] Decide Oracle DB sync strategy for learnings: keep bundled entry vs supersede with 3 atomic learnings
- [ ] Sanity check: spot-check a few markdown notes that previously embedded `![[pic/...]]` to confirm images resolve

## Cleanup Context
- Git status should be inspected before any commit; migration likely produced large move churn (delete/add) and should not be committed unless explicitly desired.

## Next Session Goals (Scope)
1) Inbox triage routing pass (fast wins)
2) Hub/plan hygiene (ensure the hub links to the right outputs, and plan captures the next deliverable)
3) Optional: Oracle DB supersede/sync for the atomic learnings

## Next Session: Pick Your Path

| Option | Command | What It Does |
|---|---|---|
| **Continue** | `/recap` | Pick up from the current vault state and execute the triage routing pass |
| **Clean up first** | Review git status, then `/recap` | Ensure repo state is safe/intentional before doing more moves |
| **Fresh start** | `/recap --quick` | Minimal context, switch focus to another task |

### Cleanup Checklist (if any)
- [ ] Review `git status --short` output before committing anything

