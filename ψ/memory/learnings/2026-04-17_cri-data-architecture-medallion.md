# Learning: CRI Data Architecture — The Medallion Pattern

**Context**: CRI Phase 1 Data Pipeline (Stages 1-4)
**Date**: 2026-04-17

## Pattern
To handle high-resolution national disaster data (200k+ records across 70k villages), a **Medallion Architecture** is superior to flat-file management. 

1.  **Bronze (Raw)**: Store immutable extracts (Excel/CSV) from agencies (BMA, DDPM, DOPA). Never edit these.
2.  **Silver (Staging)**: Cleaned, schema-aligned, and UTF-8 encoded tables. Convert Excel to CSV here.
3.  **Gold (Analytical)**: The "Single Source of Truth."
    *   **Gold Spine**: A canonical dim_location_master anchored in official DOPA codes.
    *   **Gold Facts**: Unified act_impact and act_relief tables joined to the spine.

## Application to CRI
By anchoring everything in the **8-digit DOPA Village Code**, we can perform **Constrained Redistribution**. This ensures that high-resolution spatial mapping (100m pixels) always sums up to official provincial totals, maintaining institutional auditability for the DCCE.

## Technical Implementation
Use uv to manage a clean virtual environment and pandas for "zfilling" (zero-padding) administrative codes (e.g., Province '1' -> '01') to prevent ID collision.

*Added via Oracle Learn*
