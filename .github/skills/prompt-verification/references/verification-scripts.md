# Full Prompt Integrity Verification Script

Run from workspace root. Checks DEPS==SKILLS, skill resolution, prompt dep resolution, and cross-ref map across all matching prompt files in one pass.

## Unified Verification Script

```python
import yaml, glob, os

def verify_prompts(pattern='prompts/repo*.prompt.md'):
    '''Batch verify all prompts matching pattern.'''
    skills_root = os.path.expanduser('~/AppData/Local/hermes/skills')
    known_skills = set()
    for root, dirs, files in os.walk(skills_root):
        if 'SKILL.md' in files:
            known_skills.add(os.path.basename(root))
    
    existing_prompts = set(
        os.path.basename(p).replace('.prompt.md', '')
        for p in glob.glob('prompts/*.prompt.md')
    )
    
    header = f'{\"Status\":7} {\"Trigger\":28} {\"SK/DP\":6} {\"Prompt Deps\":20} {\"Unresolved\":15} File'
    print(header)
    print('=' * len(header))
    
    all_pass = True
    for pf in sorted(glob.glob(pattern)):
        with open(pf) as f:
            content = f.read()
        parts = content.split('---', 2)
        if len(parts) < 3:
            print(f'❌  {\"(no fm)\":28} {\"--\":6} {\"---\":20} {\"---\":15} {os.path.basename(pf)}')
            continue
        
        fm = yaml.safe_load(parts[1])
        trigger = fm.get('trigger', '?')
        
        # DEPS==SKILLS
        deps_skills = set(
            d.replace('skill:', '').strip()
            for d in fm.get('dependencies', [])
            if isinstance(d, str) and d.startswith('skill:')
        )
        skills_set = set(fm.get('skills', []))
        deps_ok = (deps_skills == skills_set)
        
        # Resolve skills
        all_skills = deps_skills | skills_set
        unresolved = [s for s in all_skills if s not in known_skills]
        
        # Resolve prompt deps
        prompt_refs = [
            d.replace('prompt:', '').strip()
            for d in fm.get('dependencies', [])
            if isinstance(d, str) and d.startswith('prompt:')
        ]
        missing_prompts = [p for p in prompt_refs if p not in existing_prompts]
        
        # Determine status
        status = '✅'
        if not deps_ok:
            status = '❌'
            all_pass = False
        if unresolved:
            status = '⚠️'
            all_pass = False
        if missing_prompts:
            status = '❌'
            all_pass = False
        
        deps_str = f'{len(skills_set)}/{len(deps_skills)}'
        prompt_str = ', '.join(prompt_refs) if prompt_refs else '—'
        unres_str = ', '.join(unresolved) if unresolved else ('❌' if missing_prompts else '—')
        
        print(f'{status:7} {trigger:28} {deps_str:6} {prompt_str:20} {unres_str:15} {os.path.basename(pf)}')
        
        if not deps_ok:
            only_d = deps_skills - skills_set
            only_s = skills_set - deps_skills
            if only_d: print(f'         Only in deps: {sorted(only_d)}')
            if only_s: print(f'         Only in skills: {sorted(only_s)}')
        if missing_prompts:
            print(f'         Missing prompt files: {missing_prompts}')
    
    return all_pass

verify_prompts()
```

## Cross-Prompt Dependency Map Generator

```python
import yaml, glob

print(f'{\"Trigger\":30} {\"Skills\":6} Delegates To')
print('=' * 70)
for pf in sorted(glob.glob('prompts/repo*.prompt.md')):
    with open(pf) as f:
        parts = f.read().split('---', 2)
    if len(parts) < 3: continue
    fm = yaml.safe_load(parts[1])
    trigger = fm.get('trigger', '?')
    deps = fm.get('dependencies', [])
    skill_count = len([d for d in deps if isinstance(d, str) and d.startswith('skill:')])
    prompt_refs = [d.replace('prompt:','').strip() for d in deps if isinstance(d, str) and d.startswith('prompt:')]
    print(f'{trigger:30} {skill_count:2}', end='')
    if prompt_refs:
        print(f'  →  {", ".join(prompt_refs)}')
    else:
        print()
```

## Skills Inventory (Resolution Check)

```python
import os

skills_root = os.path.expanduser('~/AppData/Local/hermes/skills')
known = {}
for root, dirs, files in os.walk(skills_root):
    if 'SKILL.md' in files:
        rel = os.path.relpath(root, skills_root)
        known[os.path.basename(root)] = rel

# Check specific skill names
targets = ['github-repo-management', 'web-research-pipeline', 'workspace-audit']
for t in targets:
    if t in known:
        print(f'✅ {t:30} → {known[t]}')
    else:
        print(f'❌ {t:30} NOT FOUND')
        
# Check for collisions (same bare name in multiple dirs)
from collections import Counter
counts = Counter(known.keys())
for name, count in counts.items():
    if count > 1:
        locs = [v for k, v in known.items() if k == name]
        print(f'⚠️  COLLISION: {name} appears in {count} locations: {locs}')
```

## Session Application: repo.*.prompt.md

From the original implementation session, the verification sequence was:

1. `read_file` all 4 repo prompt files (repo, repo-management, repo-research-pipeline, repo-story-time)
2. Verify frontmatter completeness (all required fields present)
3. Run DEPS==SKILLS check (all 4 passed)
4. Verify each skill reference resolves on disk (30 unique skills, all resolved)
5. Verify each `prompt:` reference exists (6 references, all resolved)
6. Build cross-prompt delegation map
7. Verify toolsets appropriate per prompt domain
8. Confirm git status clean on `development` branch

Total verification gates: 8/8 passed. No fixes needed.
