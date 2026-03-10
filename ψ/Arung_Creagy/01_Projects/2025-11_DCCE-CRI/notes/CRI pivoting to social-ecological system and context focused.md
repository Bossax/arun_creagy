---
status: evergreen
tags: []
created: 2026-02-02
last_updated:
AI_prompt: false
project:
  - DCCE_CRI
type:
  - note
---
# Background
Read the CRI_implementation_pland.md for the context
P Tik, the manager, stresses that he wants the CRI product to help local authority (at the municipality level) with decision making on improving their 'resilience'. He mentions that there is a gap between the data products develop by Thai researchers in the past projects. The information tells only relative ranks of the risk and historical disaster damage of the provinces. It is insufficient for the officials to understand areas that have room for improvement. 

Climate Risk Indices developed by TEI researchers [[Climate Risk Index (CRI) Pilot Methodology ]] is based on Germanwatch's methodology as part of DCCE's CRI pilot project. This index is essentially implying the impacts of climate-related disaster events. The metrics included in the index are aligned with the global DRR framework such as Sendai Framework. However, its suitability for sub-national analysis is still debatable as discussed in the [[Development of National Climate Risk Index]]. 

Meanwhile, the Risk Assessment sub division of DCCE has developed [[Spatial climate risk map DCCE v1]] and [[Evergreens/Spatial climate risk map DCCE v2|Spatial climate risk map DCCE v2]] based on IPCC's risk framework. [[Development of National Climate Risk Index]] is also another project running in parallel but led by a Mahidol University researcher. The later project produces a report that reviews available climate risk and resilience indices such as German watch , ND-GAIN, INFORM. It provides a useful analysis of the relevance and suitability of these indices to Thailand context.

In the past weeks, we have been discussing about the framing of CRI as in Climate Resilience or Readiness Index. The questions go back to the distinction between Resilience, Readiness, and Risk. Now I am coming to the conclusion of the literature review and thinking process and want to propose the way forward

This is the only first prompt in the series. I want you to suggest how you I set you up so that I can produce a comprehensive write up for documentation AND a detailed script for NotebookLM to create a presentation slide for my team mate to guide them on the creation of Powerpoint slide deck for the client  
# Framing CRI

There is a need to differentiate coping capacity and adaptive capacity: These two concepts are mixed up in several climate risk data products in the past. The unclear conceptualization led to unclear meaning of the resulted risk index. The risk index , a lot of time, include indicators/ metrics that represent exclusively short-term responses to disaster.

## My verdict 

Resilience should encompasses adaptive capacity (which already partially encompasses coping capacity) and transformative capacity. I reject the use of 'readiness' term in ND-GAIN indicator since it is not consistent with other literature (such as [[Sendai Framework Termonology on Disaster Risk Reduction]])

Now to make the data product or tool that we are developing relevant to 'decision-making' of local officials, especially municipality officials, we need to
1. accept the trade-off between comparability and context specificity
2. abandon asset-based indicators and indicative approach of making an index
3. focus more on process-based 
4. include a broader set of metrics beyond stock, assets, capital such as governance, information and agency
5. frame resilience from social-ecological system perspective
