# verify_apply.py — ad-hoc verification harness for the pending-store-apply scripts.
# Redirects all hardcoded real paths to an OS-safe temp dir, exercises the 3 scripts on
# synthetic fixtures, asserts exact outcomes, then cleans up. Does NOT touch live state.
# Run: python verify_apply.py
import os, sys, json, glob, shutil, tempfile, subprocess, importlib.util

TMP = tempfile.mkdtemp(prefix="hermes-verify-")
print(f"TMP={TMP}")
ORIG = "C:/Users/Alexa/Desktop/SandBox/scripts"
REAL = "C:/Users/Alexa/AppData/Local/hermes"

def path_sub(src):
    s = src
    s = s.replace("C:/Users/Alexa/AppData/Local/hermes/skills", os.path.join(TMP, "skills").replace("\\", "/"))
    s = s.replace("C:/Users/Alexa/AppData/Local/hermes/pending/skills", os.path.join(TMP, "pending_skills").replace("\\", "/"))
    s = s.replace("C:/Users/Alexa/AppData/Local/hermes/pending/memory", os.path.join(TMP, "pending_memory").replace("\\", "/"))
    s = s.replace("C:/Users/Alexa/AppData/Local/hermes/memories/MEMORY.md", os.path.join(TMP, "MEMORY.md").replace("\\", "/"))
    s = s.replace("C:/Users/Alexa/AppData/Local/hermes/memories/USER.md", os.path.join(TMP, "USER.md").replace("\\", "/"))
    return s

def load_mod(name):
    src = open(os.path.join(ORIG, name), encoding="utf-8").read()
    out = os.path.join(TMP, name)
    open(out, "w", encoding="utf-8").write(path_sub(src))
    spec = importlib.util.spec_from_file_location(name.replace(".", "_"), out)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

print("\n[1] py_compile")
for n in ["review_pending_skills.py", "apply_pending_skills.py", "apply_pending_memory.py"]:
    r = subprocess.run([sys.executable, "-m", "py_compile", os.path.join(ORIG, n)], capture_output=True, text=True)
    assert r.returncode == 0, f"py_compile {n} FAILED: {r.stderr}"
    print(f"  OK {n}")

print("\n[2] apply_pending_skills logic")
SK = os.path.join(TMP, "skills"); PK = os.path.join(TMP, "pending_skills")
os.makedirs(SK, exist_ok=True); os.makedirs(PK, exist_ok=True)
os.makedirs(os.path.join(SK, "existing_skill"))
open(os.path.join(SK, "existing_skill", "SKILL.md"), "w").write("---\nname: existing_skill\n---\nOLD LINE\n")
def wjson(d, payload, action, created=0):
    json.dump({"id": f"{action}_{d}", "action": action, "created_at": created, "payload": payload},
              open(os.path.join(PK, f"{action}_{d}.json"), "w"))
wjson("new", {"action": "create", "name": "new_skill", "category": "development", "content": "---\nname: new_skill\n---\nbody\n"}, "create")
wjson("exist", {"action": "create", "name": "existing_skill", "category": "development", "content": "SHOULD NOT APPLY"}, "create")
wjson("patchok", {"action": "patch", "name": "existing_skill", "old_string": "OLD LINE", "new_string": "NEW LINE"}, "patch")
wjson("patchbad", {"action": "patch", "name": "existing_skill", "old_string": "NOPE", "new_string": "X"}, "patch")
wjson("wf", {"action": "write_file", "name": "existing_skill", "file_path": "references/x.md", "content": "ref content"}, "write_file")
wjson("del", {"action": "delete", "name": "ghost"}, "delete")
load_mod("apply_pending_skills.py")
assert os.path.isfile(os.path.join(SK, "new_skill", "SKILL.md")), "create new failed"
assert "SHOULD NOT APPLY" not in open(os.path.join(SK, "existing_skill", "SKILL.md")).read(), "create-existing overwrote!"
assert "NEW LINE" in open(os.path.join(SK, "existing_skill", "SKILL.md")).read(), "patch not applied"
assert os.path.isfile(os.path.join(SK, "existing_skill", "references", "x.md")), "write_file failed"
print("  OK create/patch/write_file/skip/non-destructive-fail all correct")

print("\n[3] apply_pending_memory logic")
PM = os.path.join(TMP, "pending_memory"); os.makedirs(PM, exist_ok=True)
open(os.path.join(TMP, "MEMORY.md"), "w").write("# MEMORY.md\n\n## A\nfact one\n")
open(os.path.join(TMP, "USER.md"), "w").write("# USER.md\n\nbase\n")
def wm(d, payload, action, created=0, tgt="memory"):
    payload = dict(payload); payload["target"] = tgt
    json.dump({"id": f"{action}_{d}", "action": action, "created_at": created, "payload": payload},
              open(os.path.join(PM, f"{action}_{d}.json"), "w"))
wm("a", {"action": "add", "content": "new durable fact"}, "add")
wm("dup", {"action": "add", "content": "new durable fact"}, "add")
wm("r", {"action": "replace", "old_text": "fact one", "content": "fact ONE edited"}, "replace")
wm("bad", {"action": "replace", "old_text": "missing", "content": "x"}, "replace")
wm("b", {"action": "batch", "operations": [{"action": "add", "content": "batched fact"}, {"action": "remove", "old_text": "base"}]}, "batch", tgt="user")
load_mod("apply_pending_memory.py")
mem = open(os.path.join(TMP, "MEMORY.md")).read(); usr = open(os.path.join(TMP, "USER.md")).read()
assert "new durable fact" in mem and mem.count("new durable fact") == 1, "add/DRY failed"
assert "fact ONE edited" in mem, "replace failed"
assert "batched fact" in usr and "base" not in usr, "batch failed"
print("  OK add/DRY-skip/replace/batch all correct")

print("\n[4] review_pending_skills")
load_mod("review_pending_skills.py")
print("  OK review script executes")

shutil.rmtree(TMP, ignore_errors=True)
print(f"\nALL CHECKS PASSED — temp {TMP} cleaned")
