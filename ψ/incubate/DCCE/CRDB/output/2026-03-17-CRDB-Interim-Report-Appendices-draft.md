# ร่างภาคผนวกรายงานความก้าวหน้าระหว่างดำเนินงาน CRDB — CDM, Use Cases, and Sitemap draft

## ภาคผนวก ก รายละเอียดแบบจำลองข้อมูลเชิงแนวคิดสำหรับระบบข้อมูลความเสี่ยงและการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศ

### วัตถุประสงค์ของภาคผนวกส่วนนี้

ภาคผนวกส่วนนี้จัดทำขึ้นเพื่ออธิบายรายละเอียดของ **แบบจำลองข้อมูลเชิงแนวคิด** ที่ใช้เป็นฐานในการออกแบบโครงสร้างข้อมูลสำหรับโครงการพัฒนาชุดข้อมูลองค์ความรู้ความเสี่ยงและผลกระทบจากการเปลี่ยนแปลงสภาพภูมิอากาศของประเทศไทย โดยมีจุดประสงค์เพื่อให้ผู้อ่านเห็นทั้งขอบเขตของข้อมูลหลัก โครงสร้างความสัมพันธ์ระหว่างองค์ประกอบต่าง ๆ และตรรกะการออกแบบที่รองรับการพัฒนากรอบข้อมูลสารสนเทศด้านการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศของประเทศ

ในเนื้อหาหลักของรายงาน บทที่ 1 อธิบายบทบาทของแบบจำลองข้อมูลเชิงแนวคิดในฐานะหลักการจัดระเบียบข้อมูลและเป็นส่วนหนึ่งของสถาปัตยกรรมข้อมูลสารสนเทศของ NCAIF แต่เพื่อไม่ให้เนื้อหาหลักมีความหนาแน่นทางเทคนิคเกินไป รายละเอียดของ subject area, sub-domain, entity สำคัญ และตรรกะการออกแบบเชิงข้อมูลทั้งหมดจึงถูกรวบรวมไว้ในภาคผนวกนี้โดยเฉพาะ

### ภาพรวมของขอบเขตข้อมูลหลักของ CDM

แบบจำลองข้อมูลเชิงแนวคิดของโครงการนี้ได้รับการออกแบบให้ทำหน้าที่เชื่อมระหว่าง **ความเข้มงวดเชิงวิทยาศาสตร์** กับ **ความต้องการใช้งานเชิงนโยบายและการจัดการข้อมูล** กล่าวคือ ในด้านหนึ่งต้องสามารถรองรับกรอบความคิดจาก IPCC, WMO, Sendai Framework และ ISO ได้อย่างสอดคล้อง ขณะเดียวกันก็ต้องสามารถเชื่อมต่อไปสู่การใช้งานจริงในบริบทของการวางแผน การประเมินความเสี่ยง การบันทึกผลกระทบ และการกำหนดมาตรการปรับตัวในระบบของกรมฯ ได้

ในเชิงโครงสร้าง แบบจำลองดังกล่าวประกอบด้วย **สี่ขอบเขตข้อมูลหลัก** ได้แก่

1. **ขอบเขตข้อมูลด้านสภาพภูมิอากาศและตัวขับการเปลี่ยนแปลง** ซึ่งทำหน้าที่อธิบายปัจจัยต้นเหตุหรือแรงขับของการเปลี่ยนแปลงสภาพภูมิอากาศ รวมถึงข้อมูลภาพฉายและข้อมูลเหตุการณ์อันตรายที่เกี่ยวข้อง
2. **ขอบเขตข้อมูลด้านการประเมินความเสี่ยงและผลกระทบ** ซึ่งเป็นแกนกลางของการเชื่อมข้อมูลภัย การเผชิญภัย ความเปราะบาง และผลกระทบที่เกิดขึ้นจริงเข้าด้วยกัน
3. **ขอบเขตข้อมูลด้านการประเมินความยืดหยุ่นหรือศักยภาพในการรับมือ** ซึ่งใช้รองรับการประเมินขีดความสามารถของพื้นที่หรือระบบสังคมในการรับมือและฟื้นตัวจากความเสี่ยง
4. **ขอบเขตข้อมูลด้านการวางแผนและดำเนินการปรับตัว** ซึ่งเชื่อมผลการประเมินความเสี่ยงไปสู่ทางเลือก มาตรการ โครงการ การประเมินทางเลือก และผลลัพธ์ของการดำเนินงาน

การแบ่งขอบเขตเช่นนี้ทำให้ระบบสามารถจัดระเบียบข้อมูลจำนวนมากที่มีแหล่งกำเนิดและวัตถุประสงค์ต่างกันให้อยู่ในภาพรวมเดียว โดยแต่ละขอบเขตมีตรรกะภายในของตนเอง แต่สามารถเชื่อมต่อกับขอบเขตอื่นผ่านความสัมพันธ์ที่กำหนดไว้อย่างชัดเจน

### Subject Area 1: ข้อมูลด้านสภาพภูมิอากาศ (Climate Science)

