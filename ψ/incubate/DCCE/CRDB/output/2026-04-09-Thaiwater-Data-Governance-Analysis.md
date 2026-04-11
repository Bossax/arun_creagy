# Thaiwater Data Governance Framework — Analysis for CRDB

## 1. Purpose and scope

This note analyses the Thaiwater data system and its governance framework as documented at standard.thaiwater.net and the extracted report in [`Thaiwater Governance Framework.md`](ψ/incubate/DCCE/CRDB/inbox_source/Thaiwater%20Governance%20Framework.md). It is written for the CRDB project team and DCCE data / IT staff as a design evidence artifact.

The focus is on patterns that can inform CRDB Phase 1, especially:

- Reference information and code systems (units, administrative areas, agencies, hydrological features).
- Data record structures and metadata (how measurements and station information are packaged).
- Data exchange and integration architecture (APIs, file exchange, directories).
- Data quality control (levels, flags, review practices).
- Data governance organization, control flows, and repositories.
- Warning-oriented standards around events and thresholds.

This is an analysis note, not an implementation manual. It should be used as a reference when designing CRDB data standards, minimum datasets, quality controls, and governance documentation.

---

## 2. Overview of the Thaiwater data system

Thaiwater is a national data infrastructure operated by the Hydro-Informatics Institute (HII) to manage and exchange water-related information across Thailand. The documentation at standard.thaiwater.net and the extraction in [`Thaiwater Governance Framework.md`](ψ/incubate/DCCE/CRDB/inbox_source/Thaiwater%20Governance%20Framework.md) show a system with:

- A **root documentation index** defining the scope and audience.
- A first pillar on **Water Data Standards for Exchange** (มาตรฐานข้อมูลน้ำเพื่อการแลกเปลี่ยน).
- A second pillar on **Water Data Standards for Warning** (มาตรฐานข้อมูลน้ำเพื่อการเตือนภัย).
- Extensive **appendices** containing official code lists for agencies, administrative areas, and hydrological basins.
- A technical **glossary** and clear contact point for HII.

From the sitemap captured in [`Thaiwater data governance sitemap.md`](ψ/incubate/DCCE/CRDB/inbox_note/Thaiwater%20data%20governance%20sitemap.md), the exchange pillar is further organized into:

- **Reference information** (ข้อมูลอ้างอิง): units, symbols, time formats, coordinates, agency codes, location codes, basin and water source types, temporal intervals.
- **Data formats and structures** (รูปแบบและโครงสร้างข้อมูล): definitions of data records for measurements and for water resources / stations, including detailed data dictionaries.
- **Data exchange and integration**: application and presentation layers, secure exchange, API protocols, and file-based integration (FTP and CSV).
- **Data quality control**: control levels, quality flags, error types, and guidance for checking exchanged data.
- **Data governance**: governance body, control flow, repository for governance artifacts, and guidance for changes and integration.

The warning pillar extends these structures into hazard-specific terminology, indicators, and thresholds (e.g. flood and drought alert levels, colour scales, and station criteria).

Taken together, the Thaiwater documentation describes a complete ecosystem: reference codes, record structures, exchange channels, quality controls, and governance roles.

---

## 3. Reference information and code systems

### 3.1 Role of reference information

The reference information tier in Thaiwater provides a shared language so that data from different agencies can be combined without confusion. Key components include:

- **Units and symbols** for water quality and quantity parameters (e.g. microsiemens/cm, mg/L, NTU).
- **Date and time formats** based on ISO-like timestamps, used consistently in metadata and records.
- **Coordinate identification** for stations and water resources (latitude, longitude, altitude).
- **Agency codes** that uniquely identify data providers and owners.
- **Administrative and location codes** (province, district, sub-district) aligned with national standards.
- **Basin and water source categories** that classify rivers, reservoirs, ponds, canals, etc.
- **Interval codes** that describe measurement frequency (e.g. hourly, daily), used both in APIs and in file naming.

These components are exposed both in descriptive pages and in tabular appendices. They are treated as authoritative reference data rather than ordinary content.

### 3.2 Patterns relevant to CRDB

For CRDB, the main patterns to carry over are:

- **Centralized reference lists**: reference data (administrative units, basins, agency codes, intervals, etc.) should be managed as shared lists rather than scattered in each dataset.
- **Clear separation of reference vs observation fields**: fields that describe "where, who, and when" are standardized and re-used across subject areas.
- **Use of official national standards**: where possible, Thai national code lists should be used rather than inventing new codes under CRDB.

This directly supports the idea of a CRDB **Reference Parameter Standard**: a dedicated layer of canonical reference fields and code lists that every dataset and schema under CRDB will align with.

---

## 4. Data record structures and metadata

### 4.1 Measurement and station records

Thaiwater defines detailed record structures for different data types. The extracted mermaid diagram and data dictionary for **Station Information** illustrate the general approach:

- Each record includes a **metadata section**:
  - version of the standard,
  - data provider code and name,
  - time of document generation,
  - code for the water data type.
