---
type: literature
status: evergreen
tags: []
source:
authors: []
year:
relevance_to: "[[]]"
key_findings: []
sticker: emoji//1f5dd-fe0f
---
# Methodology of the CRI Pilot

**Objective:** The CRI pilot aimed to assess climate-related disaster risks at the provincial level in Thailand, adapting the Global Climate Risk Index (Germanwatch) framework.

**Core Concept:** 
- The index calculates a risk score based on the severity of extreme weather events (Flood, Storm, Drought, Landslide). 
- It balances **Human Impact** and **Economic Impact** equally (50% each), using specific weightings to prioritize relative vulnerability (impact per population/GPP) over absolute numbers.

> [!info] Role of this methodology in CRI Phase 2
> This document describes the **TEI Pilot** methodology as implemented, not the final CRI Phase 1–2 design. The pilot is a **loss‑ and impact‑focused provincial index**, useful as a historical baseline and for understanding data constraints. CRI Phase 1 refines the economic pillar into a **Fiscal Relief Index** with hybrid spatial methods, and Phase 2 adds **Resilience Capacity Profiles** (Coping–Adaptive–Transformative) on top of this baseline.

## 1) กรอบแนวคิดและการวิเคราะห์

การพัฒนา CRI สำหรับประเทศไทยในเบื้องต้นใช้กรอบแนวคิดที่เน้นการประเมินผลกระทบจากภัยพิบัติทางสภาพภูมิอากาศที่เกิดขึ้นจริง โดยมีรายละเอียดดังนี้:

- **หน่วยการวิเคราะห์ (Unit of Analysis):** กำหนดให้การวิเคราะห์อยู่ในระดับ **จังหวัด (ระดับจังหวัด)**
- **ประเภทภัยพิบัติที่ครอบคลุม:** มุ่งเน้นไปที่ภัยพิบัติที่เกิดจาก **สภาพอากาศสุดขั้ว (Extreme weather events)** โดยไม่รวมเหตุการณ์ที่เกิดขึ้นอย่างช้า ๆ (Slow Onset Event) เช่น การเพิ่มขึ้นของระดับน้ำทะเล ภัยพิบัติที่นำมาพิจารณาได้แก่ **อุทกภัย วาตภัย ภัยแล้ง และดินโคลนถล่ม** (โดยอ้างอิงคำนิยามจากกรมป้องกันและบรรเทาสาธารณภัย และกรมทรัพยากรน้ำ)
- **กรอบเวลา:** การวิเคราะห์ครอบคลุม 2 ช่วงเวลา:
    1. **ระยะสั้น:** **1 ปี** (แสดงถึงสถานการณ์ภัยพิบัติในปัจจุบัน)
    2. **ระยะยาว:** **ค่าเฉลี่ย 10 ปี** (แสดงถึงการเกิดซ้ำของภัยพิบัติ) (ในการศึกษานี้มีการใช้ข้อมูลย้อนหลัง 8 ปี คือ พ.ศ. 2559–2566 ในการวิเคราะห์ระยะยาว)

## 2) Calculation Equations

The CRI pilot utilizes **Min-Max Normalization** to scale data between 0 and 1. The province with the highest impact receives a score of 1.0 (100), and the province with the lowest impact receives 0. The final CRI Score is the sum of 6 weighted indicators ($S_1$ to $S_6$).

#### A. Human Impact (50% Weight)

_Focuses on fatalities and the affected population._

1. Total Deaths ($W_1 = 7.50\%$)
    $$S_1 = \left( \frac{\text{Deaths}_p - \text{Deaths}_{min}}{\text{Deaths}_{max} - \text{Deaths}_{min}} \right) \times 0.075$$
    
2. Deaths per 100k Inhabitants ($W_2 = 22.50\%$)
    $$S_2 = \left( \frac{\text{DeathRate}_p - \text{DeathRate}_{min}}{\text{DeathRate}_{max} - \text{DeathRate}_{min}} \right) \times 0.225$$
    
3. Total Affected People ($W_3 = 5.00\%$)
    $$S_3 = \left( \frac{\text{Affected}_p - \text{Affected}_{min}}{\text{Affected}_{max} - \text{Affected}_{min}} \right) \times 0.050$$
    
4. Affected per 100k Inhabitants ($W_4 = 15.00\%$)
    $$S_4 = \left( \frac{\text{AffectedRate}_p - \text{AffectedRate}_{min}}{\text{AffectedRate}_{max} - \text{AffectedRate}_{min}} \right) \times 0.150$$
    

