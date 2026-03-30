# Chapter 2 — Evidence Trace Ledger (Round 1)

Purpose:
- ใช้เป็น “บันทึกตรวจสอบย้อนกลับ (audit trail)” สำหรับบทที่ 2
- แยกออกจากร่างรายงานหลัก เพื่อคงกติกา **real sources only** ในเอกสาร sponsor-facing

Rules (hard):
- ในร่างบทที่ 2 ([`2026-03-29_ch2-round1-draft.md`](ψ/lab/foresight-report-wrting/artifacts/2026-03-29_ch2-round1-draft.md)) ห้ามอ้างอิงไฟล์ภายใน repo เป็นแหล่งอ้างอิงสุดท้าย
- Internal artifacts ใช้ได้เฉพาะใน ledger นี้ เพื่อชี้ว่า “ข้อความ/ตัวเลข” โผล่ครั้งแรกที่ไหน แล้วต้องไปผูกกับ “แหล่งจริง” ใด

Status legend:
- ✅ Ready: มีแหล่งจริงรองรับ พร้อมเอาไปอ้างในบท 2
- 🟡 Traceable: เห็นแหล่งจริงบางส่วน/เห็น URL แต่ยังต้องตรวจสอบว่า “รองรับ claim นี้จริง”
- ⛔ HOLD: ยังไม่มีแหล่งจริงที่ตรวจสอบย้อนกลับได้

---

## 1) Source register (real sources discovered so far)

> หมายเหตุ: รายการนี้เป็น “registry” ของแหล่งจริงที่พบแล้วจากภายใน workspace โดยยังไม่ยืนยันว่าแต่ละแหล่งรองรับ claim ไหนจนกว่าจะ map ใน Section 2

### 1.1 From [`วิถีทางเศรษฐกิจสำหรับเยาวชนในจังหวัดชายแดนภาคใต้ (พ.ศ. 2570–2590).md`](ψ/lab/foresight-report-wrting/artifacts/%E0%B8%A7%E0%B8%B4%E0%B8%96%E0%B8%B5%E0%B8%97%E0%B8%B2%E0%B8%87%E0%B9%80%E0%B8%A8%E0%B8%A3%E0%B8%A9%E0%B8%90%E0%B8%81%E0%B8%B4%E0%B8%88%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B9%80%E0%B8%A2%E0%B8%B2%E0%B8%A7%E0%B8%8A%E0%B8%99%E0%B9%83%E0%B8%99%E0%B8%88%E0%B8%B1%E0%B8%87%E0%B8%AB%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B8%8A%E0%B8%B2%E0%B8%A2%E0%B9%81%E0%B8%94%E0%B8%99%E0%B8%A0%E0%B8%B2%E0%B8%84%E0%B9%83%E0%B8%95%E0%B9%89%20%28%E0%B8%9E.%E0%B8%A8.%202570%E2%80%932590%29.md) (Works cited section)

- (A) สำนักงานสภาพัฒนาการเศรษฐกิจและสังคมแห่งชาติ (สศช.). รายงาน/Final report 2024 (PDF)
  - URL: https://www.nesdc.go.th/wordpress/wp-content/uploads/2025/09/Final-Report-2024_as-of-20250912.pdf
  - Status: 🟡 Traceable (ต้องเปิดดูหัวข้อ/หน้าเพื่อยืนยัน claim)

- (B) แผนพัฒนาจังหวัดนราธิวาส พ.ศ. 2566–2570 (PDF)
  - URL: https://www2.narathiwat.go.th/nara2016/files/com_news_develop_plan/2025-04_196e8f4bad94aaf.pdf
  - Status: 🟡 Traceable

- (C) แผนพัฒนาจังหวัดนราธิวาส พ.ศ. 2566–2570 (ฉบับทบทวน) (PDF)
  - URL: https://www2.narathiwat.go.th/nara2016/files/com_news_develop_plan/2023-01_09cea4479f3f3b8.pdf
  - Status: 🟡 Traceable

