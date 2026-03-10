---
type:
  - strategy
status:
  - archived
tags:
version: 1
parent_hypothesis: "[[ ]]"
created: 2025-10-29
project:
  - UNDP_BTR
---

# Phase 1 - Policy context and M&E need

In this task, we will propose an adaptation M&E framework for national and sectoral levels. The framework will consist of key processes and tools. The definitions and objectives of the processes and tools will be established to shape the structure of the adaptation M&E system. Then, we will explore, and curate existing mechanisms and processes embedded in the national budgeting cycle, strategic planning cycle, line ministry and provincial performance evaluation cycles, and NDC tracking. Through desk review and interviews with the stakeholders mapped out under Task 1, we will identify where adaptation M&E can be integrated with existing processes to minimize burden and maximize institutional fit. We will capture stakeholder perspectives on challenges encountered in adaptation M&E—both for internationally funded projects and nationally budgeted initiatives—to ground the framework in practicality. Process mapping will clarify current data collection, aggregation, verification, and reporting pathways in all relevant administrative and governance cycles. The result will highlight assets that the adaptation M&E system can reuse, and reveal the gaps need to be filled to operationalize the adaptation M&E system.

# Phase 2 - Development of the M&E framework
Using the information gathered in phase 1, Creagy will employ process mapping techniques to visualize how data currently flows from project level to national reports, and where there are gaps or inefficiencies. This will highlight what new processes or institutions need to be introduced for a comprehensive adaptation M&E system.
Based on this analysis, in this task, Creagy will begin the development of the adaptation M&E content with the conceptual baseline framework for adaptation M&E. The main references of the baseline framework development are document and reports of Result-Based Management published by climate funds, such as the Green Climate Fund, and development agencies, such as UNDP, GIZ, and World Bank. This framework will guide the establishment of a baseline for tracking adaptation implementation and its impact. Additionally, we will ensure the framework accounts for gender and social inclusion (e.g., indicators that track outcomes for vulnerable groups) as emphasized in the TOR.

Next, based on the desk review, we will compile a long list of spatially explicit indicators spanning risks, impacts, vulnerabilities (exposure, sensitivity, adaptive capacity), and adaptation actions relevant to sector-level monitoring and evaluation. The indicators will be tagged to categorize them based on types, such as monitoring indicators, evaluation indicators, output indicators, outcome indicators, and impact indicators.

From this long list, we will create prioritization criteria (e.g. SMART: Specific, Measurable, Achievable, Relevant, Time-bound) to shortlist the indicators, based on data availability and sectoral relevance. We will use the criteria to create a prioritized set of indicators with clear definitions, calculation methodologies, and units. From the short list, we will assess potential data sources for indicator baseline value computation. Based on data availability and sectoral relevance, we will select a few indicators from the short list to apply the baseline framework to calculate the baseline values.


# Phase 3 - Demonstration and refinement
From the computed baseline values, we will design an M&E product — the Data Reference Sheet —and illustrate its intended application workflow through a case example. We then combine all outputs in this task up to this point to create a prototype of the indicator toolbox, which will consist of

- Long list of M&E indicators with tags
- Prioritization criteria
- Methodologies for computing prioritized indicators, and
- Potential data sources for indicator computation
- A design guideline for the Data Reference Sheet
- A demonstration of the Baseline Data Reference Sheet

We will then organize a communication workshop with relevant agencies to present the framework and a prototype product and gather expert feedback. The feedback will be incorporated into the refinement of the Data Reference Sheet. The finalized prototype of the indicator toolbox will feed the 5NC/2BTR Adaptation Chapter’s sections on progress in monitoring and evaluation of NAP implementation. More importantly, the result of this task will serve as a foundation for future adaptation cycles.




# Developing data products and computation logic of Task 3 with aim to integrating into the central data lake
## Prototype in an Isolated Environment.
 Fork a dataset from the Task 2 database. Use a simple, flexible environment like a **Jupyter Notebook** (which is more robust and reproducible than Excel) to work with M&E experts. In this sandbox, we can develop and validate the indicator definitions, calculation methodologies, and include more data into the database in a consistent way with the database of Task 2. This is the perfect way to figure out the _what_ and _how_ of the calculations quickly.
## Recommendation to Integrate the Validated Logic. 
Once the calculation logic is proven and validated in the prototype, we will recommend to implement that _same logic_ within the main Task 2 architecture. This means translating the prototype script into a production-ready process that runs against the live **Analytics Warehouse**.