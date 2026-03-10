---
type: Artifact
tags: []
status: current
capture_date: 2026-01-06
origin_prompt: why do I need to wait for adpc database schema to design Data Reference Sheet?
relevance_to: "[[Synergy among the project - data flow]]"
---
[[Data Reference Sheet]]

Based on the **BTR Implementation Plan** and the **Synergy** documents, you need to wait for the ADPC database schema (or strictly align with it) to design the **Data Reference Sheet (DRS)** for three specific technical reasons:

### 1. To Prevent Re-work (Explicit Dependency)

The **BTR Implementation Plan** explicitly lists this as a primary control for the project. Under the "Dependencies & Controls" section, it states:

> "**Data alignment:** WP‑4 indicator fields mirror WP‑3 schema (prevent re‑work)."

If you design the DRS fields (e.g., column names, data types, units) before ADPC defines the database structure, you risk creating a reference sheet that describes a database that doesn't exist. You would then have to rewrite the DRS to match the actual physical tables ADPC builds.

### 2. The DRS acts as the "User Manual" for the Platform

In WP-4 Task 3 (Baseline framework structure), the plan lists "Alignment with platform fields" as a constraint.

The Data Reference Sheet is not just a theoretical list; it is intended to be the technical documentation for the data stored in the Risk Platform.

- **The Schema (WP-3):** Defines _how_ the data is stored physically (e.g., `Table: Flood_Risk`, `Column: flood_depth_val`, `Type: Float`).
    
- The DRS (WP-4): Defines what that data means and how to use it (e.g., "Indicator 1.1 uses flood_depth_val from Table A").
    
    Without the schema, the DRS cannot accurately point to the correct data source.
    

### 3. Synergistic Data Flow

The **Synergy** document outlines that the ecosystem operates as a pipeline. The **CRDB** (Librarian) and **CRI** (Data User) rely on the **BTR** (Builder) to ingest the data first.

- The DRS is effectively the "Metadata" for the data ADPC collects.
- If ADPC changes a dataset format (e.g., from "Point" to "Area" for Flood data, as discussed in the Dec 24 meeting), the DRS must reflect that change immediately or it becomes obsolete.
    

**Summary:** You are waiting because the DRS is the _logical_ map of the _physical_ territory ADPC is building. You cannot draw an accurate map until the territory (Schema) is surveyed.



You can proceed with the **Conceptual Design** of the DRS (defining the indicators and logic) _now_, derived from the Baseline Framework. But you should mark the **"Data Source / Computation Method"** columns in your DRS as **"Pending ADPC Schema"** rather than inventing your own field names. This allows you to progress on the M&E logic without strictly waiting for ADPC's SQL engineering.