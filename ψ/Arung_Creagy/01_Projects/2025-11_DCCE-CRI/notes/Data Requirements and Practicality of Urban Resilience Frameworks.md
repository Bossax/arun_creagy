---
status: current
tags: []
created: 2026-02-27
last_updated: 2026-02-27
AI_prompt: false
AI_output: true
project: DCCE-CRI
type: artifact
---
### (a) Extraction: Data Requirements and Practicality of Urban Resilience Frameworks

**1. Good Urban Governance for Climate Change Adaptation**

- **Chronological Context:** 2009. Reacts to the realization that poor urban populations are frequently ignored in adaptation planning, drawing on Mehta's 1998 governance framework to evaluate urban capabilities (Tanner et al., 2009).
- **Evidence of real city application:** “The case studies were undertaken by research partners in the ten cities selected for investigation... rapid governance and capacity assessment of 10 South and Southeast Asian cities (Bangkok, Chennai, Chittagong, Cochin, Dalian, Da Nang, Hangzhou, Ho Chi Minh City, Ningbo and Surat)” (Tanner et al., 2009).
- **Dimensions/Pillars:** “(1) decentralisation and autonomy, (2) accountability and transparency, (3) responsiveness and flexibility, (4) participation and inclusion and (5) experience and support” (Tanner et al., 2009).
- **Indicator types:** Qualitative expert judgment and rapid governance diagnostics (Tanner et al., 2009).
- **Data sources:** Balanced "primary and secondary data with cross-referencing and review" obtained through local researchers (Tanner et al., 2009).
- **Level of spatial granularity:** Municipal and sub-municipal (Tanner et al., 2009).
- **Frequency:** One-off rapid assessments conducted within "less than a month" (Tanner et al., 2009).
- **Data availability challenges:** Severe bias and validation issues. The short timeframe meant consultants "tended to focus on the positive aspects of municipal governance rather than illustrating examples of poor urban governance... to show the Rockefeller Foundation their city is an excellent choice," and assessments "have not been independently reviewed" (Tanner et al., 2009).
- **Implication for downstream analysis:** This highlights that purely qualitative, consultant-led frameworks require strict independent validation mechanisms to overcome political and financial reporting biases when curating governance dimensions.

**2. Strategy& Urban Resilience Assessment Framework**

- **Chronological Context:** Post-2020. Developed in reaction to the COVID-19 pandemic and the tripling of natural disasters in the MENA region since the 1980s (Strategy&, n.d.).
- **Evidence of real city application:** “We applied this framework to assess the urban resilience of nine MENA cities and 11 comparators from around the world. In the MENA region we applied our urban resilience framework to Abu Dhabi, Amman, Cairo, Casablanca, Dubai, Jeddah, Kuwait City, Muscat, and Riyadh.” (Strategy&, n.d.).
- **Dimensions/Pillars:** Vulnerabilities are assessed across "basic needs, society, economy, and the urban environment" and capacities to "Respond, Recover, and Transform" (Strategy&, n.d.).
- **Indicator types:** Quantitative composite index based on "131 key performance indicators (KPIs)" normalized using a minimum/maximum approach, paired with a "detailed qualitative checklist" (Strategy&, n.d.).
- **Data sources:** "publicly available information" including databases from the "World Bank, World Development Indicators... Global Health Security Index... Gallup... national statistics" (Strategy&, n.d.).
- **Level of spatial granularity:** City level, but frequently utilizes country-level proxies for indicators like the "Global peace index" or "Homicide rates and share of prison population" (Strategy&, n.d.).
- **Frequency:** Benchmarking snapshot utilizing historical trends (e.g., measuring "Change in temperature compared to average in the last 30 years") (Strategy&, n.d.).
- **Data availability challenges:** The reliance on national databases for city-level assessments suggests a lack of hyper-local data for specific urban vulnerabilities, necessitating proxy aggregations (Strategy&, n.d.).
- **Implication for downstream analysis:** Utilizing this framework's data structure demands identifying where national-level data accurately reflects city-level realities and where it obscures localized urban inequalities.

**3. European Resilience Management Guidelines (ERMG) / RESOLUTE (CRAMSS)**

