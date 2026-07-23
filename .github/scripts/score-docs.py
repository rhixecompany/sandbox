#!/usr/bin/env python3
"""Score Docs — Validate and score markdown documents for AI-readiness.

Provides async CLI entry points for scoring frontmatter, summary, headings,
code blocks, cross-references, and wall-of-text detection.
"""

import asyncio
import argparse
import json
import re
import sys
from pathlib import Path
from typing import List, Optional, Tuple


# ---------------------------------------------------------------------------
# Scoring criteria
# ---------------------------------------------------------------------------

def score_frontmatter(text: str) -> Tuple[int, List[str]]:
    """YAML frontmatter present and well-formed (20 pts)."""
    notes = []
    if not text.startswith("---"):
        return 0, ["No YAML frontmatter found"]
    end = text.find("---", 3)
    if end == -1:
        return 0, ["Frontmatter not closed"]
    fm = text[3:end].strip()
    if not fm:
        return 5, ["Empty frontmatter"]
    # Check for title and description
    has_title = bool(re.search(r"^title\s*:", fm, re.MULTILINE))
    has_desc = bool(re.search(r"^description\s*:", fm, re.MULTILINE))
    score = 20
    if not has_title:
        score -= 5
        notes.append("Missing title in frontmatter")
    if not has_desc:
        score -= 5
        notes.append("Missing description in frontmatter")
    return max(0, score), notes


def score_summary(text: str) -> Tuple[int, List[str]]:
    """Non-empty summary paragraph within 3 lines of H1 (15 pts)."""
    notes = []
    lines = text.splitlines()
    h1_idx = None
    for i, line in enumerate(lines):
        if line.startswith("# ") and not line.startswith("## "):
            h1_idx = i
            break
    if h1_idx is None:
        return 0, ["No H1 heading found"]
    summary_zone = lines[h1_idx + 1 : h1_idx + 5]
    for line in summary_zone:
        stripped = line.strip()
        if stripped and not stripped.startswith("#") and len(stripped) > 20:
            return 15, []
    return 5, ["No summary paragraph within 3 lines of H1"]


def score_code_blocks(text: str) -> Tuple[int, List[str]]:
    """Language-tagged fenced code blocks, 10 pts each (max 30)."""
    notes = []
    blocks = re.findall(r"```(\w+)", text)
    tagged = [b for b in blocks if b and b.lower() not in ("", "text")]
    score = min(len(tagged) * 10, 30)
    if not tagged:
        notes.append("No language-tagged code blocks found")
    return score, notes


def score_headings(text: str) -> Tuple[int, List[str]]:
    """H2/H3 breaks every <200 lines (15 pts)."""
    notes = []
    lines = text.splitlines()
    heading_lines = [
        i for i, line in enumerate(lines) if re.match(r"^#{2,3}\s", line)
    ]
    if not heading_lines:
        return 0, ["No H2 or H3 headings found"]
    max_gap = 0
    prev = 0
    for h in heading_lines:
        gap = h - prev
        if gap > max_gap:
            max_gap = gap
        prev = h
    gap_to_end = len(lines) - prev
    if gap_to_end > max_gap:
        max_gap = gap_to_end
    if max_gap <= 200:
        return 15, []
    notes.append(f"Longest section is {max_gap} lines (target <200)")
    return 10, notes


def score_crossrefs(text: str, doc_path: Path) -> Tuple[int, List[str]]:
    """Relative cross-references resolve (max 20)."""
    notes = []
    refs = re.findall(r"\[.*?\]\(((?:\.\.?/)[^)]+)\)", text)
    if not refs:
        return 0, ["No relative cross-references found"]
    resolved = 0
    doc_dir = doc_path.resolve().parent
    for ref in refs:
        target = (doc_dir / ref).resolve()
        if target.exists():
            resolved += 1
        else:
            notes.append(f"Broken ref: {ref}")
    score = min(int((resolved / len(refs)) * 20), 20)
    return score, notes


def penalty_wall_of_text(text: str) -> int:
    """Penalty -20 if >500 lines without H2/H3."""
    lines = text.splitlines()
    if len(lines) <= 500:
        return 0
    has_heading = bool(re.search(r"^#{2,3}\s", text, re.MULTILINE))
    if not has_heading:
        return -20
    return 0


