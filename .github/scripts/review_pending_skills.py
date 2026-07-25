#!/usr/bin/env python3
"""Review pending skills in the hermes pending queue."""

import asyncio
import glob
import json
import os
from collections import Counter, defaultdict

HERMES_HOME = os.environ.get("LOCALAPPDATA", os.path.expanduser("~/AppData/Local")) + "/hermes"
SKILLS_ROOT = os.path.join(HERMES_HOME, "skills")
PENDING = os.path.join(HERMES_HOME, "pending", "skills")


def find_skill_dir(basename):
    """Find an existing skill dir by basename anywhere under skills root."""
    hits = []
    for d in glob.glob(os.path.join(SKILLS_ROOT, "**", basename), recursive=True):
        if os.path.isdir(d):
            hits.append(d)
    return hits


def resolve_name(name, category):
    """Resolve pending name -> (candidate_path, exists, found_paths)."""
    # name may contain '\\' (category prefix) on windows
    norm = name.replace("\\", "/")
    if "/" in norm:
        cand = os.path.join(SKILLS_ROOT, *norm.split("/"))
        return cand, os.path.isdir(cand), []
    # no slash: locate by basename on disk
    found = find_skill_dir(norm)
    if found:
        return found[0], True, found
    # not on disk: where to create?
    if category and category != "development":
        cand = os.path.join(SKILLS_ROOT, category, norm)
    else:
        cand = os.path.join(SKILLS_ROOT, norm)
    return cand, False, found


async def main():
    rows = []
    action_counter = Counter()
    target_multi = defaultdict(list)
    delete_targets = []
    edit_targets = []
    garbage = []

    files = sorted(glob.glob(os.path.join(PENDING, "*.json")))
    for f in files:
        data = json.load(open(f, encoding="utf-8"))
        p = data.get("payload", {})
        act = data["action"]
        name = p.get("name", "?")
        cat = p.get("category", "")
        action_counter[act] += 1
        cand, exists, _found = resolve_name(name, cat)
        rows.append((data["id"], act, name, cat, cand, exists))
        target_multi[name].append(data["id"])
        if act == "delete":
            delete_targets.append((data["id"], name, cand, exists))
        if act == "edit":
            edit_targets.append((data["id"], name, cand, exists))
        # garbage detection: replace with empty or trivial
        if act in ("patch",) and p.get("new_string", "") == "":
            garbage.append((data["id"], name, "empty new_string"))
        if act == "batch":
            for op in p.get("operations", []):
                if op.get("action") == "replace" and op.get("content", "") == "":
                    garbage.append((data["id"], name, f"batch replace empty: {op.get('old_text', '')[:30]}"))

    print("=== ACTION HISTOGRAM ===")
    for k, v in action_counter.most_common():
        print(f"  {k:10} {v}")

    print(f"\n=== DELETE TARGETS ({len(delete_targets)}) ===")
    for tid, name, cand, exists in delete_targets:
        print(f"  {tid} | {name} | exists={exists} | {cand}")

    print(f"\n=== EDIT/REWRITE TARGETS ({len(edit_targets)}) ===")
    for tid, name, cand, exists in edit_targets:
        print(f"  {tid} | {name} | exists={exists}")

    print("\n=== DUPLICATE-PATCHED TARGETS (patched >1x) ===")
    for name, ids in target_multi.items():
        if len(ids) > 1:
            acts = [r[1] for r in rows if r[2] == name]
            print(f"  {name}: {len(ids)}x {acts}")

    print(f"\n=== GARBAGE / EMPTY MUTATIONS ({len(garbage)}) ===")
    for tid, name, note in garbage:
        print(f"  {tid} | {name} | {note}")

    print("\n=== TARGETS NOT FOUND ON DISK (would create/relocate) ===")
    missing = [(r[0], r[2], r[3]) for r in rows if not r[5] and r[1] in ("patch", "edit", "write_file", "delete")]
    for tid, name, cand in missing:
        print(f"  {tid} | {name} | {cand}")
    print(f"\nTotal skills pending: {len(rows)}")


if __name__ == "__main__":
    asyncio.run(main())
