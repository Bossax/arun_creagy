---
status: evergreen
tags:
  - hydrophone-mooring
  - engineering-design
  - stealth-deployment
  - acoustic-silence
  - theft-deterrence
created: 2026-02-08
last_updated: 2026-02-11
AI_prompt: false
AI_output: true
project: "[[DMCR Marine Soundscape Project]]"
type: artifact
---
**Project Duration:** 4 Months (Monthly Service Intervals) **Depth:** Shallow Water (~6 Meters) **Equipment:** SoundTrap ST600 HF

## 1. Executive Summary

The design originated as a traditional surface-buoy mooring system featuring a rigid stainless steel cage, following standard oceanographic deployment protocols. However, a critical review of the operational environment revealed significant flaws regarding security and data integrity. Due to the high risk of theft in accessible shallow waters and the stringent requirement for acoustic silence, the design evolved radically into a "Stealth Subsurface" system. The final concept abandons traditional armoring in favor of a camouflaged PVC tube structure that mimics seabed debris, prioritizing invisibility and acoustic transparency over sheer mechanical hardness. This shift addresses both the human threat (theft) and the scientific requirement (high-fidelity audio) simultaneously.

## 2. Design Evolution Phases

### Phase 1: The Traditional Approach (Initial Concept)

- **Concept:** Based on the initial sketch, the design utilized a high-visibility surface buoy to mark the location, connected to a stainless steel (SS316) protective cage, and anchored by heavy chain and shackles. This represents the "textbook" approach for deep-water moorings.
    
- **Focus:** Mechanical strength, durability against currents, and standard oceanographic recovery practices (pulling the line from the surface).
    
- **Issues Identified:**
    
    - **High Visibility:** A surface marker in 6-meter depth is easily spotted by local fishermen, tourists, or scavengers. It serves as a beacon inviting theft or vandalism.
        
    - **Acoustic Interference:** The use of loose metal shackles and heavy chains creates a high risk of "clanking" or mechanical noise caused by wave action. These impulsive sounds can mask the biological signals the hydrophone is meant to record.
        
    - **Cost Prohibitive:** Fabrication of custom SS316 cages involves high material costs and specialized labor (TIG welding, polishing), consuming a large portion of the budget without guaranteeing safety.
        

### Phase 2: Vulnerability & Acoustic Analysis

- **Shift:** Moved from a **Surface Mooring** to a **Subsurface Mooring** configuration. This involves removing the surface marker entirely, leaving the equipment completely submerged to avoid detection from above.
    
- **Theft Mitigation:** Recognized that physical locks, heavy chains, or armored cages are ineffective against prepared thieves in shallow water, where tools like bolt cutters or saws can be easily deployed. The strategy shifted from "Hardening" (making it hard to break) to "Security through Obscurity" (making it impossible to find).
    
- **Noise Mitigation:** Identified metal-on-metal contact points—specifically the articulation between shackles and eye bolts—as a primary source of high-frequency noise. In shallow water, wave energy keeps these components in constant motion.
    
- **Solution:** Replaced all metal shackles with direct rope knotting (reinforced with hose protection) or heavy-duty cable ties. This eliminates the potential for metallic impact sounds and removes the need for threaded connections that can seize up.
    

### Phase 3: The "Stealth Tube" Concept (Final Design)

- **Concept:** Replaced the expensive, shiny steel cage with a modified PVC pipe structure. The goal is to make the instrument housing look like "marine trash" or a discarded pipe segment.
    
- **Structure:** A "Tube-in-Tube" design. The delicate SoundTrap instrument is suspended inside a larger, perforated PVC pipe using EVA foam rings. This creates a physical separation between the sensor and the outer shell, protecting it from direct impact.
    
- **Camouflage:** The PVC exterior is painted with matte black and olive-drab colors, then distressed to encourage rapid biofouling (algae growth). The intent is for the unit to blend seamlessly with the seabed background within days of deployment.
    
- **Recovery:** A sacrificial cable-tie link allows divers to easily cut the unit free during monthly service intervals using simple side-cutters. This eliminates the struggle with corroded threads or heavy knots underwater, leaving the heavy base anchor undisturbed on the seafloor.
    

