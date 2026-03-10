---
parent: "[["
tags:
  - DMCR_project
date:
---

## Draft Research Concept Note

**Title:**  
Characterizing underwater soundscapes of Thailand's coast for marine conservation and management

**Background and Rationale**  
Thailand’s coastal ecosystems are under severe threat from unsustainable human activities, including overtourism and destructive fishing practices. These pressures jeopardize marine biodiversity, the livelihoods of millions, and the cultural identity of coastal communities. Traditional vessel-based survey methods for monitoring marine environments are costly, resource-intensive, limited by environmental conditions, and unable to provide the spatial and temporal coverage required for effective management. This creates a critical need for innovative, scalable, and cost-effective monitoring solutions.

**Project Goal**  
1. To develop an open-access underwater sound data library of Thai waters using a passive acoustic monitoring system.
2. To develop a classification machine learning model to detect surface vessel activities and categorize underwater sounds of the Thai waters. 
3. To demonstrate the use of acoustic data for complementing existing environmental monitoring techniques.
    

**Methodology**
1. **Hardware Development:** Construct a hydrophone module using commercially available components and custom mechanical structures for at-sea deployment.
2. **Acoustic Data Collection**
	1. Deploy hydrophones at the  strategic marine site where other data collection routines exist
	2. Collect continuous underwater recording to cover seasonal variations of biological and human activities. The total deployment time is at least 6 months. 
	3. Gather the collected data at the site every month
3. Data analysis
	1. Labeling sound
	    1. Cluster acoustically similar events
		    - Feature extraction from spectrograms
		    - Dimensionality reduction (e.g., UMAP)
		    - Density-based clustering (e.g., HDBSCAN)
	    2. Identify potential vessel sound clusters from the characteristics of the cluster representatives
	    3. Analyze auxiliary data such as ship tracks from AIS and satellite images to assign vessel-type labels (e.g., trawler, speedboat) to the vessel sound clusters.
	    4. Sound Clusters Labeling by analysts
			- Auditory and visual inspection of cluster representatives
			- Cross-referencing with other data such as visual data, weather radar and station, seismic activity data, coastal project development record, or other underwater sound libraries
			- Label potential sources of the sound cluster
				- either biological, geological, atmospheric
				- specify the exact source or process if possible

4. Classification Model Development
	- Train classifiers using:
	    - Vessel-labeled events
	    - Categorized soundscapes
	- Test the model with additional collected data 

5. Analyze soundscape characteristics to establish a baseline
	1. Seasonal Power Spectral Density (PSD)
	2. Sound cluster characteristics
	3. Biodiversity acoustic indices e.g. intensity indices, acoustic complexity indices
    

**Expected Outputs**
1. An open-access Thai underwater sound library with labeled datasets.
2. Baseline acoustic indices for biodiversity 
3. Trained AI models for sound classifications.
4. System design documentation for hardware and AI workflow.
5. Reports and presentations for stakeholders, including case studies and recommendations for integrating acoustic monitoring into marine management.
    

**Expected Outcomes and Impact**
1. The foundational database for underwater sound research
2. Awareness among marine biologists and conservationists of the importance of acoustic monitoring.

**Timeline (Summary)**

| Phase            | Key Activities                                             |
| ---------------- | ---------------------------------------------------------- |
| **Months 1–3**   | Procurement , Testing, and Hydrophone deployment           |
| **Months 4–11**  | Data collecyion                                            |
| Months 4-10      | AI training: Vessel classification + sound categorization. |
| **Months 11–12** | Field validation; Stakeholder feedback integration.        |

**Key Stakeholders**
1. Researchers in marine science and conservation
2. Policymakers in marine and coastal management
3. Local coastal communities
    