- Each record includes a **main data section** (for stations):
  - station code and name,
  - station type and description,
  - operating status and last maintenance date,
  - location code, latitude, longitude, altitude,
  - sub-basin code and instrument information.

For water resources, rainfall, water level, and water quality, Thaiwater defines similar structured records, each with:

- A fixed set of metadata fields (provider, time, type, etc.).
- A fixed set of subject-specific fields (e.g. storage volume, rainfall amount, water quality indicator values).

This yields a consistent pattern: **every data record is wrapped with metadata describing its origin and timing, and the technical payload is clearly separated from contextual fields**.

### 4.2 Patterns relevant to CRDB

For CRDB, the important lessons are:

- **Metadata should be explicit and standardised** across all key datasets, not left implicit in filenames or separate notes.
- **Event and measurement records need a consistent skeleton** that always includes: provider, creation time, observation time, spatial reference, subject (what is being measured or recorded), value, unit, and any quality flag.
- **Subject-specific fields can vary by domain**, but their structure should be documented in the same level of detail as Thaiwater does for stations and water resources.

This pattern will be particularly important for CRDB’s loss and damage-related records and other multi-agency datasets that rely on consistent provenance and timing.

---

## 5. Data exchange and integration architecture

### 5.1 Online exchange

The Thaiwater sitemap and documentation distinguish several technical layers for online data exchange:

- **Application layer**: services that expose water data through APIs.
- **Presentation layer**: how data is presented on web portals and dashboards.
- **Secure exchange layer**: protocols for ensuring confidentiality and integrity.

Within this architecture, the documentation specifies:

- Basic data types used in APIs.
- Lists of resources exposed through APIs (e.g. rainfall, water level, reservoir storage, water quality, station information).
- URL structure and base URLs.
- Use of standard HTTP status codes.
- Use of interval codes to describe data frequency.
- Rules for agency, station, and water resource identifiers in API parameters.

### 5.2 File-based exchange

Thaiwater complements APIs with file-based integration using CSV and FTP. The documentation covers:

- Allowed **file formats** for exchange (CSV templates with defined column orders and encoding rules).
- **Directory structures** on FTP servers for different data types (rainfall, water level, water resources, quality, station information).
- **Naming conventions** and folder hierarchies that encode agency, station, and time.

This gives agencies with lower technical capacity a path to participate using prepared files while still following the same standards as the APIs.

### 5.3 Patterns relevant to CRDB

For CRDB, the core patterns are:

- **Describe how data flows, even if the project does not implement full APIs yet**. It is still valuable to spell out what would be online, what would be file-based, and how confidentiality is handled.
- **Use common concepts for exchange frequency and timeliness** (e.g. interval vocabulary) across datasets.
- **Design file templates together with record structures** so that data providers and DCCE staff can rely on shared formats.

This is consistent with a catalog-led architecture where CRDB references external sources and defines templates and rules for how data will be ingested and shared.

---

## 6. Data quality control

### 6.1 Quality control levels and flags

Thaiwater explicitly documents how quality control works for exchanged data:

- **Quality control levels**: stages of checking and validation that data can pass through (for example, initial ingestion checks, more detailed review, and fully validated status).
- **Quality flags**: labels that mark specific issues or special cases in data points, such as missing values, estimated values, removed values, or suspicious values.
- **Common error types and handling guidance**: how to respond to typical problems detected during quality control.
- **Procedures for checking exchanged data**: recommendations for how agencies should verify data they receive via the standard.

These elements are documented as part of the standard itself and are treated as mandatory context for using the data correctly.

### 6.2 Patterns relevant to CRDB

For CRDB, the key lessons are:

- **Quality control should be explicit and documented**, not assumed to happen informally.
- **A small but clear set of quality control levels** is better than many overlapping terms.
- **A simple vocabulary of quality flags** can cover most cases while remaining understandable for non-technical users.
- **Baseline and indicator values used in decision-support products** should carry clear information about their quality level and any limitations.

These patterns can be adapted into a CRDB Data Quality Framework that is simpler than Thaiwater’s but aligned with the same philosophy.

---

## 7. Data governance body, control flows, and repository

### 7.1 Governance organization

Thaiwater devotes a dedicated section to data governance, including:

- **Governance body**: the group responsible for overseeing standards, code lists, and quality.
- **Data stewards and operators**: agencies and units that are accountable for specific datasets or parts of the system.

Responsibilities are described in enough detail that it is clear who decides on new datasets, who approves changes, and who maintains the standard.

### 7.2 Control flows

The governance documentation also describes control flows such as:

- How new datasets and data providers are onboarded into the system.
- How changes to data structures or code lists are proposed, reviewed, and approved.
- How quality issues are tracked and resolved over time.

These flows are mapped to specific governance roles and are part of the official standard.

### 7.3 Governance repository

Finally, Thaiwater describes how governance-related information is stored and indexed:

- A **repository for governance artifacts** (decisions, procedures, change logs).
- Guidance on how agencies should document changes to data and standards.

