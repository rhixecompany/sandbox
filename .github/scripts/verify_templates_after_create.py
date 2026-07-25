#!/usr/bin/env python3
"""Post-enhancement verification: confirms the 300 missing template files now
exist and the prompt library is still schema-clean. Read-only."""

import glob
import os
import re

import yaml

P = os.path.expanduser("~/AppData/Local/hermes/prompts")
ref_re = re.compile(r"templates/[A-Za-z0-9_./#-]+\.md", re.I)

# 1) dead template refs (link + prose)
total = dead = files = 0
fset = set()
for fp in sorted(glob.glob(os.path.join(P, "*.prompt.md"))):
    raw = open(fp, encoding="utf-8", errors="replace").read()
    idx = raw.find("\n---\n")
    body = raw[idx + 5 :] if idx >= 0 else raw
    fl = False
    for m in ref_re.finditer(body):
        total += 1
        pathpart = m.group(0).split("#")[0]
        cand = os.path.normpath(os.path.join(P, pathpart))
        if not os.path.exists(cand):
            dead += 1
            fl = True
    if fl:
        files += 1
        fset.add(os.path.basename(fp))

# 2) count created template files
tmpl_files = 0
for _root, _, fs in os.walk(os.path.join(P, "templates")):
    tmpl_files += sum(1 for f in fs if f.endswith(".md"))

# 3) schema re-verify (lightweight)
CLEAN = True
bad = 0
for fp in sorted(glob.glob(os.path.join(P, "*.prompt.md"))):
    raw = open(fp, encoding="utf-8", errors="replace").read()
    if not raw.startswith("---"):
        CLEAN = False
        bad += 1
        continue
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", raw, re.DOTALL)
    try:
        fm = yaml.safe_load(m.group(1)) if m else None
    except Exception:
        fm = None
    if not isinstance(fm, dict) or fm.get("name") != os.path.basename(fp).replace(".prompt.md", ""):
        CLEAN = False
        bad += 1

print(f"TEMPLATE REFS total={total} dead={dead} (was 301) files_affected={files}/211")
print(f"TEMPLATE FILES on disk now: {tmpl_files}")
print(f"PROMPT SCHEMA clean={CLEAN} bad={bad}/211")
print("DEAD_REFS_ZERO" if dead == 0 else "DEAD_REFS_REMAIN")
