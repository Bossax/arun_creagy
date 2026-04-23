import pandas as pd
import matplotlib.pyplot as plt
import os

# Configuration
input_file = "ψ/incubate/DCCE/CRI/data_system/metadata/analysis/thailand_capital_stock_silver.csv"
output_dir = "ψ/incubate/DCCE/CRI/data_system/metadata/analysis/"
os.makedirs(output_dir, exist_ok=True)

def generate_report_visuals():
    df = pd.read_csv(input_file)
    df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
    
    # Filter for stock indicators (Constant prices)
    stock_df = df[df['INDICATOR'].str.contains('Capital stock', case=False) & 
                  df['INDICATOR'].str.contains('Constant prices', case=False)].copy()
    
    # Filter for investment indicators (% of GDP)
    inv_df = df[df['INDICATOR'].str.contains('Gross fixed capital formation', case=False) & 
                df['INDICATOR'].str.contains('Percent of GDP', case=False)].copy()

    # 1. Plot: Evolution of Total Capital Stocks (Public vs Private)
    plt.figure(figsize=(10, 6))
    for sector in stock_df['SECTOR'].unique():
        sector_data = stock_df[stock_df['SECTOR'] == sector].sort_values('Year')
        plt.plot(sector_data['Year'], sector_data['Value'], label=sector, linewidth=2)
    
    plt.title("Thailand: Evolution of Productive 'Hardware' (Capital Stocks)", fontsize=14)
    plt.xlabel("Year")
    plt.ylabel("Billion International Dollars (2017 PPP)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.savefig(os.path.join(output_dir, "report_capital_stocks.png"))
    plt.close()

    # 2. Plot: Investment Intensity (Gross Fixed Capital Formation as % of GDP)
    plt.figure(figsize=(10, 6))
    for sector in inv_df['SECTOR'].unique():
        sector_data = inv_df[inv_df['SECTOR'] == sector].sort_values('Year')
        plt.plot(sector_data['Year'], sector_data['Value'], label=sector, marker='.', markersize=4)
    
    plt.title("Thailand: Investment Velocity (Capital Formation as % of GDP)", fontsize=14)
    plt.xlabel("Year")
    plt.ylabel("% of GDP")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.savefig(os.path.join(output_dir, "report_investment_velocity.png"))
    plt.close()

    # 3. Plot: Latest Stock Composition (Bar)
    plt.figure(figsize=(8, 6))
    latest_year = stock_df['Year'].max()
    latest_data = stock_df[stock_df['Year'] == latest_year]
    plt.bar(latest_data['SECTOR'], latest_data['Value'], color=['#1f77b4', '#ff7f0e', '#2ca02c'])
    plt.title(f"Composition of Thailand's Structural Floor ({int(latest_year)})", fontsize=14)
    plt.ylabel("Billion International Dollars")
    plt.savefig(os.path.join(output_dir, "report_stock_composition.png"))
    plt.close()

    print("Visualizations generated successfully using Matplotlib.")

if __name__ == "__main__":
    generate_report_visuals()
