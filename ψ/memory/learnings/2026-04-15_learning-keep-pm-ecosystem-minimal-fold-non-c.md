---
title: # Learning — Keep PM ecosystem minimal; fold non-canonical surfaces into ledgers
tags: []
created: 2026-04-15
source: ψ/memory/learnings/2026-03-30_wmo-nfcs-project-setup-wrap.md
---

# # Learning — Keep PM ecosystem minimal; fold non-canonical surfaces into ledgers

# Learning — Keep PM ecosystem minimal; fold non-canonical surfaces into ledgers

When bootstrapping a new project PM ecosystem (CRDB-style ledgers), enforce a small canonical surface area:

- If a document/surface (e.g., a standalone “risk registry”) is not part of the ecosystem, **do not maintain it in parallel**.
- Supersede/archive the non-canonical surface (preserve history), then **map its actionable content** into canonical ledgers:
  - Direction/uncertainty → Trigger Log (T-*)
  - Constraints/assumptions → Claim Register (C-*)
  - Work products/dependencies → Deliverable Map (D-*)

Operationally, in a hybrid shell environment, prefer **small, atomic commands** with immediate verification (list destination) over large chained migrations.


---
*Added via Oracle Learn*
