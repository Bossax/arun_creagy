# Handoff: Restore local skills + standup/recap fixes

**Date**: 2026-03-25 10:58
**Context**: 90%

## What We Did
- Restored the repo’s local Roo skills baseline (kept only the tracked local skills).
- Reimplemented local `/standup` as SKILL-only (no script) with `bash -lc` retro ordering fix and no `focus-agent-main.md` usage.
- Restored local `/recap` SKILL.md pointing to the existing `.roo/skills/recap/recap.ts`.
- Tracked `.clinerules` in git.
- Tested `/standup` and `/recap --quick` outputs.

## Pending
- [ ] None (local skills and standup/recap fixes complete).

## Next Session
- [ ] Optional: verify skill files are staged and committed as expected if any further changes occur.

## Key Files
- `.roo/skills/standup/SKILL.md`
- `.roo/skills/recap/SKILL.md`
- `.roo/skills/recap/recap.ts`
- `.clinerules`
- `ψ/incubate/DCCE/CRDB/output/Conceptual Data Model for climate risk and adaptation data system.md`
