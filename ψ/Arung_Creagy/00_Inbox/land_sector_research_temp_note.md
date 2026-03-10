---
status: raw
tags:
  - land_sector
  - NotebookLM
created: 2026-03-04
last_updated: 2026-03-04
AI_prompt: false
AI_output: true
project:
type: note
---
# **Prompt 1 — IPCC AFOLU definitions** From IPCC 2006 Vol4 (AFOLU) and IPCC 2019 Refinement Vol4, extract the formal definitions of **Forest Land** and **Cropland/Agricultural Land**. Include thresholds (minimum area, minimum tree height, canopy cover) and clarify land-use vs land-cover. Provide citations with source + section/page.

**Land-Use vs. Land-Cover** According to Volume 4, Chapter 3, Section 3.2 of the IPCC 2019 Refinement, the terms "land-cover" and "land-use" are not interchangeable.

- **Land cover** refers to the **biophysical coverage of land**, such as bare soil, rocks, forests, buildings and roads, or lakes.
- **Land-use** refers to the **socioeconomic use** that is made of the land, such as agriculture, commerce, residential use, or recreation.

The definitions of land-use categories can incorporate management options and establish predominance when a single unit of land is subject to multiple uses. Distinguishing between the two is vital because inferring land-use strictly from land cover at a specific point in time can lead to misclassification. Proper attribution—associating observed land cover and cover changes with underlying socioeconomic land-use and disturbance types—is required to accurately estimate greenhouse gas (GHG) emissions and removals.

**Forest Land Definition and Thresholds** IPCC 2006 Vol 4

- **Formal Definition:** Outlined in Chapter 3, Section 3.2, Forest Land includes **all land with woody vegetation consistent with thresholds used to define Forest Land in the national greenhouse gas inventory**. It also explicitly includes systems with a vegetation structure that currently fall below the thresholds, but have the potential to reach those threshold values _in situ_ (e.g., newly planted or regrowing trees).
- **Thresholds:** The IPCC guidelines do not mandate a single, strict global numeric threshold; instead, countries set their own specific definitions. However, Box 3.1a specifies that these definitions must use a combination of **minimum canopy cover, minimum height, and minimum area** thresholds. For context on what these parameters look like, the FAO definition of a forest requires an area larger than 0.5 hectares and a forest canopy cover over 10% (Annex 3A.1, Table 3A.1.1). Additionally, the IPCC default biomass tables for Forest Land generally assume a forest definition of at least 10% tree canopy cover (Chapter 4, Table 4.7).
- **Temporary Destocking:** According to Box 3.1a, areas of Forest Land that temporarily fall below the country's structural thresholds due to forest harvesting or other disturbances (like fire or pest attacks) should continue to be reported under Forest Land, provided the loss of cover is temporary.

**Cropland / Agricultural Land Definition and Thresholds**

- **Formal Definition:** Defined in Chapter 3, Section 3.2, Cropland includes **cropped land, including rice fields, and agro-forestry systems where the vegetation structure falls below the thresholds used for the Forest Land category**.
- **Management Practices and Rotations:** As noted in Box 3.1a, this category includes lands managed under opportunistic or rotational cropping, grazing, or fallow practices. Because agricultural land management often fluctuates between cropping-pasture systems and fallows depending on climate and market conditions, countries may either keep reporting these lands under the predominant land use or transfer the lands between categories each reporting year.
- **Woody Crops vs. Forest Land Overlap:** Cropland can contain perennial woody vegetation, including orchards, agroforestry, and other woody crops. If the vegetation structure of these woody crops meets the country's defined thresholds (minimum area, height, canopy cover) for Forest Land, they may meet the definition of Forest Land. Consequently, Cropland specifically captures these woody and agro-forestry systems only when they _fall below_ the country-specific thresholds established for Forest Land.

**Formal Definition of Forest Land and Thresholds**

- **General Definition:** Forest Land includes all land with woody vegetation consistent with the thresholds used to define Forest Land in a country's national greenhouse gas inventory (V4_03_Ch3_Representation.pdf, Section 3.2). It encompasses systems with a vegetation structure that currently fall below these threshold values but have the potential to reach them _in situ_.
- **Thresholds (IPCC Glossary Framework):** The Kyoto Protocol and IPCC glossary framework define a forest as having a **minimum area of 0.05 – 1.0 hectares**, a **tree crown (canopy) cover of more than 10 – 30 percent**, and trees with the potential to reach a **minimum height of 2 – 5 meters** at maturity _in situ_ (V4_04_Ch4_Forest_Land.pdf, Annex 4A.1).
- **FAO Default Thresholds:** When standard FAO forest and land cover classes are used, Forest Land is specifically defined as land spanning **more than 0.5 hectares** with trees **higher than 5 meters** and a **canopy cover of more than 10 percent** (V4_04_Ch4_Forest_Land.pdf, Table 4.2).

**Formal Definition of Cropland**

- **General Definition:** Cropland includes arable and tillable land, rice fields, and agro-forestry systems where the vegetation structure falls below the thresholds used for the Forest Land category and is not expected to exceed those thresholds at a later time (V4_03_Ch3_Representation.pdf, Section 3.2; V4_05_Ch5_Cropland.pdf, Section 5.1).
- **Included Systems:** It encompasses all annual and perennial crops, as well as temporary fallow land (land set at rest for one or several years before cultivation resumes) (V4_05_Ch5_Cropland.pdf, Section 5.1). Perennial crops include trees and shrubs grown in combination with herbaceous crops, or as orchards, vineyards, and plantations (e.g., cocoa, coffee, oil palm, coconut, rubber trees, and bananas), provided these lands do not meet the criteria to be categorized as Forest Land. It also includes arable land temporarily used for forage crops or grazing as part of an annual crop-pasture rotation.

**Clarification: Land-Use vs. Land-Cover** The IPCC guidelines highlight that land-use categories may incorporate pure land cover type, functional land use, or a combination of both, which requires careful distinction:

