import json
import os
import sys

# Ensure skill root is on path for scripts package imports
_SKILL_ROOT = os.path.dirname(os.path.abspath(__file__))
if _SKILL_ROOT not in sys.path:
    sys.path.insert(0, _SKILL_ROOT)

from scripts.dispatcher import handle_tool_request


def main():
    try:
        raw_input = sys.stdin.read()
        if not raw_input:
            return

        input_data = json.loads(raw_input)
        tool_name = input_data.get("tool")
        arguments = input_data.get("arguments", {})

        result = handle_tool_request(tool_name, arguments)
        sys.stdout.write(json.dumps(result))

    except Exception as e:
        sys.stdout.write(json.dumps({"error": f"Dispatcher Error: {str(e)}"}))


if __name__ == "__main__":
    main()