This ensures that governance is not just a set of meetings but a durable set of artifacts that can be audited later.

### 7.4 Patterns relevant to CRDB

For CRDB, the patterns are:

- **Define a clear governance body** for climate risk data and adaptation information, even if it is initially a small central team at DCCE.
- **Assign data stewardship roles** to key partner agencies and units.
- **Document control flows** for dataset onboarding, schema changes, and baseline endorsement.
- **Maintain a governance repository** that indexes TOR, decision logs, quality frameworks, inventories, and project management ledgers as governance evidence.

This supports traceability and makes it easier to defend design decisions in future audits or follow-on phases.

---

## 8. Warning standards and event-related semantics

The second pillar of Thaiwater focuses on standards for warning and alerting. Key elements include:

- **Terminology and definitions** related to flood and drought warnings.
- **Data and criteria for warnings**: which indicators and thresholds are used to trigger alerts.
- **Levels of warning and colour codes**: how information is communicated to different audiences.
- **Station and station-criteria standards** for warning purposes.

For CRDB, the warning standards are not directly reused, because the subject matter and institutions differ. However, they illustrate how to:

- Bind **indicators to clear definitions and thresholds**.
- Make **communication formats and levels explicit**.
- Treat warning information as part of the data standard, not as an informal convention.

These ideas are useful when CRDB defines event-related datasets and loss and damage reporting structures that may be used in decision-making and communication.

---

## 9. Pattern mapping to CRDB design

This section maps Thaiwater patterns to specific CRDB design directions and future artifacts.

### 9.1 Reference information → CRDB reference parameter standards

From Thaiwater:

- Centralized code lists for agencies, administrative areas, basins, resource types, and time intervals.
- Clear separation between reference fields and measurement fields.

For CRDB, this supports the design of **reference parameter standards** that will:

- Define canonical reference fields (e.g. administrative units, responsible agency, dataset owner, time interval) used across CRDB datasets.
- Maintain official code lists and mappings to national standards.
- Provide validation lists for data entry and ingestion.

### 9.2 Record structures and metadata → CRDB dataset templates

From Thaiwater:

- Detailed record structures with explicit metadata sections and subject-specific sections.

For CRDB, this suggests that each major dataset family (e.g. loss and damage, baseline indicators, inventories) should have a **documented record structure** that:

- Clearly lists metadata fields that are always present (provider, creation time, observation time, spatial reference, etc.).
- Clearly lists subject-specific fields for that dataset.
- Is used consistently in both documentation and any forms or templates given to partners.

### 9.3 Exchange architecture → CRDB exchange posture

From Thaiwater:

- A combined approach of APIs and file-based exchange.
- Clear rules for how data is exposed, how security is handled, and how directories are structured.

For CRDB, this translates into a **described exchange posture** where:

- Some data is linked from existing services and portals.
- Some data is exchanged through structured files based on shared templates.
- Rules for confidentiality and internal vs external sharing are documented as part of the architecture, even if full APIs are not implemented in Phase 1.

### 9.4 Quality control → CRDB data quality framework

From Thaiwater:

- Formal quality control levels and flags.
- Guidance on error types and quality checks.

For CRDB, this motivates a **data quality framework** that:

- Defines a small set of quality control levels suitable for Phase 1.
- Defines a short list of quality flags that can be applied to key datasets and indicators.
- Links quality information to governance gates and to how baseline values are presented in reports and tools.

### 9.5 Governance body and repository → CRDB governance spine

From Thaiwater:

- A formal governance body, control flows, and a repository of governance artifacts.

For CRDB, this suggests a **governance spine** that:

- Names the interim governance body and its responsibilities.
- Describes control flows for datasets and standards.
- Indexes key governance-related documents (TOR, decision logs, quality frameworks, inventories, and project management ledgers) as part of the official record.

---

## 10. Implications and next steps

The Thaiwater governance framework provides a rich example of how to combine standards, data structures, exchange mechanisms, quality control, and governance into a coherent national system. For CRDB Phase 1, the practical next steps using this analysis are:

1. **Design the CRDB Reference Parameter Standard**
   - Use Section 3 as the conceptual basis.
   - Identify which reference fields and code lists CRDB must define first.

2. **Draft record structures for key CRDB datasets**
   - Use Section 4 to shape metadata and subject-specific fields for loss and damage records, baseline indicators, and inventories.

3. **Describe CRDB’s data exchange posture**
   - Use Section 5 to explain, in the architecture documents, how CRDB expects to receive and share data (links vs files, internal vs external).

4. **Create a CRDB Data Quality Framework**
   - Use Section 6 as a template to define quality levels and flags adapted to multi-hazard, multi-sector climate risk data.

5. **Define a CRDB governance spine and repository**
   - Use Section 7 and 9.5 to structure a single governance note that names roles, control flows, and the index of governance artifacts.

This file should be cited in later CRDB planning, governance, and implementation documents as the **canonical analysis of Thaiwater data governance** that underpins CRDB’s standards and governance design.

