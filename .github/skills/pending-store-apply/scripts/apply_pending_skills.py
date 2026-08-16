# apply_pending_skills.py — Phase 2: ordered, non-destructive executor for pending/skills.
# Copies entries to an inbox (so the approval store is never mutated mid-run), sorts by
# created_at, then applies create -> write_file -> patch/edit -> delete.
# Missing old_string = non-destructive skip (never force). Adjust CONFIG per env.
import json, os, glob, shutil

# ===== CONFIG (edit per environment) =====
SKILLS_ROOT = "C:/Users/Alexa/AppData/Local/hermes/skills"
PENDING = "C:/Users/Alexa/AppData/Local/hermes/pending/skills"
INBOX = "C:/Users/Alexa/Desktop/SandBox/scripts/_pending_skills_inbox"
# =========================================

os.makedirs(INBOX, exist_ok=True)
for f in glob.glob(os.path.join(PENDING, "*.json")):
    if os.path.basename(f).startswith("_"):
        continue
    shutil.copy(f, os.path.join(INBOX, os.path.basename(f)))

def find_existing(basename):
    return [d for d in glob.glob(os.path.join(SKILLS_ROOT, "**", basename), recursive=True) if os.path.isdir(d)]

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
for f in sorted(glob.glob(os.path.join(INBOX, "*.json"))):
    data = json.load(open(f, encoding="utf-8"))
    entries.append((data.get("created_at", 0), data["id"], data["action"], data.get("payload", {})))
entries.sort(key=lambda x: x[0])

def do_create(p):
    name = p["name"]; content = p.get("content", ""); cat = p.get("category", "")
    d, exists = resolve_dir(name)
    if exists:
        return ("skipped", f"create target exists: {d}")
    d = resolve_dir(name)[0] if "/" in name.replace("\\", "/") else (os.path.join(SKILLS_ROOT, cat, name) if (cat and cat != "development") else os.path.join(SKILLS_ROOT, name))
    os.makedirs(d, exist_ok=True)
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
    name = p["name"]; old = p.get("old_string", ""); new = p.get("new_string", ""); fp = p.get("file_path", "")
    d, exists = resolve_dir(name)
    if not exists:
        return ("skipped", f"patch target missing: {name}")
    target = os.path.join(d, *fp.split("/")) if fp else os.path.join(d, "SKILL.md")
    if not os.path.isfile(target):
        return ("skipped", f"patch file missing: {target}")
    txt = open(target, encoding="utf-8").read()
    if old not in txt:
        return ("failed", f"old_string not found in {target}")
    open(target, "w", encoding="utf-8").write(txt.replace(old, new, 1))
    return ("applied", f"patched {target}")

handlers = {"create": do_create, "write_file": do_write_file, "patch": do_patch, "edit": do_patch, "delete": lambda p: (("skipped", f"delete target missing: {p['name']}") if not resolve_dir(p["name"])[0] else ("applied", f"deleted {resolve_dir(p['name'])[0]}") and shutil.rmtree(resolve_dir(p["name"])[0]))}

for ts, tid, act, p in entries:
    try:
        status, msg = handlers[act](p)
        results[status].append((tid, p.get("name", "?"), act, msg))
    except Exception as e:
        results["failed"].append((tid, p.get("name", "?"), act, f"EXC {e}"))

shutil.rmtree(INBOX, ignore_errors=True)
print(f"APPLIED={len(results['applied'])} FAILED={len(results['failed'])} SKIPPED={len(results['skipped'])}")
print("FAILED:", results["failed"][:10])
print("SKIPPED (sample):", results["skipped"][:8])
