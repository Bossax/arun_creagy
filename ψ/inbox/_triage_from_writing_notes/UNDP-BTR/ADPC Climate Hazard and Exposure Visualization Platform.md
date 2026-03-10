---
status: raw
tags: []
created: 2026-02-19
last_updated: 2026-03-06
AI_prompt: false
AI_output: false
project:
  - UNDP_BTR
type: note
---
 
## ADPC Data Provider Consultation Workshop: Enriched Notes

### 1. Hazard Focus: Heat-Related Morbidity and Mortality

- **[Meeting Note]** Current status: No centralized database for this specific hazard. Attribution of cause is difficult.
    
- **[Search Insight]** In Thailand, heat-related health data is typically split between the **Ministry of Public Health (MOPH)** (clinical records) and the **Thai Meteorological Department (TMD)** (wet-bulb globe temperature data). As of 2026, there is an ongoing effort to link these via the **National Health Data Center (HDC)** to better track "Heat Exhaustion" vs. "Heat Stroke" vs. "Aggravated underlying conditions."
    

### 2. Agency Roles & Data Status

|**Agency**|**Meeting Capture**|**Search Insight (as of 2026)**|
|---|---|---|
|**DGA** (Digital Govt Agency)|Questioned status of Digital Government Act and LLD breakdown.|The **Digital Government Act (B.E. 2565)** is now in its second phase. The goal for 2026 is 100% digital adoption across all state units. **LLD (Local Link Data)** is a DGA framework specifically designed to help Local Administrative Organizations (LAOs) standardize and share data at the **Tambon (sub-district)** level.|
|**DDPM** (Disaster Prevention & Mitigation)|1-week lead time to collect data from LAO after an event. Risk-based early warning.|DDPM operates the **Thai Disaster Data (TDD)** platform. While the 1-week collection is the current manual standard, they are migrating toward the **Disaster Risk Information System (DRIS)** to automate real-time reports from the field via mobile apps used by volunteers.|
|**DPT** (Public Works and Town Planning)|Community boundaries project in progress.|DPT is the lead agency for **Urban Planning** and **Land Use**. They are currently digitizing "Community-Level" GIS boundaries to bridge the gap between "Administrative Villages" (Muban) and actual "Economic/Social Communities" which often don't align with official lines.|
|**MSDHS / พม** (Social Dev. & Human Security)|Provides disabled population data (point data).|This is managed under the **Department of Empowerment of Persons with Disabilities**. As of 2026, this "point data" is being integrated into the **iMap Platform** to help first responders identify vulnerable households during heatwaves or floods.|
|**GISTDA**|Multi-layer data for L&D (Loss and Damage).|GISTDA provides the **Actionable Intelligence Policy (AIP)** platform which uses satellite data to verify "affected area" claims, which is critical for the LAO to release compensation funds.|

### 3. Economic Damage & Assessment

- **[Meeting Note]** Economic damage assessment requires an insurance-based approach (unlike overseas), but Thailand relies on LAO assessments and reference cost inventories.
    
- **[Search Insight]** The **Ministry of Commerce (Provincial Offices)** tracks local "Price Indexes" for construction and agricultural materials. This is the "Reference Cost Inventory" mentioned in the meeting—it is used to calculate the THB value of a destroyed house or farm for government relief payments (Regulated by the Ministry of Finance).
    

### 4. Administrative & Geographic Gaps

- **[Meeting Note]** Question on Census Tracts? Community boundaries vs. Administrative units.
    
- **[Search Insight]** Thailand does not use the term "Census Tract" in the US sense. Instead, the **National Statistical Office (NSO)** uses **Enumeration Districts (ED)**.
    
    - **Administrative Hierarchy:** Province (Changwat) → District (Amphoe) → Sub-district (Tambon) → Village (Muban).
        
    - **The Gap:** There is often no official GIS boundary for "Urban Communities" that sit inside a Tambon but aren't a traditional "Village." DPT is filling this gap now.
        

---

### Key Technical Terms Clarified

- **L&D (Loss and Damage):** In the UN/Climate context, this refers to impacts that cannot be avoided by adaptation. In the meeting, this likely refers to the **Post-Disaster Needs Assessment (PDNA)** used to trigger government budgets.
    
- **Cascading Impacts:** The meeting noted a "misunderstanding" of this. An example would be: **Heatwave** (Primary) → **Drought** (Secondary) → **Crop Failure/Electricity Grid Strain** (Cascading) → **Economic Loss** (Result).
    

>[!comment] Questions regarding data confidentiality
>- ADPC sent official paper letters to potential data providers and they send back static files. Very few provide APIs
>- A participant ask if the data shown on the platform will be make downloadable. . This links to [[Data_Classification_Policy]]. The datasets of this project can be the first application of this policy.
>- In short-term, confidential datasets could be linked via GDX while other datasets can be done through data cataloging and open data gov