- **Inferring Use from Cover:** The guidelines explicitly warn that care must be taken when inferring land _use_ solely from land _cover_ characteristics, and vice versa (V4_03_Ch3_Representation.pdf, Section 3.2). For example, a land cover consisting of scattered trees might look like a forest, but if its primary use is grazing or firewood collection, it may actually be a functional Grassland.
- **Predominant Functional Use Overrides Cover:** Forest Land is determined not just by the presence of tree cover, but also by the _absence of other predominant land uses_ (V4_04_Ch4_Forest_Land.pdf, Table 4.2). If land with tree cover is predominantly under agricultural production systems (e.g., fruit orchards, palm plantations, or agroforestry systems), the agricultural land _use_ overrides the tree land _cover_, meaning it is excluded from Forest Land and classified as Cropland (V4_04_Ch4_Forest_Land.pdf, Table 4.2).
- **Mapping Resolution Discrepancies:** Conflicts between land use and land cover can also arise from mapping scales. If a country's land-use mapping resolution is coarse (e.g., 5-hectare minimum units) but its Forest Land definition uses a 1-hectare threshold, small pockets of one land use may be physically covered by another but reported incorrectly unless mapping units are reconciled (V4_03_Ch3_Representation.pdf, Section 3.2).
- **Double-Counting Prevention:** To resolve overlaps between cover and use, countries must establish clear, harmonized definitions to ensure that a specific parcel of land is accounted for in only one category (e.g., ensuring woodland on farms is not double-counted in both forestry and agriculture datasets) (V4_03_Ch3_Representation.pdf, Section 3.3.2).
# **Prompt 2 — Land-use categories + managed land** Summarize IPCC guidance on land-use categories (Forest Land, Cropland, Grassland, Wetlands, Settlements, Other Land) and how **managed land** is treated. Cite sections/pages.
*IPCC 2019*
**Treatment of Managed vs. Unmanaged Land** Under the IPCC guidelines (Volume 4, Chapter 1, Section 1.1), greenhouse gas (GHG) inventories use the **Managed Land Proxy (MLP)** to estimate anthropogenic emissions and removals.

- **Managed land** is defined as land where human interventions and practices have been applied to perform production, ecological, or social functions. All direct, human-induced effects on GHG emissions and removals are considered to occur exclusively on managed lands.
- **Unmanaged land** does not require emissions and removals reporting. However, countries are encouraged to track the area of unmanaged land so that total national area accounting remains consistent when land-use changes occur (e.g., when unmanaged land is converted to a managed use).

Because the MLP captures all emissions on managed land—including those from natural disturbances like wildfires or insect outbreaks—countries may optionally disaggregate their reporting on managed lands to separate human-caused effects from natural disturbance effects (Volume 4, Chapter 1, Section 1.4; Chapter 2, Section 2.6).

**The Six IPCC Land-Use Categories** To consistently represent land and prevent double-counting or omissions, Volume 4, Chapter 3, Section 3.2 defines six broad land-use categories. Every unit of land in a country must be classified under only one of these categories in a given year:

1. **Forest Land:** Includes all land with woody vegetation that meets the country's specific thresholds (e.g., minimum area, tree height, and canopy cover). It explicitly includes systems where vegetation currently falls below these thresholds but has the potential to reach them _in situ_ (e.g., newly planted forests).
2. **Cropland:** Includes all cropped land (such as rice fields) and agro-forestry systems, provided their vegetation structure falls below the thresholds used to define Forest Land.
3. **Grassland:** Includes rangelands, pasture land, and agricultural/silvi-pastural systems that are not considered Cropland. It also captures wild lands, recreational areas, and systems with woody or herbaceous vegetation that fall below the thresholds of Forest Land.
4. **Wetlands:** Includes areas of peat extraction and land that is covered or saturated by water for all or part of the year, provided it does not fall into Forest Land, Cropland, Grassland, or Settlements. This category is sub-divided into managed wetlands (like reservoirs) and unmanaged wetlands (like natural rivers and lakes).
5. **Settlements:** Comprises all developed land, including human settlements of any size and transportation infrastructure, unless the land is already accounted for under another category (e.g., urban parks might sometimes be classified under Grassland or Forest Land depending on definitions).
6. **Other Land:** A catch-all category that includes bare soil, rock, ice, and all land areas that do not fit into the other five categories. The primary purpose of this category is to ensure that the sum of all categorized land matches the total geographic area of the country. GHG emissions and removals are generally not reported for this category unless land is transitioning into it (e.g., extreme degradation of managed forest or cropland into barren land).

**Sub-categories: Remaining vs. Converted** According to Chapter 1, Section 1.3.1 and Chapter 3, Section 3.2, each of these six categories is further divided into two sub-categories to accurately track carbon stock changes over time:

- **Land remaining in the same category** (e.g., Forest Land Remaining Forest Land, Cropland Remaining Cropland).
- **Land converted to a new category** (e.g., Forest Land converted to Cropland, Grassland converted to Settlements). All carbon stock changes and non-CO2 emissions associated with a land-use transition are reported under the _new_ (end-use) land category.

*IPCC 2006*
**Treatment of Managed vs. Unmanaged Land** The IPCC guidelines use "managed land" as a pragmatic proxy for anthropogenic (human-induced) greenhouse gas (GHG) emissions and removals. The rationale is that all direct human-induced effects on GHG fluxes, and most indirect effects, are concentrated on managed lands.

- **Definition:** Managed land is defined as any land "where human interventions and practices have been applied to perform production, ecological or social functions".
- **Reporting Requirements:** Countries are only required to estimate and report GHG emissions and removals that occur on managed lands,. Emissions and removals on unmanaged lands do not need to be reported.
- **Area Tracking:** Even though emissions from unmanaged lands are not reported, it is good practice for countries to quantify and track the area of unmanaged land over time. This ensures that consistency in national area accounting is maintained as land-use changes occur (e.g., if unmanaged land is cleared and brought under management, it must enter the inventory),. To prevent false carbon stock increases when unmanaged lands are converted to managed lands, historical carbon stock estimates must be recalculated for the complete inventory time-series area,.

