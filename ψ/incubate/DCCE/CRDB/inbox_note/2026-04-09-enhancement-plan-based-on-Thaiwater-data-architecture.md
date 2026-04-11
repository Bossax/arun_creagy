
1. Create a thorough analysis artifact on Thaiwater data governance framework. Last session, we jumped into applying lessons from Thaiwater to CRDB without taking a step to understand the data governance framework itself. sources [[ψ/incubate/DCCE/CRDB/inbox_note/Thaiwater data governance sitemap|Thaiwater data governance sitemap]] [[ψ/incubate/DCCE/CRDB/inbox_source/Thaiwater Governance Framework|Thaiwater Governance Framework]]

In CRDB project, we need to
1. propose a set of `reference parameter standard`   as part of data standards:
	- this is crucial to set canonical models for all entries of every domain. 
	- it is like standardization of standardization. 
	- for example, rain fall intensities and Tavg_daily are two different parameters that could have a field that specifies point of the values. If one says `SUB-DISTRICT` and one uses `TAMBON` that would be a headache. 
	- `Reference Parameter Standard` will set `SUB-DISTRICT` as the standard data field with names of all sub-district. The list of  sub-district names could be used for data validation or QC when importing data to the system
2. Create a document dedicated to Loss and Damage MVD (known internally as logical data model for loss and damage sub-domain within Impact, Vulnerability and Risk Assessment domain [[ψ/incubate/DCCE/CRDB/output/Conceptual Data Model for climate risk and adaptation data system|Conceptual Data Model for climate risk and adaptation data system]])
	- we will create forms as temporary operational interface between DDPM and DCCE. Probably a doc on how to map (or excel with embedded mapping logic) is required
3. Data quality framework bases on the `Reference Parameter Standard` for data layer QC. 
	- applicable to products like data catalog and logical data model
	- flags and tier

4. follow suggestions to consolidate governance artifacts and freeze the current design and direction in a single canonical artifact 


>[!key] My reflection:
> The enhancement is mostly data standards, metadata and governance process. Loss and Damage sub-
> domain design is the most data architecture technical one
