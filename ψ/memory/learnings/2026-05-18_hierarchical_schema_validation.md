# Learning: Hierarchical Schema Validation for Administrative Data

**Date**: 2026-05-18
**Context**: National Administrative Boundary Cleanup (DCCE CRI)
**Author**: ARUN

## The Pattern
When joining disparate administrative datasets (e.g., legacy GIS Shapefiles vs. modern official DOPA records), nomenclature drift (renames, tone mark changes, district shifts) creates significant join friction.

## The Strategy: Hierarchical Schema Validation
Instead of attempting to "fix" names at the leaf node (village or subdistrict level) through fuzzy matching, enforce a strict top-down inheritance logic:

1.  **Define a Sovereign Schema**: Select the most authoritative hierarchical source (e.g., the DOPA CCAATT master list).
2.  **Inherit Downward**: Force all child records to inherit names and codes strictly from their parent hierarchy.
3.  **Purge Non-Conformants**: Any record whose parent codes do not exist in the sovereign hierarchy is treated as "noise" and purged.
4.  **Forensic Patch Registry**: For remaining spatial-to-attribute gaps (e.g., legacy GIS polygons), use a documented patch registry for remapping rather than algorithmic guessing.

## Why it Works
- **Prevents Expert Drift**: Ensures that the final dataset is anchored in verifiable, official hierarchies.
- **Reduces Maintenance**: Eliminates the need for hundreds of surgical patches for spelling variants.
- **Auditability**: Provides a clear lineage of where every name and code originated.

## Implementation Example (Python)
```python
# Inherit names from master hierarchy
master_p = ccaatt[ccaatt['type'] == 'province'][['p_code', 'p_name']]
df = df.merge(master_p, on='p_code', how='inner', suffixes=('_raw', ''))
# Inner join automatically purges records with invalid province codes
```

## Related Concepts
- #data-integrity #geocoding #dopa #spatial-join #master-data-management