**The Six Land-Use Categories** To ensure complete coverage of a country's total land area without omission or double-counting, the IPCC organizes all land into six broad, top-level categories,. National definitions can be used, provided they are applied consistently:

- **Forest Land:** Includes all land with woody vegetation that meets the country's specific thresholds for Forest Land (e.g., minimum area, tree height, and canopy cover). It also includes temporarily unstocked areas (e.g., from harvesting) and systems that currently fall below the thresholds but are expected to reach them _in situ_,.
- **Cropland:** Encompasses arable and tillable land, rice fields, and agro-forestry systems where the vegetation structure falls below the thresholds used for Forest Land,. This includes annual crops, temporary fallow land, and perennial crops like orchards, vineyards, and plantations (e.g., coffee, rubber, oil palm).
- **Grassland:** Includes rangelands, pasture land, wild lands, recreational areas, and silvi-pastural systems that are not considered Cropland. It also covers systems with woody or non-grass vegetation (such as herbs and shrubs) that fall below the thresholds for Forest Land.
- **Wetlands:** Includes land covered or saturated by water for all or part of the year (such as peatlands) and areas of peat extraction, provided they do not fit into the Forest Land, Cropland, Grassland, or Settlements categories. This category includes both managed sub-divisions (e.g., reservoirs) and unmanaged sub-divisions (e.g., natural rivers and lakes).
- **Settlements:** Consists of all developed land, including transportation infrastructure, commercial areas, and human settlements of any size,. It includes the soils, turf grass, gardens, and trees associated with rural and urban residential areas, golf courses, and parks, unless those lands are already accounted for under another category.
- **Other Land:** Includes bare soil, rock, ice, and any other land areas that do not fit into the other five categories. This category serves as a balancing term to ensure that the sum of all identified land areas matches the total national area.

**Land-Use Conversions** To accurately estimate carbon stock changes, each of the six land-use categories is further divided into two subcategories:

1. **Land remaining in the same category** (e.g., Forest Land Remaining Forest Land).
2. **Land converted to a new category** (e.g., Forest Land converted to Cropland).

When a land-use change occurs, the land remains in the "converted" category for a default transition period of 20 years. This period allows time for the carbon pools (especially soil and dead organic matter) to reach a new equilibrium before the land is eventually transferred into the "remaining" category for that land use,.
# **Prompt 3 — UNFCCC Decision 24/CP.19 forest definition** From UNFCCC Decision 24/CP.19, extract any forest definition parameters and flexibility for national definitions (threshold ranges for area, height, canopy cover). Provide citations.

The provided text for **UNFCCC Decision 24/CP.19 does not contain specific forest definition parameters** or numerical threshold ranges for area, height, or canopy cover.

Instead of dictating these specific thresholds, the decision requires Annex I Parties to provide their own **"Land-use definitions and the classification systems used"** and explain how these correspond to the land use, land-use change, and forestry (LULUCF) categories within Chapter 6 of their National Inventory Report.

If you are looking for standard forest definition parameters, they are detailed in the other sources you provided (outside of the UNFCCC decision):

- **FAO Global Forest Resources Assessment 2020:** Defines forest as land spanning **more than 0.5 hectares** with trees **higher than 5 meters** and a **canopy cover of more than 10 percent** (or trees able to reach these thresholds _in situ_),.
- **GHG Protocol Land Sector and Removals Standard:** Notes that forest land must meet a threshold of tree canopy cover and height, citing an IPCC example of at least **0.5 hectares**, a tree canopy cover of **over 10 percent**, and trees **higher than 5 meters**,.



# **Prompt 4 — FAO FRA 2020 definitions + plantations** From FAO FRA 2020 Definitions, extract definitions for forest, other wooded land, plantations, and tree crops. Note any explicit statements about rubber plantations or similar tree crops. Provide citations.

**Forest** Forest is defined as "Land spanning more than 0.5 hectares with trees higher than 5 meters and a canopy cover of more than 10 percent, or trees able to reach these thresholds in situ". This classification explicitly excludes land that is predominantly under urban or agricultural land use.

**Other Wooded Land** Other wooded land is defined as "Land not classified as 'Forest', spanning more than 0.5 hectares; with trees higher than 5 meters and a canopy cover of 5-10 percent, or trees able to reach these thresholds in situ; or with a combined cover of shrubs, bushes and trees above 10 percent". Like forests, this category does not include land that is predominantly under agricultural or urban land use.

**Plantations (Plantation Forest)** A "Plantation Forest" is a sub-category of "Planted Forest" (which is forest predominantly composed of trees established through deliberate seeding or planting). It is specifically defined as a "Planted Forest that is intensively managed and meet ALL the following criteria at planting and stand maturity: one or two species, even age class, and regular spacing". This includes short rotation plantations for wood, fibre, and energy, but excludes forests planted for ecosystem restoration or those that resemble naturally regenerating forests at maturity.

**Tree Crops and Agricultural Plantations** Tree crops fall under the category of "Other land with tree cover" and are not classified as forests. Specific sub-categories include:

- **Tree Orchards:** "“Other land with tree cover” predominantly composed of trees for production of fruits, nuts, or olives".
- **Palms:** "“Other land with tree cover” predominantly composed of palms for production of oil, coconuts or dates".

**Explicit Statements Regarding Rubber Plantations and Similar Crops** The FAO FRA 2020 definitions draw a strict line between forestry plantations and agricultural tree crops based on their intended product:

