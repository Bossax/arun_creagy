# Handoff: DMCR Hydrophone Rig Design (Tripod vs Mooring)

**Date**: 2026-02-19 09:03
**Context**: 100%

## What We Did
- Reviewed the design evolution from stealth subsurface mooring to tripod lander using:
  - [`Design Evolution Report - Shallow Water Hydrophone Mooring System.md`](src/01_Projects/2026-01_DMCR- marine-soundscape/notes/Design Evolution Report - Shallow Water Hydrophone Mooring System.md:1)
  - [`Comprehensive Engineering Report - Multi-Criteria Analysis and Design Specification for Shallow Water Hydrophone Rigs in Coral Reef Ecosystems.md`](src/01_Projects/2026-01_DMCR- marine-soundscape/source/Comprehensive Engineering Report - Multi-Criteria Analysis and Design Specification for Shallow Water Hydrophone Rigs in Coral Reef Ecosystems.md:14)
- Adopted the **Articulated 316L Tripod ("Reef-Sentry" lander)** as the baseline rig architecture via MCA/AHP.
- Captured key decisions and specs into the project task note:
  - Added a **Decision Log** and **Design Specification Snapshot** to [`Hydrophone rig design.md`](src/01_Projects/2026-01_DMCR- marine-soundscape/task/Hydrophone rig design.md:9), preserving the original mooring vs tripod comparison.
- Identified remaining open design decisions, especially around stealth/theft deterrence, site-specific parameterization (height, ballast, feet), and tracking.

## Pending
- [ ] Decide how to integrate **stealth and theft deterrence** into the tripod design (visual camouflage, absence/presence of surface markers, anti-lift or siting rules).
- [ ] Fix **standard hydrophone elevation** and whether to have one global height vs a small set of standard configs (e.g., crest vs channel rigs).
- [ ] Quantify **ballast requirements** and leg-fill strategy for DMCR sites (target submerged weight, fill material choices, per-site tuning rules).
- [ ] Finalize **foot design variants** for dominant substrate types (sand, rubble, dead coral pavement) within environmental constraints.
- [ ] Specify **flow shield implementation** (exact material, geometry, attachment) and **bungee isolation layout** (number of supports, pre-tension).
- [ ] Choose and integrate a **tracking / emergency recovery** strategy (keep AirTag concept vs acoustic release vs none, and acceptable loss rate).
- [ ] Draft a concise **diver SOP** for deployment, inspection, and recovery of the tripod rigs over the 4-month campaign.
- [ ] Define a **configuration/metadata scheme** for rigs (which parameters are fixed vs variable, and how recorded for later acoustic analysis).

## Next Session
- [ ] Update [`Hydrophone rig design.md`](src/01_Projects/2026-01_DMCR- marine-soundscape/task/Hydrophone rig design.md:9) to explicitly merge stealth/theft requirements from the mooring concept into the tripod spec (camouflage, no surface markers, emergency tracker policy).
- [ ] Parameterize the tripod design for at least **two canonical site types** (e.g., high-energy reef channel and more sheltered lagoon):
  - Target hydrophone height(s)
  - Ballast mass and leg-fill recipe
  - Preferred foot variant(s)
- [ ] Draft a first version of the **field SOP** (deployment + monthly servicing) referencing the tripod spec and DMCR operational constraints.

## Key Files
- [`Hydrophone rig design.md`](src/01_Projects/2026-01_DMCR- marine-soundscape/task/Hydrophone rig design.md:9)
- [`Design Evolution Report - Shallow Water Hydrophone Mooring System.md`](src/01_Projects/2026-01_DMCR- marine-soundscape/notes/Design Evolution Report - Shallow Water Hydrophone Mooring System.md:1)
- [`Comprehensive Engineering Report - Multi-Criteria Analysis and Design Specification for Shallow Water Hydrophone Rigs in Coral Reef Ecosystems.md`](src/01_Projects/2026-01_DMCR- marine-soundscape/source/Comprehensive Engineering Report - Multi-Criteria Analysis and Design Specification for Shallow Water Hydrophone Rigs in Coral Reef Ecosystems.md:14)

