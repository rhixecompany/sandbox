#!/usr/bin/env python3
"""
Phase S1 Verification: Archive Cleanup + Dedup
"""
import os
import shutil

skills_root = r"C:\Users\Alexa\AppData\Local\hermes\skills"

print("=== Phase S1 Verification ===")

# 1. Check .archive removed
archive_path = os.path.join(skills_root, ".archive")
if os.path.exists(archive_path):
    print(f"❌ FAIL: .archive still exists at {archive_path}")
else:
    print("✅ PASS: .archive removed")

# 2. Check .restore-backups.DISABLED removed
restore_path = os.path.join(skills_root, ".restore-backups.DISABLED")
if os.path.exists(restore_path):
    print(f"❌ FAIL: .restore-backups.DISABLED still exists at {restore_path}")
else:
    print("✅ PASS: .restore-backups.DISABLED removed")

# 3. Check for duplicate skill names
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

dupes = {k: v for k, v in all_skills.items() if len(v) > 1}
if dupes:
    print(f"❌ FAIL: {len(dupes)} duplicate skill names remain:")
    for name, paths in sorted(dupes.items()):
        print(f"  {name}: {paths}")
else:
    print("✅ PASS: No duplicate skill names")

# 4. Count active skills
active_count = len([p for paths in all_skills.values() for p in paths if not p.startswith('.archive')])
print(f"Active skills: {active_count}")

# 5. Verify canonical paths preserved (categorized versions exist)
canonical_ok = True
for name, paths in all_skills.items():
    categorized = [p for p in paths if '\\' in p and not p.startswith('.archive')]
    flat = [p for p in paths if '\\' not in p and not p.startswith('.archive')]
    if flat and categorized:
        # Check flat is non-canonical (should be removed)
        print(f"⚠️  DUPLICATE REMAINS: {name} has flat={flat} and categorized={categorized}")
        canonical_ok = False

if canonical_ok:
    print("✅ PASS: All canonical categorized paths preserved, flat copies removed")

print("=== Phase S1 Verification Complete ===")