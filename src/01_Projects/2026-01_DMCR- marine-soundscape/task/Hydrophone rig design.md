---
type: methodology
status: draft
title: Hydrophone rig design and deployment methodology (Reef-Sentry tripod/lander)
created: 2026-02-01
last_updated: 2026-02-24
project:
  - DMCR_Soundscape2026
tags:
  - hydrophone
  - subsea-deployment
  - rig-design
  - PAM
---

# Hydrophone rig design and deployment methodology (Reef-Sentry tripod/lander)

## Strategic context / objective

This methodology defines a bottom-mounted hydrophone rig architecture and field-deployment rules for shallow reef passive acoustic monitoring (PAM) under **DMCR_Soundscape2026**.

This document **consumes KO&I artifacts** produced from literature-derived notes:

- Synthesis: [[../output/Deployment configuration factors.md|Deployment configuration factors]]
- Evidence traceability: [[../output/DMCR_Hydrophone_Evidence_Index.md|DMCR_Hydrophone_Evidence_Index]]
- Field SOP: [[../output/Deployment location selection SOP EN-TH.md|Deployment location selection SOP EN-TH]]

## Conceptual framework: Mooring vs Tripod

We are choosing between a mooring-style “stealth tube” and a bottom-mounted tripod/lander. The core trade-off is: **operational convenience vs scientific stability + acoustic fidelity**.

### Summary comparison

|**Feature**|**Current "Stealth Tube" (Mooring)**|**Proposed "Stealth Tripod" (Lander)**|
|---|---|---|
|**Stability**|**Poor:** Sways with every wave (Inverted Pendulum).|**Excellent:** Rigidly fixed to seabed.|
|**Acoustics**|**Risk:** Flow noise & Strumming from rope.|**Superior:** No moving parts; precise sensor elevation.|
|**Entanglement**|**High:** Vertical rope catches debris/nets.|**Low:** Low profile, nothing to snag.|
|**Theft**|**Medium:** Can float to surface if cut.|**Low:** Stays on bottom; harder to spot.|
|**Deployment**|**Complex:** Requires adjusting rope length for tide.|**Simple:** Drop it and leave it.|

---

## Design choices and rationale

Primary design evidence trail:

- Literature factor synthesis: [[../output/Deployment configuration factors.md|Deployment configuration factors]]
- Evidence mapping: [[../output/DMCR_Hydrophone_Evidence_Index.md|DMCR_Hydrophone_Evidence_Index]]

### Decision log (accepted from [[../source/Comprehensive Engineering Report - Multi-Criteria Analysis and Design Specification for Shallow Water Hydrophone Rigs in Coral Reef Ecosystems.md|MCA Report]])

## Design Architecture Decision

- **Selected Architecture:** **Articulated Tripod (Lander)** (highest MCA score 4.05). This design best balances stability, acoustic fidelity, environmental stewardship, and deployability.
- **Rejected Alternatives:**
  - **Gravity Base (Sled/Block):** Excessive footprint, higher flow noise, sliding risk on reef slope.
  - **Helical/Pinned Anchor:** Strong but invasive and operationally complex for diver deployment.

## Criteria Weighting (AHP)

- **Structural Integrity:** 35%
- **Acoustic Performance:** 25%
- **Environmental Compatibility:** 20%
- **Operational Efficiency:** 20%

## Governing Environmental/Acoustic Constraints

- **High-energy shallow reef flow:** Drag-dominated regime (high KC). Minimize projected area and drag coefficient.
- **Flow-noise risk:** Turbulent boundary layer causes pseudo-sound below 100 Hz. Sensor must be elevated and/or shielded.
- **Benthic protection:** No chain scour. Point-contact only; avoid smothering live coral.

## Operational methodology

This section specifies the rig and how it is configured on a site, tying decisions back to the factor synthesis.

### Design specification snapshot (Reef-Sentry)

## Geometry

- **Base:** Equilateral triangle, **1.5 m** side length.
- **Total Height:** **1.2 m**.
- **Leg Angle:** **45–60°** from horizontal.

## Stability & Leveling

- **Adjustable Legs:** Telescopic/threaded extensions for leveling on uneven reef.
- **Articulated Foot Pads:** ~**100 mm** diameter, ball-and-socket with high-friction elastomer or **spike bolts** (~10 mm) for mechanical interlock.

## Materials & Corrosion Control

- **Primary Frame:** **316L Stainless Steel** (passivated welds).
- **Avoid:** Aluminum in contact with SS (galvanic risk) unless fully isolated.
- **Isolation Hardware:** **Delrin/HDPE** clamps and washers between sensor housing and frame.

## Acoustic Integration

- **Vibration Isolation:** **Bungee/shock-cord** suspension of hydrophone to decouple frame vibration.
- **Flow Shield:** Porous **ballistic nylon** or **open-cell foam (30–60 PPI)** cage around sensor to cut low-frequency flow noise.

## Ballast & Handling

- **Hollow Legs:** Transport empty; **fill in situ** with sand/lead shot for required submerged weight.
- **Safety Factors:** Design for **SF ≥ 1.5** against sliding and overturning under fouled condition (increased C_d and D).

## Deployment & Recovery

