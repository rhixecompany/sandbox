import asyncio
import os
import re
import shutil
import sys

ROOT = os.path.join(os.environ["LOCALAPPDATA"], "hermes", "skills")
BACKUP = ROOT + "_BACKUP_2026-07-10"
PATH_PAT = re.compile(
    r"C:/Users/Alexa/AppData/Local/hermes|C:\\Users\\Alexa\\AppData\\Local\\hermes|~/AppData/Local/hermes|\$HOME/AppData/Local/hermes"
)
FENCE = re.compile(r"^```(\w*)")


# Per-language substitution. Returns None if no change.
def sub_for(lang, text):
    lt = lang.lower()
    if lt in ("bash", "sh", "shell", "zsh", "console", "cmd", ""):
        return PATH_PAT.sub("$LOCALAPPDATA/hermes", text)
    if lt in ("python", "py"):
        # Capture the trailing sub-path after the hermes root (e.g. /skills, /state.db)
        # and rebuild as a valid expression: os.environ.get("LOCALAPPDATA", ...) + "/hermes<suffix>"
        pat = re.compile(
            r"""["'](?:C:/Users/Alexa/AppData/Local/hermes|C:\\[Uu]sers\\[Uu]lexa\\[Uu]ppData\\[Ll]ocal\\[Hh]ermes|~/AppData/Local/hermes|\$HOME/AppData/Local/hermes)([^"']*)["']"""
        )

        def _py(m):
            suffix = m.group(1).replace("\\", "/")
            return 'os.environ.get("LOCALAPPDATA", os.path.expanduser("~/AppData/Local")) + "/hermes' + suffix + '"'

        return pat.sub(_py, text)
    if lt in ("powershell", "pwsh"):
        return PATH_PAT.sub(lambda m: "$env:LOCALAPPDATA" + os.sep + "hermes", text)
    return None  # markdown, yaml, others -> skip


def transform_sync(path, dry, report):
    lines = open(path, encoding="utf-8").read().splitlines()
    out = []
    in_block = False
    lang = ""
    changed = 0
    for ln in lines:
        m = FENCE.match(ln.strip())
        if m:
            if not in_block:
                in_block = True
                lang = m.group(1)
                out.append(ln)
                continue
            else:
                in_block = False
                lang = ""
                out.append(ln)
                continue
        if in_block:
            new = sub_for(lang, ln)
            if new is not None and new != ln:
                changed += 1
                out.append(new)
            else:
                out.append(ln)
        else:
            out.append(ln)
    if changed > 0:
        report.append((path, changed, lang))
        if not dry:
            open(path, "w", encoding="utf-8").write("\n".join(out) + ("\n" if lines and lines[-1] == "" else ""))
    return changed


async def main():
    dry = "--apply" not in sys.argv
    loop = asyncio.get_running_loop()
    files = [
        f
        for f in (os.path.join(d, n) for d, _, fs in os.walk(ROOT) for n in fs)
        if f.endswith(".md") and "_BACKUP_" not in f
    ]
    if dry:
        print("DRY-RUN (no writes)\n")
    else:
        if not os.path.isdir(BACKUP):
            await loop.run_in_executor(None, shutil.copytree, ROOT, BACKUP)
            print(f"BACKUP created: {BACKUP}\n")
        else:
            print(f"BACKUP exists: {BACKUP}\n")
    report = []
    total = 0
    for f in files:
        c = await loop.run_in_executor(None, transform_sync, f, dry, report)
        total += c
    print(f"Files touched: {len(report)}  |  Total in-code lines changed: {total}")
    if dry:
        for p, c, lg in sorted(report, key=lambda x: -x[1])[:40]:
            print(f"  {c:3d} [{lg or 'bash'}] {os.path.relpath(p, ROOT)}")
        if len(report) > 40:
            print(f"  ... +{len(report) - 40} more files")
    print("\nDRY-RUN complete." if dry else "\nAPPLY complete. Re-scan to verify, then delete backup.")


if __name__ == "__main__":
    asyncio.run(main())
