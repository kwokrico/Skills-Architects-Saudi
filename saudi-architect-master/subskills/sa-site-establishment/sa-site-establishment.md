---
name: sa-site-establishment
description: >
  KSA pre-construction mobilisation: hoarding, temporary works, utility liaison (SEC, NWC), municipality traffic management (TMP),
  STC/Mobily telecom protection, neighbour interfaces — gate before main works after PtC/building permit.
user-invocable: true
disable-model-invocation: true
---

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Site establishment, hoarding, mobilisation, TMP, telecom diversion, utility liaison | `sa-site-establishment` | `sa-consent-scheduling` |
| Building permit / PtC sequencing only | `sa-consent-scheduling` | — |
| Construction H&S strategy, accident reporting | `sa-construction-health-safety` | — |
| Main construction sequence / look-ahead | `sa-construction-programme` | — |

## Halt conditions

- Stop and request data if **AHJ**, occupancy, or approval status is unknown (see `../../references/compliance.md`).
- Do not assert regulatory compliance without verified code edition and authority pathway.
- **Cannot commence main works** without valid building permit / PtC — cross-check `sa-consent-scheduling`.

# KSA Site Establishment (Mobilisation)

## 1. Scope and position

Covers blueprint **site-establishment**, **traffic-coordination**, and **telecom-coordination** in one KSA module. Mobilisation between permit award and main construction start.

Deep refs:
- `references/sa-site-establishment-checklist.md`
- `references/sa-traffic-submission-types.md`
- `references/sa-telecom-licensed-works.md`

## 2. Pre-construction readiness gate

| Prerequisite | Verify |
|--------------|--------|
| Building permit / PtC issued | `sa-consent-scheduling` |
| Site possession / handover from client | Contract programme |
| SEC / NWC service orders in progress | Utility NOC tracker |
| Hoarding / site permit approved | Municipality |
| TMP approved (if public frontage) | Baladiya / traffic dept |
| Telecom protection plan agreed | STC / Mobily |

## 3. Hoarding design and permits

- Municipality site permit; NEOM/RSG may require branded hoarding and 3D visuals.
- Wind load and sand accumulation on temporary fencing — anchor design for desert exposure.
- Pedestrian segregation and prayer-area access where public realm affected.
- Interface with TMP for lane closures and bus stop relocations.

## 4. Temporary works

- Site offices, welfare, batching (if allowed), crane bases.
- Sandstorm protection for open excavations and stored materials.
- Heat stress welfare: shaded rest, hydration (link `sa-construction-health-safety`).
- Prayer facilities per labour camp regulations.

## 5. Utility liaison

| Utility | Early action |
|---------|--------------|
| **SEC** | Temporary power, MV route, substation handover dates |
| **NWC** | Temporary water, sewer diversion, TSE if landscape |
| **Fuel / LPG** | If generators — local permit |

Track parallel NOCs (T-12 in deliverables catalog).

## 6. Traffic coordination (municipality TMP)

- **Planning-stage TIA** vs **construction TMP** — do not conflate.
- Riyadh Metro ROW: coordinate with transport authority for crane oversail and haul routes.
- Haul route restrictions during peak prayer / event windows.
- See `sa-traffic-submission-types.md`.

## 7. Telecom coordination (STC / Mobily)

- Licensed contractor for excavation near fibre/copper plant.
- Diversion sequencing before deep excavation or piling.
- Protection slabs and duct banks in permanent works drawings.
- See `sa-telecom-licensed-works.md`.

## 8. Authority & neighbour interfaces

- Baladiya site inspector notification.
- Landlord / compound management for access and noise windows.
- RC / heritage buffer zones — restricted working hours (`sa-heritage-conservation`).

## 9. PCI pack (pre-construction information)

Assemble for contractor / CM:
- Permit copies, approved drawings index
- Utility drawings, TMP, telecom protection plan
- Site constraints, survey, geotechnical summary
- Authority contacts (`sa-construction-stakeholder-register.md` in project-management)

## 10. Programme hooks

- Mobilisation typically 4–8 weeks post-PtC on urban sites; longer if major utility diversion.
- Align crane erection with TMP lane closure windows.
- Ramadan: reduced authority processing for street works permits.

## 11. Output checklist

- [ ] PtC / permit status confirmed
- [ ] Hoarding and site permit pathway listed
- [ ] TMP and telecom plans referenced with owners
- [ ] Utility NOC status table
- [ ] PCI index or mobilisation Gantt assumptions
- [ ] Cross-links to `sa-consent-scheduling`, `sa-construction-health-safety`
