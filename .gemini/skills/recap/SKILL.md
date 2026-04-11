---
installer: local
name: recap
description: Local recap for this repo (uses project-local script).
trigger: /recap
---

# /recap — Fresh Start Context (Local)

**Goal**: Orient quickly using the project-local recap script.

This local override uses the existing script at `.roo/skills/recap/recap.ts` and does not introduce new logic.

## Usage

```
/recap           # Local recap (project script)
/recap --quick   # Alias to the same local script
```

---

## DEFAULT MODE (Local)

Run the local recap script:

```bash
bun .roo/skills/recap/recap.ts
```

Then add 2–3 “What’s next?” options based on the output.

---

## QUICK MODE (`/recap --quick`)

Use the same local script for a fast summary:

```bash
bun .roo/skills/recap/recap.ts
```

---

## "What's next?" Rules

| If you see... | Suggest... |
|---------------|------------|
| Handoff exists | Continue from handoff |
| Untracked files | Commit them |
| Focus = completed | Pick from tracks or start fresh |
| Branch ahead | Push or create PR |
| Streak active | Keep momentum going |

---

## Hard Rules

1. **ONE bash call** — never multiple parallel calls (adds latency)
2. **No subagents** — everything in main agent
3. **Ask, don't suggest** — "What next?" not "You should..."

---

**Philosophy**: Detect reality. Surface blockers. Offer direction.

