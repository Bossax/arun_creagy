---
name: writing-th
description: Thai-first writing skill (report/article). MCP-first memory retrieval + example-report style mimicry + session style-pack summary (Option C) + outline-stop + learn-back via writing-th-learn.
---

# /writing-th [--report | --article]

> Thai-first drafting skill for formal reports and readable articles. This skill is designed to be **Oracle-aligned**:
> - **MCP-first** retrieval (no Oracle HTTP APIs)
> - **Outline-first stop** (human control boundary)
> - **Session-specific style pack summary** (Option C lifecycle)
> - **Learn-back** delegated to [`writing-th-learn`](.roo/skills/writing-th-learn/SKILL.md)

## When to use

- When the user wants a Thai draft that must match a specific report/article voice.
- When the user provides an **example report** to mimic (terminology + section flow).

## When NOT to use

- If there is no writing goal yet (topic/objective/audience unknown).
- If the task is purely editing an existing Thai document without drafting.

---

## Modes

Exactly one mode flag:

- `--report` — รายงานทางการสำหรับหน่วยงานรัฐ/องค์กร (default if not specified)
- `--article` — บทความอ่านง่าย โครงสร้างชัด จังหวะเล่าเรื่อง

---

## Inputs (minimal handshake)

Ask only for what is missing:

1) **Writing plan path** (markdown) — anchor file where we append outline + session style pack summary.
2) **Example report path** (markdown; optional but recommended) — the style reference for this session.
3) **หัวข้อ + วัตถุประสงค์** — what are we writing and what decision/action should the reader take.
4) **ผู้อ่าน** — target audience.
5) **ความยาวเป้าหมาย** — pages/words.
6) **Constraints** — must-include / must-avoid / deadline.
7) **Ground-truth sources** — only these files/notes are allowed as factual basis.

---

## Writing plan template (recommended)

Use this structure in the writing plan file so `/writing-th` and `/writing-th-learn` can stay traceable and automation-friendly.

```
# Writing Plan — <topic>

## 0) Session metadata
- Date:
- Mode: report|article
- Audience:
- Target length:
- Deadline:

## 1) Ground-truth sources (allowed facts)
- <path>

## 2) Example report (style reference)
- Path: <path>
- Permission to use as style reference: yes|no
- Mimic scope: terminology + section flow (no verbatim copying)

## 3) Output targets
- Draft output folder:
- Filename base:

## 4) Session Style Pack Summary
<!-- append-only: one block per session -->

## 5) Outline approvals
<!-- append-only: outline versions + approvals -->

## 6) Draft/Edited mapping (if names do not conform)
- Draft: <path>
- Edited: <path>
```

Notes:

- Keep this plan **append-only** (Nothing is Deleted).
- The “Permission” line is the explicit guardrail for example-report usage.

---

## Style precedence (important)

This skill uses **layered style**, with two phases:

### Phase A — Before any project session style pack exists

1) **Example report (session reference)** — primary for terminology + section flow, within bounds of the layers below.
2) **Project style brief (if present)** — binding voice/tone/concept framing for this deliverable.
3) **Persistent resonance (safety rails)** — baseline constraints that must not be violated:
   - [`ψ/memory/resonance/writing-style-th.md`](ψ/memory/resonance/writing-style-th.md)
   - [`ψ/memory/resonance/citation-style-th.md`](ψ/memory/resonance/citation-style-th.md)
4) **Learnings tagged writing-th** — evolving patterns from previous projects/sessions.

### Phase B — After a project session style pack exists

1) **Example report (session reference)** — primary for terminology + section flow, **within the bounds of the layers below**.
2) **Project Session Style Pack file** — project-specific rules that crystallized from human-edited drafts and `/writing-th-learn` patterns (e.g., `plans/<project>-writing-style-pack.md`).
3) **Project style brief (if present)** — binding voice/tone/concept framing for the deliverable.
4) **Persistent resonance (safety rails)** — global constraints for writing and citations.
5) **Learnings tagged writing-th** — additional global patterns.

If example style conflicts with a project Session Style Pack, project style brief, or resonance, **the pack + brief + resonance win**.


---

## Guardrails (Oracle alignment)

### Permission + copying

- Confirm the example report is **permitted to be used as a style reference**.
- “Mimic” means: **terminology + section flow + rhetorical moves**, NOT verbatim sentence copying.
- If quoting is required, mark it clearly and cite properly.

### Grounding + citations

- **No invented sources**.
- Citations only from user-provided sources (or explicitly retrieved via MCP from `ψ/`).

### External vs internal artifacts

