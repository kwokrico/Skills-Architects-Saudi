# Verification prompts (golden questions)

Run after changes to the suite. Formal eval definitions: [`evals/evals.json`](evals/evals.json). Eval outputs: sibling [`saudi-architect-master-workspace/`](../saudi-architect-master-workspace/).

Expectations follow GUIDELINE §7–8 and the Blueprint Section 8 playbook.

## 1. Routine — quick reference only

**Prompt:** "What authorities typically govern a high-rise residential tower permit in Riyadh, and what are the first three documents I should lock before schematic design?"

**Pass if:**

- Answers from master foundation (AHJ, SBPS, SCD) without loading every sub-skill
- Asks for occupancy / AHJ if assuming details
- No invented SBC clause numbers

## 2. Deep route — correct sub-skill

**Prompt:** "Our SCD integrated systems test failed on smoke pressurization. What should we fix before re-inspection, and which module owns this?"

**Pass if:**

- Routes to `sa-scd-licensing-compliance` and/or `sa-fire-life-safety`
- Cites halt conditions if IST records or NOC status unknown
- May reference `references/scd-closeout-checklist.md` when loaded via dispatcher

## 3. Compliance halt — must not silently comply

**Prompt:** "We changed egress on site without SBPS amendment. Can we take TOC next week and issue the occupancy certificate?"

**Pass if:**

- **Halts** or flags SCD red line per `references/compliance.md`
- Does not affirm occupancy readiness
- Offers remediated pathway (as-built amendment, resubmission)

## 4. Procurement route — correct sub-skill

**Prompt:** "Client wants fastest programme on a NEOM hospitality tower. Should we go DBB or EPC, and what contract risks should we flag before tender?"

**Pass if:**

- Routes to `sa-procurement-strategy`
- Compares routes with KSA SBPS/SCD ripple on design changes
- Does not give legal advice on Particular Conditions

## 5. Deliverables / issue pack — correct sub-skill

**Prompt:** "We are at DD freeze next week. What should be in the issue pack and who signs off on the transmittal?"

**Pass if:**

- Routes to `sa-deliverables-workstages`
- Mentions RACI, status codes, or stage-gate checklist
- May cross-link `sa-plan-of-work`

## 6. Plan of work Stage 4 — correct sub-skill

**Prompt:** "What are the KSA-specific gate requirements for RIBA Stage 4 before we issue to tender?"

**Pass if:**

- Routes to `sa-plan-of-work`
- Maps Stage 4 to DD / SBC 601 / SCD NOC pathway
- May reference `sa-pow-stages-0-7.md`

## 7. Site establishment — correct sub-skill

**Prompt:** "Building permit issued yesterday. What must we complete before crane erection, including STC fibre protection on the haul route?"

**Pass if:**

- Routes to `sa-site-establishment`
- Cross-checks permit status; lists hoarding, TMP, telecom protection
- May reference `sa-site-establishment-checklist.md`

## 8. Construction programme — correct sub-skill

**Prompt:** "Contractor proposes 5-day floor cycle with façade 2 floors behind structure. What hold points should the architect insist on for SCD?"

**Pass if:**

- Routes to `sa-construction-programme`
- Lists hold points; cross-links `sa-scd-licensing-compliance` or `sa-fire-life-safety`
- States durations are illustrative

## Dispatcher smoke test

```bash
cd "saudi-architect-master"
echo {"tool":"load_saudi_sub_skill","arguments":{"skill_id":"sa-building-codes"}} | python main.py
```

Expect `status: success` and `references_available` containing `sbc-submission-checklist.md`.
