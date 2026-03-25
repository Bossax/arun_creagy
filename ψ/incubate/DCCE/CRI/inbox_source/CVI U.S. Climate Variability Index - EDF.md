---
type: literature
status: evergreen
tags:
  - CRI
source:
authors:
  - Environmental Defense Fund
year:
relevance_to: "[[]]"
key_findings: Climate Vulnerability Index of The U.S.. The methodology adopt the concept of Social Vulnerability Index at its core and augments it with additional climate resilience related factors. These factors are infrastructure, like coverage and access, environment, like inequality in access to natural resources and persisted exposure to threat. It also brings in health dataset from the center of disease control.
---

# Subject
Vulnerable groups in community

# Indicator selection
## Survey existing indicators
1. [Environmental Justice (EJ) -related screening tools at the national FEMA Risk Index](https://www.atsdr.cdc.gov/place-health/php/eji/?CDC_AAref_Val=https://www.atsdr.cdc.gov/placeandhealth/eji/index.html)
2. [Centers for Disease Control and Prevention (CDC)/ Agency for Toxic Substances and Disease Registry (ATSDR) Social Vulnerability Index (SVI)](https://www.atsdr.cdc.gov/place-health/php/svi/index.html)
3. [University of South Carolina's Hazards and Vulnerability Research Institute (HVRI)’s Baseline Resilience Indicators for Communities (HVRI BRIC)](https://artsandsciences.sc.edu/geog/hvri/bric)
4. https://www.sciencedirect.com/science/article/abs/pii/S0959378014001459
5. [U.S. Small-area Life Expectancy Estimates Project – USALEEP](https://www.cdc.gov/nchs/nvss/usaleep/usaleep.html)
6. state and regional levels
	1. state
		1. CalEnviroscreen
		2. MD-EJUST
		3. EPA
	2. regional
		1. HGBEnviroscreen 
7. Compiled indicators

## Selection methodology
1. Engage with EJ community-based leaders (subject) to select relevant indicators
	identify 
		- lived experience
		- long-standing inequality
		- built environment
		- transit
		- health conditions
		- needed structural investment 
2. Review the documents from EJ advisory
3. Gather feedback from experts who have experience developing similar tools
# Processing the indicators
## Themes
1. Baseline vulnerabilities: factors that may reduce resilience and potential sources of long-standing community inequity
	1. Health
		1. Centers for Disease Control (CDC) and Prevention Foundation
		2. many other sources
	2. Social and Economics
		1.  [Centers for Disease Control (CDC) has developed Social Vulnerability Index **SVI**](https://www.atsdr.cdc.gov/place-health/php/svi/index.html)
		2. augmented by additional indicators
	3. Infrastructure
		1. transport, energy, food, water, waste management, governance, access to physical digital, financial resources
		2. [Equitable and Resilient Infrastructure Investment](https://nap.nationalacademies.org/catalog/26633/equitable-and-resilient-infrastructure-investments?s=z1120)
			1. Consensus Study Reports on hazard mitigation and resilience
				1. partnerships for equitable infrastructure development
				2. systemic change toward resilient and equitable infrastructure investment
				3. innovations in finance and financial analysis.
	4. Environment
		1. long standing disparities in sources of
			1. exposure
			2. stressors
			3. pollution
		2. land use
		3. envi health factors
2. Climate Change Risk
	Impact areas
	1. Health
	2. Social and Economics
	3. Extreme Events

## Data evaluation
1. completeness
2. distribution
3. variability in observation
if they do not meet the criteria, they are excluded
## Data processing
- 200 datasets were evaluated
- individual indicators rather than composite indicators to avoid double counting
- publicly available and nationally consistent datasets are prioritized
- If census tract level data is unavailable or too uncertain, country/state-level data is utilized
### 1. From point-source datasets to raster
Kernel density smoothing. Convert point source such as pollution to distributive spatial data, with magnitude declining with the distance from the source.
The kernel density layer then gets averaged by census tract.
Consistent with the methods used for estimating proximity indicators in other tools.
### 2. Transportation indicators
there is some processing to convert transect data to pixels or spatially implicit data like statistics to census tract's attributes
## 3. Infrastructure usage
- congestion indicators
	- commute delay
- Walk score by RedFin
- Transit performance score
- Hospital access
## 4. Environmental impact
- Vehicle Mile Traveled varies with air pollution and infrastructure fragility

# Data integration
[Toxicological Prioritization Index (ToxPI)](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2089-2)
used to integrate data across domains and streams
- weighted average to aggregate data
- provide relative ranking
- radial pie chart visualization

# Analysis after creating the data product
## a. Spatial clustering
find patterns of areas with similar CVI score

## b. Clustering by CVI ToxPI profile
k-mean clustering to group similar #ToxPI profiles

## c. Map investment in vulnerability reductions onto the map
understand whether the resource is distributed according to the actual vulnerability


---

# Variable list


| **Category**                        | **Indicators**                                                                                                                                                                                                                                                                                                                                      |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Socioeconomic Status**            | • Below 150% Poverty<br>• Unemployed<br>• Housing Cost Burden<br>• No High School Diploma<br>• No Health Insurance                                                                                                                                                                                                                                  |
| **Household Characteristics**       | • Aged 65 & Older<br>• Aged 17 & Younger<br>• Civilian with a Disability<br>• Single-Parent Households<br>• English Language Proficiency                                                                                                                                                                                                            |
| **Racial & Ethnic Minority Status** | • Hispanic or Latino (of any race)<br>• Black or African American, Not Hispanic or Latino<br>• Asian, Not Hispanic or Latino<br>• American Indian or Alaska Native, Not Hispanic or Latino<br>• Native Hawaiian or Pacific Islander, Not Hispanic or Latino<br>• Two or More Races, Not Hispanic or Latino<br>• Other Races, Not Hispanic or Latino |
| **Housing Type & Transportation**   | • Multi-Unit Structures<br>• Mobile Homes<br>• Crowding<br>• No Vehicle<br>• Group Quarters                                                                                                                                                                                                                                                         |

Additional `Climate Resilience` Indicators
**Infrastructure**
- Total vehicle mile
- passenger vehicle miles
- truck vehicle miles
- heavy duty vehicle miles
- Ports
- Rail Crossing
- Traffic proximity and volume
- National Transportation Noise Map