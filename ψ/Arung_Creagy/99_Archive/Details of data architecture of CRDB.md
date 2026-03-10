---
parent: "[["
tags:
creation_date: 2025-10-16
project:
  - DCCE_CRDB
status: archived
type: idea
ai_generated: false
---

## Metadata and Governance Layer
### Data catalog
1. Discover and register datasets
2. Enrich metadata context
3. Categorize datasets
4. Enable search and discovery

### Data product catalog
1. **Define what constitutes a “data product”:**  
    A reproducible, governed, and output-oriented data unit — e.g., CLIMADA API, flood risk scoring model, or IPCC hazard visualization layer.[](https://erstudio.com/blog/how-medallion-architecture-with-er-studio-and-databricks-solves-data-as-a-product-for-both-business-and-it/)​
    
2. **Design product metadata schema:**  
    Include attributes such as product name, description, input datasets (linking to the data catalog), version, owner, methodology, and output format.
    
3. **Link products to datasets:**  
    For each product entry, reference the curated Gold-layer datasets it consumes or generates (e.g., “Coastal Vulnerability Index → gold/coastal_exposure.parquet”).
    
4. **Catalog tools, pipelines, and APIs:**  
    Include references to Jupyter notebooks, geospatial tools, or machine learning APIs that operationalize the data.

### Metadata store
- Use your metadata store as a **central federation layer**, allowing:
    - Dataset-to-product mapping (which data powers which tool)
    - Product lineage visualization (tracking pipelines across layers)
    - Shared governance (uniform user access and data policies)[](https://www.cloudera.com/blog/business/data-catalog-implementation-a-step-by-step-guide.html)​
