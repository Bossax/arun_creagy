---
type:
  - idea
status: archived
tags:
  - CRI
  - Adaptation
  - DCCE
capture_date: 2025-10-27
origin_prompt:
relevance_to: "[["
---

# Context analysis

DCCE has been developing data and information products to help the country understand climate risk in granular levels. The flagship data product is the spatial climate risk map. The development of this product is led by Dr. Jeerasorn from RU CORE research group at Ramkhamhaeng university. The first version was published in 2022 and the second version was just finalized and will be released by 2025. This product is an index-based climate risk map that rank composite risk scores of the provinces in Thailand. The risk scores consist of climatic and non-climatic indicators. The climatic indicators are extreme climate indices resulted from downscaling climate models as part of the SEA-CORDEX project. The climate indices encompasses flood, heat, and drought hazards. No hazard modeling is done under this project; the climatic indicators assume correlations between the hazards and climate indices such as 1 day rainfall or number of days that max temperature exceed 35 degree Celsius for example. The second version of the product improves the *non-climatic* indicators by enriching the indicators attributed to hazard risk and sectoral impacts. The non-climatic indicators are further grouped into *exposure*, *sensitivity*, and *adaptive capacity*. Stakeholder consultations were conducted to solicit expert's  opinion on which indicators should be included in the non-climatic indicators groups to reflect sectoral-relevant entities, transmission pathways, and vulnerability.  For example, the natural resource management sector is concerned about habitat loss, forest area, so they include habitat area and forest land covers indicators into the exposure indicators that are exposed to every hazard. For each hazard, the sensitivity and adaptive capacity indicators are proposed to reflect the interplay among these factors in a particular transmission pathway. 

Although comprehensive, the spatial climate risk map still holds several limitations
1. aggregating multiple heterogeneous datasets (e.g., census data, line agency records) to the **provincial level** inevitably smooths out local variations. This results in **spatial averaging**, where pockets of high risk (hotspots) are diluted by safer areas within the same province. This is an example of the **Modifiable Areal Unit Problem (MAUP)** — a known issue in spatial analysis where results depend on the size and shape of spatial units. When risk data (e.g., rainfall anomaly, poverty index) are resampled and averaged to provincial polygons, it creates _artifacts_ that may mislead interpretation.
2. Since the risk scores are **normalized** across datasets from different agencies (using min–max scaling between 0–1), the relative ranking depends heavily on:
	- Which indicators are available at the provincial level,
	- Their spatial resolutions
	This creates an **apples-to-oranges problem**: socio-economic data often reflect people’s administrative boundaries, while climate and environmental data represent continuous spatial processes.
3. **Limited interpretability for decision-making**: At the provincial scale, the map is best used for **broad prioritization or communication**, not for **operational planning**. It answers _“Which provinces might deserve attention?”_ but not _“Which districts or sectors need intervention?”_

To complement the spatial risk map, there are several design principles that need to be decided at the start of the project, as well as building the foundational understanding of climate resilience.  

