---
type: report
tags: []
source:
authors:
  - GHG Protocol
year:
relevance_to: "[[Land Sector and Removals Standard version 1 from NotebookLM]]"
key_findings: []
status: evergreen
---
# 1. Scope and Core Updates

The transition from the Pilot Testing Draft to the Official Standard (Version 1.0) introduces fundamental changes to who must report, what activities are covered, and how baselines are managed to ensuring environmental integrity.

## Key Scope Changes

- **Forestry Excluded:** Version 1.0 applies specifically to **agriculture** and **CO2 removal technologies** (e.g., DACCS, BECCS). It explicitly **does not apply to forestry** or forest carbon accounting.
    
    - _Implication:_ Companies with mixed portfolios (e.g., agroforestry or timber) must wait for future guidance on the forestry portion of their inventory. This exclusion allows the Standard to focus on resolving the complexities of agricultural fluxes first without being delayed by the unique permanence issues inherent in commercial forestry.
        
- **Strict Baselines & Re-baselining:** To prevent "paper reductions"—where emissions appear to drop simply because a company switched to a better calculation method—companies must **re-baseline** (recalculate base years).
    
    - _Triggers:_ Re-baselining is mandatory if a company switches LUC calculation approaches (e.g., moving from the statistical sLUC method to direct dLUC) or significantly improves data quality (e.g., replacing non-spatial census data with spatial satellite mapping). This ensures that reported reductions reflect actual changes in the atmosphere, not just improvements in data granularity.
        
- **GHG Credits & Adjusted Reporting:** The Standard formalizes the separation between a company's physical impact and its market-based offsetting claims by requiring two distinct sets of values:
    
    1. **Physical GHG Inventory:** A true account of emissions and removals occurring within the company's value chain, independent of any credit purchases or sales. This represents what the atmosphere actually "sees."
        
    2. **Adjusted Emissions and Removals:** These values are adjusted to account for credits issued or sold (which must be deducted to avoid double claiming) or credits purchased (if applicable to specific reporting frameworks). This separation increases transparency regarding how much progress is achieved through internal abatement versus market mechanisms.
        

# 2. Land Management Emissions (Existing Land)

This section covers emissions from land that remains in the same use over time (e.g., farming on existing cropland or grazing on pasture). It addresses the continuous fluxes of carbon between the atmosphere and the land.

## The "Managed Land Proxy" and Natural Disturbances

The Standard removes previous flexibility regarding how companies treat natural events, adopting a stricter precautionary approach.

- **The Rule:** For productive agricultural land, the Standard applies the **"Managed Land Proxy."** This dictates that because human management dominates the landscape, _all_ carbon stock changes are considered "anthropogenic" (human-caused). It is practically impossible to scientifically disentangle exactly which ton of carbon was lost due to climate change (natural) versus poor soil management (anthropogenic).
    
- **Natural Disturbances:** Consequently, companies **must fully account** for losses from natural disturbances such as wildfires, storms, pest outbreaks, or disease.
    
    - _Implication:_ A company cannot exclude emissions from a wildfire as an "act of God." If the carbon stock is lost, it must be reported as an emission in the inventory.
        
- **Reporting (Gross vs. Net):** While reduction targets typically track "Net" emissions (gains minus losses), companies are required to separately report **"Gross biogenic land CO2 emissions."**
    
    - _Why this matters:_ This transparency allows a company to explain the narrative behind their data. If a massive wildfire causes a spike in emissions, the "Net" figure might look disastrous. By showing the "Gross" figures, the company can demonstrate that the spike was driven by a specific disturbance event rather than a systematic failure in management practices.
        
- **Reversals:** This rule is critical for the integrity of carbon removals. If a natural disturbance releases carbon that was previously claimed as a removal (e.g., soil carbon sequestered over 5 years is lost in a drought), it must be reported as a **"Reversal"** if the land is no longer in the inventory. If the land remains in the inventory, it is reported as "Land management net biogenic CO2 emissions," effectively negating the prior benefit.
    

## Calculation Approaches & Hierarchy

The Standard establishes a hierarchy of data quality. Companies are eligible to use specific approaches depending on whether they are tracking emissions (losses) or removals (gains).

