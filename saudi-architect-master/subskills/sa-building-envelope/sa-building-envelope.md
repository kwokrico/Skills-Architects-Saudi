---
name: sa-building-envelope
description: >
  Expert guidance on KSA-specific building envelope and façade design. Covers SBC 601 (Energy) 
  compliance, thermal bridging, sand/dust ingress prevention, extreme thermal expansion, 
  and Mostadam-aligned shading/glazing strategies for the Saudi climate.
user-invocable: true
disable-model-invocation: true
---

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Façade, thermal movement, dust ingress, waterproofing | `sa-building-envelope` | `sa-building-sustainability` |
| Mostadam credits / energy modelling | `sa-building-sustainability` | — |
| Structural frame selection | `sa-structural-systems` | — |

## Halt conditions

- Stop and request data if **AHJ**, occupancy, or approval status is unknown (see `../../references/compliance.md`).
- Do not assert regulatory compliance without verified code edition and authority pathway.



# KSA Building Envelope: High-Performance & SBC Compliance

## 1. Critical Saudi Climate & Regulatory Risks
- **SBC 601 & Mostadam Compliance:** Navigating mandatory U-value limits, SHGC (Solar Heat Gain Coefficient) requirements, and WWR (Window-to-Wall Ratio) restrictions.
- **Extreme Thermal Movement:** Managing expansion/contraction in high-diurnal ranges (e.g., Riyadh’s $45^{\circ}C$ vs $5^{\circ}C$ fluctuations) and long-span giga-project elevations.
- **Dust & Sand Ingress:** Detailing airtightness at interfaces, pressure-equalized rainscreens, and specialized gaskets to prevent "sand-logging" in tracks/cavities.
- **Coastal Corrosion (SBC 301):** Material selection (316L Stainless, Grade 5/6 Aluminum) for projects in NEOM, Red Sea Global, or Jeddah Corniche.

## 2. Architect-Led Technical Priorities
- **Passive Shading Strategy:** Prioritizing "Fabric First" (external fins, brise-soleil, mashrabiya) to reduce cooling loads before mechanical intervention.
- **Thermal Bridge Mitigation:** Specific detailing for slab edges, cantilevered balconies, and secondary steel fixings to prevent localized condensation and heat transfer.
- **Interface Integrity:** Ensuring the "Golden Thread" of the air barrier, vapor retarder, and insulation remains continuous across disparate systems (e.g., Curtain Wall to Precast).
- **BMU & Maintenance:** Integration of Cradle runs and Davit systems that account for high-frequency cleaning cycles due to dust storms.

## 3. Required Inputs for Analysis
- **Project Site:** Precise location (Inland/Riyadh vs. Coastal/Jeddah) to determine wind loads and corrosion class.
- **SBC 601 Target:** Are we following the *Prescriptive*, *Trade-off*, or *Performance* (Energy Modeling) path?
- **Facade System:** Stick system, Unitized, GRC cladding, or Masonry/EIFS?
- **Current Metrics:** Proposed WWR %, U-values for glazing/opaque walls, and any specific Mostadam credit targets (e.g., EN-01, EN-02).