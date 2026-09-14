#!/usr/bin/env python3
"""Verify the five-day consolidation package on disk."""
from __future__ import annotations

import json
import re
import argparse
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[5]
CORPUS = ROOT / "plans" / "run-all-goals-five-day-session-corpus.json"
SUMMARY = ROOT / "plans" / "run-all-goals-five-day-session-summary.json"
SPEC = ROOT / "specs" / "run-all-goals-five-day-consolidated-spec.md"
PLAN = ROOT / "plans" / "run-all-goals-five-day-consolidated-plan.md"
PROMPT = ROOT / ".github" / "prompts" / "general" / "run-all-goals" / "run-all-goals-five-day.prompt.md"
SKILL = ROOT / ".github" / "prompts" / "general" / "run-all-goals" / "skills" / "run-all-goals-five-day.md"
AUDIT_SCRIPT = ROOT / "scripts" / "audit_default_sessions_window.py"
SUMMARY_SCRIPT = ROOT / "scripts" / "summarize_run_all_goals_corpus.py"
INVENTORY = ROOT / ".github" / "prompts" / "general" / "run-all-goals" / "results" / "five-day-artifact-inventory.md"
RESULT = ROOT / ".github" / "prompts" / "general" / "run-all-goals" / "results" / "five-day-execution-result.md"


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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--require-result",
        action="store_true",
        help="require the final execution result artifact in addition to structural outputs",
    )
    args = parser.parse_args()
    errors: list[str] = []
    for path in (CORPUS, SUMMARY):
        errors.extend(check_json(path))
    for path in (SPEC, PLAN, PROMPT):
        errors.extend(check_frontmatter(path))
        if path.is_file() and path.stat().st_size < 500:
            errors.append(f"too small: {path}")
    for path in (SKILL, AUDIT_SCRIPT, SUMMARY_SCRIPT, INVENTORY):
        if not path.is_file():
            errors.append(f"missing required package output: {path}")
    if args.require_result and not RESULT.is_file():
        errors.append(f"missing final result: {RESULT}")
    if args.require_result and RESULT.is_file():
        result_content = RESULT.read_text(encoding="utf-8")
        for section in ("## Fresh evidence", "## Corpus summary", "## Session-end capture", "## Blockers / caveats"):
            if section not in result_content:
                errors.append(f"final result missing section: {section}")
        if CORPUS.is_file():
            corpus_count = json.loads(CORPUS.read_text(encoding="utf-8")).get("session_count", 0)
            if f"{corpus_count} sessions" not in result_content:
                errors.append(f"final result missing fresh corpus count: {corpus_count}")
        if SUMMARY.is_file():
            excerpt_count = json.loads(SUMMARY.read_text(encoding="utf-8")).get("evidence_excerpt_count", 0)
            if f"{excerpt_count} evidence excerpts" not in result_content:
                errors.append(f"final result missing fresh evidence count: {excerpt_count}")
    if PROMPT.is_file():
        prompt = PROMPT.read_text(encoding="utf-8")
        for reference in (
            "./specs/run-all-goals-five-day-consolidated-spec.md",
            "./plans/run-all-goals-five-day-consolidated-plan.md",
            "./scripts/audit_default_sessions_window.py",
            "./scripts/summarize_run_all_goals_corpus.py",
            "./.github/prompts/general/run-all-goals/scripts/verify_run_all_goals_five_day.py",
            "./.github/prompts/general/run-all-goals/skills/run-all-goals-five-day.md",
            "./.github/prompts/general/run-all-goals/results/five-day-artifact-inventory.md",
        ):
            if reference not in prompt:
                errors.append(f"prompt missing reference: {reference}")
            elif not (ROOT / reference.removeprefix("./")).is_file():
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
        profiles = {str(session.get("profile_name")) for session in data.get("sessions", []) if session.get("profile_name")}
        if profiles != {"default"}:
            errors.append(f"corpus profile scope mismatch: {sorted(profiles)}")
    if SUMMARY.is_file():
        summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
        if summary.get("session_count", 0) <= 0:
            errors.append("summary has no sessions")
        if summary.get("window", {}).get("start_wat") != "2026-09-06" or summary.get("window", {}).get("end_wat_exclusive") != "2026-09-11":
            errors.append("summary window mismatch")
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