- **Chronological Context:** 2022. Reacts against the "prevalence of management practices based on centralised control and prescriptive procedural approaches that do not take into account high variability and unpredictability" in urban infrastructure (Bellini et al., 2022).
- **Evidence of real city application:** “The operationalization is taking take place in the two pilot sites and urban transport systems, namely the City of Florence and Athens Metro” (Bellini et al., 2022).
- **Dimensions/Pillars:** Operationalizing the phases of "preparation, monitoring, reaction, adaptation, learning, and anticipation" for the Urban Transport System (UTS) (Bellini et al., 2022).
- **Indicator types:** Big Data analytics, semantic reasoning, predictive modeling, and real-time flows (Bellini et al., 2022).
- **Data sources:** "User Generated Data", "Open Data", "environmental and other kind of sensors (e.g., traffic flows, hydrometers, air pollution, underpasses water level, people flow, temperature)", "social networks", and "opportunistic sensors" like taxi GPS systems (Bellini et al., 2022).
- **Level of spatial granularity:** Highly granular, including exact GPS positioning, individual user trajectories, and "origin destination matrices at different time slots" (Bellini et al., 2022).
- **Frequency:** Continuous, asynchronous, and real-time data streaming (Bellini et al., 2022).
- **Data availability challenges:** Practitioners face severe challenges integrating "Heterogeneous data sources... with different data delivery rate (ranging from real-time to static), quality, reliability and semantics" alongside strict European data protection and privacy laws (Bellini et al., 2022).
- **Implication for downstream analysis:** Curating technology-heavy frameworks requires an explicit assessment of a city's legal and infrastructural capacity to securely host, clean, and analyze high-velocity big data.

**4. Climate Resilience Index (ESI)**

- **Chronological Context:** 2024. Builds upon and refines previous metrics from the City Resilience Index (Arup/Rockefeller) and the Urban Resilience Index (Notre Dame) (ESI, 2024).
- **Evidence of real city application:** “A pilot study of nine U.S. cities put the index into effect with an aim for evaluation of additional cities in the future.” (ESI, 2024).
- **Dimensions/Pillars:** "four major measurable cornerstone categories are: environmental, economic, infrastructural, and social" (ESI, 2024).
- **Indicator types:** Standardized quantitative sub-indicators comparing city performance to the "national average/average of major MSAs as a reference point" (ESI, 2024).
- **Data sources:** "primary and secondary data from various sources, including federal, county, and city-level agencies, bureaus, institutions, and financial reports" as well as NGO data (ESI, 2024).
- **Level of spatial granularity:** City level (ESI, 2024).
- **Frequency:** Point-in-time comparative analysis for standardizing benchmarks (ESI, 2024).
- **Data availability challenges:** To prevent skewed results, raw data availability challenges required methodological adjustments, specifically that "Metrics measuring cumulative values, such as total emissions for a city, were standardized using city population to reduce bias against cities with larger populations" (ESI, 2024).
- **Implication for downstream analysis:** Normalization techniques (like per capita adjustments) must be standardized in our data requirements to allow valid cross-city comparisons when building the evolution timeline.

**5. Global Cities Resilience Index (GCRI)**

- **Chronological Context:** 2025. Created in reaction to the limitation that "==Most current resilient city indices assess where cities stand today rather than their capacity to navigate tomorrow’s uncertainties==," moving away from static ESG outcomes to forward-looking readiness (Kearney, 2025).
- **Evidence of real city application:** “Our analysis of 31 cities for the first edition of the GCRI—across Global North and Global South economies—provides insights into the foundations that enable urban resilience” (Kearney, 2025).
- **Dimensions/Pillars:** "institutional governance; sustainable finance and business; technology and innovation; social and human capital; and global integration" (Kearney, 2025).
- **Indicator types:** Exclusively "quantifiable, verifiable data from established sources rather than survey responses, expert opinions... or subjective evaluations" encompassing binary policy assessments and quantitative ratios (Kearney, 2025).
- **Data sources:** "internationally trusted sources" such as CDP reporting, World Bank Group, UN E-Government Survey, and the Global Entrepreneurship Monitor (Kearney, 2025).
- **Level of spatial granularity:** "City-level data prioritization... When city-level data is unavailable, carefully selected country-level proxies are employed" (Kearney, 2025).
- **Frequency:** Dynamic and continuous; the framework explicitly "avoids creating fixed rankings that will become outdated" and is designed to be "regularly updated to track development over time" (Kearney, 2025).
- **Data availability challenges:** Acknowledges gaps in data quality by mathematically weighting indicator scores based on "Data richness" (the "comprehensiveness and reliability of available measurement data") (Kearney, 2025).
- **Implication for downstream analysis:** Integrating a "data richness" weighting is a vital methodological requirement for our framework curation, ensuring cities in data-poor regions are not unfairly penalized.

