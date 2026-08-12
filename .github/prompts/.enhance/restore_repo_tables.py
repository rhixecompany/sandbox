#!/usr/bin/env python3
"""restore_repo_tables.py — restore real tables in the 6 repo*.md files.

The previous plan (2026-08-12 01:0x) "aligned" tables by removing internal
pipes, producing pseudo-tables that render as paragraphs (not tables). Git
history (1b2b7d7a~1) holds the real pipe-delimited tables. This script splices
history's table blocks back into the current working-tree files at matching
block offsets, keeping all current non-table content.

Lossless: table cell content comes verbatim from history; no re-splitting.

Usage: python restore_repo_tables.py [--apply]
Default is dry-run (prints per-file block count).
"""
import pathlib
import subprocess
import sys

ROOT = pathlib.Path.home() / "Desktop/SandBox"
P = ROOT / ".github/prompts"
HIST = "1b2b7d7a~1"
APPLY = "--apply" in sys.argv

FILES = [
    "repo.prompt.md",
    "repo-management.prompt.md",
    "repo-story-time.prompt.md",
    "repo-research-pipeline.prompt.md",
    "repo-tooling-implementation.prompt.md",
    "repo-init.prompt.md",
]


def table_blocks(lines):
    blocks = []
    i = 0
    n = len(lines)
    while i < n:
        if lines[i].lstrip().startswith("|"):
            j = i
            while j < n and lines[j].lstrip().startswith("|"):
                j += 1
            blocks.append((i, j))
            i = j
        else:
            i += 1
    return blocks


def main() -> int:
    for f in FILES:
        path = P / f
        cur_lines = path.read_text(encoding="utf-8").splitlines()
        hist_text = subprocess.run(
            ["git", "show", f"{HIST}:.github/prompts/{f}"],
            cwd=ROOT, capture_output=True, text=True
        ).stdout
        if not hist_text:
            print(f"SKIP {f}: no history")
            continue
        hist_lines = hist_text.splitlines()
        cur_b = table_blocks(cur_lines)
        hist_b = table_blocks(hist_lines)
        if len(cur_b) != len(hist_b) or any(
            (b[1] - b[0]) != (h[1] - h[0]) for b, h in zip(cur_b, hist_b)
        ):
            print(f"SKIP {f}: block shape mismatch")
            continue
        out = list(cur_lines)
        # Replace each current table block's lines with history's table lines.
        for (cs, ce), (hs, he) in zip(cur_b, hist_b):
            out[cs:ce] = hist_lines[hs:he]
        new_text = "\n".join(out)
        if new_text != "\n".join(cur_lines):
            if APPLY:
                path.write_text(new_text, encoding="utf-8", newline="\n")
                print(f"RESTORED {f}: {len(cur_b)} table blocks")
            else:
                print(f"WOULD RESTORE {f}: {len(cur_b)} table blocks")
        else:
            print(f"NO CHANGE {f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
