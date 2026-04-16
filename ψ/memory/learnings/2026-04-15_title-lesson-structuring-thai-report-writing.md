---
title: ---
tags: []
created: 2026-04-15
source: ψ/memory/learnings/2026-03-24_rrr_writing-th-learn-crdb-edit-session.md
---

# ---

---
title: Lesson: Structuring Thai report-writing learn-back
status: superseded
superseded_by: 2026-03-28_lesson-writing-th-option-c-skill-redesign-oracle.md
---

## Lesson: Structuring Thai report-writing learn-back

- **Decouple drafting from learning**: ใช้ `/writing-th` สำหรับออกแบบโครงและเขียนร่าง ใช้ `/writing-th-learn` สำหรับเปรียบเทียบร่างกับฉบับแก้ไขและสกัด pattern การเขียน แทนที่จะพยายามทำทุกอย่างในสกิลเดียว.
- **Reuse human pattern notes**: หากมีไฟล์วิเคราะห์การแก้ไขที่มนุษย์เขียนไว้แล้ว (เช่น Chapter1-edit-pattern-analysis) ให้ treat เป็น “diff ที่มีการตีความแล้ว” ใช้เป็นฐานในการเขียน learnings แทน diff ดิบ เพื่อเน้น pattern มากกว่ารายละเอียดระดับบรรทัด.
- **Standardize filenames for automation**: การกำหนด pattern ของชื่อไฟล์ (`-draft.md` / `-edited.md` และ `YYYY-MM-DD_writing-th-<mode>-learn.md`) ทำให้สกิลอย่าง `/writing-th-learn` และ `/rrr` สามารถสแกนหาและเชื่อมต่อ loop การเรียนรู้ได้อัตโนมัติมากขึ้น.
- **Store only distilled rules in Oracle**: ข้อมูลที่ส่งเข้า `oracle_learn` ควรเป็น “กติกา/แนวโน้มการเขียน” ไม่ใช่ข้อความจากรายงานโดยตรง เพื่อให้ความรู้ที่เก็บไว้มีความยั่งยืนและไม่ผื่อกับบริบทเดียว.

---
*Added via Oracle Learn*
