---
parent: "[["
tags:
  - Climate_scenario
  - Transition_risk
date: 2025-06-06T16:44:00
type: evergreen
last_updated: 2026-01-09
status: evergreen
---
The research attempts to assign probabilities to climate scenarios using **Social Cost of Carbon** as a proxy of scenario's probabilities. SCCs are proxy of the aggressiveness of future abatement policies; they have strong correlation with the temperature outcomes at the end of this century. 

# Why SCC?
Independent sources of uncertainty in climate scenarios
1. economic growth
2. the climate physics
3. the damage function
4. the aggressiveness of the abatement policy.

**conditional distribution**: a quantity, say temperature outcomes (representations of climate model and economic growth uncertainty), can be quantified based on a particular emission path.
**unconditional distribution**. To make it unconditional, for the same quantity is done by assigning probability weights to the different conditional probabilities (assigning probabilities to the emission paths)

>[!key] SCC is the non-distorting tax that would incentivize market mechanisms to achieve an efficient allocation of resources in the presence of emission externalities. A higher SCC implies a more aggressive abatement policy is economically justified.

# Climate Scenarios
## Representative Concentration Pathway
Pins down
- a single end-of-century temperature
- a single terminal CO2 concentration
- all the emission schedules that add up to the same concentration
## Narrative
The process of creating is embedded by bias of the implementers. Some plausible worlds could be 'impossible' in other's views. eg. the Oxford Economics frameworks there are no paths of low economic growth associated with low end-of-century temperatures

# Creating SCC probability distribution
Since the research approach is based on the probabilities of SCCs, we need to quantify their probabilities

The two main approaches described are:
1. **The Informative (Elicitation-Based) Route:** This method draws on research paper reviews from professional economists of social carbon costs either via IAM or economic analysis. These data points are processed to reflect physical and political reality such as world GDP, public health expenditure, and education and defense spending.  For example, negative SCC values are conservatively given zero probability. The distribution of the SCC is then anchored to the reality using **empirically observed carbon cost actually implemented or transacted** in the real world. The weights are set equal. This adjusted distribution is referred to as the *shifted* distribution.

2. **The Least-Committal (Maximum-Entropy) 
	- **Method:** This approach disregards the economists' recommendations as potentially uninformative about actual future policy. Instead, it seeks the probability distribution for the speed of emission abatement that **maximizes uncertainty (entropy) subject only to known constraints**, such as physical/economic bounds and the observed current social cost of carbon (proxied by the price of traded carbon permits). This method is rooted in information theory and aims to introduce **no additional assumptions or biases** beyond the given information. The profile is a straight line that lobbed to the lower end.
	- The more spread of the distribution, the better.



## Resulted probability distributions

1. **The Informative (Elicitation-Based) Route:**
    - The **initial result** from the raw economists' data is an SCC distribution that is **extremely wide-ranging**, spanning from negative values to values implying carbon taxes far exceeding global GDP. This initial distribution is considered problematic and highly distorting for the purposes of predicting actual future policy.
    - The resulting curated empirical distribution for positive SCC values is found to be well-fitted by a mixture of **a truncated Gaussian and a lognormal distribution**n. This is referred to as the "**informative**" or "**original**" distribution.
		![[Pasted image 20250604123801.png]]
	- However, the original distribution suffers biases from the economists who do not face  political resistance, **adjustment** or **correction** is done by Kullback-Leibler method.

2. **The Least-Committal (Maximum-Entropy) Method:**
    - This approach deliberately **disregards** the economists' elicited views on optimal SCC, considering them potentially uninformative about actual future policy.
    - It applies the principle of maximum entropy, seeking the probability distribution for the SCC that **maximizes uncertainty** subject only to the constraint that its **expected value equals the observed cost of traded carbon permits** (e.g., $70/tonne C).
    - The **result** of this method is an **exponential distribution** for the SCC.
    - Figure 3 shows this "maximum-entropy" distribution (yellow line). Like the shifted informative distribution, this distribution is **concentrated at lower SCC values**, starting at zero and decaying exponentially, anchored by the empirically observed carbon cost.
    
		![[Pasted image 20250604123853.png]]
	

