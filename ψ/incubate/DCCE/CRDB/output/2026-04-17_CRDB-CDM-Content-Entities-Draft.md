# Draft: CDM Content Entities (Knowledge Domain Expansion)

**Date:** 2026-04-17
**Status:** Draft for Implementation
**Trigger:** T-018 (Governed Content Hub & Source Registration Protocol)
**Related Deliverables:** D-023 (CDM Operationalization), D-024 (NCAIF Service Architecture)

## Purpose
To formally expand the Conceptual Data Model (CDM) to govern "Content-as-Data" and solve the "Orphan Knowledge" problem. This aligns with the CH-010 pivot, replacing the outdated `KNOWLEDGE_ASSET` placeholder with a robust, metadata-driven architecture for managing static pages and external media.

---

## 1. The `CURATED_PAGE` Entity (Thin Integration)
Models the administrative metadata of a static webpage (e.g., a Provincial Risk Profile). This ensures that manually authored website pages are formally linked to the underlying data catalog, enabling impact analysis and lifecycle governance.

**Attributes:**
- `PAGE_ID` (PK)
- `PAGE_URL` (String)
- `PAGE_TITLE` (String)
- `PAGE_TYPE` (e.g., Area Profile, Sector Summary, Policy Explainer)
- `OWNER_ROLE` (FK to Governance Role)
- `LAST_REVIEWED_DATE` (Date)
- `EXPIRY_DATE` (Date)
- `PUBLISHING_STATUS` (Draft, Published, Archived)

**Relationships:**
- `CURATED_PAGE` }|--|| `DATASET_ID` : *references_data* (Links the page to the official catalog entry)
- `CURATED_PAGE` }|--o| `RISK_METRIC` : *visualizes_metric* (Links the page to a specific analytic output)

---

## 2. The `COMMUNICATION_ASSET` Entity (Media Synthesis)
Models the final output of media synthesis (e.g., Facebook infographics, policy digests, briefing packs). It acts as the parent container for public-facing communications that make data-driven claims.

**Attributes:**
- `ASSET_ID` (PK)
- `ASSET_TYPE` (Infographic, Policy Digest, Presentation, MVP-1 Briefing Pack)
- `PUBLICATION_CHANNEL` (NCAIF Website, Facebook, Print)
- `PUBLISHER_ROLE` (FK to Governance Role)
- `PUBLICATION_DATE` (Date)

**Relationships:**
- `COMMUNICATION_ASSET` }|--|| `EXTERNAL_REFERENCE` : *cites_external_source* (Governs internal staff research)
- `COMMUNICATION_ASSET` }|--|| `EVIDENCE_PACKAGE` : *grounded_in_evidence* (Governs consultant outputs)
- `COMMUNICATION_ASSET` }|--o| `HAZARDOUS_EVENT` : *communicates_about* (Links narrative to a specific shock/event)

---

## 3. The `EXTERNAL_REFERENCE` Entity
A lightweight catalog entry for ad-hoc data sourcing from the internet. This satisfies the "Source Registration Protocol" without requiring DCCE to fully host third-party datasets in their own lake.

**Attributes:**
- `REF_ID` (PK)
- `SOURCE_TITLE` (String)
- `SOURCE_URL` (URL)
- `PUBLISHING_AUTHORITY` (e.g., IPCC, WMO, TMD)
- `DATE_ACCESSED` (Date)

---

## 4. The `EVIDENCE_PACKAGE` Entity
A structured folder or container holding raw data submitted by consultants alongside their final media. This ends the "Orphan Knowledge" cycle by ensuring the raw files (CSVs, shapefiles) are retained in the DCCE infrastructure.

**Attributes:**
- `EVIDENCE_ID` (PK)
- `SUBMISSION_DATE` (Date)
- `SUBMITTED_BY` (Consultant/Contractor Name)
- `BRONZE_LAYER_PATH` (URL/URI to the Data Lake raw storage)

**Relationships:**
- `EVIDENCE_PACKAGE` ||--|{ `DATASET_ID` : *contains_datasets* (Registers the raw files into the main MVP-3 catalog for future discovery)