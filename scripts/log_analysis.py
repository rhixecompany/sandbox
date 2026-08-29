#!/usr/bin/env python3
"""Hermes log analysis.

Reads log files from ~/AppData/Local/hermes/logs/ and clusters errors by:
  - category (MCP / hook / provider / auth / ollama / etc.)
  - frequency
  - first/last seen

Outputs:
  - report.json (machine-readable, per-file stats)
  - report.md (human-readable summary)

Usage:
  python scripts/log_analysis.py [--logs-dir ~/AppData/Local/hermes/logs] [--out DIR]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

HERMES_HOME = Path.home() / "AppData" / "Local" / "hermes"
LOGS_DIR = HERMES_HOME / "logs"

# Category patterns (regex -> category name)
CATEGORIES: list[tuple[str, str]] = [
    (r"\b(?:mcp|MCP)_[A-Z_]+", "mcp"),
    (r"\bhook\b", "hook"),
    (r"\bhermes_(?:auth|provider)\b", "auth"),
    (r"\b(?:ollama|openai|deepseek|gemini|xai|grok|openrouter|opencode-zen)\b", "provider"),
    (r"\b(?:config\.yaml|\.env|api_key)\b", "config"),
    (r"\b(?:subagent|delegate_task)\b", "subagent"),
    (r"\b(?:tool_call|toolset)\b", "tool"),
    (r"\b(?:chat|stream|llm_call)\b", "chat"),
    (r"\b(?:session|state\.db)\b", "session"),
    (r"\b(?:plugin|hub)\b", "plugin"),
    (r"\b(?:rate.?limit|429|quota|throttl)", "rate_limit"),
    (r"\b(?:network|DNS|Connection|timeout)", "network"),
]


def categorize(text: str) -> str:
    """Return the first matching category for a log line."""
    for pat, name in CATEGORIES:
        if re.search(pat, text, re.IGNORECASE):
            return name
    return "other"


def analyze_file(path: Path) -> dict[str, object]:
    """Return per-file stats."""
    if not path.exists() or path.stat().st_size == 0:
        return {"path": str(path), "size": path.stat().st_size if path.exists() else 0, "lines": 0, "errors": 0, "by_category": {}}
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    errors = 0
    warnings = 0
    by_category: Counter = Counter()
    by_level: Counter = Counter()
    sample_errors: list[str] = []
    for line in lines:
        lvl_match = re.search(r"\b(ERROR|WARNING|INFO|DEBUG|CRITICAL|TRACE)\b", line, re.I)
        if lvl_match:
            by_level[lvl_match.group(1).upper()] += 1
            if lvl_match.group(1).upper() in ("ERROR", "CRITICAL"):
                errors += 1
                if len(sample_errors) < 10:
                    sample_errors.append(line[:300])
        else:
            by_level["NONE"] += 1
        # Categorize
        cat = categorize(line)
        by_category[cat] += 1
    return {
        "path": str(path),
        "name": path.name,
        "size": path.stat().st_size,
        "lines": len(lines),
        "errors": errors,
        "warnings": warnings,
        "by_level": dict(by_level),
        "by_category": dict(by_category.most_common()),
        "sample_errors": sample_errors,
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--logs-dir", default=str(LOGS_DIR))
    p.add_argument("--out", default=None)
    args = p.parse_args()
    logs_dir = Path(args.logs_dir)
    if not logs_dir.exists():
        print(f"Not found: {logs_dir}", file=sys.stderr)
        return 2
    out_dir = Path(args.out) if args.out else (
        Path(".hermes/plans") / f"log-analysis-{datetime.now(timezone.utc).strftime('%Y-%m-%d_%H%M%S')}"
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    files = sorted([p for p in logs_dir.iterdir() if p.is_file()])
    per_file = [analyze_file(p) for p in files]
    # Aggregate by category
    agg: Counter = Counter()
    agg_level: Counter = Counter()
    total_errors = 0
    total_lines = 0
    for f in per_file:
        for k, v in f.get("by_category", {}).items():
            agg[k] += v
        for k, v in f.get("by_level", {}).items():
            agg_level[k] += v
        total_errors += f.get("errors", 0)
        total_lines += f.get("lines", 0)

    report = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "logs_dir": str(logs_dir),
        "file_count": len(files),
        "total_lines": total_lines,
        "total_errors": total_errors,
        "by_category": dict(agg.most_common()),
        "by_level": dict(agg_level.most_common()),
        "per_file": per_file,
    }
    (out_dir / "report.json").write_text(json.dumps(report, indent=2))

    md = [f"# Hermes Log Analysis Report\n",
          f"Generated: {report['ts']}",
          f"Logs dir: {logs_dir}",
          f"Files: {report['file_count']} | Lines: {report['total_lines']} | Errors: {report['total_errors']}\n",
          "## By Category (top 10)",
          ""]
    for cat, count in list(report["by_category"].items())[:10]:
        md.append(f"- `{cat}`: {count}")
    md.append("\n## By Level")
    for lvl, count in report["by_level"].items():
        md.append(f"- `{lvl}`: {count}")
    md.append("\n## Per-file")
    md.append("| File | Lines | Errors | Top category |")
    md.append("|---|---|---|---|")
    for f in sorted(per_file, key=lambda x: -x.get("errors", 0)):
        top_cat = next(iter(f.get("by_category", {})), "—")
        md.append(f"| {f.get('name', '?')} | {f.get('lines', 0)} | {f.get('errors', 0)} | {top_cat} |")
    md.append("\n## Sample errors (top 10 per file with errors)")
    for f in per_file:
        if f.get("sample_errors"):
            md.append(f"### {f['name']}")
            for s in f["sample_errors"][:5]:
                md.append(f"- `{s[:200]}`")
    (out_dir / "report.md").write_text("\n".join(md))
    print(f"Files: {report['file_count']} | Lines: {total_lines} | Errors: {total_errors}")
    print(f"Top category: {next(iter(report['by_category']), '—')}")
    print(f"Report: {out_dir}/report.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
