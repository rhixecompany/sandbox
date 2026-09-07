#!/usr/bin/env python3
"""Specs Judge — score .hermes/specs/*.md on 5 dimensions (max 100).

Usage:
    python judge.py --specs-dir .hermes/specs [--plans-dir .hermes/plans] [--output PATH] [--threshold N]
"""
import argparse
import json
import re
import sys
from pathlib import Path
from datetime import datetime

REQUIRED_SECTIONS = [
    "## Goal",
    "## Requirements",
    "## Acceptance Criteria",
    "## Non-Functional Requirements",
    "## Verification",
]
RECOMMENDED_SECTIONS = ["## Linked Plan", "## Linked Specs"]
FM_FIELDS = ["name", "title", "status", "owner", "version"]
MAX_LINE = 250


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    fm_block = text[4:end]
    fm = {}
    for line in fm_block.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm


def extract_spec_references(text: str) -> list[str]:
    """Extract all spec file references from text (both ## Linked Plan and inline)."""
    refs = []
    # Check for ## Linked Specs section
    if "## Linked Specs" in text:
        spec_section = text.split("## Linked Specs", 1)[1].split("## ", 1)[0]
        for line in spec_section.splitlines():
            line = line.strip()
            if line.startswith("- ") or line.startswith("* "):
                # Extract path
                match = re.search(r'[.\w/-]+\.md', line)
                if match:
                    refs.append(match.group(0))
    # Check for ## Linked Plan (legacy)
    if "## Linked Plan" in text:
        plan_section = text.split("## Linked Plan", 1)[1].split("## ", 1)[0]
        for line in plan_section.splitlines():
            line = line.strip()
            if line.startswith("- ") or line.startswith("* "):
                match = re.search(r'[.\w/-]+\.md', line)
                if match:
                    refs.append(match.group(0))
    # Inline references
    inline_refs = re.findall(r'(\.hermes/specs/[.\w/-]+\.md|\.\./specs/[.\w/-]+\.md)', text)
    refs.extend(inline_refs)
    return list(set(refs))


def extract_plan_references(text: str) -> list[str]:
    """Extract all plan file references from text."""
    refs = []
    if "## Linked Plan" in text:
        plan_section = text.split("## Linked Plan", 1)[1].split("## ", 1)[0]
        for line in plan_section.splitlines():
            line = line.strip()
            if line.startswith("- ") or line.startswith("* "):
                match = re.search(r'[.\w/-]+\.md', line)
                if match:
                    refs.append(match.group(0))
    inline_refs = re.findall(r'(\.hermes/plans/[.\w/-]+\.md|\.\./plans/[.\w/-]+\.md)', text)
    refs.extend(inline_refs)
    return list(set(refs))


def verify_refs_exist(refs: list[str], base_dir: Path) -> tuple[int, int]:
    """Verify referenced files exist. Returns (valid_count, total_count)."""
    if not refs:
        return 0, 0
    valid = 0
    for ref in refs:
        # Normalize path
        ref_path = Path(ref)
        if ref_path.is_absolute():
            if ref_path.exists():
                valid += 1
        else:
            # Try relative to base_dir
            if (base_dir / ref_path).exists():
                valid += 1
            # Try relative to CWD
            elif Path(ref).exists():
                valid += 1
    return valid, len(refs)