|Approach|Eligibility for Land Management Emissions|Eligibility for Land Management Removals|
|---|---|---|
|**Measurement-Based**|**Yes.** Involves direct sampling (e.g., soil cores) or forest inventories.|**Yes.** This is the **"Gold Standard."** Requirement 21.LMR mandates empirical data specific to the land carbon pools. Measurement is required either as the direct estimation method or to calibrate models/remote sensing.|
|**Model-Based**|**Yes.** Uses biogeochemical models (e.g., DayCent, RothC).|**Yes, but strictly conditional.** The model **must be calibrated** with empirical field data specific to the local soil, climate, and crop conditions. Generic global models are insufficient for claiming removals.|
|**Remote-Sensing**|**Yes.** Uses satellite imagery, LiDAR, or aerial photography.|**Yes, but strictly conditional.** Like models, remote sensing data **must be calibrated** with ground-truthing (field data) to verify that the satellite interpretation matches physical reality.|
|**Activity-Based**|**Yes.** Uses activity data (e.g., fertilizer amount) x emission factors.|**No.** Global or Tier 1 emission factors are **not accepted** for claiming removals. They lack the granularity to prove that carbon was actually stored in a specific location.|
|**No Stock Change**|**Yes.** (Permits reporting zero if stocks are likely a net sink but unmeasured).|**N/A.** You cannot claim removals under this assumption; it is a conservative fallback for emissions accounting only.|

## Production Emissions

- **Renaming:** Formerly referred to as "non-CO2 emissions," this category is now formally **"Land management production emissions"** to distinguish it clearly from carbon stock changes.
    
- **Inclusions:** This category covers:
    
    - **Livestock:** Enteric fermentation (methane) and manure management.
        
    - **Soils:** N2O from fertilizer application and crop residues.
        
    - **Rice:** Methane from anaerobic decomposition in flooded paddies.
        
    - **Peatland Rewetting:** The Standard explicitly adds **CH4 emissions from peatland rewetting**. While rewetting peatlands is excellent for stopping CO2 leaks, the re-introduction of water can create anaerobic conditions that generate methane. This trade-off must be accounted for.
        
- **Fossil Fuels:** On-site energy use (tractors, diesel irrigation pumps, heating) should ideally be reported under **"fossil fuel and industrial emissions"** (Scope 1 or 3 energy). However, if data systems cannot separate on-farm fuel use from other farming data, these emissions may be grouped here, provided the aggregation is disclosed.
    

# 3. Land Use Change (LUC) Accounting

This section covers the greenhouse gas impacts of converting natural ecosystems (like forests, grasslands, or wetlands) to other uses (like cropland or pasture). The accounting must look back over a **20-year assessment period** to capture the long-term carbon debt of conversion.

## The Hierarchy of Methods

The Standard replaces the previous flexibility (where companies chose the "most relevant" metric) with a strict **accuracy hierarchy**. Companies **shall** select the most accurate approach their data allows. This prevents companies from defaulting to global averages when they have the data to be more precise.

1. **Priority 1: LMU-Level Direct LUC (dLUC)**
    
    - **Traceability:** Requires traceability to the specific **Land Management Unit (LMU)**—the exact farm, field, or plot.
        
    - **Data:** Requires precise land boundaries (polygons) and historical land use maps for that specific polygon.
        
    - **Status:** This is the **Most Accurate** method and must be used if the data exists.
        
2. **Priority 2: Jurisdictional Direct LUC (dLUC)**
    
    - **Traceability:** Used when a company can trace product to a **sourcing region** (e.g., state, province, or municipality) but _not_ to the specific farm.
        
    - **Data:** Requires a **"Crop Extent Map"** (showing exactly where that specific crop is grown in that region) overlaid with historical land cover maps.
        
    - **Why it's "Direct":** Although it covers a region, it uses **spatial data** to physically observe overlap between crop production areas and deforestation. It avoids the broad generalizations of statistical methods, classifying it as "Direct" rather than "Statistical."
        
3. **Priority 3: Statistical LUC (sLUC)**
    
    - **Traceability:** Traceable only to a sourcing region or country.
        
    - **Data:** No spatial maps are available. It relies entirely on **census or statistical data** (e.g., FAO stats showing "crop area increased by X%" and "forest area decreased by Y%").
        
    - **Status:** This is the **Least Accurate** method. It spreads the burden of deforestation across all producers in a region, regardless of whether their specific land was actually deforested.
        

## Data Requirements for dLUC

- **Spatial Data:** dLUC calculation depends on spatial visibility. Valid data sources include satellite imagery, aerial photography, and direct field GPS data.
    
- **Land Cover vs. Land Use:** A critical distinction exists between what a satellite sees and what is happening on the ground.
    
    - _Land Cover:_ The physical material at the surface (e.g., trees, grass, concrete).
        
    - _Land Use:_ The socio-economic purpose (e.g., timber forestry, conservation, cattle grazing).
        
    - _The Challenge:_ Satellites measure cover. A harvest in a managed forest looks like "cover loss" (deforestation). However, if the land use remains "forestry" and trees are replanted, it is not land use change. Companies must use management data to distinguish temporary harvest from permanent conversion.
        
- **Maps:**
    
    - **LULC Maps:** Must cover the **20-year assessment period**. At a minimum, maps from the start and end of the period are required to detect change, though annual maps are preferred for accuracy.
        
    - **Crop Extent Map (for Jurisdictional dLUC):** This map must show **all** productive land for that specific crop in the region. It serves as a filter to exclude deforestation happening in areas where the company's crop isn't even grown.
        

