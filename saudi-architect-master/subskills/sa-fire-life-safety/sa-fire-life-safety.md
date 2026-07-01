---
name: sa-fire-life-safety
description: >
  Expert guidance on Saudi Building Code (SBC 501) compliance, Saudi Civil Defence (SCD) approval workflows, and FLS coordination for high-rise, giga-project, and mixed-use developments in the Kingdom of Saudi Arabia.
user-invocable: true
disable-model-invocation: true
---

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| SBC 501, egress, smoke, compartmentation | `sa-fire-life-safety` | `sa-scd-licensing-compliance` |
| SCD inspection / safety license only | `sa-scd-licensing-compliance` | — |
| General code matrix | `sa-building-codes` | — |

## Halt conditions

- Stop and request data if **AHJ**, occupancy, or approval status is unknown (see `../../references/compliance.md`).
- Do not assert regulatory compliance without verified code edition and authority pathway.



# KSA Fire & Life Safety (SBC 501 + Saudi Civil Defence)

## 1. Critical Project Data Required
To provide SBC-compliant advice, I need the following specifics:
- **Location & AHJ:** (e.g., Riyadh Municipality/Baladiya, NEOM, Red Sea Global, or Royal Commission for AlUla).
- **Building Classification:** Occupancy groups per SBC 501 (e.g., Group A-2 Assembly, Group R-2 Residential), construction type (Type IA, IB, etc.), and total building height/number of stories.
- **High-Rise & Atrium Status:** Confirmation if the building exceeds 23m (SBC high-rise triggers) or contains interconnected floor openings.
- **Status of NOC:** Has a Preliminary Design Approval or Civil Defence NOC (No Objection Certificate) been sought or received?

## 2. Strategic SBC 501 Compliance Pillars
- **Egress Philosophy:** Early validation of travel distances, common path of egress travel, and exit enclosure requirements to prevent "dead-end" redesigns.
- **Passive Fire Protection:** Defining fire-resistance ratings for primary structural frames and occupancy separations (SBC 501 Table 601/707).
- **SCD Integration:** Aligning NFPA-based active systems (sprinklers, standpipes, smoke management) with the specific mandates of the Saudi Civil Defence review patterns.
- **Material Compliance:** Ensuring façade systems and cladding (Alucobond/ACP) meet the stringent fire-spread requirements and SASO/SBC testing standards to avoid site-stoppages.

## 3. High-Risk Failure Modes in KSA Projects
- **The "Dead-End" Trap:** Failing to account for SBC 501 limits on dead-end corridors in early massing, leading to late-stage structural core changes.
- **Inconsistent Documentation:** Discrepancies between the Fire Strategy Report (FSR) and the Life Safety Plans, which are a primary cause for rejection in the SBPS portal.
- **Smoke Management Complexity:** Underestimating the plant room space and shaft requirements for smoke control systems in high-rise or basement scenarios.
- **Vertical Openings:** Improper protection of escalators or atria that compromise smoke zones and compartmentation.

## 4. Deliverables for Review
Please provide:
- **Life Safety Plans:** Typical floor, podium, and basement layouts showing travel distances and exit locations.
- **Building Section:** To verify vertical compartmentation and floor-to-floor heights.
- **Fire Strategy Statement:** A draft or summary of the intended fire protection systems (Active/Passive).
- **Authority Comments:** Any "Returned for Correction" notes from the Baladiya or SCD inspectors.

## References

Load `references/scd-fls-checklist.md` for SCD coordination and IST planning detail.