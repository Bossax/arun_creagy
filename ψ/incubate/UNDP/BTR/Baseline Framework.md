---
type: task
status: In Progress
project:
start date:
due date:
color: var(--mk-color-teal)
---
# Essential

1. Definition of Baseline Framework
2. Scope of Baseline Framework
3. Approach to the development of baseline framework
4. Relation to [[Adaptation M&E Framework]]
5. Relation to [[Data Reference Sheet]]

<!--todo:  Draft the structure and guiding questions for developing the baseline framework-->

**Baseline framework** defines the baselines that are relevant to Climate Change Risk management

Also, defines types or categories of baselines to be monitored in the long-term

A baseline can be determined by a the result of calculation using a set of indicators 


# Theoretical Framework

## 1. Defining the Baseline

In the context of the National Adaptation Cycle and the Biennial Transparency Report (BTR), a **baseline** is not merely a static statistic from a past year. It is the **empirical reference state** against which future deviations—whether caused by climate stress or adaptation interventions—are measured.

Fundamentally, a baseline serves two distinct epistemological functions:

1. **Diagnostic Function (Stage 2 - IVRA):** It defines the "Problem Space." It answers: _What is the current level of risk assuming no new actions are taken?_
    
2. **Evaluative Function (Stage 5 - MEL):** It defines the "Counterfactual." It answers: _How much worse would the situation have been without the intervention?_
    

Unlike mitigation, where the baseline is a clear metric (tonnes of CO2 equivalent), adaptation baselines are multidimensional and dynamic. A system can improve its performance (e.g., higher crop yields) while simultaneously facing increased risk (e.g., more frequent droughts). Therefore, a single "Adaptation Baseline" is a fallacy; we must instead operate with a **Tripartite Baseline System**.

## 2. Categorization Basis: The "Cause-Subject-Effect" Triad

To resolve the confusion often found in operational manuals (such as mixing rainfall data with project performance), we categorize baselines based on their structural role in the risk equation ($Risk = Hazard \times Exposure \times Vulnerability$).

The categorization is based on three fundamental questions:

1. **The Context:** What is the physical reality we are adapting to?
    
2. **The Subject** Who or what is being exposed to this reality?
    
3. **The Result** What is the outcome of their interaction?
    

## 3. The Three Baseline Types

### Type 1: The Physical Baseline 

- **Definition:** The reference climatology and hazard frequency that characterizes the physical environment over a specific historical period (e.g., 1990–2020).
    
- **Role in Cycle:** Serves **Stage 1 (Science)** and **Stage 2 (IVRA)**. It provides the denominator for calculating anomalies.
    
- **Key Challenge: Non-Stationarity.**
    - _The Problem:_ In a changing climate, the "past" is no longer a reliable predictor of the "future." A baseline calculated on historical averages may underestimate current risk.
    - _Theoretical Implication:_ We cannot use this baseline to measure project performance (e.g., "did we reduce flood frequency?") because the project cannot control the weather. It must be treated strictly as **Contextual Data**.
        
- **How to Obtain:**
    - Historical meteorological observation data (Thai Meteorological Department).
    - Hydrological records (Royal Irrigation Department).
    - Disaster frequency statistics (Department of Disaster Prevention and Mitigation).
        

### Type 2: The Socio-Economic Baseline (Subject)

- **Definition:** The state of the human or ecological system—its assets, demographics, and inherent sensitivities—prior to specific adaptation interventions. This encompasses both **Exposure** (what is there) and **Vulnerability** (how fragile it is).
- **Role in Cycle:** Serves **Stage 2 (IVRA)** and **Stage 3 (Planning)**. It defines the target population.
- **Key Challenge: Attribution of Fragility.**
    
    - _The Problem:_ Is a community vulnerable because of climate change, or because of unrelated economic policies? Separating "Climate Vulnerability" from "Development Deficit" is difficult.
        
    - _Theoretical Implication:_ This baseline tracks the **Adaptive Capacity** (Stock). It measures _potential_ resilience (e.g., "number of doctors per capita") rather than _actual_ resilience.
        
- **How to Obtain:**
    - Census and demographic data (National Statistical Office).
    - Land use maps (Land Development Department).
    - Economic indicators (NESDC).
    - **Mapping from Track 1:** Using the "S-Series" and "A-Series" indicators from the CU/Agency monitoring reports (e.g., current poverty headcount, current reservoir capacity).
        

### Type 3: The Evaluative Baseline (Result)

- **Definition:** The historical trajectory of losses or system failures under "Business as Usual" conditions. This is the metric used to assess whether resilience has actually improved.
    
- **Role in Cycle:** Serves **Stage 5 (MEL)**. This is the core of the BTR's "Information on impacts, risks, and vulnerabilities" (MPGs Section D).
    
- **Key Challenge: The Counterfactual Gap.**
    - _The Problem:_ If a flood occurs and damage is low, was it because of the adaptation project, or because the flood was simply we
    - _Theoretical Implication:_ This requires the **Translation Matrix**. We cannot measure this directly through simple monitoring. We must infer it by correlating **Type 1 (Hazard)** data with **Type 2 (Asset)** data to see if the **Type 3 (Loss)** trend is breaking.
        
- **How to Obtain:**
    - **Historical Loss & Damage Data:** Analysis of databases like DesInventar to establish a "Loss per Hazard Intensity" curve.
    - **Activity Proxies:** Converting "Standard Output Indicators" (e.g., 500 ponds) into "Avoided Loss Estimates" using standard coefficients.
        

## 4. Operational Implications for the Research Team

To operationalize this theoretical framework, the research team must approach the data collection with these design principles:

1. **Decouple Climate from Performance:**
    
    - _Rule:_ Never use a Type 1 metric (e.g., "Reduction in drought days") as a Key Performance Indicator for a project. That is a logical fallacy.
        
    - _Action:_ In the Data Reference Sheet, tag all Type 1 variables as "Context" only.
        
2. **Use Proxies for Evaluative Baselines:**
    
    - _Rule:_ Since we cannot wait for a disaster to test resilience, we must use **Type 2 (Stock)** changes as a proxy for **Type 3 (Result)** improvement.
        
    - _Action:_ The "Translation Matrix" must explicitly state the assumption: _"An increase in Type 2 (e.g., +10% irrigation coverage) is assumed to correspond to a Type 3 improvement (e.g., -5% crop loss risk)."_
        
3. **Standardize the "Zero Year":**
    
    - _Rule:_ To ensure comparability across the BTR, a common reference year (e.g., 2024 or 2025) must be set for all Socio-Economic baselines, while Physical baselines should use the WMO standard period (e.g., 1991–2020).
        

## 5. Summary of Baseline Taxonomy

| Baseline Type      | Focus (The "What")           | Theoretical Function                | Source Data (Track 1 Input)                  |
| ------------------ | ---------------------------- | ----------------------------------- | -------------------------------------------- |
| **Physical**       | **Hazard**                   | Defines the **Stress Test** level.  | Meteorology, Hydrology, Disaster Stats       |
| **Socio-Economic** | **Vulnerability / Exposure** | Defines the **System State**.       | Census, "S-Series" & "A-Series" Indicators   |
| **Evaluative**     | **Impact / Resilience**      | Defines the **Efficacy** of action. | Historical L&D, "Translation Matrix" Outputs |