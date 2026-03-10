---
status: raw
tags: []
created: 2026-02-04
last_updated: 2026-02-04
AI_prompt: false
AI_output: true
project:
  - DCCE_CRDB
type:
  - ai_output
---

The imperative to develop a standardized Climate Risk Common Data Model (CDM) arises from the increasing complexity of "Hybrid Risk" assessments, which seek to unify probabilistic physical simulations with indicative heuristic indices. In the contemporary risk management landscape, the integrity of such models is often compromised by semantic drift, the conflation of raw data with derived metrics, and an inability to audit the judgment-based transitions from evidence to assessment. To resolve these challenges, this report provides an exhaustive benchmarking of the proposed Hybrid Risk Data Model against international standards for statistical metadata exchange (ISO 17369), foundational ontologies (UFO and CCO), disaster risk data dictionaries (Oasis OED, UNDRR Sendai, ISO 31010), and provenance tracking (W3C PROV-O). The objective is to validate a conceptual architecture that ensures semantic consistency across disjoint lineage paths while guaranteeing a strict, auditable separation between factual evidence and professional judgment.

# Phase 1: Structural Integrity in Indicator Modeling—The SDMX and GSBPM Standards

The foundational challenge in climate risk modeling lies in the "Indicator Integrity Standard," which requires a rigorous definition of metrics to ensure they are comparable across time, geography, and diverse data producers. The Statistical Data and Metadata eXchange (SDMX) Information Model, codified as ISO 17369, provides the definitive framework for this task.[1, 2] Central to SDMX is the principle that statistical data must be accompanied by comprehensive metadata that defines its structure, meaning, and validity constraints.[3, 4]

## The Information Model and Data Structure Definitions

In the SDMX paradigm, a dataset is not merely a collection of numbers but an organized set of observations structured according to a Data Structure Definition (DSD).[3, 5] The DSD acts as the architectural blueprint for the "Indicative Risk Domain," enforcing a strict hierarchy between concepts, code lists, and observations. Integrity is maintained by ensuring that every observation is unambiguously identified by its "dimensions"—the coordinates that locate it in a multi-dimensional space.[5, 6]

Dimensions serve a role analogous to primary keys in relational database systems. For a climate risk indicator, mandatory dimensions include the Indicator identifier (INDICATOR), the reference area (REF_AREA), and the time period (TIME_PERIOD).[5, 7] When these three are known, an observation can be uniquely retrieved and validated against its peers.[6] Beyond identification, SDMX distinguishes "attributes," which provide descriptive context—such as the "Observation Status" (OBS_STATUS) or "Unit of Measure" (UNIT_MEASURE)—without altering the identity of the data point.[4, 7] This structural separation is vital for a hybrid CDM because it allows the "Evidence Source" (the origin of the raw data) to be modeled as an attribute or a separate metadata object, ensuring that the "Indicator Definition" (the semantic meaning of the metric) remains consistent regardless of the source.

|SDMX Structural Component|Primary Function in Climate Risk CDM|Mandatory Requirement for Validity|
|---|---|---|
|**Dimension**|Uniquely identifies an observation within a dataset.|Every DSD must include at least one time dimension and one reference area.|
|**Attribute**|Provides qualitative metadata about the observation.|Mandatory attributes for SDGs include `UNIT_MEASURE`, `UNIT_MULT`, and `OBS_STATUS`.|
|**Primary Measure**|Represents the actual value being transmitted.|Typically denoted as `OBS_VALUE`, must adhere to a specified data type (e.g., Float).|
|**Concept Scheme**|Groups and manages the semantics of dimensions/attributes.|All concepts used in a DSD must belong to a maintainable Concept Scheme.|
|**Code List**|Enumerates the valid universe of values for a concept.|Dimensions must be coded or have a fixed format; free text is prohibited for identification.|

The SDMX 3.0 information model further enhances this by introducing "Metadata Structure Definitions" (MSD) and "Dataflows".[8] Benchmarking the proposed model against the SDMX pattern reveals that separating "Raw Data" from "Indicator Definition" is not just a preference but a compliance requirement for global interoperability. In SDMX, the Dataflow represents the "what" (the collection of indicators), while the DSD represents the "how" (the technical structure).[8] This decoupling allows a single indicator definition (e.g., "Annual Mean Temperature Change") to be applied to multiple dataflows originating from different evidence sources (e.g., satellite telemetry vs. ground stations) while maintaining identical semantic structures.

