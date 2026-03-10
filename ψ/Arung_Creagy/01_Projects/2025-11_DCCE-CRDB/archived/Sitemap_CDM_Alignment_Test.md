---
status: archived
tags: []
created: 2026-02-10
last_updated: 2026-02-10
AI_prompt: false
AI_output: true
project:
  - DCCE_CRDB
type: artifact
---
# CDM Applicability Test: Sitemap Alignment & Data Management

## 1. Overview
This document evaluates whether the refined CDM can deliver the content and functionality required by the two chosen sitemap options. It serves as a verification that the "Back-end" data structure supports the "Front-end" website expectations of DCCE.

---

## 2. Test 1: Option 1 - The "Climate Intelligence Hub"
*Philosophy: Data Transformation Pipeline (Science -> Risk -> Policy -> M&E)*

| Sitemap Module | Required Content | CDM Supporting Entity | Data Management Logic |
| :--- | :--- | :--- | :--- |
| **1. Observatory** | Future Projections, CIDs, Historical Trends | `CLIMATE_SCENARIO`, `CLIMATE_DRIVER`, `HAZARDOUS_EVENT` | Managed as NetCDF/Raster metadata pointers. CIDs map to IPCC AR6 taxonomy. |
| **2. Risk Analytics** | Risk Maps, Exposed Assets, Loss Records | `RISK_ASSESSMENT`, `EXPOSED_ASSET`, `LOSS_DAMAGE_RECORD` | `SPATIAL_UNIT` allows toggling between Admin (Provincial) and Natural (River Basin) views. |
| **3. Adaptation Knowledge** | Solution Library, Best Practices, TRL levels | `ADAPTATION_OPTION`, `EXTERNAL_CMS_SYSTEM` | Options are categorized by **KTM** (Green/Grey/Soft). Qualitative manuals are pulled from T-PLAT via the CMS Stub. |
| **4. M&E Dashboard** | NAP Progress, Project Tracking, Resilience Scores | `ADAPTATION_PROJECT`, `INTERVENTION_RESULT`, `RESILIENCE_INDEX` | Projects update their `cycle_status` from 'Plan' to 'Evaluate' based on `INTERVENTION_RESULT` inputs. |

**Result:** **PASS**. The CDM Subject Areas (1-4) map 1:1 to the Hub's primary navigation.

---

## 3. Test 2: Option 2 - The "NAP Sectoral Navigator"
*Philosophy: Stakeholder-Centric (Ministries/Sectors)*

This sitemap requires the ability to "slice" the entire data model by NAP Sector (e.g., Water, Agriculture).

| Sectoral View Requirement | CDM Application | Data Management Logic |
| :--- | :--- | :--- |
| **Sectoral Risk Profile** | Filtered `RISK_ASSESSMENT` | The query engine filters assessments where `EXPOSED_ASSET.sector` matches the page (e.g., 'Crops' for Agriculture). |
| **Sectoral Guidelines** | Filtered `ADAPTATION_OPTION` | Options possess a `sector_id` attribute (NAP-aligned). |
| **Sectoral Projects** | Filtered `ADAPTATION_PROJECT` | Registry displays projects linked to sectoral options. |
| **Sectoral KPIs** | `INTERVENTION_RESULT` | Aggregated metrics (e.g., "Yield loss reduced") per sector. |

**Result:** **PASS**. The inclusion of the `Sector` attribute in `EXPOSED_ASSET` and `ADAPTATION_OPTION` prevents information silos while allowing sectoral "views" of the same core data.

---

## 4. Stress Test: The "Cross-Cutting" Challenge
*Scenario: A user wants to see how a "Mangrove Restoration" project (Environment Sector) reduces "Storm Surge Risk" (Coastal Sector).*

1.  **Project Start:** `ADAPTATION_PROJECT` (Mangrove) is located at `SPATIAL_UNIT` (Andaman Coast).
2.  **Mitigation Link:** It is linked to a `RISK_ASSESSMENT` for 'Storm Surge'.
3.  **Result:** `INTERVENTION_RESULT` records a reduction in `LOSS_DAMAGE_RECORD` for coastal properties.
4.  **Resilience Update:** The `RESILIENCE_INDEX` for that `SPATIAL_UNIT` improves.

**Conclusion:** The CDM successfully captures the **causal chain** required for a modern Climate Intelligence platform. It allows the website to show not just *what* was done, but *why* it was done and *how well* it worked.

---

## 5. Recommendation for Deliverable
DCCE should be presented with the **Sitemap (The Visual Website)** first to satisfy their expectations, immediately followed by the **CDM (The Engine)** to explain how the content remains updated, interoperable, and scientifically valid.
