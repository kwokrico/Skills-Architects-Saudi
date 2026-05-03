---
name: sa-building-services
description: >
  Architectural leadership of MEP/ICT/Fire coordination in KSA. Focuses on SBC compliance, SCD life safety integration, desert-resilient filtration, and giga-project fast-track spatial management using metric units exclusively.
user-invocable: true
---

# KSA Building Services: Architectural & Regulatory Coordination

**Skill Purpose:**  
When users query Saudi architectural projects involving MEP/Fire/ICT coordination, invoke this skill to deliver **SBC-aligned** analysis, identify high-risk coordination conflicts, generate compliance checklists, and provide actionable resolutions optimized for desert conditions and giga-project scales.

## Capabilities
- Validate architectural layouts against **SBC 2022** (particularly SBC 301, 501, and 601) and **SCD 2023** requirements.
- Analyze spatial efficiency, life safety, envelope performance, and desert resilience.
- Produce coordination conflict matrices, compliance gap analyses, and **Mostadam** rating support.
- Output structured reports with metric units (m², kW, L/s, Pa, etc.) and practical mark-up guidance.

## Constraints
- Regulatory scope limited to current **SBC 2022** and **SCD 2023**; flag local Amana variations (Riyadh vs. Jeddah).
- Metric units only — automatically convert any imperial inputs.
- No structural calculations (FEA, wind loads, etc.).
- Optimized for large-scale projects (floor plates > 5,000–10,000 m²+).

## Input Schema
```yaml
required:
  - project_type: string          # "residential", "hospitality", "commercial", "high-rise", "giga-project"
  - key_docs: array[string]       # List of provided documents
  - constraints: object
      sbc_target: string
      scd_noc_status: string
      mostadam_level: string
      cooling_load_kw: number
      floor_plate_m2: number
```

## Output Schema
Structured Markdown with:
- Regulatory compliance status
- Coordination conflicts (with risk, impact, resolution)
- Prioritised action items
- Required diagrams / next steps

---

## 1. Core Architectural Focus Areas (SBC-Aligned)

- **Spatial Strategy & Efficiency:** Optimise Gross-to-Net ratios (target ≤ 75%) by vetting MEP plant rooms, risers (Ø300–600 mm), and distribution zones against **SBC 301** occupancy loads (0.65–1.0 m²/person).
- **Life Safety & Fire Protection:** Ensure compartmentation, smoke management, and egress align with **SBC 501** (max fire area 2,500 m², 2-hr ratings) and **SCD** requirements.
- **Envelope Integrity:** Detail MEP penetrations for thermal bridging control and air tightness (≤ 3 m³/h·m² @50Pa per **SBC 601**), supporting **Mostadam** targets.
- **Desert Durability:** Coordinate sand-trap louvres (velocity ≤ 2.5 m/s), MERV 13+ multi-stage filtration, and AHU placement to resist dust ingress and extreme loads (150–250 W/m² cooling).

## 2. High-Risk Saudi Coordination Conflicts

| Conflict                    | SBC/SCD Reference     | Key Metric                  | Typical Mitigation                          |
|-----------------------------|-----------------------|-----------------------------|---------------------------------------------|
| Headroom vs. Gravity Drainage | SBC 301.4            | Ceiling void ≥ 2.7 m       | Limited false ceiling drops (≤ 400 mm)     |
| Façade Louvre Integration   | SBC 601.5            | Free area ≥ 50%            | Reinforced mullions + aesthetic screening  |
| Acoustics & Vibration       | SBC 301 App. B       | Vibration ≤ 0.2 mm/s       | Isolation pads, inertia blocks, flexible connections |
| Shaft Pressurisation        | SCD 4.2.3            | 50 Pa differential         | Dedicated pressurisation fans sized at 0.35 × floor area (m²) |

**Additional Conflicts to Flag:**
- Roof-top chiller noise/vibration near Majlis or sleeping areas in heavy RC structures.
- Massive intake/exhaust requirements conflicting with architectural façade intent.

## 3. Regulatory Compliance Checklist Template

**SBC 501 Fire Safety:**
- □ Fire pumps: 100% + 50% standby capacity
- □ Smoke vents: minimum 2.5% of roof area
- □ Egress: 1 stair per 2,500 m², clear width 1.2 m minimum

**SCD NOC Requirements:**
- □ Hydraulic calculations submitted
- □ Fire officer access paths (min 1.5 m wide)
- □ LPG/storage separation ≥ 15 m

**Mostadam / Energy:**
- □ U-values ≤ 0.35 W/m²K
- □ Air tightness verification plan

## 4. Essential Inputs for Accurate Analysis
- MEP Basis of Design (cooling load kW/m², system type, fire water storage)
- Authority status (SCD NOC, Mostadam target level)
- Structural constraints (transfer beam locations, slab depths 200–400 mm)
- Site utility points (SEC, NWC pressures)

## Execution Workflow
1. Parse provided inputs and documents.
2. Cross-reference against SBC/SCD tables and desert-specific parameters.
3. Identify conflicts and compliance gaps.
4. Generate structured report with actionable recommendations.
5. Request missing data (e.g., exact cooling load or floor-plate sizes) if needed.

**Ready to analyse your KSA project — provide project type, key metrics, and documents.**