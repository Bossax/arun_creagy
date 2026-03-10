---
status: archived
tags: []
created: 2026-02-11
last_updated:
AI_prompt: true
AI_output: false
project:
  - DCCE_CRDB
type: note
---
This version extends the deck to **12 slides**. It prioritizes the **NCAIF Sitemap** at the beginning to set the vision (the "User Experience"), and then transitions into the **Conceptual Data Model** (the "Engine"), with a specific deep dive into every subject area including the Resilience/CRI logic.


**Role:** You are the Lead Data Architect for the Thailand DCCE Climate Risk Database (CRDB). **Task:** Create a detailed outline for a **12-slide Consultant-Style Presentation**. **Audience:** Internal Climate Risk Specialists and Project Teammates (Non-IT background). **Goal:** First, explain the **National Climate Adaptation Information Framework (NCAIF)** as the user-facing solution. Second, explain the **Conceptual Data Model (CDM)** as the "engine" that powers it. **Tone:** Strategic, authoritative, minimalist ("Blue & White" aesthetic), and professional. Use "We" language.

---

**Presentation Structure & Content Requirements:**

**Slide 1: Title Slide**

- **Title:** The National Climate Adaptation Information Framework (NCAIF)
    
- **Subtitle:** User-Centric Design & Data Architecture Strategy
    
- **Footer:** DCCE CRDB Project | Architecture Phase | [Date]
    

**Slide 2: Project Context & Status**

- _Source: Work Status Brief_
    
- **Status:** Green (On Track). Inception Phase complete; Architecture Phase active.
    
- **The Goal:** We are designing the "Blueprint" (Logical Architecture) before we buy the "Bricks" (Physical Servers).
    
- **Key Milestone:** Preparing for Focus Group #2 to validate these concepts.
    

**Slide 3: The Vision – NCAIF Sitemap (Sector-First Design)**

- _Source: National Climate Adaptation Information Framework.md_
    
- **The Shift:** Moving from "Siloed Science" to "Sectoral Solutions."
    
- **The Entry Point:** Users do not start with "Data." They start with "Sectors" (Water, Agriculture, Tourism, Health, Resources, Settlements).
    
- **User Journey:** A Ministry user clicks "Agriculture" -> sees "Drought Impacts" -> finds "Adaptation Solutions."
    
- **Why:** This directly addresses the "Plain Language" need identified in our stakeholder analysis.
    

**Slide 4: NCAIF Structure – The Three Layers**

- _Source: National Climate Adaptation Information Framework.md_
    
- **Layer 1: Sectoral Pathways:** The front door for policy users (Impacts, Solutions, Projects).
    
- **Layer 2: Climate Observatory:** The foundational scientific layer (Projections, Hazardous Events) running in the background.
    
- **Layer 3: National Progress:** The M&E dashboard that tracks the NAP goals and aggregates success.
    

**Slide 5: The "System of Systems" Concept**

- _Source: National Climate Adaptation Information Framework.md_
    
- **Integration:** The NCAIF is not an island.
- **The Hub:** It connects:
    - **Risk Data** (from DCCE/ADPC).
    - **Best Practices** (from T-Plat).
    - **M&E Results** (from the Monitoring System).
        
- **Takeaway:** We are building the "Connective Tissue" that links these assets together.
    

**Slide 6: Transition – From Interface to Engine**

- _Source: Conceptual Data Model_
    
- **The Question:** How do we deliver the right data to the right sector without chaos?
    
- **The Answer:** The **Conceptual Data Model (CDM)**.
    
- **Analogy:** The NCAIF is the "Menu" (what the user sees). The CDM is the "Kitchen" (how we organize the ingredients).
    
- **Role:** It enforces the rules of many standard ontologies

**Slide 7: Key subject Areas
- list key subject areas in the CDM

**Slide 8: CDM Subject Area 1 – Physical Climate (The Hazard Engine)**
- _Source: Conceptual Data Model (Subject Area 1)_
- **The Challenge:** Distinguishing "Weather" from "Climate."
- **The Architecture:**
    - **`HAZARDOUS_EVENT`:** Discrete disasters (e.g., "Chiang Mai Flood 2024").
    - **`CLIMATE_DRIVER`:** Long-term trends (e.g., "Mean Temperature Rise").
    - **`CLIMATE_SCENARIO`:** The "What If" future simulations (CMIP6).
        
- **Why:** This structure allows us to track both sudden disasters and slow-onset climate shifts simultaneously.
    

**Slide 8: CDM Subject Area 2 – Risk & Impact**

- _Source: Conceptual Data Model (Subject Area 2 and 3)_
    
- **The Challenge:** How do we link a loss to a specific cause both acute and slow-onset events?
    
- **The Solution:** The **`ATTRIBUTION_LINK`** entity 
    
- **Mechanism:** It connects a `LOSS_DAMAGE_RECORD` to either a specific Event (Flood) or a slow onset  (sea level rise).
- **Risk assessment results**: Risk_metric for probabilistics assessment and composite_inde for index_based assessment
    
- **Value:** It merges the two divergent methodology of assessment into one framework
    
**Slide 9: CDM Subject Area 3 – Vulnerability and Exposure (with in risk and impact) (The Attribution Engine)**
- _Source: Conceptual Data Model (Subject Area 3)_
- **The Challenge:** Different sectors measure risk differently (Math vs. Scores).
- **The Solution:** "Polymorphic Vulnerability."
- **Mechanism:** We allow for probabilistic and index-based analysis depending on Vulnerability definition
    - **`IMPACT_FUNCTION`:** For hard science/engineering curves (Quantitative).
    - **`VULNERABILITY_FRAMEWORK`:** For policy indices/scores (Qualitative). explain how it maps vulnerability_determinant  
        
- **Value:** The system adapts to new methodologies without needing a rebuild.
    

**Slide 10: CDM Pillar 4 – Response & Resilience (The CRI Engine)**

- _Source: Conceptual Data Model (Subject Area 4)_
- **The Challenge:** How do we measure "Resilience" and calculate the Climate Resilience Index (CRI)?
    
- **The Solution:** "Composite_Index." with Resilience_Framework mapping indicators and parameters based on how resilience is framed
    
- **Mechanism:**
    1. **`ADAPTATION_PROJECT`**: We implement a solution.
    2. **`INTERVENTION_RESULT`**: We measure the outcome.
    3. **`COMPOSITE_INDEX`**: The results of both index-based risk assessment and resilience assessment
        
- **Value:** This creates a dynamic loop. We don't just _assess_ risk; we track how our actions _reduce_ it over time.
    

**Slide 11: Bringing it Together – The User Scenario**

- _Source: NCAIF Sitemap & Conceptual Data Model_
    
- **Scenario:** A user asks, "Is our Rice Adaptation Project working?"
    
- **The Flow:**
    
    1. **Sitemap:** User checks "Agriculture Sector" -> "Projects."
        
    2. **CDM:** The system queries `ADAPTATION_PROJECT` -> checks `INTERVENTION_RESULT` -> updates `COMPOSITE_INDEX`.
        
- **Result:** The user sees a "Resilience Score" increase on the dashboard.
    

**Slide 12: Summary & Next Steps**

- _Source: Implementation Plan_
    
- **Summary:** We have a user-friendly front end (NCAIF) powered by a scientifically robust back end (CDM).
    
- **Immediate Action:** Validate this logic in **Focus Group #2 (Mid March )**.
    
- **Next Milestone:** Submit Interim Report (March 24).