#### B. Economic Impact (50% Weight)

_Focuses on financial damages to agriculture and infrastructure._

5. Total Economic Loss ($W_5 = 12.50\%$)
    $$S_5 = \left( \frac{\text{Loss}_p - \text{Loss}_{min}}{\text{Loss}_{max} - \text{Loss}_{min}} \right) \times 0.125$$
    
6. Loss per Gross Provincial Product (GPP) ($W_6 = 37.50\%$)
    $$S_6 = \left( \frac{\text{LossGPP}_p - \text{LossGPP}_{min}}{\text{LossGPP}_{max} - \text{LossGPP}_{min}} \right) \times 0.375$$

Total CRI Pilot Score:
$$CRI = S_1 + S_2 + S_3 + S_4 + S_5 + S_6$$



## 3) ชุดข้อมูลและตัวแปรที่ใช้ในการประเมิน (Datasets and Variables)


ดัชนี CRI สำหรับประเทศไทยพิจารณาจาก **8 ผลกระทบย่อย** ภายใต้ 2 องค์ประกอบหลัก คือ ผลกระทบต่อมนุษย์และผลกระทบต่อเศรษฐกิจ: 

| องค์ประกอบหลัก                           | ผลกระทบที่เสนอ (Variables)                              | แหล่งข้อมูลสำคัญ                                           |
| :--------------------------------------- | :------------------------------------------------------ | :--------------------------------------------------------- |
| **ผลกระทบต่อมนุษย์** (Human Impact)      | 1. จำนวนผู้เสียชีวิต (คน)                               | กรมป้องกันและบรรเทาสาธารณภัย                               |
|                                          | 2. จำนวนผู้เสียชีวิตต่อแสนประชากร (คนต่อแสนประชากร)     | กรมการปกครอง                                               |
|                                          | 3. จำนวนผู้ได้รับผลกระทบ (คน)                           | กรมป้องกันและบรรเทาสาธารณภัย                               |
|                                          | 4. จำนวนผู้ได้รับผลกระทบต่อแสนประชากร (คนต่อแสนประชากร) | กรมการปกครอง                                               |
| **ผลกระทบต่อเศรษฐกิจ** (Economic Impact) | 5. มูลค่าความเสียหายนอกภาคเกษตร (บาท)                   | กรมป้องกันและบรรเทาสาธารณภัย (แนวคิดเดิม/ข้อมูลไม่ใช้จริง) |
|                                          | 6. มูลค่าความเสียหายนอกภาคเกษตรต่อ GPP นอกภาคการเกษตร   | สศช. (แนวคิดเดิม/ข้อมูลไม่ใช้จริง)                         |
|                                          | 7. มูลค่าความเสียหายทางการเกษตร (บาท)                   | สำนักงานเศรษฐกิจการเกษตร (สศก./OAE)                        |
|                                          | 8. มูลค่าความเสียหายทางการเกษตรต่อ GPP                  | สศช. (GPP รวมทั้งจังหวัด; ยังไม่แยกภาค)                    |


**ข้อปรับปรุงสำหรับบริบทของประเทศไทย:** เนื่องจากประเทศไทยเป็นประเทศเกษตรกรรม และภาคส่วนนี้มีความสำคัญต่อความมั่นคงทางอาหาร การพัฒนาดัชนีจึงได้ **พิจารณามูลค่าความเสียหายภาคการเกษตรเพิ่มเติม** โดยแยกออกจากมูลค่าความเสียหายนอกภาคการเกษตรอย่างชัดเจน

- ในการวิเคราะห์ **ปี พ.ศ. 2566** ทีมวิจัยได้ใช้ **ข้อมูลการเยียวยาผู้ประสบภัยพิบัติ** (disaster recovery payment) จากสำนักงานเศรษฐกิจการเกษตร มาใช้แทนมูลค่าความเสียหายภาคการเกษตร เนื่องจากสามารถเข้าถึงข้อมูลการเยียวยาได้ครบถ้วนสำหรับภัยพิบัติทั้ง 4 ประเภท (โดยข้อมูลการเยียวยานี้สอดคล้องกับการขอรับความช่วยเหลือตามระเบียบของกระทรวงเกษตรและสหกรณ์) แต่ยังมีข้อจำกัดที่สำคัญ:
  - วงเงินเยียวยาถูกจำกัดตาม **เพดานพื้นที่ (เช่น ไม่เกิน 25 ไร่ต่อราย)** ทำให้สะท้อนมูลค่าความเสียหายน้อยกว่าความจริงในเหตุการณ์รุนแรง
  - ข้อมูลครอบคลุมเฉพาะ **ภาคเกษตร** จึงแทบไม่สะท้อนความเสียหายของภาคบริการ/อุตสาหกรรมและเมืองใหญ่