ขอบเขตข้อมูลส่วนแรกทำหน้าที่รองรับข้อมูลต้นเหตุและข้อมูลพื้นฐานด้านภูมิอากาศ ซึ่งเป็นฐานสำคัญของการประเมินความเสี่ยงในระบบทั้งหมด ภายใน subject area นี้ มีองค์ประกอบสำคัญดังนี้

#### ตัวขับด้านภูมิอากาศ (`CLIMATE_DRIVER`)

หน่วยข้อมูลนี้ทำหน้าที่เก็บข้อมูลเกี่ยวกับปัจจัยด้านภูมิอากาศที่มีผลต่อการก่อให้เกิดความเสี่ยง เช่น ตัวแปรด้านอุณหภูมิ ปริมาณฝน สัญญาณภูมิอากาศ และตัวชี้วัดสภาพภูมิอากาศที่เกี่ยวข้อง โดยอ้างอิงแนวคิดจาก IPCC CID และ GCOS ECVs ข้อมูลในส่วนนี้ควรรองรับคุณลักษณะสำคัญ เช่น โดเมนของข้อมูล ความละเอียดเชิงพื้นที่ ความละเอียดเชิงเวลา และระดับความไม่แน่นอน

#### ภาพฉายสถานการณ์ภูมิอากาศ (`CLIMATE_SCENARIO`)

หน่วยข้อมูลนี้รองรับข้อมูลภาพฉาย เช่น SSP หรือ RCP จากแบบจำลองภูมิอากาศ ซึ่งทำหน้าที่เป็น parent entity ของข้อมูล climate driver ในบริบทเชิงอนาคต การกำหนดให้ scenario เป็นหน่วยข้อมูลที่มีสถานะชัดเจน ทำให้ระบบสามารถติดป้ายกำกับได้ว่าข้อมูลตัวใดมาจากเส้นทางการพัฒนาใด และช่วยให้รองรับการใช้งานเชิงอนาคตได้อย่างเป็นระบบ ไม่จำกัดอยู่เพียงการบันทึกข้อมูลย้อนหลัง

#### เหตุการณ์อันตราย (`HAZARDOUS_EVENT`)

หน่วยข้อมูลนี้ใช้บันทึกเหตุการณ์อันตรายแบบ discrete event เช่น พายุ ภัยแล้ง หรือเหตุการณ์รุนแรงเฉพาะครั้ง โดยออกแบบให้สามารถอ้างอิงรหัสเหตุการณ์แบบไม่ซ้ำซ้อนตามตรรกะที่สอดคล้องกับ WMO-CHE UUIDs ได้ในอนาคต จุดสำคัญของ entity นี้คือช่วยเชื่อมระหว่างข้อมูลภัยในเชิงเหตุการณ์กับข้อมูลผลกระทบที่เกิดขึ้นจริงในภายหลัง

#### การสังเกตการณ์จากดาวเทียม (`SATELLITE_OBSERVATION`)

หน่วยข้อมูลนี้รองรับข้อมูลการสังเกตการณ์ระยะไกลที่ใช้จับขอบเขตของภัยหรือใช้สนับสนุนการสร้าง observed hazard maps โดยมีบทบาทสำคัญในการเชื่อมโลกของข้อมูลสังเกตการณ์จริงเข้ากับระบบประเมินภัยและความเสี่ยง

### Subject Area 2: การประเมินความเสี่ยงและผลกระทบ (Risk and Impact Assessment)

ขอบเขตนี้เป็นส่วนที่มีความสำคัญที่สุดในแบบจำลองข้อมูลเชิงแนวคิดของโครงการ เพราะทำหน้าที่เป็นแกนกลางที่เชื่อมข้อมูลต้นเหตุ ข้อมูลทรัพย์สินและประชากรที่ได้รับผลกระทบ ข้อมูลความเปราะบาง วิธีการคำนวณความเสี่ยง และข้อมูลผลกระทบจริงเข้าด้วยกันอย่างเป็นระบบ ภายในขอบเขตนี้ สามารถแยกเป็น sub-area หลักได้สี่ส่วน

#### Sub-area 2.1: Hazard Modeling

ส่วนนี้ทำหน้าที่แปลงข้อมูลภูมิอากาศและข้อมูลแวดล้อมที่เกี่ยวข้องไปสู่ผลลัพธ์ในรูปของแผนที่ภัยอันตราย

องค์ประกอบสำคัญ ได้แก่

- **`HAZARD_MODELS`** ซึ่งเป็นหน่วยข้อมูลที่ทำหน้าที่เป็น registry ของแบบจำลอง ไม่ว่าจะแบบจำลองอุทกวิทยา แบบจำลองไฟป่า หรือแบบจำลองลม โดยระบบจะติดตามเฉพาะว่ามี input อะไร และสร้าง output อะไร โดยไม่ผูกกับฟิสิกส์ภายในของแบบจำลองโดยตรง
- input ที่เกี่ยวข้องกับ `HAZARD_MODELS` ได้แก่ `CLIMATE_DRIVER`, `METEOROLOGICAL_OBSERVATION`, `TOPOGRAPHY`, และ `ENVIRONMENT`
- **`HAZARD_MAP`** ซึ่งเป็นผลลัพธ์เชิงพื้นที่ของการประเมินภัย โดยอาจเกิดจากการจำลองผ่าน `HAZARD_MODELS` หรือเกิดจากข้อมูลที่สังเกตการณ์จริงผ่าน `SATELLITE_OBSERVATION`