## 3. Emerging Requirements

Through the iterative design process, the following critical requirements emerged and solidified:

|Requirement|Description|
|---|---|
|**Acoustic Silence**|The rig must not generate any self-noise (strumming, clanking, creaking). This ruled out metal chains and loose shackles, leading to the use of sound-dampening materials like nylon ropes, rubber hoses, and plastic cable ties which do not resonate or clank.|
|**Vibration Isolation**|The hydrophone sensor is sensitive to structure-borne vibrations. It must not touch the rigid frame directly. **EVA Foam (Shore A 50-60)** was selected to suspend the device inside the housing, acting as a shock absorber and acoustic decoupler.|
|**Theft Deterrence**|The system must be invisible from the surface and visually uninteresting underwater. Camouflage (looking like worthless trash) was deemed more effective than armor, as "trash" does not trigger the curiosity or greed of potential thieves.|
|**Serviceability**|The unit must be retrievable by a single diver every 30 days. Complex mechanical latches were rejected because marine growth (barnacles) can jam mechanisms. "Cut-and-replace" consumables (Cable Ties/Rope) ensure reliability.|
|**Emergency Recovery**|If the unit is accidentally dislodged or floats to the surface, it needs a passive tracking beacon. An **AirTag** (waterproofed in resin/housing) was added to the design to facilitate recovery if the unit washes ashore or is picked up by a boat.|

## 4. Key Decision Points

1. **Material Selection (SS316 vs. PVC):**
    
    - _Decision:_ Switch from Stainless Steel to PVC.
        
    - _Reason:_ PVC is acoustically transparent (especially when perforated), allowing sound waves to pass through with minimal reflection compared to steel. It is also inexpensive, non-magnetic, and importantly, has zero scrap metal value to thieves, reducing the incentive for theft.
        
2. **Buoyancy Strategy:**
    
    - _Decision:_ Use off-the-shelf hard plastic fishing floats or simple PU foam, rather than expensive engineered foam (e.g., Divinycell).
        
    - _Reason:_ For shallow water depths (<10m), the compression resistance of high-end foam is unnecessary. Standard fishing floats are readily available, durable enough for the pressure, and cost-effective.
        
3. **Connection Hardware:**
    
    - _Decision:_ Eliminate metal shackles entirely.
        
    - _Reason:_ Threaded shackles often suffer from "galling" or seizing due to corrosion and biofouling after a month in saltwater, making underwater removal difficult. Furthermore, eliminating them removes the primary source of metallic clanking noise.
        
4. **Budgeting Strategy:**
    
    - _Decision:_ Base the grant funding request on the **Stainless Steel** option (~20,000 THB).
        
    - _Reason:_ To ensure a financial safety net (Worst-case scenario funding). This approach secures sufficient funds to cover the high-end option if necessary. If the cheaper PVC design is implemented as planned, the surplus funds can be reallocated to critical spares, high-capacity batteries, or boat charter costs for recovery.
        

## 5. Final Hardware List (Per Unit)

- **Housing:** 3-4 inch PVC Pipe, perforated to allow water flow and sound passage, painted with non-toxic camo patterns.
    
- **Internal Mount:** EVA Foam rings (Shore A 55) utilized as suspension bumpers to center the SoundTrap and absorb shock.
    
- **Tracker:** Apple AirTag (Resin sealed/Waterproofed) hidden in the bottom cap of the tube, protected by foam padding.
    
- **Mooring Line:** Nylon rope protected by a sheath of garden hose. The hose acts as armor against accidental cuts and prevents the rope from chafing against the anchor.
    
- **Base:** Concrete block (40-50kg wet weight) cast with a Stainless Wire loop (1m) extending from the bottom. The wire loop prevents thieves from easily cutting the line at the base level.
    
- **Linkage:** Heavy-duty Cable Ties used as the primary connection point between the mooring line and the housing. They serve as a secure but easily cut "sacrificial link" for quick recovery.