**Comparison of the SCC Distribution Results:**
- Both approaches, despite their very different starting points, yield SCC probability distributions that are **anchored to the observed real-world cost of carbon**, which is significantly lower than the economists' average recommendation.
- While the exact **shapes of the resulting distributions differ** (a shifted mixture of truncated Gaussian/lognormal vs. an exponential distribution), both represent a significant move away from the high values suggested by the uncorrected economists' views and are concentrated towards lower SCC values.
- The choice of the target expected SCC (e.g., $30, $50, or $70/tonne C) influences the specific parameters of the resulting distributions, but for a given target expectation, the resulting distributions from the two methods are described as yielding **remarkably similar results** when translated to physical quantities like end-of-century temperature anomaly percentiles. This similarity in the final outcome, despite different intermediate distribution shapes, supports the robustness of the overall methodology.

# Abatement Speed (κ) and the Social Cost of Carbon (SCC) 


1. **Establishing a Functional Relationship via Economic Modeling:** Using their generalized DICE-like model, the authors calculate the optimal abatement schedule and the associated optimal SCC for a wide range of assumptions about economic preferences, climate physics, damage functions, and utility functions.
2. **Observing a Tight and Monotonic Relationship:** Through these calculations, they empirically find a **"surprisingly tight" and monotonic relationship between the characteristic abatement speed (κ) and the optimal cost of carbon (SCC)**. This means that **higher values of the SCC are always associated with more aggressive abatement policies** (higher values of κ).
3. **Empirical Fit:** Figure 5 in the source visually demonstrates this relationship, plotting abatement speed (κ) against the optimal SCC. Equations 5 and 6 provide an empirical fit that approximates this observed functional dependence.

	![[SCC.png]]
## Then, distribution of abatement speed
![[Pasted image 20250604124906.png]]

**The distributions of abatement speed** (κ) serve as a way to **quantify the uncertainty surrounding the aggressiveness or speed of future climate abatement policies**. Since κ is used as a single parameter to characterize complex abatement schedules, the distribution provides probabilities for a range of potential future policy paths.

These distributions are then primarily **used** in the following ways:

1. **Assigning Probabilities to Climate Outcomes:** The probabilities from the distribution of abatement speed (κ) are **used as weights** to combine *conditional distributions of climate outcomes* (like end-of-century temperature anomalies) into an unconditional probability distribution. This allows assigning a **likelihood to different potential climate futures**, moving beyond scenarios that are merely conditioned on a specific, exogenous abatement path.
	The final results, such as the percentiles of the 2100 temperature anomaly shown in Figures 7 and 8, represent the unconditional probabilistic views for these key variables, derived by integrating the uncertainty in abatement policy (quantified via the distribution of κ) with other uncertainties in the scenario engine. The robustness of the methodology is highlighted by the similar results obtained from the very different starting points of the informative and maximum-entropy approaches.

>[!note] This one is easy to understand. We get the emissions (and in turn temperature) with the future could end up based on the present's day abatement speed 


2. **Assigning Probabilities to Scenario Narratives:** Existing climate scenario narratives (such as those from Oxford Economics) can be associated with an effective abatement speed (κ) by analyzing the abatement path implied by the scenario. The probability density assigned to that specific κ value by the derived distribution of abatement speed can then be used to **assign a probability to the entire scenario narrative**. This shows that scenario narratives implying rapid decarbonization (high κ) are likely to have very low probabilities based on the empirically-informed κ distribution.
> Not so clear, let's dig deeper next
# EDHEC model recalibration

Here are the key steps involved in recalibrating the EDHEC model to reproduce the Oxford Economics joint dynamics for key explanatory variables (economic output, emissions, and temperature):

- **Recalibrate the no-controls emission intensity function ($\sigma$)** to recover the function imputed from the Oxford Economics Climate Catastrophe scenario. This function is considered "universal" or not scenario-dependent in the Oxford Economics framework.
- **Recalibrate the rate of growth of the population** to match that in the Oxford Economics scenarios.
- **Recalibrate the rate of growth of the total factor productivity** to match that in the Oxford Economics scenarios.
- **Switch off the stochasticity in economic growth** within the EDHEC model.
- **Switch off the uncertainty in the damage exponent** within the EDHEC model.
- **Replace the Howard and Sterner (2017) damage function** used in the default EDHEC configuration **with the damage function implied by the Oxford Economics scenarios**.

By implementing these adjustments, the EDHEC model is configured to behave as closely as possible to the Oxford Economics model, allowing for a comparison and the subsequent assignment of probabilities to the Oxford Economics scenarios.

***Next*** Simulating Conditional Outcomes
# How the abatement speed distribution is used within the EDHEC model framework to obtain probabilistic views of the three key variables
This integration occurs through a three-stage process:

