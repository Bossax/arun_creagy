---
type: source_note
status: evergreen
creation_date: 2025-08-01
tags:
  - Risk_assessment
  - Index-based
project:
  - DCCE_CRI
ai_generated: false
---

The main objective of the CRI is to support national authorities in 
1. designing adaptation policies and plans
2. guiding the initial problem formulation phase (identification of key threats, issues and vulnerabilities)
3. screening and prioritization of areas (regions or provinces) with a higher propensity to be adversely affected by climate extremes.

>[!quote] [[PROVIA Guidance on Assessing Vulnerability, Impacts and Adaptation to Climate Change]]
>“we employ an indicator-based assessment, usually applied to provide early insights and rapid screening” (Mysiak et al., 2018, p. 3)

# Data processing
1. Hazard, exposure and sensitivity are first combined in the assessment of potential impacts at 1 × 1 km grid resolution
2. Normalize and calculate composite potential impact index
3. aggregate the composite index to the provincial level
4. subsequently combined with the AC to estimate the final risk index. 

The AC in our framework denotes the **cumulative resources available to respond to or lessen the impact of climate change** and is **estimated at a provincial level.** 

## Hazard
climate extreme indices (CEI) from climate models RCP 4.5 and 8.5 (EURO-CORDEX) 
The CEI are considered as **proxies** of the relevant hazards associated with climate extremes such us drought, heat and cold waves, floods, flash floods, landslides, soil erosion and water scarcity

### processing
calculate z-score
## Exposure and sensitivity
Many satellite high-level datasets
- Natural capital data is obtained from national departments
- Manufactured and built-environment exposure data are derived from land cover and further classified by Eurostat into high-density clusters (HDC), urban clusters (UC) and rural settlements
- Demographic data is from statistical census and transformed to 1x1 km using dasymetric mapping.
- Gridded Value Added is derived from subnational economic accounts and derived analysis for the Labour Market Areas

### processing
1. Transformed into 1x1 km grid
2. normalized (transformed into [0,1] range) by using linear (max-min) or nonlinear (sigmoid, S-shaped) functions. The nonlinear normalization was used for demographic indicators.

# Dasymetric mapping
This paper applies dasymetric mapping algorithms  to visualize a geographic field by refining a choropleth map with ancillary information about the distribution of the variable.

“Demographic indicators are derived from the latest statistical census (in 2011), transformed onto a 1 × 1 km grid by using a combination of high resolution land use and soil impervious data” (Mysiak et al., 2018, p. 6) pixelate census data using ancillary high resolution spatially explicit data

[[Dasymetric mapping]]

# exposure and hazard
overlaid and multiplied
then normalized the outputs again

# aggregation
simple weighted addition (SAW) for each RCM separately, and the ordered weighted average (OWA)
weighting method encompasses a certain degree of subjectivity

# adaptive capacity indicator
For ACI, we used the analysis described in depth in [69].It combines a set of 10 indicators related to available economic resources (such as provincial GDP, at-risk-of-poverty rate and unemployment), infrastructure, knowledge and technology (e.g. Internet access, educational level and patent applications), and institutional quality (based on the institutional quality index as in

---
# Citation

## Tag: adaptive capacity

“AC [31] denotes ‘the ability of systems, institutions, humans and other organisms to adjust to potential damage, to take advantage of opportunities, or to respond to consequences” (Mysiak et al., 2018, p. 3) IPCC Synthesis report 2014

“For ACI, we used the analysis described in depth in [69]. It combines ==a set of 10 indicators== related to available economic resources” (Mysiak et al., 2018, p. 7)

## Tag: CRI

“. The key components of the climate risk index (CRI) in this paper are hazard (H), i.e. the potential occurrence of a damaging physical event related to climate trends or climate extremes; exposure (E), i.e. the presence of environmental, social or economic elements in places that could be adversely affected; and vulnerability (V)” (Mysiak et al., 2018, p. 2)

## Tag: Exposure

“The ==main sources of data== used for MC and NC indicators included COPERNICUS Earth Observation System, the European Soil Data Centre (ESDAC), the European Environmental Agency (EEA), the Organization for Economic Co-operation and Development (OECD) and other open datasets.” (Mysiak et al., 2018, p. 5) high-level , non-national statistic data

“The indicators used for SC and EC, instead, rely on our previous work. All exposure and sensitivity indicators are represented as a regular square grid with a spatial resolution of 1 × 1 km.” (Mysiak et al., 2018, p. 5) dasymetric data

“Social and economic exposure data are based on high-resolution gridded demographic and gross added value (GVA) by macroeconomic sectors. The former include PD and the Total AgeDependency rate (TDR)” (Mysiak et al., 2018, p. 6)

“Exposure layers were first transformed to a 1 × 1 km grid and successively normalized (transformed into [0,1] range) by using linear (max-min) or nonlinear (sigmoid, S-shaped) functions. The nonlinear normalization was used for demographic indicators” (Mysiak et al., 2018, p. 7)

## Tag: hazard

“For the assessment of climate change-related hazards, we employ a wide array of climate extreme indices (CEI; table 1) developed by the Expert Team on Sector-specific Climate Indices (ET-SCI)” (Mysiak et al., 2018, p. 5)

“The anomalies of the extreme climate indices were standardized by using z-scores” (Mysiak et al., 2018, p. 7)

## Tag: index based

“. The key components of the climate risk index (CRI) in this paper are hazard (H), i.e. the potential occurrence of a damaging physical event related to climate trends or climate extremes; exposure (E), i.e. the presence of environmental, social or economic elements in places that could be adversely affected; and vulnerability (V)” (Mysiak et al., 2018, p. 2)

“we employ an indicator-based assessment, usually applied to provide early insights and rapid screening” (Mysiak et al., 2018, p. 3)

“The main objective of the CRI is to support national authorities in designing adaptation policies and plans, guiding the initial problem formulation phase (identification of key threats, issues and vulnerabilities), as well as a quick screening and prioritization of areas (regions or provinces) with a higher propensity to be adversely affected by climate extremes” (Mysiak et al., 2018, p. 3)

“For the assessment of climate change-related hazards, we employ a wide array of climate extreme indices (CEI; table 1) developed by the Expert Team on Sector-specific Climate Indices (ET-SCI)” (Mysiak et al., 2018, p. 5)

“The main sources of data used for MC and NC indicators included COPERNICUS Earth Observation System, the European Soil Data Centre (ESDAC), the European Environmental Agency (EEA), the Organization for Economic Co-operation and Development (OECD) and other open datasets.” (Mysiak et al., 2018, p. 5) high-level , non-national statistic data

“The indicators used for SC and EC, instead, rely on our previous work. All exposure and sensitivity indicators are represented as a regular square grid with a spatial resolution of 1 × 1 km.” (Mysiak et al., 2018, p. 5) dasymetric data

“Social and economic exposure data are based on high-resolution gridded demographic and gross added value (GVA) by macroeconomic sectors. The former include PD and the Total AgeDependency rate (TDR)” (Mysiak et al., 2018, p. 6)

“For ACI, we used the analysis described in depth in [69]. It combines a set of 10 indicators related to available economic resources” (Mysiak et al., 2018, p. 7)

## Tag: normalization

“Exposure layers were first transformed to a 1 × 1 km grid and successively normalized (transformed into [0,1] range) by using linear (max-min) or nonlinear (sigmoid, S-shaped) functions. The nonlinear normalization was used for demographic indicators” (Mysiak et al., 2018, p. 7)

“The anomalies of the extreme climate indices were standardized by using z-scores” (Mysiak et al., 2018, p. 7)
