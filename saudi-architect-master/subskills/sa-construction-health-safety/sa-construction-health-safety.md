---
name: sa-construction-health-safety
description: >
  KSA construction health and safety: site safety plan, risk assessments, municipality HSE liaison,
  accident reporting, CDM-equivalent duties on international projects — not building fire code.
user-invocable: true
disable-model-invocation: true
---

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Site safety plan, risk assessment, construction H&S, accident report, HSE audit | `sa-construction-health-safety` | — |
| Building fire strategy, SBC 501, SCD NOC design | `sa-fire-life-safety` | — |
| Site supervision, deviations, architect inspection | `sa-site-supervision` | — |
| Mobilisation, hoarding, TMP | `sa-site-establishment` | — |
| Project delivery plan, disputes | `sa-project-management` | — |

## Halt conditions

- Stop and request data if **AHJ**, occupancy, or approval status is unknown (see `../../references/compliance.md`).
- Do not assert regulatory compliance without verified code edition and authority pathway.
- **Not building fire code** — route fire strategy to `sa-fire-life-safety`.

# KSA Construction Health & Safety

## 1. Scope

Construction-phase H&S advisory for architect / lead consultant appointments. Covers site safety strategy, risk assessments, regulatory liaison, and accident response — **distinct from** SBC 501 fire engineering.

## 2. H&S strategy

- Project H&S plan aligned to contractor RAMS; architect reviews interface risks.
- Heat illness prevention: WBGT monitoring, work-rest cycles (KSA summer).
- Sandstorm protocol: stop work thresholds, plant securing.
- Fall protection for façade and core works — witness critical installs where contracted.

## 3. Risk assessments

| Topic | Typical control |
|-------|-----------------|
| Crane oversail | TMP + exclusion zone |
| Excavation | Shoring, telecom/SEC locate |
| Hot works | Permit-to-work, fire watch |
| Confined space | MEP pits, tanks |
| Night work | Lighting, noise curfew |

## 4. Regulatory liaison (KSA)

| Body | Interface |
|------|-----------|
| Municipality HSE / labour inspectorate | Site registration, inspections |
| SCD | Construction-phase fire watch — not design NOC |
| Client PMO | Giga-project zero-harm reporting |

International projects may impose **CDM-equivalent** duties — clarify in appointment (`sa-professional-indemnity`).

## 5. Accident investigation

1. Secure scene; preserve evidence.
2. Notify client and insurer per contract.
3. Root cause: immediate / underlying / systemic.
4. Architect: factual site observation only — not legal liability admission.
5. Corrective action tracker with close-out dates.

## 6. Site inspections

- Architect safety walk: focus on design-related hazards (temporary works, scaffold ties, edge protection).
- Record in site inspection report (T-14).
- Stop-work recommendation to client/CM if imminent danger — document in writing.

## 7. CDM-equivalent coordination (where applicable)

| Duty | KSA / intl. pattern |
|------|---------------------|
| Pre-construction info | PCI pack — `sa-site-establishment` |
| Principal designer | Lead designer hazard elimination |
| Principal contractor | Main contractor RAMS owner |
| F10-style notification | Municipality project registration |

## 8. Interfaces

- `sa-site-establishment` — welfare, hoarding, TMP safety
- `sa-site-supervision` — quality vs safety separation
- `sa-construction-programme` — night work, seasonal restrictions
- `sa-fire-life-safety` — active fire protection during construction

## 9. Output checklist

- [ ] Scope limited to construction H&S (not fire code design)
- [ ] Key hazards and controls listed
- [ ] Regulatory notification requirements noted
- [ ] Accident / inspection record template referenced (T-14)
- [ ] Escalation to client / CM / HSE stated
- [ ] Assumptions on appointment duties declared