**6. ICARIA Holistic Resilience Assessment Framework (RAF)**

- **Chronological Context:** 2026. Revises and upgrades the prior RESCCUE framework to expand focus onto regional areas, compound climate events, and nature-based solutions (Brito et al., 2026).
- **Evidence of real city application:** “Overall results of a Spanish metropolitan area (AMB) and an exploratory application to an Austrian rural case (SLR) are also presented” (Brito et al., 2026).
- **Dimensions/Pillars:** "organizational, spatial, functional, and physical" (Brito et al., 2026).
- **Indicator types:** Objective-driven performance indicators evaluated against reference values translating into development levels: "incipient, progressing, or advanced" (Brito et al., 2026).
- **Data sources:** Synthesized from "models, plans, monitoring activities, risk assessment, or city incident records, from various platforms and documents" gathered during stakeholder working sessions (Brito et al., 2026).
- **Level of spatial granularity:** Regional, city, municipal, and critical infrastructure scale (Brito et al., 2026).
- **Frequency:** Scenario-based and ongoing to "monitor the progress of resilience over time" (Brito et al., 2026).
- **Data availability challenges:** Severe issues noted with data fragmentation because "knowledge is highly dispersed, requiring the involvement of many stakeholders and good coordination at a regional level"; additionally, for natural areas, "many metrics remained unanswered... because several stakeholders manage different types of natural areas" (Brito et al., 2026).
- **Implication for downstream analysis:** Framework practicality at the regional scale relies heavily on political coordination and institutional alignment, dictating that data gathering protocols must account for inter-jurisdictional silos.

### (b) Synthesis

**1. Data Requirements and Practicality in Applied Urban Resilience Frameworks**

The literature reveals a distinct evolution in the data requirements and practical methodologies of applied urban resilience frameworks over the last two decades.

- **Indicator Types and Sources:** Early frameworks (e.g., Good Urban Governance, 2009) relied heavily on qualitative expert judgment, primary surveys, and rapid diagnostics. This posed severe practicality issues due to subjectivity and reporting bias. Modern frameworks have aggressively shifted toward purely quantifiable, verifiable data. Indices like the ESI (2024), GCRI (2025), and Strategy& (n.d.) draw almost exclusively from established international and national databases (World Bank, CDP, UN, Gallup) to ensure comparability. The most advanced technical frameworks, such as RESOLUTE (2022), rely on automated Big Data, ingesting remote sensing, IoT, and real-time social network sentiment rather than administrative reports.
- **Spatial Granularity:** A persistent challenge across all major frameworks is achieving true city-level or neighborhood-level granularity. While tools like RESOLUTE achieve hyper-local tracking (GPS-level origin-destination matrices), comprehensive global indices (GCRI, Strategy&) frequently have to substitute national-level proxies for city-level realities when assessing macroeconomic or social indicators. The ICARIA framework (2026) pushes the boundary outward, requiring data that covers regional and metropolitan ecosystems, which complicates data gathering across municipal boundaries.
- **Frequency of Collection:** There is a consensus shift from static, one-off assessments toward dynamic monitoring. Early scorecards provided point-in-time benchmarks, but modern frameworks (GCRI, ICARIA, RESOLUTE) are explicitly designed for ongoing, real-time, or continuous evaluation, reflecting the understanding that resilience is a dynamic process rather than a static achievement.
- **Data Availability Challenges:** The practicality of these frameworks is fundamentally constrained by data availability. The recurring challenges reported across case studies include:
    1. _Data Silos:_ Knowledge is highly fragmented across different municipal departments and regional stakeholders (ICARIA).
    2. _Bias and Standardization:_ Raw data requires extensive normalization (e.g., per capita adjustments) to prevent bias against large cities (ESI), and qualitative data is highly prone to political bias (Good Urban Governance).
    3. _Data Poverty:_ To combat missing data, cutting-edge frameworks (GCRI) are now mathematically weighting their indicators based on "data richness" so that structural uncertainties in data collection are factored into the final resilience score.