จุดสำคัญของส่วนนี้ คือการรักษาหลัก **model agnosticism** กล่าวคือ ฐานข้อมูลไม่จำเป็นต้อง “รู้” กลไกเชิงวิทยาศาสตร์ทั้งหมดของแบบจำลอง แต่ต้องรู้ให้ชัดว่า input และ output ของแบบจำลองคืออะไร ใช้กับพื้นที่ใด และอยู่ภายใต้ scenario หรือเงื่อนไขใด

#### Sub-area 2.2: Vulnerability & Exposure

ส่วนนี้ทำหน้าที่กำหนดว่ามีอะไรอยู่ในพื้นที่เสี่ยง และความเปราะบางนั้นถูกนิยามหรือคำนวณอย่างไร

องค์ประกอบสำคัญ ได้แก่

- **`SPATIAL_UNIT`** ซึ่งเป็น geometric super-type สำหรับรองรับหน่วยเชิงพื้นที่หลายแบบ ไม่ว่าจะเป็น DGGS, HydroBASINS หรือขอบเขตการปกครอง
- **`EXPOSED_ASSET`** ซึ่งใช้แทนองค์ประกอบของสังคมและระบบที่อาจได้รับผลกระทบ เช่น ประชากร โครงสร้างพื้นฐาน หรือทรัพย์สินประเภทต่าง ๆ
- **`VULNERABILITY_DEFINITION`** ซึ่งเป็นหน่วยข้อมูลกลางสำหรับนิยามความเปราะบาง ไม่ว่าจะในรูปของความสัมพันธ์เชิงคณิตศาสตร์หรือกรอบดัชนี
- **`IMPACT_FUNCTION`** ซึ่งใช้รองรับตรรกะเชิงคณิตศาสตร์ เช่น depth-damage curve สำหรับการคำนวณเชิง actuarial หรือการวิเคราะห์ผลกระทบเชิงกายภาพ
- **`VULNERABILITY_FRAMEWORK`** ซึ่งใช้รองรับกรอบดัชนีเชิงนโยบายหรือเชิงสังคม เช่น social vulnerability index
- **`FRAMEWORK_STRUCTURE`** ซึ่งเป็น logic layer เชื่อมตัวแปรทั่วไปเข้ากับ dimension เฉพาะของกรอบ เช่น sensitivity หรือ adaptive capacity
- **`VULNERABILITY_DETERMINANT`** ซึ่งเป็นคลังตัวแปรกลางของตัวชี้วัดทางสังคมและเศรษฐกิจ

การออกแบบส่วนนี้ตั้งอยู่บนหลัก **determinant neutrality** กล่าวคือ ตัวแปรสังคมและเศรษฐกิจควรถูกเก็บในฐานะข้อเท็จจริงกลาง แล้วค่อยถูกตีความภายใต้ framework เฉพาะในภายหลัง วิธีนี้ทำให้ตัวแปรเดียวกันสามารถถูกนำไปใช้ได้หลายกรอบโดยไม่ซ้ำซ้อน

#### Sub-area 2.4: Risk Assessment Outputs

ส่วนนี้ทำหน้าที่บันทึกเหตุการณ์ของการคำนวณความเสี่ยงและผลลัพธ์ที่เกิดขึ้นจากการประเมิน

องค์ประกอบสำคัญ ได้แก่

- **`RISK_ASSESSMENT`** ซึ่งทำหน้าที่บันทึกการประเมินความเสี่ยงแต่ละครั้ง และสามารถเชื่อมได้ทั้งกับ `HAZARD_MAP` และ `CLIMATE_DRIVER` เพื่อรองรับทั้ง physical assessment และ index-based assessment
- **`RISK_METRIC`** ซึ่งรองรับผลลัพธ์เชิงปริมาณหรือเชิงความน่าจะเป็น เช่น Average Annual Loss หรือ metric อื่นที่คำนวณจาก impact function
- **`COMPOSITE_INDEX`** ซึ่งรองรับผลลัพธ์เชิงดัชนีหรือคะแนนรวม เช่น normalized score หรือ qualitative score

ตรรกะสำคัญในส่วนนี้คือ **dual-path risk assessment** กล่าวคือ ระบบเดียวต้องรองรับได้ทั้งการประเมินจาก hazard map และการประเมินเชิงดัชนีโดยไม่ต้องแยก schema ออกเป็นคนละระบบ

#### Sub-area 2.5: Impact, Loss & Damage

ส่วนนี้ทำหน้าที่เชื่อมการประเมินความเสี่ยงเข้ากับผลกระทบที่เกิดขึ้นจริงและการบันทึกความเสียหาย

องค์ประกอบสำคัญ ได้แก่

