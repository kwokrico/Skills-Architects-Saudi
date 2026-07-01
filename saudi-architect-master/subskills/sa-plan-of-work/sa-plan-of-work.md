---
name: sa-plan-of-work
description: >
  KSA plan-of-work: RIBA Stages 0–7 mapped to Saudi fast-track gates, SBPS milestones, giga-project PMO overrides,
  and stage-gate checklists for Vision 2030 delivery.
user-invocable: true
disable-model-invocation: true
---

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| RIBA stage, plan of work, stage gate, Stage 0–7 tasks | `sa-plan-of-work` | `sa-deliverables-workstages` |
| Issue pack, RACI, transmittal, drawing scales | `sa-deliverables-workstages` | — |
| Approval programme / permit sequencing | `sa-consent-scheduling` | — |
| Project delivery plan, disputes, client reporting | `sa-project-management` | — |

## Halt conditions

- Stop and request data if **AHJ**, occupancy, or approval status is unknown (see `../../references/compliance.md`).
- Do not assert regulatory compliance without verified code edition and authority pathway.
- Do not apply UK RIBA PSC or UK Building Regulations by default — substitute KSA authorities and SBC.

# KSA Plan of Work (RIBA 0–7 Adaptation)

## 1. Core position

- **RIBA Stages 0–7** provide the neutral workstage spine; **KSA delivery** overlays SBPS/Baladiya gates, SCD NOC cycles, and giga-project PMO gateways.
- Fast-track programmes **overlap stages** — document which gates are frozen vs concurrent.
- Full per-stage checklists: `references/sa-pow-stages-0-7.md`. Stage-gate shell: `../../references/templates/stage-gate-checklist.md`.

## 2. Stage mapping (RIBA ↔ KSA ↔ deliverables)

| RIBA | KSA typical gate | Primary authority touchpoint | Key sub-skill |
|------|------------------|------------------------------|---------------|
| **0** Strategic Definition | Business case, AHJ confirmation | Client / land authority | `sa-project-management` |
| **1** Preparation & Brief | SOA, code basis, procurement route | Internal + `sa-building-programming` | `sa-building-codes` |
| **2** Concept Design | Preliminary massing, SCD in-principle | Baladiya / special entity | `sa-concept-design` |
| **3** Spatial Coordination | Schematic lock, Mostadam brief | SBPS preliminary | `sa-spatial-planning` |
| **4** Technical Design | DD coordination, SBC 601 lock | SCD conceptual NOC | `sa-construction-documentation` |
| **5** Manufacturing & Construction | IFC, PtC / building permit | SBPS full BP | `sa-op-submission-strategy` |
| **6** Handover | TOC, snagging, utility energization | SCD + Baladiya | `sa-practical-completion-snagging` |
| **7** Use | DLP, BCC / Is'har, Safety License | SCD closeout | `sa-scd-licensing-compliance` |

## 3. KSA substitution guide (never apply UK defaults)

| UK term | KSA substitute |
|---------|----------------|
| Building Control Full Plans | SBPS building permit / special-authority design gate |
| Planning permission | Municipal masterplan / subdivision / organizational survey |
| FSO / Approved Doc B | SBC 501 + SCD NOC |
| Part L | SBC 601 + Mostadam |
| CC (completion certificate) | Is'har / BCC + SCD Safety License |

## 4. Stage gate procedure

1. **Inputs complete** per `sa-pow-stages-0-7.md` for the target stage.
2. **Compliance check** — `../../references/compliance.md`; occupancy and AHJ confirmed.
3. **Issue pack** — `sa-deliverables-workstages` transmittal with status codes.
4. **Approver sign-off** — client gateway + AOR where statutory.
5. **Freeze log** — record what is locked; route changes via DCN (`sa-alterations-additions`).

## 5. Role routing by stage

| Role | Stages 0–2 | Stages 3–4 | Stages 5–6 | Stage 7 |
|------|------------|------------|------------|---------|
| Lead consultant | Brief, RACI | Coordination freeze | IFC quality | Handover index |
| Architect / AOR | Concept, code basis | DD, submissions | Site supervision | As-built / BCC pack |
| PM | Programme, risk | Gateway workshops | Construction reporting | DLP admin |
| QS | Feasibility budget | Cost plan update | Valuations | Final account |
| Fire engineer | Early strategy | SCD NOC package | IST support | Safety License |

## 6. Per-stage KSA reminders

- **Stage 2:** Lock FAR/coverage against organizational survey or masterplan — not planning alone on lease plots (`sa-lease-compliance`).
- **Stage 3:** SBC 501 workshop before façade freeze; sand/dust detailing (`sa-building-envelope`).
- **Stage 4:** Mostadam credit register aligned with SBC 601 envelope targets.
- **Stage 5:** Golden Thread MAR trail starts; SASO long-leads on order.
- **Stage 6:** Partial OP only where AHJ permits; never conflate contractual PC with Is'har.
- **Stage 7:** SCD Safety License is separate from architectural snagging closeout.

## 7. Giga-project overrides

NEOM, RSG, DGDA, Qiddiya, ROSHN often impose **additional design gates** (envelope, landscape, ICT) that run parallel to RIBA stages. Map client PMO gate IDs to RIBA stage in the project execution plan.

## 8. Output checklist

- [ ] Stage ID and RIBA mapping stated
- [ ] AHJ and procurement route confirmed
- [ ] Gate inputs / outputs listed with owners
- [ ] Frozen vs concurrent workstreams documented
- [ ] Cross-links to `sa-deliverables-workstages` and `sa-consent-scheduling`
- [ ] Assumptions declared where AHJ pathway unverified
