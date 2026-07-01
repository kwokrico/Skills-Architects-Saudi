---
name: sa-building-typology
description: >
  Comprehensive KSA building typologies and benchmarks (High-rise, Giga-projects, Hospitality, Healthcare). 
  Integrates SBC compliance logic, Saudi Civil Defence (SCD) requirements, and fast-track delivery 
  workflows specific to the KSA regulatory landscape.
user-invocable: true
disable-model-invocation: true
---

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Asset class strategy (hospitality, residential, mixed-use) | `sa-building-typology` | `sa-concept-design` |
| Code occupancy classification detail | `sa-building-codes` | — |

## Halt conditions

- Stop and request data if **AHJ**, occupancy, or approval status is unknown (see `../../references/compliance.md`).
- Do not assert regulatory compliance without verified code edition and authority pathway.



# KSA Building Typology & Delivery Benchmarks

## 1. High-Rise & Mixed-Use (Urban KSA Focus)
- **SBC 501 & Life Safety:** High-rise classification triggers stringent smoke management and pressurized exit enclosures. Podium/tower interfaces must address structural fire separation and "transfer floor" service coordination.
- **Vertical Transportation (VT):** KSA-specific peak occupancy factors often exceed international benchmarks; VT analysis must be locked during Schematic Design (SD) to fix the core footprint.
- **Wind & Thermal:** High-performance façades must account for extreme diurnal temperature swings and sand-abrasion resistance (ASTM/SASO standards).

## 2. Hospitality & Luxury Resorts (Red Sea / NEOM Context)
- **Logistics:** Strict BOH (Back of House) / FOH (Front of House) separation is a non-negotiable for luxury operators in KSA. 
- **Coastal/Desert Durability:** Focus on Grade 316L stainless steel, specialized coatings for corrosion (C5-M environment), and dust-ingress prevention for MEP intakes.
- **Mostadam/LEED:** Compliance with SBC 601 (Energy Conservation) and Mostadam 'Green Key' credits is now standard for giga-project funding.

## 3. Healthcare & Education (Social Infrastructure)
- **SBC 1101 (Health) & SBC 1001 (Accessibility):** Patient flow and universal access must meet the latest Ministry of Health (MoH) and SBC requirements.
- **Modular Delivery:** Increasing shift toward Design for Manufacturing and Assembly (DfMA) to meet aggressive 2030 deadlines.

## 4. Giga-Project Patterns (The Line, Qiddiya, Diriyah)
- **Authority Regime:** Understanding if the project sits under a Special Project Tech Committee or standard Baladiya (Municipality) workflows.
- **Fast-Track Risks:** Managing "Long Lead Procurement Items" (LLPI) during the Design Development (DD) phase to ensure site readiness.

## 5. Critical Inputs Required for Consultation
- **Typology & GFA:** (e.g., 50-storey Mixed-use, 300-key Resort).
- **Location & Authority:** (e.g., Riyadh/Baladiya, NEOM/NCA, Red Sea Global).
- **Current Stage:** (Concept, SD, DD, or Tender).
- **Procurement Route:** (e.g., FIDIC Red Book, Design-Build, or EPC).