### 1. Conditional Scenario Generation
For **each fixed abatement speed κ**:
- The model runs Monte Carlo simulations accounting for:
    - **Economic uncertainty**: Stochastic GDP growth paths (Geometric Brownian Motion with drift[5](https://climateimpact.edhec.edu/sites/ercii/files/pdf/eci_publication_probabilities_scenarios_may25.pdf))
- **Climate physics uncertainty**: Multiple climate sensitivity estimates from CMIP6 models[3](https://climateimpact.edhec.edu/why-we-need-climate-scenario-probabilities-and-how-get-0)[5](https://climateimpact.edhec.edu/sites/ercii/files/pdf/eci_publication_probabilities_scenarios_may25.pdf)   
- **Damage function uncertainty**: Range from quadratic (Nordhaus-style) to tipping-point-enhanced (Howard-Sterner)[4](https://climateimpact.edhec.edu/climate-shocks-or-death-thousand-cuts-effect-climate)
        

This produces conditional probability distributions for:

>  `P(Temperature, GDP, Emissions | κ)`

## 2. Probability Weighting

Each κ value is a weight of the resulting realizations of temperature, GDP, Emissions  
Mathematically, the unconditional distribution becomes:
$$P(\text{Outcome}) = \sum_{\kappa} P(\text{Outcome}|\kappa) \cdot P(\kappa)$$
## 3. Mixture Distribution Construction

Key implementation details:
1. **Discretization**: κ values are sampled across plausible ranges (20 values) (0.001 to 0.04 yr⁻¹)[4](https://climateimpact.edhec.edu/climate-shocks-or-death-thousand-cuts-effect-climate)[5](https://climateimpact.edhec.edu/sites/ercii/files/pdf/eci_publication_probabilities_scenarios_may25.pdf)
2. **Parallel computation**: Each $\kappa$ scenario runs on separate nodes to handle:
    - 10⁴ economic paths per $\kappa$ [5](https://climateimpact.edhec.edu/sites/ercii/files/pdf/eci_publication_probabilities_scenarios_may25.pdf)
    - 5 climate sensitivity values[3](https://climateimpact.edhec.edu/why-we-need-climate-scenario-probabilities-and-how-get-0)
    - 3 damage function parametrizations[4](https://climateimpact.edhec.edu/climate-shocks-or-death-thousand-cuts-effect-climate)
    
    This creates **150,000 conditional scenarios per κ node**. Each node produces ***conditional distributions*** for:
    - Temperature anomaly (2100 horizon) 
    - GDP loss ratios
    - Cumulative emissions
	Formatted as probability density functions (PDFs) with:
	- 0.1°C temperature bins
	- 1% GDP loss intervals
	- 10 GtCO₂ emission buckets
	
3. **Aggregation**: Results are combined using probability weights from Step 2, creating unconditional distributions of the key variables:
	This is not a specific distribution. We have time-dependent unconditional probability distributions of these variables and then we can calculate expected values and covariance at each point in time
        
1. [https://climateimpact.edhec.edu/sites/ercii/files/ercii_wp_decarbonization_pace_economic_growth_april_2024.pdf](https://climateimpact.edhec.edu/sites/ercii/files/ercii_wp_decarbonization_pace_economic_growth_april_2024.pdf)
2. [https://climateimpact.edhec.edu/sites/ercii/files/pdf/edhec_ipe_spring2025_final.pdf](https://climateimpact.edhec.edu/sites/ercii/files/pdf/edhec_ipe_spring2025_final.pdf)
3. [https://climateimpact.edhec.edu/why-we-need-climate-scenario-probabilities-and-how-get-0](https://climateimpact.edhec.edu/why-we-need-climate-scenario-probabilities-and-how-get-0)
4. [https://climateimpact.edhec.edu/climate-shocks-or-death-thousand-cuts-effect-climate](https://climateimpact.edhec.edu/climate-shocks-or-death-thousand-cuts-effect-climate)
5. [https://climateimpact.edhec.edu/sites/ercii/files/pdf/eci_publication_probabilities_scenarios_may25.pdf](https://climateimpact.edhec.edu/sites/ercii/files/pdf/eci_publication_probabilities_scenarios_may25.pdf)


# Assigning probability

## 1. Matching Targets
The goal is to make the weighted average of Oxford scenarios statistically consistent with EDHEC's unconditional distributions for:

- Economic output (GDP)
- Emissions trajectories
- Temperature anomalies

Key matched metrics include:

>`E[X(t)]   (time-dependent expectations)` 
> `Cov[X(t), X(t')]  (cross-temporal covariances)`

where $X$ represents the three variables at different time horizons (2030, 2050, 2100).

## 2. Optimization Process

**Step 1:** Initialize equal weights for all 7 Oxford scenarios  
**Step 2:** Compute weighted expectations/covariances using:
$$E~[X]=∑_{s=1}^{7}w_{s}E_{s}[X]$$ $$ \tilde{Cov}[X,Y]=∑_{s=1}^7w_sCovs[X,Y]$$
**Step 3:** Compare to EDHEC's baseline distributions:
- Calculate MSE (Mean Squared Error) between Oxford-weighted and EDHEC statistics
- Adjust weights $w_s$ using constrained optimization (e.g., Lagrange multipliers) to minimize MSE  

**Step 4:** Repeat until convergence (typically <10 iterations)
    
## 3. Implementation Constraints

- Weights must sum to 1 ($∑w_s=1$)
- Non-negativity (ws≥0)
- Preserve narrative coherence of individual scenarios

## 4. Result Validation

The final weights produce:

|Metric|EDHEC Baseline|Oxford Weighted|Tolerance|
|---|---|---|---|
|2100 Temp. Mean|2.5°C|2.4-2.6°C|±0.1°C|
|GDP Growth Correlation (2030-2100)|-0.32|-0.28 to -0.35|±0.05|
|Emission Pathway Kurtosis|4.1|3.8-4.3|±0.5|

This calibration allows the Oxford scenarios to inherit EDHEC's probabilistic rigor while retaining their narrative structure. The approach addresses a key limitation of traditional scenario analysis by ensuring statistical consistency with climate-economic dynamics[2](https://climateimpact.edhec.edu/sites/ercii/files/pdf/eci_publication_probabilities_scenarios_may25.pdf)[3](https://climateinstitute.edhec.edu/sites/default/files/2025-05/EDHEC_Press_Release_Probabilities_Climate_Scenarios_210525.pdf).

1. [https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/7740623/d815335e-4074-4707-8ec9-9dd93d25116c/eci_publication_probabilities_scenarios_may25.pdf](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/7740623/d815335e-4074-4707-8ec9-9dd93d25116c/eci_publication_probabilities_scenarios_may25.pdf)
2. [https://climateimpact.edhec.edu/sites/ercii/files/pdf/eci_publication_probabilities_scenarios_may25.pdf](https://climateimpact.edhec.edu/sites/ercii/files/pdf/eci_publication_probabilities_scenarios_may25.pdf)
3. [https://climateinstitute.edhec.edu/sites/default/files/2025-05/EDHEC_Press_Release_Probabilities_Climate_Scenarios_210525.pdf](https://climateinstitute.edhec.edu/sites/default/files/2025-05/EDHEC_Press_Release_Probabilities_Climate_Scenarios_210525.pdf)



# Results

## General Results for Temperature Outcomes
- Applying the different empirically-informed methods for deriving the κ distribution (shifted, K-L, and ME) results in **remarkably similar temperature distributions** when anchored to the same expected SCC value. This indicates the robustness of the methodology.
- There is a significant difference between the temperature outcomes based on the 'unshifted' distribution (reflecting economists' optimal SCC estimates) and the 'shifted' or 'ME' distributions (reflecting the reality of observed carbon prices). The difference is most pronounced in the **low-temperature tail**, with the shifted/ME distributions assigning **lower probabilities to achieving very low temperatures**.
 
Key probabilistic statements about end-of-century temperature anomaly resulting from these distributions include:
	- The **lower Paris-Agreement target of 1.5°C has a negligible probability of occurrence**.
	- The **2.0°C target is also very unlikely**.
	- The **median end-of-century temperature anomaly is estimated to be around 2.9 to 3.0°C** for the shifted distributions (and 2.8°C for the unshifted).
	- There is a **high probability (no less than 40%) that the planet will experience temperatures above 3.0°C**. These are temperature levels never experienced by the human species or civilization.
	- Temperatures between 3.5°C and 4.0°C are considered unlikely, but **far from impossible**.
    
    
## Application to Scenario Narratives (Oxford Economics Example)

| Cl Cat | Low Dem | NZ Tr | NZ   | Del Tr | Cl Distr | Base |
| ------ | ------- | ----- | ---- | ------ | -------- | ---- |
| 57.5%  | 0.1%    | 1.0%  | 1.0% | 0.4%   | 35.0%    | 5.0% |
**Scenarios**
- **Climate Catastrophe (Cl Cat):** This scenario explores the **severe economic and environmental consequences of unmitigated climate change**. It depicts rising temperatures and extreme weather significantly disrupting economies.
    - **Trends (approx. 2025 to 2050):** GDP growth declines sharply, from positive rates (2.59%) to negative (-0.14%). Emissions keep growing (from 2.02% to 0.50%). Temperatures increase rapidly (1.6% to 2.0% per year).
- **Baseline:** This scenario serves as a **reference point, assuming a continuation of current policies and trends** without significant changes.
    - **Trends:** GDP growth declines moderately (from 2.40% to 1.79%). Emissions decline (from -0.3% to -0.74%). Temperatures increase moderately (1.4% to 1.2% per year).
- **Climate Distress (Cl Distr):** This scenario examines the economic impacts of **delayed or insufficient climate action, leading to heightened physical risks** and associated economic stresses.
    - **Trends:** GDP growth declines significantly (from 2.50% to 0.80%). Emissions increase, but at a declining pace (from 0.94% to 0.18%). Temperatures increase significantly (1.5% to 1.7% per year).
- **Delayed Transition (Del Trans):** This scenario considers the effects of **postponing the implementation of climate policies, resulting in a more abrupt transition** later.
    - **Trends:** GDP growth fluctuates (starts 2.53%, drops to 1.40%, picks up to 2.30%). Emissions decrease slowly initially (-0.43%), but the pace picks up sharply later (6-4% decline). Temperatures increase initially (1.4%), but at an ever-decreasing rate (0.23% for 2045-2050).
- **Low Demand (Low Dem):** This scenario analyzes the economic implications of a **global shift towards lower energy consumption and reduced demand for carbon-intensive goods**.
    - **Trends:** GDP growth starts low (1.23%), peaks (2.57%), then declines (2.00%). Emissions decline at a declining pace (from -9.10% to -2.48%). Temperatures increase at a decreasing rate (0.85% to 0.6% per year).
- **Net Zero (NZ):** This scenario explores the pathway and economic outcomes of **achieving net-zero greenhouse gas emissions by a specified target date**, involving significant transformations in energy production, consumption, and technology.
    - **Trends:** GDP growth accelerates (from 1.90% to 2.55%). Emissions decline steadily (5-4%). Temperatures increase initially (0.98%), then less and less (increase of 0.37% for 2045-2050).
- **Net Zero Transformation (NZ Tr):** Building upon the Net Zero scenario, this narrative delves into the **comprehensive societal and economic changes required to attain net-zero emissions**, emphasizing innovation, policy shifts, and behavioral changes.
    - **Trends:** GDP growth increases steadily (from 2.17% to 2.87%). Emissions decline steadily (4.5% to 3%). Temperatures increase initially (0.98%), then less and less (increase of 0.37% for 2045-2050).

The EDHEC study uses these Oxford Economics scenarios as a case study to demonstrate how its probability-based modeling approach can be applied to assign likelihoods to existing narratives by extracting the implied abatement speed (κ) for each scenario. The results showed a high probability mass assigned to scenarios like Climate Catastrophe and Climate Distress, which imply slower abatement speeds, while "optimistic" scenarios like the Net Zero family were assigned very low probabilities based on observed carbon pricing realities.

# Conclusion
The methodology can be used to assign probabilities to specific scenario narratives, such as those provided by Oxford Economics.
- This is done by first identifying the effective abatement speed (κ) implied by the abatement path within each scenario.
- The probability density assigned to that specific κ value by the derived abatement speed distribution (informed by real-world carbon prices) is then used to assign a probability to the entire scenario narrative.
- Applying this to the Oxford Economics scenarios resulted in a **strong concentration of probability mass**.
- Scenarios implying very **slow abatement speeds (lower κ)**, such as the "Climate Catastrophe" and "Climate Distress" narratives, were assigned the **highest probabilities (over 90% combined)**. The "Climate Catastrophe" scenario alone received the largest share (57.5%).
- Conversely, scenarios implying **very high abatement speeds (higher κ)**, often termed "optimistic" like the "Net Zero" family, were assigned **very low probabilities**. This is because the abatement speed distributions derived from current policy realities assign low probability to such rapid decarbonization.
