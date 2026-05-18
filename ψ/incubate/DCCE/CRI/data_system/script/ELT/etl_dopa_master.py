import pandas as pd
import os
import re

def normalize_admin_name(value):
    if value is None: return ""
    # Standardize whitespace and invisible characters
    s = str(value).strip()
    s = s.replace("\u200b", "").replace("\xa0", " ").replace("\r", "").replace("\n", "")
    s = re.sub(r"\s+", " ", s)
    # Strip common admin prefixes
    prefixes = ["จังหวัด", "จ.", "อำเภอ", "อ.", "เขต", "ตำบล", "ต.", "แขวง", "กิ่งอำเภอ"]
    for p in prefixes:
        if s.startswith(p):
            s = s[len(p):].strip()
    return s.replace("ฯ", "").strip()

def main():
    # Resolve project root: ψ/incubate/DCCE/CRI/data_system/
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(script_dir))
    
    bronze_dir = os.path.join(project_root, 'data', '0_bronze', 'dopa')
    output_dir = os.path.join(project_root, 'data', '2_gold', 'dopa')
    
    ccaatt_path = os.path.join(bronze_dir, 'ccaatt.xlsx')
    village_path = os.path.join(bronze_dir, 'code_village_dopa_2019.xls')
    output_path = os.path.join(output_dir, 'dim_location_master.csv')

    os.makedirs(output_dir, exist_ok=True)

    # 1. Parse CCAATT: The Absolute Hierarchy Schema
    print(f"Loading {ccaatt_path}...")
    df_cc = pd.read_excel(ccaatt_path, engine='openpyxl', skiprows=4, header=None)
    df_cc.columns = ['code', 'name_th', 'name_en', 'status']
    df_cc = df_cc[df_cc['status'] == 0].copy()
    df_cc['code'] = df_cc['code'].astype(str).str.zfill(8)
    
    p_map, a_map, t_map = {}, {}, {}
    
    print("Extracting Canonical Schema (CCAATT)...")
    for _, row in df_cc.iterrows():
        c, n = row['code'], normalize_admin_name(row['name_th'])
        if c.endswith('000000'): p_map[c[:2]] = n
        elif c.endswith('0000'): a_map[c[:4]] = n
        elif c.endswith('00'): t_map[c[:6]] = n

    # 2. Parse Village List: The Unverified Candidates
    print(f"Loading {village_path}...")
    df_v = pd.read_excel(village_path, engine='openpyxl', dtype=str)
    
    canonical_rows = []
    
    def clean_code(val, length):
        if pd.isna(val): return None
        return str(val).replace('.0', '').strip().zfill(length)

    print("Executing Hierarchical Schema Validation on Village List...")
    stats = {'total': 0, 'invalid_p': 0, 'invalid_a': 0, 'invalid_t': 0, 'passed': 0}
    
    for _, row in df_v.iterrows():
        stats['total'] += 1
        p_c = clean_code(row['PROV_CODE'], 2)
        a_c = clean_code(row['AMP_CODE'], 4)
        t_c = clean_code(row['TAM_CODE'], 6)
        v_c = clean_code(row['VILL_CODE'], 8)

        # Multi-Tier Validation Gate
        if p_c not in p_map: 
            stats['invalid_p'] += 1; continue
        if a_c not in a_map: 
            stats['invalid_a'] += 1; continue
        if t_c not in t_map: 
            stats['invalid_t'] += 1; continue
            
        # ENFORCE CCAATT nomenclature strictly
        canonical_rows.append({
            'location_id': v_c,
            'province_code': p_c, 'province_name_th': p_map[p_c],
            'district_code': a_c, 'district_name_th': a_map[a_c],
            'subdistrict_code': t_c, 'subdistrict_name_th': t_map[t_c],
            'village_code': v_c, 'village_name_th': str(row['VILL_T']).strip() if pd.notna(row['VILL_T']) else '',
            'admin_level': 'village', 'source': 'DOPA_2019'
        })
        stats['passed'] += 1

    print(f"Validation Finished: {stats['passed']}/{stats['total']} records passed.")
    print(f"Discarded: {stats['invalid_p']} (Prov), {stats['invalid_a']} (Amphoe), {stats['invalid_t']} (Tambon)")

    # 3. Completeness Pass: Inject missing Subdistrict hierarchy
    print("Ensuring coverage for administrative subdistricts (no-village zones)...")
    for t_c, t_n in t_map.items():
        canonical_rows.append({
            'location_id': t_c + '00',
            'province_code': t_c[:2], 'province_name_th': p_map[t_c[:2]],
            'district_code': t_c[:4], 'district_name_th': a_map[t_c[:4]],
            'subdistrict_code': t_c, 'subdistrict_name_th': t_n,
            'village_code': '', 'village_name_th': '',
            'admin_level': 'subdistrict', 'source': 'CCAATT'
        })

    master_df = pd.DataFrame(canonical_rows)
    master_df = master_df.drop_duplicates(subset=['location_id'], keep='first')
    master_df.to_csv(output_path, index=False, encoding='utf-8-sig')
    
    print(f"Cleaned GOLD Spine created: {output_path} ({len(master_df)} records)")

if __name__ == "__main__":
    main()
