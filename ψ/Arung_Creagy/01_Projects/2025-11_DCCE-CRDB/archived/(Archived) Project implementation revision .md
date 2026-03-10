---
type: hypothesis
status: archived
version: 1
tags: []
project:
  - DCCE_CRDB
parent_note: "[[Refine CRDM implementation using data architecture jargon]]"
created: 2025-11-24
---
>[!note] incorporated



Developing the National Climate Adaptation Information Framework (NCAIF) = developing an Enterprise Data Model (EDM)

# EDM
Enterprise data model provides a view of all databases in the company
- conceptual and logical models
- no physical model since actual data resides across the databases
- physical models are schemas
	- kept in **Schema Registry**

> We are not focusing on the schemas. We try to get the logical models right.


# NCAIF
developing NCAIF means

1. document and draft business logic: interview DCCE staff and stakeholders to map out subject areas in addition the 4 areas stated in the TOR [[CRDB - Technical proposal final]] 
2. identify key entities in each area
3. identify relationships among the entities
4. create **glossary** ~~and~~ **~~data dictionaries (technical metadata)~~**
5. create hierarchical knowledge structure as a **business artifact**. 
6. dig into the detail of disaster area, and loss&damage entities
	1. design **a logical model** for the loss and damage entities
7. dig into the data product area
	1. design **business metadata** for the analytical data products
	2. design a schema for the analytical data products
8. draft **technical metadata** and **EDM logical model** for specific areas that are considered essential for risk assessment (needs to be defined in more detail)
9.  create data dictionaries 
10. implement a "**data catalog**" to search through the **data dictionaries** and **data products**  in a spreadsheet
11. fulfill data governance framework by creating artifacts
	1. data owner
	2. data custodian
	3. data quality
	4. data lineage 