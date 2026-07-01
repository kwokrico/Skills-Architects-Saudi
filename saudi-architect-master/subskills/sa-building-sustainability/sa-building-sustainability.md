---
name: sa-building-sustainability
description: >
  Expert guidance on KSA sustainability compliance: Navigating Mostadam (Residential/Commercial) 
  certification, SBC 601 (Energy Conservation) mandates, and high-performance desert envelope 
  strategies for Vision 2030 giga-projects.
user-invocable: true
disable-model-invocation: true
---

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| SBC 601, Mostadam, envelope energy | `sa-building-sustainability` | `sa-building-envelope` |
| Detailed façade jointing | `sa-building-envelope` | — |

## Halt conditions

- Stop and request data if **AHJ**, occupancy, or approval status is unknown (see `../../references/compliance.md`).
- Do not assert regulatory compliance without verified code edition and authority pathway.



# KSA Building Sustainability (Mostadam & SBC 601 Mastery)

## 1. Critical Project Inputs
To provide a compliant Saudi-specific strategy, I need the following:
- **Project Governance:** Is this under a specific Municipality (e.g., Riyadh Momraah), a Giga-project authority (NEOM, RSG, Diriyah), or MODON?
- **Certification Target:** Mostadam Level (Green, Bronze, Silver, Gold, Diamond) and whether it is 'Design' or 'Construction' stage.
- **SBC 601 Baseline:** Building typology (Group R, B, M, etc.) to determine prescriptive vs. performance-based energy modeling requirements.
- **Climatic Data:** Specific KSA region (e.g., Zone 1 - Arid/Riyadh vs. Zone 2 - Humid/Jeddah) to calibrate thermal mass and latent cooling loads.
- **Envelope Strategy:** Current Window-to-Wall Ratio (WWR), U-values for glazing/Opaque assemblies, and Shading Coefficient (SC) targets.

## 2. KSA Technical Priorities & Hard Constraints
- **SBC 601 Compliance:** Mandating strict U-value limits and R-values for roof/wall assemblies. Note that SBC 601 (2023/24 updates) requires rigorous thermal bridging analysis in high-mass Saudi construction.
- **Extreme Solar Gain:** Passive cooling is paramount. External shading must be integrated into the architecture to reduce the Solar Heat Gain Coefficient (SHGC) before it hits the MEP systems.
- **Dust & Airtightness:** In KSA, infiltration isn't just about heat; it's about sand ingress. Mostadam credit requirements for air leakage testing (SBC 601 Section 505) are high-risk for fast-track handovers.
- **Water Scarcity:** Focus on TSE (Treated Sewage Effluent) for irrigation and high-efficiency fixture selections as per SBC 701 and Mostadam 'Water' category.

## 3. Professional Delivery Workflow
- **The "Evidence Index":** A live tracker mapping every SBC 601 requirement and Mostadam credit to a specific Drawing Number or Specification Section.
- **Early-Stage Modeling:** Shift from prescriptive paths to Whole Building Energy Simulation (e.g., IESVE/EnergyPlus) early in Schematic Design to optimize CAPEX vs. OPEX.
- **NOC Management:** Coordination with Saudi Civil Defence (SBC 501) to ensure high-performance insulation (e.g., PIR/Mineral Wool) meets fire propagation standards (NFPA 285 equivalent).
- **Construction Evidence (The Golden Thread):** Tracking site photos, material submittals (MARs), and delivery notes required for the Final Mostadam Certificate.

## 4. Cross-Reference Routing
- **Façade Systems & Thermal Breaks:** Refer to `sa-building-envelope`.
- **Statutory Permitting & SBPS Portal:** Refer to `sa-op-submission-strategy`.
- **MEP/Cooling Plants & SBC 801:** Refer to `sa-building-services`.

## References

Load `references/mostadam-sbc601.md` for Mostadam / SBC 601 alignment and evidence indexing.