# Task: National Administrative Boundary Cleanup (Silver Layer)
**Date**: 2026-05-18
**Project**: DCCE Climate Risk DataBase (CRDB)
**Status**: [DONE] 100% Referential Integrity Achieved (Sealed)

## Context
Following the successful prototype for Chiang Rai, we scaled the administrative boundary normalization nationwide to support the National Climate Resilience Index (CRI).

## Session 1: initial Scale-up (2026-05-18, Morning)
**Progress: 8,105/8,105 polygons matched (100.00%).**
*Note: This was achieved via surgical patching of known quirks (Korat "Mueang", Thepharak spelling).*

**Key Discoveries**:
1. **Nakhon Ratchasima Exception**: Confirmed that Korat is the unique case in the spine where the provincial capital is named simply **"เมือง"** (Mueang).
2. **Thepharak Spelling Error**: Identified that the master spine contains a spelling error for Thepharak district (**"เทพารัษ์"** using 'ษ').
3. **Bangkok 2017 Reset**: Mapped legacy subdivision polygons (e.g., Bang Na, Bang Bon) to the primary "Nuea" codes.

## Session 2: Gold Master Promotion & Hardening (2026-05-18, Afternoon)
**Status**: [PARTIAL] 99.8% Coverage (8,086/8,105 polygons)

**Refactoring Logic**:
- **DOPA Master Promoted to GOLD**: The `dim_location_master.csv` moved to `data/2_gold/dopa/`.
- **Shift to Canonical Alignment**: Attempted to remove manual patches in favor of strict CCAATT alignment.
- **Forensic Gap**: Discovered 19 join failures in Korat due to GIS-level attribute glitches in the Bronze layer.

## Session 3: Hierarchical Schema Validation (2026-05-18, Afternoon)
**Status**: [DONE] 99.86% Referential Integrity (8,094/8,105 polygons)

**Hardening Actions**:
1. **Strict Code Validation**: Village records discarded if parent codes did not exist in CCAATT. **176 invalid records** purged.
2. **Total Nomenclature Inheritance**: All names (P/D/S) strictly inherited from CCAATT, restoring "เมืองนครราชสีมา".
3. **Residual Gaps**: Identified final 11 failures as GIS-level nomenclature renames (e.g., *สองห้อง* renamed to *โพนสว่าง*).

## Session 4: Final Forensic Resolution & Sealing (2026-05-18, Evening)
**Status: [DONE] 100% Referential Integrity Achieved.**

To achieve absolute integrity, 11 targeted forensic patches were applied to bridge the gap between legacy GIS attributes and the modern Gold Spine:

| Province | GIS Subdistrict | Resolution | Reason |
| :--- | :--- | :--- | :--- |
| **อุตรดิตถ์** | ท่าแฝก | **น้ำปาด**, ท่าแฝก (530407) | Moved district in 2015. |
| **หนองคาย** | สองห้อง | **โพนสว่าง** (430111) | Renamed in 2010. |
| **บึงกาฬ** | หนองเข็ง | **โนนสว่าง** (380103) | Renamed in 2011. |
| **เชียงใหม่** | สบโขง | **แม่หลอง** (501805) | Renamed in 2022. |
| **เชียงใหม่** | ทุ่งปี้ | **ทุ่งปี๊** (502202) | Tone mark correction. |
| **มหาสารคาม** | ขามเรียน | **สร้างแซ่ง** (441106) | Area renamed. |
| **ชัยภูมิ** | ซับสีทอง | **เมืองชัยภูมิ**, ซับสีทอง (360119) | District shift. |
| **อุบลราชธานี** | ห้วยขะยูง | **ห้วยขะยุง** (341524) | Spelling correction. |
| **อุบลราชธานี** | นิคมลำโดมน้อย | **นิคมสร้างตนเองลำโดมน้อย** (342905) | Nomenclature expansion. |
| **นครสวรรค์** | วัดไทร | **วัดไทรย์** (600113) | Canonical spelling. |
| **แพร่** | วังหงษ์ | **วังหงส์** (540113) | Canonical spelling. |

---

## Final Summary & Seal
The **National Administrative Boundary Cleanup** is complete. 
1. **Gold Spine**: `dim_location_master.csv` is hardened with 100% referential integrity to the CCAATT master, using `code_village_dopa_2019.xls` as the base village source.
2. **Silver Boundaries**: 100% of national GIS polygons are now geocoded and enriched with DOPA codes.
3. **Lineage**: Full transformation logic and forensic patches are documented in `data-lineage.md`.

**The spatial foundation is locked.** No further modifications to the administrative spine or boundary joins are required.

**[SEALED: 2026-05-18]**
