#!/usr/bin/env python3
"""Plans Judge — score .hermes/plans/*.md on 6 dimensions (max 100).

Usage:
    python judge.py --plans-dir .hermes/plans [--specs-dir .hermes/specs] [--output PATH] [--threshold N]
"""
import argparse
import json
import re
import sys
from pathlib import Path
from datetime import datetime

FM_FIELDS = ["title", "description", "date", "author", "status", "profile", "model"]
REQUIRED_SECTIONS = ["## Goal", "## Verification"]
PHASE_PATTERN = re.compile(r"^## Phase [A-Z0-9]+", re.MULTILINE)
GATE_PATTERN = re.compile(r"\*\*Gate\*\*", re.MULTILINE)
MAX_LINE = 300


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    fm = {}
    for line in text[4:end].splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm


def extract_spec_references(text: str) -> list[str]:
    """Extract all spec file references from text."""
    refs = []
    # Check for ## Linked Specs section (plural for multi-spec)
    if "## Linked Specs" in text:
        spec_section = text.split("## Linked Specs", 1)[1].split("## ", 1)[0]
        for line in spec_section.splitlines():
            line = line.strip()
            if line.startswith("- ") or line.startswith("* "):
                match = re.search(r'[.\w/-]+\.md', line)
                if match:
                    refs.append(match.group(0))
    # Check for ## Linked Spec (singular, legacy)
    if "## Linked Spec" in text:
        spec_section = text.split("## Linked Spec", 1)[1].split("## ", 1)[0]
        for line in spec_section.splitlines():
            line = line.strip()
            if line.startswith("- ") or line.startswith("* "):
                match = re.search(r'[.\w/-]+\.md', line)
                if match:
                    refs.append(match.group(0))
    # Inline references
    inline_refs = re.findall(r'(\.hermes/specs/[.\w/-]+\.md|\.\./specs/[.\w/-]+\.md)', text)
    refs.extend(inline_refs)
    return list(set(refs))


def verify_refs_exist(refs: list[str], base_dir: Path) -> tuple[int, int]:
    """Verify referenced files exist. Returns (valid_count, total_count)."""
    if not refs:
        return 0, 0
    valid = 0
    for ref in refs:
        ref_path = Path(ref)
        if ref_path.is_absolute():
            if ref_path.exists():
                valid += 1
        else:
            if (base_dir / ref_path).exists():
                valid += 1
            elif Path(ref).exists():
                valid += 1
    return valid, len(refs)