- (D) แผนพัฒนาจังหวัดปัตตานี พ.ศ. 2566 (page)
  - URL: http://www.pattani.go.th/news_devpro/showList?cid=17
  - Status: 🟡 Traceable

- (E) UNDP SDG profile จังหวัดยะลา (PDF)
  - URL: https://www.undp.org/sites/g/files/zskgke326/files/2024-11/sdg_profile_yala_thai.pdf
  - Status: 🟡 Traceable

- (F) UNICEF Thailand Annual Report 2021 (PDF)
  - URL: https://www.unicef.org/thailand/media/8571/file/UNICEF%20Thailand%20Annual%20Report%202021.pdf
  - Status: 🟡 Traceable

- (G) depa: Digital Workforce / Digital Skill Roadmap (page)
  - URL: https://www.depa.or.th/en/article-view/20240902_02
  - Status: 🟡 Traceable

- (H) CEA: Neramyth City (page)
  - URL: https://www.cea.or.th/en/single-project/Neramyth-City
  - Status: 🟡 Traceable

- (I) EEF/กสศ. ข่าว “รัฐบาลชู 6 งาน กสศ. … ชายแดนใต้” (page)
  - URL: https://www.eef.or.th/news-090123/
  - Status: 🟡 Traceable

- (J) The101 article (NEETs ใน นราธิวาส) (page)
  - URL: https://www.the101.world/neets-in-narathiwat/
  - Status: 🟡 Traceable

---

## 2) Claim → evidence mapping (Chapter 2)

> รูปแบบแนะนำ: 1 claim ต่อ 1 แถว เพื่อให้ตรวจสอบย้อนกลับง่าย และใช้เป็น checklist ก่อนย้าย claim เข้า “draft-ready prose”

