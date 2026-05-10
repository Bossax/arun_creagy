# user_use_case_raw

## กลุ่มที่ 1 ข้อมูลทางเศรษฐศาตร์และการเงิน

- Agency: TBA (Thai Bankers' Association) / Commercial Banks
  - Use case: ทำ “การทดสอบภาวะวิกฤตด้านสภาพภูมิอากาศ (ICAAP/BoT stress test)” สำหรับพอร์ตสินเชื่อ โดยใช้ “แผนที่ความเสี่ยงน้ำท่วมแบบความน่าจะเป็นระดับสินทรัพย์ (asset-level probabilistic flood maps)” (รวมความลึก/ระยะเวลาน้ำท่วม) ร่วมกับ “damage functions มาตรฐาน” เพื่อคำนวณความเสี่ยง/ความเสียหายทางการเงิน และประเมินผลกระทบลูกโซ่ (เช่น การหยุดชะงักซัพพลายเชน)
  - Goal: ประเมิน/หาปริมาณ (quantify) ความเสี่ยงกายภาพและความสูญเสียทางการเงินของพอร์ตสินเชื่อให้สอดคล้องกรอบการวิเคราะห์ความเสี่ยงกายภาพของ BoT
  - Required data/products: แผนที่น้ำท่วมแบบความน่าจะเป็นระดับตำแหน่ง/สินทรัพย์ (ระบุชนิดน้ำท่วม pluvial/riverine/coastal); เมตริกความลึกและระยะเวลาน้ำท่วม (depth/duration); damage functions ที่ใช้ได้กับการประเมินเชิงการเงินระดับสินทรัพย์; ข้อมูล/กรอบสำหรับเชื่อม “ความเสี่ยงกายภาพ → ผลกระทบลูกโซ่/ซัพพลายเชน” เพื่อใช้ประกอบคำแนะนำลูกค้าองค์กร
  - Source anchors: [`Interview Summary - Thai Bankers' Association.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20Thai%20Bankers'%20Association.md:48), [`Interview Summary - Thai Bankers' Association.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20Thai%20Bankers'%20Association.md:26), [`Interview Summary - Thai Bankers' Association.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20Thai%20Bankers'%20Association.md:28), [`Interview Summary - Thai Bankers' Association.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20Thai%20Bankers'%20Association.md:33)

- Agency: TBA (Thai Bankers' Association) / Commercial Banks
  - Use case: วิเคราะห์ “การเปิดรับความเสี่ยงน้ำท่วมของพอร์ตสินทรัพย์/หลักประกัน” เพื่อรองรับกรอบ “BoT physical risk analysis” โดยต้องใช้ข้อมูลความเสี่ยงระดับสินทรัพย์ (ไม่ใช่ระดับจังหวัด) และ “แผนที่ความน่าจะเป็น” มากกว่าแผนที่ดัชนีแบบหยาบ
  - Goal: ทำให้แบบจำลองความเสี่ยง/การเงินของธนาคารสามารถสะท้อนความเสี่ยงเชิงพื้นที่ได้ละเอียดพอสำหรับการตัดสินใจและการรายงาน
  - Required data/products: ข้อมูล/แผนที่น้ำท่วมระดับตำแหน่งที่ให้ความน่าจะเป็นของการเกิดน้ำท่วม ณ จุด (probability at specific locations); แผนที่/ข้อมูลติดตามน้ำท่วมหลายรูปแบบ (pluvial/riverine/coastal); สเปกความละเอียด/การใช้งานที่ชัดเจนเพื่อหลีกเลี่ยงการสรุปแบบระดับจังหวัด
  - Source anchors: [`Interview Summary - Thai Bankers' Association.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20Thai%20Bankers'%20Association.md:17), [`Interview Summary - Thai Bankers' Association.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20Thai%20Bankers'%20Association.md:26)

- Agency: TBA (Thai Bankers' Association) / Commercial Banks
  - Use case: ประเมินความเสี่ยงการเปลี่ยนผ่าน (transition risk) ของพอร์ตธุรกิจ โดยต้อง “เชื่อม/แปล” ข้อมูลเส้นทาง LT-LEDS เชิงตัวเลขลงถึงระดับสาขาย่อย (sub-sector) และทำ mapping จากรหัส ISIC ไปสู่การประกอบกิจการจริงในประเทศ เพื่อจัดกลุ่ม/ประเมินความเสี่ยงของลูกหนี้ได้ถูกต้อง
  - Goal: ทำให้การประเมิน transition risk ของธนาคารมีตัวเลขอ้างอิงและการจำแนกกิจการที่สอดคล้องกับความเป็นจริงในประเทศ
  - Required data/products: เส้นทาง LT-LEDS เชิงตัวเลขที่แตกย่อยถึงระดับ sub-sector; ตาราง mapping ISIC → กิจการ/การดำเนินงานจริงในประเทศ (domestic operations); แนวทางการใช้งานสำหรับการจัดกลุ่มพอร์ตและการประเมินความเสี่ยง
  - Source anchors: [`Interview Summary - Thai Bankers' Association.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20Thai%20Bankers'%20Association.md:35)

- Agency: NESDC (Office of the National Economic and Social Development Council / สภาพัฒน์)
  - Use case: ช่องว่างระหว่าง “เงินเยียวยา” กับ “ความสูญเสียทางเศรษฐกิจที่แท้จริง” — แยกแยะ “เงินเยียวยา/ชดเชย” ออกจาก “ความสูญเสียทางเศรษฐกิจที่แท้จริง” เพื่อคำนวณ Loss and Damage ทางเศรษฐกิจอย่างเป็นระบบ
  - Goal: แก้ pain point ที่ข้อมูลของ DDPM สะท้อนเพียง “ยอดเงินชดเชยจากรัฐ” แต่ไม่ครอบคลุมความเสียหายทางเศรษฐกิจที่แท้จริง (เช่น วันสูญเสียโอกาสทางธุรกิจ การหยุดชะงักด้านโลจิสติกส์)
  - Required data/products: ระบบ/กรอบวิธีการมาตรฐานสำหรับคำนวณ Loss and Damage ทางเศรษฐกิจ; ชุดข้อมูลความสูญเสียจากภัยพิบัติที่มากกว่า “ยอดเงินชดเชย” (ความเสียหายโดยตรง + ความสูญเสียทางอ้อม/การหยุดชะงักทางธุรกิจ/ต้นทุนโอกาส + ผลกระทบลูกโซ่ด้านโลจิสติกส์)
  - Source anchors: [`Interview Summary - NESDC.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NESDC.md:45), [`Interview Summary - NESDC.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NESDC.md:56)

- Agency: NESDC (Office of the National Economic and Social Development Council / สภาพัฒน์)
  - Use case: คำนวณ “ความสูญเสียทางเศรษฐกิจมหภาคที่แท้จริง” (ความเสียหายสินทรัพย์โดยตรง + การหยุดชะงักทางธุรกิจ/ต้นทุนโอกาส) จากน้ำท่วมครั้งใหญ่ในพื้นที่เศรษฐกิจสำคัญ เพื่อปรับประมาณการ GDP รายไตรมาส และใช้ประกอบการอนุมัติเงินกู้/โครงการโครงสร้างพื้นฐานในอนาคต
  - Goal: ใช้ค่าประมาณความสูญเสียทางเศรษฐกิจมหภาคที่แท้จริงในการปรับประมาณการ GDP รายไตรมาส และสนับสนุนเหตุผลในการอนุมัติเงินกู้/โครงการโครงสร้างพื้นฐานในอนาคต
  - Required data/products: ข้อมูลผลกระทบน้ำท่วมระดับเหตุการณ์ (event-level) สำหรับพื้นที่เศรษฐกิจสำคัญ; ค่าประมาณความเสียหายสินทรัพย์โดยตรง; ค่าประมาณความสูญเสียจากการหยุดชะงักทางธุรกิจ/ต้นทุนโอกาส; สมมติฐาน/การเชื่อมโยงตัวแปรที่นำไปใช้ในแบบจำลองเศรษฐกิจมหภาคได้
  - Source anchors: [`Interview Summary - NESDC.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NESDC.md:58)

- Agency: NESDC (Office of the National Economic and Social Development Council / สภาพัฒน์)
  - Use case: คาดการณ์ผลกระทบทางเศรษฐกิจจากภัยแล้ง โดยใช้ข้อมูลฐาน (baseline) เช่น ผลผลิตพืชผล การใช้น้ำ และระดับน้ำในอ่างเก็บน้ำ เพื่อสนับสนุนการวิเคราะห์เศรษฐกิจมหภาค
  - Goal: คาดการณ์ผลกระทบทางเศรษฐกิจจากภัยแล้งในมุมมองเศรษฐกิจมหภาค
  - Required data/products: ข้อมูลฐานจากกระทรวงเกษตรฯ (ผลผลิตพืชผล การใช้น้ำ); ข้อมูลฐานจากกระทรวงทรัพยากรธรรมชาติฯ (ระดับน้ำในอ่างเก็บน้ำ)
  - Source anchors: [`Interview Summary - NESDC.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NESDC.md:36)

- Agency: NESDC (Office of the National Economic and Social Development Council / สภาพัฒน์)
  - Use case: “การประเมินความเสี่ยงสภาพภูมิอากาศต่อโครงสร้างพื้นฐาน” — ใช้อัตราคิดลดมาตรฐาน 7% เพื่อสะท้อนความเสี่ยงจากการเปลี่ยนแปลงสภาพภูมิอากาศ การระบาดของโรค และความไม่แน่นอนในอนาคต ในการประเมินเงินกู้/โครงการโครงสร้างพื้นฐานขนาดใหญ่
  - Goal: ทำให้การลงทุนโครงสร้างพื้นฐานขนาดใหญ่มีความคุ้มค่าทางเศรษฐกิจ ภายใต้ความเสี่ยงสภาพภูมิอากาศและความไม่แน่นอนในอนาคต
  - Required data/products: ข้อมูล/ตัวแปรความเสี่ยงสภาพภูมิอากาศที่นำไปใช้ในการประเมินเศรษฐศาสตร์โครงการโครงสร้างพื้นฐานได้; สมมติฐาน/พารามิเตอร์สำหรับการคิดลด (รวมความเสี่ยงโรคระบาดและความไม่แน่นอนในอนาคต)
  - Source anchors: [`Interview Summary - NESDC.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NESDC.md:29)

- Agency: DDPM (Department of Disaster Prevention and Mitigation)
  - Use case: ประเมิน “ความสูญเสียทางเศรษฐกิจ” จากความเสียหายทางกายภาพด้วยวิธี proxy (เช่น “ต้นทุนต่อกิโลเมตรถนน”) เพื่อใช้ประเมินความเสียหายจากภัยพิบัติ (แนวทาง PDNA ที่เคยทดลอง)
  - Goal: แปลง “ข้อมูลความเสียหายเชิงกายภาพ” ให้เป็น “มูลค่าความสูญเสียทางเศรษฐกิจ” ที่นำไปใช้ตัดสินใจ/รายงานได้
  - Required data/products: ตาราง proxy value/ต้นทุนมาตรฐานรายประเภทสินทรัพย์ (เช่น ถนน อาคาร ปศุสัตว์); ข้อมูลความเสียหายเชิงกายภาพรายเหตุการณ์/รายพื้นที่; แนวทางคำนวณที่ระบุข้อจำกัดของการประเมิน (โดยเฉพาะความสูญเสียทางอ้อม)
  - Source anchors: [`Interview Summary DDPM.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20DDPM.md:56)

- Agency: DDPM (Department of Disaster Prevention and Mitigation)
  - Use case: ประเมิน “ความสูญเสียทางเศรษฐกิจ (รวมความสูญเสียทางอ้อม)” จากภัยพิบัติ โดยต้องใช้ข้อมูลจากหลายหน่วยงานร่วมกัน แต่ติดขัดจากการเข้าถึง/เชื่อมโยงข้อมูลข้ามหน่วยงาน
  - Goal: ได้ค่าประมาณความสูญเสียทางเศรษฐกิจที่ครอบคลุมมากกว่า “ความเสียหายเชิงกายภาพ” เพื่อสนับสนุนการสรุปภาพรวม Loss and Damage
  - Required data/products: กลไกเชื่อมโยง/แลกเปลี่ยนข้อมูลข้ามหน่วยงาน (multi-agency data); ชุดข้อมูลเศรษฐกิจ/ภาคส่วนที่ใช้ประเมินความสูญเสียทางอ้อม; ระเบียบวิธีคำนวณที่รองรับ indirect loss
  - Source anchors: [`Interview Summary DDPM.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20DDPM.md:56)

- Agency: DLA (Department of Local Administration / สถ.)
  - Use case: เชื่อมโยง “ข้อมูลความเสี่ยงสภาพภูมิอากาศระดับท้องถิ่น” เข้ากับ “เทศบัญญัติรายจ่าย/งบประมาณประจำปีของเทศบาล (Annual Budget Ordinance)” เพื่อใช้เป็นเหตุผลเชิงหลักฐานในการอนุมัติ/จัดสรรงบสำหรับโครงการลดความเสี่ยงเชิงรุก และรองรับการใช้ “เงินสะสม” ได้อย่างถูกระเบียบ
  - Goal: ทำให้ อปท./เทศบาลสามารถใช้ข้อมูลความเสี่ยงเชิงพื้นที่เป็นหลักฐานประกอบการตั้งงบ/อนุมัติโครงการ และลดแรงเสียดทานด้านข้อจำกัดงบประมาณเมื่อเกิด/ก่อนเกิดภัย
  - Required data/products: ชั้นข้อมูล/ตัวชี้วัดความเสี่ยงเชิงพื้นที่ระดับเทศบาล/ตำบล; กลไกเชื่อมโยงความเสี่ยง→รายการโครงการ/กิจกรรม→งบประมาณ; ตัวอย่างแม่แบบ/แนวทางการเขียนคำชี้แจงงบประมาณที่อ้างอิงข้อมูลความเสี่ยง
  - Source anchors: [`Interview Summary - DLA.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DLA.md:52), [`Interview Summary - DLA.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DLA.md:68)

- Agency: DLA (Department of Local Administration / สถ.)
  - Use case: ประเมิน “ความคุ้มค่า/ผลตอบแทนการลงทุน (ROI) ของมาตรการหรือโครงการด้านสภาพภูมิอากาศ” (เช่น โครงการลดความเสี่ยง หรือโครงการลดการปล่อย GHG) เพื่อใช้ประกอบการอนุมัติงบประมาณและจัดลำดับความสำคัญของโครงการท้องถิ่น
  - Goal: ทำให้การตัดสินใจลงทุนด้านสภาพภูมิอากาศของ อปท. มีเหตุผลเชิงเศรษฐศาสตร์/ความคุ้มค่าและเปรียบเทียบทางเลือกได้
  - Required data/products: ตัวชี้วัด/เครื่องมือคำนวณต้นทุน-ประโยชน์/ROI ของมาตรการ (ลดความเสี่ยง/ลด GHG); ข้อมูลฐานความเสียหาย/ความเสี่ยง (baseline) และผลลัพธ์ที่คาดว่าจะลดลง; แบบฟอร์มสรุปผลที่ “เข้าใจง่าย” สำหรับประกอบการอนุมัติงบ
  - Source anchors: [`Interview Summary - DLA.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DLA.md:57), [`Interview Summary - DLA.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DLA.md:59)

- Agency: FTI (Federation of Thai Industries / สภาอุตสาหกรรมแห่งประเทศไทย)
  - Use case: ประเมินการปล่อยคาร์บอนของ SMEs (Scope 1 และ 2) “ก่อนและหลัง” ได้รับเงินกู้ เพื่อพิสูจน์การลดการปล่อยฯ ซึ่งธนาคารใช้เป็นเหตุผลกำหนดอัตรา “green loan”
  - Goal: พิสูจน์การลดการปล่อยก๊าซเรือนกระจกจากการสนับสนุนสินเชื่อสีเขียวของ SMEs และใช้ประกอบการกำหนดอัตราสินเชื่อ
  - Required data/products: ข้อมูล/ผลการประเมินการปล่อยคาร์บอนของ SMEs (Scope 1 และ 2) ก่อนและหลังได้รับเงินกู้; วิธีการ/มาตรฐานการคำนวณที่ยอมรับร่วมกันสำหรับการเปรียบเทียบก่อน–หลัง
  - Source anchors: [`Interview Summary - FTI.md:L18-L23`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20FTI.md:18)

- Agency: FTI (Federation of Thai Industries / สภาอุตสาหกรรมแห่งประเทศไทย)
  - Use case: จัดทำคู่มือ/แนวทางประเมินผลกระทบ (Impact Assessment Guidelines) เพื่อสอนธุรกิจและท้องถิ่นว่า “จะคำนวณผลกระทบทางการเงินจากภัยสภาพภูมิอากาศอย่างไร” (เช่น แปล “จำนวนวันน้ำท่วม” เป็น “ต้นทุนการหยุดชะงักทางธุรกิจ”)
  - Goal: ทำให้การคำนวณผลกระทบทางการเงินจากภัยสภาพภูมิอากาศของภาคธุรกิจและท้องถิ่นทำได้ถูกต้องและสม่ำเสมอ
  - Required data/products: คู่มือ/Manual และตัวอย่างวิธีคำนวณที่ชัดเจนสำหรับการประเมินผลกระทบทางการเงินจากภัยสภาพภูมิอากาศ (เช่น business interruption costs)
  - Source anchors: [`Interview Summary - FTI.md:L52-L55`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20FTI.md:52)

- Agency: FTI (Federation of Thai Industries / สภาอุตสาหกรรมแห่งประเทศไทย)
  - Use case: แปลผลคาดการณ์คลื่นความร้อนระดับ 10 ตารางกม. ให้เป็น “ต้นทุนการหยุดชะงักทางธุรกิจ” และ “การสูญเสียผลิตภาพแรงงาน” โดยตรง สำหรับสถานประกอบการภาคการผลิต
  - Goal: ทำให้ข้อมูลคาดการณ์ความร้อนสามารถนำไปใช้ประเมินผลกระทบทางเศรษฐกิจ/การดำเนินธุรกิจได้โดยตรง
  - Required data/products: ผลคาดการณ์คลื่นความร้อนระดับ 10 ตารางกม.; วิธี/โมเดลการแปลงผลคาดการณ์เป็นต้นทุนการหยุดชะงักทางธุรกิจและการสูญเสียผลิตภาพแรงงาน
  - Source anchors: [`Interview Summary - FTI.md:L63-L64`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20FTI.md:63)

- Agency: NSO (National Statistical Office)
  - Use case: ใช้บัญชีการท่องเที่ยวของกระทรวงการท่องเที่ยวและกีฬา (tourism accounts) เพื่อทำแบบจำลอง “ความสูญเสียทางเศรษฐกิจ”/ความเปราะบางทางเศรษฐกิจเชิงลึก (economic vulnerability) ตามข้อเสนอแนะของ NSO
  - Goal: ประเมินความเปราะบางทางเศรษฐกิจและความสูญเสียทางเศรษฐกิจจากความเสี่ยงสภาพภูมิอากาศด้วยข้อมูลเศรษฐกิจภาคการท่องเที่ยวที่ละเอียดขึ้น
  - Required data/products: ข้อมูลบัญชีการท่องเที่ยว (tourism accounts); วิธี/กรอบการนำข้อมูลบัญชีการท่องเที่ยวไปใช้ในแบบจำลองความสูญเสียทางเศรษฐกิจ/ความเปราะบางทางเศรษฐกิจ
  - Source anchors: [`Interview Summary - NSO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NSO.md:110)

## กลุ่มที่ 2 ข้อมูลสนับสนุนการวางแผนและนโยบายเชิงพื้นที่

- Agency: UDDC (Urban Design and Development Center)
  - Use case: ใช้แบบจำลองน้ำท่วมในอนาคตที่ downscale ระดับเมือง (ฉากทัศน์ SSP3/SSP5) ร่วมกับข้อมูล DEM ความละเอียด 1 เมตร เพื่อทำแผนที่พื้นที่น้ำท่วมในอนาคต และใช้เป็นฐานสำหรับการประเมินความเสี่ยง/ความเปราะบางระดับท้องถิ่น และการทำแผนเชิงพื้นที่ (เช่น spatial strategic plans, แผนป้องกันและบรรเทาสาธารณภัยท้องถิ่น)
  - Goal: สนับสนุนการวางแผนและการตัดสินใจเชิงพื้นที่ระดับเมือง/ท้องถิ่นโดยมีแผนที่ความเสี่ยงน้ำท่วมในอนาคตที่ละเอียดและสอดคล้องกับบริบทพื้นที่
  - Required data/products: ผลการ downscale ฉากทัศน์สภาพภูมิอากาศระดับเมือง (SSP3/SSP5); DEM ความละเอียด 1 เมตร; แบบจำลอง/แผนที่น้ำท่วมในอนาคต (future flood inundation maps) ที่นำไปใช้ในงานประเมินความเสี่ยง/ความเปราะบางและงานวางแผนเชิงพื้นที่ได้
  - Source anchors: [`Interview Summary - UDDC.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20UDDC.md:20), [`Interview Summary - UDDC.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20UDDC.md:31), [`Interview Summary - UDDC.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20UDDC.md:33)

- Agency: UDDC (Urban Design and Development Center)
  - Use case: ออกแบบและประเมินทางเลือก Nature-based Solutions (NbS) ระดับโครงการ/ระดับพื้นที่แทรกแซง โดยใช้ข้อมูลความละเอียดสูง (เช่น drone 20 ซม. เพื่อสร้าง DSM/DTM) และใช้แบบจำลองบริการระบบนิเวศ (Urban InVest) เพื่อประเมินความสามารถการกักเก็บน้ำ/การระบายน้ำของระบบนิเวศเมือง
  - Goal: ออกแบบ NbS ให้เหมาะกับสภาพพื้นที่จริง และประเมินผลด้านการกักเก็บ/ระบายน้ำเพื่อใช้ประกอบการตัดสินใจและทำแผนปฏิบัติการในพื้นที่นำร่อง
  - Required data/products: ข้อมูลภาพถ่ายโดรนความละเอียด ~20 ซม.; DSM/DTM ที่ระบุรายละเอียดพื้นที่ (เช่น canopy/ชั้นความหลากหลายทางชีวภาพในระดับที่ใช้ระบุจุดแทรกแซงได้); อินพุต/พารามิเตอร์และผลลัพธ์จากแบบจำลอง Urban InVest เพื่อประเมิน retention/drainage; ชั้นข้อมูลเชิงพื้นที่ที่เชื่อมจากแบบจำลองไปสู่งานออกแบบ/วางแผน NbS ได้
  - Source anchors: [`Interview Summary - UDDC.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20UDDC.md:35), [`Interview Summary - UDDC.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20UDDC.md:37), [`Interview Summary - UDDC.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20UDDC.md:63)

- Agency: MSDHS (Ministry of Social Development and Human Security / พม.)
  - Use case: ซ้อนทับ (spatial overlay) “hazard maps” กับ “ตำแหน่ง/ฐานข้อมูลกลุ่มเปราะบางระดับรายบุคคล/ครัวเรือน” เพื่อระบุพื้นที่เสี่ยงและกลุ่มเป้าหมายในระดับตำบล (ตำบล) และเทศบาล (เทศบาล/อปท.)
  - Goal: ระบุ “พื้นที่เสี่ยง × กลุ่มเปราะบาง” เพื่อสนับสนุนการวางแผนการดูแล/การช่วยเหลือในระดับพื้นที่ที่ตรงกลไกงบท้องถิ่น
  - Required data/products: แผนที่ภัย/ชั้นข้อมูลภัยที่ใช้งานได้ (เช่น floods, droughts, heatwaves, landslides, PM2.5); ฐานข้อมูลกลุ่มเปราะบางของ MSDHS (welfare registries/field surveys) ที่เชื่อมโยงเชิงพื้นที่ได้; การสรุปผลระดับตำบลและเทศบาล (map/dashboard) เพื่อใช้งานเชิงแผนและการสื่อสารกับท้องถิ่น
  - Source anchors: [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20MSDHS.md:22), [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20MSDHS.md:23), [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20MSDHS.md:25), [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20MSDHS.md:32)

- Agency: MSDHS (Ministry of Social Development and Human Security / พม.)
  - Use case: “Mapping flood risk down to the municipality (เทศบาล) level” เพื่อจับคู่ “exposed subgroups (เช่น pregnant women, bedridden patients)” กับ “local government units ที่ควบคุมงบช่วยเหลือ”
  - Goal: ทำให้การจัดสรร/การตัดสินใจงบช่วยเหลือสอดคล้องกับระดับหน่วยงานที่ถือ budget และกลุ่มเป้าหมายที่ได้รับผลกระทบจริง
  - Required data/products: แผนที่/ชั้นข้อมูลความเสี่ยงน้ำท่วมระดับเทศบาล; ข้อมูลกลุ่มเป้าหมาย/กลุ่มเปราะบางที่จำแนกตามประเภท (เช่น pregnant women, bedridden patients); ผลการจับคู่พื้นที่เสี่ยง–กลุ่มเป้าหมาย–หน่วยงานท้องถิ่น (table/map/dashboard) ที่ใช้ประกอบการจัดสรรงบ
  - Source anchors: [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20MSDHS.md:32), [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20MSDHS.md:53)

- Agency: MSDHS (Ministry of Social Development and Human Security / พม.)
  - Use case: “Relocation Timelines” — ใช้ “2–5 year habitability forecasts” (เช่น “This area will be permanently flooded”) เพื่อวางแผน “community relocations” และ “occupational retraining” ล่วงหน้า
  - Goal: วางแผนย้ายถิ่น/ปรับอาชีพเชิงรุก ก่อนพื้นที่อยู่อาศัยเสื่อมสภาพหรือมีน้ำท่วมถาวร
  - Required data/products: ผลคาดการณ์/ฉากทัศน์ความเหมาะสมต่อการอยู่อาศัยช่วง 2–5 ปี (habitability forecasts) ระบุพื้นที่เสี่ยง “permanently flooded” หรือความเสี่ยงหลักอื่นๆ; การสรุปผลระดับพื้นที่เพื่อใช้กำหนดแผนย้ายถิ่นและแผนฝึกอาชีพใหม่
  - Source anchors: [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20MSDHS.md:44), [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20MSDHS.md:51)

- Agency: DDPM (Department of Disaster Prevention and Mitigation)
  - Use case: โครงการ “Northern Region Climate Risk Assessment” — พัฒนา “ชุดดัชนีความเปราะบางมาตรฐาน 10–20 ดัชนี” เพื่อให้จังหวัดและ อปท. สามารถ “เลือกใช้ดัชนี” ที่เหมาะสมในการประเมินความเสี่ยงระดับพื้นที่ของตนอย่างเป็นระบบ (น้ำท่วม ดินถล่ม แผ่นดินไหว)
  - Goal: สนับสนุนจังหวัดและ อปท. ให้ประเมินความเสี่ยงเชิงพื้นที่ได้อย่างเป็นระบบด้วยชุดดัชนีมาตรฐาน
  - Required data/products: ชุดดัชนีความเปราะบางมาตรฐาน (10–20 ดัชนี); ข้อมูล/ตัวแปรนำเข้าที่ใช้คำนวณดัชนี; คู่มือการเลือกใช้ดัชนีให้เหมาะกับบริบทพื้นที่; ผลลัพธ์เชิงพื้นที่ (เช่น คะแนน/ชั้นความเสี่ยงรายพื้นที่)
  - Source anchors: [`Interview Summary DDPM.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20DDPM.md:23), [`Interview Summary DDPM.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20DDPM.md:28)

- Agency: DDPM (Department of Disaster Prevention and Mitigation)
  - Use case: จัดทำ “แผนที่ภัย (hazard map)” โดยใช้ข้อมูลเหตุการณ์ย้อนหลัง (เช่น 3–5 ปี) เพื่อทำแผนที่กึ่งภัย (quasi-hazard maps) สำหรับการสื่อสาร/ใช้งานเชิงพื้นที่
  - Goal: มีแผนที่เชิงพื้นที่จากข้อมูลย้อนหลังเพื่อสนับสนุนการวางแผน/การสื่อสารความเสี่ยง
  - Required data/products: ฐานข้อมูลเหตุการณ์ย้อนหลังที่มีพิกัด/ตำแหน่งเพียงพอสำหรับทำแผนที่; เครื่องมือทำแผนที่และการสรุปเชิงพื้นที่; แนวทางการเลือกช่วงเวลาย้อนหลัง (3–5 ปี) และข้อจำกัดของการใช้ข้อมูลอดีตแทนการคาดการณ์อนาคต
  - Source anchors: [`Interview Summary DDPM.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20DDPM.md:31)

- Agency: BMA (Bangkok Metropolitan Administration / กรุงเทพมหานคร)
  - Use case: เชื่อมโยง “ข้อมูลฝน ระดับน้ำคลอง สถานีสูบน้ำ และเซนเซอร์น้ำท่วมของ BMA” กับ “ข้อมูลลุ่มน้ำต้นน้ำ และข้อมูลน้ำขึ้นน้ำลง” เพื่อสนับสนุนการปฏิบัติการรับมือน้ำท่วมระยะสั้นและการตอบโต้เหตุการณ์
  - Goal: สนับสนุนการตัดสินใจเชิงปฏิบัติการน้ำท่วมแบบระยะสั้น (short-term flood operations) และการตอบโต้เหตุการณ์ ด้วยข้อมูลที่เชื่อมโยงครบวงจร (เมือง–ต้นน้ำ–น้ำทะเลหนุน)
  - Required data/products: ชุดข้อมูล near real-time ของ BMA (ฝน/ระดับน้ำคลอง/สถานะการสูบ/เซนเซอร์น้ำท่วม); ชุดข้อมูลลุ่มน้ำต้นน้ำ (สภาพน้ำ/การระบาย/เงื่อนไขลุ่มน้ำ); ชุดข้อมูลน้ำขึ้นน้ำลง; กลไกเชื่อมโยงข้อมูล/มาตรฐานแลกเปลี่ยน (เช่น API/metadata) เพื่อให้ใช้งานได้ในงานปฏิบัติการ
  - Source anchors: [`Interview Summary - BMA.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20BMA.md:73)

- Agency: DLA (Department of Local Administration / สถ.)
  - Use case: ใช้ “ข้อมูลคาดการณ์/ฉากทัศน์ความเสี่ยงภัย (hazard projections) ที่ลงถึงขอบเขตเทศบาล/ตำบล” เพื่อให้ อปท. รู้ว่าพื้นที่ของตนต้องวางแผนงบประมาณและโครงการรับมือความเสี่ยงอะไร ในรอบแผน/งบประมาณประจำปี
  - Goal: ลดช่องว่างที่ อปท. ไม่มีข้อมูลสภาพภูมิอากาศ/สิ่งแวดล้อมเชิงระบบ และต้องการข้อมูลคาดการณ์ที่ใช้ได้จริงสำหรับการวางแผนและการตั้งงบในระดับท้องถิ่น
  - Required data/products: ชุดข้อมูล/แผนที่คาดการณ์ความเสี่ยงภัย (เช่น น้ำท่วม ภัยแล้ง PM2.5) ระดับเทศบาล/ตำบล; วิธีสรุปผลที่ “เข้าใจง่าย” (เช่น แผนที่/คะแนน/ชั้นความเสี่ยง); เมทาดาทาอธิบายสมมติฐาน/ข้อจำกัดของการคาดการณ์
  - Source anchors: [`Interview Summary - DLA.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DLA.md:37), [`Interview Summary - DLA.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DLA.md:48), [`Interview Summary - DLA.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DLA.md:49)

- Agency: DLA (Department of Local Administration / สถ.)
  - Use case: รวมศูนย์ “ข้อมูลภัย/ข้อมูลความเสี่ยงจากหน่วยงานเทคนิคหลายหน่วยงาน” เพื่อให้ อปท. ไม่ต้องเดาว่าควรใช้ข้อมูลของหน่วยงานใดในการทำแผนพื้นที่/โครงการความยืดหยุ่น (resilience projects)
  - Goal: ลดปัญหาข้อมูลภัยกระจัดกระจาย (data fragmentation) ที่ทำให้ อปท. ต้องค้นหาและเลือกแหล่งข้อมูลเอง
  - Required data/products: รายการชุดข้อมูลภัย/ความเสี่ยงที่เป็นมาตรฐาน (catalog) พร้อมผู้ดูแลข้อมูล; จุดเข้าถึงแบบรวมศูนย์ (single entry point) เพื่อค้นหา/ดาวน์โหลด/อ้างอิง; เอกสารกำกับคุณภาพ/การแนะนำการเลือกใช้ข้อมูลตามประเภทภัยและบริบทพื้นที่
  - Source anchors: [`Interview Summary - DLA.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DLA.md:40), [`Interview Summary - DLA.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DLA.md:55), [`Interview Summary - DLA.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DLA.md:57)

- Agency: DPT (Department of Public Works and Town & Country Planning)
  - Use case: ใช้ “การคาดการณ์ปริมาณฝนที่ปรับตามการเปลี่ยนแปลงสภาพภูมิอากาศ (climate-adjusted rainfall projections)” ร่วมกับ “แผนที่พื้นที่เสี่ยงน้ำท่วม” และ “เรขาคณิตโครงสร้างพื้นฐานท้องถิ่น” เพื่อสนับสนุนการวางแผนระบบระบายน้ำและการป้องกันน้ำท่วมในเขตเมือง
  - Goal: ทำให้การวางแผนระบายน้ำ/ป้องกันน้ำท่วมมีฐานข้อมูลที่สะท้อนความเสี่ยงในอนาคตมากกว่าอิงสถิติฝนย้อนหลังเพียงอย่างเดียว และรองรับการตัดสินใจเชิงผังเมืองและวิศวกรรม
  - Required data/products: ข้อมูลคาดการณ์ปริมาณฝนที่ปรับตามสภาพภูมิอากาศ (พร้อมสมมติฐาน/ช่วงเวลา); ข้อมูลอุทกวิทยาที่เกี่ยวข้องสำหรับงานระบายน้ำ; แผนที่พื้นที่เสี่ยงน้ำท่วมที่ใช้เป็นฐานข้อมูลการวางผัง/ออกแบบ; ข้อมูลเรขาคณิต/รายละเอียดโครงสร้างพื้นฐานระดับท้องถิ่น (เช่น ความสูงถนน รูปตัด/โครงข่ายระบายน้ำ ความหนาแน่นสถานี/จุดสำคัญ)
  - Source anchors: [`Interview Summary - DPT.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DPT.md:57), [`Interview Summary - DPT.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DPT.md:63), [`Interview Summary - DPT.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DPT.md:75)

- Agency: DPT (Department of Public Works and Town & Country Planning)
  - Use case: ซ้อนทับ (overlay) “ข้อมูลน้ำท่วม–ภัยแล้ง–กัดเซาะชายฝั่ง–การใช้ประโยชน์ที่ดิน–ข้อมูลเศรษฐสังคม” เพื่อกำหนดผังเมือง ควบคุมการใช้ประโยชน์ที่ดิน และออกแบบรูปแบบเมืองให้มีความยืดหยุ่น
  - Goal: สนับสนุนการตัดสินใจด้านผังเมืองและการกำกับการใช้ที่ดินด้วยฐานข้อมูลที่บูรณาการทั้งมิติภัย (hazard) การใช้ที่ดิน และเศรษฐสังคมในหลายระดับพื้นที่
  - Required data/products: ชั้นข้อมูล/แผนที่ภัยที่เกี่ยวข้อง (น้ำท่วม ภัยแล้ง กัดเซาะชายฝั่ง) ที่พร้อมใช้งานเชิงพื้นที่; ชั้นข้อมูลการใช้ประโยชน์ที่ดิน/การใช้ประโยชน์อาคาร; ข้อมูลเศรษฐสังคมที่เชื่อมโยงเชิงพื้นที่ได้; รูปแบบข้อมูลเชิงพื้นที่ที่ “ดิจิทัลและอ้างอิงพิกัด” (GIS-ready) พร้อมเมทาดาทาเพื่อใช้ซ้ำในการวางแผน
  - Source anchors: [`Interview Summary - DPT.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DPT.md:43), [`Interview Summary - DPT.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DPT.md:45), [`Interview Summary - DPT.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DPT.md:49), [`Interview Summary - DPT.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DPT.md:61), [`Interview Summary - DPT.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DPT.md:77)

- Agency: DPT (Department of Public Works and Town & Country Planning)
  - Use case: ใช้ “ข้อมูลความร้อนเมืองระดับละเอียด (fine-scale urban heat information)” เพื่อสนับสนุนการตัดสินใจผังเมืองเชิงรายละเอียดเกี่ยวกับพื้นที่สีเขียว/พื้นที่โล่ง และการออกแบบเมืองให้ทนทานต่อความร้อน
  - Goal: ทำให้การบูรณาการความเสี่ยงความร้อนเข้าสู่ผังเมืองและการวางแผนย่อย (ต่ำกว่าระดับจังหวัด) ทำได้จริง ด้วยข้อมูลที่ใช้ได้ในเชิงพื้นที่และการออกแบบ
  - Required data/products: ข้อมูลความร้อนเมืองระดับละเอียดที่ใช้งานได้สำหรับผังเมืองต่ำกว่าระดับจังหวัด; ตัวชี้วัด/แผนที่ความร้อนเชิงพื้นที่; เมทาดาทาอธิบายวิธีการ/ความละเอียด/ข้อจำกัด เพื่อใช้ในการตัดสินใจด้านพื้นที่สีเขียว พื้นที่โล่ง และมาตรการออกแบบเมืองลดความร้อน
  - Source anchors: [`Interview Summary - DPT.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DPT.md:59), [`Interview Summary - DPT.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DPT.md:79)

- Agency: FTI (Federation of Thai Industries / สภาอุตสาหกรรมแห่งประเทศไทย)
  - Use case: จัดทำ “Thailand Risk Map” ที่เป็นแผนที่ความเสี่ยงแบบระบุพิกัดระดับละเอียด (location-based) ระดับ 10 ตารางกม. และแบบจำแนกตามภาคเศรษฐกิจ (sector-based)
  - Goal: ให้ภาคเอกชนใช้ข้อมูลความเสี่ยงเชิงพื้นที่และเชิงภาคส่วนในการวางแผน/ตัดสินใจ
  - Required data/products: แผนที่ความเสี่ยงระดับ 10 ตารางกม. แบบ location-based และ sector-based
  - Source anchors: [`Interview Summary - FTI.md:L52-L53`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20FTI.md:52)

- Agency: FTI (Federation of Thai Industries / สภาอุตสาหกรรมแห่งประเทศไทย)
  - Use case: บูรณาการข้อมูลคาดการณ์ปริมาณน้ำต้นทุนระดับประเทศ กับข้อมูลความต้องการใช้น้ำภาคอุตสาหกรรมย้อนหลังมากกว่า 10 ปี เพื่อประเมินความเสี่ยงการขาดแคลนน้ำระยะ 20 ปี (โฟกัส EEC)
  - Goal: ประเมินความเสี่ยงการขาดแคลนน้ำระยะยาวเพื่อใช้ประกอบการวางแผนและการตัดสินใจลงทุน/มาตรการด้านเทคโนโลยีป้องกันการขาดแคลนน้ำ
  - Required data/products: ข้อมูลคาดการณ์น้ำต้นทุน/น้ำประปาหรืออุปทานน้ำระดับประเทศ; ข้อมูลความต้องการใช้น้ำภาคอุตสาหกรรมย้อนหลังมากกว่า 10 ปี; ผลการประเมินความเสี่ยงการขาดแคลนน้ำระยะ 20 ปี
  - Source anchors: [`Interview Summary - FTI.md:L28-L33`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20FTI.md:28)

- Agency: FTI (Federation of Thai Industries / สภาอุตสาหกรรมแห่งประเทศไทย)
  - Use case: คาดการณ์ความเสี่ยงการขาดแคลนน้ำ 20 ปีในพื้นที่ EEC โดยซ้อนทับความต้องการใช้น้ำภาคอุตสาหกรรมกับการคาดการณ์อุปทานน้ำที่ปรับตามสภาพภูมิอากาศ เพื่อกระตุ้นการลงทุนเทคโนโลยี
  - Goal: ใช้ผลคาดการณ์เป็นตัวกระตุ้น/เงื่อนไขการตัดสินใจลงทุนเทคโนโลยีเพื่อป้องกันการขาดแคลนน้ำ
  - Required data/products: ข้อมูลความต้องการใช้น้ำภาคอุตสาหกรรม; ข้อมูลคาดการณ์อุปทานน้ำที่ปรับตามสภาพภูมิอากาศ; ผลการซ้อนทับเพื่อประเมินความเสี่ยงการขาดแคลนน้ำระยะ 20 ปี (EEC)
  - Source anchors: [`Interview Summary - FTI.md:L61-L62`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20FTI.md:61)

- Agency: NSO (National Statistical Office)
  - Use case: ให้ DCCE ใช้ตรรกะ/หน่วยพื้นที่ “Enumeration Area (EA)” (บล็อกราว ~250 อาคาร) เพื่อเพิ่มความละเอียดเชิงพื้นที่ของชั้น “exposure” ในแผนที่ความเสี่ยง (risk map)
  - Goal: ยกระดับความละเอียดเชิงพื้นที่ของการทำ exposure mapping ให้ละเอียดกว่าการสรุปแบบกว้าง โดยอิงหน่วยพื้นที่ที่ NSO ใช้งานจริง
  - Required data/products: คำอธิบาย/ตรรกะการแบ่งหน่วย EA และขอบเขตการใช้งาน; ข้อมูล/ขอบเขตเชิงพื้นที่ของ EA ที่นำไปซ้อนทับในงานทำแผนที่ได้; แนวทางการเชื่อม EA กับชั้นข้อมูล exposure ของ risk map
  - Source anchors: [`Interview Summary - NSO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NSO.md:63), [`Interview Summary - NSO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NSO.md:106)

- Agency: NSO (National Statistical Office)
  - Use case: ใช้ฐานข้อมูล “Common Frame Database” (ข้อมูลสถานประกอบการ/กิจการทั่วประเทศถึงระดับตำบล) เพื่อประเมินความเปราะบางด้าน Human Settlement และใช้เป็นอินพุตในงานประเมินความเสี่ยงเชิงพื้นที่
  - Goal: ประเมินความเปราะบางของพื้นที่อยู่อาศัย/ชุมชน (Human Settlement vulnerability) ด้วยข้อมูลสถานประกอบการที่ครอบคลุมระดับพื้นที่ย่อย
  - Required data/products: ฐานข้อมูล Common Frame (ระดับตำบล); การแม็ปตัวแปร/ดัชนีที่ใช้สะท้อนความเปราะบางด้าน Human Settlement; ผลสรุปเชิงพื้นที่ที่นำไปใช้ในงานประเมินความเสี่ยงได้
  - Source anchors: [`Interview Summary - NSO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NSO.md:49), [`Interview Summary - NSO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NSO.md:108)

- Agency: NXPO (Office of National Higher Education Science Research and Innovation Policy Council)
  - Use case: ใช้ข้อมูลระดับมหภาค (macro-level) เป็นฐานหลักสำหรับการออกแบบนโยบายระดับชาติด้วยกระบวนการ “Double Diamond” โดยอาศัยข้อมูลจากรายงานต่างประเทศ สไลด์นำเสนอของ DCCE และรายงาน/ผลลัพธ์จากที่ปรึกษา
  - Goal: สนับสนุนการกำหนดนโยบาย/การออกแบบมาตรการระดับชาติด้วยหลักฐานเชิงข้อมูลระดับมหภาคที่เพียงพอ
  - Required data/products: ชุดข้อมูล/ฐานข้อมูลระดับมหภาคที่ใช้สำหรับนโยบาย (macro-data); รายงาน/สรุปสาระจากแหล่งต่างประเทศ; ชุดสรุป/รวบรวมข้อมูลจาก DCCE และรายงานที่ปรึกษาให้อยู่ในรูปแบบที่ใช้งานได้ในการออกแบบนโยบาย
  - Source anchors: [`Interview Summary - NXPO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NXPO.md:40)

- Agency: NXPO (Office of National Higher Education Science Research and Innovation Policy Council)
  - Use case: ใช้วิธี Foresight เพื่อสร้างฉากทัศน์ (scenarios) สำหรับการวางนโยบาย โดยต้องการให้ “ข้อมูลที่ถูกพัฒนา/เก็บ” สอดคล้องกับ “ข้อมูลที่ผู้ใช้ปลายทางต้องใช้ตัดสินใจ” (ลดปัญหา supply–demand mismatch ของข้อมูล)
  - Goal: ทำให้การสร้างฉากทัศน์และการวางนโยบายใช้ข้อมูลที่ตรงกับการตัดสินใจจริง และลดการเก็บข้อมูลจำนวนมากที่ “ไม่ถูกนำไปใช้”
  - Required data/products: ชุดข้อมูล/ตัวแปรที่ผู้ใช้ปลายทางต้องใช้ในการตัดสินใจ (end-user decision data requirements); กรอบ/กระบวนการเชื่อม “ความต้องการผู้ใช้” กับการออกแบบแบบจำลอง/การเก็บข้อมูล; สรุปช่องว่าง/รายการข้อมูลที่ถูกเก็บแต่ไม่ถูกใช้เพื่อปรับแผนการผลิตข้อมูล
  - Source anchors: [`Interview Summary - NXPO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NXPO.md:42)

- Agency: NXPO (Office of National Higher Education Science Research and Innovation Policy Council)
  - Use case: ขยายขอบเขตการวางนโยบายปรับตัวจาก “น้ำ” ไปสู่ “ผลกระทบลูกโซ่ (cascading impacts)” เช่น คลื่นความร้อน วิกฤตสุขภาพ (พาหะนำโรค) และคุณภาพอาหาร/ความเสื่อมโทรมของอาหาร โดยต้องมีข้อมูลสนับสนุนสำหรับการบูรณาการประเด็นเหล่านี้ในระดับชาติ
  - Goal: ทำให้การสนทนา/นโยบายปรับตัวระดับชาติครอบคลุมความเสี่ยงหลายมิติและผลกระทบลูกโซ่มากกว่าโฟกัสน้ำเพียงอย่างเดียว
  - Required data/products: ชุดข้อมูล/ตัวชี้วัดความเสี่ยงและผลกระทบสำหรับ heatwaves, health crises (disease vectors), และ food degradation; สรุปความเชื่อมโยงผลกระทบลูกโซ่เพื่อใช้ประกอบนโยบาย (evidence package)
  - Source anchors: [`Interview Summary - NXPO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NXPO.md:44)

- Agency: OTP (Office of Transport and Traffic Policy and Planning / สนข.)
  - Use case: โครงการนำร่อง “Climate Change Adaptation of Transport Infrastructure” — ประเมินผลกระทบความเสี่ยงภัยพิบัติต่อโครงสร้างพื้นฐานคมนาคมหลักระดับระหว่างเมือง (national highways, rural roads, railways, airports, ports)
  - Goal: ใช้ผลการประเมินเพื่อจัดทำคู่มือปฏิบัติ/แนวทางปรับตัว (operational manuals / adaptation guidelines) สำหรับหน่วยงานก่อสร้าง/หน่วยงานปฏิบัติ (เช่น Department of Highways) และให้ OTP ใช้ต่อในบทบาทเชิงนโยบายและการประเมินผล
  - Required data/products: ข้อมูลน้ำย้อนหลัง 10 ปี; จุดเสี่ยงใน GIS; แบบจำลองปริมาณฝนช่วงกลับซ้ำ 50–100 ปี; แบบจำลองอุทกวิทยาความละเอียดสูงเพื่อทำแผนที่การไหลของภัย (hazard flows) ซ้อนทับบนเส้นทางคมนาคมถึงระดับจุดระบุสินทรัพย์/ตำแหน่งเฉพาะ (เช่น หลักกิโลเมตรทางหลวง, หมายเลขเสาไฟตามแนวรถไฟ)
  - Source anchors: [`Interview Summary - OTP.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20OTP.md:18), [`Interview Summary - OTP.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20OTP.md:21), [`Interview Summary - OTP.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20OTP.md:54), [`Interview Summary - OTP.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20OTP.md:58)

## กลุ่มที่ 3 ข้อมูลสนับสนุนการปฏิบัติงานเชิงพื้นที่

- Agency: MSDHS (Ministry of Social Development and Human Security / พม.)
  - Use case: ใช้ “dashboards” ที่สรุปผลจาก “raw data → dashboards for executives” เพื่อให้ผู้บริหารใช้ระหว่างลงพื้นที่ (iPads during field visits) และให้สำนักงานจังหวัดใช้ติดตามสถานการณ์
  - Goal: สนับสนุนการตัดสินใจเชิงปฏิบัติการ/การลงพื้นที่ด้วยข้อมูลเชิงพื้นที่ที่สรุปแล้วและเข้าถึงง่าย
  - Required data/products: แดชบอร์ดที่แปลงข้อมูลดิบเป็นภาพรวมเชิงพื้นที่ (โดย Technology Center เป็น data hub); ข้อมูล hazard + vulnerable populations ที่สรุประดับตำบลเพื่อสื่อสารและตัดสินใจภาคสนาม
  - Source anchors: [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20MSDHS.md:25), [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20MSDHS.md:27)

- Agency: MSDHS (Ministry of Social Development and Human Security / พม.)
  - Use case: ระหว่างวิกฤต “share detailed personal data with local authorities and health departments” เพื่อดำเนินการ “physical evacuations” ของกลุ่มเปราะบาง
  - Goal: สนับสนุนการอพยพ/การช่วยเหลือเชิงปฏิบัติการที่ต้องใช้ข้อมูลรายบุคคลอย่างแม่นยำและทันเวลา
  - Required data/products: ข้อมูลกลุ่มเปราะบางระดับรายบุคคล/ครัวเรือน (เช่น ข้อมูลทะเบียนสวัสดิการ/สำรวจภาคสนาม) ที่สามารถแลกเปลี่ยนกับหน่วยงานท้องถิ่น/สาธารณสุขได้อย่างปลอดภัย; กลไกการแชร์ข้อมูลภายใต้ข้อกำกับ (เช่น สิทธิ์เข้าถึง/การบันทึกการใช้งาน)
  - Source anchors: [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20MSDHS.md:27)

- Agency: DDPM (Department of Disaster Prevention and Mitigation)
  - Use case: ติดตาม “ข้อมูลเหตุการณ์ภัยพิบัติและความเสียหาย” ถึงระดับหมู่บ้าน (ฐานย้อนหลัง 10 ปี) เพื่อใช้สนับสนุนการตอบโต้เหตุการณ์และการสรุปสถานการณ์
  - Goal: มีข้อมูลเหตุการณ์และผลกระทบเชิงพื้นที่ระดับหมู่บ้านเพื่อใช้งานเชิงปฏิบัติการ
  - Required data/products: ข้อมูลเหตุการณ์และความเสียหายระดับหมู่บ้าน (10 ปี); ตัวระบุพื้นที่มาตรฐาน (หมู่บ้าน/ตำบล/อำเภอ/จังหวัด); เครื่องมือสรุป/รายงานสถานการณ์ตามพื้นที่
  - Source anchors: [`Interview Summary DDPM.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20DDPM.md:44)

- Agency: DDPM (Department of Disaster Prevention and Mitigation)
  - Use case: เพิ่ม “พิกัดเชิงพื้นที่ที่ละเอียดขึ้น” ภายในระดับหมู่บ้านด้วยเครื่องมือรายงาน GIS ใหม่ เพื่อแก้ปัญหา “ขาดพิกัดที่แน่นอน” ในข้อมูลปัจจุบัน
  - Goal: ยกระดับความละเอียดเชิงพื้นที่ของข้อมูลเหตุการณ์/ความเสียหาย เพื่อให้ใช้ทำแผนที่/วิเคราะห์พื้นที่ได้แม่นยำขึ้น
  - Required data/products: เครื่องมือรายงาน GIS; มาตรฐานพิกัด/รูปแบบการบันทึกตำแหน่ง; การฝึกอบรม/แนวทางใช้งานสำหรับผู้บันทึกข้อมูลระดับพื้นที่
  - Source anchors: [`Interview Summary DDPM.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20DDPM.md:44)

- Agency: DDPM (Department of Disaster Prevention and Mitigation)
  - Use case: ใช้ “แพลตฟอร์มเตือนภัย/พอร์ทัลข้อมูล (DDPM Alert Platform / Data Portal)” ที่รวบรวมข้อมูลแจ้งเตือนจากหน่วยงานเทคนิค (ผ่าน MOU) เพื่อใช้สนับสนุนการปฏิบัติการเตือนภัย
  - Goal: รวมศูนย์ข้อมูลแจ้งเตือนเพื่อสนับสนุนการเฝ้าระวังและการเตือนภัยเชิงปฏิบัติการ
  - Required data/products: ข้อมูลแจ้งเตือนจากหน่วยงานเทคนิคหลายหน่วยงาน; กลไกการรวม/แสดงผลข้อมูลแบบ near real-time; ช่องทางการเผยแพร่/แจ้งเตือนที่ใช้ได้จริงในภาคสนาม
  - Source anchors: [`Interview Summary DDPM.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20DDPM.md:33), [`Interview Summary DDPM.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20DDPM.md:34)

- Agency: DDPM (Department of Disaster Prevention and Mitigation)
  - Use case: กระบวนการเก็บข้อมูลความเสียหาย “LAO → อำเภอ → จังหวัด → ส่วนกลาง” โดยจังหวัดทำ QC ก่อนบันทึกเข้าระบบส่วนกลาง (ส่วนกลางไม่สามารถตรวจสอบภาคสนามได้)
  - Goal: ให้ข้อมูลความเสียหายที่ถูกรายงานผ่านสายงานได้รับการยืนยัน/ควบคุมคุณภาพก่อนเข้าระบบส่วนกลางเพื่อใช้ตัดสินใจ/สรุปสถานการณ์
  - Required data/products: ขั้นตอน QC มาตรฐานสำหรับจังหวัด; เกณฑ์/ตัวชี้วัดคุณภาพข้อมูล; ระบบติดตามสถานะ/ความครบถ้วนของการรายงานตามสายงาน
  - Source anchors: [`Interview Summary DDPM.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20DDPM.md:40), [`Interview Summary DDPM.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20DDPM.md:42)

- Agency: BMA (Bangkok Metropolitan Administration / กรุงเทพมหานคร)
  - Use case: ผสาน “ข้อมูลการติดตามดัชนีความร้อนของ BMA” กับ “ตำแหน่งจุดคลายร้อน (cooling points)” และ “การพยากรณ์ไมโครไคลเมตในอนาคต” เพื่อกำหนดเป้าหมายมาตรการลดความเสี่ยงความร้อนเมืองในระดับเขตและย่าน
  - Goal: สนับสนุนการกำหนดเป้าหมาย/จัดสรรมาตรการรับมือความร้อน (urban heat-risk interventions) ให้ตรงพื้นที่เสี่ยงในระดับเขต/ย่าน ด้วยข้อมูลการติดตามและการคาดการณ์ที่ละเอียดขึ้น
  - Required data/products: ข้อมูล heat index/ตัวชี้วัดความร้อนระดับเมืองและระดับพื้นที่; ฐานข้อมูลตำแหน่งและคุณลักษณะของ cooling points; ผลพยากรณ์ไมโครไคลเมต/ตัวแปรที่เกี่ยวข้องสำหรับการเตือนภัย/วางแผนระยะสั้น; เครื่องมือแผนที่/แดชบอร์ดเพื่อระบุกลุ่มเป้าหมายและติดตามการดำเนินการ
  - Source anchors: [`Interview Summary - BMA.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20BMA.md:75)

- Agency: NSO (National Statistical Office)
  - Use case: ระหว่างเกิดภัย (เช่น น้ำท่วม) ซ้อนทับ “ข้อมูลสำมะโน/ข้อมูลพื้นฐาน” (ประชากร เกษตร สถานประกอบการ) กับ “พื้นที่ภัยพิบัติที่ DDPM ประกาศ” ถึงระดับตำบล เพื่อคำนวณปริมาณ “คนและทรัพย์สินที่ได้รับผลกระทบ”
  - Goal: คำนวณและสรุปจำนวนผู้ได้รับผลกระทบ/ทรัพย์สินที่ได้รับผลกระทบในพื้นที่ภัยพิบัติ เพื่อสนับสนุนการทำงานช่วงเกิดเหตุ
  - Required data/products: ข้อมูลพื้นฐานจากสำมะโน/ฐานข้อมูลของ NSO (ประชากร เกษตร สถานประกอบการ) ที่ผูกเชิงพื้นที่ได้; ขอบเขตพื้นที่ภัยพิบัติที่ DDPM ประกาศ (ระดับตำบล); เครื่องมือ/กระบวนการซ้อนทับเชิงพื้นที่เพื่อสรุปผลกระทบ
  - Source anchors: [`Interview Summary - NSO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NSO.md:59)

## กลุ่มที่ 4 ข้อมูลสนับสนุนกลุ่มเปราะบางและความสามารถในการรับมือปรับตัว

- Agency: UDDC (Urban Design and Development Center)
  - Use case: ซ้อนทับ “แผนที่ภัยกายภาพ/ความเสี่ยงสภาพภูมิอากาศระดับพื้นที่” กับ “ข้อมูลเศรษฐสังคม” เพื่อระบุ “double vulnerability” (กลุ่มประชากรที่เปราะบางจากตำแหน่งที่ตั้ง/เส้นทางน้ำท่วม ฯลฯ แม้ไม่เข้าเกณฑ์ความยากจนตามนิยามเดิม) และใช้ระบุกลุ่มเป้าหมาย/พื้นที่ที่ควรได้รับการช่วยเหลือหรือการลงทุนเชิงรุก
  - Goal: ระบุและจัดลำดับความสำคัญของ “กลุ่มเปราะบางใหม่” จากความเสี่ยงเชิงพื้นที่ เพื่อสนับสนุนการวางมาตรการและการจัดสรรทรัพยากรเชิงรุก
  - Required data/products: แผนที่ภัยกายภาพ/ความเสี่ยงสภาพภูมิอากาศที่ลงถึงระดับพื้นที่ย่อย; ข้อมูลเศรษฐสังคมที่เชื่อมโยงเชิงพื้นที่ได้; ผลการซ้อนทับ/ตัวชี้วัด double vulnerability (เช่น แผนที่/ตารางสรุป) เพื่อใช้กำหนดพื้นที่และกลุ่มเป้าหมาย
  - Source anchors: [`Interview Summary - UDDC.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20UDDC.md:39), [`Interview Summary - UDDC.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20UDDC.md:65)

- Agency: MSDHS (Ministry of Social Development and Human Security / พม.)
  - Use case: “Highly granular impact data” — ต้องรู้ว่า “specific hazards impact specific subgroups” (เช่น children vs. elderly vs. the 7 types of disabled persons)
  - Goal: ออกแบบการดูแล/สวัสดิการ/มาตรการรับมือภัยให้เหมาะกับกลุ่มเปราะบางแต่ละประเภท (จำแนกตาม subgroup)
  - Required data/products: ข้อมูลผลกระทบจากภัยแยกตาม hazard × subgroup (children / elderly / ประเภทความพิการ 7 ประเภท ฯลฯ); โครงสร้างข้อมูล/ตัวชี้วัดทางสังคมที่ทำให้จำแนก subgroup ได้อย่างสอดคล้อง
  - Source anchors: [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20MSDHS.md:42), [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20MSDHS.md:40)

- Agency: MSDHS (Ministry of Social Development and Human Security / พม.)
  - Use case: “Gender and Equality” — ใช้ข้อมูลเพื่อวางแผน “gender-inclusive shelters, safe bathrooms, และ specific protocols” สำหรับ “pregnant women และ LGBTQ+ individuals” ระหว่างภัยพิบัติ
  - Goal: ทำให้การจัดการศูนย์พักพิง/การช่วยเหลือในภัยพิบัติครอบคลุมความต้องการเฉพาะของกลุ่มเปราะบางด้านเพศและความเท่าเทียม
  - Required data/products: ข้อมูล/ตัวชี้วัดที่จำแนกความต้องการด้านเพศและความเท่าเทียม (เช่น pregnant women, LGBTQ+ individuals) สำหรับการออกแบบศูนย์พักพิง; แนวทาง/โปรโตคอลการปฏิบัติในศูนย์พักพิงที่อ้างอิงข้อมูล (protocols)
  - Source anchors: [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20MSDHS.md:43)

- Agency: DDPM (Department of Disaster Prevention and Mitigation)
  - Use case: ประเมิน/วัด “ขีดความสามารถในการจัดการ (management capacity) หรือ adaptive capacity” เพื่อเข้าใจความสามารถในการรับมือ/ความยืดหยุ่นของพื้นที่ แต่ปัจจุบันทำไม่ได้เชิงปริมาณและอาศัย After Action Reviews (AAR)
  - Goal: ทำให้สามารถประเมินขีดความสามารถในการรับมือ/ปรับตัวได้อย่างเป็นระบบ (มากกว่าเชิงคุณภาพจาก AAR)
  - Required data/products: ตัวชี้วัด/กรอบวิธีการวัด adaptive capacity หรือ management capacity; ข้อมูลปฏิบัติการ/ทรัพยากร/กระบวนการที่ใช้สร้างตัวชี้วัด; รูปแบบรายงาน/แดชบอร์ดสรุป bottlenecks และความสามารถในการจัดการ
  - Source anchors: [`Interview Summary DDPM.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20DDPM.md:61), [`Interview Summary DDPM.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20DDPM.md:63)

- Agency: NSO (National Statistical Office)
  - Use case: ให้ DCCE นำ “ตัวชี้วัดความเปราะบางด้านเกษตรระดับละเอียด” จาก Agricultural Census (เช่น หนี้ครัวเรือน สถานะการชำระหนี้ ความเป็นเจ้าของสินทรัพย์เกษตร เช่น รถไถ สถานะการถือครองที่ดิน: เป็นเจ้าของ vs เช่า) ไปใช้ในแบบจำลอง เพื่อเพิ่มความแม่นยำ
  - Goal: เพิ่มความแม่นยำของแบบจำลอง/การประเมินความเปราะบางภาคเกษตร โดยใช้ตัวชี้วัดฐานที่สะท้อนสภาพจริงของครัวเรือนเกษตร
  - Required data/products: ตัวชี้วัดจาก Agricultural Census (หนี้/การชำระหนี้/สินทรัพย์/การถือครองที่ดิน); โครงสร้างตัวแปร/นิยามและเมทาดาทาเพื่อใช้ในแบบจำลอง; การเชื่อมโยงตัวชี้วัดเหล่านี้เข้ากับดัชนีความเปราะบาง/ความเสี่ยง
  - Source anchors: [`Interview Summary - NSO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NSO.md:93), [`Interview Summary - NSO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NSO.md:108)

- Agency: NXPO (Office of National Higher Education Science Research and Innovation Policy Council)
  - Use case: บูรณาการ “ดัชนีความยืดหยุ่น/ขีดความสามารถเชิงสถาบันของท้องถิ่น (Institutional Resilience Index)” เข้ากับ “การคาดการณ์คลื่นความร้อนระดับพื้นที่” เพื่อระบุเทศบาลที่ควรได้รับการแทรกแซงฉุกเฉินโดยมหาวิทยาลัย (ภายใต้ Net Zero Campus) ในช่วงเหตุการณ์ความร้อนจัด
  - Goal: ระบุพื้นที่ที่มีความเสี่ยงสูงและขีดความสามารถต่ำ เพื่อจัดลำดับความสำคัญการช่วยเหลือ/การแทรกแซงเชิงปฏิบัติการโดยเครือข่ายมหาวิทยาลัย
  - Required data/products: ดัชนี Institutional Resilience Index (ประเมินความสามารถของ อปท./เทศบาล); ผลคาดการณ์คลื่นความร้อนระดับพื้นที่ (localized heatwave projections); ผลการผสาน/จัดอันดับพื้นที่ “เสี่ยง × ขีดความสามารถ” (เช่น แผนที่/ตารางจัดลำดับ); เกณฑ์คัดเลือกเทศบาลเป้าหมายเพื่อการแทรกแซง
  - Source anchors: [`Interview Summary - NXPO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NXPO.md:70)

## กลุ่มที่ 5 ข้อมูลสนับสนุนการตีความข้อมูลและพัฒนาระบบข้อมูล

- Agency: UDDC (Urban Design and Development Center)
  - Use case: จัดทำพอร์ทัลข้อมูลแบบ “Single Source of Truth” เพื่อรวมศูนย์ข้อมูลน้ำที่กระจัดกระจายจากหลายหน่วยงาน (เช่น RID/ONWR/HII ฯลฯ) และทำมาตรฐานข้อมูลฐาน/แบบจำลอง (เช่น ระบุว่า SSP/Heat Index/PM2.5 metrics ใดควรใช้เป็นมาตรฐาน) พร้อมออกแบบการเข้าถึงแบบ 2 ชั้น: ข้อมูลดิบที่ประมวลผลต่อได้ (เช่น CSVs/APIs) สำหรับนักวิจัย และแดชบอร์ดสรุปแบบเข้าใจง่ายสำหรับผู้บริหารท้องถิ่น
  - Goal: ลดปัญหา data fragmentation และทำให้ผู้ใช้สามารถเข้าถึงทั้งข้อมูลดิบสำหรับการวิเคราะห์ และข้อมูลสรุปสำหรับการตัดสินใจ/การสื่อสารเชิงผู้บริหาร โดยอ้างอิงชุดข้อมูล/มาตรฐานเดียวกัน
  - Required data/products: พอร์ทัลรวมศูนย์ข้อมูลน้ำ; กลไกมาตรฐาน/การรับรองข้อมูลฐานและแบบจำลอง (รวมการ “ประกาศ” ชุดมาตรฐานที่ใช้ร่วมกัน); ช่องทางข้อมูลดิบที่ดาวน์โหลด/เรียกใช้ได้ (CSV/APIs); แดชบอร์ดสรุปสำหรับผู้บริหารท้องถิ่น
  - Source anchors: [`Interview Summary - UDDC.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20UDDC.md:46), [`Interview Summary - UDDC.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20UDDC.md:52), [`Interview Summary - UDDC.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20UDDC.md:56), [`Interview Summary - UDDC.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20UDDC.md:61)

- Agency: UDDC (Urban Design and Development Center)
  - Use case: ใช้ “แผนที่ความเสี่ยง (risk maps) ที่เป็นทางการ/เชื่อถือได้จาก DCCE” เป็นหลักฐานอ้างอิงเพื่อช่วยให้ท้องถิ่นสามารถให้เหตุผลและขออนุมัติงบประมาณสำหรับมาตรการปรับตัวเชิงรุก (แทนการรออนุมัติงบหลังเกิดภัย)
  - Goal: ทำให้การจัดสรรงบประมาณด้านการป้องกัน/ปรับตัวเชิงรุกของท้องถิ่นอาศัยหลักฐานเชิงข้อมูลที่ “ถูกยอมรับ” ในกระบวนการงบประมาณ
  - Required data/products: ชุดแผนที่ความเสี่ยงจาก DCCE ที่มีสถานะเป็นทางการ/อ้างอิงได้; เอกสารกำกับ/เมทาดาทาเพื่อใช้เป็นหลักฐานประกอบการอนุมัติงบ; รูปแบบการอ้างอิงที่นำไปใช้ในเอกสาร/กระบวนการงบประมาณของหน่วยงานท้องถิ่นได้
  - Source anchors: [`Interview Summary - UDDC.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20UDDC.md:48), [`Interview Summary - UDDC.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20UDDC.md:54)

- Agency: TBA (Thai Bankers' Association) / Commercial Banks
  - Use case: ต้องมี “คลังข้อมูลกลางที่เข้าถึงได้ (central, accessible data repository)” สำหรับชุดข้อมูลพื้นฐานและแผนที่ความเสี่ยง เพื่อให้ธนาคารดึงไปใช้ทำแบบจำลองความเสี่ยง/การเงินได้โดยตรง ลดการต้องจัดซื้อข้อมูลที่ผ่านการปรับแต่งจากผู้ให้บริการภายนอก และทำให้ทุกธนาคารอ้างอิงข้อมูลชุดเดียวกันได้มากขึ้น
  - Goal: ลดต้นทุน/แรงเสียดทานในการเข้าถึงข้อมูล และเพิ่มความสอดคล้องของข้อมูลอ้างอิงที่ใช้ในภาคการเงิน
  - Required data/products: จุดเข้าถึงแบบรวมศูนย์สำหรับชุดข้อมูลพื้นฐาน (foundational datasets) และ risk maps; รูปแบบการนำเสนอที่จัดหมวด/สรุปตามประเภทสินทรัพย์ (asset type-aggregates) เพื่อให้ใช้งานในพอร์ตสินทรัพย์ได้ง่าย; เมทาดาทา/เงื่อนไขการใช้งานที่ชัดเจน
  - Source anchors: [`Interview Summary - Thai Bankers' Association.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20Thai%20Bankers'%20Association.md:41)

- Agency: TBA (Thai Bankers' Association) / Commercial Banks
  - Use case: ตีความและใช้งาน “แผนที่น้ำท่วมแบบความน่าจะเป็น” อย่างถูกต้อง โดยต้องมีแนวทาง/มาตรฐานสำหรับการจัดการความไม่แน่นอน (uncertainty handling) เพื่อป้องกันการนำแผนที่ความน่าจะเป็น (เช่น 100-year flood map) ไปใช้แบบ deterministic จนทำให้ประเมินผลกระทบทางการเงินสูงเกินจริง
  - Goal: ทำให้การประเมินความเสี่ยงสภาพภูมิอากาศของภาคการเงินสะท้อนความไม่แน่นอนอย่างเหมาะสมและลดข้อผิดพลาดเชิงระเบียบวิธี
  - Required data/products: แนวทาง/มาตรฐานการอ่านและใช้ probabilistic hazard maps (รวมตัวอย่างการตีความที่ถูกต้อง); เมทาดาทาอธิบายความหมายของช่วงกลับซ้ำ/ความน่าจะเป็นและข้อจำกัด; สื่ออบรม/คู่มือเพื่อยกระดับความเข้าใจของนักวิเคราะห์
  - Source anchors: [`Interview Summary - Thai Bankers' Association.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20Thai%20Bankers'%20Association.md:39)

- Agency: MSDHS (Ministry of Social Development and Human Security / พม.)
  - Use case: จัดทำ “central data catalog” และ “technical metadata / data dictionaries” เพื่อแก้ปัญหา “staff waste time hunting across multiple websites” และ “ต้องโทรถามหน่วยงานต้นทางเพื่ออ่านข้อมูลให้เป็น”
  - Goal: ลดเวลาและความคลาดเคลื่อนในการค้นหา/ทำความเข้าใจชุดข้อมูลภัยจากหลายแหล่ง และทำให้การใช้งานข้อมูลทำได้ถูกต้องสม่ำเสมอ
  - Required data/products: แค็ตตาล็อกข้อมูลแบบรวมศูนย์ (single entry point); เมทาดาทาทางเทคนิค (เช่น คำอธิบายตัวแปร ความละเอียด ช่วงเวลา หน่วยวัด); data dictionary/คู่มืออ่านข้อมูลสำหรับชุดข้อมูลภัยสำคัญ (เช่น DDPM historical disasters)
  - Source anchors: [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20MSDHS.md:34), [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20MSDHS.md:49)

- Agency: MSDHS (Ministry of Social Development and Human Security / พม.)
  - Use case: ต้องมี “Projections and Baselines” (ไม่ใช่แค่ historical, annual statistical data) และต้อง “broken down to the sub-district (ตำบล) and municipality (เทศบาล/อปท.) levels” เพื่อใช้ในงานวางแผน
  - Goal: ทำให้ MSDHS สามารถใช้ข้อมูลคาดการณ์/ฐานข้อมูลที่เหมาะสมต่อการตัดสินใจเชิงพื้นที่ในระดับที่หน่วยงานท้องถิ่นใช้จริง
  - Required data/products: ชุดข้อมูลคาดการณ์/forecast (predictive) และ baseline ที่สรุประดับตำบลและเทศบาล; เมทาดาทาอธิบายสมมติฐาน/ข้อจำกัดของการคาดการณ์ เพื่อให้ผู้ใช้ตีความได้ถูกต้อง
  - Source anchors: [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20MSDHS.md:32)

- Agency: NESDC (Office of the National Economic and Social Development Council / สภาพัฒน์)
  - Use case: “SDG Voluntary National Review (VNR) 2025” — จัดทำรายงานความก้าวหน้า 10 ปีของทุกเป้าหมาย SDGs โดยทำความสะอาด/จัดรูปแบบข้อมูลจากหลายกระทรวงเพื่อสร้าง baseline เดียว (เช่น ทำให้ตัวชี้วัดการเสียชีวิตจากอุบัติเหตุทางถนนสอดคล้องกัน)
  - Goal: สร้าง baseline เดียวข้ามกระทรวงเพื่อใช้รายงานความก้าวหน้า SDGs
  - Required data/products: ข้อมูลตัวชี้วัด SDGs ที่ผ่านการทำความสะอาด/มาตรฐานร่วมกันข้ามกระทรวง; นิยาม baseline และตัวชี้วัดที่ทำให้เทียบเคียงได้ (เช่น การทำให้ตัวชี้วัดการเสียชีวิตบนท้องถนนสอดคล้องกันระหว่างกระทรวงมหาดไทยและกระทรวงสาธารณสุข)
  - Source anchors: [`Interview Summary - NESDC.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NESDC.md:25)

- Agency: NESDC (Office of the National Economic and Social Development Council / สภาพัฒน์)
  - Use case: ให้ DCCE จัดทำ “ตัวชี้วัด/ค่า baseline/ค่าเป้าหมาย” ที่เป็นมาตรฐาน เพื่อให้ NESDC สามารถติดตามและประเมินความสำเร็จของ Milestone 11 (ภูมิคุ้มกันของสังคมต่อการเปลี่ยนแปลงสภาพภูมิอากาศ) ภายใต้แผนพัฒนาฯ ฉบับที่ 13
  - Goal: ติดตามและประเมินความสำเร็จของ Milestone 11 ภายใต้แผนพัฒนาฯ ฉบับที่ 13
  - Required data/products: ตัวชี้วัดมาตรฐาน; ค่า baseline; ค่าเป้าหมายที่สอดคล้องกับ Milestone 11 (ภูมิคุ้มกันของสังคมต่อการเปลี่ยนแปลงสภาพภูมิอากาศ)
  - Source anchors: [`Interview Summary - NESDC.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NESDC.md:51)

- Agency: DDPM (Department of Disaster Prevention and Mitigation)
  - Use case: ใช้ “Data Catalog ~40 datasets” สำหรับการแลกเปลี่ยนข้อมูลระหว่างหน่วยงานผ่าน API เพื่อสนับสนุนการบูรณาการข้อมูลเตือนภัย/ข้อมูลภัยพิบัติ
  - Goal: ทำให้การแลกเปลี่ยนข้อมูลข้ามหน่วยงานทำได้จริง (ผ่าน API) และจัดการรายการชุดข้อมูลที่แชร์ได้อย่างเป็นระบบ
  - Required data/products: แค็ตตาล็อกชุดข้อมูลพร้อมเมทาดาทา; API และมาตรฐานการเข้าถึง/สิทธิ์การใช้ข้อมูล; รายการชุดข้อมูลที่แลกเปลี่ยนได้และคู่มือการใช้งาน
  - Source anchors: [`Interview Summary DDPM.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20DDPM.md:34)

- Agency: DDPM (Department of Disaster Prevention and Mitigation)
  - Use case: จัดหมวดหมู่/ตีความ “ข้อมูลนับจำนวนความเสียหายดิบ” (เช่น ถนนเสียหาย ปศุสัตว์ตาย วัดเสียหาย) ให้เข้ากรอบมาตรฐาน “Exposure” และ “Vulnerability” (เช่น UNDRR sector groupings) เพื่อใช้สรุปความสูญเสียเชิงเศรษฐกิจระดับมหภาค
  - Goal: ทำให้ข้อมูลความเสียหายดิบถูกจัดหมวดหมู่ตามมาตรฐานและนำไปใช้สรุป/เปรียบเทียบเชิงระบบได้
  - Required data/products: taxonomy/กรอบจัดหมวดหมู่มาตรฐาน (เช่น UNDRR); mapping table ระหว่างหมวดหมู่ข้อมูลของ DDPM กับมาตรฐาน; นิยามข้อมูล/รหัสหมวดหมู่ที่ใช้ร่วมกัน
  - Source anchors: [`Interview Summary DDPM.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20DDPM.md:52), [`Interview Summary DDPM.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20DDPM.md:54)

- Agency: DDPM (Department of Disaster Prevention and Mitigation)
  - Use case: ใช้ “เครื่องมือคัดกรองอัตโนมัติ/AI” เพื่อตรวจจับและทำความสะอาดข้อมูลที่ LAO บันทึก “ล่าช้า/ผิดพลาด/ลงหมวดผิด” ก่อนเข้าสู่ฐานข้อมูลส่วนกลาง
  - Goal: ลดความผิดพลาดของข้อมูลดิบและทำให้ข้อมูลที่เข้าสู่ส่วนกลางมีมาตรฐานมากขึ้น
  - Required data/products: กฎ/โมเดลสำหรับตรวจจับความผิดปกติและการลงหมวดผิด; ขั้นตอน data cleaning/standardization; รายงานผลการคัดกรอง (เช่น flagged records) และวงจรการแก้ไขข้อมูล
  - Source anchors: [`Interview Summary DDPM.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20DDPM.md:58), [`Interview Summary DDPM.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20DDPM.md:60)

- Agency: DGA (Digital Government Development Agency)
  - Use case: ใช้โครงสร้างพื้นฐานกลางของ DGA (เช่น GDX และ CKAN/data.go.th) เพื่อรองรับการแลกเปลี่ยนข้อมูลที่ไม่เปิดเผย (confidential) และการเผยแพร่ข้อมูลเปิด (open data) แทนการสร้างระบบแลกเปลี่ยนข้อมูลใหม่ซ้ำซ้อน
  - Goal: ลดการลงทุนซ้ำซ้อนของโครงสร้างพื้นฐานการแลกเปลี่ยนข้อมูล และทำให้การออกแบบสถาปัตยกรรมของโครงการ CRDB สอดคล้องกับแนวทาง/แพลตฟอร์มภาครัฐที่ใช้อยู่แล้ว
  - Required data/products: แนวทางสถาปัตยกรรมการเชื่อมต่อกับ GDX สำหรับข้อมูลไม่เปิดเผย; แนวทางการเผยแพร่ Open Data ผ่าน data.go.th/CKAN; ข้อเสนอแนะในรายงานสุดท้ายให้ใช้ GDX สำหรับข้อมูลไม่เปิดเผย และใช้ data.go.th สำหรับข้อมูลเปิด
  - Source anchors: [`Interview Summary - DGA.md:L82-L88`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DGA.md:82), [`Interview Summary - DGA.md:L87-L88`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DGA.md:87)

- Agency: DGA (Digital Government Development Agency)
  - Use case: จัดชั้นข้อมูล (Data Classification) เพื่อกำหนดว่า “ข้อมูลใดต้องเป็นข้อมูลภายในเท่านั้น” “ข้อมูลใดแชร์แบบปลอดภัยผ่าน GDX ได้” และ “ข้อมูลใดต้องส่ง/เผยแพร่เป็น Open Data ผ่าน data.go.th”
  - Goal: ทำให้การกำกับดูแลข้อมูลภายในหน่วยงานและการแลกเปลี่ยน/เผยแพร่ข้อมูลทำได้ถูกต้องตามกรอบ Data Governance Framework (DGF) และลดความเสี่ยงด้านการเปิดเผยข้อมูลไม่เหมาะสม
  - Required data/products: แนวปฏิบัติ/เกณฑ์การจัดชั้นข้อมูลตาม DGA (3 กลุ่ม: internal / share via GDX / open data); กระบวนการ/คู่มือการจัดชั้นข้อมูลสำหรับหน่วยงาน; การอ้างอิงแนวทาง Data Classification ของ DGA ในงาน Data Governance Framework (WP3)
  - Source anchors: [`Interview Summary - DGA.md:L69-L72`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DGA.md:69), [`Interview Summary - DGA.md:L87-L88`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DGA.md:87)

- Agency: DGA (Digital Government Development Agency)
  - Use case: แก้ข้อกังวลด้าน PDPA ที่ทำให้หน่วยงาน “ปฏิเสธการแชร์ข้อมูล” ด้วยการทำ data masking / anonymization เพื่อแยก/ลบตัวระบุข้อมูลส่วนบุคคล และเผยแพร่ “ข้อมูลเพื่อการวิเคราะห์” เป็น Open Data ได้
  - Goal: ลดอุปสรรคการแชร์ข้อมูลภาครัฐที่อ้างเหตุผลข้อมูลส่วนบุคคล และเพิ่มความสามารถในการเผยแพร่ข้อมูลเปิดโดยไม่ละเมิดกฎหมายคุ้มครองข้อมูลส่วนบุคคล
  - Required data/products: แนวทาง/เทคนิค data masking และ anonymization สำหรับชุดข้อมูลภาครัฐ; หลักปฏิบัติในการแยก personal identifiers ออกจากข้อมูลแกนสำหรับการวิเคราะห์ก่อนเผยแพร่เป็น Open Data
  - Source anchors: [`Interview Summary - DGA.md:L78-L79`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DGA.md:78)

- Agency: DGA (Digital Government Development Agency)
  - Use case: ออกแบบ/ตัดสินใจสถาปัตยกรรม “Climate Data Hub” ของ DCCE (ผนวกเข้ากับ DCCE Agency Catalog เดิม หรือทำแพลตฟอร์มแยก) โดยต้องคำนึงว่าการเลือกสถาปัตยกรรมมีผลต่อคะแนน “Digital Government Readiness” KPI และควรปรึกษา DGA เพื่อเลือกโฮสต์หลักให้เหมาะกับการประเมิน
  - Goal: ให้การออกแบบคลังข้อมูล/แค็ตตาล็อกข้อมูลของ DCCE สอดคล้องกับการประเมิน Digital Government Readiness และเพิ่มคะแนน/ผลการประเมินของหน่วยงาน
  - Required data/products: เกณฑ์/คำแนะนำจาก DGA สำหรับการเลือกสถาปัตยกรรมแค็ตตาล็อกข้อมูล (integrate vs separate platform); ข้อกำหนด/แนวทางการเลือก primary host ที่สอดคล้องกับ KPI Digital Government Readiness; กลไกการปรึกษาหารือกับ DGA ระหว่างออกแบบระบบ
  - Source anchors: [`Interview Summary - DGA.md:L54-L61`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DGA.md:54)

- Agency: DGA (Digital Government Development Agency)
  - Use case: ใช้ GDX เป็น “ทางด่วนกลาง (highway)” เพื่อดึงข้อมูลการปล่อยก๊าซเรือนกระจก (GHG) ที่จำเป็นจากหน่วยงานผู้ถือข้อมูล (เช่น DIW และกระทรวงพลังงาน) เข้าสู่แพลตฟอร์มรายงาน GHG ของ DCCE โดยไม่ต้องสร้าง API แบบเชื่อมต่อรายคู่ (1-on-1) ใหม่
  - Goal: ทำให้การบูรณาการข้อมูล GHG สำหรับแพลตฟอร์มรายงานของ DCCE ทำได้รวดเร็วและลดต้นทุนการเชื่อมต่อแบบรายคู่
  - Required data/products: รายการชุดข้อมูล GHG ที่ต้องใช้จากหน่วยงานเป้าหมาย (เช่น 3–4 หน่วยงาน); การตรวจสอบว่ามี API ของชุดข้อมูลเหล่านี้อยู่บน GDX แล้วหรือไม่; แผนการประชุมเชิงเทคนิคเพื่อกำหนดชุดข้อมูลและแนวทางเชื่อมต่อผ่าน GDX
  - Source anchors: [`Interview Summary - DGA.md:L89-L91`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DGA.md:89)

- Agency: DLA (Department of Local Administration / สถ.)
  - Use case: จัดทำ “คลังข้อมูล/แหล่งอ้างอิงข้อมูลแบบรวมศูนย์ (centralized, easy-to-digest data repository)” ที่ อปท. สามารถอ้างอิงได้โดยตรง เพื่อใช้ประกอบการขออนุมัติงบและโครงการด้านความยืดหยุ่นต่อสภาพภูมิอากาศ
  - Goal: ลดแรงเสียดทานในการเข้าถึงข้อมูลสำหรับ อปท. และทำให้การอ้างอิงข้อมูลเพื่ออนุมัติงบ/โครงการทำได้รวดเร็ว
  - Required data/products: จุดเข้าถึงข้อมูลกลาง (single source of truth) พร้อมวิธีสืบค้นและสรุปผลแบบเข้าใจง่าย; ชุดข้อมูล/ตัวชี้วัดความเสี่ยงและผลกระทบที่ใช้เป็นหลักฐานเชิงนโยบาย; รูปแบบการอ้างอิง (citation/metadata) ที่หน่วยงานท้องถิ่นใช้ประกอบเอกสารอนุมัติงบได้
  - Source anchors: [`Interview Summary - DLA.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DLA.md:57), [`Interview Summary - DLA.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DLA.md:66)

- Agency: DLA (Department of Local Administration / สถ.)
  - Use case: เชื่อมโยง “ข้อมูลความเสี่ยงสภาพภูมิอากาศ” เข้ากับระบบ “e-MENSCR” เพื่อให้แผนท้องถิ่น–แผนจังหวัด–แผนชาติ สอดคล้องกัน และลดงานเอกสาร/การแปลความข้อมูลซ้ำซ้อน
  - Goal: ทำให้การจัดทำและติดตามแผนตามกรอบยุทธศาสตร์ชาติ/แผนปฏิบัติราชการที่ใช้ e-MENSCR ใช้ข้อมูลความเสี่ยงชุดเดียวกันและสอดคล้องกันทุกระดับ
  - Required data/products: มาตรฐานการแม็ปข้อมูลความเสี่ยง/ตัวชี้วัดเข้ากับโครงสร้าง e-MENSCR; กลไกเชื่อมต่อ/แลกเปลี่ยนข้อมูล (เช่น API หรือชุดข้อมูลที่อ้างอิงได้) ระหว่างคลังข้อมูลความเสี่ยงกับ e-MENSCR; คู่มือการใช้งานสำหรับท้องถิ่นและจังหวัด
  - Source anchors: [`Interview Summary - DLA.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DLA.md:61)

- Agency: DPT (Department of Public Works and Town & Country Planning)
  - Use case: พัฒนา/ใช้โครงสร้าง CRDB ที่ทำให้ “ข้อมูลเชิงพื้นที่แบบดิจิทัล (GIS-ready) + เมทาดาทาที่ดี + รูปแบบเชิงพื้นที่ที่อ่านได้ด้วยเครื่อง (machine-readable spatial formats)” สามารถค้นพบและนำไปใช้ซ้ำได้ข้ามหน่วยงาน เพื่อรองรับงานผังเมืองและวิศวกรรมหลายระดับพื้นที่ (multi-scale)
  - Goal: ลดภาระการขอข้อมูลแบบ ad hoc และการแปลงรูปแบบข้อมูลซ้ำๆ พร้อมทำให้ชุดข้อมูลที่อยู่ในแค็ตตาล็อก “นำไปใช้ได้จริง” ในงานวางแผนและออกแบบ (ไม่ใช่มีแค่รายการชื่อชุดข้อมูล)
  - Required data/products: ชุดข้อมูลเชิงพื้นที่ที่เป็นดิจิทัลและอ้างอิงพิกัด (แทนไฟล์กระดาษ/PDF); เมทาดาทาที่ชัดเจน (ผู้ดูแลข้อมูล ความละเอียด ขอบเขตการใช้ ข้อจำกัด); มาตรฐาน/รูปแบบข้อมูลเชิงพื้นที่ที่อ่านได้ด้วยเครื่อง; รายการชุดข้อมูลขั้นต่ำที่จำเป็นต่อการประเมินความเสี่ยง; แนวทาง/บริการข้อมูลที่เชื่อม “การคาดการณ์สภาพภูมิอากาศ” เข้ากับ workflow การออกแบบเชิงวิศวกรรม/ภาคส่วน
  - Source anchors: [`Interview Summary - DPT.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DPT.md:61), [`Interview Summary - DPT.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DPT.md:65), [`Interview Summary - DPT.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DPT.md:71), [`Interview Summary - DPT.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DPT.md:81)

- Agency: FTI (Federation of Thai Industries / สภาอุตสาหกรรมแห่งประเทศไทย)
  - Use case: ต้องการหน่วยงานกลาง (เช่น DCCE) ตรวจสอบ (verify) และประกาศชุดข้อมูลภัย (hazard data) ให้เป็น “แหล่งอ้างอิงเดียว (single source of truth)” เพื่อให้ภาคเอกชนรู้ว่าควรเชื่อถือชุดข้อมูลใดสำหรับการวางแผนทางการเงิน
  - Goal: ลดความสับสนจากข้อมูลน้ำ/ข้อมูลภัยที่มาจากหลายหน่วยงานไม่ประสานกัน และทำให้การเลือกใช้ข้อมูลเพื่อการวางแผนทางการเงินมีความน่าเชื่อถือ
  - Required data/products: กลไก/กระบวนการตรวจสอบและรับรองชุดข้อมูลภัย (รวมถึงข้อมูลน้ำ) และการประกาศชุดข้อมูลที่เป็น single source of truth
  - Source anchors: [`Interview Summary - FTI.md:L46-L47`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20FTI.md:46)

- Agency: FTI (Federation of Thai Industries / สภาอุตสาหกรรมแห่งประเทศไทย)
  - Use case: ขอให้มีพอร์ทัลแบบโต้ตอบ (interactive portal) พร้อม chatbot และข้อมูลผู้ติดต่อที่อัปเดต โดยชี้ว่าเว็บไซต์ภาครัฐ (รวมถึงเว็บไซต์ DCCE) “ล่มบ่อย” เบอร์ติดต่อไม่รับสาย และการเปลี่ยนคนทำงานสูงทำให้สูญเสียความรู้
  - Goal: ลดอุปสรรคการเข้าถึงข้อมูล/การติดต่อประสานงาน และลดการสูญเสียความรู้จากการเปลี่ยนคนทำงาน (knowledge loss)
  - Required data/products: พอร์ทัลแบบโต้ตอบ (interactive portal) พร้อม chatbot; รายชื่อ/ช่องทางติดต่อที่อัปเดต; กลไกดูแลความต่อเนื่องของความรู้/ข้อมูลผู้รับผิดชอบ
  - Source anchors: [`Interview Summary - FTI.md:L48-L49`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20FTI.md:48)

- Agency: FTI (Federation of Thai Industries / สภาอุตสาหกรรมแห่งประเทศไทย)
  - Use case: สร้างแรงจูงใจให้ภาคเอกชนยอมแชร์ข้อมูล โดยต้องสื่อสาร “คุณค่าทางธุรกิจ” ของการแชร์ข้อมูลอย่างชัดเจน และเสนอให้สร้าง “Data User Community” เพื่อแชร์การวิเคราะห์และสร้างความร่วมมือ
  - Goal: เพิ่มความร่วมมือและการแชร์ข้อมูลจากภาคเอกชนด้วยแรงจูงใจจากคุณค่าทางธุรกิจและชุมชนผู้ใช้ข้อมูล
  - Required data/products: แนวทาง/การสื่อสารคุณค่าทางธุรกิจของการแชร์ข้อมูล; กลไก/โครงสร้างชุมชนผู้ใช้ข้อมูล (Data User Community) เพื่อแชร์การวิเคราะห์และสร้างความร่วมมือ
  - Source anchors: [`Interview Summary - FTI.md:L50-L51`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20FTI.md:50)

- Agency: NXPO (Office of National Higher Education Science Research and Innovation Policy Council)
  - Use case: ทำให้มี “ข้อมูลฐาน/ค่า baseline และมาตรฐานข้อมูลเดียว” สำหรับการทำแบบจำลองระดับชาติ (แก้ปัญหาหน่วยงานเก็บตัวแปรเดียวกันแต่ได้ตัวเลขต่างกัน) โดยต้องมีหน่วยงาน/กลไกที่ “ตรวจสอบ (verify) และประกาศ” แหล่งอ้างอิงเดียว (single source of truth)
  - Goal: ลดความไม่สอดคล้องของข้อมูลพื้นฐานที่ใช้ในแบบจำลอง และทำให้การวิเคราะห์ระดับชาติยึดชุดข้อมูลอ้างอิงเดียวที่เชื่อถือได้
  - Required data/products: baseline/ชุดข้อมูลอ้างอิงที่เป็นมาตรฐาน (unified baseline); กระบวนการตรวจสอบ/รับรองข้อมูล (verification) และกลไกประกาศ single source of truth; แนวทาง/เอกสารกำกับเพื่อให้หน่วยงานต่าง ๆ ใช้ baseline เดียวกัน
  - Source anchors: [`Interview Summary - NXPO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NXPO.md:49)

- Agency: NXPO (Office of National Higher Education Science Research and Innovation Policy Council)
  - Use case: จัดทำ/รื้อฟื้น “Thailand Assessment Reports” (ลักษณะคล้ายรายงาน IPCC) เพื่อเป็นฐานข้อมูลมหภาค (macro-data) ที่จำเป็นต่อการกำหนดนโยบาย
  - Goal: ให้ผู้กำหนดนโยบายมีชุดรายงานประเมินระดับประเทศที่ครอบคลุม เป็นฐานสำหรับการออกแบบนโยบายและการกำหนดทิศทางการวิจัย
  - Required data/products: รายงาน Thailand Assessment Reports (ฉบับครอบคลุม); ชุดข้อมูล/สาระสรุประดับมหภาคสำหรับนโยบายที่อ้างอิงได้; กลไกการอัปเดต/ทบทวนรายงานเป็นระยะ
  - Source anchors: [`Interview Summary - NXPO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NXPO.md:53)

- Agency: NXPO (Office of National Higher Education Science Research and Innovation Policy Council)
  - Use case: ออกแบบแพลตฟอร์ม CRDB ให้เป็น “Clearinghouse/Shopping Mall” ที่ลิงก์ไปยังข้อมูลภายนอก (แทนการเป็นเจ้าของข้อมูลทั้งหมด) โดยอ้างอิงแนวทาง “Climate-ADAPT (EU)” เพื่อให้เหมาะกับข้อจำกัดด้านสถาบันและการแชร์ข้อมูล
  - Goal: ทำให้ CRDB ใช้งานได้จริงภายใต้บริบทไทยที่มีอุปสรรคด้านการถือครอง/การแชร์ข้อมูล และเพิ่มโอกาสการเข้าถึงข้อมูลผ่านการเชื่อมโยงแหล่งภายนอก
  - Required data/products: สถาปัตยกรรม/แนวทางการทำ Clearinghouse ที่เน้นการลิงก์ชุดข้อมูลภายนอก; ฟังก์ชันค้นหาและลิงก์ไปยังแหล่งข้อมูลภายนอกพร้อมเมทาดาทา; แนวทางอ้างอิง/เทียบเคียงกับ Climate-ADAPT (EU)
  - Source anchors: [`Interview Summary - NXPO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NXPO.md:63)

- Agency: NSO (National Statistical Office)
  - Use case: จัดทำ “Framework for the Development of Environment Statistics (FDES)” ในบริบทไทย และผ่านกระบวนการคณะกรรมการสถิติรายสาขาเพื่อ (1) ตรวจสอบข้อมูลที่มีอยู่ (2) จัด tier (Tier 1: เผยแพร่สม่ำเสมอ, Tier 2: ใช้ภายใน, Tier 3: ยังไม่ผลิต) และ (3) มอบหมายหน่วยงานผู้รับผิดชอบการผลิตข้อมูลอย่างเป็นทางการ
  - Goal: ทำให้รายการสถิติสิ่งแวดล้อมเป็นระบบ มาตรฐาน และระบุ “ใครผลิตข้อมูลอะไร” อย่างชัดเจน เพื่อรองรับระบบสถิติทางการ
  - Required data/products: รายการสถิติภายใต้ FDES (6 components / 21 sub-components) ที่แม็ปกับหน่วยงาน; เกณฑ์การจัด tier และผลการจัด tier; มติ/เอกสารมอบหมายหน่วยงานผู้รับผิดชอบการผลิตข้อมูล
  - Source anchors: [`Interview Summary - NSO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NSO.md:33), [`Interview Summary - NSO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NSO.md:39)

- Agency: NSO (National Statistical Office)
  - Use case: พัฒนา “Natural Resources and Environment Statistical Data Center” ให้เป็นศูนย์กลาง โดย (ก) ถ้าชุดข้อมูลอยู่บน Government Data Catalog (GD Catalog) ให้ดึงมาใช้ และ (ข) ถ้าชุดข้อมูลอยู่บนเว็บไซต์หน่วยงาน ให้ “ลิงก์ไปยัง URL ต้นทาง” โดยไม่คัดลอกข้อมูลดิบ
  - Goal: ทำหน้าที่เป็นศูนย์กลางการค้นพบข้อมูลสิ่งแวดล้อม/ทรัพยากรธรรมชาติแบบรวมศูนย์ โดยยังคงอ้างอิงแหล่งข้อมูลต้นทางอย่างเป็นทางการ
  - Required data/products: รายการชุดข้อมูลที่ดึงจาก GD Catalog; กลไกการลิงก์ชุดข้อมูลที่อยู่บนเว็บไซต์หน่วยงาน (URL linking); แนวทาง/มาตรฐานการอ้างอิงแหล่งข้อมูลต้นทาง
  - Source anchors: [`Interview Summary - NSO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NSO.md:41), [`Interview Summary - NSO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NSO.md:43)

- Agency: NSO (National Statistical Office)
  - Use case: ใช้ระบบ tag กลางในการจัดการข้อมูล โดย tag ชุดข้อมูลจากหลายหน่วยงานตามกรอบมาตรฐาน (เช่น FDES) เพื่อให้ผู้ใช้ค้นพบชุดข้อมูลเดียวกันได้จากหลายมุมมองเชิงธีม
  - Goal: เพิ่มความสามารถในการค้นหา/ค้นพบ (discoverability) และการจัดหมวดหมู่ข้อมูลแบบข้ามธีมโดยไม่ทำซ้ำชุดข้อมูล
  - Required data/products: โครงสร้าง/มาตรฐาน tag กลาง; mapping ระหว่าง tag กับกรอบมาตรฐาน (เช่น FDES); ฟังก์ชันค้นหาหลายมุมมองที่อิง tag
  - Source anchors: [`Interview Summary - NSO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NSO.md:44)

- Agency: NSO (National Statistical Office)
  - Use case: ทำ capacity building ให้หน่วยงานเจ้าของข้อมูลเพื่อให้ข้อมูลบน GD Catalog มีคุณภาพ โดยเน้นโครงสร้างข้อมูล/รูปแบบมาตรฐานสำหรับแลกเปลี่ยน และการแนบเมทาดาทาที่ครบถ้วน (ความถี่การปรับปรุง, นิยาม, project tags) ก่อนอัปโหลด
  - Goal: ยกระดับคุณภาพข้อมูลและเมทาดาทาบน GD Catalog เพื่อให้ข้อมูลใช้งานได้จริงและตีความได้ถูกต้อง
  - Required data/products: มาตรฐานรูปแบบ/โครงสร้างข้อมูลสำหรับแลกเปลี่ยน; ข้อกำหนดเมทาดาทาขั้นต่ำ (revision frequency, definitions, tags); คู่มือ/สื่ออบรมสำหรับหน่วยงานผู้ผลิตข้อมูล
  - Source anchors: [`Interview Summary - NSO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NSO.md:71)

- Agency: NSO (National Statistical Office)
  - Use case: เป็น “International Data Focal Point” ประสานหน่วยงานในประเทศเพื่อรวบรวมข้อมูลที่องค์กรระหว่างประเทศร้องขอ และจัดทำให้เป็น “official national dataset” ชุดเดียวเพื่อส่งมอบตามพันธกรณีระหว่างประเทศ
  - Goal: ส่งมอบชุดข้อมูลระดับชาติที่เป็นทางการและสอดคล้องกัน สำหรับการรายงาน/ข้อผูกพันต่อองค์กรระหว่างประเทศ
  - Required data/products: กลไกประสาน/ดึงข้อมูลจากหลายหน่วยงาน; กระบวนการรวม/จัดรูปแบบให้เป็นชุดข้อมูลชาติชุดเดียว (single official national dataset); เอกสารกำกับนิยาม/เมทาดาทาเพื่อความสอดคล้อง
  - Source anchors: [`Interview Summary - NSO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NSO.md:18)

- Agency: OTP (Office of Transport and Traffic Policy and Planning / สนข.)
  - Use case: ต้องการ “ข้อมูลคาดการณ์สภาพภูมิอากาศระยะยาวที่เป็นทางการและได้รับการยอมรับสูง” (โดยเฉพาะการคาดการณ์เชิงอุทกวิทยา) เพื่อให้ใช้ซ้ำได้เป็นประจำทุกปีในทุกกระทรวงสำหรับงานวางแผน/ประเมินความเสี่ยงและการปรับตัว
  - Goal: มีชุดข้อมูลคาดการณ์ระยะยาวที่เป็นแหล่งอ้างอิงร่วม (authoritative / highly accepted) สำหรับการใช้งานข้ามหน่วยงานอย่างต่อเนื่องรายปี
  - Required data/products: ชุดข้อมูลคาดการณ์สภาพภูมิอากาศระยะยาวที่ได้รับการยอมรับ (โดยเฉพาะ hydrological projections) ที่หน่วยงานต่าง ๆ นำไปใช้ได้รายปี; รูปแบบการให้บริการ/การเผยแพร่ที่รองรับการนำไปใช้ซ้ำ
  - Source anchors: [`Interview Summary - OTP.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20OTP.md:73)

- Agency: OTP (Office of Transport and Traffic Policy and Planning / สนข.)
  - Use case: ศูนย์ข้อมูลกระทรวงคมนาคม (Open Data) — รวมศูนย์ข้อมูลคมนาคม (เช่น OD, ทะเบียนรถ, พลังงาน/เชื้อเพลิง, พื้นที่เชิงพื้นที่, เส้นทาง, อุบัติเหตุ) เพื่อให้ประชาชนเข้าถึงผ่านแดชบอร์ด และให้หน่วยงานรัฐอื่น “ขอเชื่อมระบบ” เพื่อดาวน์โหลดข้อมูลดิบเชิงเทคนิค (เช่น Shapefiles, Excel) ไปวิเคราะห์ต่อ
  - Goal: ทำให้การเข้าถึง/ใช้ข้อมูลคมนาคมเป็นระบบเดียว ใช้ได้ทั้งการสื่อสารสาธารณะ (dashboard) และการวิเคราะห์เชิงเทคนิคของหน่วยงานรัฐอื่น (raw downloads / integration)
  - Required data/products: แดชบอร์ดสาธารณะ; ช่องทาง/กระบวนการเชื่อมระบบสำหรับหน่วยงานรัฐ (ผ่านหนังสือราชการ) เพื่อเข้าถึงและดาวน์โหลดข้อมูลดิบ (เช่น Shapefiles, Excel)
  - Source anchors: [`Interview Summary - OTP.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20OTP.md:33), [`Interview Summary - OTP.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20OTP.md:37), [`Interview Summary - OTP.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20OTP.md:39)