- **`DISASTER_RECORD`** ซึ่งใช้แทนเหตุการณ์ภัยพิบัติที่เกิดขึ้นจริงพร้อมข้อมูลสรุป เช่น ผู้ได้รับผลกระทบ ระยะเวลา หรือความเสียหายรวม
- **`LOSS_DAMAGE_RECORD`** ซึ่งใช้เก็บข้อมูลเชิงประวัติของผลกระทบหรือความเสียหายที่เกิดขึ้นจริงกับทรัพย์สินหรือองค์ประกอบที่ได้รับผลกระทบ
- **`ATTRIBUTION_LINK`** ซึ่งทำหน้าที่เป็น aggregated attribution summary ที่เชื่อม `LOSS_DAMAGE_RECORD` เข้ากับ `CLIMATE_DRIVER` เมื่อมีหลักฐานผลกระทบเพียงพอ

หลักการสำคัญในส่วนนี้คือ **loss-driven attribution** กล่าวคือ ระบบจะไม่เชื่อม attribution แบบตรงจาก climate driver หรือ event ไปยังข้อสรุปเชิงสาเหตุโดยปราศจากข้อมูลความสูญเสียที่เกิดขึ้นจริง เพื่อหลีกเลี่ยงการอ้างเหตุผลเชิงสาเหตุที่เกินหลักฐาน

### Subject Area 3: การประเมินความยืดหยุ่น (Resilience Assessment)

ขอบเขตนี้ทำหน้าที่รองรับการประเมินศักยภาพในการรับมือและฟื้นตัวของพื้นที่หรือระบบสังคม ซึ่งแตกต่างจากการประเมินความเสี่ยงเชิงกายภาพโดยตรง ภายในขอบเขตนี้ ประกอบด้วยองค์ประกอบสำคัญ ได้แก่

- **`RESILIENCE_FRAMEWORK`** ซึ่งเป็นกรอบวิธีการหลัก
- **`RESILIENCE_DIMENSION`** ซึ่งใช้แบ่งมิติ เช่น social, economic, institutional
- **`RESILIENCE_STRUCTURE`** ซึ่งกำหนด logic การรวมตัวแปรภายในแต่ละมิติ
- **`RESILIENCE_ASSESSMENT`** ซึ่งเป็นการนำ framework ไปใช้กับ `SPATIAL_UNIT` เพื่อสร้างผลลัพธ์ในรูป `COMPOSITE_INDEX`

จุดแข็งของการออกแบบส่วนนี้คือรองรับ **recursive aggregation** หรือการรวมคะแนนแบบหลายชั้นได้ ทำให้สามารถแทนทั้ง national index, provincial sub-index, thematic score และ indicator score ภายใต้ตรรกะเดียวกัน

### Subject Area 4: การวางแผนและดำเนินการปรับตัว

ขอบเขตนี้ใช้รองรับวงจรการตัดสินใจและการดำเนินมาตรการปรับตัวตามตรรกะที่สอดคล้องกับ ISO 14090 โดยมีองค์ประกอบสำคัญ ได้แก่

- **`DECISION_CONTEXT`** กำหนดบริบท ปัญหา และระดับความไม่แน่นอนของการวางแผน
- **`RISK_TOLERANCE_PROFILE`** ใช้บันทึกระดับการยอมรับความเสี่ยงของผู้มีส่วนได้ส่วนเสีย
- **`ADAPTATION_PORTFOLIO`** ใช้จัดกลุ่มหลาย `ADAPTATION_OPTION`
- **`ADAPTATION_OPTION`** เป็นคลังทางเลือกของมาตรการปรับตัว
- **`APPRAISAL_EVENT`** ใช้บันทึกกระบวนการประเมินทางเลือก
- **`APPRAISAL_METRIC`** ใช้เก็บผลการประเมินรายตัวชี้วัด
- **`ADAPTATION_PROJECT`** ใช้แทนโครงการหรือการดำเนินการจริงในพื้นที่
- **`INTERVENTION_RESULT`** ใช้เก็บผลลัพธ์หรือ KPI ของการดำเนินการ

ตรรกะสำคัญของส่วนนี้คือ **adaptation as a cycle** ไม่ใช่โครงการครั้งเดียว กล่าวคือ ผลของโครงการหนึ่งควรย้อนกลับไปเป็น baseline หรือข้อมูลนำเข้าให้กับการประเมินรอบถัดไปได้ผ่านกลไก feedback loop

### ตรรกะการเชื่อมโยงข้อมูลระหว่าง subject areas

เมื่อมองทั้งระบบร่วมกัน จะเห็นว่า subject areas ทั้งสี่ไม่ได้แยกขาดจากกัน แต่เชื่อมต่อกันตามตรรกะของการใช้งานจริง ดังนี้

1. `CLIMATE_SCENARIO` และ `CLIMATE_DRIVER` เป็นฐานของการทำความเข้าใจสภาพภูมิอากาศและอนาคต
2. ข้อมูลดังกล่าวถูกนำเข้าสู่ `HAZARD_MODELS` เพื่อสร้าง `HAZARD_MAP`
3. `HAZARD_MAP` เชื่อมกับ `EXPOSED_ASSET`, `SPATIAL_UNIT`, และ `VULNERABILITY_DEFINITION` ผ่าน `RISK_ASSESSMENT`
4. ผลของ `RISK_ASSESSMENT` อาจออกมาเป็น `RISK_METRIC` หรือ `COMPOSITE_INDEX`
5. เมื่อเกิดเหตุการณ์จริง `DISASTER_RECORD` และ `LOSS_DAMAGE_RECORD` จะทำหน้าที่สะท้อนผลกระทบจริง และอาจเชื่อมกับ `ATTRIBUTION_LINK`
6. ผลการประเมินความเสี่ยงและผลกระทบเหล่านี้สามารถเชื่อมต่อไปยัง `ADAPTATION_OPTION`, `ADAPTATION_PROJECT`, และ `INTERVENTION_RESULT` ใน subject area ด้านการวางแผนและดำเนินการปรับตัว


