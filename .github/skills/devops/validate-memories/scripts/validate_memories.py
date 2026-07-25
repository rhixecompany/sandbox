#!/usr/bin/env python3
"""validate_memories.py — lightweight memory artifact validator.

Discovers and validates USER.md and MEMORY.md files for the default profile
and non-default profiles, with size and basic schema checks. Outputs a
structured validation report to stdout.

Usage:
    python validate_memories.py
    python validate_memories.py --json
    python validate_memories.py --path "C:\\Users\\Alexa\\AppData\\Local\\hermes"
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import os
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple


DEFAULT_HERMES = Path(os.environ.get("HERMES_HOME", "C:/Users/Alexa/AppData/Local/hermes"))
USER_CHAR_LIMIT = 2_000
MEMORY_CHAR_LIMIT = 6_000


@dataclass(frozen=True)
class FileResult:
    path: str
    exists: bool
    size: int
    ok: bool
    issues: Tuple[str, ...]

    def to_dict(self) -> dict:
        return {
            "path": self.path,
            "exists": self.exists,
            "size": self.size,
            "ok": self.ok,
            "issues": list(self.issues),
        }


def find_profiles(hermes_home: Path) -> List[Tuple[str, Path]]:
    profiles: List[Tuple[str, Path]] = []
    profiles_dir = hermes_home / "profiles"
    if profiles_dir.exists():
        for path in sorted(profiles_dir.iterdir()):
            if path.is_dir():
                profiles.append((path.name, path))
    return profiles


def iter_candidate_paths(hermes_home: Path, profile_name: str, profile_dir: Path) -> Iterable[Path]:
    if profile_name == "default":
        yield hermes_home / "SOUL.md"
        yield hermes_home / "memories" / "MEMORY.md"
        yield hermes_home / "memories" / "USER.md"
    else:
        yield profile_dir / "memories" / "USER.md"
        yield profile_dir / "memories" / "MEMORY.md"
        yield profile_dir / "SOUL.md"


def file_result(path: Optional[Path], expected_exists: bool = True) -> FileResult:
    issues: List[str] = []
    if path is None:
        return FileResult(path="", exists=False, size=0, ok=False, issues=("missing",))
    if not path.exists():
        return FileResult(path=str(path), exists=False, size=0, ok=False, issues=("missing",))
    size = path.stat().st_size
    ok = True
    if size <= 0:
        issues.append("empty")
        ok = False
    return FileResult(path=str(path), exists=True, size=size, ok=ok, issues=tuple(issues))


def _core_frontmatter(text: str) -> bool:
    return bool(re.search(r"^---\s*$", text, re.M))


def _required_sections(text: str, require_model: bool = True) -> Tuple[bool, Tuple[str, ...]]:
    lowered = text.lower()
    checks = {
        "identity": "identity" in lowered,
        "execution preferences": "execution preferences" in lowered,
    }
    if require_model:
        checks["model"] = any(tag in lowered for tag in ("active model", "default model", "model"))
    missing = tuple(name for name, present in checks.items() if not present)
    return (len(missing) == 0, missing)


def validate_user(path: Path, require_model: bool = True) -> Tuple[bool, Tuple[str, ...]]:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception as exc:  # pragma: no cover
        return False, (f"read-error: {exc}",)
    issues: List[str] = []
    if not _core_frontmatter(text):
        issues.append("missing frontmatter marker")
    ok, missing = _required_sections(text, require_model)
    if not ok:
        issues.append(f"missing sections: {', '.join(missing)}")
    if len(text) > USER_CHAR_LIMIT:
        issues.append(f"size {len(text)}>{USER_CHAR_LIMIT}")
    return len(issues) == 0, tuple(issues)


def validate_memory(path: Path) -> Tuple[bool, Tuple[str, ...]]:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception as exc:  # pragma: no cover
        return False, (f"read-error: {exc}",)
    issues: List[str] = []
    if len(text) <= 0:
        issues.append("empty")
    if len(text) > MEMORY_CHAR_LIMIT:
        issues.append(f"size {len(text)}>{MEMORY_CHAR_LIMIT}")
    return len(issues) == 0, tuple(issues)


def validate(hermes_home: Path, *, pretty: bool = True) -> str:
    profiles = find_profiles(hermes_home)
    summary_files = 0
    summary_pass = 0
    summary_fail = 0
    rows: List[dict] = []

    def _record(label: str, result: FileResult) -> None:
        nonlocal summary_files, summary_pass, summary_fail
        summary_files += 1
        if result.ok:
            summary_pass += 1
        else:
            summary_fail += 1
        rows.append({"profile": label, **result.to_dict()})

    for profile_name, profile_dir in [("default", hermes_home), *profiles]:
        for candidate in iter_candidate_paths(hermes_home, profile_name, profile_dir):
            result = file_result(candidate)
            issues = list(result.issues)
            ok = result.ok
            if candidate is None:
                _record(profile_name, result)
                continue
            name = candidate.name.lower()
            if name == "user.md" and result.exists and ok:
                schema_ok, schema_issues = validate_user(candidate, require_model=profile_name == "default")
                if not schema_ok:
                    ok = False
                    issues.extend(schema_issues)
            elif name == "memory.md" and result.exists and ok:
                schema_ok, schema_issues = validate_memory(candidate)
                if not schema_ok:
                    ok = False
                    issues.extend(schema_issues)
            _record(
                profile_name,
                FileResult(
                    path=result.path,
                    exists=result.exists,
                    size=result.size,
                    ok=ok,
                    issues=tuple(issues),
                ),
            )

    payload = {
        "hermes_home": str(hermes_home),
        "files_checked": summary_files,
        "files_passing": summary_pass,
        "files_failing": summary_fail,
        "files": rows,
    }
    if pretty:
        return _pretty_report(payload)
    return json.dumps(payload, indent=2)


def _pretty_report(payload: dict) -> str:
    lines = ["## Memory Validation Report", ""]
    files = payload["files"]
    current_profile = ""
    for row in files:
        if row["profile"] != current_profile:
            current_profile = row["profile"]
            lines.append(f"### Profile: {current_profile}")
        status = "✅" if row["ok"] else "❌"
        size = f"{row['size']}B" if row["exists"] else "N/A"
        issue_text = " — " + ", ".join(row["issues"]) if row["issues"] else ""
        lines.append(f"- {row['path'].split('/')[-1]}: {status} ({size}){issue_text}")
    lines += [
        "",
        "### Summary",
        f"- Profiles checked: {len({r['profile'] for r in files})}",
        f"- Files passing: {payload['files_passing']}",
        f"- Files failing: {payload['files_failing']}",
        f"- Total issues: {sum(len(r['issues']) for r in files)}",
    ]
    return "\n".join(lines)


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate Hermes memory artifacts")
    parser.add_argument(
        "--path",
        default=str(DEFAULT_HERMES),
        help="Hermes home directory (default: %(default)s)",
    )
    parser.add_argument(
        "--json",
        dest="json_output",
        action="store_true",
        help="Emit machine-readable JSON",
    )
    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    args = parse_args(argv)
    report = validate(Path(args.path), pretty=not args.json_output)
    sys.stdout.write(report + "\n")
    return 0 if ("❌" not in report or args.json_output and json.loads(report)["files_failing"] == 0) else 1


if __name__ == "__main__":
    raise SystemExit(main())