- **Diver Deployment:** Use **lift bag** for recovery; avoid manual heavy lifting.
- **Optional Diver-Less Recovery:** Acoustic release + pop-up buoy (future upgrade).

### Field configuration rules (site-specific adjustments)

These are the **controllable** configuration factors that must be set at the site (see also [[../output/Deployment configuration factors.md|Deployment configuration factors]]).

comparing how the **Mooring (Stealth Tube)** and the **Tripod (Lander)** handle them.

### 1. Vertical Adjustment (Sensor Height)

- **The Goal:** Position the hydrophone slightly above the highest nearby coral head to avoid "Acoustic Shadowing", while staying below the wave energy zone.

|**Feature**|**Mooring (Stealth Tube)**|**Tripod (Lander)**|
|---|---|---|
|**Adjustment Mechanism**|**Rope Length.** You cut the rope or adjust a knot/clamp to change the distance between the anchor and the tube.|**Mast Height.** You extend a central vertical pipe (the mast) upwards from the tripod base.|
|**Field Difficulty**|**Very Low.** Cutting rope is instant. You can even adjust it underwater if you use a sliding knot (like a taut-line hitch) before locking it.|**Medium.** Requires a "Telescoping" design (a smaller pipe sliding inside a larger one) secured with a through-bolt or pin.|
|**Precision**|**Low.** Even if you set the rope to 1.5m, currents will push the buoy over, reducing effective height (Pythagorean theorem). The sensor "bobs" in the current.|**High.** The sensor stays exactly where you pin it (e.g., 1.5m). It does not dip or sway.|
|**Winner**|**Tripod.** For scientific data, fixed geometry is superior. You can design a central PVC mast with pre-drilled holes every 10cm for rapid height selection on the boat.||

**Methodology rule (height):**

- Use selectable height increments (do not hard-code one height across all sites).
- Default working band: **~0.6–1.0 m above seabed**, adjusted for coral head height and wave zone.
- If edge effects or directivity bias is suspected, combine a height change with an orientation change (horizontal/reef-facing) rather than changing only one parameter.

### 2. Footprint & Leveling (Seabed Interaction)

- **The Goal:** Ensure the rig sits flat and stable on an uneven reef or sand patch without tipping over.

|**Feature**|**Mooring (Stealth Tube)**|**Tripod (Lander)**|
|---|---|---|
|**Adjustment Mechanism**|**None Needed (Self-Leveling).** The anchor block sits however it lands. The buoyancy of the tube pulls the system vertical automatically.|**Leg Length/Angle.** You must adjust individual leg lengths to compensate for uneven ground (e.g., one leg on a rock, two on sand).|
|**Field Difficulty**|**Zero.** The physics of buoyancy handles leveling for you. This is the mooring's biggest advantage.|**High.** A fixed tripod will wobble on uneven ground. You need **articulated feet** or **adjustable legs** (like camera tripod legs) to get it level.|
|**Risk**|**Dragging.** If the anchor isn't heavy enough or the footprint is too small, the whole system slides.|**Toppling.** If not leveled, a current can tip the tripod over.|
|**Winner**|**Mooring.** It is "set and forget" regarding the seabed angle. A tripod requires careful placement by a diver.||

**Methodology rule (environmental protection):**

- Point-contact feet only; avoid contact with live coral.
- Prefer stable sand/rubble patches when possible; document substrate and slope.

### 3. Ballast Tuning (Weight Adjustment)

- **The Goal:** Adding enough weight to resist drag forces (currents/waves) without making it too heavy to lift.

| **Feature**              | **Mooring (Stealth Tube)**                                                                                                                               | **Tripod (Lander)**                                                                                                          |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Adjustment Mechanism** | **Anchor Size.** You must cast the concrete block _before_ you get on the boat. Changing weight on-spot means adding loose weights (danger of clanking). | **Hollow Legs.** You can bring empty PVC legs and fill them with sand, lead shot, or chain _on the boat_ or even underwater. |
| **Field Difficulty**     | **Hard.** You are committed to the 40-50kg block you made. If it's too light, you're in trouble.                                                         | **Easy.** You can fine-tune stability by adding/removing weight inside the tubes.                                            |
| **Winner**               | **Tripod.** Hollow PVC structures allow you to transport a light frame and "ballast down" on site using local sand or lead diving weights.               |                                                                                                                              |

**Methodology rule (noise + stability):**

- Avoid loose weights that can clank; secure ballast internally or with constrained mounts.
- Design for stability under fouled conditions (biofouling increases drag), targeting SF ≥ 1.5 as baseline.

## Outputs and interpretation

This rig + deployment methodology is intended to produce:

- Stationary shallow-reef PAM recordings suited to comparing habitats and conditions, with explicit control of height/orientation/proximity.

Interpretation caveats:

- A single station is not automatically “reef-representative” in heterogeneous mosaics; representativeness depends on explicit placement intent and (when needed) replication.

## Limitations and future extensions

- Site-specific phase-cancellation / null patterns are not predictable from first principles; incorporate short test recordings where feasible.
- Quantitative treatment of “sediment noise” is not yet strong in the current evidence set; track as an evidence gap.
- Future upgrades may include acoustic release recovery or alternative mast geometries for faster field adjustment.