## ภาคผนวก ข รายละเอียดกรณีการใช้งานและเส้นทางการใช้งานของผู้ใช้

### วัตถุประสงค์ของภาคผนวกส่วนนี้

ภาคผนวกส่วนนี้จัดทำขึ้นเพื่อรวบรวมรายละเอียดของกรณีการใช้งานและเส้นทางการใช้งานของผู้ใช้ ซึ่งเป็นฐานสำคัญของการออกแบบ NCAIF และการเลือกผลิตภัณฑ์ขั้นต่ำในระยะที่ 1 เนื้อหาส่วนนี้ช่วยให้ผู้อ่านเห็นว่า การออกแบบระบบไม่ได้เกิดจากการจัดหมวดหมู่ข้อมูลตามมุมมองของผู้พัฒนาเพียงอย่างเดียว แต่เกิดจากการสังเคราะห์ความต้องการใช้งานจริงที่ปรากฏจากการสัมภาษณ์ stakeholder และการหารือเชิงปฏิบัติการ

### ข.2 วิธีสังเคราะห์กรณีการใช้งาน

กรณีการใช้งานในภาคผนวกนี้สังเคราะห์จากข้อสังเกตใน workshop ภายในหน่วยงานและ stakeholder interview summaries โดยกระบวนการสังเคราะห์ไม่ได้มุ่งทำรายการแยกหน่วยงานแบบตรงตัวเท่านั้น แต่พยายามสกัด **รูปแบบการใช้งานซ้ำ** ที่ปรากฏร่วมกัน across agencies เช่น ความต้องการ briefing packs, การประเมินผลกระทบหลังเหตุการณ์, ความต้องการ recommended baseline, และความจำเป็นของการตีความข้อมูลที่มีความไม่แน่นอนอย่างปลอดภัย

### ข.3 ชุดกรณีการใช้งานหลัก

#### ข.3.1 UC-01 — การประเมินผลกระทบหลังเหตุการณ์และ loss & damage

**Primary user:** นักวิเคราะห์ของ DCCE และ focal point ของหน่วยงานด้านภัยพิบัติ  
**Trigger:** เกิดเหตุการณ์น้ำท่วม ภัยแล้ง คลื่นความร้อน หรือเหตุการณ์อันตรายอื่นที่ต้องมีการสรุปผลกระทบ

**User journey ขั้นต่ำ**
1. เลือกเหตุการณ์ตามพื้นที่ เวลา และประเภทภัย
2. ตรวจสอบจำนวนประชากรและทรัพย์สินที่ได้รับผลกระทบ พร้อมข้อมูลความใหม่ของข้อมูล
3. เปรียบเทียบผลกระทบข้ามจังหวัดหรืออำเภอด้วยขอบเขตที่สอดคล้องกัน
4. ส่งออกข้อมูลในรูปแบบรายงานมาตรฐานพร้อมข้อจำกัด

**Data needs**
- event registry
- administrative boundaries
- impact observations
- reference cost inventories

**Governance needs**
- schema มาตรฐานสำหรับ impact reporting
- governance ของ reference cost
- metadata เกี่ยวกับ timeliness และ uncertainty

#### ข.3.2 UC-02 — ข้อมูลบริบทความเสี่ยงสำหรับการเตรียมพร้อมและการแจ้งเตือน

**Primary user:** ผู้วางแผนหรือผู้สนับสนุนการปฏิบัติการด้านภัยพิบัติ  
**Goal:** ผสานข้อมูล hazard context กับข้อมูล exposure / vulnerability เพื่อสนับสนุนการเตรียมพร้อมและการจัดวางทรัพยากร

**User journey ขั้นต่ำ**
1. เลือกประเภทภัยและช่วงเวลา
2. ดูข้อมูลเชิงพื้นที่ที่จัดวางบนขอบเขตมาตรฐาน
3. ซ้อนทับกับกลุ่มเปราะบางหรือทรัพย์สินสำคัญ
4. ส่งออก briefing pack สำหรับผู้ตัดสินใจ

#### ข.3.3 UC-03 — Provincial risk profile สำหรับผู้กำหนดนโยบายและผู้วางแผน

**Primary user:** ผู้กำหนดนโยบายหรือผู้วางแผนระดับจังหวัด  
**Goal:** ได้รับ one-pager หรือชุดข้อมูลสรุปที่อ่านง่ายเกี่ยวกับ hazard, exposure, vulnerable groups และบริบทการปรับตัว

**Data needs**
- hazard layers
- socio-economic indicators
- critical infrastructure or key assets

