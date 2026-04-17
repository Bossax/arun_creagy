
# Data Medallion: Bronze Layer (Raw Data)
Location: `ψ/incubate/DCCE/CRI/data_system/data/0_bronze/`

This layer contains immutable, raw source files used as the foundation for the CRI Phase 1 Impact Index.

##  1 BMA (Bangkok Metropolitan Administration)
- **Source:** BMA direct file transfer
- **File**: `สถิติข้อมูลอุทกภัย ภัยแล้ง ดินถล่ม และวาตภัย ในพื้นที่กรุงเทพมหานคร_BMA.xlsx`
- **Description**: Multi-hazard disaster statistics for Bangkok districts.
- **Role**: Primary source for capital-specific impact metrics.

## 2 DDPM (Dept of Disaster Prevention & Mitigation)
- **Source:** DDPM direct file transfer
- **Village Statistics (2557 - 2567)**:
  - Individual yearly CSVs: `2557 - สถิติการเกิดสาธารณภัยรายหมู่บ้าน.csv` to `2567 - สถิติการเกิดสาธารณภัยรายหมู่บ้าน.csv`.
  - **Contents**: Granular village-level (`Moo`) impact data (house damage, livestock, human impact).
- **Financial Relief**:
  - **File**: `สถิติข้อมูลการใช้จ่ายเงินทดรองราชการ ปี 2546 - ปัจจุบัน.xlsx`
  - **Description**: Provincial-level emergency fund spending records.

## 3 DOPA (Dept of Provincial Administration)  
- `commu.xlsx` (Communities)
- `rcode.xlsx` (Regional codes)
- `soi.xlsx` (Alleys/Small streets)
- `thanon.xlsx` (Main Roads)
- `trok.xlsx` (Lanes)
- **`ccaatt.xlsx`**: Master administrative code sequential file (Province-District-Subdistrict).
	- **Source:**  https://stat.bora.dopa.go.th/stat/statnew/statMenu/newStat/ccaa.php
		**โครงสร้างข้อมูลทำเนียบท้องที่**
		FILE NAME: `ccaatt.xlsx`
		FILE TYPE: SEQUENTIAL (fixed length)
		
		หมายเหตุ:
		1. ข้อมูลขณะนี้เป็นข้อมูลในระดับจังหวัด อำเภอ ตำบล  
		2. รายการรหัสข้อมูลใดที่มีเครื่องหมาย * หมายถึง รหัสนี้ถูกยกเลิก

|FIELD NAME|CHARS|STORE|TYPE|KEY|DESCRIPTION|
|---|---|---|---|---|---|
|TBCCAA-KEY|   |   |   |PK||
|-TBC-CC|2|2|N||CHANGWAT (จังหวัด)|
|-TBC-AA|2|2|N||AMPUR (อำเภอ)|
|-TBC-TT|2|2|N||TAMBOON (ตำบล)|
|-TBC-MM|2|2|N||MOO BARN (หมู่บ้าน)|
|TBC-DESC|40|40|AN||DESCRIPTION (คำอธิบาย)|

- **`code_village_dopa_2019.xls`**: High-resolution village code master (2019 vintage).
	- สถาบันพัฒนาองค์กรค์ชุมชน (CODI)
		**Source:** https://ref.codi.or.th/2015-08-17-16-14-30/2015-08-19-16-00-10
		FILE NAME: [code_villagedopa53.xls](https://ref.codi.or.th/2015-08-17-16-14-30/2015-08-19-16-00-10?download=12:2011-07-25-04-23-09)
		รหัสพื้นที่ หมู่บ้าน อ้างอิง จากกรมการปกครองกระทรวงมหาดไทย ปี 2553
		File Size: 3.64 MB
		Date: 25 กรกฎาคม 2554

## 3.4 TEI Pilot (Baseline Data)
- **Source:** TEI direct file transfer
- **Files**:
  - `casualties_by_hazard_2559_2566.csv`
  - `relief_by_hazard_2559_2566.csv`
  - `population_avg_2559_2566.csv`
  - `gpp_agri_avg_2559_2566.csv`
- **Role**: Pre-processed average statistics from the 2023 Pilot Phase used for benchmarking and calibration.
