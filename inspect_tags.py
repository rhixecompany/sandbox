#!/usr/bin/env python3
import glob
import os
import re
from collections import Counter

import yaml

PROMPTS_DIR = r"C:/Users/Alexa/AppData/Local/hermes/prompts"
files = sorted(glob.glob(os.path.join(PROMPTS_DIR, "*.prompt.md")))


def extract_frontmatter(text):
    if not text.startswith("---"):
        return None, text
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.DOTALL)
    if not m:
        return None, text
    return m.group(1), m.group(2)


tag_counter = Counter()
name_tokens = Counter()
for f in files:
    base = os.path.basename(f)
    name = base.replace(".prompt.md", "")
    with open(f, encoding="utf-8") as fh:
        text = fh.read()
    fm_text, body = extract_frontmatter(text)
    tags = []
    if fm_text is not None:
        try:
            fm = yaml.safe_load(fm_text) or {}
            tags = fm.get("tags") or []
            if not isinstance(tags, list):
                tags = [str(tags)]
        except Exception:
            pass
    for t in tags:
        tag_counter[t] += 1
    for tok in re.split(r"[-_]", name):
        if tok:
            name_tokens[tok] += 1

print("=== TOP TAGS ===")
for t, c in tag_counter.most_common(60):
    print(f"  {t}: {c}")
print("\n=== FILE STEMS ===")
for f in files:
    print("  " + os.path.basename(f).replace(".prompt.md", ""))
