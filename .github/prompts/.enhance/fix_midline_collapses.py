#!/usr/bin/env python3
"""Phase 3 (Class C) — mid-line newline-collapse repair.

Repairs lines where multiple intact lines were collapsed into a single
current line (no separators), e.g.:

    current:  Only display results in table with icons:```markdown| Module |...
    intact:   Only display results in table with icons:
              (blank)
              ```markdown
              | Module | ...

Repair strategy: splice the intact line range (from commit 879b4532) back in,
replacing the collapsed current line. Only applied when the normalized current
line EXACTLY equals the normalized concatenation of the intact range with >= 2
non-empty lines — a lossless, verifiable match. No heuristic splitting.

Usage (run from repo root):
    python .github/prompts/.enhance/fix_midline_collapses.py            # dry-run
    python .github/prompts/.enhance/fix_midline_collapses.py --apply    # write
    python .github/prompts/.enhance/fix_midline_collapses.py --files NAME [--apply]

Notes:
- Byte-preserving IO: detects CRLF vs LF per file and writes back the same.
- Reports ORIGINAL line numbers (pre-edit positions).
- 4-backtick fences in intact (````markdown ... ````) are legitimate paired
  fences and are restored verbatim.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path.home() / "Desktop/SandBox"
CUR = ROOT / ".github/prompts"
INTACT_COMMIT = "879b4532"
DEFAULT_FILES = [
    "comicwise-development.prompt.md",
    "create-llms.prompt.md",
    "create-oo-component-documentation.prompt.md",
    "java-mcp-server-generator.prompt.md",
    "memory-merger.prompt.md",
    "php-mcp-server-generator.prompt.md",
    "skills-fix.prompt.md",
    "swift-mcp-server-generator.prompt.md",
    "tldr-prompt.prompt.md",
    "update-avm-modules-in-bicep.prompt.md",
]


def norm(s: str) -> str:
    return re.sub(r"\s+", "", s)


def intact_lines(name: str) -> list[str] | None:
    r = subprocess.run(
        ["git", "show", f"{INTACT_COMMIT}:.github/prompts/{name}"],
        cwd=ROOT, capture_output=True, text=True,
    )
    if r.returncode != 0:
        return None
    return r.stdout.splitlines()


def find_collapse(cline: str, il: list[str]) -> tuple[int, int, int] | None:
    """Return (start, end, nonempty) 1-based intact slice whose normalized
    concat exactly equals normalized cline, with >= 2 non-empty lines and the
    current line longer than any single intact line. Else None."""
    cnorm = norm(cline)
    if not cnorm:
        return None
    for start in range(len(il)):
        acc = ""
        nonempty = 0
        for end in range(start, len(il)):
            if il[end].strip():
                nonempty += 1
            acc += norm(il[end])
            if acc == cnorm and end > start and nonempty >= 2:
                if len(cline) > max((len(x) for x in il[start : end + 1]), default=0):
                    return (start + 1, end + 1, nonempty)
            if len(acc) > len(cnorm):
                break
    return None


def read_text(p: Path) -> tuple[str, str]:
    b = p.read_bytes()
    nl = "\r\n" if b"\r\n" in b else "\n"
    return b.decode("utf-8", errors="replace"), nl


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--files", nargs="*", default=DEFAULT_FILES)
    args = ap.parse_args()

    total = 0
    for name in args.files:
        path = CUR / name
        il = intact_lines(name)
        if il is None:
            print(f"{name}: no intact at {INTACT_COMMIT}, skipped")
            continue
        text, nl = read_text(path)
        lines = text.split(nl)
        # collect genuine collapses (current line -> intact slice)
        fixes: list[tuple[int, tuple[int, int, int], str]] = []
        for ci, cline in enumerate(lines, 1):
            hit = find_collapse(cline, il)
            if hit:
                fixes.append((ci, hit, cline[:60]))
        if not fixes:
            print(f"{name}: 0 midline collapses")
            continue
        print(f"{name}: {len(fixes)} midline collapse(s)")
        for ci, (s, e, n), preview in fixes:
            print(f"  cur L{ci} -> intact L{s}-L{e} ({n} nonempty): {preview!r}")
        if not args.apply:
            total += len(fixes)
            continue
        # apply bottom-up so line numbers stay valid
        for ci, (s, e, _n), _prev in sorted(fixes, key=lambda x: x[0], reverse=True):
            replacement = il[s - 1 : e]
            lines[ci - 1 : ci] = replacement
        path.write_text(nl.join(lines) + nl, encoding="utf-8", newline="")
        total += len(fixes)

    print(f"\nSUMMARY: {total} collapse(s) {'applied' if args.apply else 'would apply'} (dry-run)" if not args.apply else f"\nSUMMARY: {total} collapse(s) applied")
    return 0


if __name__ == "__main__":
    sys.exit(main())