#### ข.3.4 UC-03b — Municipality / LAO budget justification pack

**Primary user:** ผู้วางแผนท้องถิ่นและที่ปรึกษาขององค์กรปกครองส่วนท้องถิ่น  
**Goal:** สร้าง evidence pack ที่เชื่อมความเสี่ยงในพื้นที่กับเหตุผลการขอจัดสรรงบประมาณ

**User journey ขั้นต่ำ**
1. เลือกเทศบาลหรือองค์กรปกครองส่วนท้องถิ่น
2. เรียก risk layers และ baseline ที่เกี่ยวข้อง
3. ดึง indicator snippets และ assumptions ที่อธิบายการลงทุน
4. ส่งออกเอกสารสรุปเพื่อใช้ประกอบคำของบประมาณ

#### ข.3.5 UC-04 — Vulnerable group mapping and service targeting

**Primary user:** นักวางแผนด้าน social protection  
**Goal:** ระบุพื้นที่เสี่ยงที่มีกลุ่มเปราะบางกระจุกตัวอยู่

**Constraints**
- มีข้อมูลที่อาจอ่อนไหวและต้องมี aggregation rules และ access control

#### ข.3.6 UC-05 — Heat-health surveillance roadmap

**Primary user:** หน่วยงานสาธารณสุขหรือผู้ประสานงานด้าน climate-health  
**Goal:** ระบุว่าต้องมีข้อมูลอะไรบ้างจึงจะวัด heat morbidity หรือ heat mortality ได้อย่างน่าเชื่อถือ

**Phase 1 deliverable**
- data gap register + candidate data owners + feasibility notes

#### ข.3.7 UC-06 — Cascading impacts explainer and analysis entry point

**Primary user:** ผู้ใช้ผสมทั้งเชิงนโยบายและเชิงวิเคราะห์  
**Goal:** ทำให้ผู้ใช้เข้าใจความสัมพันธ์แบบลูกโซ่ของผลกระทบ เช่น flood → transport disruption → supply chain impact

#### ข.3.8 UC-07 — Infrastructure disruption and critical corridor exposure

**Primary user:** ผู้วางแผนโครงสร้างพื้นฐานหรือผู้วิเคราะห์ความยืดหยุ่นของระบบคมนาคม  
**Goal:** ทำความเข้าใจว่าภัยส่งผลต่อ corridor หรือ critical assets อย่างไร

**Phase 1 stance**
- เริ่มจาก catalog + showcase ของ datasets และ methods ไม่อ้างว่าจะมี nationwide high-resolution modeling พร้อมใช้ทั้งหมด

#### ข.3.9 UC-08 — Statistical baselines and thematic tagging

**Primary user:** ผู้ดูแล data catalog หรือผู้ประสานข้อมูลสถิติ  
**Goal:** ให้ระบบมี baseline ที่สอดคล้องและค้นพบได้ง่ายผ่าน tagging frameworks

#### ข.3.10 UC-09 — True economic loss & damage estimation

**Primary user:** นักวิเคราะห์นโยบายของ NESDC และนักวิเคราะห์ของ DCCE  
**Goal:** ปิดช่องว่างระหว่างข้อมูลการเยียวยากับความสูญเสียทางเศรษฐกิจที่แท้จริง

**User journey ขั้นต่ำ**
1. เลือกเหตุการณ์หรือช่วงเวลา
2. ดึง baseline ทางเศรษฐกิจที่เกี่ยวข้อง
3. ประเมิน direct loss และ indirect loss ภายใต้สมมติฐานที่ชัดเจน
4. ส่งออก brief ที่แยกชัดระหว่าง relief กับ true loss พร้อม caveats

#### ข.3.11 UC-10 — Baseline verification / single source of truth

**Primary user:** policy integrator หรือผู้ดูแลมาตรฐานข้อมูลของ DCCE  
**Goal:** นิยามกลไกที่ใช้เลือก baseline ที่ “official enough” สำหรับการใช้งานร่วมกัน

#### ข.3.12 UC-11 — Financial-sector physical risk analysis and climate stress testing

**Primary user:** bank risk analyst และ regulator-facing reporting teams  
**Goal:** สนับสนุนการวิเคราะห์พอร์ตการเงินผ่าน foundational datasets และแนวทางการตีความ uncertainty อย่างสอดคล้องกัน

### ข.4 ข้อสังเกตข้าม use cases

เมื่อพิจารณา use cases ทั้งหมดร่วมกัน จะเห็นข้อสังเกตสำคัญดังนี้

1. ผู้ใช้จำนวนมากต้องการ **exportable packs** มากกว่าหน้าข้อมูลเชิงสำรวจอย่างเดียว
2. granularity เป็นประเด็นกลางที่ต่างกันตาม user group อย่างมีนัยสำคัญ
3. metadata, glossary, และ limitation statements เป็นเงื่อนไขพื้นฐานของ almost all use cases
4. uncertainty handling เป็นประเด็นสำคัญมาก โดยเฉพาะเมื่อข้อมูลถูกนำไปใช้เพื่อการตัดสินใจเชิงงบประมาณหรือเชิงการเงิน
5. sensitive data onboarding ต้องมี governance path ที่ชัดเจน

