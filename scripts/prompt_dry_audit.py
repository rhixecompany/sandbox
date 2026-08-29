#!/usr/bin/env python3
"""Prompt library DRY compliance audit.

For every .github/prompts/*.prompt.md file, check:
  - Required frontmatter fields: name, title, description, version, author, license
  - Optional but recommended: trigger, toolsets, skills, dependencies, tags
  - Structure: has Goal/Context/Rules/Phases/Verification sections
  - References: any prompts/templates/_shared/ references resolve to existing files
  - Broken fences: any unclosed code blocks
  - Missing required sections: Goal, Verification

Writes a JSON + markdown report.

Usage:
  python scripts/prompt_dry_audit.py [--prompts-dir .github/prompts] [--out DIR]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REQUIRED_FM = ["name", "title", "description", "version", "author", "license"]
RECOMMENDED_FM = ["trigger", "toolsets", "skills", "dependencies", "tags", "metadata"]
REQUIRED_SECTIONS = ["## Goal", "## Verification"]  # at minimum


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Extract YAML-like frontmatter (key: value or list)."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text
    fm_text = text[3:end].strip()
    body = text[end + 4:].lstrip("\n")
    fm: dict = {}
    current_list_key: str | None = None
    for raw in fm_text.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.startswith("  - ") or raw.startswith("- "):
            if current_list_key:
                item = raw.lstrip().lstrip("-").strip()
                # strip leading inline key if present
                if ":" in item and not item.startswith('"'):
                    fm.setdefault(f"_list_{current_list_key}", []).append(item)
                else:
                    fm.setdefault(f"_list_{current_list_key}", []).append(item)
            continue
        if ":" in raw:
            key, _, val = raw.partition(":")
            key = key.strip()
            val = val.strip()
            if val == "":
                # could be dict or list start
                current_list_key = key
                fm[key] = ""
            else:
                current_list_key = None
                # strip surrounding quotes
                if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                    val = val[1:-1]
                fm[key] = val
    return fm, body


def check_fences(text: str) -> int:
    """Return 1 if there are unclosed code fences, 0 if balanced.

    Uses a state machine: tracks fence open/close. A ``` (or longer) opens; the
    next ``` (or longer) closes. Nested fences (4+) are handled by counting
    consecutive backticks; same or longer closes, shorter doesn't.
    """
    in_fence = False
    fence_len = 0
    for line in text.splitlines():
        m = re.match(r"^(`{3,})(.*)$", line)
        if not m:
            continue
        ticks = len(m.group(1))
        rest = m.group(2)
        if not in_fence:
            in_fence = True
            fence_len = ticks
            # If line ends with closing ticks of same length, it's self-closing
            line_stripped = line.rstrip()
            if line_stripped.endswith("`" * ticks) and line_stripped.count("`") > ticks:
                # Check if the line has both open + close (unusual)
                # Actually treat as just an open fence; subsequent ``` will close
                pass
        else:
            if ticks >= fence_len:
                in_fence = False
                fence_len = 0
    return 1 if in_fence else 0


def check_sections(text: str) -> list[str]:
    """Return list of REQUIRED_SECTIONS that are missing."""
    return [s for s in REQUIRED_SECTIONS if s not in text]


def check_shared_refs(text: str, shared_dir: Path) -> list[str]:
    """Find any references to _shared/ files and verify they exist."""
    missing: list[str] = []
    # Look for "See templates/_shared/X.md" or "prompts/templates/_shared/X"
    for m in re.findall(r"templates/_shared/([\w\-\.]+\.md)", text):
        if not (shared_dir / m).exists():
            missing.append(f"templates/_shared/{m}")
    return missing


def audit(prompts_dir: Path) -> dict:
    prompts = sorted(prompts_dir.glob("*.prompt.md"))
    shared_dir = prompts_dir / "templates" / "_shared"
    results: list[dict] = []
    fm_missing_counts: dict[str, int] = {k: 0 for k in REQUIRED_FM + RECOMMENDED_FM}
    section_missing_counts: dict[str, int] = {s: 0 for s in REQUIRED_SECTIONS}
    broken_fences: list[str] = []
    missing_shared_refs: list[str] = []

    for p in prompts:
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except OSError as e:
            results.append({"file": p.name, "error": str(e)})
            continue
        fm, body = parse_frontmatter(text)
        for k in REQUIRED_FM + RECOMMENDED_FM:
            if k not in fm:
                fm_missing_counts[k] += 1
        missing_secs = check_sections(body)
        for s in missing_secs:
            section_missing_counts[s] += 1
        fence_err = check_fences(text)
        if fence_err:
            broken_fences.append(p.name)
        missing_refs = check_shared_refs(text, shared_dir)
        missing_shared_refs.extend(missing_refs)
        results.append({
            "file": p.name,
            "frontmatter_keys": sorted(fm.keys()),
            "missing_required_fm": [k for k in REQUIRED_FM if k not in fm],
            "missing_recommended_fm": [k for k in RECOMMENDED_FM if k not in fm],
            "missing_required_sections": missing_secs,
            "broken_fences": fence_err,
            "missing_shared_refs": missing_refs,
        })

    return {
        "ts": datetime.now(timezone.utc).isoformat(),
        "total": len(prompts),
        "fm_missing_counts": fm_missing_counts,
        "section_missing_counts": section_missing_counts,
        "broken_fences": broken_fences,
        "missing_shared_refs": missing_shared_refs,
        "per_file": results,
    }


def render_markdown(report: dict, prompts_dir: Path) -> str:
    lines = ["# Prompt DRY Audit Report\n",
             f"Generated: {report['ts']}",
             f"Prompts dir: {prompts_dir}",
             f"Total prompts: {report['total']}\n",
             "## Frontmatter Coverage (missing count out of total)"]
    for k, v in report["fm_missing_counts"].items():
        if v > 0:
            lines.append(f"- `{k}`: {v} prompts missing")
    lines.append("\n## Required Sections (missing count)")
    for k, v in report["section_missing_counts"].items():
        if v > 0:
            lines.append(f"- `{k}`: {v} prompts missing")
    lines.append(f"\n## Broken code fences: {len(report['broken_fences'])}")
    if report["broken_fences"]:
        for f in report["broken_fences"][:20]:
            lines.append(f"- {f}")
    lines.append(f"\n## Missing shared template references: {len(report['missing_shared_refs'])}")
    for r in report["missing_shared_refs"][:20]:
        lines.append(f"- {r}")
    lines.append("\n## Per-file (top 20 most-incomplete)")
    ranked = sorted(
        [r for r in report["per_file"] if "error" not in r],
        key=lambda r: -(len(r["missing_required_fm"]) + len(r["missing_recommended_fm"]) + len(r["missing_required_sections"]) + r["broken_fences"]),
    )
    lines.append("| File | Missing required FM | Missing recommended FM | Missing sections | Broken fences |")
    lines.append("|---|---|---|---|---|")
    for r in ranked[:20]:
        lines.append(f"| {r['file']} | {len(r['missing_required_fm'])} | {len(r['missing_recommended_fm'])} | {len(r['missing_required_sections'])} | {r['broken_fences']} |")
    return "\n".join(lines)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--prompts-dir", default=".github/prompts")
    p.add_argument("--out", default=None)
    args = p.parse_args()
    prompts_dir = Path(args.prompts_dir)
    if not prompts_dir.exists():
        print(f"Not found: {prompts_dir}", file=sys.stderr)
        return 2
    out_dir = Path(args.out) if args.out else (
        Path(".hermes/plans") / f"prompt-dry-audit-{datetime.now(timezone.utc).strftime('%Y-%m-%d')}"
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    report = audit(prompts_dir)
    (out_dir / "report.json").write_text(json.dumps(report, indent=2))
    (out_dir / "report.md").write_text(render_markdown(report, prompts_dir))
    print(f"Total: {report['total']} prompts")
    print(f"Broken fences: {len(report['broken_fences'])}")
    print(f"Missing required FM (any field): {sum(1 for r in report['per_file'] if r.get('missing_required_fm'))}")
    print(f"Report: {out_dir}/report.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
