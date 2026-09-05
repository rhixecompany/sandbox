#!/usr/bin/env python3
"""Apply and verify a quick-command registry through the Hermes CLI."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


def run(cli: str, args: list[str]) -> subprocess.CompletedProcess[str]:
    """Run Hermes with an argument list and no shell interpolation."""
    return subprocess.run(
        [cli, *args], capture_output=True, text=True, timeout=120
    )


def read_commands(cli: str) -> dict[str, Any]:
    """Read the active profile's quick-command map."""
    result = run(cli, ["config", "get", "quick_commands", "--json"])
    if result.returncode:
        return {}
    value = json.loads(result.stdout)
    if not isinstance(value, dict):
        raise ValueError("Hermes quick_commands is not a mapping")
    return value


def compact_yaml(registry: dict[str, Any]) -> str:
    """Serialize the registry compactly using a YAML mapping merge alias."""
    parts: list[str] = []
    anchor_written = False
    for key, value in registry.items():
        encoded_key = json.dumps(key)
        if isinstance(value, dict) and value.get("type") == "exec":
            command = json.dumps(value.get("command", ""))
            if not anchor_written:
                parts.append(f"{encoded_key}: &exec {{type: exec, command: {command}}}")
                anchor_written = True
            else:
                parts.append(f"{encoded_key}: {{<<: *exec, command: {command}}}")
        else:
            encoded_value = json.dumps(value, separators=(",", ":"))
            parts.append(f"{encoded_key}: {encoded_value}")
    return "{" + ",".join(parts) + "}"


def apply_profile(cli: str, profile: str, desired: dict[str, Any]) -> dict[str, Any]:
    """Apply one complete mapping through the CLI and verify readback."""
    switched = run(cli, ["profile", "use", profile])
    if switched.returncode:
        return {"profile": profile, "passed": False, "error": switched.stderr.strip()}
    current = read_commands(cli)
    payload = compact_yaml(desired)
    result = run(cli, ["config", "set", "--force", "quick_commands", payload])
    if result.returncode:
        return {
            "profile": profile,
            "passed": False,
            "error": f"unable to set quick_commands: {result.stderr.strip()}",
        }
    actual = read_commands(cli)
    passed = actual == desired
    return {
        "profile": profile,
        "passed": passed,
        "before": len(current),
        "payload_bytes": len(payload.encode("utf-8")),
        "after": len(actual),
        "expected": len(desired),
        "error": "structural readback mismatch" if not passed else "",
    }


def main(argv: list[str] | None = None) -> int:
    """Apply the registry to each requested profile and verify readback."""
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--registry", type=Path, required=True)
    ap.add_argument("--profiles", nargs="+", required=True)
    ap.add_argument("--cli", default=os.environ.get("HERMES_CLI") or shutil.which("hermes") or "hermes")
    args = ap.parse_args(argv)
    desired = json.loads(args.registry.read_text(encoding="utf-8"))
    if not isinstance(desired, dict):
        raise ValueError("Registry must be a JSON object")
    results = [apply_profile(args.cli, profile, desired) for profile in args.profiles]
    print(json.dumps({"profiles": results, "all_passed": all(item["passed"] for item in results)}, indent=2))
    return 0 if all(item["passed"] for item in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
