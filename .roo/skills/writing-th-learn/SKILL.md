---
name: writing-th-learn
description: Extracts Thai writing patterns by comparing draft vs edited versions, focusing on word choice and semantic arrangement, and writes learnings for reuse by the writing-th skill or when invoked from retrospectives like /rrr.
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
2) **Draft file path**: a markdown file whose name ends with `-draft.md`.
3) **Edited file path**: a markdown file with the same base name as the draft, ending with `-edited.md`.
4) (Optional) **Context tags**: short tags for `oracle_learn` (e.g., `thai-tone`, `gov-report`, `interview-prep`).

## Workflow

1) **Validate inputs**
   - Confirm that both files exist and are markdown.
   - Confirm that they share the same base name and differ only by the `-draft` vs `-edited` suffix.

2) **Read both files**
   - Read the full content of the `draft` and `edited` files.

3) **Compare and extract patterns**
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

4) **Write learning note to ψ/memory**

   - Compose a learning note in Thai (with English only where necessary) with sections:
     - `## Word choice and phrasing`
     - `## Semantic and structure patterns`
     - `## Implications for future drafts`
   - Save it to:
     - `ψ/memory/learnings/YYYY-MM-DD_writing-th-<mode>-learn.md` where `<mode>` is `report` or `article`.
   - If multiple learning notes already exist for the same day and mode, append a new section with a clear heading instead of overwriting.

5) **oracle_learn call**

   - Call `oracle_learn` with:
     - `pattern`: the distilled patterns from the learning note (especially "Implications for future drafts").
     - `concepts`: tags including `writing-th`, the mode (`report` or `article`), and any additional context tags.
     - `source`: a short identifier like `"writing-th-learn: draft-vs-edited"`.

6) **Link back to execution skill**

   - In the learning note, add a short line that this file is discoverable by `/writing-th` via MCP search:
     - e.g. "เรียนรู้จากการเปรียบเทียบฉบับร่างและฉบับแก้ไขสำหรับ writing-th (mode: report/article)".

## Notes for /rrr integration

- `/rrr` should **not** recreate this logic; instead, it can:
  - Detect when a Thai draft/edited pair was created in the session; then
  - Invoke `/writing-th-learn` once per pair to record learnings.
- Retrospective and Thai-writing learnings must stay in **separate files**:
  - `/rrr` writes session retrospectives under `ψ/memory/retrospectives/...` and general learnings under `ψ/memory/learnings/...`.
  - `/writing-th-learn` writes **Thai-writing-focused** learnings with the `writing-th-<mode>-learn` suffix so they are easy to query later.