- **Rubber and Cork:** The explanatory notes for the "Forest" definition explicitly state that the forest category **includes "rubber-wood, cork oak and Christmas tree plantations"**.
- **Fruit, Oil, and Olive:** Conversely, the forest definition explicitly **excludes "tree stands in agricultural production systems, such as fruit tree plantations, oil palm plantations, olive orchards and agroforestry systems when crops are grown under tree cover"**. These agricultural tree systems are instead classified under "Other land with tree cover".
# **Prompt 5 — Rubber plantations classification** Based on the above sources, is a **rubber tree plantation** classified as Forest Land or Cropland/Agricultural Land for GHG accounting? If ambiguous, explain the conditions and cite sources.

Based on the authoritative definitions provided by the FAO Global Forest Resources Assessment 2020, a rubber tree plantation is classified as **Forest Land**, not as Cropland or Agricultural Land.

While it might seem conceptually similar to agricultural tree crops, the classification is not ambiguous in the standard guidelines. Here are the specific definitions that dictate this classification:

- **Explicit Inclusion in Forest Land:** The FAO guidelines explicitly state that the definition of "Forest" _includes_ "rubber-wood, cork oak and Christmas tree plantations".
- **Distinct from Agricultural Tree Crops:** The guidelines draw a strict line between rubber trees and agricultural tree crops. The FAO explicitly _excludes_ "tree stands in agricultural production systems, such as fruit tree plantations, oil palm plantations, [and] olive orchards" from the Forest category. These excluded agricultural systems are instead classified as "Other land with tree cover".
- **Classification of the Output:** To further solidify this categorization, the FAO defines the rubber and latex harvested from these plantations as **"Non wood forest products"** (NWFPs). The definitions specify that rubber and latex are NWFPs "regardless of whether from natural forests or plantations".

Therefore, for the purposes of global forest resources and GHG assessments following these definitions, rubber tree plantations are formally treated as forests rather than agricultural cropland.


# **Prompt 6 — Shade coffee / agroforestry** Based on the above sources, how should **coffee under shade/perennial trees** be classified (Forest Land vs Cropland vs agroforestry)? Provide decision criteria + citations.

*IPCC 2019*
The classification of coffee grown under shade or perennial trees is determined by the **national structural thresholds** a country uses to define a forest.

**When to classify as Forest Land:** If the combined vegetation structure of the coffee bushes and overstorey shade trees meets the country's specific thresholds used to define **Forest Land** (which typically consist of a minimum area, minimum tree height, and minimum canopy cover), the system may be classified as Forest Land. Countries can document which woody crops meet their forest definition and may create specific sub-divisions within the Forest Land category to explicitly track these lands.

**When to classify as Cropland (Agroforestry):** If the vegetation structure of the shaded coffee system **falls below** the country's established thresholds for Forest Land, it must be classified as **Cropland**.

- Within the Cropland category, coffee grown under or between overstorey shade trees is classified as a **polyculture agroforestry system**.
- Specifically, the IPCC guidelines define this management practice within Cropland agroforestry as a **"shaded perennial-crop system"**.

_(Note: For comparison, if coffee is grown as a monoculture without any shade trees, it is also considered Cropland, but is sub-classified as a "Plantation")._

*FAO*
Coffee grown under shade or perennial trees is an example of an agroforestry system (specifically, multi-strata agroforestry or crops grown under tree cover). Its exact classification for GHG accounting and global forest resources reporting depends on the physical structure of the shade trees.

Here are the decision criteria for classifying this system:

**1. It is explicitly EXCLUDED from the "Forest" classification.** Even if the shade trees are tall and dense, the system is not considered a standard forest. The FAO explicitly excludes "agroforestry systems when crops are grown under tree cover" and agricultural tree crops from its definition of Forest.

**2. Condition for classification as CROPLAND:** The system is classified strictly as **Cropland** if the vegetation structure of the shade trees consistently falls _below_ the established thresholds for forest land. For example, if the shade trees do not meet the minimum area (0.5 hectares), height (5 meters), or canopy cover (10 percent) requirements, it remains cropland.

**3. Condition for classification as AGROFORESTRY / OTHER LAND WITH TREE COVER:** If the shade trees are large and dense enough to reach the height and canopy thresholds of a forest (e.g., able to reach 5 meters in height with >10% canopy cover), the system is classified by the FAO under the broad category of **"Other land with tree cover"** and the specific sub-category of **"Agroforestry"**.

**GHG Accounting Implications for this System:**

- **Land Use Change:** If a natural forest is cleared and replaced by coffee under shade trees, the GHG Protocol considers this a **subcategory land use change** (the replacement of a natural forest with "tree crops" or "agroforestry systems when crops are grown under tree cover"). Companies must account for the gross carbon stock loss from this conversion.
- **Land Management Units (LMUs):** When companies account for their scope 3 spatial boundaries at the farm level, land integrated into "multi-strata agroforestry/shade trees" can be included within the LMU boundary, provided it is managed under a single land management plan and connected biophysically or socio-economically to the productive lands.
# **Prompt 7 — Practical decision rules** Synthesize concise decision rules for classifying land with perennial tree crops (rubber, coffee) in GHG inventories, highlighting where national definitions or managed-land approach override default classification. Provide citations.

*IPCC 2019*
**Decision Rules for Classifying Perennial Tree Crops**

**1. Apply the Managed Land Proxy (MLP)**

- **Rule:** All land containing perennial tree crops (like rubber, coffee, or oil palm) cultivated for production is classified as "managed land".
- **Override Context:** Under the MLP, all greenhouse gas emissions and removals on this land are considered anthropogenic and must be reported, overriding the need to separate direct human-induced effects from natural background emissions on these specific lands.

**2. Check National Forest Land Thresholds**

- **Rule:** The classification of perennial tree crops is fundamentally driven by the specific structural thresholds (e.g., minimum area, tree height, and canopy cover) established by the country to define a "forest".
- **Override Context:** National definitions override default categorizations. Even if a crop is traditionally considered "agricultural" (like rubber or orchards), if its physical structure meets the country's national definition of a forest, it can be classified as Forest Land.

