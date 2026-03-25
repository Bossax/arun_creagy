---
installer: oracle-skills-cli v1.5.73
name: standup
description: v1.5.73 G-SKLL | Daily standup check - pending tasks, appointments, recent progress. Local override (SKILL-only).
alias: /standup
---

# /standup - Daily Standup (Local, SKILL-only)

Quick check: pending tasks (git), appointments (ψ), recent progress (git log), latest retrospective (ψ).

This local override **does not use** `ψ/inbox/focus-agent-main.md`. Focus is handled elsewhere.

## Usage

```bash
/standup
```

## Action

Run these commands sequentially in the repo root:

### 0) Timestamp
```bash
date "+🕐 %H:%M %Z (%A %d %B %Y)"
```

### 1) Open issues (optional)
```bash
gh issue list --state open --limit 10 --json number,title,updatedAt --jq '.[] | "#\(.number) \(.title)"'
```

### 2) Resolve ψ path
```bash
PSI=$(readlink -f ψ 2>/dev/null || echo "ψ")
```

### 3) Schedule / appointments
```bash
grep "^|" "$PSI/inbox/schedule.md" 2>/dev/null | grep -v "Date\|---" | head -5
```

### 4) Recent progress (24h)
```bash
git log --since="24 hours ago" --format="%h %s" | head -10
```

### 5) Latest retrospective (fixed ordering)
Use `bash -lc` to ensure consistent glob expansion + `ls -t` ordering:

```bash
bash -lc "ls -t \"$PSI\"/memory/retrospectives/$(date +%Y-%m)/*/*.md 2>/dev/null | head -1"
```

## Output Format

```markdown
## Standup @ [TIME]

### Done (24h)
- [commit 1]
- [commit 2]

### Pending Issues
| # | Task | Updated |
|---|------|---------|
| #N | title | date |

### Appointments Today
- [from schedule.md or "ไม่มีนัด"]

### Latest Retrospective
- [filename or "none"]

### Next Action
- [suggest based on priorities]
```

