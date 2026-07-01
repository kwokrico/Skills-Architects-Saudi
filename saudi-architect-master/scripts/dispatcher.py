import os

try:
    from scripts.calculators import run_calculation
except ImportError:
    try:
        from calculators import run_calculation
    except ImportError:
        run_calculation = None


class SaudiArchitectDispatcher:
    def __init__(self):
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.subskills_base = os.path.join(self.base_path, "subskills")

        self.valid_skills = [
            "sa-accessibility-design",
            "sa-acoustic-design",
            "sa-architect-calculator",
            "sa-building-codes",
            "sa-building-envelope",
            "sa-building-programming",
            "sa-building-services",
            "sa-building-sustainability",
            "sa-building-typology",
            "sa-concept-design",
            "sa-construction-documentation",
            "sa-daylighting-design",
            "sa-design-theory",
            "sa-fire-life-safety",
            "sa-material-selection",
            "sa-spatial-planning",
            "sa-structural-systems",
            "sa-minor-works",
            "sa-consent-scheduling",
            "sa-alterations-additions",
            "sa-lease-compliance",
            "sa-heritage-conservation",
            "sa-site-supervision",
            "sa-unauthorised-building-works",
            "sa-tender-contract-administration",
            "sa-fee-proposal-strategy",
            "sa-mic-dfma",
            "sa-professional-indemnity",
            "sa-cashflow-debt-recovery",
            "sa-certificate-of-compliance",
            "sa-project-resource-levelling",
            "sa-op-submission-strategy",
            "sa-practical-completion-snagging",
            "sa-scd-licensing-compliance",
            "sa-plan-of-work",
            "sa-deliverables-workstages",
            "sa-project-management",
            "sa-procurement-strategy",
            "sa-cost-consultancy",
            "sa-site-establishment",
            "sa-construction-programme",
            "sa-construction-health-safety",
        ]

    def load_saudi_sub_skill(self, skill_id):
        """Loads `subskills/{skill_id}/{skill_id}.md` and returns its contents."""
        if skill_id not in self.valid_skills:
            return {"error": f"Skill ID '{skill_id}' not recognized."}

        skill_dir = os.path.join(self.subskills_base, skill_id)
        canonical_path = os.path.join(skill_dir, f"{skill_id}.md")
        file_path = canonical_path
        ref_path = os.path.join(self.subskills_base, skill_id, "references")

        try:
            if not os.path.exists(file_path) and os.path.isdir(skill_dir):
                md_candidates = [
                    os.path.join(skill_dir, f)
                    for f in os.listdir(skill_dir)
                    if f.lower().endswith(".md")
                ]
                if md_candidates:
                    file_path = sorted(md_candidates)[0]

            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            available_refs = []
            if os.path.exists(ref_path):
                available_refs = os.listdir(ref_path)

            return {
                "status": "success",
                "skill_id": skill_id,
                "instructions": content,
                "references_available": available_refs,
            }
        except FileNotFoundError:
            return {
                "error": "Sub-skill markdown file not found.",
                "skill_id": skill_id,
                "expected_path": canonical_path,
            }
        except Exception as e:
            return {"error": str(e)}

    def run_saudi_calculator(self, calc_type, data=None):
        """Runs a calculation from `scripts.calculators.run_calculation`."""
        if not run_calculation:
            return {"error": "Calculator module not found in scripts/."}
        return {"status": "success", "result": run_calculation(calc_type, data)}


def handle_tool_request(tool_name, arguments):
    """Dispatch a tool request and return the result dict."""
    dispatcher = SaudiArchitectDispatcher()

    if tool_name == "load_saudi_sub_skill":
        return dispatcher.load_saudi_sub_skill(arguments.get("skill_id"))
    if tool_name == "run_saudi_calculator":
        return dispatcher.run_saudi_calculator(
            arguments.get("calc_type"),
            arguments.get("data"),
        )
    if tool_name == "load_sub_skill":
        return dispatcher.load_saudi_sub_skill(arguments.get("skill_id"))
    if tool_name == "run_sa_calculator":
        return dispatcher.run_saudi_calculator(
            arguments.get("calc_type"),
            arguments.get("data"),
        )
    return {"error": f"Unknown tool: {tool_name}"}
