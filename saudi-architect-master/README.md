# Saudi Architect Master Suite

Tier 2 professional skill package for KSA architectural practice (GUIDELINE canonical layout).

## Contents

| Path | Purpose |
|------|---------|
| `SKILL.md` | Master router, workflow, routing table |
| `references/config.json` | Strict mode and governance flags |
| `references/compliance.md` | Compliance halts and advisory boundaries |
| `references/operational.md` | SOP, platform mapping, artifact naming |
| `references/domain_terms.json` | KSA acronyms |
| `references/templates/` | Deliverables catalog (T-01–T-24), stage gate, tender route, OP matrix, look-ahead |
| `subskills/` | 43 domain modules (`<id>/<id>.md`) |
| `scripts/dispatcher.py` | `load_saudi_sub_skill`, `run_saudi_calculator` logic |
| `scripts/calculators.py` | Proxy calculators (not AHJ sign-off) |
| `main.py` | Claude Desktop stdin/stdout entry point |
| `evals/evals.json` | Eval test cases |
| `VERIFICATION.md` | Golden test prompts |

## Quick start

```bash
claude --plugin-dir "/path/to/Skills-Architect-Saudi/saudi-architect-master"
```

Keep `SKILL.md`, `subskills/`, `references/`, `scripts/`, and `main.py` together.

## Routing

- **42 modules** are routable via `load_saudi_sub_skill`.
- **`sa-architect-foundations`** is auto-activate persona/discovery only (not in dispatcher).

See repo root [`README.md`](../README.md) for the full sub-skill index and example prompts.

## Eval workspace

Eval run outputs live in sibling [`saudi-architect-master-workspace/`](../saudi-architect-master-workspace/) (not inside this skill folder).
