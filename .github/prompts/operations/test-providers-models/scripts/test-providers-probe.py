#!/usr/bin/env python3
"""Probe all Hermes auth providers and write structured output to .hermes/reports/.
Uses verified live state (hermes auth list / config show / status / doctor / doctor --fix / insights / fallback list / model).
Run: python scripts/test-providers-probe.py
"""
import subprocess, json
from pathlib import Path

REPORT_DIR = Path(".hermes/reports")
REPORT_DIR.mkdir(parents=True, exist_ok=True)

COMMANDS = [
    ("hermes auth list", "auth_list"),
    ("hermes config show", "config_show"),
    ("hermes status", "status"),
    ("hermes doctor", "doctor"),
    ("hermes doctor --fix", "doctor_fix"),
    ("hermes insights", "insights"),
    ("hermes fallback list", "fallback"),
    ("hermes model", "model"),
]

results = {}
for cmd, label in COMMANDS:
    try:
        out = subprocess.run(cmd.split(), capture_output=True, text=True, timeout=60)
        results[label] = {"exit": out.returncode, "stdout": out.stdout[-8000:], "stderr": out.stderr[-2000:]}
    except Exception as e:
        results[label] = {"exit": -1, "error": str(e)}

# Write JSON + text summary
json_path = REPORT_DIR / "test-providers-probe.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

text_path = REPORT_DIR / "test-providers-probe.md"
with open(text_path, "w", encoding="utf-8") as f:
    f.write("# Probe results — test-providers-models\n\n")
    for label, info in results.items():
        f.write(f"## {label}\nexit={info.get('exit')}\n```\n{info.get('stdout', info.get('error',''))}\n```\n")

print(f"Wrote {json_path} ({len(results)} probes) and {text_path}")
