import json
from collections import defaultdict

with open('C:/Users/Alexa/AppData/Local/Temp/skill_files.txt') as f:
    skill_files = [line.strip() for line in f if line.strip()]

skills_by_name = defaultdict(list)
root_level = []
archived = []

prefixes = [
    r'C:\Users\Alexa\AppData\Local\hermes\skills\\',
    '/c/Users/Alexa/AppData/Local/hermes/skills/',
    'C:/Users/Alexa/AppData/Local/hermes/skills/',
]

for path in skill_files:
    relative = path
    for prefix in prefixes:
        if path.startswith(prefix):
            relative = path[len(prefix):]
            break
    
    parts = relative.replace('/', '\\').split('\\')
    
    # Skip archived
    if parts[0] == '.archive':
        archived.append({'name': parts[-1], 'path': path})
        continue
    
    if len(parts) == 1:
        # Shouldn't happen since all skills are in category/name/SKILL.md
        root_level.append({'name': parts[0], 'path': path})
    elif len(parts) == 2:
        # category/SKILL.md - this is a root-level skill without a name dir
        category = parts[0]
        skills_by_name[f"{category}/SKILL.md"].append({'category': category, 'path': path, 'root_level': True})
    elif len(parts) >= 3:
        # category/name/SKILL.md
        category = parts[0]
        name = parts[1]  # The skill name is the directory name
        skills_by_name[name].append({'category': category, 'path': path})

duplicates = {name: locs for name, locs in skills_by_name.items() if len(locs) > 1}

print(f'Total skill files: {len(skill_files)}')
print(f'Archived: {len(archived)}')
print(f'Root-level (no name dir): {len(root_level)}')
print(f'Unique names: {len(skills_by_name)}')
print(f'Duplicate names: {len(duplicates)}')
print(f'\n=== DUPLICATE SKILLS (first 30) ===')
for name, locs in list(duplicates.items())[:30]:
    cats = [l['category'] for l in locs]
    print(f'  {name}: {cats}')
print(f'\n=== ROOT-LEVEL SKILLS (first 30) ===')
for s in root_level[:30]:
    print(f'  {s["name"]}')
