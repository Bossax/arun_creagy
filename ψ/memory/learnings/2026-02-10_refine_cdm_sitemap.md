# Lesson Learned: Bridging Science and Policy via Conceptual Data Modeling

## Pattern: The "Universal Adapter" for Temporal Heterogeneity
In climate data systems, a common failure point is the "Semantic Schism" between event-driven disaster reporting (Sendai) and trend-driven climate science (IPCC). Databases designed for sudden shocks (e.g., floods) often cannot natively handle slow-onset stresses (e.g., sea-level rise) without distorting the data (e.g., creating "fake events" with arbitrary start/end dates).

**Solution**: Implement an associative entity (`ATTRIBUTION_LINK`) that acts as a polymorphic bridge. It allows a single outcome (Loss/Damage) to be explained by either a discrete event (Shock) or a continuous driver (Stress) while capturing a confidence level.

## Pattern: The "Vulnerability Strategy" for Heterogeneous Analytics
Risk assessments often conflict because they use incompatible methodologies: mathematical "Impact Functions" (e.g., CLIMADA) vs. social "Vulnerability Frameworks" (e.g., National Indices).

**Solution**: Use a dispatcher pattern in the CDM where an asset is linked to a generic `VULNERABILITY_DEFINITION`. This definition then implements either a math curve or a framework structure. This ensures schema stability as analytical requirements evolve from actuarial to policy-based.

## Pattern: Sitemap-to-CDM Stress Testing
The project sponsor's mental model is often the "Website" (Sitemap), while the architect's model is the "Engine" (CDM).

**Lesson**: Always "Stress Test" the CDM by attempting to populate specific sitemap modules with the defined entities. If a module (e.g., "Agriculture Sector Navigator") cannot be populated without a custom code change, the CDM is missing a metadata attribute (e.g., `Sector_ID`).

## Concepts
- Polymorphic Attribution
- Strategy Pattern in Data Modeling
- Semantic Schism
- Sitemap-CDM Alignment

## Source
rrr: 2025-11_DCCE-CRDB