**3. Allocate to Forest Land (If Thresholds are Met)**

- **Rule:** If the perennial tree crop (or an agroforestry system incorporating tree crops) meets the national thresholds for Forest Land, it should be classified as such.
- **Sub-rule:** Countries must document exactly which woody crops meet their Forest Land definition and are encouraged to create specific sub-divisions (e.g., within Forest Land or Cropland) to transparently separate and track these specific lands.

**4. Allocate to Cropland (If Thresholds are Not Met)**

- **Rule:** If the vegetation structure of the perennial tree crop falls below the national thresholds used for the Forest Land category, it must be classified as Cropland.
- **Sub-rule (Monocultures):** Crops like tea, coffee, cacao, rubber, and oil palms grown as monocultures without shade trees are classified under Cropland as "Plantations".
- **Sub-rule (Agroforestry):** Shade-tolerant crops (like coffee or cacao) grown under or between overstorey shade trees are classified under Cropland as "Shaded perennial-crop systems".

**5. Resolve Definition Inconsistencies to Prevent Double Counting**

- **Rule:** Every land unit must be reported in only one category to prevent double counting or misallocation.
- **Override Context:** Countries may use their own national definitions or other internationally accepted definitions (e.g., FAO, SEEA), but if these conflict with IPCC land-use category definitions, the national data must be adjusted to ensure it fits consistently within the six top-level IPCC categories. All definitions must be applied transparently and consistently over time.


**Decision Rules for Classifying Perennial Tree Crops**

**Rule 1: Rubber Plantations (Default Classification: Forest Land)**

- **Classification:** Rubber tree plantations are explicitly classified as **Forest Land** under FAO definitions.
- **Product Treatment:** The outputs of these plantations, specifically rubber and latex, are classified as "Non wood forest products," regardless of whether they are extracted from natural forests or managed plantations.

**Rule 2: Coffee under Shade Trees (Default Classification: Cropland / Agroforestry)**

- **Exclusion from Forest:** Agroforestry systems where crops are grown under tree cover (such as shade-grown coffee) are explicitly excluded from the "Forest" classification.
- **Vegetation Thresholds:** If the shade trees consistently fall below the established forest land thresholds (e.g., minimum 0.5 hectares, 10% canopy cover, and 5 meters in height), the land is definitively classified as **Cropland**.
- **Above Thresholds:** If the shade trees meet or exceed forest structural thresholds, the land is classified as **"Other land with tree cover"**. If a natural forest is cleared to establish this system, the GHG Protocol mandates accounting for it as a forest subcategory land-use change.


*FAO/ GHG Protocol*
**Overrides to Default Classifications**

**Override 1: National Definitions and Classification Systems (UNFCCC)** Under UNFCCC guidelines, the default global classifications can be overridden by a country's specific definitions if standard thresholds do not fit the local context.

- Annex I Parties are permitted to use national methodologies and definitions that they consider better able to reflect their national situation.
- However, to use this override, the Party must explicitly report its national land-use definitions and demonstrate exactly how its classification systems correspond to standard LULUCF (Land Use, Land-Use Change, and Forestry) categories in its national inventory report.

**Override 2: The Managed-Land Proxy (GHG Protocol)** In corporate GHG accounting, the "managed-land proxy" acts as a strict operational override regarding how emissions are accounted for on land actively used for perennial crops (e.g., productive agricultural lands).

- Regardless of whether the land is technically classified as Cropland or Forest Land, if it is utilized as "productive agricultural land," the GHG Protocol mandates that **all** changes in land carbon stocks are considered anthropogenic.
- This removes any option to classify parts of a perennial crop system as "unmanaged." Companies must fully account for all net carbon stock losses on these lands, including sudden stock losses caused by natural disturbances like fires, storms, or degradation.


# Prompt 8: What is the **national forest definition** used in the relevant inventory (area/height/canopy thresholds) and does it explicitly include/exclude **plantations** and **agroforestry**?

The provided sources do not contain a national forest definition based on physical inventory thresholds such as land area, tree height, or canopy cover. Instead, the relevant forestry laws define a forest strictly based on land tenure.

According to the Forest Act B.E. 2484 (1941), a **"Forest"** is legally defined as "land which is not acquired by any person under the Land Code".

Regarding whether this includes or excludes specific land uses:

- **Plantations:** Plantations are explicitly addressed and defined separately from the general legal definition of a forest. The Forest Plantation Act (No. 2) B.E. 2558 (2015) defines a **“Forest plantation”** as land that has been registered specifically for the purpose of planting and maintaining certain annexed tree species. The Commercial Forest Plantation Act B.E. 2535 (1992) similarly defines a **"Commercial Forest"** as land registered for planting restricted timber. Unlike a general "forest" (which applies only to land _not_ acquired by individuals), the land eligible for registration as a forest plantation explicitly includes privately owned land (with title deeds or certificates of utilization under the Land Code), land within agricultural reform areas, and specific permitted areas within national reserved forests.
- **Agroforestry:** The provided sources do not explicitly mention the term "agroforestry," nor do they specify whether agroforestry practices are included or excluded from the definitions of forests or plantations.


# Prompt 9: For rubber, is the national classification treating rubber primarily as **Cropland perennial plantation** (common in some national systems) or as **Forest Land** (closer to FAO “rubber-wood plantations” framing)?
Based on the provided sources, there is no information regarding the national classification of rubber, nor is there any mention of the categories "Cropland perennial plantation" or "Forest Land" in the context of rubber.

The provided texts (which consist of Thai forestry and plantation laws) do not explicitly mention rubber or the Para rubber tree (_Hevea brasiliensis_). The laws strictly define a "Forest" based on land tenure—specifically, land that has not been acquired by any person under the Land Code—and define "Forest plantations" based on the registration of specific tree species.

