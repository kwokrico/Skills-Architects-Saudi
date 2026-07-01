---
name: sa-daylighting-design
description: >
  Expert guidance on KSA-specific daylighting and glare control. Balances SBC 601 (Energy Conservation) compliance with visual comfort, Mostadam credits, and high-performance façade engineering for extreme desert environments.
user-invocable: true
disable-model-invocation: true
---

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Daylight, glare, SBC 601 daylight aspects | `sa-daylighting-design` | `sa-building-sustainability` |
| Full energy model | `sa-building-sustainability` | — |

## Halt conditions

- Stop and request data if **AHJ**, occupancy, or approval status is unknown (see `../../references/compliance.md`).
- Do not assert regulatory compliance without verified code edition and authority pathway.



# KSA Daylighting & Glare Control Strategy

## 1. Saudi Context & Regulatory Drivers
* **The Paradox:** High solar altitude and clear skies provide excessive illuminance (often >100,000 lux), making **glare control** more critical than daylight harvesting.
* **SBC 601 Compliance:** Strict limits on Solar Heat Gain Coefficient (SHGC) and Window-to-Wall Ratio (WWR). Daylighting must not compromise the building's cooling load or "Envelope Performance Factor."
* **Mostadam Alignment:** Targeting specific credits under "Health & Wellbeing" (IEQ-01: Daylighting) and "Energy" (EN-01: Energy Performance) for KSA giga-projects.

## 2. Technical Design Principles
* **Orientation-Specific Shading:** * **South:** Horizontal brise-soleil or deep overhangs (effective for high-angle summer sun).
    * **East/West:** Vertical fins or automated dynamic shading to mitigate low-angle, high-intensity solar gain.
* **Visual Comfort & Glare:** Implementation of Light Shelves to bounce light deep into the floor plate (e.g., in Ministry offices or Educational campuses) while maintaining a View Window with a lower Visible Light Transmittance (VLT) to reduce contrast glare.
* **Maintenance Reality:** All shading devices and "light pipes" must account for the **KSA Dust/Sand Environment**. Avoid horizontal surfaces that accumulate sand, which increases dead loads and degrades reflectance.

## 3. Integrated Delivery Workflow
* **Stage 1 (Concept/Schematic):** Early-stage Spatial Daylight Autonomy (sDA) and Annual Sunlight Exposure (ASE) modeling to justify WWR to the Client/Developer.
* **Stage 2 (Design Development):** Coordination with MEP Lead on "Daylight Responsive Dimming Controls" to ensure actual energy savings are realized in the cooling load.
* **Stage 3 (Authority Approval):** Preparing the "Daylight & Glare Analysis Report" required for Saudi Civil Defense (clearance of egress paths) and Municipality (Baladiya) sustainability components.

## 4. Required Inputs for Analysis
* **Project Location:** (e.g., Riyadh vs. Jeddah vs. NEOM—the latitude significantly impacts shading depth).
* **WWR & Glazing Spec:** Proposed U-value, SHGC, and VLT.
* **Program Requirements:** (e.g., Patient rooms in Healthcare vs. Gallery spaces in Cultural Institutions).
* **Surrounding Context:** Reflected glare from adjacent glazed towers or heat island impact from surrounding hardscape.