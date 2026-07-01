---
name: sa-spatial-planning
description: >
  Expert guidance on KSA-specific planning and development controls. Covers site governance 
  (Municipality vs. Giga-project authorities), SBC 101/201 spatial alignment, and 
  navigation of the Saudi Building Permit System (SBPS) and MoMRAH regulations.
user-invocable: true
disable-model-invocation: true
---

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Zoning, plot, masterplan controls | `sa-spatial-planning` | `sa-lease-compliance` |
| Land / Krooki / easements | `sa-lease-compliance` | — |

## Halt conditions

- Stop and request data if **AHJ**, occupancy, or approval status is unknown (see `../../references/compliance.md`).
- Do not assert regulatory compliance without verified code edition and authority pathway.



# KSA Spatial Planning & Authority Governance

## 1. Regulatory Jurisdiction & Governance Framework
* **Standard Municipal Jurisdiction:** Identification of the relevant **Amanat/Baladiya** and the application of **MoMRAH** (Ministry of Municipal and Rural Affairs and Housing) standard planning regulations via the **Mada'en** or **Balady/SBPS** portals.
* **Special Development Zones:** Navigating the bespoke "Development Codes" and "Design Guidelines" of Giga-project entities (e.g., **NEOM, Red Sea Global, DGDA, Qiddiya**). These often override standard municipal heights and setbacks but require rigorous **No Objection Certificate (NOC)** workflows.
* **Industrial/Economic Zones:** Coordination with **MODON** or **Royal Commission (RC)** for manufacturing or specialized logistics sites.

## 2. Core Spatial Constraints & SBC Alignment
* **SBC 201 & 1001 Integration:** Early-stage verification of "Occupancy Classification" and "Construction Type" which dictate maximum allowable floor areas and heights before fire-separation becomes a massing driver.
* **Access & Civil Defence:** Alignment with **SBC 501** for fire apparatus access roads (widths, turning radii, and proximity to hydrants/facades) and **Saudi Civil Defence** site-wide requirements.
* **Public Realm & Setbacks:** Management of **"Sikka"** (alleys), setbacks for privacy in residential typologies, and integration with the **Saudi Green Initiative** (SGI) mandates for urban shading and landscaping.
* **Infrastructure Interfaces:** Coordinating with **SEC** (Power), **NWC** (Water/Sewage), and transport authorities for ROW (Right of Way) and utility corridor protection.

## 3. Information Requirements for Review
* **Site Context:** Georeferenced plot boundary (KML/CAD), topographic survey, and the specific **Governing Authority** (e.g., ROSHN, RCJU, or Riyadh Municipality).
* **Design Intent:** Concept massing, FAR (Floor Area Ratio) calculations, and proposed GFA (Gross Floor Area).
* **Authority Documentation:** Any existing **Preliminary Planning Approval**, "Site Planning Audit," or specific **Design Code** issued by the developer/authority.