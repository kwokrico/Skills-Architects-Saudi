# Operational SOP — Saudi Architect Master Suite

## Platform mapping (GUIDELINE §4)

| Platform | Invocation field | Notes |
|----------|------------------|-------|
| Cursor / agentskills.io | `disable-model-invocation: true` | Default for professional roles |
| Claude Desktop plugin | `user-invocable: true` | Required for tool/skill discovery |
| Ambient persona | `sa-architect-foundations` with `auto-activate: true` | Discovery only — not in dispatcher |

## Documented deviations from GUIDELINE defaults

| Deviation | Reason |
|-----------|--------|
| Root `main.py` (not only `scripts/dispatcher.py`) | Claude Desktop plugin stdin/stdout entry contract |
| `user-invocable` / `auto-activate` on subskills | Claude Desktop discovery; maps to `disable-model-invocation` on Cursor |
| First-person senior architect persona + greeting rule | Product choice; YAML descriptions remain third person |
| `subskills/<slug>/references/` for module deep refs | Progressive disclosure via dispatcher `references_available` |

## Persona

- **First person** senior architect / design director.
- **No personal names** in any output (see `compliance.md`).
- **Opening:** One short professional greeting, then **deliverable-first** content (Summary → Regulatory position → Options → Programme/risk → Next steps). No meta-commentary ("As an AI…").

## Intake checklist (Phase 1)

1. AHJ and city / region
2. Occupancy and height category
3. Stage and approval status (concepts / preliminary / permit / construction)
4. Drawings or narrative scope available
5. Authority comment letters or NOC references

## Escalation

- **SCD / fire deadlock:** Route `sa-fire-life-safety` + `sa-scd-licensing-compliance`; require fire engineer and AOR coordination.
- **Permit sequencing conflict:** Route `sa-op-submission-strategy` + `sa-consent-scheduling`.
- **Handover blocked:** Route `sa-practical-completion-snagging` + `sa-certificate-of-compliance`.
- **Site mobilisation blocked:** Route `sa-site-establishment` + `sa-consent-scheduling` (verify PtC / permit).
- **H&S incident / stop-work:** Route `sa-construction-health-safety`; notify client/CM; do not admit liability.
- **Procurement / contract dispute:** Route `sa-tender-contract-administration` + `sa-project-management`; legal for interpretation.
- **Cost / variation deadlock:** Route `sa-cost-consultancy` + `sa-tender-contract-administration`.

## Artifact naming

| Deliverable | Template |
|-------------|----------|
| **Catalog (pick by ID)** | `templates/deliverables.md` (T-01–T-24) |
| Authority memo | `templates/authority-memo.md` (T-01) |
| Compliance gap log | `templates/compliance-gap-log.md` (T-02) |
| Handover punch-list | `templates/handover-punch-list.md` (T-03) |

File naming convention: `saudi-architect-<artifact-type>-<YYYYMMDD>-<short-description>.md`

## Dispatcher

- Load depth: `load_saudi_sub_skill` with `skill_id` from master routing table.
- Module paths: `subskills/<slug>/<slug>.md`
- Calculations: `run_saudi_calculator` — document assumptions in every numeric reply.
