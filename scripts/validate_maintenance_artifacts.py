#!/usr/bin/env python3
"""Validate the maintenance prompt, specification, plan, and approval record.

The validator checks frontmatter, cross-references, required sections, and
secret-safe output. It never reads or prints values from environment files.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

REQUIRED_FRONTMATTER = {"name", "title", "description", "version", "author"}
REQUIRED_HEADINGS = {
    "prompt": ("Mission", "Required phase order", "Resource allocation", "Output contract"),
    "spec": ("Goals", "Functional requirements", "Acceptance criteria", "Verification matrix"),
    "plan": ("Decision", "Milestones and timeline", "Resource allocation", "Completion checklist"),
    "approval": ("Owner decision", "Safety boundaries retained", "Rollback", "Verification required before release"),
}
SECRET_PATTERNS = (
    re.compile(r"(?i)(?:api[_-]?key|secret|token|password)\s*[:=]\s*[^`\s<]+"),
    re.compile(r"(?i)bearer\s+[A-Za-z0-9._~-]{12,}"),
    re.compile(r"(?<![A-Za-z0-9])[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}(?![A-Za-z0-9])"),
)


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """Return lightweight frontmatter and markdown body."""
    if not text.startswith("---\n"):
        raise ValueError("missing opening frontmatter delimiter")
    end = text.find("\n---", 4)
    if end < 0:
        raise ValueError("missing closing frontmatter delimiter")
    raw = text[4:end]
    body = text[end + 5 :].lstrip("\n")
    fields: dict[str, Any] = {}
    current_list: str | None = None
    for line in raw.splitlines():
        if line.startswith("  - ") and current_list:
            fields.setdefault(current_list, []).append(line[4:].strip())
            continue
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if not match:
            continue
        key, value = match.groups()
        if not value:
            fields[key] = []
            current_list = key
            continue
        current_list = None
        if value.startswith("[") and value.endswith("]"):
            fields[key] = [item.strip().strip("'\"") for item in value[1:-1].split(",") if item.strip()]
        else:
            fields[key] = value.strip().strip("'\"")
    return fields, body


def validate_file(path: Path, kind: str, repo: Path) -> list[str]:
    """Validate one artifact and return actionable issues."""
    issues: list[str] = []
    if not path.is_file():
        return [f"{kind}: missing file: {path}"]
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"{kind}: unreadable file: {exc}"]
    try:
        frontmatter, body = parse_frontmatter(text)
    except ValueError as exc:
        return [f"{kind}: {exc}"]
    missing = sorted(REQUIRED_FRONTMATTER - set(frontmatter))
    issues.extend(f"{kind}: missing frontmatter key: {key}" for key in missing)
    for heading in REQUIRED_HEADINGS[kind]:
        if not re.search(rf"^##(?:#)?\s+{re.escape(heading)}\b", body, re.MULTILINE):
            issues.append(f"{kind}: missing heading: {heading}")
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            issues.append(f"{kind}: secret-like value detected; remove value and keep env indirection")
            break
    for link_key in ("prompt", "spec", "plan", "approval"):
        target = frontmatter.get(link_key)
        if isinstance(target, str) and target and not (repo / target).is_file():
            issues.append(f"{kind}: broken {link_key} link: {target}")
    return issues


def main(argv: list[str] | None = None) -> int:
    """Run validation and emit JSON evidence."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=Path(".hermes/reports/maintenance-artifact-validation.json"))
    args = parser.parse_args(argv)
    repo = args.repo.resolve()
    targets = {
        "prompt": repo / ".github/prompts/comprehensive-hermes-maintenance.prompt.md",
        "spec": repo / ".hermes/specs/comprehensive-hermes-maintenance-spec.md",
        "plan": repo / ".hermes/plans/comprehensive-hermes-maintenance-plan.md",
        "approval": repo / ".hermes/approvals/2026-09-05-comprehensive-hermes-maintenance.md",
    }
    issues = [issue for kind, path in targets.items() for issue in validate_file(path, kind, repo)]
    result = {"repo": str(repo), "files": {kind: str(path) for kind, path in targets.items()}, "issues": issues, "passed": not issues}
    output = args.output if args.output.is_absolute() else repo / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="")
    print(json.dumps(result, indent=2))
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
