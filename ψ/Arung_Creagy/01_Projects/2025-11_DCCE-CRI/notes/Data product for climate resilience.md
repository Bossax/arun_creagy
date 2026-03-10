---
status: archived
tags: []
created: 2026-01-29
last_updated:
AI_prompt: false
project:
  - DCCE_CRI
type:
  - idea
aliases:
  - Idea / note
---
# Principles for Data Product Design

To build a data product that guides "right action," you cannot simply display a risk map (Hazard $\times$ Exposure). You must design an interface that helps users navigate the **Resilience Calculus** (ACI vs. TCI) within the **Management Cycle** (UAE).

Here are 5 principles for designing a **Socio-Ecological Resilience Platform**:

## Principle 1: Distinguish "Maintenance" from "Transformation" Signals

- **The Problem:** Most dashboards mix all data into one "vulnerability" score. This confuses planners about whether they need to _fix_ the current system or _change_ it 
    
- **The Design Solution:** The product must separate indicators into two clear buckets based on the **Resilience Index ($RI$)** equation:
    
    - **The Maintenance Dashboard (ACI):** Shows economic stability, road density, and safety equipment. _Action Trigger:_ "Budget for maintenance/DRR."
        
    - **The Transformation Dashboard (TCI):** Shows "Hard Limits" data—e.g., permanent flood zones, failing industries, or rigid political structures. _Action Trigger:_ "Initiate System Transition/Strategic Retreat."
        
- **Visual Cue:** Use a "Traffic Light" system where Red doesn't just mean "Danger," but explicitly suggests "Transformation Required" (TCI issue), while Yellow suggests "Adaptation Required" (ACI issue).
    

## Principle 2: Visualize the "Arena of Engagement" (Trade-offs)

- **The Problem:** CRD states that resilience is negotiated, not calculated. A single "optimal" pathway is a myth.
    
- **The Design Solution:** The product should not output a single "Correct Plan." Instead, it should offer **Scenario Modeling** that reveals trade-offs:
    
    - _Scenario A (Protect):_ High cost, maintains current land use, low equity.
        
    - _Scenario B (Transform):_ High disruption, restores ecosystem, high long-term equity.
        
- **Feature:** An interactive "Impact Chain" visualizer where stakeholders can toggle interventions and see how they affect different groups (Equity lens).
    

#### **Principle 3: Monitor the "Process," not just the "Result"**

- **The Problem:** We often measure resilience only _after_ a disaster (did it break?).
    
- **The Design Solution:** Align with the **UAE Framework's Dimensional Targets**. The data product must track the **governance lifecycle**:
    
    - _Is the risk assessment up to date?_ (Step 1).
        
    - _Is there a funded plan?_ (Step 2).
        
    - _Is the system 'Ready'?_ (Step 3 - Readiness/Preparedness).
        
- **Metric:** A "Governance Maturity Score" displayed alongside the physical risk score. A city with High Physical Risk but High Governance Maturity is safer than a Medium Risk city with no plan.
    

#### **Principle 4: Integrate "Residual Risk" as a Decision Gate**

- **The Problem:** Planners often ignore risk they cannot reduce, hoping it won't happen.
    
- **The Design Solution:** Explicitly visualize **Residual Risk** as a distinct data layer.
    
    - If Residual Risk > Tolerance Threshold $\rightarrow$ The product auto-suggests **Risk Financing** (Insurance) or **Loss & Damage** mechanisms.
        
    - This prevents "Adaptation Limits" from being ignored.
        

#### **Principle 5: Socio-Ecological Coupling**

- **The Problem:** Infrastructure data is often separated from ecosystem data.
    
- **The Design Solution:** The product must link "Grey" and "Green" data.
    
    - _Example:_ If a user selects a "Flood Barrier" (Grey), the system should show the impact on downstream "River Ecology" (Green).
        
    - _Data Structure:_ Use the **System Transitions** categories (Energy, Land, Urban, Industry, Societal) as the top-level navigation, rather than just "Department of Roads" or "Department of Water".
        

### Summary: The "Right Action" Workflow

The data product should guide the user through this logic flow:

1. **Diagnostic:** "Is the Risk Index high?" (Risk Map).
    
2. **Capacity Check:** "Do we have the capacity to cope (ACI)?"
    
    - _Yes:_ Deploy **Incremental Adaptation** (DRR).
        
    - _No:_ Check **Transformative Capacity (TCI)**.
        
3. **Transformation Gate:** "Is the TCI high enough to change the system?"
    
    - _Yes:_ Design a **System Transition** (CRD Pathway).
        
    - _No:_ Focus on **Governance & Political Reform** (UAE Framework) to build that capacity.
        
4. **Residual Check:** "What risk is left?" $\rightarrow$ Arrange **Risk Financing**.