While the annex of eligible plants for registered forest plantations includes fruit-bearing trees like mango, durian, and tamarind, rubber is not listed among them. _(Note: The texts frequently regulate a tree referred to as "Yang", but in Thai forestry context, this refers to Dipterocarpus species, not the Para rubber tree)._

---

# Analysis (IPCC AFOLU-oriented)

## 1) What IPCC is *actually asking you to do*

- **Pick one land-use category per land unit per year** (avoid double counting), using the six IPCC top-level categories and your **national definitions/classification rules** (incl. forest thresholds) ([`V4_03_Ch3_Representation.pdf`](V4_03_Ch3_Representation.pdf:1), Section 3.2; Section 3.3.2).
- **Do not infer land-use from land-cover blindly**: tree cover can exist on land whose *predominant use* is agriculture, and that may drive classification ([`V4_03_Ch3_Representation.pdf`](V4_03_Ch3_Representation.pdf:1), Section 3.2; [`V4_04_Ch4_Forest_Land.pdf`](V4_04_Ch4_Forest_Land.pdf:1), Table 4.2).
- Use **Managed Land Proxy (MLP)** to scope what’s “anthropogenic” for *IPCC inventory* purposes: perennial crop systems used for production are managed land and therefore in-scope for reporting ([`V4_01_Ch1_Introduction.pdf`](V4_01_Ch1_Introduction.pdf:1), Section 1.1; Section 1.4; [`V4_02_Ch2_Generic_Methods.pdf`](V4_02_Ch2_Generic_Methods.pdf:1), Section 2.6).

## 2) Working definitions to anchor decisions

- **Forest Land**: land with woody vegetation consistent with *national forest thresholds* (min area + min canopy cover + min height), including temporarily below-threshold stands that can reach thresholds _in situ_ and temporarily destocked forests ([`V4_03_Ch3_Representation.pdf`](V4_03_Ch3_Representation.pdf:1), Section 3.2; Box 3.1a; [`V4_04_Ch4_Forest_Land.pdf`](V4_04_Ch4_Forest_Land.pdf:1), Annex 4A.1; Table 4.2).
- **Cropland**: arable/tillable land + rice + **annual and perennial crops**, including agroforestry systems where vegetation structure is below Forest Land thresholds and not expected to exceed them later ([`V4_03_Ch3_Representation.pdf`](V4_03_Ch3_Representation.pdf:1), Section 3.2; [`V4_05_Ch5_Cropland.pdf`](V4_05_Ch5_Cropland.pdf:1), Section 5.1).

## 3) Hypothesis answers

#### H1 — Is a rubber tree plantation “Forest Land” under IPCC?

**Answer (IPCC framing): it depends on national definitions AND the rule you apply for “predominant use” (land-use vs land-cover).**

- IPCC explicitly treats **rubber trees as a perennial crop** example within Cropland when these systems **do not meet** the criteria for Forest Land ([`V4_05_Ch5_Cropland.pdf`](V4_05_Ch5_Cropland.pdf:1), Section 5.1).
- IPCC also allows that **woody systems that meet the national Forest Land structural thresholds** may be classified as Forest Land (subject to consistent national rules) ([`V4_03_Ch3_Representation.pdf`](V4_03_Ch3_Representation.pdf:1), Section 3.2; Box 3.1a; [`V4_04_Ch4_Forest_Land.pdf`](V4_04_Ch4_Forest_Land.pdf:1), Annex 4A.1).
- The NotebookLM output also cites a crucial nuance: Forest Land determination can depend on **absence of other predominant land uses**, and it indicates that agricultural production systems (orchards/plantations/agroforestry) may be excluded from Forest Land even if there is tree cover ([`V4_04_Ch4_Forest_Land.pdf`](V4_04_Ch4_Forest_Land.pdf:1), Table 4.2; [`V4_03_Ch3_Representation.pdf`](V4_03_Ch3_Representation.pdf:1), Section 3.2).

**Reconciling the FAO statement**: FAO FRA 2020 explicitly includes “rubber-wood … plantations” under its Forest definition, but **FAO and IPCC categories are not identical**, and IPCC still requires a single national classification system mapped consistently into the six IPCC land-use categories ([`FAO-FRA-2020-Definitions.pdf`](FAO-FRA-2020-Definitions.pdf:1); [`V4_03_Ch3_Representation.pdf`](V4_03_Ch3_Representation.pdf:1), Section 3.3.2).

**Practical takeaway**: For inventory work, treat rubber plantations as **managed land**; then classify as **Cropland (perennial plantation)** or **Forest Land** based on your national forest definition/thresholds and your explicit rule for agricultural tree crops vs forest land to avoid double counting.

#### H2 — Is coffee under shade/perennial trees “Forest Land” under IPCC?

**Answer (IPCC framing): typically “Cropland (agroforestry/shaded perennial-crop system)” unless your national forest definition/classification rules place it in Forest Land.**

- IPCC includes **agroforestry systems** in Cropland **when vegetation structure falls below Forest Land thresholds** ([`V4_03_Ch3_Representation.pdf`](V4_03_Ch3_Representation.pdf:1), Section 3.2).
- The NotebookLM output labels shaded coffee as a “shaded perennial-crop system” within Cropland agroforestry when below thresholds; and notes that if the overstorey structure meets Forest Land thresholds, a country could classify it as Forest Land (with clear documentation/sub-classes) ([`V4_05_Ch5_Cropland.pdf`](V4_05_Ch5_Cropland.pdf:1), Section 5.1; [`V4_03_Ch3_Representation.pdf`](V4_03_Ch3_Representation.pdf:1), Section 3.2).
- FAO explicitly excludes “agroforestry systems when crops are grown under tree cover” from Forest, placing them under “Other land with tree cover” / agroforestry, which again highlights that **you must map definitions carefully rather than mix them** ([`FAO-FRA-2020-Definitions.pdf`](FAO-FRA-2020-Definitions.pdf:1)).