| Claim ID | Claim (what we want to say in Ch2) | Where it appears internally (do not cite in main) | Real source (final cite in main) | Status | Notes / what to do next |
|---|---|---|---|---|---|
| C2-001 | วิธีอ่านบทนี้: นิยาม signals/drivers/uncertainties + STEEPV เพื่อช่วยให้ผู้อ่านอ่านบท 2 แบบ foresight | N/A (framework prose) | N/A | ✅ Ready | ไม่ใช่ข้อเท็จจริงเชิงตัวเลข (ไม่ต้อง cite) |
| C2-002 | ต้องยืนยัน “ตัวเลข baseline” ของกลุ่มเปราะบางใน 3 จชต. ก่อนสรุปเชิงนโยบาย | [`สถานการณ์พื้นฐานเด็กและเยาวชนกลุ่มเปราะบางในพื้นที่จังหวัดชายแดนภาคใต้.md`](ψ/lab/foresight-report-wrting/artifacts/%E0%B8%AA%E0%B8%96%E0%B8%B2%E0%B8%99%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%93%E0%B9%8C%E0%B8%9E%E0%B8%B7%E0%B9%89%E0%B8%99%E0%B8%90%E0%B8%B2%E0%B8%99%E0%B9%80%E0%B8%94%E0%B9%87%E0%B8%81%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B9%80%E0%B8%A2%E0%B8%B2%E0%B8%A7%E0%B8%8A%E0%B8%99%E0%B8%81%E0%B8%A5%E0%B8%B8%E0%B9%88%E0%B8%A1%E0%B9%80%E0%B8%9B%E0%B8%A3%E0%B8%B2%E0%B8%B0%E0%B8%9A%E0%B8%B2%E0%B8%87%E0%B9%83%E0%B8%99%E0%B8%9E%E0%B8%B7%E0%B9%89%E0%B8%99%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%88%E0%B8%B1%E0%B8%87%E0%B8%AB%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B8%8A%E0%B8%B2%E0%B8%A2%E0%B9%81%E0%B8%94%E0%B8%99%E0%B8%A0%E0%B8%B2%E0%B8%84%E0%B9%83%E0%B8%95%E0%B9%89.md) | [ต้องเติมแหล่งอ้างอิง] | ⛔ HOLD | ตารางในไฟล์มีช่องแหล่งข้อมูลว่าง → ต้องย้อนหา dataset/report ที่ตัวเลขมาจริง |
| C2-003 | เส้นทางการเรียนรู้หลายแบบ (ในระบบ/ปอเนาะ/นอกระบบ/ออกจากระบบ) และช่องว่าง “การเชื่อมต่อ-การยอมรับ” | [`ข้อมูลจากดุลย์ - เก็บข้อมูลรายงานกลุ่ม 5G.md`](ψ/lab/foresight-report-wrting/artifacts/%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%B9%E0%B8%A5%E0%B8%88%E0%B8%B2%E0%B8%81%E0%B8%94%E0%B8%B8%E0%B8%A5%E0%B8%A2%E0%B9%8C%20-%20%E0%B9%80%E0%B8%81%E0%B9%87%E0%B8%9A%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%B9%E0%B8%A5%E0%B8%A3%E0%B8%B2%E0%B8%A2%E0%B8%87%E0%B8%B2%E0%B8%99%E0%B8%81%E0%B8%A5%E0%B8%B8%E0%B9%88%E0%B8%A1%205G.md) | [ต้องเติมแหล่งอ้างอิง] หรือใช้รูปแบบสัมภาษณ์ (ถ้าถือเป็นแหล่งจริง) | 🟡 Traceable | ต้องตัดสินใจเชิงกติกา: “สัมภาษณ์ภาคสนาม” ถือเป็นแหล่งจริงที่ cite ได้หรือไม่; หากได้ ต้องลงรูปแบบอ้างอิงสัมภาษณ์ตาม [citation-style-th.md](ψ/memory/resonance/citation-style-th.md) |
| C2-004 | ช่องว่างการเข้าถึงสิทธิในทางปฏิบัติ (เอกสารซับซ้อน/ไม่เข้าใจระบบ/ไม่ไว้วางใจ) | [`ข้อมูลจากดุลย์ - เก็บข้อมูลรายงานกลุ่ม 5G.md`](ψ/lab/foresight-report-wrting/artifacts/%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%B9%E0%B8%A5%E0%B8%88%E0%B8%B2%E0%B8%81%E0%B8%94%E0%B8%B8%E0%B8%A5%E0%B8%A2%E0%B9%8C%20-%20%E0%B9%80%E0%B8%81%E0%B9%87%E0%B8%9A%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%B9%E0%B8%A5%E0%B8%A3%E0%B8%B2%E0%B8%A2%E0%B8%87%E0%B8%B2%E0%B8%99%E0%B8%81%E0%B8%A5%E0%B8%B8%E0%B9%88%E0%B8%A1%205G.md) | [ต้องเติมแหล่งอ้างอิง] | 🟡 Traceable | เช่นเดียวกับ C2-003: ถ้า cite interview ได้ จะกลายเป็น ✅; ถ้าไม่ได้ ต้องหาแหล่งงานวิจัย/รายงานที่ยืนยัน |
| C2-005 | “ระบบการศึกษาเปิดช่องทางเลือกในกฎหมาย (ม.12) แต่การ scale ในทางปฏิบัติยังไม่ชัด” | [`Evidence Pack - Education Governance and Legal Feasibility.md`](ψ/lab/foresight-report-wrting/artifacts/Evidence%20Pack%20-%20Education%20Governance%20and%20Legal%20Feasibility.md) | ข้อกฎหมายจริง: พ.ร.บ.การศึกษาแห่งชาติ พ.ศ. 2542 มาตรา 12; พ.ร.บ.พื้นที่นวัตกรรมการศึกษา พ.ศ. 2562; ฯลฯ | 🟡 Traceable | ต้องเพิ่ม “ตัวบท/เอกสารทางการ” เป็นรายการอ้างอิงจริง (URL/ราชกิจจานุเบกษา) |

