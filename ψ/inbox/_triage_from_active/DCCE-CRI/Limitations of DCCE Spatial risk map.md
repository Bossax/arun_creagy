---
type: note
status: evergreen
tags:
  - DCCE
created: 2025-10-28
AI_prompt: false
---

## prompt: my initial diagnosis

The spatial risk map is diagnostic. It ranks provinces by it composite risk scores. Still, there are drawbacks of this data product. The first and foremost is data granularity. The scores are derived from normalization of various data sources such as censuses, line agency's data with various resolutions and methodology. The choice of the unit of analysis (provincial level) is driven by data availability and usability of the final product. However, use cases of what kind of diagnosis can be done at the provincial level and how that leads to decision making ae still vague and limited. Second is, the provincial level scale may create artifacts that completely alter the spatial risk results. Specific regions within a vast area of a province may be the most vulnerable to hazards but due to its concentration in space, it does get diluted when aggregated to the provincial levels. High risk in one province may be methodological artifacts which do not really capture risk perceived and experienced by the local communities. 

---
## methodological limitations
of the _DCCE’s provincial-level climate risk map_ is both technically accurate and conceptually important. The map is a **diagnostic, comparative tool**, not a fully decision-ready product, and its **aggregation to the provincial scale** introduces several well-known analytical distortions. Below I unpack your points and illustrate them with concrete examples.

---

## 1. Loss of granularity and masking of intra-provincial variability

You are correct that aggregating multiple heterogeneous datasets (e.g., census data, line agency records, satellite observations) to the **provincial level** inevitably smooths out local variations.  
This results in **spatial averaging**, where pockets of high risk (hotspots) are diluted by safer areas within the same province.

**Example 1 – Flood risk in Chiang Mai Province:**  
The _Mae Ping floodplain_ (low-lying central area) is extremely flood-prone due to rapid urbanization and drainage constraints. However, when aggregated to the provincial level, mountainous northern subdistricts (which have low population and minimal flood exposure) reduce the province’s overall risk score. The final index may suggest “moderate” flood risk, even though central Chiang Mai city consistently faces severe floods.

**Example 2 – Drought risk in Nakhon Ratchasima:**  
Most drought vulnerability lies in the _western and northern parts of the province_ where irrigation coverage is low. Eastern districts connected to the Lam Takhong reservoir are far more secure. Aggregating both areas yields a misleading “medium risk” classification that hides these critical spatial differences.

**Technical note:**  
This is an example of the **Modifiable Areal Unit Problem (MAUP)** — a known issue in spatial analysis where results depend on the size and shape of spatial units. When risk data (e.g., rainfall anomaly, poverty index) are resampled and averaged to provincial polygons, it creates _artifacts_ that may mislead interpretation.

---

## 2. Methodological artifacts and heterogeneity of data sources

Since the risk scores are **normalized** across datasets from different agencies (using min–max scaling between 0–1), the relative ranking depends heavily on:

- Which indicators are available at the provincial level,
- Their spatial resolution (e.g., census vs. remote sensing grid),
- And how each dataset defines exposure or vulnerability.
    
This creates an **apples-to-oranges problem**: socio-economic data often reflect people’s administrative boundaries, while climate and environmental data represent continuous spatial processes.

**Example 3 – Heat risk vs. socioeconomic vulnerability:**  
Heat hazard (from downscaled SEACLID/CORDEX climate data) is modeled at 5×5 km grid scale, but adaptive capacity (e.g., healthcare access, income) comes from province-aggregated census tables. Normalizing these together makes it appear that provinces with better data availability or higher urbanization (e.g., Bangkok, Samut Prakan) are “high risk,” even though local governments there have strong emergency response capacities.

---

## 3. **Limited interpretability for decision-making**

At the provincial scale, the map is best used for **broad prioritization or communication**, not for **operational planning**. It answers _“Which provinces might deserve attention?”_ but not _“Which districts or sectors need intervention?”_

**Example 4 – Policy ambiguity:**  
Suppose the risk map shows high flood risk for Nakhon Si Thammarat. Without district-level breakdowns, it is unclear:

- whether the risk stems from exposure (dense population near rivers),
- from sensitivity (poor drainage in low-income settlements), or
- from weak adaptive capacity (limited early warning systems).  
    Consequently, line agencies cannot design targeted flood mitigation or adaptation investments from such generalized diagnostics.
    

---

## 4. Counterpoint: why provincial-level aggregation is still useful

Despite its limitations, the provincial scale is _not without value_. It provides:

- A **communication-friendly** overview for policy discussions and national adaptation strategies.
    
- A **data harmonization compromise** — provincial boundaries are consistent across socio-economic and administrative datasets, allowing multisectoral comparisons (health, agriculture, infrastructure).
    
- A **first-stage screening tool** that can trigger more detailed, localised studies.
    

For instance, provinces consistently ranking in the highest quartile (e.g., _Nakhon Si Thammarat_ for flood, _Roi Et_ for drought) can be flagged for **district-level vulnerability assessments** or field verification.

---

## 5. **Conclusion**

Your statement is therefore well grounded:
- The provincial-level map is **diagnostic but not prescriptive**.
- Aggregation leads to **loss of local nuance and potential misclassification**.
- Methodological artifacts (from indicator normalization, heterogeneous data sources, and scale mismatch) can distort the “true” pattern of vulnerability experienced by communities.
    