## 4) Decision checklist (use for both rubber + shaded coffee)

1. **Managed land?** If it’s under production/management, treat as managed land (in-scope) ([`V4_01_Ch1_Introduction.pdf`](V4_01_Ch1_Introduction.pdf:1), Section 1.1).
2. **National forest thresholds**: confirm your chosen min area / canopy / height (often within the Kyoto/IPCC glossary range cited: 0.05–1 ha; 10–30%; 2–5 m) ([`V4_04_Ch4_Forest_Land.pdf`](V4_04_Ch4_Forest_Land.pdf:1), Annex 4A.1).
3. **Predominant land-use rule**: decide and document how you treat agricultural tree crops and agroforestry when they meet structural thresholds (land-use vs land-cover precedence) ([`V4_03_Ch3_Representation.pdf`](V4_03_Ch3_Representation.pdf:1), Section 3.2; [`V4_04_Ch4_Forest_Land.pdf`](V4_04_Ch4_Forest_Land.pdf:1), Table 4.2).
4. **No double counting**: ensure each parcel is in exactly one category each year; reconcile mapping scale differences if needed ([`V4_03_Ch3_Representation.pdf`](V4_03_Ch3_Representation.pdf:1), Section 3.2; Section 3.3.2).

## 5) Thailand context — land-classification rules + watershed constraints (and IPCC mapping implications)

**Thailand land-classification rules referenced in the sources**

- The Land Development Committee’s revised criteria define **“areas to be conserved as permanent forest”** using multiple filters, including: (1) land with forest condition, (2) watershed class 1 or 2 areas, (3) soils unsuitable for agriculture, and (4) mountainous or slope >35% areas in contiguous blocks ≥3.125 rai (0.5 ha) that are forested ([`src/00_Inbox/ปรับเกณฑ์จำแนกที่ดินใหม่ กันพื้นที่ป่าไม้ถาวร.md`](src/00_Inbox/ปรับเกณฑ์จำแนกที่ดินใหม่%20กันพื้นที่ป่าไม้ถาวร.md:30); [`src/00_Inbox/คณะกรรมการพัฒนาที่ดิน เห็นชอบการปรับปรุงหลักเกณฑ์การจำแนกประเภทที่ดิน ให้เหมาะสมกับสถานการณ์ปัจจุบันหวังให้เกิดประโยชน์แก่เกษตรกรอย่างยั่งยืน.md`](src/00_Inbox/คณะกรรมการพัฒนาที่ดิน%20เห็นชอบการปรับปรุงหลักเกณฑ์การจำแนกประเภทที่ดิน%20ให้เหมาะสมกับสถานการณ์ปัจจุบันหวังให้เกิดประโยชน์แก่เกษตรกรอย่างยั่งยืน.md:14)).
- The same framework also defines **“permanent forest suitable to be reclassified for agriculture/other use”**, including degraded forest with agriculture-suitable soils and existing use, public-use areas, and government-use areas ([`src/00_Inbox/ปรับเกณฑ์จำแนกที่ดินใหม่ กันพื้นที่ป่าไม้ถาวร.md`](src/00_Inbox/ปรับเกณฑ์จำแนกที่ดินใหม่%20กันพื้นที่ป่าไม้ถาวร.md:39); [`src/00_Inbox/คณะกรรมการพัฒนาที่ดิน เห็นชอบการปรับปรุงหลักเกณฑ์การจำแนกประเภทที่ดิน ให้เหมาะสมกับสถานการณ์ปัจจุบันหวังให้เกิดประโยชน์แก่เกษตรกรอย่างยั่งยืน.md`](src/00_Inbox/คณะกรรมการพัฒนาที่ดิน%20เห็นชอบการปรับปรุงหลักเกณฑ์การจำแนกประเภทที่ดิน%20ให้เหมาะสมกับสถานการณ์ปัจจุบันหวังให้เกิดประโยชน์แก่เกษตรกรอย่างยั่งยืน.md:29)).
- Watershed quality classification is used as a **conservation zoning tool**: watershed class 1 areas align with conservation forest zoning and overlap protected areas (national parks, wildlife sanctuaries); use of resources is constrained and subject to cabinet decisions and EIA requirements in sensitive zones ([`src/00_Inbox/ความสัมพันธ์กับป่าในเขตอนุรักษ์.md`](src/00_Inbox/ความสัมพันธ์กับป่าในเขตอนุรักษ์.md:11)).

**Thailand legal definition nuance (from Prompt 8 sources)**

- A key mismatch to manage explicitly: Thai forestry law can define **“forest”** based on **land tenure** (land not acquired under the Land Code), rather than structural thresholds like canopy/height/area ([`src/00_Inbox/สรุปสาระสำญของพระราชบัญญัติป่าไม้ พุทธศักราช 2484 และที่แก้ไขเพิ่มเติม.md`](src/00_Inbox/สรุปสาระสำญของพระราชบัญญัติป่าไม้%20พุทธศักราช%202484%20และที่แก้ไขเพิ่มเติม.md:10)).
- Therefore, “is it forest under Thai law?” and “is it Forest Land under IPCC?” are **different questions**. For inventory, you still need a **GHG-inventory forest definition / mapping rule set** that is applied consistently over time ([`V4_03_Ch3_Representation.pdf`](V4_03_Ch3_Representation.pdf:1), Section 3.2; Section 3.3.2).

**Implications for IPCC AFOLU mapping (Thailand-specific)**

