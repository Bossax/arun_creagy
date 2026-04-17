15:50 17 April 2026

To understand a platform as comprehensive as the Copernicus Climate Data Store (CDS), we must look past the frontend user interface and examine the underlying **Spatial Data Infrastructure (SDI)** and **Distributed Data Architecture**. The CDS is not a monolithic database; rather, it is a highly decoupled, cloud-native ecosystem built on the principle of bringing "compute to data" rather than moving massive petabyte-scale datasets to the user.

Here is an architectural breakdown of how these digital assets and services are modeled, replacing frontend terminology with industry-standard data architecture paradigms.

### 1. "Information Pages" $\rightarrow$ Content Management & Unstructured Data Layer

The static and dynamic informational content of the platform is not modeled alongside the scientific data. Instead, it is managed via a decoupled **Headless Content Management System (CMS)**.

- **Data Modeling:** The text, imagery, and structural metadata of these pages are modeled as hierarchical, semi-structured document objects (typically JSON).
    
- **Infrastructure:** This is stored in a NoSQL document database (e.g., MongoDB) or delivered statically via a Content Delivery Network (CDN) at the edge. This separation of concerns ensures that high traffic to informational pages does not consume compute resources meant for complex climate data querying.
    

### 2. "Data Catalog" $\rightarrow$ Metadata Management & Discovery Layer

The catalog is the central nervous system of a data platform. It does not store the physical datasets; it stores the **metadata schemas** that make the datasets discoverable and interoperable, adhering to **FAIR (Findable, Accessible, Interoperable, Reusable)** principles.

- **Data Modeling:** Metadata is strictly modeled using international geospatial and data cataloging standards. For a climate platform, this involves **STAC (SpatioTemporal Asset Catalog)**, **DCAT-AP (Data Catalog Vocabulary)**, and **ISO 19115/19139** for geographic information.
    
- **Infrastructure:** The catalog is driven by a relational database (like PostgreSQL with PostGIS extensions) or a dedicated search index engine (like Elasticsearch or Apache Solr) to allow sub-second semantic querying, spatial bounding-box intersections, and temporal filtering.
    

### 3. "Hosted Actual Datasets" $\rightarrow$ Payload Data & The Data Lakehouse Layer

In climate architecture, observational and modeled data are massive, multi-dimensional arrays (tensors). Traditional relational databases cannot handle this. Copernicus utilizes a **Distributed Data Lake** approach combined with a central **Data Broker**.

- **Data Modeling:** The physical data payloads are modeled as multi-dimensional arrays. Instead of proprietary or heavy legacy formats, modern architectures serialize this data into **Cloud-Optimized Formats** such as **Zarr**, **Cloud-Optimized GeoTIFFs (COG)**, and **NetCDF/GRIB** (often indexed via Kerchunk). These formats support byte-range requests, allowing a user to read a tiny slice of a petabyte-scale file over the web without downloading the whole asset.
    
- **Infrastructure:** The data resides in scalable **Object Storage** (e.g., AWS S3, Google Cloud Storage, or on-premise object stores via Ceph). Copernicus specifically uses a distributed architecture where the central CDS acts as an **API Gateway and Broker**, routing user requests to distributed backend data nodes (managed by different European agencies) rather than hosting all petabytes in one centralized server.
    

### 4. "Dashboards" $\rightarrow$ Presentation Layer & Materialized Analytics

Dashboards require low-latency aggregation of data. Running complex geospatial queries directly against the Data Lake for every dashboard load is architecturally inefficient and cost-prohibitive.

- **Data Modeling:** Data for dashboards is modeled in an **Online Analytical Processing (OLAP)** paradigm. The raw multi-dimensional data is pre-processed through Extract, Transform, Load (ETL) pipelines into aggregated forms.
    
- **Infrastructure:** The results are stored in **Materialized Views**, an OLAP database (like ClickHouse or Google BigQuery), or an in-memory caching layer (like Redis). The frontend dashboard communicates with this layer via a RESTful or GraphQL API, completely decoupled from the raw data lake.
    

### 5. "Application Store" $\rightarrow$ Compute-to-Data Orchestration & Microservices

What you refer to as the application store (the CDS Toolbox) is a sophisticated **Container Orchestration and Serverless Compute** environment.

- **Data Modeling:** Applications are modeled as containerized microservices or functional execution graphs. Users define a workflow (e.g., calculating a temperature anomaly over a specific polygon).
    
- **Infrastructure:** When a user runs an app, the platform provisions an ephemeral compute container (via Kubernetes). This compute node is spun up _in the same cloud region_ as the Object Storage (the Data Lake) to ensure high-bandwidth, low-latency data access. Once the operation is complete, the resultant derivative data is temporarily stored in a cache, passed to the user, and the compute container is destroyed. This is executed via standardized APIs, such as the **OGC (Open Geospatial Consortium) API - Processes**.
    

