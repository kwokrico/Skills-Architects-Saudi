---
name: sa-procurement-strategy
description: >
  KSA procurement route selection: Traditional DBB, Design-Build, EPC, management contracting; FIDIC and NEC mapping;
  risk allocation; sandstorm, heat, Ramadan/Hajj EOT treatment by contract type.
user-invocable: true
disable-model-invocation: true
---

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Procurement route, D&B vs DBB vs EPC, contract form selection, risk allocation | `sa-procurement-strategy` | `sa-tender-contract-administration` |
| Tender issue, variations, FIDIC CA duties, EOT assessment | `sa-tender-contract-administration` | — |
| Fee bid / appointment scope | `sa-fee-proposal-strategy` | — |
| Cost plan, BoQ, valuations | `sa-cost-consultancy` | — |

## Halt conditions

- Stop and request data if **AHJ**, occupancy, or approval status is unknown (see `../../references/compliance.md`).
- Do not assert regulatory compliance without verified code edition and authority pathway.
- Halt route recommendation if client objectives and risk appetite are unknown.

# KSA Procurement Strategy

## 1. When to use

Before tender documentation is frozen. Defines **how** the project is procured and **which contract** allocates programme, design, and authority risk.

Deep refs: `references/sa-procurement-routes-comparison.md`, `references/sa-weather-eot-by-procurement.md`.  
Template: [`../../references/templates/tender-route-recommendation.md`](../../references/templates/tender-route-recommendation.md).

## 2. Route decision guide

| Client priority | Favoured route | Watch-out (KSA) |
|-----------------|--------------|-----------------|
| Design control, competitive price | Traditional DBB + FIDIC Red | SBPS changes = variation + re-approval |
| Single point, fast programme | D&B FIDIC Yellow / Silver | Employer’s Requirements must lock SBC/SCD |
| Maximum speed, performance risk to contractor | EPC / FIDIC Silver | Limited employer design change |
| Phased packages | Management contracting / multiple primes | Interface risk at MEP/façade |
| Giga-project collaborative | NEC4 ECC (where adopted) | Pain/gain and early warning culture |

## 3. Comparison matrix (summary)

See full matrix in `sa-procurement-routes-comparison.md`.

| Route | Design risk | Authority delay risk | Typical KSA use |
|-------|-------------|---------------------|-----------------|
| DBB | Consultant | Shared | Municipal, mid-rise |
| D&B | Contractor | Contractor (if ER complete) | Hospitality, residential towers |
| EPC | Contractor | Contractor | Industrial, MODON, utilities-heavy |
| NEC target cost | Shared | Shared | NEOM / ROSHN pilots |

## 4. Contract form map

| Route | Common KSA form | Architect role |
|-------|-----------------|----------------|
| DBB | FIDIC Red Book | Lead designer + optional CA |
| D&B | FIDIC Yellow Book | ER author; limited post-award |
| EPC | FIDIC Silver Book | Employer’s Requirements only |
| Public / ECA | Government standard | Specified supervision only |

Particular Conditions often shift risk — document in tender strategy memo.

## 5. Weather & seasonal delay (KSA)

Sandstorms, extreme heat, Ramadan, and Hajj affect productivity and authority processing. Route-specific treatment: `sa-weather-eot-by-procurement.md`.

- **FIDIC:** Sub-Clause 8.4 / 8.5 — exceptional events vs employer risk events.
- **NEC:** compensation events for weather measurements if Z clauses included.

## 6. Programme / authority interface

- Design changes under D&B still trigger **SBPS amendment** — price risk to contractor if ER incomplete.
- Early contractor involvement (ECI) can secure long-leads (façade, lifts) before permit.

## 7. Stage-gate outputs

| Stage | Procurement output |
|-------|-------------------|
| 1 | Route recommendation memo |
| 2 | Preliminary ER or scope split |
| 4 | Tender strategy + evaluation criteria |
| 5 | Award recommendation |

## 8. Cross-references

- Post-award: `sa-tender-contract-administration`
- Programme: `sa-consent-scheduling`, `sa-construction-programme`
- Commercial: `sa-cost-consultancy`, `sa-project-management`

## 9. Output checklist

- [ ] Client objectives and risk appetite stated
- [ ] Recommended route with contract form
- [ ] Risk allocation table (design, authority, weather, ground)
- [ ] EOT / weather pointer to seasonal memo
- [ ] SBPS / SCD ripple effect on variations noted
- [ ] Assumptions declared