## Compliance with the Generic Statistical Business Process Model

The requirement for this structural separation is further reinforced by the Generic Statistical Business Process Model (GSBPM). GSBPM describes the set of activities involved in producing statistics through eight distinct phases: Specify Needs, Design, Build, Collect, Process, Analyse, Disseminate, and Evaluate.[9, 10] Within the "Design" phase, sub-process 2.2 explicitly focuses on "Design variable descriptions," which involves aligning concepts with existing standards.[9] This occurs _before_ any data is collected, proving that the semantic definition of a risk indicator is a prerequisite for, and independent of, the raw evidence used to populate it.

The GSBPM also emphasizes "Metadata Management" as an overarching process that describes the inputs, outputs, and steps used in each iteration.[11] For the hybrid risk CDM, this implies that the lineage from a "Source Dataset" (Evidence) to a "Risk Score" (Indicator) must be mediated by a transformation process where the structural metadata remains invariant. The transition from Phase 5 (Process) to Phase 6 (Analyse) in GSBPM is where the "raw data" is integrated, classified, and cleaned, effectively transforming it into the "indicator" that conforms to the DSD.[9, 12]

# Phase 2: Semantic Integrity and the Problem of Methodological Polymorphism

The second phase of the benchmark addresses the semantic risks associated with mixed methodologies. A "Risk" derived from a physics-based simulation (e.g., a hydrodynamic model) and a "Risk" derived from a heuristic index (e.g., a community vulnerability survey) often share the same label but possess disjoint lineage paths. Solving this "Polymorphism" risk requires a foundational ontology that can distinguish between these paths without breaking the definition of the parent entity.

## Risk as a Disposition in the Unified Foundational Ontology

The Unified Foundational Ontology (UFO) provides a rigorous framework for clarifying these concepts. UFO distinguishes between "Endurants" (objects that exist fully in time) and "Events" (perdurants that have temporal parts).[13] Within this ontology, "Risk" is most accurately modeled as a "Disposition".[13, 14] A disposition is a "Realizable Entity" that inheres in an object (the bearer) and is causally explanatory of its potential manifestations.[13]

For instance, the "Flood Risk" of a physical asset is a disposition. It exists whether or not a flood occurs. A flood event is the "manifestation" of that disposition, which is triggered by a specific event (e.g., heavy rainfall) under certain conditions.[13] This distinction is critical for the hybrid CDM: it allows the model to categorize risk not just as a probability value, but as an inherent property of the system.

The "Common Ontology of Value and Risk" (COVER), which extends UFO, further unpacks risk into three constituent components: a Threat Event, a Vulnerability, and an Impact.[15, 16]

• **Threat Event:** A potential event that can trigger a loss (e.g., a heatwave).

• **Vulnerability:** A disposition to be harmed by a specific threat (e.g., the sensitivity of a power grid to heat).

• **Impact:** A loss event relative to a specific goal (e.g., a blackout).[15]

|Ontological Concept|UFO/CCO Definition|Application to Climate Risk|
|---|---|---|
|**Object (Bearer)**|An existentially independent endurant.|The physical building or population center at risk.|
|**Disposition**|An internally grounded realizable entity.|The structural fragility of the asset.|
|**Role**|An externally grounded realizable entity.|The designation of an asset as "Essential Service."|
|**Event (Manifestation)**|A perdurant triggered by a disposition.|The actual occurrence of a disaster or failure.|
|**Truth Maker**|Aspects of reality that confer truth.|The physical state (e.g., water level) that validates a risk score.|

## Design Patterns for Disjoint Lineage Paths

The primary challenge in a hybrid model is ensuring that the "Risk Score" entity can accommodate different sources of truth. The Common Core Ontology (CCO) and the MEVIR framework provide a solution through the concepts of "Truth Bearers" and "Truth Makers".[15, 17] A risk score is a "Truth Bearer"—a symbolic representation (e.g., a data entry in a database). The "Truth Maker" is the aspect of reality that makes that score true.[15]

The disjoint lineage paths can be modeled using specific design patterns in CCO:

1. **Physics-Based Path:** This path is grounded in "Causal Laws." It links a triggering event type to a resulting event type via a disposition that is "internally grounded" in the bearer.[13, 14] The lineage follows a chain of physical causality: Asset Physical Properties → Disposition → Simulation Activity → Risk Score.

