---
name: sa-project-management
description: >
  KSA project leadership: business case, consultant appointments, delivery plan, risk/VM, contractor selection,
  disputes, programme/budget monitoring, and construction-to-occupation transition on fast-track Vision 2030 programmes.
user-invocable: true
disable-model-invocation: true
---

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Delivery plan, consultant selection, risk register, client reporting, disputes | `sa-project-management` | `sa-plan-of-work` |
| RIBA stage gates and checklists | `sa-plan-of-work` | — |
| Issue packs, RACI, transmittals | `sa-deliverables-workstages` | — |
| Procurement route / contract form selection | `sa-procurement-strategy` | — |
| Post-award FIDIC CA duties | `sa-tender-contract-administration` | — |
| Construction sequencing / look-ahead | `sa-construction-programme` | — |

## Halt conditions

- Stop and request data if **AHJ**, occupancy, or approval status is unknown (see `../../references/compliance.md`).
- Do not assert regulatory compliance without verified code edition and authority pathway.
- Contractual certification and legal interpretation → route to CA / counsel (`sa-tender-contract-administration`).

# KSA Project Management (Architectural Leadership)

## 1. Scope

Lead consultant and project-lead duties on KSA commissions: strategic brief through occupation transition. Emphasis on **overlapping fast-track**, **authority gateway ownership**, and **giga-project PMO** interfaces (NEOM, RSG, DGDA, Qiddiya, ROSHN).

Stakeholder map: `references/sa-construction-stakeholder-register.md`.

## 2. Business case & strategic brief

- Confirm vision, success criteria, and budget envelope.
- Identify primary AHJ and special-authority overlays early.
- Align RIBA stages to client payment milestones (`sa-fee-proposal-strategy`, `sa-plan-of-work`).

## 3. Consultant appointments

- Scope by discipline with deliverable list tied to workstages (`sa-deliverables-workstages`).
- SCE registration categories for AOR, structural, MEP where statutory.
- PI limits and duty-of-care framing (`sa-professional-indemnity`).

## 4. Delivery plan

- Master programme integrating design, permits, procurement, construction (`sa-consent-scheduling`).
- Critical path: SCD NOC and SBPS permit typically govern.
- Resource plan vs fee drawdown (`sa-project-resource-levelling`).

## 5. Risk, VM & design review

- Risk register: authority, commercial, technical, programme.
- VM workshops with documented SBC/SCD/Mostadam impact.
- Design review minutes with action owners and due dates.

## 6. Contractor selection & commercial control

- Support PQ/tender review with technical weighting (`sa-tender-contract-administration`).
- Validate contractor programme against permit and long-lead realities.
- Payment validation aligned with FIDIC certificates — architect advises; QS certifies per appointment.

## 7. Disputes & escalation

| Situation | Escalate to |
|-----------|-------------|
| Novel SBC / authority interpretation | AOR + specialist consultant |
| SCD / fire deadlock | `sa-fire-life-safety` + fire engineer |
| Contract claim / EOT quantum | CA + QS + legal |
| PI incident | Firm risk manager + broker |
| Enforcement on non-compliant works | AOR + `sa-unauthorised-building-works` |

## 8. Programme & budget monitoring

- Earned value vs design progress; flag fee burn (`sa-cashflow-debt-recovery`).
- Authority comment cycle tracking in CRM (T-05).
- Change control linked to SBPS amendment need.

## 9. Construction to occupation

- Mobilisation gate: `sa-site-establishment` before main works.
- Supervision cadence: `sa-site-supervision`.
- Handover chain: snagging → BCC/Is'har → Safety License (`sa-practical-completion-snagging`, `sa-certificate-of-compliance`, `sa-scd-licensing-compliance`).

## 10. Client reporting

- Monthly: progress, risks, authority status, budget snapshot.
- Gate reports at Stage 2, 4, tender, PC.
- Transparent assumptions on AHJ timelines.

## 11. Interfaces

| Partner | Interface |
|---------|-----------|
| QS | Cost plans, variations | `sa-cost-consultancy` |
| Contractor | RFIs, NCRs, programme | `sa-site-supervision` |
| PMO | Gate submissions | `sa-deliverables-workstages` |
| Authorities | SBPS, SCD | `sa-op-submission-strategy` |

## 12. Output checklist

- [ ] AHJ and stage stated
- [ ] Delivery plan or risk excerpt with owners
- [ ] Authority / commercial blockers identified
- [ ] Cross-links to specialist modules
- [ ] Assumptions on programme and budget declared
