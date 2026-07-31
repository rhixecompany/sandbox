#!/usr/bin/env python3
"""Phase 1: INVENTORY — scan .github/prompts/, parse frontmatter, produce export + index + report.

Deliverables (written to .copilot/session-state/):
- prompt-management-export.txt   consolidated concatenation of all prompts
- prompts-index.json             machine-readable index (frontmatter per file)
- inventory-report.md            human-readable stats
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]          # .github/prompts/.enhance -> .github/prompts
PROMPTS_DIR = Path(__file__).resolve().parents[1]    # .github/prompts
REPO_ROOT = Path(__file__).resolve().parents[3]      # repo root (SandBox)
OUT_DIR = REPO_ROOT / ".copilot" / "session-state"   # repo-root/.copilot/session-state

FM_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    m = FM_RE.match(text)
    if not m:
        return {}, text
    raw = m.group(1)
    # Minimal YAML-ish parse for the common flat fields used in this library.
    data: dict = {}
    for line in raw.splitlines():
        line = line.rstrip()
        if not line or line.startswith("#") or line.startswith(" ") or line.startswith("\t"):
            continue
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip().strip("'\"")
        if val.startswith("[") or val == "" or val.startswith("-"):
            data[key] = val
            continue
        data[key] = val
    body = text[m.end():]
    return data, body


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    files = sorted(p for p in PROMPTS_DIR.rglob("*") if p.is_file() and p.suffix in {".md", ".prompt", ".txt"})
    # Keep only prompt files: any .md or .prompt.md under prompts dir
    files = [p for p in files if p.suffix == ".md" or p.name.endswith(".prompt.md")]

    index: list[dict] = []
    export_parts: list[str] = []
    stats = {"total": 0, "with_frontmatter": 0, "missing_name": 0, "missing_title": 0,
             "missing_description": 0, "missing_tags": 0, "missing_version": 0, "bytes": 0}
    field_counts: dict[str, int] = {}

    for p in files:
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except Exception as e:  # noqa: BLE001
            index.append({"path": str(p.relative_to(PROMPTS_DIR)), "error": str(e)})
            continue
        fm, body = parse_frontmatter(text)
        rel = str(p.relative_to(PROMPTS_DIR)).replace("\\", "/")
        entry = {"path": rel, "size": len(text.encode("utf-8")), "frontmatter": fm}
        index.append(entry)
        stats["total"] += 1
        stats["bytes"] += len(text.encode("utf-8"))
        if fm:
            stats["with_frontmatter"] += 1
            for f in ("name", "title", "description", "tags", "version"):
                if not fm.get(f):
                    stats[f"missing_{f}"] += 1
                field_counts[f] = field_counts.get(f, 0) + (1 if fm.get(f) else 0)
        export_parts.append(f"\n\n===== FILE: {rel} =====\n\n{text}")

    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    index_path = OUT_DIR / "prompts-index.json"
    export_path = OUT_DIR / "prompt-management-export.txt"
    report_path = OUT_DIR / "inventory-report.md"

    index_path.write_text(json.dumps({"generated": ts, "count": stats["total"], "prompts": index}, indent=2), encoding="utf-8")
    export_path.write_text("".join(export_parts), encoding="utf-8")

    fm_pct = round(100 * stats["with_frontmatter"] / max(stats["total"], 1), 1)
    report = f"""# Prompt Library Inventory Report

> Generated: {ts} | Source: `.github/prompts/`

## Summary

| Metric | Value |
|--------|-------|
| Total prompt files | {stats['total']} |
| With YAML frontmatter | {stats['with_frontmatter']} ({fm_pct}%) |
| Total size | {stats['bytes'] / 1024:.1f} KB |

## Frontmatter Completeness

| Field | Present | Missing |
|-------|---------|---------|
| name | {field_counts.get('name', 0)} | {stats['missing_name']} |
| title | {field_counts.get('title', 0)} | {stats['missing_title']} |
| description | {field_counts.get('description', 0)} | {stats['missing_description']} |
| tags | {field_counts.get('tags', 0)} | {stats['missing_tags']} |
| version | {field_counts.get('version', 0)} | {stats['missing_version']} |

## Files Without Frontmatter

"""
    no_fm = [e["path"] for e in index if not e.get("frontmatter")]
    report += "\n".join(f"- `{p}`" for p in no_fm[:100]) if no_fm else "(none)"
    report += "\n\n## Size Distribution\n\n"
    sizes = [e["size"] for e in index]
    if sizes:
        sizes.sort()
        import statistics
        report += f"- Min: {sizes[0]} bytes\n- Median: {statistics.median(sizes):.0f} bytes\n- Max: {sizes[-1]} bytes\n"
    report_path.write_text(report, encoding="utf-8")

    print(json.dumps({
        "total": stats["total"],
        "with_frontmatter": stats["with_frontmatter"],
        "no_frontmatter": len(no_fm),
        "export_bytes": export_path.stat().st_size,
        "index_bytes": index_path.stat().st_size,
        "report_bytes": report_path.stat().st_size,
        "output_dir": str(OUT_DIR),
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
