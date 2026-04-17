import pandas as pd
import os

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    silver_dir = os.path.join(base_dir, 'data', '1_silver')
    gold_dir = os.path.join(base_dir, 'data', '2_gold')
    
    relief_hazard_path = os.path.join(silver_dir, 'ddpm', 'master_financial_relief_by_hazard.csv')
    relief_sector_path = os.path.join(silver_dir, 'ddpm', 'master_financial_relief_by_sector.csv')
    dim_loc_path = os.path.join(gold_dir, 'dim_location_master.csv')
    output_path = os.path.join(gold_dir, 'fact_relief.csv')

    print("Loading data for relief harmonization...")
    # For relief, we only need Province-level codes from Gold Spine
    dim_loc = pd.read_csv(dim_loc_path, dtype=str)
    province_map = dim_loc[['province_name_th', 'province_code']].drop_duplicates()
    
    # 1. Process Hazard-based Relief
    print("Processing hazard-based relief data...")
    df_hazard = pd.read_csv(relief_hazard_path, dtype={'ปี': str})
    
    # Map Province Names to Codes
    df_hazard = df_hazard.merge(province_map, left_on='จังหวัด', right_on='province_name_th', how='left')
    
    hazards = ['อุทกภัย', 'ภัยแล้ง', 'ฝนทิ้งช่วง', 'ภัยหนาว', 'อัคคีภัย', 'วาตภัย', 'โรคศัตรูพืช', 'โรคระบาดสัตว์', 'ภัยอื่น']
    
    relief_rows = []
    for _, row in df_hazard.iterrows():
        p_code = str(row['province_code']).replace('.0', '').zfill(2) if pd.notna(row['province_code']) else None
        if not p_code: continue
        
        for h in hazards:
            val = pd.to_numeric(row[h], errors='coerce')
            if val > 0:
                relief_rows.append({
                    'year_be': row['ปี'],
                    'location_id': p_code + '000000', # Provincial level ID
                    'hazard_type_th': h,
                    'sector_th': 'ALL',
                    'amount_approved_baht': val,
                    'source': 'DDPM_FINANCIAL_HAZARD'
                })

    # 2. Process Sector-based Relief
    print("Processing sector-based relief data...")
    df_sector = pd.read_csv(relief_sector_path, dtype={'ปี': str})
    df_sector = df_sector.merge(province_map, left_on='จังหวัด', right_on='province_name_th', how='left')
    
    sectors = ['ด้านดำรงชีพ', 'ด้านสังคมสงเคราะห์', 'ด้านการแพทย์และสาธารณสุข', 'ด้านเกษตร_พืช', 'ด้านเกษตร_ประมง', 'ด้านเกษตร_ปศุสัตว์', 'ด้านเกษตร_อื่น', 'ด้านบรรเทาสาธารณภัย', 'เชิงป้องกันหรือยับยั้ง']
    
    for _, row in df_sector.iterrows():
        p_code = str(row['province_code']).replace('.0', '').zfill(2) if pd.notna(row['province_code']) else None
        if not p_code: continue
        
        for s in sectors:
            val = pd.to_numeric(row[s], errors='coerce')
            if val > 0:
                relief_rows.append({
                    'year_be': row['ปี'],
                    'location_id': p_code + '000000',
                    'hazard_type_th': 'ALL',
                    'sector_th': s,
                    'amount_approved_baht': val,
                    'source': 'DDPM_FINANCIAL_SECTOR'
                })

    # 3. Combine and Finalize
    fact_relief = pd.DataFrame(relief_rows)
    fact_relief = fact_relief.dropna(subset=['location_id'])

    # Save to Gold
    fact_relief.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"Successfully created Unified Fact Relief at: {output_path}")
    print(f"Total records: {len(fact_relief)}")

if __name__ == "__main__":
    main()
