import pandas as pd
import os

# Paths relative to script directory
BRONZE_FILE = '../data/0_bronze/tei_pilot/casualties_by_hazard_2559_2566.csv'
SILVER_SPINE = '../data/1_silver/dopa/dim_location_master.csv'
SILVER_OUTPUT = '../data/1_silver/tei_pilot/provincial_casualties_clean.csv'

def main():
    # Resolve absolute paths relative to script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    bronze_path = os.path.normpath(os.path.join(script_dir, BRONZE_FILE))
    spine_path = os.path.normpath(os.path.join(script_dir, SILVER_SPINE))
    silver_path = os.path.normpath(os.path.join(script_dir, SILVER_OUTPUT))

    print(f"Loading Silver spine from {spine_path}...")
    if not os.path.exists(spine_path):
        print(f"Error: Silver spine not found at {spine_path}")
        return

    # Load unique province mapping from Silver spine
    # province_code is 2-digit, province_name_th is Thai name
    try:
        spine_df = pd.read_csv(spine_path, dtype={'province_code': str})
    except Exception as e:
        print(f"Error reading Silver spine: {e}")
        return

    # Extract unique mapping
    province_map = spine_df[['province_name_th', 'province_code']].drop_duplicates().dropna()
    
    # Create dictionary for mapping
    # Clean up names to handle potential whitespace or encoding artifacts
    mapping_dict = dict(zip(province_map['province_name_th'].astype(str).str.strip(), province_map['province_code']))
    
    print(f"Found mapping for {len(mapping_dict)} provinces.")

    print(f"Loading Bronze TEI data from {bronze_path}...")
    if not os.path.exists(bronze_path):
        print(f"Error: Bronze file not found at {bronze_path}")
        return

    try:
        tei_df = pd.read_csv(bronze_path)
    except Exception as e:
        print(f"Error reading Bronze file: {e}")
        return
    
    # Map province names to codes
    # Use str.strip() to ensure robust matching
    tei_df['province_name_th_clean'] = tei_df['province_name_th'].astype(str).str.strip()
    tei_df['province_code'] = tei_df['province_name_th_clean'].map(mapping_dict)
    
    # Check for unmapped provinces
    unmapped = tei_df[tei_df['province_code'].isna()]['province_name_th'].unique()
    if len(unmapped) > 0:
        print(f"Warning: The following provinces were not found in Silver spine: {unmapped}")
    
    # Reorder columns and drop the intermediate clean column
    output_cols = ['province_code', 'province_name_th', 'hazard_code', 'hazard_name_th', 
                   'injured_count_avg_2559_2566', 'deaths_count_avg_2559_2566']
    
    # Select desired columns
    # We keep rows even if unmapped, but they will have NaN in province_code (user might want to filter them)
    silver_df = tei_df[output_cols].copy()
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(silver_path), exist_ok=True)
    
    print(f"Saving cleaned data to {silver_path}...")
    # Use utf-8-sig to ensure Excel compatibility with Thai characters
    silver_df.to_csv(silver_path, index=False, encoding='utf-8-sig')
    print("Process completed successfully.")

if __name__ == "__main__":
    main()