>[!warning]
>Disaster relief payment is not close to the actual damage and it is released per cabinet's circumstantial decision. The Thai government allocates the disaster recovery payment budget primarily through the national Central Fund for Emergencies or Immediate Needs, which typically receives about 2%–3.5% of the total annual budget. The amount is also decided based on BoB and Ministry of Finance judgement.  

>[!attention]
>**Clarification (TEI–Creagy meeting 4 Feb 2026):** ชุดข้อมูล Pilot ที่ใช้งานจริง **ไม่มีข้อมูลมูลค่าความเสียหายเป็นตัวเงินจาก ปภ.** (มีเฉพาะผู้เสียชีวิตและผู้ได้รับผลกระทบ). ส่วนตัวเลขเชิงเศรษฐกิจใช้ **เงินเยียวยาเกษตรกรจาก สศก.** เป็น Proxy หลัก และใช้ **GPP รวมทั้งจังหวัด** เป็นตัวหาร (ยังไม่แยกภาค). ค่าศูนย์ (0) ในหลายจังหวัดจึงสะท้อน **ไม่มีรายงานเข้า** มากกว่าการไม่มีความเสียหายจริง โดยเฉพาะในกรุงเทพฯ และจังหวัดที่มีสัดส่วนภาคเกษตรต่ำ.


## 4) วิธีการคำนวณและการถ่วงน้ำหนัก (Calculation and Weighting)

### 1 การปรับค่ามาตรฐาน (Data Normalization)

เพื่อให้สามารถนำข้อมูลของแต่ละจังหวัดมาเปรียบเทียบกันได้ (เนื่องจากมีหน่วยที่แตกต่างกัน) ข้อมูลดิบของตัวแปรทั้ง 8 ตัวจะถูกนำมาปรับค่าเป็น **คะแนนมาตรฐาน (Normalize)**:

- **ค่าสูงสุด:** จังหวัดที่มีผลกระทบสูงสุดในแต่ละองค์ประกอบจะถูกกำหนดให้มีคะแนนเท่ากับ **1**
- **ค่าต่ำสุด:** จังหวัดที่มีผลกระทบน้อยที่สุด (หรือไม่มีข้อมูลภัยพิบัติเกิดขึ้น) จะถูกกำหนดให้มีคะแนนเท่ากับ **0**
- **คะแนนอื่น:** คะแนนของจังหวัดอื่น ๆ จะถูกเปรียบเทียบตามสัดส่วนให้อยู่ในช่วง **0 ถึง 1**

>[!info] Relative "impact"
>CRI scores are still relative to the "best" performer. There was a dialogue about setting absolute threshold for some indicators so that an lerting system can be implemented to inform highly impacted provinces
### 2 การให้ค่าน้ำหนัก (Weighting)

การให้ค่าน้ำหนักสอดคล้องกับแนวทางของ Germanwatch CRI โดยมีหลักการสำคัญคือ **ให้ความสำคัญกับผลกระทบต่อมนุษย์และผลกระทบต่อเศรษฐกิจเท่าเทียมกัน** และเน้นให้ความสำคัญกับ **ค่าสัมพัทธ์ (Relative values)** มากกว่าค่าจริง (Absolute values) เนื่องจากค่าสัมพัทธ์สะท้อนความรุนแรงของปัญหาในแต่ละจังหวัดได้ดีกว่า:

- **ผลกระทบต่อมนุษย์ (50%):** ให้ความสำคัญกับค่าสัมพัทธ์ (ผู้เสียชีวิตและผู้ได้รับผลกระทบต่อแสนประชากร) มากกว่าค่าจริง (จำนวนผู้เสียชีวิตและผู้ได้รับผลกระทบ)
- **ผลกระทบต่อเศรษฐกิจ (50%):** ให้ความสำคัญกับค่าสัมพัทธ์ (มูลค่าความเสียหายต่อ GPP) มากกว่าค่าจริง (มูลค่าความเสียหาย)

