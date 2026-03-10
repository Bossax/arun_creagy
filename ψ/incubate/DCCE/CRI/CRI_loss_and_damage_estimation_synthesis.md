---
type: knowledge_artifact
status: current
project:
  - DCCE_CRI
title: CRI – Historical Loss and Damage Estimation (Synthesis)
description: Synthesis of methods for estimating historical disaster loss and damage with limited data for CRI Phase 1
sticker: emoji//1f345
---

# CRI – Historical Loss and Damage Estimation (Synthesis)

This note summarizes methods for reconstructing historical disaster loss and damage under data constraints and links them to design decisions in CRI Phase 1.

## 1. Methods Landscape

Source:

- [`Estimating Historical Disaster Damage and Loss with Limited Data.md`](Estimating%20Historical%20Disaster%20Damage%20and%20Loss%20with%20Limited%20Data.md)

**Core methods**

- Proxy-based national disaster inventory (DesInventar-style).
- Remote sensing and satellite analysis (e.g., flood extent from SAR).
- Catastrophe risk modeling (hazard × exposure × vulnerability).
- Hybrid methods that combine the above.

**Accuracy vs complexity**

- Hybrid multi-source approaches are most accurate but also more complex.
- Proxy-based inventories are the most feasible starting point for institutions with limited technical capacity.

## 2. Implications for CRI Phase 1

**Shift from total damage to Fiscal Relief Index**

- Given incomplete loss data, CRI Phase 1 redefines the economic component as a **Fiscal Relief Index**, based on disaster recovery/relief payments rather than total physical loss.
- This aligns with the data reality and still captures a critical dimension: pressure on public finances.

**Constrained redistribution and dasymetric mapping**

- Official provincial or district totals (population, relief payments) serve as **hard constraints**.
- High-resolution global datasets (WorldPop, land cover) are used only to **redistribute** these totals spatially, preserving consistency with administrative records.

**Gap-aware calculations**

- Zeros in administrative datasets are no longer assumed to mean "no risk".
- Satellite hazard layers and other evidence are used to flag potential **administrative data gaps**, which are then excluded from "low risk" classifications.

## 3. Future Extensions

- As data systems improve (e.g., PDNA adoption, better sectoral loss records), CRI can gradually shift toward more comprehensive loss indices.
- Hybrid approaches combining modeling, remote sensing, and improved administrative data should be piloted for major events (e.g., 2011 flood) as part of capacity building.

