# PM - Evidence Spine

Purpose:
- ใช้เป็นแกนกลางสำหรับเชื่อม `source -> evidence -> analysis -> chapter section`
- ลดปัญหาที่ข้อมูลมีอยู่หลายไฟล์ แต่ยังไม่ถูกแปลงเป็น “ข้ออธิบายที่พร้อมเขียนรายงาน”

How to use:
1. อ่าน section เป้าหมายในรายงานจาก [`base_report.md`](ψ/lab/foresight-report-wrting/artifacts/base_report.md)
2. ระบุไฟล์ต้นทางที่มีข้อมูลเกี่ยวข้อง
3. แยกให้ชัดว่าอะไรคือ evidence เชิงพรรณนา อะไรคือ analysis และอะไรคือ strategic implication
4. ถ้ายังไม่มีหลักฐานพอ ให้ใส่ “Gap” และห้ามเลื่อนเป็น draft-ready

---

## 1) Canonical writing spine

| Chapter / section | Narrative job in the report | Current state in [`base_report.md`](ψ/lab/foresight-report-wrting/artifacts/base_report.md) | Main supporting files already present | Evidence / analysis gap | Required output artifact |
|---|---|---|---|---|---|
| 1.1 ที่มาและความสำคัญ | วางเหตุผลว่าทำไมต้องมอง 20 ปี และทำไมเด็ก/เยาวชนในชายแดนใต้คือโจทย์เชิงยุทธศาสตร์ | โครงสร้างมี แต่ยังเป็นหัวข้อเปล่าและคำอธิบายกว้าง | [`Evidence collection to support the final draft of the report.md`](ψ/lab/foresight-report-wrting/artifacts/Evidence%20collection%20to%20support%20the%20final%20draft%20of%20the%20report.md), [`สาระสำคัญจากการประชุมกลุ่ม 5G เพื่อจัดทำรายงานฉบับสุดท้าย.md`](ψ/lab/foresight-report-wrting/artifacts/%E0%B8%AA%E0%B8%B2%E0%B8%A3%E0%B8%B0%E0%B8%AA%E0%B8%B3%E0%B8%84%E0%B8%B1%E0%B8%8D%E0%B8%88%E0%B8%B2%E0%B8%81%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%8A%E0%B8%B8%E0%B8%A1%E0%B8%81%E0%B8%A5%E0%B8%B8%E0%B9%88%E0%B8%A1%205G%20%E0%B9%80%E0%B8%9E%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%88%E0%B8%B1%E0%B8%94%E0%B8%97%E0%B8%B3%E0%B8%A3%E0%B8%B2%E0%B8%A2%E0%B8%87%E0%B8%B2%E0%B8%99%E0%B8%89%E0%B8%9A%E0%B8%B1%E0%B8%9A%E0%B8%AA%E0%B8%B8%E0%B8%94%E0%B8%97%E0%B9%89%E0%B8%B2%E0%B8%A2.md) | ยังขาด baseline ที่ชัดเกี่ยวกับเด็กกลุ่มเปราะบาง, การศึกษา, และเหตุผลเชิงนโยบายที่เกินกว่าบริบทความรุนแรง | 1-page context brief |
| 1.2 บริบทสังคมชายแดนใต้ | ทำให้ “ฉากหลัง” รองรับบท 2 โดยไม่ให้ความรุนแรงกลบเรื่องเด็ก | มีหัวข้อ แต่ยังไม่จัดระเบียบบริบท | [`Evidence collection to support the final draft of the report.md`](ψ/lab/foresight-report-wrting/artifacts/Evidence%20collection%20to%20support%20the%20final%20draft%20of%20the%20report.md) | ยังขาดการจัดหมวดบริบท: มลายู, โครงสร้างประชากร, การศึกษา, เศรษฐกิจใหม่, เครือข่ายพื้นที่ | Context evidence pack |
| 2.1 การกวาดสัญญาณ | อธิบายวิธีได้มาซึ่งสัญญาณให้ traceable | มีคำอธิบายเบื้องต้น + ลิงก์ตารางภายนอก | [`base_report.md`](ψ/lab/foresight-report-wrting/artifacts/base_report.md) | ยังขาด signal inventory ในไฟล์ภายใน repo และหลักฐานว่าใคร scan อะไร | Signal log + source ledger |
| 2.1.1 drivers / trends | แปลงสัญญาณเป็น drivers เชิงโครงสร้าง / พลวัต / emergent | มีเนื้อหาเริ่มต้น แต่ยังปะปน note กับ prose | [`Source mapping.md`](ψ/lab/foresight-report-wrting/artifacts/Source%20mapping.md), [`สาระสำคัญจากการประชุมกลุ่ม 5G เพื่อจัดทำรายงานฉบับสุดท้าย.md`](ψ/lab/foresight-report-wrting/artifacts/%E0%B8%AA%E0%B8%B2%E0%B8%A3%E0%B8%B0%E0%B8%AA%E0%B8%B3%E0%B8%84%E0%B8%B1%E0%B8%8D%E0%B8%88%E0%B8%B2%E0%B8%81%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%8A%E0%B8%B8%E0%B8%A1%E0%B8%81%E0%B8%A5%E0%B8%B8%E0%B9%88%E0%B8%A1%205G%20%E0%B9%80%E0%B8%9E%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%88%E0%B8%B1%E0%B8%94%E0%B8%97%E0%B8%B3%E0%B8%A3%E0%B8%B2%E0%B8%A2%E0%B8%87%E0%B8%B2%E0%B8%99%E0%B8%89%E0%B8%9A%E0%B8%B1%E0%B8%9A%E0%B8%AA%E0%B8%B8%E0%B8%94%E0%B8%97%E0%B9%89%E0%B8%B2%E0%B8%A2.md) | ยังขาด source-backed driver cards และความเชื่อมกับเด็ก/เยาวชนแบบ explicit | Driver cards |
| 2.1.2 ชีวิตเด็กและเยาวชนกลุ่มเป้าหมาย | ทำให้เห็น lived experience และเส้นทางชีวิตจริง | ตอนนี้เป็น list of asks / assigned names มากกว่า analysis | [`Evidence collection to support the final draft of the report.md`](ψ/lab/foresight-report-wrting/artifacts/Evidence%20collection%20to%20support%20the%20final%20draft%20of%20the%20report.md) | ยังขาด baseline เด็กกำพร้า, access to education, welfare journey, tech access, livelihood pathway | Youth reality pack |
| 2.1.3 wild cards | ระบุ low-probability high-impact events ที่ต้องใช้ stress test | มี draft prose เรื่อง flood disaster ค่อนข้างพร้อม | [`base_report.md`](ψ/lab/foresight-report-wrting/artifacts/base_report.md) | ต้องเติม source support และแยก direct / indirect / long-tail impacts | Wild card brief |
| 2.2 ผังระบบ | เปลี่ยนจาก note เชิง workshop ให้เป็นระบบที่อ่านแล้วใช้ต่อได้ | มีวงจรจำนวนมาก แต่ศูนย์กลางเดิมยังยึด “ความรุนแรง” | [`base_report.md`](ψ/lab/foresight-report-wrting/artifacts/base_report.md), [`Evidence collection to support the final draft of the report.md`](ψ/lab/foresight-report-wrting/artifacts/Evidence%20collection%20to%20support%20the%20final%20draft%20of%20the%20report.md) | ต้อง re-center ระบบไปที่คุณภาพชีวิตเยาวชน / การเรียนรู้ / โอกาสทางเศรษฐกิจ | System map narrative note |
| 3 scenario logic | อธิบายว่าทำไมเลือกแกนนี้ และแตกต่างกันอย่างไร | มี direction ใหม่ค่อนข้างชัดจาก education x creative economy | [`สาระสำคัญจากการประชุมกลุ่ม 5G เพื่อจัดทำรายงานฉบับสุดท้าย.md`](ψ/lab/foresight-report-wrting/artifacts/%E0%B8%AA%E0%B8%B2%E0%B8%A3%E0%B8%B0%E0%B8%AA%E0%B8%B3%E0%B8%84%E0%B8%B1%E0%B8%8D%E0%B8%88%E0%B8%B2%E0%B8%81%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%8A%E0%B8%B8%E0%B8%A1%E0%B8%81%E0%B8%A5%E0%B8%B8%E0%B9%88%E0%B8%A1%205G%20%E0%B9%80%E0%B8%9E%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%88%E0%B8%B1%E0%B8%94%E0%B8%97%E0%B8%B3%E0%B8%A3%E0%B8%B2%E0%B8%A2%E0%B8%87%E0%B8%B2%E0%B8%99%E0%B8%89%E0%B8%9A%E0%B8%B1%E0%B8%9A%E0%B8%AA%E0%B8%B8%E0%B8%94%E0%B8%97%E0%B9%89%E0%B8%B2%E0%B8%A2.md), [`Four scenario narratives (year 2047).md`](ψ/lab/foresight-report-wrting/artifacts/Four%20scenario%20narratives%20%28year%202047%29.md) | ยังขาด descriptor matrix และ linkage จาก drivers -> axes -> scenario consequences | Scenario logic sheet |
| 3 scenario narratives | ทำให้แต่ละ quadrant มีชีวิตและ policy meaning | มี 2047 narratives แล้ว แต่เป็น English draft และยังไม่ผูกกับ chapter descriptors แบบเต็ม | [`Four scenario narratives (year 2047).md`](ψ/lab/foresight-report-wrting/artifacts/Four%20scenario%20narratives%20%28year%202047%29.md) | ต้องแปลงเป็น Thai report-ready narrative + age-group impacts + indicators | Scenario narrative pack |
| 4 strategies / leverage points | เชื่อมจาก scenario -> strategy -> actors -> execution | มีชุด leverage point และ actor assignment ที่ดี | [`Analysis and actor assignment.md`](ψ/lab/foresight-report-wrting/artifacts/Analysis%20and%20actor%20assignment.md), [`Source mapping.md`](ψ/lab/foresight-report-wrting/artifacts/Source%20mapping.md) | ยังขาด chapter mapping, robustness test, H1/H2/H3 table ที่เขียนเสร็จจริง | Strategy build sheet |
| 4 portfolio / actors / early actions | ทำให้ข้อเสนอเป็น actionable และ assignable | มีแนวคิดกระจัดกระจายอยู่ในหลายไฟล์ | [`base_report.md`](ψ/lab/foresight-report-wrting/artifacts/base_report.md), [`Research prompts for final report.md`](ψ/lab/foresight-report-wrting/artifacts/Research%20prompts%20for%20final%20report.md) | ยังขาดตารางเจ้าภาพหลัก + quick wins + evidence of feasibility | Action portfolio board |
| 5 policy implications / conclusion | ขมวดเป็นข้อเสนอเชิงนโยบายที่แข็งแรง | มี generic scaffold แต่ยังไม่ผูกกับ evidence chain | [`base_report.md`](ψ/lab/foresight-report-wrting/artifacts/base_report.md) | ต้องมี synthesis note ที่ตอบว่า “so what” ต่อผู้กำหนดนโยบายและภาคสนาม | Policy synthesis memo |