**ตารางค่าน้ำหนักองค์ประกอบในการคำนวณค่าดัชนี CRI**:

| องค์ประกอบ                       | ตัวแปร                                                          | ค่าน้ำหนัก (%) |
| :------------------------------- | :-------------------------------------------------------------- | :------------- |
| **ผลกระทบต่อมนุษย์** (รวม 50%)   | จำนวนผู้เสียชีวิต (คน)                                          | 7.50%          |
|                                  | จำนวนผู้เสียชีวิตต่อแสนประชากร (คนต่อแสนประชากร) (Relative)     | **22.50%**     |
|                                  | จำนวนผู้ได้รับผลกระทบ (คน)                                      | 5.00%          |
|                                  | จำนวนผู้ได้รับผลกระทบต่อแสนประชากร (คนต่อแสนประชากร) (Relative) | **15.00%**     |
| **ผลกระทบต่อเศรษฐกิจ** (รวม 50%) | มูลค่าความเสียหาย (บาท)                                         | 12.50%         |
|                                  | มูลค่าความเสียหายต่อผลิตภัณฑ์มวลรวมจังหวัด (GPP) (Relative)     | **37.50%**     |

**สูตรการคำนวณคะแนน CRI รวม** คะแนน CRI รวมคำนวณจากผลรวมของแต่ละองค์ประกอบคูณด้วยค่าน้ำหนักของแต่ละองค์ประกอบ: **คะแนน CRI รวม =**

- **0.125** [0.6 (คะแนนผู้เสียชีวิต) + 0.4 (คะแนนผู้ได้รับผลกระทบ)] (Absolute Human Impact)
- **+ 0.375** [0.6 (คะแนนผู้เสียชีวิตต่อประชากรแสนคน) + 0.4 (คะแนนผู้ได้รับผลกระทบต่อประชากรแสนคน)] (Relative Human Impact)
- **+ 0.125** (คะแนนมูลค่าความเสียหาย) (Absolute Economic Impact)
- **+ 0.375** (คะแนนมูลค่าความเสียหายต่อ GPP จังหวัด) (Relative Economic Impact)

# Challenges and Limitations of the CRI Pilot

The pilot phase exposed critical "pain points" regarding data readiness and scope:

1. **Critical Data Gaps (Economic Loss):** The most significant limitation was the lack of complete economic loss data. For the 2023 pilot year, **only 5 provinces** had sufficient **online and open data** to calculate the full index. The rest needs to ask for line agencies

>[!Quote] From 8 May 2025 Meeting
>จากการสืบค้นข้อมูลผ่านเว็บไซต์ของหน่วยงานภาครัฐ พบว่ามีการเผยแพร่ข้อมูลย้อนหลัง 10 ปี โดยเฉพาะข้อมูลในระดับจังหวัด โดยพบว่า มี**ข้อมูลที่สามารถดาวน์โหลดได้ทันทีประมาณ 22 จังหวัด** ซึ่งสะท้อนว่าแต่ละจังหวัดน่าจะมีข้อมูลอยู่ในระบบ


>[!quote] From 30 June 2025 meeting 
> ดัชนีชี้วัดที่ทางทีมวิจัยรวบรวมข้อมูลได้ในปี 2566 พบว่าจังหวัดที่มีข้อมูลครบถ้วน 5 จังหวัด ได้แก่ จังหวัดนราธิวาส จังหวัดชุมพร จังหวัดตาก จังหวัดกระบี่ และจังหวัดชัยนาท ซึ่งได้ข้อมูลจากข้อมูลเปิด (Open Data) ส่วนข้อมูลของจังหวัดอื่น ๆ **ปัจจุบันกำลังดำเนินการขอข้อมูลจากหน่วยงานที่เกี่ยวข้อง** (as of June 2025) นอกจากนี้ได้ข้อมูลตัวอย่างจากปี 2562 เนื่องจากทางทีมวิจัยพยายามหาข้อมูลที่สมบูรณ์มากที่สุด พบว่าข้อมูลที่หายากคือข้อมูลมูลค่าความเสียหายของภัยพิบัติ จึงย้อนหลังไปดูข้อมูลในปี 2562 ซึ่งหาข้อมูลได้ 9 จังหวัด ได้แก่ จังหวัดอำนาจเจริญ จังหวัดหนองบัวลำภู จังหวัดหนองคาย จังหวัดสกลนคร จังหวัดชุมพร จังหวัดลำปาง จังหวัดน่าน จังหวัดพะเยา และจังหวัดสุราษฎร์ธานี ซึ่งหากมีข้อมูลสัดส่วนของคะแน
  
    
2. **Ambiguity in "Zero" vs. "Missing":** The datasets often failed to distinguish between "zero impact" (no event occurred) and "missing data" (event occurred but unrecorded). In Min-Max normalization, this can severely skew results if missing data is treated as 0 (the minimum). The CRI pilot did not differentiate between **"missing data"** (an event occurred but was not recorded) and **"true zero"** (no event occurred). Consequently, missing data points were effectively **treated as 0** in the calculation.

