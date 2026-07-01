"""Inject 'When to Use This Skill' tables into sub-skill markdown files."""
from __future__ import annotations

import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
SUB = BASE / "subskills"

# skill_id -> list of (question, use_instead) — "—" means this skill is primary
ROUTING: dict[str, list[tuple[str, str]]] = {
    "sa-accessibility-design": [
        ("Inclusive circulation, ramps, lifts, SBC 1001", "—", "sa-building-codes"),
        ("General SBC occupancy matrix only", "sa-building-codes", "—"),
        ("Fire egress / SCD NOC", "sa-fire-life-safety", "—"),
    ],
    "sa-acoustic-design": [
        ("Building acoustics, noise criteria, vibration", "—", "sa-building-services"),
        ("MEP plant noise / shaft sizing", "sa-building-services", "—"),
        ("Environmental EIA statutory sign-off", "—", "halt — licensed consultant"),
    ],
    "sa-alterations-additions": [
        ("Extensions, structural additions, major retrofit", "—", "sa-minor-works"),
        ("Cosmetic fit-out only", "sa-minor-works", "—"),
        ("Fire strategy overhaul", "sa-fire-life-safety", "—"),
    ],
    "sa-architect-calculator": [
        ("Egress proxy, GFA, U-value, delta-T, layout sort", "—", "—"),
        ("Code compliance sign-off", "sa-building-codes", "—"),
        ("Stamped fire engineering", "sa-fire-life-safety", "—"),
    ],
    "sa-architect-foundations": [
        ("Persona, discovery, KSA defaults only", "—", "saudi-architect-master (SKILL.md)"),
        ("Deep technical sub-domain", "—", "load sub-skill via master router"),
    ],
    "sa-building-codes": [
        ("SBC matrix, occupancy, SBPS code basis", "—", "sa-fire-life-safety"),
        ("SCD licensing closeout only", "sa-scd-licensing-compliance", "—"),
        ("Permit packaging / OP pathway", "sa-op-submission-strategy", "—"),
    ],
    "sa-building-envelope": [
        ("Façade, thermal movement, dust ingress, waterproofing", "—", "sa-building-sustainability"),
        ("Mostadam credits / energy modelling", "sa-building-sustainability", "—"),
        ("Structural frame selection", "sa-structural-systems", "—"),
    ],
    "sa-building-programming": [
        ("SOA, unit mix, functional adjacency", "—", "sa-building-typology"),
        ("Massing / concept narrative", "sa-concept-design", "—"),
    ],
    "sa-building-services": [
        ("MEP/ICT/fire spatial coordination", "—", "sa-fire-life-safety"),
        ("Fire strategy / SCD NOC narrative", "sa-fire-life-safety", "—"),
        ("Energy / Mostadam", "sa-building-sustainability", "—"),
    ],
    "sa-building-sustainability": [
        ("SBC 601, Mostadam, envelope energy", "—", "sa-building-envelope"),
        ("Detailed façade jointing", "sa-building-envelope", "—"),
    ],
    "sa-building-typology": [
        ("Asset class strategy (hospitality, residential, mixed-use)", "—", "sa-concept-design"),
        ("Code occupancy classification detail", "sa-building-codes", "—"),
    ],
    "sa-cashflow-debt-recovery": [
        ("Receivables, milestone billing, debt recovery", "—", "sa-fee-proposal-strategy"),
        ("Fee bid / scope strategy", "sa-fee-proposal-strategy", "—"),
    ],
    "sa-certificate-of-compliance": [
        ("BCC / closeout compliance package", "—", "sa-practical-completion-snagging"),
        ("Snagging / TOC process", "sa-practical-completion-snagging", "—"),
        ("SCD safety license", "sa-scd-licensing-compliance", "—"),
    ],
    "sa-concept-design": [
        ("Early massing, design narrative, compliance shaping", "—", "sa-building-codes"),
        ("Detailed tender documentation", "sa-construction-documentation", "—"),
    ],
    "sa-construction-documentation": [
        ("Tender/IFC architectural packages", "—", "sa-building-codes"),
        ("Early concept only", "sa-concept-design", "—"),
    ],
    "sa-consent-scheduling": [
        ("Approval programme, milestone sequencing", "—", "sa-op-submission-strategy"),
        ("Submission content / OP strategy", "sa-op-submission-strategy", "—"),
    ],
    "sa-daylighting-design": [
        ("Daylight, glare, SBC 601 daylight aspects", "—", "sa-building-sustainability"),
        ("Full energy model", "sa-building-sustainability", "—"),
    ],
    "sa-design-theory": [
        ("Precedent, positioning, conceptual language", "—", "sa-concept-design"),
        ("Code compliance path", "sa-building-codes", "—"),
    ],
    "sa-fee-proposal-strategy": [
        ("Scope, fee bid, additional services", "—", "sa-tender-contract-administration"),
        ("Post-contract claims", "sa-tender-contract-administration", "—"),
    ],
    "sa-fire-life-safety": [
        ("SBC 501, egress, smoke, compartmentation", "—", "sa-scd-licensing-compliance"),
        ("SCD inspection / safety license only", "sa-scd-licensing-compliance", "—"),
        ("General code matrix", "sa-building-codes", "—"),
    ],
    "sa-heritage-conservation": [
        ("Heritage, adaptive reuse, RCU/Diriyah guidelines", "—", "sa-spatial-planning"),
        ("Standard greenfield codes only", "sa-building-codes", "—"),
    ],
    "sa-lease-compliance": [
        ("Plot, Krooki, easements, land-use", "—", "sa-spatial-planning"),
        ("Zoning masterplan controls", "sa-spatial-planning", "—"),
    ],
    "sa-material-selection": [
        ("Materials, SASO, desert/coastal durability", "—", "sa-building-envelope"),
        ("U-value / energy compliance", "sa-building-sustainability", "—"),
    ],
    "sa-mic-dfma": [
        ("Modular, precast, DfMA logistics", "—", "sa-structural-systems"),
        ("Traditional in-situ structure only", "sa-structural-systems", "—"),
    ],
    "sa-minor-works": [
        ("Fit-out, minor renovation, ChOO", "—", "sa-alterations-additions"),
        ("Major extension / structural add", "sa-alterations-additions", "—"),
    ],
    "sa-op-submission-strategy": [
        ("SBPS packaging, OP / partial OP pathway", "—", "sa-consent-scheduling"),
        ("Programme milestones only", "sa-consent-scheduling", "—"),
    ],
    "sa-practical-completion-snagging": [
        ("TOC, snagging, DLP closeout", "—", "sa-certificate-of-compliance"),
        ("Authority BCC / Is’har package", "sa-certificate-of-compliance", "—"),
    ],
    "sa-professional-indemnity": [
        ("PI exposure, liability clauses (advisory)", "—", "sa-tender-contract-administration"),
        ("Contract claims administration", "sa-tender-contract-administration", "—"),
    ],
    "sa-project-resource-levelling": [
        ("Resource levelling, burn rate, capacity", "—", "sa-fee-proposal-strategy"),
    ],
    "sa-scd-licensing-compliance": [
        ("SCD NOC, safety license, inspection closeout", "—", "sa-fire-life-safety"),
        ("Fire strategy design (pre-NOC)", "sa-fire-life-safety", "—"),
    ],
    "sa-site-supervision": [
        ("Site supervision, NCR/RFI, construction compliance", "—", "sa-practical-completion-snagging"),
        ("Handover / snagging", "sa-practical-completion-snagging", "—"),
    ],
    "sa-spatial-planning": [
        ("Zoning, plot, masterplan controls", "—", "sa-lease-compliance"),
        ("Land / Krooki / easements", "sa-lease-compliance", "—"),
    ],
    "sa-structural-systems": [
        ("Structural system, transfers, spans", "—", "sa-building-codes"),
        ("Modular / DfMA delivery", "sa-mic-dfma", "—"),
    ],
    "sa-tender-contract-administration": [
        ("Tender, FIDIC, variations, claims, post-award CA", "—", "sa-fee-proposal-strategy"),
        ("Procurement route, D&B vs DBB vs EPC", "sa-procurement-strategy", "—"),
        ("Cost plan, BoQ, valuations", "sa-cost-consultancy", "—"),
        ("Fee proposal only", "sa-fee-proposal-strategy", "—"),
    ],
    "sa-unauthorised-building-works": [
        ("Unauthorized works, rectification, enforcement risk", "—", "sa-building-codes"),
        ("Routine permitted minor works", "sa-minor-works", "—"),
    ],
    "sa-plan-of-work": [
        ("RIBA stage, plan of work, stage gate", "—", "sa-deliverables-workstages"),
        ("Issue pack / RACI only", "sa-deliverables-workstages", "—"),
        ("Approval programme", "sa-consent-scheduling", "—"),
    ],
    "sa-deliverables-workstages": [
        ("Issue pack, transmittal, RACI, stage freeze", "—", "sa-plan-of-work"),
        ("RIBA stage checklist", "sa-plan-of-work", "—"),
        ("Named templates T-01–T-24", "—", "references/templates/deliverables.md"),
    ],
    "sa-project-management": [
        ("Delivery plan, risk, disputes, client reporting", "—", "sa-plan-of-work"),
        ("Construction look-ahead", "sa-construction-programme", "—"),
        ("Post-award FIDIC CA", "sa-tender-contract-administration", "—"),
    ],
    "sa-procurement-strategy": [
        ("Procurement route, contract form, risk allocation", "—", "sa-tender-contract-administration"),
        ("Variations / EOT assessment", "sa-tender-contract-administration", "—"),
        ("Cost plan", "sa-cost-consultancy", "—"),
    ],
    "sa-cost-consultancy": [
        ("Cost plan, BoQ, valuation, final account", "—", "sa-tender-contract-administration"),
        ("FIDIC certificate / CA duties", "sa-tender-contract-administration", "—"),
        ("Procurement route", "sa-procurement-strategy", "—"),
    ],
    "sa-site-establishment": [
        ("Hoarding, mobilisation, TMP, telecom, utilities", "—", "sa-consent-scheduling"),
        ("Permit sequencing only", "sa-consent-scheduling", "—"),
        ("Site H&S strategy", "sa-construction-health-safety", "—"),
    ],
    "sa-construction-programme": [
        ("Sequencing, look-ahead, hold points", "—", "sa-project-management"),
        ("Site supervision / NCR", "sa-site-supervision", "—"),
        ("Mobilisation / TMP", "sa-site-establishment", "—"),
    ],
    "sa-construction-health-safety": [
        ("Site safety, RAMS, accident, HSE audit", "—", "—"),
        ("Fire strategy / SBC 501 design", "sa-fire-life-safety", "—"),
        ("Site supervision quality", "sa-site-supervision", "—"),
    ],
}