2. **Heuristic-Based Path:** This path is grounded in "Information Content Entities" and "Assessment Activities".[18] The risk is often derived from "Roles" or "Attributes" that are "externally grounded"—meaning they depend on the context or the judgment of an agent rather than just physical change.[14] The lineage follows: Survey/Expert Activity → Information Entity → Assessment Activity → Risk Score.

By utilizing the CCO's "Information Entity Ontology" and "Event Ontology," these two lineages are maintained as separate branches that converge on the same "Risk Score" entity.[18] The "parent entity" definition of Risk remains a realizable entity (a disposition), but its "lineage" attribute distinguishes between physics-based manifestations and heuristic-based assessments. This prevents the circular logic of treating a qualitative index as a physical law while allowing them to be stored in the same domain.

# Phase 3: Domain Scoping—Consensus Terminology for Assets, Population, and Vulnerability

The third phase of the benchmarking process focuses on scoping the "Impact" domain based on global standards to prevent ambiguity. A comparative analysis of the data dictionaries for UNDRR (Sendai), the Oasis Loss Modelling Framework (OED), and ISO 31010 reveals a consensus on the "Minimum Viable Entities" (MVE) required for a complete domain model.

Comparative Data Dictionary Analysis

The Oasis Open Exposure Data (OED) standard is widely recognized as the industry benchmark for catastrophe risk modeling.[19, 20] OED focuses heavily on "Property" exposure, organized into four primary files: Location (`loc`), Account (`acc`), Reinsurance Info (`RIinfo`), and Reinsurance Scope (`RIscope`).[20] Conversely, the UNDRR DesInventar Sendai framework focuses on disaster losses and statistics, emphasizing human impact and socio-economic variables.[21, 22]

|Data Domain|Oasis OED Terminology|UNDRR Sendai Terminology|Consensus CDM Entity (MVE)|
|---|---|---|---|
|**Assets**|Building TIV, Contents TIV, Other TIV.|Physical Damage, Economic Loss.|`Asset_Exposed_Value`|
|**Population**|N/A (Financial focus).|Mortality, Missing, Affected.|`Population_At_Risk`|
|**Vulnerability**|OccupancyCode, ConstructionCode.|Vulnerability/Fragility Functions.|`Vulnerability_Function`|
|**Geography**|CountryCode, Lat/Long.|Admin Levels 0, 1, 2.|`Geospatial_Reference`|

The "Minimum Viable Entities" for the Impact domain are those necessary to quantify loss. In OED, the `Location` file is the only mandatory file required to generate ground-up losses.[20] The MVE list includes:

• **LocNumber:** Unique identifier for the asset or location.

• **Geographical Coordinates:** Accurate latitude and longitude.

• **Occupancy and Construction Codes:** Essential for determining the vulnerability of the structure.[19, 20]

• **Total Insured Value (TIV):** The financial exposure of the asset.[20]

For the population domain, the UNDRR standards require disaggregated data by age and sex to ensure that the "Vulnerability" metric accounts for demographic sensitivities.[7, 21] Benchmarking against ISO 31010 confirms that vulnerability should be scoped as a relationship between a hazard intensity and an expected loss, rather than a fixed attribute of the asset.

## Scoping the Vulnerability Domain

A common error in risk CDM development is treating "Vulnerability" as a static score (e.g., "High"). Rigorous standards like OED and ISO 31010 treat vulnerability as a "Function" or "Fragility Curve".[23] The OED schema allows for "Secondary Modifiers"—specific details such as roof type or basement presence—which adjust the core vulnerability function of an asset.[20, 24] To consider the "Vulnerability" domain complete, the CDM must move beyond qualitative labels and include a mechanism to map hazard intensity (e.g., wind speed in m/s) to damage ratios (0.0 to 1.0).[23]

# Phase 4: Provenance and Auditability—Tracing Judgment to Evidence

The final requirement for the Climate Risk CDM is to prevent circular logic by strictly separating "Evidence" from "Assessment." The W3C PROV-O (Provenance Ontology) provides the standard topological pattern for this auditability. Provenance is defined as information about the entities, activities, and agents involved in producing a piece of data.[25, 26]

The PROV-O Topological Pattern

The PROV-O model is centered on a core triplet: **Entity**, **Activity**, and **Agent**.[27, 28] In the context of risk assessment, the "Best Practice" pattern for auditability follows this chain:

1. **Source Entity (Evidence):** The raw dataset (e.g., a LIDAR elevation map).

