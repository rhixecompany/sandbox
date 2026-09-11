#!/usr/bin/env python3
"""Reconstruct the skills tree to its pre-dedupe state.

Sources of truth: results/skills-dup-analysis-2026-09-11.json (221 paths).
For every expected skill dir:
  1. If <dir>/SKILL.md is a DIRECTORY (move-nesting pathology), flatten it.
  2. If the dir is missing, find a candidate dir by name elsewhere in the tree
     (containing a SKILL.md) and move it home.
Logs everything; read-only for anything not matching a known path.
"""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

SKILLS = Path(r"C:\Users\Alexa\AppData\Local\hermes\skills")
RESULTS = Path(__file__).resolve().parent.parent / "results"
ANALYSIS = RESULTS / "skills-dup-analysis-2026-09-11.json"


def skill_dirs() -> set[Path]:
    out: set[Path] = set()
    data = json.loads(ANALYSIS.read_text(encoding="utf-8"))
    for cluster in data["clusters"]:
        for p in cluster["paths"]:
            out.add(SKILLS / Path(p["path"]).parent)
    return out


def main() -> int:
    expected = skill_dirs()
    print(f"expected skill dirs: {len(expected)}")
    flattened = 0
    moved = 0
    for d in sorted(expected):
        while (d / "SKILL.md").is_dir():
            nested = d / "SKILL.md"
            tmp = d / ".flatten-tmp"
            tmp.mkdir(exist_ok=True)
            for child in sorted(nested.iterdir()):
                tgt = tmp / child.name
                if tgt.exists():
                    (shutil.rmtree(tgt) if tgt.is_dir() else tgt.unlink())
                shutil.move(str(child), str(tgt))
            nested.rmdir()
            for child in sorted(tmp.iterdir()):
                tgt = d / child.name
                if tgt.exists():
                    print(f"collision at {tgt} — keeping existing, dropping nested copy")
                    continue
                shutil.move(str(child), str(tgt))
            tmp.rmdir()
            flattened += 1
            print(f"flattened: {d.relative_to(SKILLS)}")
        if not any(d.rglob("SKILL.md")):
            # missing — search the whole tree for a same-named dir with a SKILL.md
            name = d.name
            candidates = sorted(
                p for p in SKILLS.rglob("*") if p.is_dir() and p.name == name and any(p.rglob("SKILL.md")) and p != d
            )
            if len(candidates) == 1:
                src = candidates[0]
                # don't capture a dir that is inside another expected location
                if d.parent.exists():
                    shutil.move(str(src), str(d))
                    moved += 1
                    print(f"moved home: {src.relative_to(SKILLS)} -> {d.relative_to(SKILLS)}")
                else:
                    print(f"missing parent for {d}; candidate {src}")
            else:
                print(f"MISSING (candidates={len(candidates)}): {d.relative_to(SKILLS)}")
    # sanity: count SKILL.md files
    total = sum(1 for _ in SKILLS.rglob("SKILL.md") if ".quarantine" not in str(_))
    print(f"flattened: {flattened} | moved: {moved} | total SKILL.md now: {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())