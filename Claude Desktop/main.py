import os
import json
import sys

# Specialized math logic can still reside in /core
try:
    from core.calculators import run_calculation
except ImportError:
    run_calculation = None


class SaudiArchitectDispatcher:
    def __init__(self):
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.sub_skills_base = os.path.join(self.base_path, "sub_skills")

        # Mapping Skill IDs to their specific folders
        self.valid_skills = [
            "sa-accessibility-design", "sa-acoustic-design", "sa-architect-calculator",
            "sa-building-codes", "sa-building-envelope", "sa-building-programming",
            "sa-building-services", "sa-building-sustainability", "sa-building-typology",
            "sa-concept-design", "sa-construction-documentation", "sa-daylighting-design",
            "sa-design-theory", "sa-fire-life-safety", "sa-material-selection",
            "sa-spatial-planning", "sa-structural-systems", "sa-minor-works",
            "sa-consent-scheduling", "sa-alterations-additions", "sa-lease-compliance",
            "sa-heritage-conservation",
            "sa-site-supervision", "sa-unauthorised-building-works",
            "sa-tender-contract-administration", "sa-fee-proposal-strategy", "sa-mic-dfma",
            "sa-professional-indemnity", "sa-cashflow-debt-recovery", "sa-certificate-of-compliance",
            "sa-project-resource-levelling", "sa-op-submission-strategy", "sa-practical-completion-snagging",
            "sa-scd-licensing-compliance"
        ]

    def load_saudi_sub_skill(self, skill_id):
        """Loads `sub_skills/{skill_id}/{skill_id}.md` and returns its contents."""
        if skill_id not in self.valid_skills:
            return {"error": f"Skill ID '{skill_id}' not recognized."}

        skill_dir = os.path.join(self.sub_skills_base, skill_id)
        canonical_path = os.path.join(skill_dir, f"{skill_id}.md")
        file_path = canonical_path
        ref_path = os.path.join(self.sub_skills_base, skill_id, "references")

        try:
            # Backwards-compat for legacy naming mistakes (e.g. sa-minor-works/sa-minor-work.md)
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

            # List available reference files so Claude knows what else it can ask to see
            available_refs = []
            if os.path.exists(ref_path):
                available_refs = os.listdir(ref_path)

            return {
                "status": "success",
                "skill_id": skill_id,
                "instructions": content,
                "references_available": available_refs
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
        """Runs a calculation from `core.calculators.run_calculation`."""
        if not run_calculation:
            return {"error": "Calculator module not found in /core."}
        return {"status": "success", "result": run_calculation(calc_type, data)}


def main():
    try:
        # Standard input for Claude Desktop Skills
        raw_input = sys.stdin.read()
        if not raw_input:
            return

        input_data = json.loads(raw_input)
        tool_name = input_data.get("tool")
        arguments = input_data.get("arguments", {})

        dispatcher = SaudiArchitectDispatcher()

        # New KSA-branded tool APIs
        if tool_name == "load_saudi_sub_skill":
            result = dispatcher.load_saudi_sub_skill(arguments.get("skill_id"))
        elif tool_name == "run_saudi_calculator":
            result = dispatcher.run_saudi_calculator(
                arguments.get("calc_type"),
                arguments.get("data")
            )
        # Legacy aliases (optional compatibility)
        elif tool_name == "load_sub_skill":
            result = dispatcher.load_saudi_sub_skill(arguments.get("skill_id"))
        elif tool_name == "run_sa_calculator":
            result = dispatcher.run_saudi_calculator(
                arguments.get("calc_type"),
                arguments.get("data")
            )
        else:
            result = {"error": f"Unknown tool: {tool_name}"}

        sys.stdout.write(json.dumps(result))

    except Exception as e:
        sys.stdout.write(json.dumps({"error": f"Dispatcher Error: {str(e)}"}))


if __name__ == "__main__":
    main()