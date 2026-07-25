# review_pending_skills.py — Phase 1: review + prune the skills pending store.
# Adjust CONFIG to your HERMES_HOME, then: python review_pending_skills.py
import json, os, glob
from collections import Counter, defaultdict

# ===== CONFIG (edit per environment) =====
SKILLS_ROOT = "C:/Users/Alexa/AppData/Local/hermes/skills"
PENDING = "C:/Users/Alexa/AppData/Local/hermes/pending/skills"
# =========================================

def find_skill_dir(basename):
    return [d for d in glob.glob(os.path.join(SKILLS_ROOT, "**", basename), recursive=True) if os.path.isdir(d)]

def resolve_name(name, category):
    norm = name.replace("\\", "/")
    if "/" in norm:
        return os.path.join(SKILLS_ROOT, *norm.split("/")), True
    found = find_skill_dir(norm)
    if found:
        return found[0], True
    cand = os.path.join(SKILLS_ROOT, category, norm) if (category and category != "development") else os.path.join(SKILLS_ROOT, norm)
    return cand, False

rows = []; action_counter = Counter(); target_multi = defaultdict(list)
delete_targets = []; edit_targets = []; garbage = []
files = sorted(glob.glob(os.path.join(PENDING, "*.json")))
for f in files:
    data = json.load(open(f, encoding="utf-8")); p = data.get("payload", {})
    act = data["action"]; name = p.get("name", "?"); cat = p.get("category", "")
    action_counter[act] += 1
    cand, exists, _ = resolve_name(name, cat)
    rows.append((data["id"], act, name, cat, cand, exists))
    target_multi[name].append(data["id"])
    if act == "delete":
        delete_targets.append((data["id"], name, cand, exists))
    if act == "edit":
        edit_targets.append((data["id"], name, cand, exists))
    if act in ("patch",) and p.get("new_string", "") == "":
        garbage.append((data["id"], name, "empty new_string"))
    if act == "batch":
        for op in p.get("operations", []):
            if op.get("action") == "replace" and op.get("content", "") == "":
                garbage.append((data["id"], name, f"batch replace empty: {op.get('old_text','')[:30]}"))

print("=== ACTION HISTOGRAM ===")
for k, v in action_counter.most_common():
    print(f"  {k:10} {v}")
print(f"\n=== DELETE TARGETS ({len(delete_targets)}) ===")
for tid, name, cand, exists in delete_targets:
    print(f"  {tid} | {name} | exists={exists}")
print(f"\n=== EDIT/REWRITE TARGETS ({len(edit_targets)}) ===")
for tid, name, cand, exists in edit_targets:
    print(f"  {tid} | {name} | exists={exists}")
print(f"\n=== GARBAGE / EMPTY MUTATIONS ({len(garbage)}) ===")
for tid, name, note in garbage:
    print(f"  {tid} | {name} | {note}")

# Move garbage (no-ops) into _pruned/ — non-destructive
pruned = os.path.join(PENDING, "_pruned"); os.makedirs(pruned, exist_ok=True)
moved = 0
for tid, name, _ in garbage:
    src = os.path.join(PENDING, f"{tid}.json")
    if os.path.isfile(src):
        os.rename(src, os.path.join(pruned, f"{tid}.json")); moved += 1
print(f"\n=== PRUNED {moved} garbage/no-op entries to _pruned/ ===")

print(f"\n=== DUPLICATE-PATCHED TARGETS (patched >1x) ===")
for name, ids in target_multi.items():
    if len(ids) > 1:
        print(f"  {name}: {len(ids)}x {[r[1] for r in rows if r[2]==name]}")
print(f"\nTotal skills pending: {len(files) - moved}")