HALT_BLOCK = """
## Halt conditions

- Stop and request data if **AHJ**, occupancy, or approval status is unknown (see `../../references/compliance.md`).
- Do not assert regulatory compliance without verified code edition and authority pathway.
"""


def build_table(skill_id: str, rows: list[tuple[str, str, str]]) -> str:
    lines = [
        "## When to Use This Skill",
        "",
        "| Question type | This skill | Use instead |",
        "|---------------|------------|-------------|",
    ]
    for q, this_skill, instead in rows:
        this_col = f"`{skill_id}`" if this_skill == "—" else f"`{this_skill}`"
        inst_col = "—" if instead == "—" else f"`{instead}`"
        lines.append(f"| {q} | {this_col} | {inst_col} |")
    lines.append("")
    lines.extend(HALT_BLOCK.strip().split("\n"))
    return "\n".join(lines) + "\n\n"


def inject(content: str, skill_id: str, table: str) -> str:
    if "## When to Use This Skill" in content:
        content = re.sub(
            r"\n## When to Use This Skill[\s\S]*?(?=\n## [^W]|\n# |\Z)",
            "\n" + table.rstrip() + "\n\n",
            content,
            count=1,
        )
        # Remove any duplicate halt blocks left after table replacement
        halt_pattern = (
            r"(## Halt conditions\n\n"
            r"- Stop and request data[^\n]+\n"
            r"- Do not assert[^\n]+\n)"
        )
        halts = list(re.finditer(halt_pattern, content))
        if len(halts) > 1:
            first_end = halts[0].end()
            rest = content[first_end:]
            rest = re.sub(halt_pattern, "", rest)
            content = content[:first_end] + rest
        return content
    m = re.match(r"(---\n[\s\S]*?---\n)(\n*)([\s\S]*)", content)
    if not m:
        return content
    front, _, body = m.group(1), m.group(2), m.group(3)
    return front + "\n" + table + body.lstrip()


def main() -> None:
    for skill_id, rows in ROUTING.items():
        path = SUB / skill_id / f"{skill_id}.md"
        if not path.exists():
            print(f"skip missing {path}")
            continue
        table = build_table(skill_id, rows)
        text = path.read_text(encoding="utf-8")
        path.write_text(inject(text, skill_id, table), encoding="utf-8")
        print(f"updated {skill_id}")


if __name__ == "__main__":
    main()
