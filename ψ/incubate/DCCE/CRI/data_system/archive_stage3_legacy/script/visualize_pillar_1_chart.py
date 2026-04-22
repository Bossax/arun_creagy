import pandas as pd
import os
import warnings

warnings.filterwarnings('ignore')

# -------------------------------------------------------------------------
# Configuration & Paths
# -------------------------------------------------------------------------
BASE_DIR = r"C:\Users\sitth\OracleWorkspace\Arun_Creagy\ψ\incubate\DCCE\CRI\data_system\data"
SILVER_IMPACT_PATH = os.path.join(BASE_DIR, '1_silver', 'ddpm', 'master_village_disaster_stat_2557_2567.csv')
OUTPUT_DIR = os.path.join(BASE_DIR, '..', 'artifacts', 'visualizations')
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_CHART_PATH = os.path.join(OUTPUT_DIR, 'pillar1_human_impact_distribution.html')

def main():
    print("=== CRI Phase 1: Pillar 1 (Human Impact) Country-Wide Visualization ===")
    
    # 1. Load Administrative Baseline (Numerators)
    print("Loading DDPM Silver Impact Data...")
    try:
        df = pd.read_csv(SILVER_IMPACT_PATH, low_memory=False)
    except FileNotFoundError:
        print(f"Error: Could not find the file at {SILVER_IMPACT_PATH}")
        return
        
    # Clean province names (handle variants identified in audit)
    df['Province'] = df['Province'].str.strip()
    df['Province'] = df['Province'].replace({'กทม.': 'กรุงเทพมหานคร', 'กรุงเทพฯ': 'กรุงเทพมหานคร'})
    
    # 2. Aggregate Data to Provincial Level
    print("Aggregating Affected Households & Deaths by Province...")
    for col in ['Affected Households', 'Deaths']:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
        
    agg_df = df.groupby('Province')[['Affected Households', 'Deaths']].sum().reset_index()
    agg_df = agg_df.sort_values(by='Affected Households', ascending=False)
    
    top_provinces = agg_df.head(20)
    
    # Extract data for JavaScript
    labels = top_provinces['Province'].tolist()
    households = top_provinces['Affected Households'].tolist()
    
    total_hh = agg_df['Affected Households'].sum()
    top20_hh = sum(households)
    concentration = (top20_hh / total_hh) * 100 if total_hh > 0 else 0

    # 3. Generate HTML Visualization using Chart.js
    print("Generating Interactive HTML Chart...")
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="th">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CRI Pillar 1: Human Impact Baseline</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; padding: 20px; background-color: #f8f9fa; }}
            .container {{ background-color: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); max-width: 1200px; margin: auto; }}
            h1 {{ color: #2c3e50; text-align: center; margin-bottom: 5px; }}
            p.subtitle {{ text-align: center; color: #7f8c8d; margin-bottom: 30px; font-style: italic; }}
            canvas {{ margin-top: 20px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Pillar 1: Top 20 Provinces by Human Impact</h1>
            <p class="subtitle">Administrative Baseline (DDPM Silver Data 2557-2567)<br>
            Note: Top 20 provinces account for {concentration:.1f}% of all affected households.</p>
            <canvas id="impactChart" height="120"></canvas>
        </div>

        <script>
            const ctx = document.getElementById('impactChart').getContext('2d');
            const impactChart = new Chart(ctx, {{
                type: 'bar',
                data: {{
                    labels: {labels},
                    datasets: [{{
                        label: 'Total Affected Households',
                        data: {households},
                        backgroundColor: 'rgba(54, 162, 235, 0.7)',
                        borderColor: 'rgba(54, 162, 235, 1)',
                        borderWidth: 1
                    }}]
                }},
                options: {{
                    responsive: true,
                    plugins: {{
                        legend: {{ position: 'top' }},
                        tooltip: {{
                            callbacks: {{
                                label: function(context) {{
                                    return context.parsed.y.toLocaleString() + ' Households';
                                }}
                            }}
                        }}
                    }},
                    scales: {{
                        y: {{ beginAtZero: true, title: {{ display: true, text: 'Number of Affected Households' }} }},
                        x: {{ title: {{ display: true, text: 'Province (จังหวัด)' }} }}
                    }}
                }}
            }});
        </script>
    </body>
    </html>
    """
    
    with open(OUTPUT_CHART_PATH, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    print(f"\nSuccess! Interactive Chart saved to: {OUTPUT_CHART_PATH}")
    print("Open this HTML file in any web browser to view.")

if __name__ == "__main__":
    main()

