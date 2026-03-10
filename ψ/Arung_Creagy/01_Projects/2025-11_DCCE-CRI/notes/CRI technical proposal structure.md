---
type:
  - hypothesis
status: archived
version: 1
parent_hypothesis: "[[CRI_Project Context]]"
created: 2025-10-29
project:
  - DCCE_CRI
tags:
---

**status**
- seed - just jotted down
- testing - wait for gathering more data
- refined - intermediate status
- validated - wait for migration to `output`
- rejected - discard

# 1. Framing and approach
### Plan
This section lays out the foundational concepts of climate risk management and adaptation. 
- Explaining what is the objective of climate change adaptation
- risk concept of IPCC 
- Key concepts of risk management Readiness, Resilience, Risk, Impact
- Review of the spatial risk map as a risk diagnostic tool 
- review CRI version 1 as an impact diagnostic tool
- existing gaps of the risk map and CRI V1
- elaborate why measuring resilience and readiness is crucial to close the gaps
- Wrap up the approach for CRI phase2: the hybrid approach where we will improve impact indicator of phase 1 work (top-down approach) and develop resilience and readiness indices based on bottom up approach
- Summarize the methodological steps of this project
	1. ทบทวนผลการศึกษา CRI ระยะที่ 1 และพัฒนา CRI ในระยะที่ 2 ด้วยแนวทางเดิม
	2. Develop theory and methodology for resilience และ readiness indices
	3. implement the methodology to create resilience and readiness index
	4. engage with local officials of targeted municipalities to validate the assumptions and verify the actionability
	5. Iterate the analytics product and conclude the project
- Summary table of the matches between outputs of each step and project TOR

>[!Content material]
>Four pillars of risk management  
> 1. Readiness
> 2. Resilience
> 3. Risk
> 4. Impact
> 
> These 4 pillars of risk management frame the feedback loop that guides action in the long term
> 
> These 4 pillars are operating in the backdrop of "risk layering" concept as part of the comprehensive risk management. Other important concepts are
> 
> 5. risk = propensity toward adverse impact due to the interplay among hazard, exposure, vulnerability
> 6. residual risk = risk that is above the coping capacity. risk below the coping capacity is considered avoided
> 7. coping capacity = the level where risk below this level will not cause impact. determined by resilience
> 8. resilience = ability to prepare, absorb, respond, recover from a disaster. determined by sensitivity, adaptive capacity, exposure, and non risk elements such as enabling factors
> 9. soft limit to adaptation = upper bound of the solution space, constrained by immature enabling factors. Soft limits can be extended through transformative adaptation and advancing enabling environment
> 10. hard limit to adaptation is set by physical constraints
> 11. impact = realized risk which is closely related to residual risk. It could be view as realizations of the residual risk. 
> 12. readiness = ability to advance resilience
> 13. risk management = how to deal with the residual risk
> 14. risk reduction = decreasing residual risk by improving coping capacity (increasing resilience). prior to disaster events
> 15. risk avoidance = avoid activities that increase risk such as increasing exposure (this is highly relevant to exposure modification measure)
> 16. risk absorption = no further action of risk reduction is done or could be done and the residual risk is ok to be born by individual. Government compensation could be part of risk absorb
> 17. risk transfer = transfer part of the residual risk to other parties.
> 
> 
> The risk analytics data products are needed to assist the steps through out adaptation cycle
> Readiness index-> focus on process. Because readiness can be pre-determined. There is a largely fix set of desired characteristics of the enabling factors that are cross sectoral. 
> 
> High readiness index implies higher ability to implement activities that enhance resilience. Resilience can be viewed as the state of a system or as an outcome indicator. However, it could be added process elements. Resilience encompasses 'vulnerability' and 'exposure' components of  'risk'. 
> 
> Risk index extends from overing vulnerability and exposure to include hazard. Risk index is an indicative of adverse impact, but it does not translate directly to impacts due to uncertain nature of risk and risk components
> 
> Impact index can indicate the actual residual risk that cannot be avoided at this point. The impact that is captured is only economic impact
> 
> These 4 indices could be viewed as system diagnostics. Readiness allows for resilience building. Resilience builds up resistance against risk. Lower risk implies lower impact. Them=n everything is calibrated by the actual impact (realized risk)
> 
> Thus, the effective adaptation cycle needs these diagnostics to complete the support required by the adaptation cycle
> 
> 

## 3. กลุ่มงานที่ 1 Improve Climate Impact Index using Dasymetric mapping

## Plan

This section recaps CRI V1 and discuss the plan to improve data granularity of the spatial impact by introducing external datasets. Key activities are
1. set the objective of what should be seen in higher resolution? which parameters or variables
2. explore ancillary datasets and create selection criteria of the datasets
3. develop a dasymetric mapping technique to implement calculation logic
4. implement the technique on the CRI V1 database

>[! Content material] 
>### Objective of dasymetric mapping
> we want to know of each category of impacts
> 1. what could be disaggregated based on available ancillary datasets?
> 2. what do the dasymetric maps of the variables inform the local governments?
> 3. of all possible targeted variables, which one should be prioritized ?
> 
> If comes down to
> 1. The inventory of available external datasets
> 2. Compatibility with the aggregated Thailand's official statistics
> 3. Prioritized sectors that the impact has been historically high 
> 
> remarks:
> - Strategy for incorporating and retiring the ancillary datasets need to be considered in conjunction with the ongoing data system development effort of line agencies in Thailand. The developing line agencies should be consulted if known
>   
> ### Ancillary datasets
> The ancillary datasets that are to be used to disaggregate
> 
> things to considers: 
> 1. Can it help increasing granularity?
> 2. is the ancillary dataset being supported by the data provider? such as a research lab? when will the data product be expired? 
> 3. stability of the data product. has it undergone methodological changes too often? any major corrections in the development history
> 4. quality  and limitations of the methodology


## 3. Resilience and Readiness Methodology Development
## Plan
This section focuses on setting up the methodological approach to Resilience and Readiness Methodology  development. First, we want to have a well-defined definitions and objectives of resilience and readiness index. The objectives of readiness and resilience need to be agreed in this step. Possible options of the objectives and theory of change if resilience and readiness indices can be explained briefly here such as
- Resilience index could be made more action-oriented rather than state descriptor (vulnerability), using multi faceted capacity concept 
- Resilience index should be a diagnostic tool for planning rather than a ranking tool for central government agency to allow for local engagement.
- The elements of the indicators can be grouped by controllability of the municipalities so that
- Readiness index should represent the state of the enabling factors at the local levels. The enabling factors are governance, finance, and knowledge system according to IPCC. What indicators reflect these factors will need to be discussed in the project. 

This section also includes the analytical framework of interpreting and using the information about the four elements of risk management for policy making, adaptation planning (decision under deep uncertainty approach)
## 4. Implement the methodology
- explore datasets of indicators
	- open access
	- Other data reporting platforms such as Local Performance Assessment and
	- through stakeholder consultation
- curate datasets
- apply quality control to vet the datasets
- compute 
- get preliminary result

## 5. Piloting
- engage local authority
	- important to frame the engagement not to be audit from local official's point of view
- validate the assumptions of the methodology
	- what constitutes resilience and readiness in their perspective
	- Does our knowledge taxonomy align with their perception? (language and structure)
	- are these indicators and aspects really under their control?
	- Attribution and causality of local actions and the changes in the indices (readiness, resilience, risk, index)

- verify its policy and action relevance (action)
	-  what kind of data products they can relate to
	- how should the analytical results be presented to best lead to adoption?