---
###  Summary of Data Requirements and Practicality in Applied Frameworks

|Framework (Year)|Indicator Types|Data Sources|Spatial Granularity|Frequency|Reported Data Challenges|
|:--|:--|:--|:--|:--|:--|
|**Good Urban Governance** (2009)|Qualitative rapid diagnostics & expert judgment.|Balanced primary and secondary data gathered by local researchers.|Municipal and sub-municipal.|One-off rapid assessments.|Positive reporting bias by consultants; lack of independent review.|
|**Strategy& Assessment** (n.d., ~2021)|Quantitative composite index & qualitative institutional checklist.|Public databases (e.g., World Bank, Gallup, national statistics).|City level (with national proxies).|Snapshot based on historical averages.|Need to rely on national proxies when city-level data is unavailable.|
|**RESOLUTE / ERMG** (2022)|Big data, semantic reasoning, predictive modeling.|IoT sensors, open data, social networks, GPS systems.|Highly granular (GPS level, transport matrices).|Continuous, real-time data streaming.|Integrating heterogeneous data sources at varying delivery rates.|
|**ESI Climate Resilience** (2024)|Standardized quantitative sub-indicators.|Primary/secondary data from federal, county, and city agencies.|City level.|Point-in-time benchmarking.|Raw data biases require careful normalization (e.g., per capita).|
|**GCRI** (2025)|Quantifiable, verifiable data (binary & ratios).|Internationally trusted sources (CDP, UN, World Bank).|City-level prioritized (country proxies if needed).|Dynamic/continuous updating.|Variable data richness across cities requires statistical weighting.|
|**ICARIA RAF** (2026)|Objective-driven performance indicators.|Risk models, municipal plans, incident records.|Regional, city, and critical infrastructure scale.|Scenario-based and ongoing monitoring.|Extreme data fragmentation across diverse regional stakeholders.|

- **Implication for downstream analysis:** Structuring this data table provides a direct rubric for evaluating whether a newly proposed city resilience project possesses the technical and administrative maturity required to support specific framework methodologies.


###  Consistently Appearing Dimensions

- _Strategy& (n.d.)_: Dimensions are structured to eliminate vulnerabilities across “basic needs, society, economy, and the urban environment”.
- _ESI Climate Resilience Index (2024)_: Focuses on four identical foundational pillars: “four major measurable cornerstone categories are: environmental, economic, infrastructural, and social”.
- _Global Cities Resilience Index (Kearney, 2025)_: Expands on these core areas with a forward-looking twist: “institutional governance; sustainable finance and business; technology and innovation; social and human capital; and global integration”.
- _ICARIA Holistic Resilience Assessment (Brito et al., 2026)_: Groups variables into “organizational, spatial, functional, and physical” dimensions.
- **Implication for downstream analysis:** The universal convergence around four macro-categories (Physical/Infrastructure, Social, Economic, and Organizational/Governance) provides a standardized taxonomy for curating and cross-walking indicators from disparate assessment tools.


### Weighting and Emphasizing Governance

- _Early Governance Primacy (2009)_: Frameworks like Tanner et al. focused entirely on the political capacity to deliver resilience, defining dimensions exclusively as “(1) decentralisation and autonomy, (2) accountability and transparency, (3) responsiveness and flexibility, (4) participation and inclusion and (5) experience and support”.
- _Empirical Moderation Weighting (Valdivieso et al., 2021)_: Empirical regression analysis of 345 Chilean municipalities proved that “municipal organizational robustness—operational rules, planning, managerial flexibility and integration, and accountability—is the most quantitatively outstanding moderating factor” determining actual infrastructure investment.
- _Explicit Over-weighting (WHO UGHW, ~2023)_: In specialized frameworks merging health and resilience, governance is mathematically prioritized: “To highlight the primary importance of urban governance, cities’ achievements in governance will be assessed with double the weightage compared to other indicators”.
- _Standard Weighting (2024-2025)_: In global composite tools like the GCRI and ESI, governance is treated as an equally weighted sub-pillar (e.g., ESI weights infrastructure and economy at "20 percent weighting in the final score" alongside policy response).
- **Implication for downstream analysis:** When building mathematical indices or dashboards, developers must consciously decide whether governance is an equal pillar to infrastructure or an overarching "multiplier" (moderating variable) that fundamentally dictates the success of all other dimensions.


