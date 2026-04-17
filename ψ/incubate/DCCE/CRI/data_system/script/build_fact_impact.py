import pandas as pd
import os

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    silver_dir = os.path.join(base_dir, 'data', '1_silver')
    gold_dir = os.path.join(base_dir, 'data', '2_gold')
    
    bkk_path = os.path.join(silver_dir, 'bma', 'bkk_hazard_impact_yearly.csv')
    ddpm_path = os.path.join(silver_dir, 'ddpm', 'master_village_disaster_stat_2557_2567.csv')
    dim_loc_path = os.path.join(gold_dir, 'dim_location_master.csv')
    old_dim_loc_path = os.path.join(gold_dir, 'dim_location.csv') # Need this to map BKK LOC IDs
    output_path = os.path.join(gold_dir, 'fact_impact.csv')

    print("Loading data for harmonization...")
    dim_loc = pd.read_csv(dim_loc_path, dtype=str)
    
    # 1. Harmonize BMA Data
    print("Processing BMA impact data...")
    df_bkk = pd.read_csv(bkk_path, dtype={'report_year_be': str})
    df_old_loc = pd.read_csv(old_dim_loc_path)
    
    # Map BKK LOC_IDs to Names then to DOPA codes
    # BKK data in silver uses LOC_IDs from the old dim_location
    bkk_mapping = df_old_loc[df_old_loc['source'] == 'BMA'][['location_id', 'district_name_th', 'subdistrict_name_th']]
    df_bkk = df_bkk.merge(bkk_mapping, left_on='location_id', right_on='location_id', how='left')
    
    # Map Names to DOPA Codes (Gold Spine)
    # Filter Gold Spine for BKK (province_code 10)
    bkk_spine = dim_loc[dim_loc['province_code'] == '10'].copy()
    
    def get_bkk_code(row):
        # Match subdistrict name in BKK spine
        match = bkk_spine[bkk_spine['subdistrict_name_th'] == row['subdistrict_name_th']]
        if not match.empty:
            return match.iloc[0]['location_id']
        return None

    df_bkk['canonical_location_id'] = df_bkk.apply(get_bkk_code, axis=1)
    
    # Prepare BMA for fact table
    bma_fact = pd.DataFrame({
        'year_be': df_bkk['report_year_be'],
        'location_id': df_bkk['canonical_location_id'],
        'hazard_type_id': df_bkk['hazard_type_id'], # Keep source IDs for now, join dim_hazard later
        'deaths': df_bkk['deaths_count'].fillna(0),
        'affected': df_bkk['affected_people_count'].fillna(0),
        'relief_baht': df_bkk['relief_amount_baht'].fillna(0),
        'source': 'BMA'
    })

    # 2. Harmonize DDPM Data
    print("Processing DDPM village impact data...")
    df_ddpm = pd.read_csv(ddpm_path, low_memory=False, dtype={'Village Code': str, 'ปี': str})
    
    # Standardize numeric columns
    num_cols = ['Deaths', 'Affected People', 'Agriculture Damage'] # Added some key ones
    for col in num_cols:
        if col in df_ddpm.columns:
            df_ddpm[col] = pd.to_numeric(df_ddpm[col], errors='coerce').fillna(0)

    ddpm_fact = pd.DataFrame({
        'year_be': df_ddpm['ปี'],
        'location_id': df_ddpm['Village Code'].str.zfill(8),
        'hazard_type_id': df_ddpm['Disaster Type'], # Text-based in DDPM
        'deaths': df_ddpm['Deaths'],
        'affected': df_ddpm['Affected People'],
        'relief_baht': 0, # DDPM stats don't include relief amount (it's in the other table)
        'source': 'DDPM_VILLAGE'
    })

    # 3. Combine and Finalize
    print("Combining datasets...")
    fact_impact = pd.concat([bma_fact, ddpm_fact], ignore_index=True)
    
    # Remove records with missing location_id (failed mapping)
    initial_count = len(fact_impact)
    fact_impact = fact_impact.dropna(subset=['location_id'])
    print(f"Dropped {initial_count - len(fact_impact)} records due to missing location IDs.")

    # Save to Gold
    fact_impact.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"Successfully created Unified Fact Impact at: {output_path}")
    print(f"Total records: {len(fact_impact)}")

if __name__ == "__main__":
    main()
