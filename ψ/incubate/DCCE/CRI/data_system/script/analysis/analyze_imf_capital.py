import pandas as pd
import matplotlib.pyplot as plt
import os

# Configuration
input_file = "0_bronze/imf/imf_capital_stock_raw.csv"
output_dir = "ψ/incubate/DCCE/CRI/data_system/metadata/analysis/"
os.makedirs(output_dir, exist_ok=True)

def analyze_thailand_capital():
    print("--- Ingesting and Analyzing IMF Capital Stock for Thailand ---")
    
    # Load dataset
    df = pd.read_csv(input_file)
    
    # Filter for Thailand
    # Note: Some datasets use 'Thailand' or 'Thailand, Kingdom of'
    th_df = df[df['COUNTRY'].str.contains('Thailand', case=False, na=False)].copy()
    
    if th_df.empty:
        print("Error: No data found for Thailand.")
        return

    # Identify metadata columns vs year columns
    meta_cols = [c for c in th_df.columns if not c.isdigit()]
    year_cols = [c for c in th_df.columns if c.isdigit()]
    
    # Melt the dataframe for analysis (Wide to Long)
    th_long = th_df.melt(id_vars=['SERIES_CODE', 'INDICATOR', 'SECTOR', 'PRICES', 'UNIT'], 
                         value_vars=year_cols, 
                         var_name='Year', 
                         value_name='Value')
    
    th_long['Year'] = th_long['Year'].astype(int)
    th_long['Value'] = pd.to_numeric(th_long['Value'], errors='coerce')
    
    # 1. Overview of available indicators for TH
    print("\nAvailable Indicators for Thailand:")
    print(th_df['INDICATOR'].unique())
    
    # 2. Filter for key "Stock" indicators (Constant PPP prices)
    # We prioritize 'Capital stock' in 'Constant prices' and 'Purchasing power parity' 
    # to measure 'Structural Potential' without inflation noise.
    stock_targets = [
        'Capital stock, General government, Constant prices, Purchasing power parity (PPP) international dollar, ICP benchmark 2017',
        'Capital stock, Private sector, Constant prices, Purchasing power parity (PPP) international dollar, ICP benchmark 2017'
    ]
    
    analysis_df = th_long[th_long['INDICATOR'].isin(stock_targets)].copy()
    
    # Summary Statistics (Latest Year vs Historical)
    latest_year = analysis_df['Year'].max()
    print(f"\n--- Capital Stock Statistics (Thailand, {latest_year}) ---")
    for indicator in stock_targets:
        val = analysis_df[(analysis_df['INDICATOR'] == indicator) & (analysis_df['Year'] == latest_year)]['Value'].values
        if len(val) > 0:
            print(f"{indicator}: {val[0]:,.2f} billion")

    # 3. Visualization: Trend of Public vs Private Capital Stock (Structural Floor)
    plt.figure(figsize=(12, 6))
    for sector in ['General government', 'Private sector']:
        data = analysis_df[analysis_df['SECTOR'] == sector].sort_values('Year')
        plt.plot(data['Year'], data['Value'], label=sector, marker='o', markersize=2)
    
    plt.title("Thailand: Public vs Private Capital Stock (Constant 2017 PPP $)")
    plt.xlabel("Year")
    plt.ylabel("Value (Billion International Dollars)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(os.path.join(output_dir, "th_capital_stock_trend.png"))
    print(f"\nTrend plot saved to {output_dir}")

    # Export clean Silver-layer data for Thailand
    th_long.to_csv("ψ/incubate/DCCE/CRI/data_system/metadata/analysis/thailand_capital_stock_silver.csv", index=False)
    print("Silver layer data exported.")

if __name__ == "__main__":
    analyze_thailand_capital()