### ข.5 ความเชื่อมโยงจาก use cases ไปสู่ผลิตภัณฑ์ขั้นต่ำและโครงสร้างข้อมูล

กลุ่ม use cases ข้างต้นเป็นเหตุผลสำคัญที่ทำให้โครงการพัฒนาต่อไปสู่ workflow patterns และ MVPs ได้แก่

- curated briefing pack
- post-event reporting pack
- recommended dataset registry
- uncertainty guidance pack และ publishing standard

ในขณะเดียวกัน use cases เหล่านี้ยังเป็นฐานของการกำหนดความสำคัญของ entity และความสัมพันธ์ใน CDM เพราะช่วยชี้ให้เห็นว่าข้อมูลประเภทใดต้องถูกเชื่อมเข้าหากันตั้งแต่ระยะแรกของการพัฒนาระบบ

## ภาคผนวก ค รายละเอียด sitemap และสถาปัตยกรรมสารสนเทศของ NCAIF

### ค.1 วัตถุประสงค์ของภาคผนวกส่วนนี้

ภาคผนวกส่วนนี้จัดทำขึ้นเพื่อรวบรวมรายละเอียดของ sitemap และสถาปัตยกรรมสารสนเทศของ NCAIF ซึ่งในบทหลักถูกย่อเหลือเฉพาะเหตุผลเชิงโครงสร้างและหลักการออกแบบ ส่วนรายละเอียดระดับเมนู ระดับหน้า และองค์ประกอบที่อยู่ในระดับการจัดวางแพลตฟอร์มทั้งหมด ถูกรวมไว้ในภาคผนวกนี้เพื่อให้สามารถใช้เป็นฐานในการตรวจทานและพัฒนาระบบต่อไปได้อย่างชัดเจน

### ค.2 หลักการออกแบบ sitemap

หลักการสำคัญของ sitemap ประกอบด้วย

1. ใช้ **adaptation-cycle backbone** เป็นแกนกลางของเนื้อหา
2. มี **Policy Maker Center** เป็นทางเข้าหลักสำหรับผู้ใช้เชิงนโยบาย
3. ใช้ **hybrid access model** เพื่อให้ผู้ใช้หลายกลุ่มเข้าถึงข้อมูลจากคนละเส้นทางได้
4. แยก **narrative surface** ออกจาก **technical support layer**
5. ใช้ **top-level navigation ที่ตื้น** และหลีกเลี่ยงเมนูซ้อนลึกเกินจำเป็น
6. ใช้ **progressive disclosure** เพื่อค่อย ๆ เปิดเผยรายละเอียดตามระดับความต้องการของผู้ใช้

### ค.3 Top-level navigation

โครงสร้าง top-level navigation ที่ refined แล้ว ประกอบด้วย

1. **Home**
2. **Data Management Center for Policy Makers**
3. **Adaptation Information by Cycle**
4. **Risk and Area Profiles**
5. **Adaptation Measures Guidance & Implementation Examples**
6. **Knowledge, Tools, and Data Services**
7. **News, Updates, and About**

### ค.4 รายละเอียดระดับรองของแต่ละหมวด

#### ค.4.1 Home
- National climate adaptation overview
- Key climate risks and adaptation priorities
- Featured maps and insight cards
- Latest updates
- Quick entry by need
  - Understand risks
  - Plan adaptation action
  - Monitor adaptation progress
  - Access data services

#### ค.4.2 Data Management Center for Policy Makers
- Decision-ready summaries
  - National summary
  - Provincial profiles
  - Sector summaries
- Indicators
  - Disaster indicators and extreme events
  - Risk indicators
  - Adaptation progress indicators
  - M&E indicators
- Status of national adaptation measures
  - National adaptation plan progress
  - Priority measures by sector
  - Implementation progress snapshots
- Data services for strategic planning
  - Hazard and vulnerability overlay tool
  - Spatial risk database
  - Scenario and planning support pages
  - Data methodology and standards

#### ค.4.3 Adaptation Information by Cycle
- Climate science
  - Climate drivers and trends
  - Historical observations
  - Future climate scenarios
  - Hazard overview pages
- Risks and impacts
  - Exposure and vulnerability
  - Risk assessments by sector
  - Risk assessments by area
  - Cascading impacts and cross-sector effects
- Loss and damage
  - Event overviews
  - Post-event impact pages
  - Damage and loss summaries
  - Revision and update notes
- Adaptation planning
  - Adaptation planning guidance
  - Priority options and response pathways
  - Planning case examples
  - Budget justification packs
- Adaptation implementation
  - Ongoing projects and interventions
  - Who is doing what
  - Local and sector implementation examples
  - Implementation challenges and lessons
- Results and monitoring
  - Monitoring and evaluation framework
  - Outcome and progress dashboards
  - Adaptation stories
  - Adaptation projects
  - Reporting resources

#### ค.4.4 Risk and Area Profiles
- Provincial risk profiles
- Area-based summaries
- Sector-based risk pages
- Cross-area comparison views
- Printable briefing packs

#### ค.4.5 Adaptation Measures Guidance & Implementation Examples
- Adaptation measures guidance
  - Nature-based solutions
  - Infrastructure and engineering
  - Governance and policy measures
  - Community-based approaches
