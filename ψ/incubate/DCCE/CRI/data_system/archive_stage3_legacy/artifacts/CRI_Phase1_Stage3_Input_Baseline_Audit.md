# Stage 3 Input Baseline Audit Snapshot

Generated (UTC): 2026-04-20T16:41:51.314091+00:00

## CSV Inputs
- `data/2_gold/dim_location_master.csv`: exists=True, rows=69704
  - columns: location_id, province_code, province_name_th, district_code, district_name_th, subdistrict_code, subdistrict_name_th, village_code, village_name_th, admin_level, source
- `data/2_gold/dim_location.csv`: exists=True, rows=86
  - columns: location_id, province_name_th, district_name_th, subdistrict_name_th, village_name_th, admin_level_note, location_nk, source, source_filename
- `data/1_silver/ddpm/master_village_disaster_stat_2557_2567.csv`: exists=True, rows=209935
  - columns: Incident Name, ปี, Disaster Type, Disaster Date, Province Code, Province, District Code, District, Subdistrict Code, Subdistrict, Moo, Municipal Code, Municipality, Community, Village Code, Zone Center Name, Title, Cause, Status, Situation, Relief Declared Date, Disaster Area Date, Other Announce Date, End Disaster Date, Affected People, Affected Households, Evacuated People, Evacuated Households, Deaths, Missing, Injured, Housing Damage, Business Damage, Agriculture Damage, Livestock Damage, Fishing Damage, Transport Damage, Health Damage, Culture Damage, Education/Sports, Utilities Damage, Govt Property Damage, Other Public Benefits_1, Other Public Benefits_2
- `data/1_silver/ddpm/master_financial_relief_by_sector.csv`: exists=True, rows=1872
  - columns: จังหวัด, ปี, ด้านดำรงชีพ, ด้านสังคมสงเคราะห์, ด้านการแพทย์และสาธารณสุข, ด้านเกษตร_พืช, ด้านเกษตร_ประมง, ด้านเกษตร_ปศุสัตว์, ด้านเกษตร_อื่น, ด้านบรรเทาสาธารณภัย, ด้านการปฏิบัติงานบรรเทาทุกข์, เชิงป้องกันหรือยับยั้ง, รวมทั้งสิ้น, วงเงินเสนอ, วงเงินอนุมัติ, วงเงินไม่อนุมัติ
- `data/1_silver/bma/bkk_hazard_impact_yearly.csv`: exists=True, rows=9
  - columns: impact_id, import_batch_id, report_year_be, report_year_ce, location_id, hazard_type_id, deaths_count, affected_people_count, relief_amount_baht, source_sheet_name, source_row_no, has_observation

## DOPA Boundary Assets
- `THA_Province`: shp=True, dbf=True, shx=True, cpg=True
  - dbf_fields: P_NAME_T, P_NAME_E, Area_km2
  - prj: PROJCS["WGS_1984_UTM_Zone_47N",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.01...
- `THA_Amphoe`: shp=True, dbf=True, shx=True, cpg=True
  - dbf_fields: P_NAME_T, P_NAME_E, A_NAME_T, A_NAME_E, Area_km2
  - prj: PROJCS["WGS_1984_UTM_Zone_47N",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.01...
- `THA_Tambon`: shp=True, dbf=True, shx=True, cpg=True
  - dbf_fields: P_NAME_T, P_NAME_E, A_NAME_T, A_NAME_E, T_NAME_T, T_NAME_E, Area_km2
  - prj: PROJCS["WGS_1984_UTM_Zone_47N",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453...

## WorldPop Asset
- expected `.tif` exists=True; alternate `.tiff` exists=False
- raster details: driver=None, width=None, height=None, count=None, crs=None, dtype=None, nodata=None, bounds=None, rasterio_error=ModuleNotFoundError: No module named 'rasterio'
