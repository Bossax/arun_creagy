---
parent: "[["
tags:
  - Bioacoustics
  - Underwater_Acoustics
date: 2025-06-19T22:04:00
---


The **Semi-Supervised Categorization of Shallow Marine Soundscapes** is a methodology designed to categorize and interpret different underwater acoustic environments, particularly in shallow waters, by linking them to concurrent environmental conditions. It aims to provide an automatic way to assign labels to acoustic scenes and to understand their ecological meaning without extensive manual annotation.

This method primarily focuses on continuous sounds or sounds that are frequently repeated in complex sequences, such as fish choruses or breaking waves, encompassing the overall combination of sounds present under specific conditions at particular locations.

The methodology involves several key steps:

1. **Acoustic Data Processing and Environmental Data Matching**
    
    - Underwater acoustic recordings are processed into short, overlapping time windows (e.g., 5-second segments with 60% overlap, composed of 1-second bins).
    - For each segment, acoustic features are extracted, such as the root mean squared value of sound pressure in one-third octave bands, which are commonly used for environmental impact assessment and soundscape description.
    - These acoustic samples are then matched with corresponding environmental data (e.g., season, bathymetry, moon phase, time of day, shipping density, substrate type, salinity, temperature, current speed, proximity to shipwrecks, distance to coast) [180, 181, Table 1]. Cyclic variables are converted into their sine and cosine values, and categorical variables are one-hot encoded to represent their continuous or discrete nature.
-
2. **Dimension Reduction and Acoustic Categorization**

    - **Dimension Reduction (UMAP):** Uniform Manifold Approximation and Projection (UMAP), a non-linear dimension reduction technique, is applied to the acoustic data. This maps the data to a two-dimensional space where acoustically similar points are clustered together, and dissimilar points are further apart, allowing for visual identification of acoustic clusters and computation of acoustic dissimilarity.
    - **Data Cleaning (Semi-supervised Artifact Removal):** A semi-supervised approach is used to identify and remove ecologically irrelevant sounds (artifacts) caused by instrument noise, rope noise, or small particles hitting the hydrophone.
        - Initial manual annotation of artifact segments from a subset of recordings is performed.
        - Density-Based Spatial Clustering of Applications with Noise (DBSCAN) is applied to the UMAP-reduced data, and clusters predominantly composed of manually labeled artifacts are identified and removed from the dataset, assuming any unlabeled samples within these clusters are also artifacts.
    - **Final Acoustic Categories (Second UMAP + DBSCAN):** UMAP is reapplied to the cleaned data (without artifacts) to achieve clearer distinctions among ecologically relevant clusters. DBSCAN is then used again to identify the final acoustic categories, with outlier "noise" samples removed.
3. **Characterization of Acoustic Classes using Explainable AI (XAI)**
    
    - A Random Forest (RF) Classifier is trained using the environmental variables to predict the identified acoustic clusters.
    - **SHAP (SHapley Additive exPlanations):** Explainable AI tools like SHAP are employed to interpret the RF model. SHAP computes the contribution of each environmental feature to the prediction of an acoustic category, thereby explaining how each feature influences the model's decisions.
    - **Redundancy Analysis:** The model is evaluated for redundancy between environmental variables, and highly redundant features are iteratively removed to prevent misleading conclusions about feature importance, ensuring that the true impact of ecological phenomena is assessed.
    - The final RF model, with non-redundant features, is then interpreted using SHAP to generate an ecological profile for each soundscape category, revealing which environmental parameters are most important in shaping and differentiating them. Incorrectly classified data are also analyzed to understand sound classes not directly linked to the considered environmental parameters.

**Advantages of this methodology:**

- **Ecological Interpretability:** It offers a novel way to interpret soundscape categories by linking them to spatio-temporal environmental conditions using explainable machine learning tools, providing practical ecological profiles for each soundscape type.
- **Reduced Human Effort:** The methodology is largely unsupervised in categorizing acoustic scenes and automates the characterization process, significantly reducing the need for laborious manual data annotation.
- **Artifact Removal:** It includes a semi-supervised method for effectively removing ecologically irrelevant artifacts, which can be a rapid solution for detecting instrument malfunctions or noise from the deployment structure in long-term recordings.
- **Handling Complex Environments:** It is particularly useful for studying soundscapes in poorly described or challenging environments, such as shallow, turbid coastal waters or remote areas with low visibility, where traditional visual surveying methods are difficult or impossible.
- **Soundscape Monitoring and Conservation:** The categorization of soundscapes assigns identifiable labels to acoustic environments, which can be valuable for policy-making and conservation programs. It enables monitoring of acoustic trends, status, and seasonal patterns, providing indicators of biodiversity and ecosystem health changes.
- **Holistic View:** By using acoustic features like one-third octave bands, the method takes a holistic view of the soundscape, capturing major quantifiable differences and avoiding reliance on specific acoustic indices that might not be robust in marine environments.
- **Foundation for Future Research:** The method can be applied to new datasets, and if environmental data are unavailable, the categories can still serve as a baseline for future monitoring and understanding of acoustic changes.