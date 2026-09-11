#!/usr/bin/env python3
"""Undo a bad dedupe pass: move quarantined skill dirs back to their originals.

Reads the dedupe log (Keeper | Deleted | Merges) and moves every deleted path
back from the quarantine dir. Also reports which keepers received merge blocks
(those need manual block-stripping before re-running dedupe).
"""
from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

SKILLS = Path(r"C:\Users\Alexa\AppData\Local\hermes\skills")
QUARANTINE = SKILLS / ".quarantine-2026-09-11"
LOG = Path(__file__).resolve().parent.parent / "results" / "skills-deduped-2026-09-11.md"

ROW_RE = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*(\d+) section")


def main() -> int:
    if not QUARANTINE.exists():
        print("no quarantine dir; nothing to restore")
        return 0
    restored = 0
    merged_keepers = []
    for line in LOG.read_text(encoding="utf-8", errors="replace").splitlines():
        m = ROW_RE.match(line)
        if not m:
            continue
        keeper, deleted_csv, merges = m.group(1).strip(), m.group(2).strip(), int(m.group(3))
        if merges > 0:
            merged_keepers.append(keeper)
        for rel in (d.strip() for d in deleted_csv.split(",") if d.strip()):
            q = QUARANTINE / Path(rel).parent.name
            target = SKILLS / rel
            if q.exists() and not target.exists():
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(q), str(target))
                restored += 1
            elif target.exists():
                print(f"skip (target already exists): {rel}")
    print(f"restored: {restored} skill dir(s)")
    print(f"keepers with merge blocks (strip before re-run): {len(merged_keepers)}")
    for k in merged_keepers:
        print(f"  - {k}")
    if not any(QUARANTINE.iterdir()):
        QUARANTINE.rmdir()
        print("quarantine dir removed (empty)")
    return 0


if __name__ == "__main__":
    sys.exit(main())