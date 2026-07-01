---
name: sa-cost-consultancy
description: >
  KSA quantity surveying scope: feasibility, benchmarking, cost plans, VM, BoQ, tender evaluation, variations,
  valuations, claims support, and final account — CESMM-adapt / local BOQ practice.
user-invocable: true
disable-model-invocation: true
---

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Cost plan, BoQ, tender pricing, variation estimate, valuation, final account | `sa-cost-consultancy` | `sa-tender-contract-administration` |
| FIDIC certificates, CA determination, EOT legal position | `sa-tender-contract-administration` | — |
| Procurement route selection | `sa-procurement-strategy` | — |
| VE memo with code/SCD impact | `sa-deliverables-workstages` (T-16) + `sa-building-codes` | — |

## Halt conditions

- Stop and request data if **AHJ**, occupancy, or approval status is unknown (see `../../references/compliance.md`).
- Do not assert regulatory compliance without verified code edition and authority pathway.
- Certification sign-off interface → cross-check CA appointment (`sa-tender-contract-administration`).

# KSA Cost Consultancy (QS)

## 1. Scope

Full QS service on architectural commissions: feasibility through final account. KSA context: **SDR/local content** cost risk, **import duty** on specialist façade/MEP, **authority-driven variations** (SBPS resubmit).

## 2. Feasibility, benchmarking & budget

- Elemental cost plan vs typology benchmarks (hospitality, residential tower, compound).
- Plot infrastructure allowances (SEC, NWC, telecom).
- Contingency: authority comments, geotechnical unknowns, FX on imported systems.

## 3. Design-stage cost control

- Cost plans at Stage 2, 3, 4 aligned to `sa-plan-of-work` gates.
- Cash-flow forecast vs client milestones (`sa-cashflow-debt-recovery`).
- Track Mostadam / SBC 601 premium vs base envelope.

## 4. Risk & VM

- VM workshops with architect — document SBC 501, SCD, Mostadam impacts (T-16).
- Option costing for modular vs in-situ (`sa-mic-dfma`).

## 5. Cost plans, cash flow & BoQ

- Measurement: CESMM-adapt or client BOQ format; agree rules pre-tender.
- BoQ coordination with IFC (`sa-construction-documentation`).
- Provisional sums for authority-dependent items.

## 6. Tender issue & evaluation

- Tender comparison report (architect technical + QS commercial).
- Normalization for SDR compliance, programme, and methodology.
- Clarifications log — no post-bid scope creep without VO pathway.

## 7. Post-contract — variations, valuations, claims

| Activity | QS lead | Architect interface |
|----------|---------|---------------------|
| Variation estimate | Yes | Design intent, SBPS need |
| Interim valuation | Yes | Site measure with supervision |
| EOT cost | Support | Cause analysis with PM |
| Final account | Yes | As-built scope confirmation |

**KSA nexus:** Variations affecting fire or occupancy → budget **and** permit amendment.

## 8. Interfaces

- **CA / architect:** FIDIC Sub-Clause 13, 14 — QS certifies per appointment.
- **Contractor:** BOQ queries, site quantities.
- **Client:** Cost reports at gate reviews (`sa-project-management`).

## 9. Output checklist

- [ ] Stage and cost plan revision stated
- [ ] Measurement basis documented
- [ ] Contingency and risk items listed
- [ ] Authority / SBC ripple on variations noted
- [ ] Certification boundary (QS vs CA) clear
- [ ] Assumptions on rates and FX declared
