import asyncio
import glob
import json
import os

HERMES_HOME = os.environ.get("LOCALAPPDATA", os.path.expanduser("~/AppData/Local")) + "/hermes"
MEM = os.path.join(HERMES_HOME, "memories", "MEMORY.md")
USR = os.path.join(HERMES_HOME, "memories", "USER.md")
PENDING = os.path.join(HERMES_HOME, "pending", "memory")


def load_sync(p):
    return open(p, encoding="utf-8").read() if os.path.isfile(p) else ""


def save_sync(p, t):
    open(p, "w", encoding="utf-8").write(t)


async def main():
    loop = asyncio.get_running_loop()
    results = {"applied": [], "skipped": [], "failed": []}
    m = await loop.run_in_executor(None, load_sync, MEM)
    u = await loop.run_in_executor(None, load_sync, USR)

    entries = []
    for f in sorted(glob.glob(os.path.join(PENDING, "*.json"))):
        if os.path.basename(f).startswith("_"):
            continue
        data = await loop.run_in_executor(None, _load_json, f)
        entries.append((data.get("created_at", 0), data["id"], data["action"], data.get("payload", {})))

    entries.sort(key=lambda x: x[0])

    def apply_to(text, op):
        """Return (new_text, status, msg) for a single op dict against text."""
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
            old = op.get("old_text", "")
            new = op.get("content", "")
            if old and old in text:
                return text.replace(old, new, 1), "applied", "replaced"
            if not old:  # replace with empty old = pure add
                if new and new not in text:
                    return text + "\n" + new, "applied", "added"
                return text, "skipped", "dup"
            return text, "failed", "old not found"
        return text, "skipped", f"unknown op {a}"

    for _ts, tid, act, p in entries:
        tgt = p.get("target", "memory")
        store = u if tgt == "user" else m
        try:
            if act in ("add", "replace"):
                new, st, msg = apply_to(store, p)
                if st == "applied":
                    if tgt == "user":
                        u = new
                    else:
                        m = new
                results[st].append((tid, tgt, act, msg))
            elif act == "batch":
                for op in p.get("operations", []):
                    new, st, msg = apply_to(store, op)
                    results[st].append((tid, tgt, f"batch/{op.get('action')}", msg))
                    if st == "applied":
                        store = new
                if tgt == "user":
                    u = store
                else:
                    m = store
            else:
                results["skipped"].append((tid, tgt, act, "unhandled"))
        except Exception as e:
            results["failed"].append((tid, tgt, act, f"EXC {e}"))

    await loop.run_in_executor(None, save_sync, MEM, m)
    await loop.run_in_executor(None, save_sync, USR, u)
    print(f"MEMORY.md: {len(m.encode())}B | USER.md: {len(u.encode())}B")
    print(f"APPLIED={len(results['applied'])} SKIPPED={len(results['skipped'])} FAILED={len(results['failed'])}")
    print("FAILED:", results["failed"][:10])
    print("SKIPPED sample:", results["skipped"][:8])


def _load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    asyncio.run(main())