2. **Assessment Activity (The Judgment):** The process of calculating risk (e.g., a flood depth analysis).

3. **Output Entity (Risk Score):** The resulting indicator.

4. **Agent:** The modeler or the software engine that performed the calculation.[27]

The critical relationship that guarantees auditability is the distinction between `prov:used` and `prov:wasGeneratedBy`.[27, 29]

• The **Assessment Activity** _used_ the **Source Entity**.

• The **Risk Score** _wasGeneratedBy_ the **Assessment Activity**.

• The **Risk Score** _wasDerivedFrom_ the **Source Entity** (a direct lineage shortcut).[26, 29]

|PROV-O Relationship|Semantic Role in Risk CDM|Audit Function|
|---|---|---|
|`prov:used`|Connects an Activity to its input data.|Identifies exactly which evidence supported a judgment.|
|`prov:wasGeneratedBy`|Connects a Result to the process that created it.|Proves that a score did not "appear" but was calculated.|
|`prov:wasAssociatedWith`|Connects an Activity to an Agent.|Attributes responsibility to a person or algorithm version.|
|`prov:startedAtTime`|Records when the assessment began.|Prevents using future data to justify past scores.|
|`prov:wasDerivedFrom`|Links an Output directly to its Input.|Allows a "trace back" from high-level score to raw data.|

Preventing Circular Logic and Ensuring Traceability

Auditability is compromised when the "Assessment" becomes indistinguishable from the "Fact." PROV-O prevents this by requiring that an "Activity" be a process with a temporal start and end.[26] This means that the "judgment" is captured as a discrete event in time. If a risk score is updated, a new "Activity" is recorded, creating a versioned lineage.[25, 30]

The "Best Practice" ER diagram for a risk CDM must include a join entity between `Entity` and `Activity` that carries "Role" metadata. For example, a dataset might be used in the "Role" of a "Calibration Set" or a "Validation Set." This prevents circularity by ensuring that the data used to train a risk model is not the same data used to evaluate its performance. The use of "Qualified Usages" in PROV-O allows the CDM to record exactly _how_ a specific evidence entity influenced a risk score.[29]

Synthesis and Recommendations for CDM Integrity

The benchmarking of the Climate Risk CDM against international standards demonstrates that semantic and structural integrity are achieved through the strict application of layered modeling. The separation of "Evidence" (Factual Data) from "Indicator" (Structured Metadata) and "Assessment" (Provenance) creates a multi-dimensional safeguard against the most common failures in risk modeling.

Core Integrity Principles for CDM Implementation

The first principle, derived from SDMX and GSBPM, is the **Separation of Structure and Data**. The CDM must maintain a central registry of Data Structure Definitions (DSDs) that define the "shape" of risk indicators independently of the "Evidence Sources" that populate them.[1, 8] This ensures that a "Heat Risk Score" is semantically identical whether it is derived from a satellite or a ground sensor.

The second principle, based on UFO and CCO, is the **Explicit Typing of Lineage**. To handle the polymorphism of hybrid risk, the model must differentiate between risk as a "Disposition" (physics-based) and risk as a "Claim" (heuristic-based).[13, 15] This allows for the integration of mixed methodologies into a single repository without conflating their underlying logic.

The third principle, extracted from OED and Sendai, is the **Minimum Viable Impact Scope**. A risk CDM is only complete if it encompasses Assets (Financial Value), Population (Human Count), and Vulnerability (Mathematical Functions).[20, 23] Scoping "Vulnerability" as a function of hazard intensity, rather than a static label, is the primary defense against ambiguity.

The final principle, enforced by W3C PROV-O, is **Chain-of-Evidence Traceability**. Every value in the CDM must be an entity that can be traced back through an "Assessment Activity" to a "Used Entity" (the evidence).[27, 29] This topological pattern ensures that every judgment-based transition is visible to auditors and users, preventing the "black box" syndrome common in complex climate models.

By adhering to these standards, the Climate Risk CDM establishes a robust, auditable, and semantically consistent infrastructure. This framework allows for the unification of diverse methodologies into a "Hybrid Risk Data Model" that can withstand the rigors of international compliance, scientific peer review, and strategic decision-making in an increasingly volatile climate future.[31] The transition from "Ad-Hoc Data" to "Standardized Information" is not merely a technical upgrade but a compliance requirement for the modern era of risk management.[1]