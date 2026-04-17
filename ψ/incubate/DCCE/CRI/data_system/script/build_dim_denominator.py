import pandas as pd
import os

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    silver_dir = os.path.join(base_dir, 'data', '0_bronze', 'tei_pilot') # Pilot data is in Bronze since it's "source" for benchmarks
    gold_dir = os.path.join(base_dir, 'data', '2_gold')
    
    pop_path = os.path.join(silver_dir, 'population_avg_2559_2566.csv')
    gpp_path = os.path.join(silver_dir, 'gpp_agri_avg_2559_2566.csv')
    dim_loc_path = os.path.join(gold_dir, 'dim_location_master.csv')
    output_path = os.path.join(gold_dir, 'dim_denominator.csv')

    print("Loading denominator source data...")
    df_pop = pd.read_csv(pop_path)
    df_gpp = pd.read_csv(gpp_path)
    
    dim_loc = pd.read_csv(dim_loc_path, dtype=str)
    province_map = dim_loc[['province_name_th', 'province_code']].drop_duplicates()

    # 1. Align Population
    print("Aligning population denominators...")
    df_pop = df_pop.merge(province_map, left_on='province_name_th', right_on='province_name_th', how='left')
    
    # 2. Align GPP
    print("Aligning GPP denominators...")
    df_gpp = df_gpp.merge(province_map, left_on='province_name_th', right_on='province_name_th', how='left')

    # 3. Merge into single denominator table
    print("Merging denominators...")
    # Standardize columns: location_id (Provincial), pop_avg, gpp_agri_avg
    
    denom_df = df_pop[['province_code', 'population_avg_2559_2566']].copy()
    denom_df = denom_df.merge(df_gpp[['province_code', 'gpp_agriculture_avg_2559_2566']], on='province_code', how='outer')
    
    denom_df['location_id'] = denom_df['province_code'].str.zfill(2) + '000000'
    denom_df = denom_df.rename(columns={
        'population_avg_2559_2566': 'pop_avg_pilot',
        'gpp_agriculture_avg_2559_2566': 'gpp_agri_avg_pilot'
    })

    # Save to Gold
    denom_df[['location_id', 'pop_avg_pilot', 'gpp_agri_avg_pilot']].to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"Successfully created Denominator Table at: {output_path}")

if __name__ == "__main__":
    main()
