import pandas as pd
import os
import urllib.request
import json
import warnings
warnings.filterwarnings('ignore')

# -------------------------------------------------------------------------
# Configuration & Paths
# -------------------------------------------------------------------------
BASE_DIR = r"C:\Users\sitth\OracleWorkspace\Arun_Creagy\ψ\incubate\DCCE\CRI\data_system\data"
SILVER_IMPACT_PATH = os.path.join(BASE_DIR, '1_silver', 'ddpm', 'master_village_disaster_stat_2557_2567.csv')
OUTPUT_DIR = os.path.join(BASE_DIR, '..', 'artifacts', 'maps')

os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_MAP_PATH = os.path.join(OUTPUT_DIR, 'pillar1_human_impact_baseline.html')

# GeoJSON with Thai Province Names
# We use a reliable open-source GeoJSON for Thailand provinces
GEOJSON_URL = "https://raw.githubusercontent.com/apisit/thailand.json/master/thailandWithVT.geojson"
LOCAL_GEOJSON = os.path.join(BASE_DIR, '..', 'artifacts', 'maps', 'thailand_provinces.geojson')

def download_geojson():
    if not os.path.exists(LOCAL_GEOJSON):
        print("Downloading Thailand GeoJSON...")
        urllib.request.urlretrieve(GEOJSON_URL, LOCAL_GEOJSON)
    with open(LOCAL_GEOJSON, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    print("=== CRI Phase 1: Pillar 1 (Human Impact) Visualization ===")
    
    # 1. Load Administrative Baseline (Numerators)
    print("Loading DDPM Silver Impact Data...")
    df = pd.read_csv(SILVER_IMPACT_PATH, low_memory=False)
    
    # Clean province names (handle variants identified in audit)
    # Note: 'Province' is the column in DDPM silver file
    df['Province'] = df['Province'].str.strip()
    df['Province'] = df['Province'].replace({'กทม.': 'กรุงเทพมหานคร', 'กรุงเทพฯ': 'กรุงเทพมหานคร'})
    
    # 2. Aggregate Data to Provincial Level
    # In full Pillar 1, we downscale to 100m. Here we visualize the country-wide total 
    # to identify the "Hotspots" before applying the WorldPop constraints.
    print("Aggregating Affected Households & Deaths by Province...")
    agg_df = df.groupby('Province')[['Affected Households', 'Deaths', 'Affected People']].sum().reset_index()
    
    # 3. Load Spatial Boundaries
    geo_data = download_geojson()
    
    # The apisit GeoJSON uses "name" for the Thai province name in its properties.
    # We will map our 'Province' to 'name' in the geojson.
    
    # 4. Generate Interactive Map using Folium
    try:
        import folium
    except ImportError:
        print("Folium not installed. Please install using: pip install folium")
        return
        
    print("Generating Choropleth Map...")
    
    # Center map on Thailand
    m = folium.Map(location=[13.736717, 100.523186], zoom_start=6, tiles='cartodb positron')
    
    # Add Affected Households Choropleth
    folium.Choropleth(
        geo_data=geo_data,
        name='Affected Households (DDPM Total 2557-2567)',
        data=agg_df,
        columns=['Province', 'Affected Households'],
        key_on='feature.properties.name',
        fill_color='YlOrRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Total Affected Households',
        highlight=True
    ).add_to(m)

    # Add Deaths Choropleth as an optional layer
    folium.Choropleth(
        geo_data=geo_data,
        name='Deaths (DDPM Total 2557-2567)',
        data=agg_df,
        columns=['Province', 'Deaths'],
        key_on='feature.properties.name',
        fill_color='PuRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Total Deaths',
        highlight=True,
        show=False # Hidden by default
    ).add_to(m)
    
    # 5. (Future) WorldPop Raster Overlay Placeholder
    # This serves as the integration point for Phase 2, Stage 3 (Constrained Redistribution)
    # where we will use `rasterio` to mask the 100m population counts.
    # raster_layer = folium.raster_layers.ImageOverlay(...)
    
    folium.LayerControl().add_to(m)
    
    m.save(OUTPUT_MAP_PATH)
    print(f"\nSuccess! Map saved to: {OUTPUT_MAP_PATH}")
    print("Open this HTML file in any web browser to explore the Pillar 1 Administrative Baseline.")

if __name__ == "__main__":
    main()
