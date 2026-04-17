import pandas as pd
import os
import re

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bronze_dir = os.path.join(base_dir, 'data', '0_bronze', 'dopa')
    gold_dir = os.path.join(base_dir, 'data', '2_gold')
    
    ccaatt_path = os.path.join(bronze_dir, 'ccaatt.xlsx')
    village_path = os.path.join(bronze_dir, 'code_village_dopa_2019.xls')
    output_path = os.path.join(gold_dir, 'dim_location_master.csv')

    # 1. Parse CCAATT (Hierarchy)
    print(f"Loading {ccaatt_path}...")
    df_cc = pd.read_excel(ccaatt_path, engine='openpyxl', skiprows=4, header=None)
    df_cc.columns = ['code', 'name_th', 'name_en', 'status']
    
    # Filter active only
    df_cc = df_cc[df_cc['status'] == 0].copy()
    df_cc['code'] = df_cc['code'].astype(str).str.zfill(8)
    
    hierarchy = {}
    
    print("Building administrative hierarchy from CCAATT...")
    # Province: CC000000
    for _, row in df_cc[df_cc['code'].str.endswith('000000')].iterrows():
        p_code = row['code'][:2]
        hierarchy[p_code] = {'name': row['name_th'], 'districts': {}}
        
    # District: CCAA0000 (AA != 00)
    for _, row in df_cc[df_cc['code'].str.endswith('0000') & ~df_cc['code'].str.endswith('000000')].iterrows():
        p_code = row['code'][:2]
        a_code = row['code'][:4]
        if p_code in hierarchy:
            hierarchy[p_code]['districts'][a_code] = {'name': row['name_th'], 'subdistricts': {}}
            
    # Subdistrict: CCAATT00 (TT != 00)
    for _, row in df_cc[df_cc['code'].str.endswith('00') & ~df_cc['code'].str.endswith('0000')].iterrows():
        p_code = row['code'][:2]
        a_code = row['code'][:4]
        t_code = row['code'][:6]
        if p_code in hierarchy and a_code in hierarchy[p_code]['districts']:
            hierarchy[p_code]['districts'][a_code]['subdistricts'][t_code] = row['name_th']

    # 2. Parse Village (Supplement)
    print(f"Loading {village_path}...")
    df_v = pd.read_excel(village_path, engine='openpyxl', dtype=str)
    
    canonical_rows = []
    
    # helper to clean string codes
    def clean_val(val, length):
        if pd.isna(val): return '0' * length
        s = str(val).replace('.0', '').strip()
        return s.zfill(length)

    # Process villages
    print("Processing village records...")
    for _, row in df_v.iterrows():
        v_code = clean_val(row['VILL_CODE'], 8)
        p_code = clean_val(row['PROV_CODE'], 2)
        a_code = clean_val(row['AMP_CODE'], 4)
        t_code = clean_val(row['TAM_CODE'], 6)
        
        p_name = str(row['PROV_T']).replace('จ.', '').strip()
        a_name = str(row['AMP_T']).replace('อ.', '').replace('เขต', '').strip()
        t_name = str(row['TAM_T']).replace('ต.', '').replace('แขวง', '').strip()
        v_name = str(row['VILL_T']).strip() if pd.notna(row['VILL_T']) else ''
        
        canonical_rows.append({
            'location_id': v_code,
            'province_code': p_code,
            'province_name_th': p_name,
            'district_code': a_code,
            'district_name_th': a_name,
            'subdistrict_code': t_code,
            'subdistrict_name_th': t_name,
            'village_code': v_code,
            'village_name_th': v_name,
            'admin_level': 'village',
            'source': 'DOPA_2019'
        })
        
    # Process BKK and other areas from CCAATT that might not be in Village file
    # We add Subdistrict-level records as well for mapping data that isn't village-specific
    print("Adding subdistrict and district records from CCAATT...")
    for p_code, p_data in hierarchy.items():
        p_name = p_data['name'].replace('จังหวัด', '').strip()
        for a_code, a_data in p_data['districts'].items():
            a_name = a_data['name'].replace('อำเภอ', '').replace('เขต', '').strip()
            for t_code, t_name in a_data['subdistricts'].items():
                t_name_clean = t_name.replace('ตำบล', '').replace('แขวง', '').strip()
                
                # Check if we already have this subdistrict covered (basic check)
                # For simplicity, we add all subdistricts from CCAATT with village_code as empty or 00
                canonical_rows.append({
                    'location_id': t_code + '00', # 8-digit padded
                    'province_code': p_code,
                    'province_name_th': p_name,
                    'district_code': a_code,
                    'district_name_th': a_name,
                    'subdistrict_code': t_code,
                    'subdistrict_name_th': t_name_clean,
                    'village_code': '',
                    'village_name_th': '',
                    'admin_level': 'subdistrict',
                    'source': 'CCAATT'
                })

    # Convert to DataFrame
    master_df = pd.DataFrame(canonical_rows)
    
    # Deduplicate (keep village over subdistrict if codes clash, though unlikely with our padding)
    master_df = master_df.drop_duplicates(subset=['location_id'], keep='first')

    # Save to CSV
    master_df.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"Successfully created Unified Gold Spine at: {output_path}")
    print(f"Total records: {len(master_df)}")

if __name__ == "__main__":
    main()
