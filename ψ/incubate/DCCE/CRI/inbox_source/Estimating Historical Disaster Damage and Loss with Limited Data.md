---
type:
  - Artifact
status: raw
tags:
  - Loss_and_Damage
  - Methodology
capture_date: 2025-10-30
origin_prompt:
relevance_to: "[["
AI_output: true
topics:
  - loss_and_damage
  - historical_estimation
phase_support:
  - CRI_Phase_1
evidence_type: ai_synthesis
use_case:
  - data_methods
  - loss_estimation_design
---

## Introduction

Thailand’s Department of Climate Change and Environment (DCCE) faces the challenge of estimating **30 years of climate-related disaster damages and losses** – including floods, droughts, tropical storms (wind damage), landslides, and heat-related mortality – with very limited historical data. The only available figures are government **post-disaster compensation payouts**, which were determined ad hoc and do not reflect actual total losses. Comprehensive **Post-Disaster Needs Assessment (PDNA)** tools were developed by the Department of Disaster Prevention and Mitigation (DDPM) five years ago, but they have yet to be operationalized in practice. This report explores methods to retroactively estimate historical disaster damage and loss under data-scarce conditions, compares these methods by accuracy and complexity, and recommends a best-fit approach for DCCE. The focus is on approaches applicable in Thailand’s context, including use of proxy indicators, modeling techniques, satellite remote sensing, and hybrid methods. Where relevant, examples of successful implementations in other countries are highlighted.

## Challenges with Limited Historical Data