---

## 2) Immediate evidence priorities

### Priority A — facts that unblock Chapter 1 and 2
- baseline การเข้าถึงการศึกษาของเด็ก/เยาวชนกลุ่มเปราะบางในพื้นที่
- baseline เส้นทางเด็กกำพร้าและการเข้าถึงสวัสดิการ
- ภาพรวมเศรษฐกิจใหม่ในพื้นที่ที่มากกว่า narrative เชิงหวัง
- map ของเครือข่าย actors ที่ทำงานจริงในพื้นที่

### Priority B — facts that make scenarios believable
- rationale ที่ชัดสำหรับแกน `การศึกษา` x `เศรษฐกิจ`
- descriptor matrix ของแต่ละฉากทัศน์
- turning points / triggers ที่ทำให้แต่ละ quadrant เกิดขึ้นได้จริง

### Priority C — facts that make strategy actionable
- evidence ว่า leverage point ใดทำได้จริงในเชิงกฎหมาย สถาบัน และ actor
- owner / broker / enabler ของแต่ละ action
- quick wins ที่มีทรัพยากรตั้งต้นรองรับ

---

## 3) Quality rule

ห้ามเลื่อน section ใดไปสู่ “draft-ready” หากยังไม่มีอย่างน้อย:
- source ที่ระบุได้ชัดว่าเอามาจากไหน
- note วิเคราะห์ที่แยกจาก raw source summary
- คำอธิบายว่า evidence ชิ้นนั้นรองรับ claim ไหนในรายงาน

