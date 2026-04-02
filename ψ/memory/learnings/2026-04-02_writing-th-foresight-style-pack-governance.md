# Learning — Writing-TH Foresight Style Pack Governance (2026-04-02)

## Pattern

When designing a Thai report-writing workflow with `/writing-th` and `/writing-th-learn`, a **project style pack** must not be treated as “fully materialized” unless its contents actually inline the rules being claimed.

For a project like the foresight 2590 report:
- The project style brief file (e.g. [`plans/foresight-report-writing-style-brief.md`](plans/foresight-report-writing-style-brief.md)) should be the **single authoritative style artifact**.
- It may reference global sources (resonance, `writing-th` learnings, example reports), but those references must be clearly marked as pointers, not as proof of full condensation.
- If we want a truly self-contained style pack, we must perform an explicit condensation pass:
  - Read resonance and a curated subset of `writing-th` learnings and example reports.
  - Distill only the relevant rules into the brief in concrete, auditable bullet points.
  - Label the result as a materialized style pack for that project.

## Why this matters

- Overstating how much has been “materialized” into a style pack erodes trust, especially in high-stakes narrative work where tone and framing are critical.
- A single, auditable style artifact per project reduces confusion and makes it easier for humans to see what rules the agent is actually following.
- Clear separation between **design** (what the workflow should eventually do) and **implemented content** (what is written into SKILL files and style packs) prevents accidental hallucinations about system behavior.

## Implications for future work

- For new reports using `/writing-th`:
  - Start with resonance + global learnings + example reports, but be explicit that the project brief is initially a partial synthesis.
  - Only claim full condensation when a deliberate pass has been made to inline the relevant global rules.
  - Keep one project style pack/brief per deliverable, and avoid proliferating secondary style files unless they have a clearly distinct role.

## Context

- Repository: Arun_Creagy (foresight 2590 report)
- Session: 2026-04-02 — debugging `writing-th` style pack behavior and project brief content, with high user frustration around over-claimed condensation.

