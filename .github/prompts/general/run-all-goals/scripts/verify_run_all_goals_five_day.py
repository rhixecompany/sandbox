#!/usr/bin/env python3
"""Verify the five-day consolidation package on disk."""
from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[5]
CORPUS = ROOT / ".hermes" / "plans" / "run-all-goals-five-day-session-corpus.json"
SUMMARY = ROOT / ".hermes" / "plans" / "run-all-goals-five-day-session-summary.json"
SPEC = ROOT / ".hermes" / "specs" / "run-all-goals-five-day-consolidated-spec.md"
PLAN = ROOT / ".hermes" / "plans" / "run-all-goals-five-day-consolidated-plan.md"
PROMPT = ROOT / ".github" / "prompts" / "general" / "run-all-goals" / "run-all-goals-five-day.prompt.md"


def check_json(path: Path) -> list[str]:
    if not path.is_file():
        return [f"missing: {path}"]
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return [f"invalid JSON {path}: {exc}"]
    return []


def check_frontmatter(path: Path) -> list[str]:
    if not path.is_file():
        return [f"missing: {path}"]
    content = path.read_text(encoding="utf-8")
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", content, re.DOTALL)
    if not match:
        return [f"missing frontmatter: {path}"]
    try:
        metadata = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as exc:
        return [f"invalid YAML frontmatter {path}: {exc}"]
    if not isinstance(metadata, dict):
        return [f"frontmatter is not a mapping: {path}"]
    required = {"name", "title", "description", "version", "author", "license", "tags"}
    return [f"frontmatter missing {field}: {path}" for field in sorted(required - set(metadata))]


def main() -> int:
    errors: list[str] = []
    for path in (CORPUS, SUMMARY):
        errors.extend(check_json(path))
    for path in (SPEC, PLAN, PROMPT):
        errors.extend(check_frontmatter(path))
        if path.is_file() and path.stat().st_size < 500:
            errors.append(f"too small: {path}")
    if PROMPT.is_file():
        prompt = PROMPT.read_text(encoding="utf-8")
        for reference in (".hermes/specs/run-all-goals-five-day-consolidated-spec.md", ".hermes/plans/run-all-goals-five-day-consolidated-plan.md"):
            if reference not in prompt:
                errors.append(f"prompt missing reference: {reference}")
            elif not (ROOT / reference).is_file():
                errors.append(f"prompt reference missing on disk: {reference}")
    if CORPUS.is_file():
        data = json.loads(CORPUS.read_text(encoding="utf-8"))
        window = data.get("window", {})
        if window.get("start_wat") != "2026-09-06" or window.get("end_wat_exclusive") != "2026-09-11":
            errors.append("corpus window mismatch")
        home = str(data.get("hermes_home", "")).replace("/", "\\").lower()
        if not home.endswith("appdata\\local\\hermes"):
            errors.append("corpus Hermes home mismatch")
        databases = data.get("databases", [])
        if len(databases) != 1 or not str(databases[0].get("path", "")).lower().endswith("state.db"):
            errors.append("corpus is not limited to default state.db")
        if data.get("session_count", 0) <= 0:
            errors.append("corpus has no sessions")
    if SUMMARY.is_file():
        summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
        if summary.get("session_count", 0) <= 0:
            errors.append("summary has no sessions")
    for path in (SPEC, PLAN, PROMPT):
        if path.is_file():
            content = path.read_text(encoding="utf-8")
            if any(marker in content for marker in ("[SKILL_PRUNED]", "FIXME:", "TODO:")):
                errors.append(f"placeholder marker in {path}")
    if PLAN.is_file() and SPEC.is_file():
        plan_content = PLAN.read_text(encoding="utf-8")
        spec_content = SPEC.read_text(encoding="utf-8")
        if "run-all-goals-five-day-consolidated-spec.md" not in plan_content:
            errors.append("plan does not link to spec")
        if "run-all-goals-five-day-consolidated-plan.md" not in spec_content:
            errors.append("spec does not link to plan")
    print("=== Five-Day Consolidation Verification ===")
    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS")
    for path in (CORPUS, SUMMARY, SPEC, PLAN, PROMPT):
        print(f"- {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
