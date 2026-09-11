#!/usr/bin/env python3
"""Normalize SKILL.md files with a heading BEFORE the YAML frontmatter.

Pattern:  ^# .+\n+---\n...name:...\n---  ->  standard layout (frontmatter first).
Only touches files that match the exact pattern; logs every change.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

SKILLS = Path(r"C:\Users\Alexa\AppData\Local\hermes\skills")
LOG = Path(__file__).resolve().parent.parent / "results" / "skill-frontmatter-normalized-2026-09-11.md"

PAT = re.compile(r"^(# [^\n]+\n+)(---\r?\n.*?\r?\n---)(\r?\n.*)$", re.S)


def main() -> int:
    changed = 0
    rows: list[str] = []
    for sk in sorted(SKILLS.rglob("SKILL.md")):
        if any(".quarantine" in p for p in sk.parts):
            continue
        text = sk.read_text(encoding="utf-8", errors="replace")
        m = PAT.match(text)
        if not m:
            continue
        heading, fm, body = m.group(1), m.group(2), m.group(3)
        # dedupe: if frontmatter title equals heading text, drop heading entirely
        title = re.search(r"^title:\s*['\"]?(.+?)['\"]?\s*$", fm, re.M)
        clean = heading.lstrip("#").strip().lower()
        keep_heading = not (title and title.group(1).strip().lower() == clean)
        new_text = fm + ("\n\n" + heading if keep_heading else "\n\n") + body.lstrip("\n") + "\n"
        if new_text != text:
            sk.write_text(new_text, encoding="utf-8", newline="\n")
            changed += 1
            rows.append(f"| {sk.parent.relative_to(SKILLS)} | {'heading kept' if keep_heading else 'heading dropped (title exists)'} |")
    LOG.write_text(
        "# Frontmatter Normalization — 2026-09-11\n\n"
        f"{changed} file(s) normalized\n\n| Skill | Action |\n|---|---|\n" + "\n".join(rows) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"normalized: {changed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())