## Deep Dive: Jurisdictional dLUC Workflow

For **Priority 2 (Jurisdictional dLUC)**, the Standard provides a sophisticated workflow to attribute regional emissions to a company that lacks farm-level traceability. This method bridges the gap between precise farm data and vague national statistics.

### 1. Crop Extent Map as a Spatial Filter

The "Crop Extent Map" acts as a spatial sieve. It ensures the company accounts only for deforestation that is spatially relevant to the product they buy.

- **Defining "Attributable" Land:** The map must be a **"spatial, non-statistical"** representation of the location of all **"attributable productive agricultural lands"** in the jurisdiction.
    
    - _Example:_ If a company sources soy from Mato Grosso, Brazil, the map must delineate exactly where soy—and only soy—is cultivated. It filters out deforestation occurring in the Amazon biome if the soy is only grown in the Cerrado biome within that state.
        
- **The Overlay Analysis:** This crop extent map is electronically overlaid with historical Land Use/Land Cover (LULC) maps covering the 20-year assessment period.
    
    - The analysis identifies specific pixels (locations) where the _current_ crop footprint overlaps with land that was converted from natural ecosystems (e.g., forest) during the relevant window.
        
    - This effectively isolates conversion driven by that specific commodity, filtering out deforestation caused by urbanization, mining, or other crops (like corn or cotton).
        

### 2. Calculation & Allocation of Carbon Stock Loss

Because the company lacks traceability to the specific farm, it must assume its share of the region's impact is proportional to its share of the region's production.

- **Creation of an Emission Factor:** The total LUC emissions calculated from the spatial overlay (Total Carbon Loss on Soy Lands) are divided by the total production volume of that crop in the jurisdiction.
    
    $$\frac{\text{Total Crop Specific LUC Emissions (tonnes CO2e)}}{\text{Total Crop Production Volume (tonnes)}} = \text{Jurisdictional Emission Factor (tCO2e/t)}$$
- **Attribution to the Company:** The company applies this emission factor to the volume of product it purchased. By doing so, the company is effectively allocated a weighted average of the deforestation associated with that specific crop in that specific region, rewarding sourcing from regions with cleaner crop footprints.
    

### 3. Summary of the Workflow

1. **Map:** Identify the specific footprint of the crop (e.g., soy) in the region.
    
2. **Overlay:** Cross-reference this footprint with historical deforestation maps.
    
3. **Sum:** Calculate the total carbon lost specifically on those crop lands.
    
4. **Allocate:** Assign a proportional share of those total emissions to the company based on the volume they purchased.
    

# 4. Allocation Methods

Allocation rules determine how to split emissions when a single system produces multiple valuable outputs (e.g., a soy crusher producing oil and meal, or a farm growing maize and beans together).

## For Statistical LUC (sLUC)

- **Product Expansion Method (Mandatory):** This method operates on the logic of "causality." It attributes sLUC emissions _only_ to crops that are expanding their land area in the region.
    
    - _Logic:_ If the soy area is growing and the forest area is shrinking, soy is the likely driver of deforestation. Crops with stable or shrinking areas are not penalized for land expansion they didn't cause.
        
- **Shared Responsibility (Exception):** This allocates emissions to _all_ crops in the region based on their total area. This is only permitted if the company provides specific justification regarding data limitations that prevent the use of the expansion method.
    

## For Direct LUC (dLUC) and Land Management

- **Processing Level (e.g., Oil vs. Meal):** When a raw material is processed into co-products, **Economic Allocation** is the standard.
    
    - _Why:_ Emissions should be split based on the economic value of the outputs. If soy oil drives the profitability of the crushing plant, it should carry the bulk of the embedded carbon, rather than splitting it by mass (which would overburden the heavier but cheaper soy meal).
        
- **Land Level (e.g., Intercropping):**
    
    1. **Economic Allocation:** (Preferred) Assign emissions based on the share of total economic value generated by each crop on the land.
        
    2. **Area-Time Allocation:** (Secondary) Assign emissions based on the physical resource use—specifically, the **square meter-years (**$m^2\text{-year}$**)** occupied by each product. This is used when economic prices are volatile or non-representative, but it requires detailed data on how long each crop occupies the soil.
        

# 5. Land Tracking & Leakage Metrics

The "menu of options" from the Draft is gone. The Standard now mandates specific metrics to ensure a complete picture of land use impacts.

## Reporting Requirements

1. **Land Occupation (Mandatory):** Companies _shall_ account for the total land area occupied (in hectares). This is a basic measure of the company's footprint on the planet's finite land surface.
    
