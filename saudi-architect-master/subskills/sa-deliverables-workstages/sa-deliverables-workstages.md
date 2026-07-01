---
name: sa-deliverables-workstages
description: >
  KSA deliverables discipline: issue packs, transmittals, RACI, stage freeze, drawing scales, status codes,
  and lead-consultant coordination across RIBA-aligned workstages.
user-invocable: true
disable-model-invocation: true
---

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Deliverables register, issue pack, transmittal, RACI, stage freeze | `sa-deliverables-workstages` | `sa-plan-of-work` |
| RIBA stage gates and KSA authority mapping | `sa-plan-of-work` | — |
| Named artifact templates (T-01–T-24) | `../../references/templates/deliverables.md` | — |
| Tender / IFC drawing content | `sa-construction-documentation` | — |

## Halt conditions

- Stop and request data if **AHJ**, occupancy, or approval status is unknown (see `../../references/compliance.md`).
- Do not assert regulatory compliance without verified code edition and authority pathway.
- Authority submissions require registered professional sign-off — provide templates and checklists only.

# KSA Deliverables & Workstages

## 0. Issue-pack ready rule

No issue pack leaves the consultant team unless:

1. Cover sheet lists revision, status code, and recipient group.
2. Drawing index matches files in the transmittal.
3. Compliance gaps are logged (T-02) or explicitly deferred with owner.
4. Stage freeze log updated if the issue locks design parameters.

Template catalog: [`../../references/templates/deliverables.md`](../../references/templates/deliverables.md) (T-01–T-24).  
Stage gate shell: [`../../references/templates/stage-gate-checklist.md`](../../references/templates/stage-gate-checklist.md).

## 1. Stakeholder groups (recipient matrix)

| Group | Typical receive at | Format |
|-------|-------------------|--------|
| Client / developer | All stages | PDF + native where contracted |
| PMO (giga-project) | Gate reviews | Client portal + transmittal |
| AOR / QSCP | Permit stages | SBPS-ready sets |
| SCD / fire consultant | DD onward | Fire strategy + drawings |
| Contractor / CM | Tender onward | IFC + specs |
| QS | DD, tender, construction | BoQ-linked indices |
| Landlord / asset manager | Handover | O&M + as-built index |

## 2. Workstage deliverable definitions (RIBA-aligned)

| Stage | Architectural core | Multi-discipline |
|-------|-------------------|------------------|
| 0–1 | Brief, SOA, options | Feasibility services load |
| 2 | Concept report, massing | Early structural/MEP schematics |
| 3 | Schematic plans, elevations | Coordinated sections, plant strategy |
| 4 | DD plans, specs outline | SBC 601 narrative, fire report inputs |
| 5 | IFC drawings, spec | Tender BoQ alignment, SBPS index |
| 6 | Site issue sketches, MAR | Inspection reports, snag support |
| 7 | As-built, O&M index | BCC / Is'har support pack |

## 3. Status codes

| Code | Meaning | Use |
|------|---------|-----|
| **S1** | Work in progress | Internal only |
| **S2** | Client review | Not for permit |
| **S3** | Coordinated issue | Inter-discipline sign-off |
| **S4** | Issued for construction / permit | SBPS upload eligible |
| **S5** | As-built / record | Handover |

## 4. Drawing scales (metric — KSA practice)

| Drawing type | Typical scale |
|--------------|---------------|
| Site / masterplan | 1:500 – 1:2000 |
| Plans / elevations | 1:100 – 1:200 |
| Large floor plates | 1:200 – 1:500 |
| Details | 1:5 – 1:20 |
| Sections | 1:50 – 1:100 |

State scale bar and north point on every sheet; Arabic/English title block per client standard.

## 5. Lead consultant coordination

### 5.1 RACI (default pattern)

| Activity | Lead architect | Structural | MEP | Client |
|----------|----------------|------------|-----|--------|
| Issue pack approval | A | C | C | I |
| Stage freeze | A | C | C | A |
| SBPS submission index | A | C | C | I |
| SCD NOC package | C | I | C | I |
| VM workshop | C | C | C | A |

A = Accountable, C = Consulted, I = Informed.

### 5.2 Meeting cadence

- **Weekly** coordination during Stages 3–5 on fast-track.
- **Gate workshops** at Stage 2, 4, and pre-tender.
- **Authority comment** meetings within 48h of receipt where programme critical.

### 5.3 Stage freeze & change control

- Freeze registers: parameter, value, date, approver.
- Post-freeze changes → DCN / variation pathway (`sa-alterations-additions`, `sa-tender-contract-administration`).
- Never reissue S4 sets without revision clouding and transmittal.

### 5.4 VM integration

VE options documented with SBC / SCD / Mostadam impact before client decision (T-16 in deliverables catalog).

## 6. Transmittal minimum fields

- Project name, plot ref, issue date, revision
- Prepared by / checked by / approved by
- Purpose of issue (review / tender / permit / construction)
- File list with SHA or version ID where BIM
- Exclusions and pending items

## 7. Output checklist

- [ ] Recipient group and stage identified
- [ ] Status code applied consistently
- [ ] RACI or named owners for each deliverable
- [ ] Cross-reference to T-XX template if formal artifact required
- [ ] Freeze log updated if applicable
- [ ] Secondary route noted (e.g. `sa-op-submission-strategy` for SBPS)