### Capacity-Based Frameworks (Coping, Adaptive, Transformative)

- _Agent Capacities (Tyler & Moench, 2012)_: Early SES models focused on the human element, measuring “Agent capacities... Responsiveness... Resourcefulness... Capacity to learn” to adapt to climate stress.
- _Resilience Engineering Cycle (Bellini et al., 2022)_: The RESOLUTE framework measures a "sustained adaptability cycle" mapping to the abilities to “Anticipate, Respond, Monitor, Learn” to continuous performance variability in critical infrastructure.
- _Institutional Action Capacities (Strategy&, n.d.)_: Strategy& organizes its entire matrix around three time-horizon capacities: “CAPACITY TO RESPOND... CAPACITY TO RECOVER... CAPACITY TO TRANSFORM: The ability to advance economically, socially, and technologically with new systems, structures, and reconfigurations through innovation”.
- _Holistic Capabilities (Brito et al., 2026)_: The ICARIA tool explicitly structures its critical infrastructure assessment around “resilience capabilities (withstand–recover–adapt–anticipate–prepare)”.
- **Implication for downstream analysis:** Identifying frameworks rooted in "capacities" rather than "static states" is critical for assessing cities facing high uncertainty, as these tools measure the _ability to change_ rather than just the structural strength to resist.


### **(b) Synthesis: Narrative Responses**

**1. In practice, which dimensions consistently appear across frameworks?** Despite variations in terminology over the last two decades, a clear consensus has emerged in practice: nearly all comprehensive frameworks evaluate urban resilience through a four-pillar model. These consistent dimensions are the **Physical/Environmental** (infrastructure, basic needs, ecosystems, spatial planning), the **Social** (human capital, social justice, community cohesion), the **Economic** (sustainable finance, business environments, livelihoods), and the **Organizational/Governance** (institutional mechanisms, strategy, leadership). While advanced indices like the 2025 GCRI add specialized modern dimensions like "technology" and "global integration", these invariably nest within or expand upon the foundational physical, economic, and social pillars.

**2. To what extent do frameworks weight or emphasize governance relative to other dimensions?** The emphasis on governance has shifted from a qualitative prerequisite to an empirically weighted multiplier. Early frameworks (e.g., Tanner et al., 2009) focused almost exclusively on governance variables, arguing that physical adaptation is impossible without decentralization and political inclusion. In modern global benchmarking indices (ESI, GCRI), governance is typically normalized as an equally weighted pillar alongside infrastructure and the economy. However, in deeply localized or scientifically modeled studies, governance is heavily emphasized as the ultimate _driver_ of resilience. For example, the WHO explicitly applies "double the weightage" to governance achievements compared to other indicators, and Valdivieso et al. (2021) mathematically proved that municipal organization acts as the primary "moderating factor" that dictates whether raw financial capacities actually translate into real-world adaptation investments.

**3. Which frameworks are conceptually closest to a capacity‑based view?** Several frameworks explicitly abandon static "checklists of assets" in favor of measuring dynamic operational capacities (coping, adaptive, and transformative).

1. The **Strategy& Urban Resilience Assessment Framework** is the most explicit structural example, directly organizing its metrics into institutional capacities to _"Respond"_ (cope/protect), _"Recover"_ (adapt/mitigate), and _"Transform"_ (advance/innovate).
2. The **ICARIA Resilience Assessment Tool (RAT)** similarly focuses critical infrastructure evaluations around continuous "resilience capabilities (withstand–recover–adapt–anticipate–prepare)".
3. In the high-tech/engineering domain, the **RESOLUTE ERMG** framework utilizes a "sustained adaptability cycle" measuring the continuous capacities to anticipate, respond, monitor, and learn.
4. From a sociological perspective, the **Urban Climate Resilience Framework (Tyler & Moench, 2012)** takes a capacity-based view of humans, assessing "Agent capacities" like resourcefulness and responsiveness to foster social-ecological learning.