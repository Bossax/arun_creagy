---
title: # Learning — Foresight v4 edit discipline and style pack enforcement
tags: [foresight, thai-writing, style-pack, editing-discipline, translationese, metaphor-control]
created: 2026-04-15
source: ψ/memory/learnings/2026-04-05_foresight-v4-edit-discipline-and-style-pack-enforcement.md
---

# # Learning — Foresight v4 edit discipline and style pack enforcement

# Learning — Foresight v4 edit discipline and style pack enforcement

## Context
- Project: Arun_Creagy (foresight report on children and youth in Thailand’s Southern Border Provinces)
- Date: 2026-04-05
- Trigger: Review and rewrite of sections 2.1.2–2.1.4 after human edits and inline comments highlighted awkward, unclear, or meta-language (เช่น ชี้โลก, จุดงอก, ช่องทางทบทวน, การสนทนาเชิงวิเคราะห์)

## Pattern Observed

1) **Style pack present but under-enforced**
- The writing style pack for the foresight report already defines strong principles:
  - Thai-first analytical prose (no translationese).
  - Child-/actor-first analysis.
  - Mechanism-first, concrete, system-aware writing.
- However, several problematic phrases slipped into v4 sections and internal spines:
  - ชี้โลก, จุดงอก, การขยับของเส้นทางการเรียนรู้
  - ภาระจริงสูงกว่ามาตรการจะรับรู้, ช่องทางทบทวน, ช่องทางอุทธรณ์ที่ปลอดภัย
  - เมตา–ภาษา เช่น สามแนวโน้มข้างต้น, การอ่านเชิงระบบ
- These patterns were not caused by missing rules but by **partial enforcement** and the absence of explicit anti-pattern examples.

2) **Internal scaffolding language leaks into final drafts**
- Synthesis spine files and outlines contained metaphorical shorthand:
  - "เด็กที่มีคนพาเดินระบบ" vs "เด็กที่ต้องเดินลำพัง"
  - "การอ่านเชิงระบบ" as a label for how to interpret signals
- Even though these were intended as internal prompts, they shaped the way I described mechanisms in the integrated draft, increasing the chance of vague or metaphor-heavy language in the final report.

3) **Human comment files are hard signals that must feed back into rules**
- Human editors wrote strong flags such as “what the heck is this?” next to phrases that felt unnatural or incoherent in Thai.
- Initially, I used these comments only to rewrite the local sentence, without feeding them back into the style pack as **codified anti-patterns**, which allowed similar structures to reoccur.

## What changed in this session

1) **Section 2.1.4 and 2.1.3 rewrites**
- 2.1.4 (สัญญาณอ่อน) and 2.1.3 (เหตุไม่คาดฝัน) were rewritten into standalone files:
  - `ψ/lab/foresight-report-wrting/2026-04-05_foresight-2590-section-2.1.4-rewrite-v5.md`
  - `ψ/lab/foresight-report-wrting/2026-04-05_foresight-2590-section-2.1.3-rewrite-v5.md`
- The rewrites:
  - Removed or replaced metaphorical/undefined labels (ชี้โลก, จุดงอก).
  - Replaced translationese phrases with natural Thai that still carry the same analytical meaning (เช่น ภาระจริงสูงกว่ามาตรการจะรับรู้ → เกณฑ์ช่วยเหลือไม่ครอบคลุมภาระจริงที่ครัวเรือนแบกรับอยู่).
  - Turned generic or meta language into mechanism-first sentences tied to actors and drivers.

2) **Style pack hardened with anti-pattern bullets**
- `plans/foresight-report-writing-style-pack.md` was updated under §1.1 with explicit anti-pattern examples:
  - Disallowing constructions like "ภาระจริงสูงกว่ามาตรการจะรับรู้".
  - Flagging shorthand metaphors like "ชี้โลก" and "จุดงอก" unless explicitly defined and tied to core frameworks.
  - Requiring expansion of compressed phrases like "ช่องทางทบทวน" into explicit, idiomatic policy Thai.

3) **Plan updates acknowledge internal-spine risk**
- Rewrite plans for 2.1.3 and 2.1.4 now explicitly treat comments from human editors as inputs to both the **local fix** and **style pack evolution**, closing the loop between line comments and global rules.

## Lessons

1) **Style packs need concrete “do not use” examples, not just principles**
- High-level rules (Thai-first, mechanism-first) are necessary but not sufficient for reliable enforcement.
- Adding a small list of anti-patterns drawn from real failures (phrases that humans already rejected) dramatically improves future checking by providing hooks for fast pattern recognition.

2) **Internal scaffolding must mostly obey the same language discipline as external prose**
- Synthesis spines and outlines are de facto prompts for drafting; metaphorical or vague language here almost guarantees similar vagueness in generated sections.
- Treating scaffolding as a place where “anything goes” is unsafe for a project that reuses those files as generative anchors.

3) **Human comments are global signals, not local annotations**
- When a human tags a phrase as incoherent or unnatural, that phrase should be:
  - Fixed locally **and**
  - Evaluated as a candidate anti-pattern to encode in the style pack.
- This turns one-off edits into reusable guardrails.

## Recommended tags / concepts
- concepts: ["foresight", "thai-writing", "style-pack", "editing-discipline", "translationese", "metaphor-control"]
- source: "rrr: Arun_Creagy"


---
*Added via Oracle Learn*
