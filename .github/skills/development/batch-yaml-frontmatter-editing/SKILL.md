---
name: batch-yaml-frontmatter-editing
title: Batch YAML Frontmatter Editing
description: 'Batch-remediate YAML frontmatter in SKILL.md files — add missing name/description fields, fix merged key corruption, normalize trailing newlines. For bulk skill library maintenance.'
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [yaml, frontmatter, batch, remediation, skills]
---

# Batch YAML Frontmatter Editing

## Goal
Safely add or repair `name:` and `description:` fields across many SKILL.md files without corrupting existing frontmatter.

## Workflow

### Phase 1: Discover
Find all target files: `find ... -name "SKILL.md"` or target a specific category.

### Phase 2: Parse
```python
import re
fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
if not fm_match:
    # No frontmatter — add minimal:
    text = f"---\nname: {name}\ndescription: \"{title}\"\n---\n\n{text.lstrip()}"
```

### Phase 3: Normalize (critical)
```python
fm = fm_match.group(1)
# fm does NOT include the trailing \n before ---
if not fm.endswith("\n"):
    fm += "\n"
```
Without this, appending `\ndescription: "Foo"` to `name: foo` produces `name: foodescription: "Foo"` (merged).

### Phase 4: Add missing fields
```python
if not re.search(r"^name:", fm, re.M):
    fm = f"name: {skill_name}\n" + fm
if not re.search(r"^description:", fm, re.M):
    title_m = re.search(r"^title:\s*[\"']?([^\"'\n]+)", fm, re.M)
    desc = title_m.group(1) if title_m else skill_name.replace("-"," ").title()
    fm = fm + f"description: \"{desc}\"\n"
text = f"---\n{fm}\n---\n{body}"
```

### Phase 5: Verify structurally (NOT by body content)
Check only: frontmatter opener, name:, description:. Do NOT penalize short descriptions or small body — those are content issues, not structural defects.

### Phase 6: Edge-Case Verify (ad-hoc script)
Before declaring done, create a focused temp script that tests common edge cases:

- Has-all-fields (no change needed)
- Missing name: (prepend)
- Missing description: (append)
- Missing both (prepend + append)
- No frontmatter (create from scratch)
- Title-derived description
- Empty frontmatter (`---\n---`)
- Complex existing frontmatter (author, license, metadata)
- Missing trailing newline in `fm` (the field-merge trap)

This catches YAML manipulation bugs before they hit the real skill library. Example pattern at `references/verify-script.md`.

## Pitfalls
- **Trailing newline trap**: Regex `(.*?)\n---` captures text BETWEEN `\n` after `---\n` and the `\n` before `---`. The captured fm never ends with `\n`. Always normalize before append.
- **Structural vs body scoring**: When verifying results, score only structural fields. Body-content scoring on a frontmatter audit produces 90%+ false failures.
- **Root-level duplicates**: Skills at both `skills/<name>/` and `skills/<category>/<name>/` are duplicates. Remove root-level copy when identical.
- **Prefer category location**: The categorized copy under a skill category directory is canonical. Root-level copies are legacy.

## Related Skills
- `batch-skills-audit` — full audit pipeline
- `validate-memories` — YAML corruption recovery reference