>[!quote]
>จัดทําข้อมูลให้เป็นคะแนนมาตรฐาน (Data normalization) โดยให้คะแนนที่สูงที่สุดแต่ละ องค์ประกอบเป็นหนึ่ง และค่าต่ําสุดของทุกองค์ประกอบเท่ากับศูนย์ จากนั้นจึงเปรียบเทียบ คะแนนตามสัดส่วนให้ได้คะแนนแต่ละองค์ประกอบเป็นศูนย์ถึงหนึ่ง สําหรับองค์ประกอบบาง จังหวัดที่ไม่พบข้อมูลให้ระบุเป็นศูนย์


> [!note] 
> **Post‑hoc clarification (4 Feb 2026):** TEI confirmed that for several years and provinces, a value of `0` was used when no report was available from the provincial level, not as a validated estimate of no damage. This reinforces the need for the **Administrative Gap Flag** introduced in CRI Phase 1 and adopted in Phase 2.



3. **Coarse Resolution:** The analysis was limited to the **provincial level**. This is too broad to identify specific high-risk districts or communities, limiting its utility for local resource allocation.
    
4. **Retrospective Only:** The pilot is strictly a "Loss Index." It measures past damage but provides no insight into future coping capacities or preparedness.


5. **Scale and Precision:** Although experts proposed extending the assessment to the sub-district or sub-area level (อำเภอ/ตำบล) for more accurate resource allocation, the current framework is limited to the **provincial level** (ระดับจังหวัด) due to data availability and project constraints.

6. **Risk Modeling:** If the analysis uses data from only one year (short-term), it may be misleading, as a region might not experience an extreme event in that specific year. Therefore, relying only on past data (end-point data) might not fully reflect the **preparedness or adaptive capacity** of an area.





# Excel sheet audit

Data from TEI
[CRI1-TEI_Data_59_66 cal.xlsx](https://thecreagycom.sharepoint.com/:x:/s/DCCECRI2/IQBmI_yahsxBQ5m8uAiRRJ-CAS7jDzkpqunCw3cPJO_nBZs?e=nCYmGf)

| Table name | data owner                              | Processed? | comment                                                                                                                                                                                                                                                                     |
| ---------- | --------------------------------------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| pop59-66   | Department of Provincial Administration | yes        | 2 columns; Province name and "59-66" which is assumed to be average populations between 2013 and 2021 because the values are in floating numbers, not integers.<br>                                                                                                         |
| GPP59-66   | NEDSC                                   | yes        | 2 columns; Province name and "GPPเกษตร59-66" which is assumed to be average GPP of the agricultural sector between 2013 and 2021                                                                                                                                            |
| ตายเจ็บ    | DDPM                                    |            | 4 hazards; landslide, flood, drought, TC<br>\|เจ็บถล่ม59_66\|ตายถล่ม59_66\|เจ็บอุทก59_66\|ตายอุทก59_66\|เจ็บแล้ง59_66\|ตายแล้ง59_66\|เจ็บพายุ59_66\|ตายพายุ59_66\|                                                                                                          |
| เยียวยา    | Office of Agricultural Economics        | yes        | 4 hazards; landslide, flood, drought, TC<br>\|ดินถล่มAva62_66\|แล้ง59_66\|วาตภัย59_66\|อุทก59_66\|\|เยียวยารวม59_66\|                                                                                                                                                       |
| Cal        |                                         | yes        | Score calculation sheet.<br>Data lineage cannot be traced.<br>A lot of variables are hard coded<br>Data processing columns are<br>\|`sum`X\|`Score`X\|`Rel`X\|<br>where X is ตาย ✅ เจ็บ ✅<br>เยียวยา / loss ไม่มี column `sum`<br>✏️ ==loss = เงินเยียวยา/ GPP (ภาคเกษตร)== |

