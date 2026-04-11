---
name: writing-th-learn
description: learn a writing style from any articles, edits, notes, writt-up. Use when the human says 'learn from this note, report, write-up', study writing style or pattern. 
---

# /writing-th-learn

> Learning-only companion for `/writing-th`. Compares a **Thai draft** and its **human-edited** version then stores the changed as reusable patterns. Or study a writing style of a writing sample. 

## When to use this skill

- When you have any Thai draft/edited pair and want to update `writing-th`'s understanding of your word choice and phrasing.
- When you have a writing sample you want to capture its style


## Inputs required
1) a writing sample

## Inputs optional
1) **Draft file path**: markdown file.
2) **Edited file path**: markdown file.
3) (Optional) **Example report path**: the style reference used in the session (if any).
4) (Optional) **Context tags**: short tags for `oracle_learn` (e.g., `thai-tone`, `gov-report`, `interview-prep`).

### Naming rule (recommended, but not mandatory)

- Preferred: `...-draft.md` and `...-edited.md` pairing.
- If real files do not conform, proceed only if a clear mapping is recorded (Nothing is Deleted):
  - Add a small mapping block in the writing plan (recommended template is in [`/writing-th`](.roo/skills/writing-th/SKILL.md:1)).

## Workflow
To break down a writing style into a strict, rule-based system, you have to turn the writing into numbers, limits, and hard "yes/no" checks.

Here are the specific building blocks and patterns you must measure to create your rules:

1. Word Rules (Vocabulary)
Word Length: Count the syllables. Is the rule to stick mostly to 1-2 syllable words, or are longer words allowed?

Word Types: Do they rely on strong action verbs (e.g., "sprint," "crush") or do they pile on describing words (e.g., "very fast," "really bad")?

Jargon and Slang: Make a strict list of phrases they use all the time.

The "Never Use" List: Just as important as what they say is what they refuse to say. Make a list of banned words.

2. Sentence Rules (Structure)
Sentence Length Limits: Find the average word count per sentence. Set a hard rule (like "no sentence over 15 words" or "always follow a long sentence with a 3-word sentence").

Sentence Openers: Track the first word of every sentence. Do they start with names? Do they start with words like "And," "But," or "Because"?

Action vs. Happening: Does the writer use active voice ("The cat ate the mouse") or passive voice ("The mouse was eaten by the cat")? Set a rule for which one to use.

3. Punctuation and Layout Rules
Paragraph Size: Count the sentences per paragraph. Set a strict limit (e.g., "Maximum of three sentences per paragraph").

Punctuation Quotas: Track the commas, dashes, and semicolons. A rule might be "Never use semicolons, but use dashes to interrupt thoughts."

Questions vs. Statements: How often do they ask the reader a question? Set a ratio (e.g., "One question per page").

4. Point of View Rules
The Subject: Who is the focus? Set a rule on whether to use "I" (personal), "You" (talking to the reader), or "They/It" (distanced and objective).

Certainty: Does the writer sound like an expert ("This is the only way") or a thinker ("It seems like this might work")?

5. **Write learning note to ψ/memory**

    - Compose a learning note in Thai (with English only where necessary) with sections (optional):
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


8) **Optional promotion to resonance (with explicit human approval)**

- Useได้เมื่อ:
+  - pattern เดิม (เช่น วิธีตั้งประโยค วิธีจัดลำดับบริบท → ประเด็นหลัก → นัยเชิงยุทธศาสตร์) ปรากฏซ้ำใน **อย่างน้อย 2 session** และ
+  - คุณในฐานะมนุษย์ตัดสินใจแล้วว่าอยากให้ pattern นั้นกลายเป็น “กติกาถาวร” ของการเขียน (ไม่ใช่แค่ preference ชั่วคราวของโปรเจกต์เดียว)

- ขั้นตอน:
+  1. เปิด learning note ล่าสุดที่เกี่ยวข้อง (ใน `ψ/memory/learnings/YYYY-MM-DD_writing-th-<mode>-learn.md`) และเลือกเฉพาะ pattern ที่ควรโปรโมต
+  2. สร้างบล็อกข้อความสั้น ๆ ในรูปแบบ:
+     ```markdown
+     ## YYYY-MM-DD — promoted from writing-th-learn (mode: report/article)
+
+     - บรรยาย pattern เชิงกติกาแบบสั้น กระชับ และทั่วไปพอใช้ได้ข้ามโปรเจกต์
+     - ระบุว่าเรียนรู้จาก draft/edited คู่ใด (ลิงก์ path แบบย่อ)
+     ```
+  3. เพิ่มบล็อกนี้แบบ append-only ลงใน
+     - [`ψ/memory/resonance/writing-style-th.md`](ψ/memory/resonance/writing-style-th.md)
+     - หรือ [`ψ/memory/resonance/citation-style-th.md`](ψ/memory/resonance/citation-style-th.md) ถ้าเป็นเรื่อง citation โดยเฉพาะ
+
+- Guardrail:
+  - ห้ามลบบรรทัดเก่าใน resonance (Nothing is Deleted)
+  - ต้องมี “เหตุผล” ที่ชัดเจนว่าทำไม pattern นี้จึงควรใช้ข้ามโปรเจกต์ ไม่ใช่ข้อยกเว้นเฉพาะกรณี
+  - การตัดสินใจโปรโมตยังคงต้องอาศัยการยืนยันของมนุษย์ ไม่ใช่ agent ตัดสินใจเองลำพัง
