# CRDB Integrated Concept Proposal: The Governed Content Hub

**Date:** 2026-04-17
**Status:** Draft for Approval
**Trigger:** T-018 (Copernicus CDS Benchmark & Content-as-Data realization)

## 1. Executive Summary

This proposal reframes the CRDB project's architectural stance. While the sponsor (DCCE) expects NCAIF to function as a traditional, manually curated "website" for policy makers and the public, our gap analysis and benchmarks (Copernicus CDS, T-PLAT) demonstrate that a monolithic website will quickly become a "cemetery of reports" with broken links and orphaned data.

To bridge the gap between **sponsor expectations (static pages)** and **enterprise architecture (interoperable data)**, we propose a "Thin Integration" approach: **The Governed Content Hub**. 

We will not force a complex Headless CMS in Phase 1. Instead, we will allow DCCE to manage static/curated pages using their existing tools, but we will strictly govern those pages as **Administrative Assets** within the Enterprise Data Model (EDM).

## 2. Core Architectural Shifts

### A. Solving the "Static Page" Expectation (Thin Integration)
DCCE staff need to publish narrative summaries and other info related to climate risk and adaptation manually. 
*   **The Pivot:** The EDM will model the **Page as an Asset**. We introduce a new entity, `CURATED_PAGE` (e.g., a Provincial Risk Profile page).
*   **The Rule:** The page itself can be static HTML, but its existence must be registered in the EDM. The registry entry *must* explicitly link the `CURATED_PAGE` to the official `DATASET_ID`, `RISK_METRIC`. or any other data it references. If the underlying dataset changes or is deprecated, the database flags the static page for manual review.

### B. Solving the "Orphan Knowledge" Problem (Media Synthesis)
DCCE staff and consultants frequently produce media (Facebook infographics, policy digests) using external research. The final PDF/JPEG is published, but the underlying structured data is lost.
*   **The Pivot:** We expand the CDM to include `COMMUNICATION_ASSET`, `EXTERNAL_REFERENCE`, and `EVIDENCE_PACKAGE`.
*   **The Rule (Source Registration Protocol):** No data-driven claim can be published on official channels unless its source is registered.
    *   *For internal staff:* They must register the URL/Citation of the external research as an `EXTERNAL_REFERENCE`.
    *   *For consultants:* TORs will mandate that alongside the final media, they submit an `EVIDENCE_PACKAGE` (raw CSVs, shapefiles) into the Data Lake's "Bronze Layer," ensuring the DCCE retains the raw data.

## 3. Impact on Phase 1 Deliverables

| Deliverable          | Previous Stance                                                                            | Proposed Stance (Governed Content Hub)                                                                                                                                                                                                        |
| :------------------- | :----------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CDM (Data Model)** | Focused on Hazard, Exposure, Vulnerability, and Loss accounting.                           | **Expanded Knowledge Domain**: Adds `CURATED_PAGE`, `COMMUNICATION_ASSET`, `EXTERNAL_REFERENCE`, and `EVIDENCE_PACKAGE` linked to scientific entities.                                                                                        |
| **NCAIF (Sitemap)**  | A taxonomy of website pages.                                                               | **Service & Resource Hub**: The navigation remains the same (Policy Maker Center, Adaptation Cycle), but pages act as "front doors" to the catalog, with dynamic "Data Sources Used" citations.                                               |
| **Data Governance**  | "Publishing Rails" for tabular datasets.                                                   | **Publishing Protocols**: Governance gates apply to *Narrative Content*. A `CURATED_PAGE` cannot be listed on the official sitemap if its linked data is unverified. Includes the "Source Registration Protocol."                             |
| **Use Cases**        | Focused on finding data and viewing maps.                                                  | **Content Lifecycle Focus**: Added workflows for "DCCE Author drafting a briefing and linking official baselines" and "Consultant submitting an Evidence Package."                                                                            |
| **MVPs**             | MVP-1 (Briefing Packs) as simple downloads; MVP-3 (Clearinghouse) as a basic dataset list. | **Integrated Output**: MVP-1 packs are structured `COMMUNICATION_ASSET`s. MVP-3 acts as the governed metadata catalog (enforcing access controls and publishing protocols) providing the endorsed baselines that static pages *must* link to. |

## 4. TOR Compliance & Strategic Value

This decoupled, governance-first approach perfectly satisfies the TOR constraints while future-proofing the DCCE:
*   **TOR 5.2.3 (Data Management Structure):** We provide a structure that manages both "Hard Data" (tables) and "Soft Data" (communications/web pages), eliminating shadow IT.
*   **TOR 5.3.8 (Gap Analysis):** We directly address the gap of "Orphan Knowledge" and fragmented web content.
*   **Interoperability:** By treating pages as metadata-linked assets, we prepare the DCCE for a future transition to a true Headless CMS (like Copernicus) without throwing away their work, while keeping the data layer clean for machine-to-machine exchange (GDX).

## 5. Action Plan for Sealing

Pending your approval of this concept, the following execution steps will be taken:
1.  **Register CH-010**: Formalize the pivot to the "Governed Content Hub" and "Source Registration Protocol" in the Change Log.
2.  **Update D-024 (NCAIF Architecture)**: Revise the service architecture to reflect `CURATED_PAGE` integration.
3.  **Update D-025 (Governance Plan)**: Detail the "Publishing Protocols" for static pages and media synthesis.
4.  **Draft CDM Content Entities**: Outline the specific entity relationships (`COMMUNICATION_ASSET` -> `EXTERNAL_REFERENCE` / `DATASET_ID`).