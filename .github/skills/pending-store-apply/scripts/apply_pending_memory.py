# apply_pending_memory.py — Phase 3: DRY-safe applier for pending/memory -> MEMORY.md/USER.md.
# 'add' skips if content already present (prevents ~7x bloat). 'replace'/'remove' skip if old_text
# absent. Writes back to live files. Adjust CONFIG per env.
import json, os, glob

# ===== CONFIG (edit per environment) =====
MEM = "C:/Users/Alexa/AppData/Local/hermes/memories/MEMORY.md"
USR = "C:/Users/Alexa/AppData/Local/hermes/memories/USER.md"
PENDING = "C:/Users/Alexa/AppData/Local/hermes/pending/memory"
# =========================================

def load(p): return open(p, encoding="utf-8").read() if os.path.isfile(p) else ""
def save(p, t): open(p, "w", encoding="utf-8").write(t)

results = {"applied": [], "skipped": [], "failed": []}
m = load(MEM); u = load(USR)
entries = []
for f in sorted(glob.glob(os.path.join(PENDING, "*.json"))):
    if os.path.basename(f).startswith("_"):
        continue
    data = json.load(open(f, encoding="utf-8"))
    entries.append((data.get("created_at", 0), data["id"], data["action"], data.get("payload", {})))
entries.sort(key=lambda x: x[0])

def apply_to(text, op):
    a = op.get("action")
    if a == "add":
        c = op.get("content", "")
        if c and c not in text:
            return text + "\n" + c, "applied", "added"
        return text, "skipped", "dup"
    if a == "remove":
        old = op.get("old_text", "")
        if old and old in text:
            return text.replace(old, ""), "applied", "removed"
        return text, "skipped", "not found"
    if a == "replace":
        old = op.get("old_text", ""); new = op.get("content", "")
        if old and old in text:
            return text.replace(old, new, 1), "applied", "replaced"
        if not old:
            if new and new not in text:
                return text + "\n" + new, "applied", "added"
            return text, "skipped", "dup"
        return text, "failed", "old not found"
    return text, "skipped", f"unknown op {a}"

for ts, tid, act, p in entries:
    tgt = p.get("target", "memory")
    store = u if tgt == "user" else m
    path = USR if tgt == "user" else MEM
    try:
        if act in ("add", "replace"):
            new, st, msg = apply_to(store, p)
            if st == "applied":
                if tgt == "user": u = new
                else: m = new
            results[st].append((tid, tgt, act, msg))
        elif act == "batch":
            for op in p.get("operations", []):
                new, st, msg = apply_to(store, op)
                results[st].append((tid, tgt, f"batch/{op.get('action')}", msg))
                if st == "applied":
                    store = new
            if tgt == "user": u = store
            else: m = store
        else:
            results["skipped"].append((tid, tgt, act, "unhandled"))
    except Exception as e:
        results["failed"].append((tid, tgt, act, f"EXC {e}"))

save(MEM, m); save(USR, u)
print(f"MEMORY.md: {len(m.encode())}B | USER.md: {len(u.encode())}B")
print(f"APPLIED={len(results['applied'])} SKIPPED={len(results['skipped'])} FAILED={len(results['failed'])}")
print("FAILED:", results["failed"][:10])
