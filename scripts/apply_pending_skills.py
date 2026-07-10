import json, os, glob, shutil, re, sys

HERMES_HOME = os.environ.get("LOCALAPPDATA", os.path.expanduser("~/AppData/Local")) + "/hermes"
SKILLS_ROOT = os.path.join(HERMES_HOME, "skills")
PENDING = "C:/Users/Alexa/Desktop/SandBox/scripts/_pending_skills_inbox"
# Use a staging copy so we never mutate the approval store mid-run
os.makedirs(PENDING, exist_ok=True)
for f in glob.glob(os.path.join(HERMES_HOME, "pending", "skills", "*.json")):
    if os.path.basename(f).startswith("_"):
        continue
    shutil.copy(f, os.path.join(PENDING, os.path.basename(f)))

def find_existing(basename):
    hits = []
    for d in glob.glob(os.path.join(SKILLS_ROOT, "**", basename), recursive=True):
        if os.path.isdir(d):
            hits.append(d)
    return hits

def resolve_dir(name):
    norm = name.replace("\\", "/")
    if "/" in norm:
        return os.path.join(SKILLS_ROOT, *norm.split("/")), True
    found = find_existing(norm)
    if found:
        return found[0], True
    return None, False

results = {"applied": [], "failed": [], "skipped": []}
entries = []
for f in sorted(glob.glob(os.path.join(PENDING, "*.json"))):
    data = json.load(open(f, encoding="utf-8"))
    p = data.get("payload", {})
    entries.append((data.get("created_at", 0), data["id"], data["action"], p))

entries.sort(key=lambda x: x[0])  # timestamp order

def do_create(p):
    name = p["name"]; content = p.get("content", ""); cat = p.get("category", "")
    d, exists = resolve_dir(name)
    if exists:
        # already on disk: fall through to patch-like behavior if content differs
        return ("skipped", f"create target exists: {d}")
    if "/" in name.replace("\\", "/"):
        d = resolve_dir(name)[0]
    elif cat and cat != "development":
        d = os.path.join(SKILLS_ROOT, cat, name)
    else:
        d = os.path.join(SKILLS_ROOT, name)
    os.makedirs(d, exist_ok=True)
    # content may include frontmatter + body; write to SKILL.md
    open(os.path.join(d, "SKILL.md"), "w", encoding="utf-8").write(content)
    return ("applied", f"created {d}")

def do_write_file(p):
    name = p["name"]; fp = p.get("file_path", ""); content = p.get("content", "")
    d, exists = resolve_dir(name)
    if not exists:
        return ("skipped", f"write_file target missing: {name}")
    target = os.path.join(d, *fp.split("/")) if fp else os.path.join(d, "SKILL.md")
    os.makedirs(os.path.dirname(target), exist_ok=True)
    open(target, "w", encoding="utf-8").write(content)
    return ("applied", f"wrote {target}")

def do_patch(p):
    name = p["name"]; old = p.get("old_string", ""); new = p.get("new_string", "")
    fp = p.get("file_path", "")
    d, exists = resolve_dir(name)
    if not exists:
        return ("skipped", f"patch target missing: {name}")
    target = os.path.join(d, *fp.split("/")) if fp else os.path.join(d, "SKILL.md")
    if not os.path.isfile(target):
        return ("skipped", f"patch file missing: {target}")
    txt = open(target, encoding="utf-8").read()
    if old not in txt:
        return ("failed", f"old_string not found in {target}")
    txt2 = txt.replace(old, new, 1)
    open(target, "w", encoding="utf-8").write(txt2)
    return ("applied", f"patched {target}")

def do_edit(p):
    # edit = rewrite: old_string/new_string full replacement
    return do_patch(p)

def do_delete(p):
    name = p["name"]
    d, exists = resolve_dir(name)
    if not exists:
        return ("skipped", f"delete target missing: {name}")
    shutil.rmtree(d)
    return ("applied", f"deleted {d}")

handlers = {"create": do_create, "write_file": do_write_file, "patch": do_patch,
            "edit": do_edit, "delete": do_delete}

for ts, tid, act, p in entries:
    try:
        status, msg = handlers[act](p)
        results[status].append((tid, p.get("name", "?"), act, msg))
    except Exception as e:
        results["failed"].append((tid, p.get("name", "?"), act, f"EXC {e}"))

print(f"APPLIED={len(results['applied'])} FAILED={len(results['failed'])} SKIPPED={len(results['skipped'])}")
print("\n=== FAILED ===")
for r in results["failed"]:
    print(f"  {r[0]} | {r[1]} | {r[2]} | {r[3]}")
print("\n=== SKIPPED ===")
for r in results["skipped"]:
    print(f"  {r[0]} | {r[1]} | {r[2]} | {r[3]}")

# Write a machine-readable report
with open("C:/Users/Alexa/Desktop/SandBox/scripts/_pending_skills_report.json", "w") as fh:
    json.dump(results, fh, indent=2)
