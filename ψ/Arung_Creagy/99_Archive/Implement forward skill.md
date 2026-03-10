# ORACLE MODE: FORWARD + PLAN PATTERN

When I use the command "/forward" or say "wrap up session", you must strictly follow this "Forward + Plan" chain protocol. Do not skip steps.

## PHASE 1: HANDOFF (The Context)
1.  **Create a Handoff File**:
    - Path: `psi\inbox\handoff\YYYY-MM-DD_HH-MM_slug.md` (Use backslashes for Windows paths if needed, but forward slashes usually work).
    - Content must include:
      - **Context**: One-line summary of the session's focus.
      - **What We Did**: Bullet points of accomplishments.
      - **Pending**: Items left unfinished.
      - **Next Session**: Specific actions for the next time.
2.  **Git Sync**:
    - Run `git add .`
    - Run `git commit -m "handoff: [slug]"`
    - Run`git push`

## PHASE 2: PLAN MODE (The Direction)
*IMMEDIATELY after the git push succeeds, enter "Plan Mode". Do not ask for permission.*

1.  **Create/Update a Project Plan File**:
    - Create a new markdown file (if not exisit) that serves as the instruction for the *next* work session of a project using `~\src\00_Meta\template\TODO.md` as a template.
    - Name the file with "(project_code) - Plan"
    - update the properties of the file

2.  **Finalize**:
    - Show me the content of the Plan file.
    - Tell me: "Plan secured. Ready for context clear."

## PHASE 3: CLEANUP
- Wait for me to issue `/clear` or `/compact`.