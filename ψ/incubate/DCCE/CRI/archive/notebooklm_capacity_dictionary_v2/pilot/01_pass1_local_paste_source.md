# Pilot Pass 1 local paste source

This file captures the small pasted subset used for the local-only Pass 1 pilot transformation.

It intentionally mixes a few rows from the existing dictionary and a few rows from Tik's CBI note so the pilot can test source-near raw-row conversion without harmonisation.

## 1. Source provenance

- Existing dictionary subset from [`CRI_Capacity_Tagging_Dictionary.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary.md)
- CBI subset from [`2026-04-07-CBI_Indicator_Metadata-Ai-generated-P-Tik.md`](ψ/incubate/DCCE/CRI/inbox_source/2026-04-07-CBI_Indicator_Metadata-Ai-generated-P-Tik.md)

## 2. Local-only instruction block used for Pass 1

```text
Work only on the text pasted by the human.

Convert the pasted material into the same flat raw-row schema used by the NotebookLM extraction passes.

Preserve the source wording as much as possible.
Do not invent new concepts.
Do not harmonise labels.
Do not remove duplicates.
If a field is not explicit in the pasted text, write "not explicit".
```

## 3. Pasted subset

### 3.1 Existing dictionary subset

From [`CRI_Capacity_Tagging_Dictionary.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary.md):

| Indicator concept | Baseline proxy | Capacity category | Governance function |
| --- | --- | --- | --- |
| Plan revision cycle | Plan exists + last revised year (or last published version) | Adaptive | Planning |
| Cross-department coordination meetings | Formal coordination body exists (committee/taskforce) + publicized meeting minutes (if available) | Adaptive | Coordination |
| Climate budget tagging coverage | Climate budget tagging policy exists; # items tagged (if counts exist) | Adaptive | Finance / accountability |
| Community engagement frequency | Participation mechanism exists; engagement activities documented in annual report | Transformative | Inclusion / legitimacy |

### 3.2 Tik CBI subset

From [`2026-04-07-CBI_Indicator_Metadata-Ai-generated-P-Tik.md`](ψ/incubate/DCCE/CRI/inbox_source/2026-04-07-CBI_Indicator_Metadata-Ai-generated-P-Tik.md):

> CBI ใช้กรอบแนวคิดที่ประกอบด้วย 3 เสาหลัก (Pillars) และ 2 มิติ (Dimensions) ดังนี้:
>
> **เสาหลักที่ 1: Coping Capacity** --- ขีดความสามารถในการรับมือเฉพาะหน้า
>
> **เสาหลักที่ 2: Adaptive Capacity** --- ขีดความสามารถในการปรับตัว
>
> **เสาหลักที่ 3: Transformative Capacity** --- ขีดความสามารถในการเปลี่ยนผ่าน
>
> แต่ละเสาหลักแบ่งเป็น 2 มิติ ได้แก่ มิติด้านสินทรัพย์ (Asset) ซึ่งวัดทรัพยากรที่มีอยู่ และมิติด้านกระบวนการ (Process) ซึ่งวัดกลไกและการดำเนินงาน

Selected indicator rows:

| รหัส | ตัวชี้วัด | เสาหลัก | มิติ |
| --- | --- | --- | --- |
| CA4 | จำนวนบุคลากรด้านการแพทย์ฉุกเฉิน | Coping | Asset |
| AP2 | บูรณาการข้อมูลสภาพภูมิอากาศเข้าสู่แผนพัฒนา | Adaptive | Process |
| AP3 | การมีส่วนร่วมของชุมชนในการจัดทำแผนรับมือภัย | Adaptive | Process |
| TP3 | นวัตกรรม/เทคโนโลยีด้านภูมิอากาศ | Transformative | Process |

## 4. Resulting local raw output

The transformed Pass 1 pilot output is stored in [`responses/2026-04-08_pilot_pass1_local_raw_rows.json`](ψ/incubate/DCCE/CRI/archive/notebooklm_capacity_dictionary_v2/responses/2026-04-08_pilot_pass1_local_raw_rows.json).