# ---------------------------------------------------------------------------
# Scoring engine
# ---------------------------------------------------------------------------

async def score_document(file_path: Path, threshold: int = 70) -> dict:
    """Score a single markdown document. File I/O is offloaded via thread."""
    try:
        text = await asyncio.to_thread(file_path.read_text, encoding="utf-8")
    except Exception as exc:
        return {
            "file": str(file_path),
            "error": str(exc),
            "score": 0,
            "passed": False,
        }

    result = {"file": str(file_path), "details": {}, "notes": []}

    fm_score, fm_notes = score_frontmatter(text)
    result["details"]["frontmatter"] = fm_score
    result["notes"].extend(fm_notes)

    summary_score, summary_notes = score_summary(text)
    result["details"]["summary"] = summary_score
    result["notes"].extend(summary_notes)

    code_score, code_notes = score_code_blocks(text)
    result["details"]["code_blocks"] = code_score
    result["notes"].extend(code_notes)

    heading_score, heading_notes = score_headings(text)
    result["details"]["headings"] = heading_score
    result["notes"].extend(heading_notes)

    xref_score, xref_notes = score_crossrefs(text, file_path)
    result["details"]["crossrefs"] = xref_score
    result["notes"].extend(xref_notes)

    penalty = penalty_wall_of_text(text)
    result["details"]["wall_of_text_penalty"] = penalty

    total = (
        fm_score + summary_score + code_score + heading_score + xref_score + penalty
    )
    result["score"] = total
    result["passed"] = total >= threshold
    return result


async def main() -> None:
    parser = argparse.ArgumentParser(
        description="Score markdown documents for AI-readiness."
    )
    parser.add_argument(
        "--workspace",
        type=str,
        default=".",
        help="Root directory (default: .)",
    )
    parser.add_argument(
        "--pattern",
        type=str,
        default="**/*.md",
        help="File glob pattern (default: **/*.md)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Report output path (default: stdout)",
    )
    parser.add_argument(
        "--threshold",
        type=int,
        default=70,
        help="Pass threshold (default: 70)",
    )
    parser.add_argument(
        "--fix",
        type=str,
        default=None,
        help="Auto-fix categories: frontmatter,summary,code-blocks",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="JSON output",
    )
    args = parser.parse_args()

    workspace = Path(args.workspace).resolve()
    pattern = args.pattern

    # Gather files synchronously (CPU-bound globbing)
    files = list(workspace.glob(pattern))
    if not files:
        print(f"No files matching {pattern} in {workspace}", file=sys.stderr)
        sys.exit(1)

    # Score each document — each file I/O is individually offloaded
    results = await asyncio.gather(
        *(score_document(f, args.threshold) for f in files)
    )

    passed = [r for r in results if r.get("passed")]
    failed = [r for r in results if not r.get("passed")]

    if args.json:
        output = json.dumps(
            {"results": results, "passed": len(passed), "failed": len(failed)},
            indent=2,
        )
        if args.output:
            await asyncio.to_thread(
                Path(args.output).write_text, output, encoding="utf-8"
            )
        else:
            print(output)
    else:
        lines = [f"\n=== Score Docs Report ==="]
        lines.append(f"Scanned {len(files)} file(s) — Passed: {len(passed)}, Failed: {len(failed)}")
        for r in results:
            status = "PASS" if r.get("passed") else "FAIL"
            score = r.get("score", 0)
            fpath = r.get("file", "?")
            lines.append(f"  [{status}] {score:3d}  {fpath}")
            if r.get("notes"):
                for note in r["notes"]:
                    lines.append(f"          - {note}")
            if r.get("error"):
                lines.append(f"          ERROR: {r['error']}")
        report = "\n".join(lines)
        if args.output:
            await asyncio.to_thread(
                Path(args.output).write_text, report, encoding="utf-8"
            )
        else:
            print(report)

    sys.exit(0 if len(failed) == 0 else 1)


if __name__ == "__main__":
    asyncio.run(main())