def score_one(path: Path, specs_dir: Path | None = None) -> dict:
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    fm = parse_frontmatter(text)

    # Frontmatter (20)
    fm_pts = sum(round(20 / len(FM_FIELDS), 2) for f in FM_FIELDS if f in fm)
    fm_pts = min(round(fm_pts), 20)

    # Structure (20): ≥3 phases, each with gate
    phase_count = len(PHASE_PATTERN.findall(text))
    gate_count = len(GATE_PATTERN.findall(text))
    if phase_count >= 3 and gate_count >= phase_count:
        struct_pts = 20
    elif phase_count >= 3:
        struct_pts = 14
    elif phase_count >= 1:
        struct_pts = 8
    else:
        struct_pts = 0

    # Content (20): risks + files section + tasks
    content_pts = 0
    if "## Risks" in text:
        content_pts += 7
    if "## Files to Create" in text or "## Files to Modify" in text:
        content_pts += 7
    if re.search(r"## Phase [A-Z0-9]+.*?##", text, re.DOTALL):
        content_pts += 6

    # Spec Coupling (20 pts) — NEW: plan must reference ≥1 spec
    coupling_pts = 0
    spec_refs = extract_spec_references(text)
    spec_valid, spec_total = verify_refs_exist(spec_refs, path.parent) if specs_dir else (0, 0)

    if spec_total > 0 and spec_valid == spec_total:
        coupling_pts = 20
    elif spec_total > 0 and spec_valid > 0:
        coupling_pts = 15
    elif spec_total > 0:
        coupling_pts = 5
    else:
        coupling_pts = 0  # HARD GATE: no spec references = 0

    # Check reverse linkage: do specs reference this plan?
    if specs_dir and specs_dir.is_dir():
        reverse_refs = 0
        for spec_file in specs_dir.glob("*.md"):
            spec_text = spec_file.read_text(encoding="utf-8", errors="ignore")
            spec_plan_refs = []
            # Check for spec's plan references
            if "## Linked Plan" in spec_text:
                plan_section = spec_text.split("## Linked Plan", 1)[1].split("## ", 1)[0]
                for line in plan_section.splitlines():
                    line = line.strip()
                    if line.startswith("- ") or line.startswith("* "):
                        match = re.search(r'[.\w/-]+\.md', line)
                        if match:
                            spec_plan_refs.append(match.group(0))
            # Also check inline
            inline_refs = re.findall(r'(\.hermes/plans/[.\w/-]+\.md|\.\./plans/[.\w/-]+\.md)', spec_text)
            spec_plan_refs.extend(inline_refs)

            plan_name = path.name
            for ref in spec_plan_refs:
                if plan_name in ref or path.stem in ref:
                    reverse_refs += 1
                    break

        if reverse_refs > 0:
            # Already at max 20, but this confirms bidirectional
            pass
        elif spec_total > 0:
            # Plan references specs but no specs reference back
            coupling_pts = min(coupling_pts, 15)

    coupling_pts = min(coupling_pts, 20)

    # Status Tracking (15 pts) — reduced from 20 to make room for coupling
    status = fm.get("status", "")
    valid = status in {"draft", "in_progress", "completed", "blocked"}
    if valid:
        status_pts = 10
    elif status:
        status_pts = 4
    else:
        status_pts = 0
    checks = sum(1 for l in lines if l.strip().startswith("- ["))
    if checks >= 3:
        status_pts += 5
    elif checks >= 1:
        status_pts += 2
    status_pts = min(status_pts, 15)

    # DRY (15 pts) — reduced from 20
    n_lines = len(lines)
    if n_lines <= MAX_LINE:
        dry_pts = 15
    elif n_lines <= MAX_LINE * 1.5:
        dry_pts = 9
    else:
        dry_pts = 4

    total = fm_pts + struct_pts + content_pts + coupling_pts + status_pts + dry_pts
    return {
        "file": str(path),
        "score": total,
        "rating": "PASS" if total >= 70 else "WARN" if total >= 50 else "FAIL",
        "dims": {
            "frontmatter": fm_pts,
            "structure": struct_pts,
            "content": content_pts,
            "spec_coupling": coupling_pts,
            "status": status_pts,
            "dry": dry_pts,
        },
        "lines": n_lines,
        "phases": phase_count,
        "gates": gate_count,
        "status": status,
        "checklist_items": checks,
        "spec_refs": spec_refs,
        "spec_valid": spec_valid,
        "spec_total": spec_total,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Plans Judge")
    ap.add_argument("--plans-dir", default=".hermes/plans")
    ap.add_argument("--specs-dir", default=".hermes/specs", help="dir containing specs (for cross-validation)")
    ap.add_argument("--output", default="judge_results/plans_audit")
    ap.add_argument("--threshold", type=int, default=70)
    args = ap.parse_args()

    pdir = Path(args.plans_dir)
    if not pdir.is_dir():
        print(f"ERR: plans dir not found: {pdir}", file=sys.stderr)
        return 1

    specs_dir = Path(args.specs_dir) if args.specs_dir else None

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)

    results = [score_one(p, specs_dir) for p in sorted(pdir.glob("*.md"))]
    avg = sum(r["score"] for r in results) / max(len(results), 1)
    passed = sum(1 for r in results if r["score"] >= args.threshold)

    (out.with_suffix(".json")).write_text(json.dumps({
        "ts": datetime.utcnow().isoformat() + "Z",
        "dir": str(pdir),
        "specs_dir": str(specs_dir) if specs_dir else None,
        "threshold": args.threshold,
        "count": len(results),
        "avg": round(avg, 1),
        "passed": passed,
        "results": results,
    }, indent=2))

    md = [
        f"# Plans Audit — {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        f"Dir: `{pdir}` | Specs Dir: `{specs_dir}` | Threshold: {args.threshold}",
        f"Count: {len(results)} | Avg: {avg:.1f} | Passed: {passed}",
        "",
        "| File | Score | Rating | FM | Struct | Content | Spec Coupling | Status | DRY | Phases | Gates |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for r in results:
        d = r["dims"]
        md.append(
            f"| `{Path(r['file']).name}` | {r['score']} | {r['rating']} | "
            f"{d['frontmatter']} | {d['structure']} | {d['content']} | "
            f"{d['spec_coupling']} | {d['status']} | {d['dry']} | {r['phases']} | {r['gates']} |"
        )
    (out.with_suffix(".md")).write_text("\n".join(md) + "\n")
    print(f"Plans Judge: {len(results)} files, avg {avg:.1f}, passed {passed}/{len(results)}")
    print(f"Report: {out.with_suffix('.md')}")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())