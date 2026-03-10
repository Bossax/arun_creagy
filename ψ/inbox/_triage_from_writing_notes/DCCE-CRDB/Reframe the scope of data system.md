---
status: archived
tags: []
created: 2026-01-12
last_updated: 2026-01-13
AI_prompt: true
project:
  - DCCE_CRDB
type:
aliases:
  - Idea / note
---
When we look at the data management strategy from the Adaptation Cycle perspective, we need to reframe the scope of the 'data system' to
1. ensure practicality under project timeline and scope
2. incremental buy-in from various stakeholders 

The adaptation cycle detail is in [[Hypothesis_Adaptation Cycle]]

- the M&E stage is taken up by the CU research team, which defines key frameworks of M&E while containing many flaws
- [[DCCE  website diagram]] reveals that data management of DCCE is still fragmented. Most data products are designed to function separately and were delivered by individual projects. The DCCE website is just a shelf where products are sloppily arranged. 
- On DCCE website, there are many other website platforms and data products like dashboards and visualizations that lack strong use case patched together. These visuals are produced from separate databases with minimal shared repositories (I guess)
- The IVRA stage is the main responsibility of the Risk Assessment sub division who is the project sponsor. The data system we are designing in this project should serve this stage first. The 'platform' that the sub-division will create, however, should be the prime example of how the data is managed.
- In the future, harmonization of fragmented data systems across DCCE divisions can be done by linking other systems to the IVRA data system. 


**Ideas for demonstrating data exchange and integration**
1. create a data pipeline and a canonical data model to ingest datasets from the adaptation M&E platform into risk assessment platform
	1. scan for data domain that overlaps with this risk domain
	2. ask if we can have an API to periodically load data