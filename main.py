#!/usr/bin/env python3
"""Read-only validator and previewer for Git interactive-rebase todo files."""
import argparse
import json
import re
import sys
from pathlib import Path

ALIASES = {
    "p": "pick", "r": "reword", "e": "edit", "s": "squash",
    "f": "fixup", "d": "drop", "x": "exec", "b": "break",
    "l": "label", "t": "reset", "m": "merge",
}
ACTIONS = {"pick", "reword", "edit", "squash", "fixup", "drop",
           "exec", "break", "label", "reset", "merge", "update-ref"}
COMMIT_ACTIONS = {"pick", "reword", "edit", "squash", "fixup", "drop"}
SHA = re.compile(r"^[0-9a-fA-F]{4,40}$")

def parse_todo(text):
    entries = []
    errors = []
    warnings = []
    previous_commit = False
    for line_number, raw in enumerate(text.splitlines(), 1):
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        parts = stripped.split(None, 2)
        action = ALIASES.get(parts[0], parts[0])
        if action not in ACTIONS:
            errors.append(f"line {line_number}: unknown action '{parts[0]}'")
            continue
        argument = parts[1] if len(parts) > 1 else ""
        subject = parts[2] if len(parts) > 2 else ""
        if action in COMMIT_ACTIONS:
            if not SHA.fullmatch(argument):
                errors.append(f"line {line_number}: {action} requires a 4-40 character hexadecimal commit id")
                continue
            if action in {"squash", "fixup"} and not previous_commit:
                warnings.append(f"line {line_number}: {action} has no preceding commit to combine with")
            previous_commit = True
        elif action == "exec" and not argument:
            errors.append(f"line {line_number}: exec requires a command")
        elif action in {"label", "reset", "update-ref", "merge"} and not argument:
            errors.append(f"line {line_number}: {action} requires an argument")
        entries.append({
            "line": line_number,
            "action": action,
            "argument": argument,
            "subject": subject,
        })
    return {
        "entries": entries,
        "commit_actions": sum(item["action"] in COMMIT_ACTIONS for item in entries),
        "errors": errors,
        "warnings": warnings,
        "valid": not errors,
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", help="interactive-rebase todo file")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    args = parser.parse_args()
    report = parse_todo(Path(args.file).read_text(encoding="utf-8"))
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        for item in report["entries"]:
            print(f"{item['line']:>4}  {item['action']:<10} {item['argument']} {item['subject']}".rstrip())
        for warning in report["warnings"]:
            print("WARNING: " + warning, file=sys.stderr)
        for error in report["errors"]:
            print("ERROR: " + error, file=sys.stderr)
        print(f"\n{report['commit_actions']} commit actions; {'valid' if report['valid'] else 'invalid'}")
    raise SystemExit(0 if report["valid"] else 1)

if __name__ == "__main__":
    main()
