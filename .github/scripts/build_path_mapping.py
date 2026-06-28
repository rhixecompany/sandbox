#!/usr/bin/env python3
"""Rebuild skill_name_to_path.json from actual disk state."""
import os, json, re, yaml
from pathlib import Path

base = Path(r"C:\Users\Alexa\AppData\Local\hermes\skills")
mapping = {}
for p in base.rglob("SKILL.md"):
    try:
        text = p.read_text(encoding="utf-8", errors="ignore")
        fm = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
        name = ""
        if fm:
            parsed = yaml.safe_load(fm.group(1))
            if parsed and "name" in parsed:
                name = parsed["name"]
        rel = p.relative_to(base)
        parts = str(rel.parent).split(os.sep)
        category = parts[0] if len(parts) > 1 else ""
        if not name:
            name = parts[-1] if len(parts) > 1 else parts[0]
        mapping[name] = {
            "category": category if category != name else "",
            "path": str(p.resolve()).replace("/", "\\"),
        }
    except Exception as e:
        print(f"SKIP {p}: {e}")

print(f"Total skills mapped: {len(mapping)}")
json.dump(mapping, open(base.parent / "scripts" / "skill_name_to_path.json", "w"), indent=2)

cats = {}
for v in mapping.values():
    c = v["category"] if v["category"] else "uncategorized"
    cats[c] = cats.get(c, 0) + 1
for c, n in sorted(cats.items(), key=lambda x: -x[1]):
    print(f"  {c}: {n}")
