#!/usr/bin/env python3
"""Webhook filter/transform script for todoist-hermes-label.
Reads JSON payload from stdin (route payload). If payload label does not contain
"hermes", produces [SILENT] and exits 0 (ignored). Else transforms payload:
sets body from payload content and prints JSON stdout.
Verified against docs §2 (script): .py -> current Python interpreter; stdin=JSON;
JSON stdout=payload replacement; [SILENT]=ignore; nonzero exit=ignore.
"""
import json, sys

payload = json.load(sys.stdin)
labels = payload.get("payload", {}).get("labels", [])
if "hermes" not in labels:
    print("[SILENT]")
    raise SystemExit(0)

# Transform: set body to payload content; keep original payload intact
payload["body"] = payload.get("payload", {}).get("content", "")
print(json.dumps(payload))
