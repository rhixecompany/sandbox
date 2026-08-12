#!/usr/bin/env python3
"""Corruption-marker sweep for .github/prompts/*.md (Class A/B/C/D).

Read-only. Emits a JSON artifact with per-file scores so later passes can
verify 0 hits for classes A/B/C and count D.

Classes:
  A. Doubled leading pipes        ^\|\|            (table rows)
  B. Glued headings               ^#{2,4} <long inline run with body glue>
  C. Fence/blockquote artifacts   empty ``` pairs or '> /' inside fences
  D. plan: 'None' string          frontmatter plan == 'None'
  LF. CRLF bytes present          \r\n
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # .github/prompts
OUT = Path.home() / "Desktop/SandBox/.hermes/plans/docs"

PIPE_LEAD = re.compile(r"^\|{2,}")
GLUED_HEAD = re.compile(r"^(#{2,4})\s+(\S.*)$")


def count_glued_heading(line: str) -> int:
    m = GLUED_HEAD.match(line)
    if not m:
        return 0
    body = m.group(2)
    # A glued heading: run is very long (> 120) OR contains fence markers,
    # AND there is a body-sentence boundary (2+ spaces + lowercase) OR
    # an inline code backtick run that indicates body text.
    if len(body) > 120:
        return 1
    if "```" in body or "`" in body:
        return 1
    if re.search(r"\s{2,}[a-z(]", body):
        return 1
    return 0


def count_fence_artifacts(text: str) -> int:
    hits = 0
    # empty fence pairs: ```\n``` adjacent
    hits += len(re.findall(r"```\s*\n\s*```", text))
    # '> /' artifacts inside fences (rough: any '> /' line)
    hits += len(re.findall(r"^\s*>\s*/\s*$", text, re.M))
    return hits


def scan_file(path: Path) -> dict:
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return {"file": path.name, "error": "non-utf8"}
    lines = text.splitlines()
    cls_a = sum(1 for ln in lines if PIPE_LEAD.match(ln))
    cls_b = sum(1 for ln in lines if count_glued_heading(ln))
    cls_c = count_fence_artifacts(text)
    cls_d = 1 if re.search(r"^plan:\s*['\"]?None['\"]?\s*$", text, re.M) else 0
    crlf = raw.count(b"\r\n")
    return {
        "file": path.name,
        "A": cls_a,
        "B": cls_b,
        "C": cls_c,
        "D": cls_d,
        "CRLF": crlf,
        "score": cls_a + cls_b * 2 + cls_c * 3 + cls_d,
    }


def main() -> None:
    files = sorted(ROOT.glob("*.md"))
    results = [scan_file(p) for p in files]
    totals = {"A": 0, "B": 0, "C": 0, "D": 0, "CRLF": 0, "files": len(results)}
    for r in results:
        if "error" in r:
            continue
        for k in ("A", "B", "C", "D", "CRLF"):
            totals[k] += r[k]
    out = {
        "generated": __import__("datetime").datetime.now().isoformat(timespec="seconds"),
        "totals": totals,
        "files": results,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    ts = __import__("datetime").datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path = OUT / f"prompts-baseline-{ts}.json"
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"Wrote {out_path}")
    print(f"TOTALS A={totals['A']} B={totals['B']} C={totals['C']} D={totals['D']} CRLF={totals['CRLF']} files={totals['files']}")
    # Top offenders
    scored = sorted([r for r in results if "error" not in r], key=lambda r: -r["score"])
    print("TOP 10 by score:")
    for r in scored[:10]:
        print(f"  {r['score']:>3}  {r['file']}")


if __name__ == "__main__":
    sys.exit(main())