- Good practices and case studies
- National and local implementation status
- Implementation support resources

#### ค.4.6 Knowledge, Tools, and Data Services
- Interactive tools / dashboards
  - Provincial risk map
  - Scenario exploration
  - Other task-oriented tools
- Data catalog / download / APIs
  - Browse datasets by theme
  - Browse datasets by sector
  - Browse datasets by area
  - Dataset detail pages with steward, cadence, access, and usage notes
- Methods, limitations, and standards
  - Risk interpretation and caveats
  - Uncertainty guidance
  - Methodology references
- Glossary and learning resources

#### ค.4.7 News, Updates, and About
- News and events
- Recent publications
- About the platform
- Partner agencies
- Contact and feedback

### ค.5 รายละเอียดของ page types หลัก

เพื่อให้โครงสร้าง sitemap สามารถนำไปใช้จริงได้ มีการกำหนด page archetypes หลักไว้ดังนี้

1. **Landing / Hub page**
   - ใช้เพื่อจัดทางเข้าให้ผู้ใช้และอธิบายคุณค่าของหมวดนั้นอย่างรวดเร็ว
2. **Explainer / Concept page**
   - ใช้แปลแนวคิดหรือวิธีการทางเทคนิคให้อยู่ในรูปแบบที่ผู้ใช้เข้าใจได้ง่าย
3. **Area profile page**
   - ใช้แสดงสรุปข้อมูลความเสี่ยงรายจังหวัดหรือรายพื้นที่ พร้อม caveat ที่จำเป็น
4. **Sector knowledge page**
   - ใช้อธิบายความเสี่ยง ปัจจัย และทางเลือกของภาคส่วนต่าง ๆ
5. **Tool entry page**
   - ใช้เป็นหน้าทางเข้าสู่เครื่องมือ interactive หรือ dashboard โดยให้ข้อมูล task framing และข้อจำกัดก่อนใช้งาน
6. **Data catalog / download page**
   - ใช้สำหรับค้นพบ dataset ดู steward, cadence, access condition, และการดาวน์โหลดหรือขอใช้ข้อมูล
7. **Methodology / limitations page**
   - ใช้รองรับความโปร่งใสด้านวิธีการและการตีความ
8. **Case study / briefing pack page**
   - ใช้ถ่ายทอดข้อมูลในรูป narrative หรือ exportable evidence packs

### ค.6 องค์ประกอบที่คงเสถียรภาพและองค์ประกอบที่ยืดหยุ่นได้

#### ค.6.1 Stable backbone
- adaptation-cycle structure
- Policy Maker Center as a top-level anchor
- core topic families
- existence of data services, methodology, glossary, and updates sections

#### ค.6.2 Flexible elements
- specific sectors
- hazard subtopics
- named tools and dashboards
- case studies and featured stories
- agency collections
- indicator sets

### ค.7 กฎการเปลี่ยนแปลง sitemap ในระยะต่อไป

การเปลี่ยนแปลง sitemap สามารถแบ่งได้เป็นสามระดับ ได้แก่

1. **Minor content change** เช่น การเพิ่ม subpage ใหม่ การปรับ label หรือการเพิ่ม case study ใช้การอนุมัติในระดับ section owner
2. **Structural extension** เช่น การเพิ่ม subtopic ใหม่ใต้ cycle branch หรือเพิ่มหน้า sector ใหม่ ใช้การทบทวนร่วมของทีม CRDB / NCAIF
3. **Backbone change** เช่น การเปลี่ยน top-level navigation หรือเปลี่ยน adaptation-cycle structure ต้องผ่านการพิจารณาของผู้บริหาร DCCE

นอกจากนี้ การตัดสินใจเชิงโครงสร้างระดับสำคัญควรอ้างอิงหลักฐานจาก Pack A product constraints, Pack B TOR scope, Pack C usability guidance และ decision matrix ที่เกี่ยวข้อง เพื่อให้การเปลี่ยนแปลงมีหลักฐานและความต่อเนื่องทางตรรกะรองรับ

### ค.8 ความหมายของ sitemap ต่อการพัฒนาแพลตฟอร์มในระยะต่อไป

รายละเอียดของ sitemap ในภาคผนวกนี้มีความหมายมากกว่าการเป็นรายการเมนู เพราะเป็นการกำหนดว่า ผู้ใช้แต่ละกลุ่มจะเข้าถึงข้อมูลผ่านเส้นทางใด ผลิตภัณฑ์แบบใดจะถูกทำให้มองเห็นก่อน และส่วนใดของแพลตฟอร์มควรทำหน้าที่เป็นพื้นที่สื่อสารเชิงนโยบาย พื้นที่วิเคราะห์เชิงพื้นที่ หรือพื้นที่สนับสนุนด้านเครื่องมือและบริการข้อมูล การบันทึกรายละเอียดดังกล่าวไว้อย่างชัดเจนในภาคผนวกจึงช่วยให้การพัฒนาระยะต่อไปไม่หลุดจากหลักการออกแบบที่ได้จากการสังเคราะห์หลักฐานในช่วงรายงานความก้าวหน้า
