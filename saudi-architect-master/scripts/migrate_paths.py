"""One-time migration: update paths after GUIDELINE restructure."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUB = ROOT / "subskills"


def dedupe_halts(text: str) -> str:
    pattern = (
        r"(## Halt conditions\n\n"
        r"- Stop and request data[^\n]+\n"
        r"- Do not assert[^\n]+\n)"
    )
    matches = list(re.finditer(pattern, text))
    if len(matches) <= 1:
        return text
    first_end = matches[0].end()
    rest = text[first_end:]
    rest = re.sub(pattern, "", rest)
    return text[:first_end] + rest


def add_disable_model_invocation(text: str) -> str:
    if "disable-model-invocation" in text:
        return text
    m = re.match(r"(---\n)([\s\S]*?)(---\n)", text)
    if not m:
        return text
    body = m.group(2).rstrip() + "\ndisable-model-invocation: true\n"
    return m.group(1) + body + m.group(3) + text[m.end() :]


def update_root_md(path: Path) -> None:
    t = path.read_text(encoding="utf-8")
    t = t.replace("rules/compliance.md", "references/compliance.md")
    t = t.replace("rules/operational.md", "references/operational.md")
    t = t.replace("vocabulary/domain_terms.json", "references/domain_terms.json")
    t = t.replace("](config.json)", "](references/config.json)")
    t = t.replace("`config.json`", "`references/config.json`")
    t = t.replace("templates/", "references/templates/")
    t = t.replace("sub_skills", "subskills")
    t = t.replace("Claude Desktop", "saudi-architect-master")
    t = t.replace("core/calculators.py", "scripts/calculators.py")
    t = t.replace("/core", "/scripts")
    if path.name == "SKILL.md":
        t = add_disable_model_invocation(t)
    path.write_text(t, encoding="utf-8")
    print(f"updated {path}")


def update_subskill(path: Path) -> None:
    t = path.read_text(encoding="utf-8")
    t = t.replace("rules/compliance.md", "../../references/compliance.md")
    t = t.replace("sub_skills", "subskills")
    t = dedupe_halts(t)
    t = add_disable_model_invocation(t)
    path.write_text(t, encoding="utf-8")
    print(f"updated {path.name}")


def update_references_md(path: Path) -> None:
    t = path.read_text(encoding="utf-8")
    t = t.replace("../rules/compliance.md", "../compliance.md")
    t = t.replace("../vocabulary/domain_terms.json", "../domain_terms.json")
    t = t.replace("rules/compliance.md", "compliance.md")
    t = t.replace("sub_skills", "subskills")
    t = t.replace("Claude Desktop", "saudi-architect-master")
    path.write_text(t, encoding="utf-8")
    print(f"updated {path}")


def main() -> None:
    for name in ("SKILL.md", "VERIFICATION.md", "README.md"):
        p = ROOT / name
        if p.exists():
            update_root_md(p)

    for path in sorted(SUB.glob("*/*.md")):
        update_subskill(path)

    for path in sorted(ROOT.glob("references/**/*.md")):
        update_references_md(path)

    print("done")


if __name__ == "__main__":
    main()
