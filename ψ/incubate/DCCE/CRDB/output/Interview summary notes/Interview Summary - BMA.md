**Date:** 6/3/2569 (March 6, 2026)

**Interviewee Name/Title:** Multi-office Bangkok Metropolitan Administration (BMA) team, including representatives from the Drainage and Sewerage Department and the Environment Department; named speakers captured in the transcript include Prathan Banchong, Dechchat Phakdiphan, Theerapat Tangprapruttikul, Ritsara Phocharoen, and Anan Kaosaiphan.

**Department:** Drainage and Sewerage Department; Environment Department

**Agency:** Bangkok Metropolitan Administration (BMA / กรุงเทพมหานคร)

### 1. Role and Responsibility of the Agency

- **Key duty and roles:** BMA acts as the primary urban operator for Bangkok’s climate-related frontline management. In this interview, the clearest operational responsibilities were urban flood management, drainage infrastructure operation, heat-risk management, and environmental monitoring at city scale.

- **Institutional role in climate adaptation:** BMA is not only a user of climate-risk information, but also a producer of city-scale operational data. Its role spans immediate response (rainfall, flooding, pumping, drainage, cooling shelters) and medium- to long-term planning for urban resilience investments.

- **Associated legal or policy frameworks:** No single legal framework was emphasized in the interview, but the discussion repeatedly referenced city policy direction under the Bangkok Governor, inter-agency water coordination mechanisms, and BMA’s newly approved heat-management plan for 2026.

### 2. Highlighted Key Projects

- **Bangkok flood and drainage system operations and expansion:**

    - _Status & Scope:_ Active and ongoing. BMA described a large-scale drainage system composed of radar, rainfall monitoring, road-flood monitoring, canals, pumping stations, gates, monkey-cheek retention areas, and major drainage tunnels.

    - _Core assets highlighted in the interview:_ Approximately 6,800 km of drainage pipes, about 2,700 km of canals, major pumping and gate infrastructure, 4 operating drainage tunnels, and additional tunnels under construction.

    - _Strategic direction:_ BMA is continuing to strengthen both routine maintenance (e.g., canal and drain clearing) and major structural upgrades because extreme rainfall intensity now exceeds older drainage design assumptions.

- **Heat management plan for Bangkok (2026):**

    - _Status & Scope:_ Recently approved and being implemented. BMA reported that the city has established a heat-management committee chaired at deputy-governor level and adopted a formal heat-management plan.

    - _Current measures:_ 255 designated cooling rooms, with an expansion effort toward broader “cooling points” in parks, public facilities, and possibly temples.

    - _Future lifecycle:_ BMA is working with the World Bank on a microclimate data platform for localized heat forecasting and early warning.

- **Urban water retention / “sponge city” and monkey-cheek measures:**

    - _Status & Scope:_ Active. BMA described retention areas, monkey cheeks, and related measures as part of the city’s strategy for handling excess rainfall when drainage conveyance alone is insufficient.

    - _Operational logic:_ Water is temporarily stored and later released once the drainage system regains available capacity.

### 3. Current Workflow & Data Usage

- **Hazard scope:** BMA is currently working across several climate-related hazards, with the strongest operational maturity in flood management. The interview also surfaced growing attention to heat stress, rain bombs / highly localized extreme rainfall, tidal backflow, salinity, and—through the Environment Department—air-quality management.

- **BMA-generated operational data:** BMA stated that it collects its own rainfall measurements, canal water levels, road-flood monitoring data, weather-station observations, and radar data. It also operates air-quality monitoring stations and uses those measurements to derive heat index values for public warning.

- **External data dependencies:** BMA integrates or manually pulls data from multiple agencies, including the Thai Meteorological Department (TMD), the Hydro-Informatics Institute / relevant national water-information systems, Chao Phraya basin information sources, and Royal Thai Navy tide-related data.

- **Short-term flood operations:** The city uses near-real-time monitoring and short lead-time forecasts—such as 1-hour and 3-hour forecasts—to trigger operational decisions. The focus is on rainfall intensity, canal levels, upstream water conditions, tide conditions, and system capacity.

- **Medium- and long-term water planning:** BMA does not manage Bangkok’s flood system in isolation. It coordinates with RID, TMD, ONWR/related national water-planning bodies, and Chao Phraya basin committees to track upstream releases, floodway decisions, and regional water-routing plans that affect Bangkok.

- **Heat workflow:** For heat management, BMA currently uses heat index derived from city monitoring stations and relies on the declared heat-season window to activate short-term public measures such as cooling rooms and communications.

### 4. Climate Data Needs & Gaps

- **Automated data exchange remains weak:** A major gap is the lack of seamless API-based data exchange with upstream and partner agencies. BMA described cases where staff still need to manually check external websites for river or basin conditions rather than receiving structured machine-readable feeds.

- **Localized extreme-rainfall forecasting gap:** BMA needs better predictive capability for highly localized “rain bomb” events. The discussion suggests that existing forecasting is still too weak at the fine urban scale needed for operational urban flood management.

- **Urban climate / heat analytics gap:** Heat management is newer and less mature than flood management. BMA has started operating with heat index, but the interview shows broader unanswered needs around urban heat-island behavior, localized heat-dome conditions, airflow, and other variables that shape real street-level heat exposure.

- **Integrated infrastructure-capacity analytics gap:** The conversation highlighted interest in more advanced tools for estimating localized water-storage and drainage capacity—such as area-by-area absorption or overflow behavior—rather than relying only on broad system descriptions.

- **Emerging water-quality and salinity concerns:** BMA noted that rising heat and hydrological shifts can worsen water-quality issues, salinity, and odor / biochemical conditions in urban water systems, but these areas appear less systematized than flood operations.

### 5. Next Steps & CRDB Integration

- **Map to implementation plan:** BMA strongly validates the need for a platform that serves both operational users and strategic planners. For CRDB, this means the future architecture should not only catalog data sources, but also support near-real-time interoperability, metadata clarity, and role-specific service design.

- **Seed use cases for WP3 Conceptual Data Model (CDM):**

    - _Scenario 1:_ “Integrating BMA rainfall, canal, pump, and flood-sensor data with upstream basin and tidal data to support short-term flood operations and event response.”

    - _Scenario 2:_ “Combining BMA heat-index monitoring, cooling-point locations, and future microclimate forecasting to target urban heat-risk interventions at district and neighborhood scale.”

    - _Scenario 3:_ “Linking drainage-infrastructure geometry, storage assets, and city hydrology to estimate localized runoff-handling capacity and identify priority upgrade zones.”

- **Design implications for CRDB / NCAIF:** BMA’s case reinforces the need for tiered services: raw and interoperable machine-readable data for technical operators, plus simplified dashboards, maps, and decision-ready indicators for managers and policy teams.

- **Planned participation:** The interview indicates that BMA is an important stakeholder for the upcoming workshop and feedback process, especially for water operations, urban heat management, and practical data-exchange design.