- Keep **DCCE/sponsor-facing prose** free from repo-internal links and internal scaffolding.
- If traceability/QA is needed, create a separate internal artifact (map/log) rather than embedding it in main prose.

---

## Workflow

### Step 0 — Decide mode

- If user does not specify: default to `--report`.

### Step 1 — Retrieve memory (MCP-first)

Hard rule: **no Oracle HTTP APIs**.

Use MCP tools to retrieve:

- Resonance:
  - [`ψ/memory/resonance/writing-style-th.md`](ψ/memory/resonance/writing-style-th.md)
  - [`ψ/memory/resonance/citation-style-th.md`](ψ/memory/resonance/citation-style-th.md)
- Learnings:
  - `ψ/memory/learnings/*writing-th*` and/or relevant tags for the selected mode.

Then read the user-provided example report file (path from the writing plan) to extract:

- preferred terminology (key nouns/verbs)
- section flow (ordering + headings style)
- paragraph rhythm (length, transitions)
- typical “summary blocks” vs narrative

### Step 2 — Session Style Pack handling

There are two cases:

1) **No project Session Style Pack yet (first drafting phase)**

- Do **not** create a Session Style Pack file yet.
- Use only:
  - resonance (writing-style-th + citation-style-th),
  - existing learnings tagged `writing-th`,
  - example report(s),
  - project style brief (ถ้ามี).
- Proceed to Step 3 (Outline) and Step 4 (Draft) using these layers.

2) **Project Session Style Pack exists**

- Load the Session Style Pack file referenced in the writing plan (เช่น `plans/<project>-writing-style-pack.md`).
- Append a new "Session Style Pack Summary" block into that file (append-only):

  ```markdown
  ## Session Style Pack Summary (YYYY-MM-DD HH:MM)

  ### Primary reference
  - Example report: <path>
  - Project style brief (if any): <path>

  ### Terminology (preferred)
  - ...

  ### Section flow
  - ...

  ### Voice + constraints (safety rails)
  - (from resonance + project brief)

  ### Citations
  - ...

  ### Placeholders
  - [ต้องเติมตัวเลข] / [ต้องเติมแหล่งอ้างอิง] ...

Notes:

- The summary is **session-scoped** and must not overwrite past summaries.


### Step 3 — Outline first, then STOP

Produce (at least) one numbered Thai outline (optionally 2 variants if structure choices exist):

- Variant A: closest to example flow
- Variant B: closest to plan/TOR flow (if different)

Append the chosen outline into the writing plan and **STOP** for explicit confirmation.

### Step 4 — Draft

After confirmation:

- Write the draft as a new file (no overwrite).
- Recommended naming:
  - `<topic-slug>-v1-draft.md`
  - If re-drafting: increment version (`v2`, `v3`, ...).


### Step 4b — Post-section sanity check (mechanical style validation)

After completing a substantial section (เช่น หัวข้อย่อยที่มีหมายเลข หรือหนึ่งบทเต็ม) ให้รัน **sanity check แบบเชิงกล** เปรียบเทียบร่างกับ writing style pack ที่ใช้งานอยู่ (resonance + project style brief ถ้ามี + Session Style Pack Summary):

หากข้อใดข้อหนึ่งไม่ผ่าน ให้แก้ไขส่วนดังกล่าวภายใต้ style pack เดียวกันก่อนจะนับว่าเป็นร่างที่พร้อมสำหรับให้มนุษย์ทบทวน

### Step 5 — Human edit handshake

Ask the user to:

- Copy the draft and create an edited version.
- Preferred naming pair for automation:
  - `...-draft.md`
  - `...-edited.md`

If the user wants different filenames, preserve originals and create a conforming copy pair (Nothing is Deleted).

### Step 6 — Learn-back (delegated)

If an edited version exists, invoke the learning-only companion:

- [`writing-th-learn`](.roo/skills/writing-th-learn/SKILL.md:1)

- [`writing-th-learn`](.roo/skills/writing-th-learn/SKILL.md)

Goal of learn-back:

- extract patterns in word choice + semantic arrangement
- store as `ψ/memory/learnings/YYYY-MM-DD_writing-th-<mode>-learn.md`

---

## /rrr integration (document-only, for now)

This redesign does **not** implement automatic detection in `/rrr` yet.

Intended future behavior:

- When `/rrr` runs, it may detect draft/edited pairs created in the session and invoke [`/writing-th-learn`](.roo/skills/writing-th-learn/SKILL.md).

Reason to keep this separate:

- Avoid coupling retrospective generation to writing-learning extraction until the naming/mapping rules are stable.

