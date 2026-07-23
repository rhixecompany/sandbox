#!/usr/bin/env python3
"""Verify duplicate-path skills: only delete flat-root copy if it is byte-identical
to the canonical category-subdir copy. Safety-first: no deletion otherwise.
Writes a JSON report of what was/wasn't removed."""
from __future__ import annotations
import asyncio
import json, shutil, hashlib, os
from pathlib import Path

HERMES_HOME = Path(os.environ.get("HOME", os.path.expanduser("~"))) / "AppData" / "Local" / "hermes"
SANDBOX = Path(os.environ.get("HOME", os.path.expanduser("~"))) / "Desktop" / "SandBox"

async def main():
    SKILLS = HERMES_HOME / "skills"
    loop = asyncio.get_running_loop()

    # Parse the dedupe-report.md table for (name, flat_path, canonical_path)
    report_text = await loop.run_in_executor(None, _read_text, SANDBOX / "docs/dedupe-report.md")
    import re
    rows = []
    for m in re.finditer(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", report_text, re.M):
        name = m.group(1).strip()
        loc = m.group(2).strip().replace("\\", "/")
        if name in ("Skill",) or set(name) <= set("- "):
            continue
        if "/" in loc and name == loc.split("/")[-1]:
            # canonical (has slash) vs flat (no slash)
            flat = SKILLS / name
            canon = SKILLS / loc
            rows.append((name, flat, canon))

    removed, kept = [], []
    for name, flat, canon in rows:
        flat_sm = flat / "SKILL.md"
        canon_sm = canon / "SKILL.md"
        if not flat_sm.exists() or not canon_sm.exists():
            kept.append((name, "missing-path"))
            continue
        flat_data = await loop.run_in_executor(None, flat_sm.read_bytes)
        canon_data = await loop.run_in_executor(None, canon_sm.read_bytes)
        flat_hash = hashlib.md5(flat_data).hexdigest()
        canon_hash = hashlib.md5(canon_data).hexdigest()
        if flat_hash == canon_hash:
            # byte-identical — safe to remove flat copy
            try:
                await loop.run_in_executor(None, shutil.rmtree, flat)
                removed.append((name, str(flat)))
            except Exception as e:
                kept.append((name, f"rm-error:{e}"))
        else:
            kept.append((name, "differs-from-canonical"))

    out = {"removed": removed, "kept": kept,
           "removed_count": len(removed), "kept_count": len(kept)}
    await loop.run_in_executor(None, _write_json, SANDBOX / "judge_results/dedupe_action_report.json", out)
    print(f"Removed {len(removed)} identical flat duplicates; kept {len(kept)} (differ/missing).")
    for r in removed:
        print("  REMOVED", r[0])
    for k in kept:
        print("  KEPT   ", k[0], k[1])

def _read_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def _write_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    asyncio.run(main())