- These rules effectively function as a **national land-use classification system**, which IPCC allows if consistently mapped into the six land-use categories; therefore, the “permanent forest” class and watershed-class constraints can be mapped to **Forest Land** under Thailand’s national definition (documented as national rules) ([`V4_03_Ch3_Representation.pdf`](V4_03_Ch3_Representation.pdf:1), Section 3.2; Section 3.3.2).
- Areas **reclassified out of permanent forest** (e.g., degraded forest with agricultural suitability and existing use) imply **land-use conversion** and should be treated as “Forest Land converted to Cropland” or another end-use category depending on actual use; ensure a single category per parcel per year ([`V4_03_Ch3_Representation.pdf`](V4_03_Ch3_Representation.pdf:1), Section 3.2; Section 3.3.2).
- The explicit **slope/contiguity threshold (≥0.5 ha)** and watershed-class rules provide **national structural/administrative constraints** that can complement forest thresholds (height/canopy/area) when defining Forest Land in Thailand; document how these are applied to avoid cross-category overlap.

## 6) Ambiguities

- **Thailand inventory definition gap (Prompt 8):** The legal definition of “forest” being tenure-based does *not* answer the IPCC question. Identify the **forest definition used in Thailand’s GHG inventory/LULUCF reporting** (structural thresholds and/or an operational land-use decision tree) and document how it maps into the six IPCC categories ([`src/00_Inbox/สรุปสาระสำญของพระราชบัญญัติป่าไม้ พุทธศักราช 2484 และที่แก้ไขเพิ่มเติม.md`](src/00_Inbox/สรุปสาระสำญของพระราชบัญญัติป่าไม้%20พุทธศักราช%202484%20และที่แก้ไขเพิ่มเติม.md:10); [`V4_03_Ch3_Representation.pdf`](V4_03_Ch3_Representation.pdf:1), Section 3.2; Section 3.3.2).
- **Plantations / agroforestry mapping (Prompt 8):** Thailand has administrative definitions for “forest plantation/commercial forest” via registration, but the provided sources do not state how **agroforestry** is treated. Decide (and document) whether perennial crop systems that meet structural thresholds are forced into **Cropland** (predominant use) or can be **Forest Land** under national rules.
- **Rubber classification (Prompt 9):** Current Thai-law sources do not state how rubber is categorized in national inventory terms, and rubber is not evidenced here as a “registered forest plantation” species. You still need an inventory-side rule for rubber (Cropland perennial plantation vs Forest Land), especially for parcels inside/outside “permanent forest” / watershed constraint zones.
- **Shaded coffee stability:** Define a stability rule (e.g., multi-year averaging, predominant use, or minimum time-in-category) to avoid year-to-year oscillation when shade-tree cover fluctuates around thresholds.

## 7) Final verdict (best guess; Thailand-oriented, IPCC AFOLU compatible)

**Scope note:** This is a *best guess* to enable progress when Thailand’s GHG-inventory forest definition / decision tree is not yet confirmed. It should be superseded once you locate Thailand’s inventory-side definition and mapping rules (see Section 6) ([`V4_03_Ch3_Representation.pdf`](V4_03_Ch3_Representation.pdf:1), Section 3.2; Section 3.3.2).

### Final classification calls (most defensible defaults)

1) **Rubber plantation**

- **Default (best guess): classify as _Cropland (perennial plantation)_** because rubber is a production perennial crop and IPCC Cropland explicitly includes perennial plantations such as rubber when not treated as Forest Land, and because the “predominant land use” rule often overrides tree cover when the system is agricultural ([`V4_05_Ch5_Cropland.pdf`](V4_05_Ch5_Cropland.pdf:1), Section 5.1; [`V4_04_Ch4_Forest_Land.pdf`](V4_04_Ch4_Forest_Land.pdf:1), Table 4.2).
- **If rubber exists inside Thailand’s “permanent forest” / watershed conservation constraints:** still record the *actual land use* in the inventory, but treat it as **Forest Land converted to Cropland** (i.e., a land-use conversion/deforestation signal) rather than silently keeping it as “Forest Land remaining Forest Land” ([`src/00_Inbox/ปรับเกณฑ์จำแนกที่ดินใหม่ กันพื้นที่ป่าไม้ถาวร.md`](src/00_Inbox/ปรับเกณฑ์จำแนกที่ดินใหม่%20กันพื้นที่ป่าไม้ถาวร.md:30); [`V4_03_Ch3_Representation.pdf`](V4_03_Ch3_Representation.pdf:1), Section 3.2).

2) **Coffee grown under shade/perennial trees (agroforestry / shaded coffee)**

- **Default (best guess): classify as _Cropland (agroforestry / shaded perennial-crop system)_**. IPCC Cropland explicitly includes agroforestry systems when the vegetation structure is below Forest Land thresholds; and even when structure is high, many national systems still keep these in Cropland because the land use is agriculture ([`V4_03_Ch3_Representation.pdf`](V4_03_Ch3_Representation.pdf:1), Section 3.2; [`V4_05_Ch5_Cropland.pdf`](V4_05_Ch5_Cropland.pdf:1), Section 5.1; [`V4_04_Ch4_Forest_Land.pdf`](V4_04_Ch4_Forest_Land.pdf:1), Table 4.2).

### Practical “tie-breaker” rule (use until Thailand inventory rules are found)

- If the system is clearly a **commercial agricultural production system** (rubber, coffee), treat it as **Cropland by default**, unless you have a written Thailand inventory rule that explicitly includes that system under Forest Land.
- If it is located in areas Thailand classifies for conservation/permanent forest via watershed/slope/forest-condition criteria, treat any agricultural use as **conversion** for inventory accounting (Forest Land → Cropland), and surface it as a policy/land-management issue (rather than re-labelling it as “forest”) ([`src/00_Inbox/ความสัมพันธ์กับป่าในเขตอนุรักษ์.md`](src/00_Inbox/ความสัมพันธ์กับป่าในเขตอนุรักษ์.md:11); [`src/00_Inbox/ปรับเกณฑ์จำแนกที่ดินใหม่ กันพื้นที่ป่าไม้ถาวร.md`](src/00_Inbox/ปรับเกณฑ์จำแนกที่ดินใหม่%20กันพื้นที่ป่าไม้ถาวร.md:30)).