### Strategic Implications for Thailand's DCCE

For our Terms of Reference (TORs), attempting to build a monolithic database for climate risk will fail at scale. We must advocate for:

1. **Strict Decoupling:** Separating the CMS, Metadata Catalog, and Data Lake.
    
2. **Standardized Metadata Ontologies:** Adopting STAC and ISO standards to ensure our data can interoperate with global bodies like Copernicus or NOAA.
    
3. **Cloud-Optimized Storage:** Moving away from traditional GIS servers serving heavy shapefiles, and transitioning to object storage with Zarr and COG arrays to democratize access to high-resolution climate modeling for local adaptation planning.
    
4. **Identity and Access Management (IAM):** Being transparent about data access limits by implementing a robust API Gateway that enforces quotas and rate limits, ensuring operational stability without hiding public data.

# How CMS is modeled

While Entity-Relationship Diagrams (ERDs) perfectly capture the strict tabular constraints and Third Normal Form (3NF) relational architecture of a Data Catalog, attempting to model a modern Headless Content Management System (CMS) with an ERD is an architectural anti-pattern.

CMS data—such as policy briefs, news updates, public guidelines, and dynamic page layouts—is inherently unstructured or semi-structured. Imposing rigid relational schemas on this data creates fragile, overly complex architectures.

Instead, in a Headless CMS architecture, we utilize **Content Modeling** within a **Document-Oriented** or **Graph-Based** paradigm. Here is how this information is modeled structurally and strategically.

---

### 1. The Paradigm: Document-Oriented Schemas

Rather than tables, rows, and columns, a Headless CMS relies on **JSON (JavaScript Object Notation)** document stores (backed by NoSQL databases like MongoDB, DynamoDB, or PostgreSQL with JSONB columns).

The data is modeled hierarchically. A single "document" can contain deeply nested arrays and objects, eliminating the need for the complex, computationally expensive `JOIN` operations required in relational models.

### 2. Core Modeling Primitives

When we model the CMS, we define a structured ontology using the following primitives:

- **Content Types (Entities):** This is the blueprint. Instead of a "Table," we define a Content Type (e.g., `ClimatePolicyDocument`, `Author`, `LandingPage`).
    
- **Fields (Attributes):** The specific data points within a Content Type. These range from primitives (Strings, Booleans, Dates) to rich types (Markdown, Rich Text, GeoJSON points).
    
- **Components / Modular Blocks:** This is where document modeling outshines relational modeling. If a web page requires a dynamic sequence of text, an image gallery, and a quote, we model these as reusable "Components." The CMS stores an array of these components directly within the JSON document, preserving the exact rendering order without requiring external junction tables.
    
- **Taxonomies:** Controlled vocabularies (Categories, Tags, Regions) mapped as flat or hierarchical lists to classify content for search and filtering.
    

### 3. Relationship Modeling and the Graph

While an ERD relies on Primary Keys (PK) and Foreign Keys (FK) enforced at the database engine level, a CMS models relationships via **Document References**.

- **Directed Acyclic Graphs (DAG):** Relationships in a CMS form a graph. For example, an `Article` document contains an array of reference IDs pointing to specific `Author` documents and `Category` documents.
    
- **GraphQL Resolvers:** Because the data is modeled as a graph, modern CMS architectures standardly expose a **GraphQL API**. This allows the frontend presentation layer to traverse the graph and request the exact nested structure it needs in a single query, rather than making multiple REST calls to different relational endpoints.
    

### 4. How We Visualize the Model

Since we do not use ERDs for a CMS, we rely on alternative visual documentation standards during the architecture phase:

- **UML Class Diagrams:** Adapted to show Content Types as classes, highlighting inheritance and compositional relationships (e.g., a `Page` _has many_ `Blocks`).
    
- **Content Model Graphs:** Visual node-and-edge diagrams mapping the reference paths between Content Types.
    
- **JSON Schemas:** Technical, machine-readable specifications that strictly define the allowed structure, required fields, and validation rules for the JSON documents.
    

---

### Strategic Alignment for DCCE

For the Department of Climate Change and Environment, modeling our informational assets using a decoupled, Document-Oriented approach serves our strategic TORs in two critical ways:

1. **Agility in Public Communication:** The DCCE needs to rapidly publish varied content—from urgent weather advisories to complex, multi-page adaptation strategies. A document model allows content creators to build pages modularly without requiring database engineers to alter SQL schemas.
    
2. **Omnichannel Data Transparency:** By modeling the content purely as JSON payloads accessible via APIs, we do not just build a website. We build a centralized content repository that can simultaneously syndicate public alerts to a web dashboard, a mobile application, and digital public kiosks across Thailand without duplicating the data layer.