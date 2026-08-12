#!/usr/bin/env python3
"""Phase 3 (Class C) — missing fence closer reconstruction.

Fixes files where ` ``` ` (closer) + blank + ` ```lang ` (next opener)
collapsed into just ` ```lang ` — i.e. a lang-opener appears while a fence
is still open. Inserts the missing bare closer (+ blank) before it.

Pattern:
    ```python
    ...code...
    ```json          <- lang opener while fence open → missing closer
becomes:
    ```python
    ...code...
    ```

    ```json
"""
import argparse
import re
from pathlib import Path

ROOT = Path.home() / "Desktop/SandBox/.github/prompts"

FENCE_RE = re.compile(r"^(\s*)(`{3,})(.*)$")


def process(text: str) -> tuple[list[str], list[tuple[int, str]]]:
    """Return (new_lines, [(orig_line_no, reason)])."""
    lines = text.splitlines()
    out: list[str] = []
    open_len: int | None = None  # backtick length of currently open fence
    fixes: list[tuple[int, str]] = []
    for i, line in enumerate(lines):
        m = FENCE_RE.match(line)
        if not m:
            out.append(line)
            continue
        n = len(m.group(2))
        rest = m.group(3).strip()
        if rest:
            # lang opener
            if open_len is not None and open_len == n:
                # missing closer before this opener
                out.append("```")  # bare closer
                out.append("")     # blank line
                fixes.append((i + 1, f"inserted missing ``` before opener {line.strip()!r}"))
                open_len = None
            elif open_len is not None:
                # different-length open fence; lang line is content inside it
                out.append(line)
                continue
            open_len = n
            out.append(line)
        else:
            # bare fence line
            if open_len is not None and open_len == n:
                open_len = None  # closer
            elif open_len is None:
                open_len = n  # opener
            # else: mismatched length inside open fence → content, keep
            out.append(line)
    return out, fixes


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--files", nargs="*", default=[])
    args = ap.parse_args()

    targets = [ROOT / f for f in args.files] if args.files else sorted(ROOT.glob("*.md"))
    total_fixes = 0
    for path in targets:
        text = path.read_text(encoding="utf-8")
        out, fixes = process(text)
        if fixes:
            print(f"{path.name}: {len(fixes)} missing-closer fix(es)")
            for ln, reason in fixes[:12]:
                print(f"  L{ln}: {reason}")
            if args.apply:
                new_text = "\n".join(out) + "\n"
                path.write_text(new_text, encoding="utf-8", newline="\n")
            total_fixes += len(fixes)
    print(f"SUMMARY: {total_fixes} missing-closer fix(es) "
          + ("APPLIED" if args.apply else "(dry-run — re-run with --apply)"))


if __name__ == "__main__":
    main()