---

## 3) Immediate trace-back tasks (to unlock grounded drafting)

1) ปิดช่องว่างตัวเลข baseline:
- เปิดไฟล์ [`สถานการณ์พื้นฐานเด็กและเยาวชนกลุ่มเปราะบางในพื้นที่จังหวัดชายแดนภาคใต้.md`](ψ/lab/foresight-report-wrting/artifacts/%E0%B8%AA%E0%B8%96%E0%B8%B2%E0%B8%99%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%93%E0%B9%8C%E0%B8%9E%E0%B8%B7%E0%B9%89%E0%B8%99%E0%B8%90%E0%B8%B2%E0%B8%99%E0%B9%80%E0%B8%94%E0%B9%87%E0%B8%81%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B9%80%E0%B8%A2%E0%B8%B2%E0%B8%A7%E0%B8%8A%E0%B8%99%E0%B8%81%E0%B8%A5%E0%B8%B8%E0%B9%88%E0%B8%A1%E0%B9%80%E0%B8%9B%E0%B8%A3%E0%B8%B2%E0%B8%B0%E0%B8%9A%E0%B8%B2%E0%B8%87%E0%B9%83%E0%B8%99%E0%B8%9E%E0%B8%B7%E0%B9%89%E0%B8%99%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%88%E0%B8%B1%E0%B8%87%E0%B8%AB%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B8%8A%E0%B8%B2%E0%B8%A2%E0%B9%81%E0%B8%94%E0%B8%99%E0%B8%A0%E0%B8%B2%E0%B8%84%E0%B9%83%E0%B8%95%E0%B9%89.md`](ψ/lab/foresight-report-wrting/artifacts/%E0%B8%AA%E0%B8%96%E0%B8%B2%E0%B8%99%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%93%E0%B9%8C%E0%B8%9E%E0%B8%B7%E0%B9%89%E0%B8%99%E0%B8%90%E0%B8%B2%E0%B8%99%E0%B9%80%E0%B8%94%E0%B9%87%E0%B8%81%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B9%80%E0%B8%A2%E0%B8%B2%E0%B8%A7%E0%B8%8A%E0%B8%99%E0%B8%81%E0%B8%A5%E0%B8%B8%E0%B9%88%E0%B8%A1%E0%B9%80%E0%B8%9B%E0%B8%A3%E0%B8%B2%E0%B8%B0%E0%B8%9A%E0%B8%B2%E0%B8%87%E0%B9%83%E0%B8%99%E0%B8%9E%E0%B8%B7%E0%B9%89%E0%B8%99%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%88%E0%B8%B1%E0%B8%87%E0%B8%AB%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B8%8A%E0%B8%B2%E0%B8%A2%E0%B9%81%E0%B8%94%E0%B8%99%E0%B8%A0%E0%B8%B2%E0%B8%84%E0%B9%83%E0%B8%95%E0%B9%89.md) แล้วสกัด “ตัวเลขแต่ละแถว” → สร้างรายการแหล่งจริงที่รองรับ (NSO/UNICEF/EEF/กระทรวงฯ ฯลฯ)

2) ตัดสินใจกติกา “ภาคสนาม/สัมภาษณ์”:
- ถ้าอนุญาตให้ cite เป็นแหล่งจริง → แปลงเป็นรายการอ้างอิงสัมภาษณ์ตาม [citation-style-th.md](ψ/memory/resonance/citation-style-th.md)
- ถ้าไม่อนุญาต → ใช้สัมภาษณ์เป็น narrative signal และหาแหล่งรายงาน/งานวิจัยรองรับเชิงระบบ

3) ปิดช่องว่างกฎหมาย:
- เพิ่ม URL/รายการอ้างอิงตัวบทกฎหมายและเอกสารทางการ (ราชกิจจานุเบกษา/เว็บไซต์หน่วยงาน)

