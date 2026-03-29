---
name: writing-th-learn
description: Extracts Thai writing patterns by comparing draft vs edited versions. links learnings to the session writing plan + example report style reference.
---

# /writing-th-learn

> Learning-only companion for `/writing-th`. Compares a **Thai draft** and its **human-edited** version, then stores what changed as reusable patterns.

## When to use this skill

- After you used `/writing-th` to produce a draft **and** you have an edited version (`...-edited.md`).
- When closing a session with `/rrr` and you want to capture **Thai writing style learnings** separate from the general retrospective.
- When you have any Thai draft/edited pair and want to update `writing-th`'s understanding of your word choice and phrasing.

## When NOT to use this skill

- If there is no edited version yet (only a draft exists) — use `/writing-th` first to draft and let the human edit.
- If the change is not about Thai wording, phrasing, or narrative structure (for example pure data or numbers updates).
- If you only need to generate a new Thai draft — use `/writing-th` instead.

## Inputs required

1) **Mode**: `report` or `article` (must match the mode originally used in `/writing-th`).
2) **Writing plan path** (recommended): the anchor plan markdown file for the session.
3) **Draft file path**: markdown file.
4) **Edited file path**: markdown file.
5) (Optional) **Example report path**: the style reference used in the session (if any).
6) (Optional) **Context tags**: short tags for `oracle_learn` (e.g., `thai-tone`, `gov-report`, `interview-prep`).

### Naming rule (recommended, but not mandatory)

- Preferred: `...-draft.md` and `...-edited.md` pairing.
- If real files do not conform, proceed only if a clear mapping is recorded (Nothing is Deleted):
  - Add a small mapping block in the writing plan (recommended template is in [`/writing-th`](.roo/skills/writing-th/SKILL.md:1)).

## Workflow

1) **Validate inputs**
   - Confirm that both files exist and are markdown.
   - Prefer: they share the same base name and differ only by `-draft` vs `-edited`.
   - If not: require explicit mapping (in the plan or user message) before continuing.

2) **Read session context (Option C)**

   - If a writing plan path is provided:
     - Read it and find the latest “Session Style Pack Summary”.
     - Capture:
       - example report reference + permission line
       - session terminology / flow constraints
       - safety rails (citations/hedging/no hallucinations)

3) **Read both files**
   - Read the full content of the `draft` and `edited` files.

4) **Compare and extract patterns**
   - Focus on **what the human changed**, not on line-by-line diffs.
   - Identify and summarize:
     - **Word choice and phrasing**:
       - recurrent substitutions (e.g., more formal vs informal verbs, consistent noun choices);
       - changes in tone (more/less formal, softer/stronger hedging);
       - preference for certain connectors, transitions, or emphasis styles.
     - **Semantic arrangement and structure**:
       - reordering of sentences or paragraphs to improve flow;
       - patterns in how the human introduces context, states key messages, and provides evidence;
       - ways the human simplifies or elaborates concepts for clarity.
   - Keep the summary concise and pattern-based (no full text copies).

5) **Write learning note to ψ/memory**

    - Compose a learning note in Thai (with English only where necessary) with sections:
      - `## Word choice and phrasing`
      - `## Semantic and structure patterns`
      - `## Implications for future drafts`
      - `## Session context (traceability)`
   - Save it to:
     - `ψ/memory/learnings/YYYY-MM-DD_writing-th-<mode>-learn.md` where `<mode>` is `report` or `article`.
    - If multiple learning notes already exist for the same day and mode, append a new section with a clear heading instead of overwriting.

   - In `## Session context (traceability)` include links:
     - writing plan path (if any)
     - draft path + edited path
     - example report path (if any)

6) **oracle_learn call**

   - Call `oracle_learn` with:
     - `pattern`: the distilled patterns from the learning note (especially "Implications for future drafts").
      - `concepts`: tags including `writing-th`, the mode (`report` or `article`), and any additional context tags.
      - `source`: a short identifier like `"writing-th-learn: draft-vs-edited"`.

   **Materialization guardrail (IMPORTANT)**

   - After `oracle_learn()`, immediately read the returned `file` path.
   - If read fails with `ENOENT`, materialize the file manually (patch tooling), per:
     - [`ψ/memory/learnings/2026-03-27_oracle-learn-file-materialization-guardrail.md`](ψ/memory/learnings/2026-03-27_oracle-learn-file-materialization-guardrail.md:1)

7) **Link back to execution skill**

    - In the learning note, add a short line that this file is discoverable by `/writing-th` via MCP search:
      - e.g. "เรียนรู้จากการเปรียบเทียบฉบับร่างและฉบับแก้ไขสำหรับ writing-th (mode: report/article)".

   - If a writing plan exists, append an “Learn-back recorded” line into the plan (append-only) with a link to the learning note.

## Notes for /rrr integration

- `/rrr` should **not** recreate this logic; instead, it can:
  - Detect when a Thai draft/edited pair was created in the session; then
  - Invoke `/writing-th-learn` once per pair to record learnings.
- Retrospective and Thai-writing learnings must stay in **separate files**:
  - `/rrr` writes session retrospectives under `ψ/memory/retrospectives/...` and general learnings under `ψ/memory/learnings/...`.
  - `/writing-th-learn` writes **Thai-writing-focused** learnings with the `writing-th-<mode>-learn` suffix so they are easy to query later.

