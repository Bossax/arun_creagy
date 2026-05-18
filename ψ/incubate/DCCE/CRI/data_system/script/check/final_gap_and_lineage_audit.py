import pandas as pd
import os

BASE_DIR = r"C:\Users\sitth\OracleWorkspace\Arun_Creagy\ψ\incubate\DCCE\CRI\data_system\data"
SILVER_SPINE_PATH = os.path.join(BASE_DIR, '1_silver', 'dopa', 'dim_location_master.csv')

def load_silver_spine():
    df = pd.read_csv(SILVER_SPINE_PATH, dtype={'province_code': str})
    return df[['province_name_th', 'province_code']].drop_duplicates()

def audit_file(file_path, name, name_col, spine):
    print(f"\n{'='*20} AUDIT: {name} {'='*20}")
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
        
    df = pd.read_csv(file_path)
    unique_names = df[name_col].unique()
    total_provinces = len(unique_names)
    
    # Check mapping
    merged = pd.DataFrame({name_col: unique_names}).merge(spine, left_on=name_col, right_on='province_name_th', how='left')
    unmapped = merged[merged['province_code'].isna()][name_col].tolist()
    
    mapping_rate = ((total_provinces - len(unmapped)) / total_provinces) * 100
    
    print(f"Total Provinces: {total_provinces}")
    print(f"Mapping Rate to DOPA: {mapping_rate:.2f}%")
    if unmapped:
        print(f"Unmapped Variants: {unmapped}")
    
    # Gap Analysis (Zeros/Nulls)
    metric_cols = [c for c in df.columns if any(m in c.lower() for m in ['death', 'affect', 'baht', 'relief', 'avg'])]
    for col in metric_cols:
        zeros = (df[col] == 0).sum()
        nulls = df[col].isna().sum()
        print(f"Column '{col:25}': Zeros={zeros:5} | Nulls={nulls:5}")

def main():
    spine = load_silver_spine()
    
    # 1. TEI Pilot Files
    audit_file(os.path.join(BASE_DIR, '0_bronze', 'tei_pilot', 'casualties_by_hazard_2559_2566.csv'), "TEI Casualties", "province_name_th", spine)
    audit_file(os.path.join(BASE_DIR, '0_bronze', 'tei_pilot', 'relief_by_hazard_2559_2566.csv'), "TEI Relief", "province_name_th", spine)
    audit_file(os.path.join(BASE_DIR, '0_bronze', 'tei_pilot', 'population_avg_2559_2566.csv'), "TEI Population", "province_name_th", spine)
    
    # 2. DDPM Silver Files
    audit_file(os.path.join(BASE_DIR, '1_silver', 'ddpm', 'master_financial_relief_by_hazard.csv'), "DDPM Silver Relief", "จังหวัด", spine)

if __name__ == "__main__":
    main()
