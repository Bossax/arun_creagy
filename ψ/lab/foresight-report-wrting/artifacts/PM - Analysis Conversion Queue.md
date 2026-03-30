# PM - Analysis Conversion Queue

Purpose:
- ใช้เป็นสะพานจาก raw source files ไปสู่ “report-ready analysis”
- ป้องกันไม่ให้ทีมกระโดดจาก source summary ไปเขียน prose ทันทีโดยยังไม่ผ่านขั้นสังเคราะห์

---

## 1) Conversion workflow

### Layer A — Raw source
ไฟล์ต้นทางที่มีข้อมูลดิบ/บันทึก/ผลประชุม/research memo

Examples:
- [`base_report.md`](ψ/lab/foresight-report-wrting/artifacts/base_report.md)
- [`Source mapping.md`](ψ/lab/foresight-report-wrting/artifacts/Source%20mapping.md)
- [`Evidence collection to support the final draft of the report.md`](ψ/lab/foresight-report-wrting/artifacts/Evidence%20collection%20to%20support%20the%20final%20draft%20of%20the%20report.md)
- [`Analysis and actor assignment.md`](ψ/lab/foresight-report-wrting/artifacts/Analysis%20and%20actor%20assignment.md)
- [`Four scenario narratives (year 2047).md`](ψ/lab/foresight-report-wrting/artifacts/Four%20scenario%20narratives%20%28year%202047%29.md)

### Layer B — Evidence card
รูปแบบสั้นที่ตอบให้ได้ว่า source นี้ใช้รองรับ “claim ไหน”

Template:

```md
## Evidence Card — [ID]
- Source file:
- Source type: meeting note | synthesis memo | scenario narrative | legal research | field note
- Key usable claims:
  -
  -
- Relevant chapter sections:
  -
- Limitations / caveats:
  -
```

### Layer C — Analysis note
สังเคราะห์หลาย evidence cards ให้กลายเป็นข้ออธิบายพร้อมเขียน

Template:

```md
## Analysis Note — [topic]
- Question this note answers:
- Synthesis:
  -
- Implication for report:
  - Chapter:
  - Section:
- Still missing:
  -
```

### Layer D — Report-ready block
ย่อหน้า ตาราง หรือ bullet set ที่พร้อมย้ายเข้า draft

Rule:
- จะสร้าง report-ready block ได้ก็ต่อเมื่อมี evidence card รองรับ และ analysis note ที่ตอบคำถามของ section นั้นแล้ว

---

## 2) Queue by report chapter

### Queue A — Background and framing
Goal: เติมบท 1 ให้ไม่เป็น generic foresight prose

Needed analysis notes:
- A1. ทำไมต้องมอง 20 ปี ในบริบทชายแดนใต้
- A2. เด็กกำพร้า/เด็กเปราะบางในพื้นที่เป็น strategic issue อย่างไร
- A3. บริบทมลายู พหุวัฒนธรรม และความสัมพันธ์กับการศึกษา/เศรษฐกิจ

### Queue B — Present conditions and drivers
Goal: ทำบท 2 ให้เป็น evidence-backed reality map ไม่ใช่ list of notes

Needed analysis notes:
- B1. baseline การศึกษาและการเข้าถึงโอกาส
- B2. baseline สวัสดิการ/เส้นทางเด็กกำพร้า
- B3. drivers ทางเศรษฐกิจสร้างสรรค์และฮาลาล
- B4. role ของ actors / networks ในพื้นที่
- B5. weak signals ที่ควรเฝ้าระวัง

### Queue C — Scenario package
Goal: ทำบท 3 ให้มี logic + descriptors + narratives อยู่ในระบบเดียวกัน

Needed analysis notes:
- C1. rationale ของแกน `การศึกษา` x `เศรษฐกิจ`
- C2. descriptor matrix ของ 4 quadrants
- C3. baseline future narrative
- C4. preferable future narrative
- C5. trigger events / turning points ของแต่ละฉาก

### Queue D — Strategy package
Goal: ทำบท 4 ให้ขยับจาก “ข้อเสนอเชิงฝัน” ไปสู่ “execution architecture”

Needed analysis notes:
- D1. leverage point rationale
- D2. actor map และบทบาท
- D3. H1/H2/H3 per strategy
- D4. robustness test across scenarios
- D5. portfolio of actions + quick wins

### Queue E — Policy packaging
Goal: ทำบท 5 ให้สรุปได้จริงและไม่ generic

Needed analysis notes:
- E1. policy implications for state actors
- E2. implications for field actors / CSOs / local leaders
- E3. cross-cutting insight on trust, youth agency, and plural education

---

## 3) Recommended minimum PM bundle before drafting resumes

Drafting should resume only after the team has at least:
- 1 source ledger
- 8–12 evidence cards
- 5–8 analysis notes
- 1 descriptor matrix for chapter 3
- 1 strategy build sheet for chapter 4

If these are absent, continue analysis work first.

