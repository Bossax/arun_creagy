---
type: literature
status: evergreen
tags: []
source: https://www.tandfonline.com/doi/epdf/10.1080/02626667.2010.489281?needAccess=true
authors: []
year: ""
relevance_to: "[[]]"
key_findings: []
sticker: emoji//1f4f0
---
# Definitions

## Floods

The sources define a ==**flood** as a rise in the water level of a stream to a peak, followed by a slower recession==. From a data modeling perspective, ==a flood is a magnitude parameter specifically referring to **streams** and river discharge==. The European Directive on the Assessment and Management of Flood Risks fundamentally links flood probabilities to the return periods of annual river discharge maxima or peak-over-threshold series. ==However, the sources note that river discharge alone may not accurately reflect the true magnitude of an event==, particularly in Arctic or sub-Arctic basins where ice formations disturb flow conditions.

### Inundations

In contrast to floods, ==**inundations** characterize the **exposure of areas** to water, regardless of the water's provenance.== Key attributes for this entity include:

- **Spatial Grip:** The extent and boundaries of the water on the land.
- **Polygenic Nature:** Inundations are often "polygenic," meaning they are a compound of multiple sources such as river floods, marine submergences, and pluvial (rain-related) inundations.
- **Susceptibility:** This refers to the empirical likelihood of a specific area being flooded, based on the spatial aggregation of past events rather than just stream discharge values.

# Hazard
The sources discuss **hazard** through the following frameworks and data entities:

## 1. Inundation Hazard Mapping

The sources note that the European Directive on the Assessment and Management of Flood Risks defines **i==nundation hazard maps** based on flood probabilities==. These probabilities are typically derived from return periods of annual river discharge maxima or peak-over-threshold series. However, the sources argue that this standard model is often ineffective for mapping flood hazards in regions like the lower Ölfusá basin because discharge does not consistently reflect the spatial extent of the hazard, particularly during ice-jamming events.

### 2. Susceptibility to Flooding

 **Susceptibility to flooding** serves as a core attribute for assessing hazard. This is defined as the empirical likelihood of a specific area being inundated, based on the spatial aggregation of past events rather than just stream discharge values.

- **Likelihood Calculation:** Each surface unit (represented in the sources by a 250 x 250 m grid) is assigned a "likelihood of flooding".
- **Empirical Return Period:** This is calculated by dividing the total duration of the study period by the number of substantiated flooding events for that specific grid square.

### 3. Hazard Magnitude Parameters

When modeling the magnitude of a hazard event, the sources suggest that **inundation extent** (spatial grip) is a more reliable parameter than river discharge.

- **Discharge vs. Extent:** In 60% of analyzed cases involving ice jams, relying solely on discharge led to a clear underestimation of the hazard extent.
- **Polygenic Hazard:** A comprehensive hazard model must account for "polygenic" events—compounds of river floods, marine submergences, and pluvial inundations—which a discharge-only methodology cannot easily combine.

### 4. Hazard, Risk and Exposure

The sources link hazard directly to **risk management**, particularly in districts with concentrated urban populations. ==The "hazard itself" is characterized by the overall magnitude and spatial range of inundation, which must be distinguished from the "impact"== (local destruction or disruptions). For data modeling purposes, the hazard represents the physical threat (likelihood and extent), while exposure refers to the settlement areas and territories located within the delineated **flood plain**.