2. **Carbon Opportunity Cost (COC) (Recommended):** This metric quantifies the "road not taken." It estimates how much carbon _could_ have been stored on that land if it were allowed to revert to its natural state (e.g., a forest) instead of being used for agriculture. It is a powerful metric for understanding the trade-offs of land use but remains optional.
    
3. **Land Carbon Leakage (Conditional Requirement):** Companies _must_ report leakage if they engage in **"High Risk Activities."** Leakage occurs when a company's action to reduce emissions in one place inadvertently causes emissions to increase elsewhere.
    

## High Risk Activities

Leakage reporting is triggered if a company engages in activities that are likely to displace production:

- **Non-Food/Non-Feed Use:** Diverting food crops to produce fuel (biofuels) or materials (bioplastics). The world still needs the food, so someone else will likely cut down a forest to replace the diverted supply.
    
- **LUC Reducing Food Production:** Converting productive cropland into forests (e.g., afforestation projects for carbon credits) that causes a significant reduction in food supply. This forces the market to find that food elsewhere, potentially driving deforestation outside the project boundary.
    
- **Yield Reduction:** Implementing "sustainable" practices (like drastically cutting fertilizer) that significantly drop crop yields per hectare. If the company buys the same volume, they now require more land to produce it, creating pressure to expand agriculture elsewhere.
    

# 6. Bioenergy Accounting

The Standard reinforces that **bioenergy cannot be assumed to be carbon neutral**. Burning biomass releases CO2, and that CO2 must be accounted for.

### Biogenic CO2 Reporting

How you report combustion emissions depends entirely on whether you are tracking the carbon stock changes on the land where the biomass grew:

- **Scenario 1 (Full Tracking):** This applies if you report **all life cycle emissions**, including the annual net land carbon stock changes of the sourcing lands.
    
    - _Accounting:_ You report combustion CO2 separately as **"Gross CO2 Fluxes"**.
        
    - _Logic:_ Since you have already counted the carbon loss (harvest) in your land sector inventory, counting the combustion emissions in Scope 1 would be double counting. Reporting it as a "Flux" ensures transparency without inflating the inventory.
        
- **Scenario 2 (Incomplete Tracking):** This applies if you do _not_ track the full life cycle (e.g., buying wood pellets from a generic market) or lack traceability.
    
    - _Accounting:_ You must report combustion CO2 under **"Land Emissions"** in your physical inventory (Scope 1, 2, or 3).
        
    - _Logic:_ Because you did not account for the carbon loss at the forest level, you must account for it at the smokestack. This treats bioenergy similarly to fossil fuels to ensure the climate impact is not ignored.
        

### Other Bioenergy Rules

- **Non-CO2:** Emissions of CH4 and N2O from combustion are _always_ reported in the physical inventory under "Biogenic Product Emissions," regardless of the scenario.
    
- **Upstream:** All upstream life cycle emissions (LUC, fertilizer, harvesting machinery) for purchased bioenergy must be reported in **Scope 3, Category 3** (Fuel- and energy-related activities).
    
- **BECCS (Bioenergy with Carbon Capture and Storage):** This can be claimed as a "Removal with Geologic Storage" only if strict safeguards are met. Specifically, the company must demonstrate that the bioenergy feedstock did not cause significant land use change emissions (<5% of the sourcing area). You cannot clear a rainforest to plant bioenergy crops and then claim credit for capturing the smoke.
    

# 7. Removals Accounting

Removals (drawing carbon out of the atmosphere) are optional to report but are governed by strict regulations to ensuring they are real and permanent.

## Key Changes

- **Product Storage is NOT a Removal:** Carbon stored in short-lived products (e.g., paper, wood furniture, cotton) is **not considered a removal** in the main inventory. It is a separate, optional reporting category called "Product Carbon Storage." This reflects the reality that most products eventually decay or are burned, returning the carbon to the atmosphere.
    
- **Categorization:** Removals are strictly categorized to differentiate their durability:
    
    - **Land management CO2 removals:** Enhancing carbon in soils and biomass (reversible).
        
    - **Removals with geologic storage:** Technological solutions like DACCS or BECCS (highly permanent).
        
- **Allocation Cap:** To preventing double counting in complex supply chains, **Requirement 22** mandates that the sum of allocated removals from a specific region cannot exceed 100% of the actual removals physically occurring there.
    

## Scope 3 Traceability & Safeguards

The Standard offers a pragmatic approach to Scope 3 removals, acknowledging that full farm-level data is hard to get.

- **Interim Traceability:** Companies are permitted to trace to a **sourcing region** (rather than a specific farm) for claiming removals, but only _if_ they meet strict **"Sourcing Region Safeguards."**
    
- **Safeguards:** These include using conservative assumptions (so uncertainty doesn't lead to over-crediting) and demonstrating robust mechanisms to prevent double counting with other buyers in the same region. This allows companies to incentivize removals in their supply sheds even while working toward perfect traceability.