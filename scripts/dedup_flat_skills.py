#!/usr/bin/env python3
"""
Phase S1: Remove flat duplicate skills, keeping only categorized canonical versions.
Run AFTER archive removal.
"""
import os
import shutil

skills_root = r"C:\Users\Alexa\AppData\Local\hermes\skills"

print("=== Phase S1: Dedup Flat Skills ===")

# Build skill name -> paths map
all_skills = {}
for root, dirs, files in os.walk(skills_root):
    if 'SKILL.md' in files:
        rel = os.path.relpath(root, skills_root)
        if rel == '.': continue
        try:
            with open(os.path.join(root, 'SKILL.md'), 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    import yaml
                    fm = yaml.safe_load(parts[1])
                    name = fm.get('name', rel)
                else:
                    name = rel
            else:
                name = rel
        except:
            name = rel
        if name not in all_skills:
            all_skills[name] = []
        all_skills[name].append(rel)

# Find duplicates with flat + categorized
removed = []
kept = []
for name, paths in all_skills.items():
    categorized = [p for p in paths if '\\' in p and not p.startswith('.archive')]
    flat = [p for p in paths if '\\' not in p and not p.startswith('.archive')]
    
    if flat and categorized:
        # Keep the first categorized version, remove flat copies
        for f in flat:
            flat_path = os.path.join(skills_root, f)
            if os.path.exists(flat_path):
                try:
                    shutil.rmtree(flat_path)
                    removed.append(f)
                    print(f"  REMOVED flat: {f} (kept categorized: {categorized[0]})")
                except Exception as e:
                    print(f"  ERROR removing {f}: {e}")
        kept.append(categorized[0])
    elif categorized and not flat:
        kept.append(categorized[0])

print(f"\nRemoved {len(removed)} flat duplicate skill directories")
print(f"Kept {len(kept)} canonical categorized skills")

# Verify
print("\n=== Post-Dedup Verification ===")
all_skills2 = {}
for root, dirs, files in os.walk(skills_root):
    if 'SKILL.md' in files:
        rel = os.path.relpath(root, skills_root)
        if rel == '.': continue
        try:
            with open(os.path.join(root, 'SKILL.md'), 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    import yaml
                    fm = yaml.safe_load(parts[1])
                    name = fm.get('name', rel)
                else:
                    name = rel
            else:
                name = rel
        except:
            name = rel
        if name not in all_skills2:
            all_skills2[name] = []
        all_skills2[name].append(rel)

dupes2 = {k: v for k, v in all_skills2.items() if len(v) > 1}
if dupes2:
    print(f"⚠️  Remaining duplicates: {len(dupes2)}")
    for name, paths in sorted(dupes2.items()):
        print(f"  {name}: {paths}")
else:
    print("✅ No duplicate skill names")

active_count = sum(len(v) for v in all_skills2.values())
print(f"Active skills after dedup: {active_count}")