# Saudi Architect Skills

### A professional skill suite for architectural practice in the Kingdom of Saudi Arabia

`Skills-Architect-Saudi` is a localized architecture plugin built for Saudi delivery realities. It centers on one master router skill and domain subskills aligned with KSA codes, authority pathways, and project conditions across municipalities and giga-project ecosystems.

The suite is tuned for:
- **SBC-based compliance strategy** across core code families (including life safety, accessibility, and energy-related checks)
- **Saudi Civil Defence (SCD) integration** for NOC-sensitive scopes
- **Baladiya/SBPS and authority-facing workflows** for permits, fit-out, and occupancy transitions
- **Mostadam-aware design coordination** for sustainability and envelope performance
- **Desert and high-load design contexts** (dust, cooling demand, resilience)

---

- `SKILL.md`: Main entry skill (master router) with routing logic and quick-reference behavior.
- `references/`: Governance (`compliance.md`, `operational.md`, `config.json`, `domain_terms.json`, `templates/`).
- `subskills/<id>/<id>.md`: Specialized KSA subskills for compliance, technical coordination, delivery, and practice workflows.
- `scripts/calculators.py`: Calculation helpers used by calculator workflows.
- `main.py`: Runtime entry point for loading subskills and tool dispatch.
- `evals/evals.json`: Formal eval test cases; `saudi-architect-master-workspace/` for run outputs.
- `VERIFICATION.md`: Golden test prompts; `AGENTS.md` at repo root for Cursor activation.

- [Quick Start](#quick-start)
- [What You Get](#what-you-get)
- [How It Works](#how-it-works)
- [Router-Declared Subskills](#router-declared-subskills)
- [Calculators](#calculators)
- [Folder Structure](#folder-structure)
- [Example Prompts](#example-prompts)
- [Saudi Regulatory and Delivery Context](#saudi-regulatory-and-delivery-context)
- [Credits](#credits)

---

## Quick Start

### Option 1: Use directly in Claude Desktop

1. Copy or clone this folder into your Claude Desktop skills workspace.
2. Keep the package structure unchanged:
   - `SKILL.md`
   - `references/`
   - `subskills/`
   - `scripts/`
   - `main.py`
3. Load the skill package from the `saudi-architect-master` directory.
4. Start a new chat and ask a Saudi architecture question.

### Option 2: Plugin directory launch

```bash
claude --plugin-dir "/path/to/Skills-Architect-Saudi/saudi-architect-master"
```

---

## What You Get

- **1 master router skill** in `SKILL.md` for intake and specialist routing
- **Saudi-focused routing tree** covering code, authority, design, delivery, and practice operations
- **Built-in quick-reference behavior** for practical first-pass guidance before deep dive routing
- **Calculation support** via `scripts/calculators.py`
- **Structured dispatch flow** through `load_saudi_sub_skill` and `run_saudi_calculator`

---

## How It Works

The system follows a progressive routing flow:

1. **Quick answer first**  
   The master skill handles straightforward queries with concise KSA-oriented guidance where possible.

2. **Route to a specialist when needed**  
   For deeper or risk-sensitive topics, it dispatches to the best-matching subskill using `load_saudi_sub_skill`.

3. **Run computations for numeric checks**  
   For quantitative tasks, it calls calculator workflows through `run_saudi_calculator`.

This keeps routine architectural support fast while preserving depth for high-risk regulatory and technical coordination work.

---

## Router-Declared Subskills

The master router in `saudi-architect-master/SKILL.md` currently declares the following subskills:

- `sa-building-codes`
- `sa-fire-life-safety`
- `sa-op-submission-strategy`
- `sa-building-sustainability`
- `sa-building-envelope`
- `sa-building-services`
- `sa-spatial-planning`
- `sa-accessibility-design`
- `sa-building-typology`
- `sa-structural-systems`
- `sa-building-programming`
- `sa-concept-design`
- `sa-construction-documentation`
- `sa-acoustic-design`
- `sa-daylighting-design`
- `sa-material-selection`
- `sa-architect-calculator`
- `sa-design-theory`
- `sa-minor-works`
- `sa-consent-scheduling`
- `sa-alterations-additions`
- `sa-site-supervision`
- `sa-tender-contract-administration`
- `sa-fee-proposal-strategy`
- `sa-cashflow-debt-recovery`
- `sa-project-resource-levelling`
- `sa-certificate-of-compliance`
- `sa-scd-licensing-compliance`
- `sa-practical-completion-snagging`
- `sa-professional-indemnity`
- `sa-mic-dfma`
- `sa-unauthorised-building-works`
- `sa-lease-compliance`
- `sa-heritage-conservation`

Note: this section reflects the router declaration in `SKILL.md` (source of truth for routing).

---

## Calculators

The calculator module currently supports:

- **Egress check** (`egress_1004_7`): travel-distance style compliance logic from room geometry
- **GFA aggregation** (`gfa_aggregator`): accountable vs exempt GFA roll-up logic
- **U-value calculator** (`u_value_from_layers`): layered envelope thermal transmittance check
- **Temperature delta check** (`delta_t_check`): simple delta-T verification helper
- **Layout sorting utility** (`layout_sort`): OCR/layout ordering helper by X/Y coordinates

---

## Folder Structure

```text
saudi-architect-master/
├── SKILL.md                            # Master router entry
├── main.py                             # Claude Desktop stdin/stdout entry
├── references/
│   ├── config.json                     # Strict mode and governance flags
│   ├── compliance.md
│   ├── operational.md
│   ├── domain_terms.json
│   └── templates/                      # Memo, gap log, punch-list, catalog
├── subskills/<id>/
│   ├── <id>.md
│   └── references/                     # Deep refs (selected modules)
├── scripts/
│   ├── dispatcher.py
│   ├── calculators.py
│   └── inject_when_to_use.py
├── evals/
│   ├── evals.json
│   └── files/
└── VERIFICATION.md

saudi-architect-master-workspace/       # Sibling — eval run outputs
└── iteration-1/
```

---

## Example Prompts

- "Review this high-rise concept for SBC and SCD life-safety coordination risks."
- "For a Riyadh office fit-out, what triggers full Change of Occupancy instead of minor renovation approval?"
- "Check likely conflicts between façade intent and ventilation intake/exhaust requirements for a desert site."
- "Draft a Saudi-ready submission checklist for Baladiya plus SCD review."
- "Assess this MEP plant zoning strategy against spatial efficiency and maintainability targets."
- "Create an action plan to close compliance gaps before authority submission."
- "Use the calculator to aggregate GFA and show accountable vs exempt areas."

---

## Saudi Regulatory and Delivery Context

This suite is intended for KSA architectural workflows and frequently references:

- **Saudi Building Code (SBC)** families relevant to building, fire/life safety, accessibility, and energy performance
- **Saudi Civil Defence (SCD)** requirements where NOC, fire systems, and life safety approvals are in scope
- **Municipality/Baladiya and SBPS submission processes** for permits and renovation routes
- **Mostadam sustainability pathways** and project performance expectations
- **Authority-specific overlays** for major development entities (for example, giga-project governance frameworks)

Always verify the latest authority circulars, municipality interpretation, and project-specific conditions, since local jurisdiction and asset-owner requirements can override baseline assumptions.

---

## Credits

This project is a Saudi localization and expansion of the original [Skills-Architects](https://github.com/Amanbh997/Skills-Architects) framework by Abhinav Bhardwaj, adapted for KSA regulations, authority workflows, and delivery practice.