Before outlining methods, it is important to recognize the limitations of the available data. Historical disaster impacts in Thailand have not been systematically recorded, especially for localized or “extensive” events. Relying only on recorded compensation or insured losses will vastly undercount true impacts – **in developing countries, often less than 10% of disaster losses are insured or compensated, with the vast majority of losses going unrecorded**[undrr.org](https://www.undrr.org/explainer/the-invisible-toll-of-disasters-2022#:~:text=%E2%80%9CAdding%20to%20the%20long,reversing%20global%20progress%20in%20a). Heatwave impacts are particularly under-reported, since official death certificates often fail to attribute deaths to heat. For example, during the 1995 Chicago heat wave, **465 heat-related deaths were officially recorded, but statistical analysis of total mortality found about 700 excess deaths – indicating many heat fatalities were not identified in official records**[epa.gov](https://www.epa.gov/climate-indicators/climate-change-indicators-heat-related-deaths#:~:text=Many%20factors%20can%20influence%20the,related%20deaths%20that%20result). These challenges necessitate alternative analytical approaches to estimate the “invisible” toll of disasters.

## Methods for Estimating Historical Damage and Loss

### Method 1: Proxy Data and Historical Disaster Inventory

One approach is to compile a **national historical disaster loss database** using proxy data and archives. This involves gathering information on past disasters from any available sources – such as government reports, newspaper archives, academic case studies, community records, and the existing compensation payout data – to infer the impacts on lives, property, and the economy. The **DesInventar methodology** (developed by UNDRR) is a well-known framework for systematically recording historical disaster losses in a homogeneous database format[desinventar.cimafoundation.org](https://desinventar.cimafoundation.org/what_is.html#:~:text=DesInventar%20Disaster%20Information%20Management%20System,of%20damage%2C%20losses%20and). Many countries have implemented DesInventar or similar systems to reconstruct 30–50 years of disaster data. **Sri Lanka**, for example, built a _DesInventar-based national disaster losses and damages database_ covering decades of events[undrr.org](https://www.undrr.org/building-risk-knowledge/disaster-data#:~:text=hotspot%2C%20vulnerability%20and%20risk%20analysis,existing%20vulnerabilities). **Nepal** and several Latin American countries have likewise populated national disaster inventories by mining local records back in time.

 

Using Thailand’s context, DCCE could coordinate with DDPM and provincial authorities to gather records of past floods, storms, etc., including the number of homes/buildings damaged, area of crops affected, infrastructure hits, casualties, and estimated economic losses when available. **Government compensation data** can be included as one proxy – though it underestimates actual loss, it provides a baseline that can be scaled up using expert judgment or known ratios. (Studies indicate that official aid/insurance often covers only a small fraction of actual damage[undrr.org](https://www.undrr.org/explainer/the-invisible-toll-of-disasters-2022#:~:text=%E2%80%9CAdding%20to%20the%20long,reversing%20global%20progress%20in%20a), so DCCE might, for instance, multiply compensation figures by a factor to approximate total loss, calibrating that factor based on any detailed assessments of major events.) In the absence of direct economic loss data, other proxies can be used: for example, **reports of crop yield loss or GDP dips in drought years** to estimate drought impact, or **excess mortality analysis** during extreme heat events (comparing total deaths during heatwaves to baseline levels) to estimate heat-related fatalities[epa.gov](https://www.epa.gov/climate-indicators/climate-change-indicators-heat-related-deaths#:~:text=Many%20factors%20can%20influence%20the,related%20deaths%20that%20result). This proxy-based inventory approach has **moderate complexity** – largely involving data collection and basic analysis – and can be implemented with limited technical tools. Its **accuracy depends on data completeness**: it can capture documented losses relatively well, but may miss undocumented damages (especially in remote areas or smaller events). Nonetheless, assembling such a database is a **critical first step**. It provides a foundation of evidence and can reveal patterns and trends (e.g. hotspots of recurring floods), even if some loss estimates are rough. UNDRR emphasizes that **even modest improvements in the coverage and consistency of loss data can greatly enhance risk understanding and modeling**[undrr.org](https://www.undrr.org/building-risk-knowledge/disaster-data#:~:text=vulnerabilities%20visible,existing). This method aligns well with Sendai Framework goals of systematically recording disaster losses and could leverage DDPM’s coordinating role to gather historical data from various agencies.

### Method 2: Satellite Imagery and Remote Sensing Analysis

In the absence of ground reports, **satellite and aerial remote sensing** can be a powerful tool to retrospectively assess disaster impacts. Over the past few decades, the increase in satellite coverage means many major events have some imagery available. **Remote sensing is a reliable method for determining the extent and severity of physical damage** across large areas. For example, synthetic-aperture radar (SAR) imagery (e.g. from Sentinel-1) can penetrate clouds and is routinely used to map flood inundation extent during and after floods[un-spider.org](https://un-spider.org/advisory-support/recommended-practices/recommended-practice-google-earth-engine-flood-mapping#:~:text=Flood%20Mapping%20and%20Damage%20Assessment,operate%20in%20any%20weather). By analyzing archived SAR and optical images on platforms like Google Earth Engine, one can delineate flood footprints for past events and measure how much area was flooded and for how long. These flood extent maps, combined with land use data and property maps, allow estimation of assets and crops exposed to each flood (and applying depth-damage functions if flood depth can be inferred). Similarly, remote sensing can detect **wind/storm damage**: severe storms and tropical cyclones often leave visible scars – for instance, uprooted or defoliated vegetation and roof damage. Studies have shown that **tornado and hurricane damage tracks cause changes in land surface that are clearly observable via satellite imagery**[pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC7263478/#:~:text=Severe%20weather%20events%20including%20tornadoes%2C,in%20remote%20areas%20where%20staffing). High-resolution images (or change detection techniques using radar interferometry) can reveal areas of building destruction and fallen trees after a cyclone, which can be correlated with damage on the ground. For **droughts**, satellites indirectly capture impacts through vegetation health indices. **Normalized Difference Vegetation Index (NDVI)** and related indicators (VCI – Vegetation Condition Index, etc.) from MODIS or Landsat can show how crop and vegetation growth deviated from normal during known drought years[sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S2214581824000375#:~:text=,VHI%29%2C%20which%20assess). Large drops in NDVI sustained over a season can serve as a proxy for agricultural loss area and yield reduction due to drought. **Landslides** can also be mapped via remote sensing: optical imagery time-series can reveal new landslide scars on hillsides, and DEM (Digital Elevation Model) data can be used to estimate volume of landslide material. Initiatives like NASA’s global landslide catalog combine satellite detection with news reports to identify landslide events.

 

Remote sensing **offers an objective, consistent way to assess past events**, especially for physical damage. It is particularly useful for Thailand’s frequent floods and storms, where ground surveys might have been sparse. The **accuracy** of satellite-based assessments for physical damage is **fairly high for large, visible impacts** – for instance, flood inundation maps from SAR are highly reliable[un-spider.org](https://un-spider.org/advisory-support/recommended-practices/recommended-practice-google-earth-engine-flood-mapping#:~:text=Flood%20Mapping%20and%20Damage%20Assessment,operate%20in%20any%20weather), and building damage can be reasonably estimated with before/after imagery in many cases. However, this approach may **underestimate losses that are not directly visible from space**. It captures **direct damages** (e.g. area flooded, structures destroyed), but **economic losses** (like business interruption, or health impacts like heat mortality) need additional modeling. Converting satellite-detected damage into monetary loss requires assigning values (e.g. using exposure datasets: building inventories, land value, or agricultural prices). For drought, NDVI reductions would need to be translated into crop losses using yield models. Thus, while remote sensing provides a **rich hazard and impact dataset**, some modeling or assumptions are needed to get to dollar figures or casualty estimates. In terms of **complexity**, this approach is **moderate**: it demands GIS and remote-sensing expertise and computing resources, but many tools are openly available, and international agencies (like UN-SPIDER or Copernicus EMS) provide methodologies that can be adopted. Overall, satellite analysis is a **feasible method in Thailand**, given the increasing national capacity in GIS; it could be used to retrospectively map major floods (e.g. the 2011 flood) and storms to quantify their impacts beyond what official records show.

### Method 3: **Modeling and Simulation (Catastrophe Risk Modeling)**

Another approach is to use **analytical modeling techniques to simulate disaster impacts**, essentially filling in gaps with scientific estimates. Probabilistic **catastrophe risk models** are widely used in the insurance sector and by institutions like the World Bank to estimate losses for events, even with limited historical loss data. The idea is to combine three components: **hazard models** (frequency and intensity of events), **exposure data** (assets, population, economic values at risk), and **vulnerability functions** (how much damage occurs to a given asset for a given hazard intensity). In practice, building such a model for Thailand would involve gathering hazard information for the past 30 years – e.g. flood hazard maps or streamflow records, cyclone wind speed footprints for storms that affected Thailand, drought indices, landslide susceptibility maps, and temperature records for heatwaves. Each hazard event can then be analyzed: for example, a flood model (using hydrological simulation or flood depth maps) can estimate water depths in affected provinces for a given event year, and then a vulnerability curve can estimate the percentage of damage to buildings and crops at those depths. Summing across assets yields an economic loss estimate for that event. Repeating for all major events over 30 years produces a modeled loss time series. This can also be done in a **probabilistic way**, simulating thousands of possible events based on climate statistics to estimate average annual loss and the range of extremes, though in this case we want to hindcast actual historical impacts.

 

A noteworthy example is the World Bank’s **Global Rapid Post-Disaster Damage Estimation (GRADE)** approach, which is essentially a modeling-based method applied immediately after disasters. GRADE analyses use pre-existing risk models combined with any available data to estimate losses within days. Over 2015–2024, GRADE was applied in 66 disasters worldwide and was found to be **highly accurate – within about 10-12% of the official PDNA results on average**[blogs.worldbank.org](https://blogs.worldbank.org/en/opendata/-data-in-action--a-decade-of-remote--rapid-damage-assessments#:~:text=When%20compared%20with%2017%20events,%E2%80%9D). This demonstrates that a modeling approach can approximate ground-truth losses well. The GRADE framework is a **hybrid risk modeling method**: it uses simulated hazard intensity maps, overlays **census and socioeconomic data** on exposure, applies vulnerability functions, and integrates any available **historical data or satellite observations** to calibrate the estimates[blogs.worldbank.org](https://blogs.worldbank.org/en/opendata/-data-in-action--a-decade-of-remote--rapid-damage-assessments#:~:text=The%20framework%20uses%20a%20combination,rapidly%20make%20critical%20recovery%20decisions). Essentially, it is a desk-based reconstruction of damage. Another example is the **Pacific Catastrophe Risk Assessment and Financing Initiative (PCRAFI)**, which built detailed risk models for Pacific Island countries that had little historical loss data. PCRAFI compiled historic cyclone tracks and earthquake data, constructed an exposure database of buildings and infrastructure across islands, and used simulation models to estimate what losses each country could expect from events of various severities[openknowledge.worldbank.org](https://openknowledge.worldbank.org/bitstreams/3c942c5b-af94-537f-b93e-8945a172339c/download#:~:text=,and%20historical%20loss). The result was a baseline risk profile (average losses per year and probable maximum losses) that governments could use for planning and insurance, even though historical records were sparse.

 

For Thailand, a modeling approach could leverage existing data (e.g. flood hazard maps from the Hydro and Agro Informatics Institute, climate data from Thai Meteorological Department, national building inventories or economic data from the census). It could also incorporate **global datasets** (such as global flood models or wind models) if local data is lacking. The **accuracy** of this approach can be **high for well-modeled hazard events**, as seen with GRADE’s ~90% alignment with detailed assessments[blogs.worldbank.org](https://blogs.worldbank.org/en/opendata/-data-in-action--a-decade-of-remote--rapid-damage-assessments#:~:text=When%20compared%20with%2017%20events,%E2%80%9D). It is particularly useful to estimate **losses for larger events or to extrapolate where data is missing**, ensuring that even undocumented impacts are modeled. However, the accuracy depends on the quality of input data – poor exposure data or unknown vulnerability patterns (e.g. how do Thai traditional homes fare in floods) can introduce uncertainty. Also, indirect losses (economic ripple effects) are usually not captured unless a more complex economic model is added. In terms of **complexity**, full catastrophe modeling is the **most complex approach** listed: it requires multi-disciplinary expertise (hazard science, engineering, GIS, economics) and substantial data gathering and computing. Building a custom national risk model is time- and resource-intensive. Simplified approaches, like focusing on a single hazard at a time or using regional models, can reduce complexity. Tools like the **UNISDR/UNDP Basic Risk Assessment guidelines** or open-source models (e.g. CAPRA) could provide a starting template. Given DCCE’s current capacity, this method might need external technical support (from universities, international agencies, or the DDPM if they have a modeling unit). Over time, however, developing such a model would greatly enhance Thailand’s ability to analyze disaster risk under climate change scenarios as well, not just historical losses.

### Method 4: **Hybrid and Multi-Source Approaches**

No single method may perfectly compensate for limited data, so a **hybrid approach** that combines elements of the above can be very effective. In fact, the most robust analyses often integrate **multiple data sources and techniques** to cross-validate and enrich the estimates. This can be tailored to the Thai context by taking advantage of whatever information is available for each event or hazard type. For example, DCCE could adopt a workflow where for each major disaster in the past 30 years, they **triangulate** the losses from: (a) any **recorded data** (government reports, compensation amounts, EM-DAT entries, etc.), (b) **remote sensing outputs** (flood extent maps, damage proxies from satellites), and (c) **modeled estimates** (using hazard intensity and exposure for that event). Each source provides a piece of the puzzle – the recorded data gives a minimum confirmed impact, the satellite analysis shows the spatial extent and severity, and the model fills in the blanks (such as estimating economic value of what the satellite observed, or adding sectors not visible from space). By combining these, analysts can come up with an **informed estimate of damage and loss for each event**, with uncertainty bounds.

 

An example of a hybrid approach in action is again the **World Bank’s GRADE methodology**, which explicitly merges risk modeling with satellite imagery and on-ground information[blogs.worldbank.org](https://blogs.worldbank.org/en/opendata/-data-in-action--a-decade-of-remote--rapid-damage-assessments#:~:text=The%20framework%20uses%20a%20combination,rapidly%20make%20critical%20recovery%20decisions). Another example is how the **Philippines Red Cross** developed an impact-based forecasting system: they trained a machine learning model on _historical hazard data and impact data from 60 past typhoons_ (a data hybridization exercise) to predict impacts of future storms[undrr.org](https://www.undrr.org/building-risk-knowledge/disaster-data#:~:text=Case%20study%3A%20Impact,to%20typhoons%20in%20the%20Philippines)[undrr.org](https://www.undrr.org/building-risk-knowledge/disaster-data#:~:text=time%20of%20120%20to%2072,on%20over%2060%20historical%20events). While that is forward-looking, it illustrates how multi-source historical data (in their case, combining weather data with recorded impacts) can be used to estimate losses. In building Thailand’s historical loss estimates, a hybrid approach could also mean **starting simple and iteratively improving**: for instance, use the proxy database (Method 1) as a base, then layer in remote sensing results for the largest events to adjust those figures, and perhaps use a mini-model to estimate aspects like heat mortality or indirect losses that neither proxies nor satellites directly capture. The **accuracy** of a hybrid approach is potentially **the highest**, because it leverages the strengths of each method and compensates for individual weaknesses. As evidence, GRADE’s hybrid technique achieved about 88–90% agreement with full field assessments[blogs.worldbank.org](https://blogs.worldbank.org/en/opendata/-data-in-action--a-decade-of-remote--rapid-damage-assessments#:~:text=When%20compared%20with%2017%20events,%E2%80%9D), outperforming what any single-source estimate would likely achieve. However, **complexity is also high**: a hybrid approach requires managing diverse data inputs and analytical methods. It may demand coordination across agencies (e.g. meteorological, GIS, finance ministries for economic data) and strong data management. That said, the approach can be **modular** – DCCE can start with a basic combination (say, proxies + a bit of remote sensing) and later incorporate more modeling sophistication, ideally with support from DDPM’s resources and other partners. In summary, a hybrid approach is essentially the _“all of the above”_ strategy: it strives for the best accuracy but will require higher technical capacity and inter-agency collaboration.

## Comparison of Methods by Accuracy and Complexity

The table below ranks the above methods in terms of **accuracy** (ability to realistically estimate historical damage/loss) and **complexity** (data and skill requirements). The ranking is relative, with 1 = highest/best (for accuracy) and 1 = least complex (for ease).

 

**Table 1. Accuracy Ranking of Methods (1 = Most Accurate)**

| Rank (Accuracy) | Method                                                  | Notes on Accuracy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **1**           | Hybrid Multi-Source Approach                            | Leverages multiple sources; ~90% alignment with true losses in examples[blogs.worldbank.org](https://blogs.worldbank.org/en/opendata/-data-in-action--a-decade-of-remote--rapid-damage-assessments#:~:text=When%20compared%20with%2017%20events,%E2%80%9D). Most comprehensive, reduces omissions.                                                                                                                                                                                                                                                     |
| **2**           | Modeling/Simulation (Catastrophe Risk Model)            | Can closely approximate actual losses if model is well-calibrated; good for large events and scenario consistency. May miss nuances without data.                                                                                                                                                                                                                                                                                                                                                                                                      |
| **3**           | Satellite Remote Sensing Analysis                       | High accuracy for visible physical damage (flood extent, destroyed structures)[un-spider.org](https://un-spider.org/advisory-support/recommended-practices/recommended-practice-google-earth-engine-flood-mapping#:~:text=Flood%20Mapping%20and%20Damage%20Assessment,operate%20in%20any%20weather)[pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC7263478/#:~:text=Severe%20weather%20events%20including%20tornadoes%2C,in%20remote%20areas%20where%20staffing), but needs conversion to losses and may not capture indirect effects. |
| **4**           | Proxy Data/Disaster Inventory                           | Captures documented impacts; accuracy depends on completeness of historical records. Tends to undercount small/unreported losses but provides ground-truth for recorded events.                                                                                                                                                                                                                                                                                                                                                                        |
| **5**           | Compensation Data Extrapolation _(simple proxy subset)_ | Very rough approximation; official payouts significantly undervalue actual losses (often <10% in developing contexts[undrr.org](https://www.undrr.org/explainer/the-invisible-toll-of-disasters-2022#:~:text=%E2%80%9CAdding%20to%20the%20long,reversing%20global%20progress%20in%20a)). Useful as baseline but low standalone accuracy.                                                                                                                                                                                                               |


**Table 2. Complexity Ranking of Methods (1 = Least Complex)**

|Rank (Complexity)|Method|Notes on Complexity|
|---|---|---|
|**1**|Proxy Data/Disaster Inventory|Relatively straightforward data gathering and cataloguing, but labor-intensive. Requires coordination and archival research more than advanced analysis.|
|**2**|Compensation Data Extrapolation _(simple proxy)_|Easiest technically (basic arithmetic on existing data), but oversimplified. Included here as a quick-start subset of proxy methods.|
|**3**|Satellite Remote Sensing Analysis|Moderate complexity: needs GIS/remote sensing skills and computing tools. Many open-source tools and methods available; analysis can be done event by event.|
|**4**|Hybrid Multi-Source Approach|High complexity: must integrate multiple datasets/techniques. Involves multidisciplinary team (GIS experts, modelers, statisticians) and robust data management. Can be phased, but full implementation is complex.|
|**5**|Modeling/Simulation (Catastrophe Risk Model)|Very data- and skill-intensive. Requires hazard modeling, exposure data development, and engineering expertise. Typically a major project to develop and calibrate a national risk model.|

_(Note: The above complexity ranking treats the simple use of compensation data as a subset of the proxy data method, but listed separately to highlight its ease. In practice, it would be combined with Method 1 or 4 for better accuracy.)_

## Recommendation and Implementation Path

**Recommended Initial Method:** DCCE should begin with a **Proxy Data/Inventory approach (Method 1)**, augmented with selective **Remote Sensing analysis**, as the best-fit initial method. This approach strikes a balance between feasibility and improving accuracy. Given DCCE’s current technical capacity, starting by building a **==historical disaster loss database==** is achievable and lays a critical foundation. Concretely, DCCE can initiate a project (in collaboration with DDPM) to compile all available disaster impact information from the last 30 years into a structured database. The existing compensation records can serve as a spine for this database – for each recorded disaster, they provide a date, location, and a baseline loss figure (the payouts). Around this spine, DCCE can add additional layers: reports from DDPM’s provincial offices, old disaster reports from line ministries (e.g. Agriculture for drought impacts, Health for heatwave mortality), and media archives for events that might not have official reports. This process will immediately highlight data gaps, which is where a bit of ==**satellite analysis**== can be plugged in. For instance, if the records show a flood in 2005 in Chiang Mai with meager details, DCCE could task a GIS officer to retrieve satellite images for that period and map the flood extent, thereby estimating how many villages or how much cropland was inundated (to infer damages). This hybridization at a small scale will improve the database’s fidelity without overwhelming complexity.
 

Importantly, this recommended approach is **incremental and capacity-building**. It produces a tangible result – a historical loss dataset – relatively quickly, which DCCE can use for preliminary analysis and reporting (e.g. showing trends of disaster losses increasing or which provinces suffered most). At the same time, the process of building it will develop skills and data infrastructure that pave the way for more advanced methods. The UNDRR advises that **systematic loss data collection, even if imperfect, is invaluable for understanding risk trends and informing models**[undrr.org](https://www.undrr.org/building-risk-knowledge/disaster-data#:~:text=patterns%20and%20trends%20that%20can,global%20risk%20models%20have%20limitations). Thailand would benefit from this foundational step, as it currently lacks an institutionalized loss database.

 

**Involvement of DDPM:** DDPM, as the national disaster management agency, should be a key partner in this effort. In the short term, DDPM can provide access to any raw data they have (they may have incident reports, even if PDNA was not done) and help coordinate information gathering from local authorities. DDPM’s experience with the PDNA framework (though not operationalized, the _tools_ exist) is also an asset – their PDNA forms define what data should be collected post-disaster. DCCE can use those definitions to guide the data compilation (ensuring the historical database captures categories like housing damage, infrastructure, agriculture, etc., consistent with PDNA structure). This will make the eventual transition to PDNA easier.

 

**Future Improvements:** Once the initial historical loss database is in place and DCCE has strengthened its team (perhaps by training staff in GIS or basic risk analysis), the **next step** could be to gradually incorporate **Method 4 (Hybrid)** on a broader scale. For example, DCCE could pilot a full **GRADE-style analysis** for one past disaster (maybe the 2011 great flood, which had abundant data). This pilot, possibly done with support from the World Bank or academic experts, would combine modeling with satellite data and compare the result to the known assessments for that event[blogs.worldbank.org](https://blogs.worldbank.org/en/opendata/-data-in-action--a-decade-of-remote--rapid-damage-assessments#:~:text=When%20compared%20with%2017%20events,%E2%80%9D). Lessons from this pilot can inform how to do rapid modeling for other events. As capacity grows, DCCE can move up the complexity ladder – developing in-house modeling capability (Method 3) for key hazards. In doing so, DCCE might leverage regional initiatives (like ASEAN risk assessment programs or UNDP’s support) to get technical assistance.

 

**Why not jump straight to full modeling?** While probabilistic modeling is powerful, it is recommended that DCCE first accumulate reliable historical impact data and experience. This will not only yield immediate usable results (for reporting Thailand’s past losses, including for international frameworks) but also provide the calibration data needed to make any future model credible. Moreover, collecting local loss data fosters institutional awareness and political buy-in for disaster risk reduction (it makes the risk “visible” to officials, as UNDRR notes)[undrr.org](https://www.undrr.org/explainer/the-invisible-toll-of-disasters-2022#:~:text=Poorer%20countries%20almost%20always%20have,of%20lives%20lost%20and%20disrupted)[undrr.org](https://www.undrr.org/explainer/the-invisible-toll-of-disasters-2022#:~:text=%E2%80%9CAdding%20to%20the%20long,reversing%20global%20progress%20in%20a). Given that PDNA has been identified as a goal but remains unused, starting simpler will build the confidence and demand for fully institutionalizing PDNA.

 

In summary, **DCCE’s best initial course** is to adopt a **proxy-data-driven methodology, enhanced with modern tools (like remote sensing)**, to estimate historical losses. This method is relatively low in complexity but can significantly improve upon raw compensation figures. It sets up a baseline database that DCCE and DDPM can keep updating. With this groundwork laid, Thailand can then progress toward more sophisticated hybrid or modeling approaches – possibly even developing its own rapid loss estimation mechanism akin to GRADE, and fully operationalizing PDNA for future events. By involving DDPM from the outset in data collection and later in analysis, DCCE ensures that the method is sustainable and that DDPM’s mandate in disaster data coordination is utilized. This collaborative, phased approach will yield the most accurate estimates feasible now, and steadily enhance accuracy over time as more data and better models become available.

Citations

[

The invisible toll of disasters in 2022 | UNDRR

https://www.undrr.org/explainer/the-invisible-toll-of-disasters-2022

](https://www.undrr.org/explainer/the-invisible-toll-of-disasters-2022#:~:text=%E2%80%9CAdding%20to%20the%20long,reversing%20global%20progress%20in%20a)[

![](https://www.google.com/s2/favicons?domain=https://www.epa.gov&sz=32)

Climate Change Indicators: Heat-Related Deaths | US EPA

https://www.epa.gov/climate-indicators/climate-change-indicators-heat-related-deaths

](https://www.epa.gov/climate-indicators/climate-change-indicators-heat-related-deaths#:~:text=Many%20factors%20can%20influence%20the,related%20deaths%20that%20result)[

DesInventar Disaster Information Management System

https://desinventar.cimafoundation.org/what_is.html

](https://desinventar.cimafoundation.org/what_is.html#:~:text=DesInventar%20Disaster%20Information%20Management%20System,of%20damage%2C%20losses%20and)[

Disaster losses and damages data | UNDRR

https://www.undrr.org/building-risk-knowledge/disaster-data

](https://www.undrr.org/building-risk-knowledge/disaster-data#:~:text=hotspot%2C%20vulnerability%20and%20risk%20analysis,existing%20vulnerabilities)[

Disaster losses and damages data | UNDRR

https://www.undrr.org/building-risk-knowledge/disaster-data

](https://www.undrr.org/building-risk-knowledge/disaster-data#:~:text=vulnerabilities%20visible,existing)[

![](https://www.google.com/s2/favicons?domain=https://un-spider.org&sz=32)

Flood Mapping and Damage Assessment Using Sentinel-1 SAR ...

https://un-spider.org/advisory-support/recommended-practices/recommended-practice-google-earth-engine-flood-mapping

](https://un-spider.org/advisory-support/recommended-practices/recommended-practice-google-earth-engine-flood-mapping#:~:text=Flood%20Mapping%20and%20Damage%20Assessment,operate%20in%20any%20weather)[

Incorporation and Use of Earth Remote Sensing Imagery within the NOAA/NWS Damage Assessment Toolkit - PMC

https://pmc.ncbi.nlm.nih.gov/articles/PMC7263478/

](https://pmc.ncbi.nlm.nih.gov/articles/PMC7263478/#:~:text=Severe%20weather%20events%20including%20tornadoes%2C,in%20remote%20areas%20where%20staffing)[

![](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com&sz=32)

Drought analysis using normalized difference vegetation index and ...

https://www.sciencedirect.com/science/article/pii/S2214581824000375

](https://www.sciencedirect.com/science/article/pii/S2214581824000375#:~:text=,VHI%29%2C%20which%20assess)[

Data in action: a decade of remote, rapid damage assessments

https://blogs.worldbank.org/en/opendata/-data-in-action--a-decade-of-remote--rapid-damage-assessments

](https://blogs.worldbank.org/en/opendata/-data-in-action--a-decade-of-remote--rapid-damage-assessments#:~:text=When%20compared%20with%2017%20events,%E2%80%9D)[

Data in action: a decade of remote, rapid damage assessments

https://blogs.worldbank.org/en/opendata/-data-in-action--a-decade-of-remote--rapid-damage-assessments

](https://blogs.worldbank.org/en/opendata/-data-in-action--a-decade-of-remote--rapid-damage-assessments#:~:text=The%20framework%20uses%20a%20combination,rapidly%20make%20critical%20recovery%20decisions)[

![](https://www.google.com/s2/favicons?domain=https://openknowledge.worldbank.org&sz=32)

(PCRAFI) Better Risk Information for Smarter Investments

https://openknowledge.worldbank.org/bitstreams/3c942c5b-af94-537f-b93e-8945a172339c/download

](https://openknowledge.worldbank.org/bitstreams/3c942c5b-af94-537f-b93e-8945a172339c/download#:~:text=,and%20historical%20loss)[

Disaster losses and damages data | UNDRR

https://www.undrr.org/building-risk-knowledge/disaster-data

](https://www.undrr.org/building-risk-knowledge/disaster-data#:~:text=Case%20study%3A%20Impact,to%20typhoons%20in%20the%20Philippines)[

Disaster losses and damages data | UNDRR

https://www.undrr.org/building-risk-knowledge/disaster-data

](https://www.undrr.org/building-risk-knowledge/disaster-data#:~:text=time%20of%20120%20to%2072,on%20over%2060%20historical%20events)[

Disaster losses and damages data | UNDRR

https://www.undrr.org/building-risk-knowledge/disaster-data

](https://www.undrr.org/building-risk-knowledge/disaster-data#:~:text=patterns%20and%20trends%20that%20can,global%20risk%20models%20have%20limitations)[

The invisible toll of disasters in 2022 | UNDRR

https://www.undrr.org/explainer/the-invisible-toll-of-disasters-2022

](https://www.undrr.org/explainer/the-invisible-toll-of-disasters-2022#:~:text=Poorer%20countries%20almost%20always%20have,of%20lives%20lost%20and%20disrupted)