def score_one(path: Path, plans_dir: Path | None = None) -> dict:
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    fm = parse_frontmatter(text)

    # Frontmatter (20 pts)
    fm_pts = sum(4 for f in FM_FIELDS if f in fm)
    fm_pts = min(fm_pts, 20)

    # Structure (20 pts): required sections
    sec_pts = sum(4 for s in REQUIRED_SECTIONS if s in text)
    rec_pts = sum(2 for s in RECOMMENDED_SECTIONS if s in text)
    struct_pts = min(sec_pts + rec_pts, 20)

    # Content (20 pts): requirements have measurable criteria
    # Bug fix: previous split on "## " matched any H2, including a
    # `## Functional Requirements` subsection that immediately followed
    # `## Requirements`, leaving the section text empty. Use a regex
    # that matches only the next level-2 heading (## Foo) and not
    # level-3+ (### Bar, #### Baz).
    content_pts = 0
    if "## Requirements" in text:
        m = re.split(r"(?m)^## (?!#)", text.split("## Requirements", 1)[1], maxsplit=1)
        req_section = m[0] if m else ""
        measurable = sum(1 for line in req_section.splitlines()
                         if any(c.isdigit() for c in line) or "When" in line or "Then" in line)
        content_pts = min(measurable * 2, 20)

    # Spec-Plan Coupling (20 pts): bidirectional linkage
    coupling_pts = 0
    spec_refs = extract_spec_references(text)
    plan_refs = extract_plan_references(text)

    # Spec must reference at least one plan
    plan_valid, plan_total = verify_refs_exist(plan_refs, path.parent) if plans_dir else (0, 0)
    if plan_total > 0 and plan_valid == plan_total:
        coupling_pts += 10
    elif plan_total > 0:
        coupling_pts += 5

    # Check if any plans reference this spec (reverse linkage)
    if plans_dir and plans_dir.is_dir():
        reverse_refs = 0
        for plan_file in plans_dir.glob("*.md"):
            plan_text = plan_file.read_text(encoding="utf-8", errors="ignore")
            plan_spec_refs = extract_spec_references(plan_text)
            # Check if this spec is referenced
            spec_name = path.name
            for ref in plan_spec_refs:
                if spec_name in ref or path.stem in ref:
                    reverse_refs += 1
                    break
        if reverse_refs > 0:
            coupling_pts += 10
        elif plan_refs:  # Spec references plans but no plans reference back
            coupling_pts += 5

    coupling_pts = min(coupling_pts, 20)

    # Cross-refs (10 pts): legacy, kept for backwards compat but reduced weight
    xref_pts = 0
    if "## Linked Plan" in text:
        xref_pts = 10
    elif "../plans/" in text or ".hermes/plans/" in text:
        xref_pts = 5

    # DRY (20 pts): under MAX_LINE lines
    n_lines = len(lines)
    if n_lines <= MAX_LINE:
        dry_pts = 20
    elif n_lines <= MAX_LINE * 1.5:
        dry_pts = 12
    else:
        dry_pts = 5

    total = fm_pts + struct_pts + content_pts + coupling_pts + xref_pts + dry_pts
    return {
        "file": str(path),
        "score": total,
        "rating": "PASS" if total >= 70 else "WARN" if total >= 50 else "FAIL",
        "dims": {
            "frontmatter": fm_pts,
            "structure": struct_pts,
            "content": content_pts,
            "spec_plan_coupling": coupling_pts,
            "cross_refs": xref_pts,
            "dry": dry_pts,
        },
        "lines": n_lines,
        "fm_fields": sorted(fm.keys()),
        "sections_found": [s for s in REQUIRED_SECTIONS + RECOMMENDED_SECTIONS if s in text],
        "spec_refs": spec_refs,
        "plan_refs": plan_refs,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Specs Judge")
    ap.add_argument("--specs-dir", default=".hermes/specs", help="dir containing specs")
    ap.add_argument("--plans-dir", default=".hermes/plans", help="dir containing plans (for cross-validation)")
    ap.add_argument("--output", default="judge_results/specs_audit")
    ap.add_argument("--threshold", type=int, default=70)
    args = ap.parse_args()

    spec_dir = Path(args.specs_dir)
    if not spec_dir.is_dir():
        print(f"ERR: specs dir not found: {spec_dir}", file=sys.stderr)
        return 1

    plans_dir = Path(args.plans_dir) if args.plans_dir else None

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    md_path = out.with_suffix(".md")
    json_path = out.with_suffix(".json")

    results = []
    for spec in sorted(spec_dir.glob("*.md")):
        results.append(score_one(spec, plans_dir))

    if not results:
        print(f"WARN: no specs found in {spec_dir}", file=sys.stderr)
        results = []

    avg = sum(r["score"] for r in results) / max(len(results), 1)
    passed = sum(1 for r in results if r["score"] >= args.threshold)

    # JSON
    json_path.write_text(json.dumps({
        "ts": datetime.utcnow().isoformat() + "Z",
        "dir": str(spec_dir),
        "plans_dir": str(plans_dir) if plans_dir else None,
        "threshold": args.threshold,
        "count": len(results),
        "avg": round(avg, 1),
        "passed": passed,
        "results": results,
    }, indent=2))

    # MD
    lines = [
        f"# Specs Audit — {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        f"Dir: `{spec_dir}` | Plans Dir: `{plans_dir}` | Threshold: {args.threshold}",
        f"Count: {len(results)} | Avg: {avg:.1f} | Passed: {passed}",
        "",
        "| File | Score | Rating | FM | Struct | Content | Coupling | XRef | DRY | Lines |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for r in results:
        d = r["dims"]
        lines.append(
            f"| `{Path(r['file']).name}` | {r['score']} | {r['rating']} | "
            f"{d['frontmatter']} | {d['structure']} | {d['content']} | "
            f"{d['spec_plan_coupling']} | {d['cross_refs']} | {d['dry']} | {r['lines']} |"
        )
    md_path.write_text("\n".join(lines) + "\n")

    print(f"Specs Judge: {len(results)} files, avg {avg:.1f}, passed {passed}/{len(results)}")
    print(f"Report: {md_path}")
    print(f"JSON:   {json_path}")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())