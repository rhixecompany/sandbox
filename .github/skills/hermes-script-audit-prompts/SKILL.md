---
name: hermes-script-audit-prompts
title: Prompt Library Verification
description: "Verify prompts (no mutation); separate from fixers."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [hermes, scripts, devops, prompts, verification, audit]
metadata:
  hermes:
    tags: [hermes, scripts, devops, prompts, verification]
    related_skills: [prompt-library-maintenance, prompt-library-consolidation]
    script_path: "C:\\Users\\Alexa\\AppData\\Local\\hermes\\scripts\\verify_canonical.py"
---

# Prompt Library Verification Skill

## Overview

Independent verification of the prompt library (no mutation). Separate code path from the fixer so a fixer's self-report can never be trusted as proof of validity. Run after every batch fix.

## When to Use

- After running `fix_canonical.py --apply` to verify repairs
- CI gate for prompt quality
- Before committing prompt library changes
- Auditing prompt library health

## Script Interface

**Path:** `$LOCALAPPDATA/hermes/scripts/verify_canonical.py`

```bash
# Full verification
MSYS_NO_PATHCONV=1 python3 verify_canonical.py
```

## Checks Performed

1. No CRLF line endings
2. Valid YAML frontmatter exists
3. No duplicate `metadata:` keys
4. All 8 universal required fields present + non-empty
5. All 5 local required fields present
6. `name` == filename slug
7. `trigger` == `/slug`
8. Skill deps == skills list (DEPS==SKILLS)
9. No MCP entries in skills list
10. Toolsets valid (in HERMES_TOOLSETS)
11. tool:mcp- dep → mcp toolset present
12. All skills resolve to known skills
13. No "Legacy Prompt Details" section

## Skills Required

| Skill | Purpose |
|---|---|
| `prompt-library-maintenance` | Batch frontmatter validation + toolset normalization |
| `prompt-library-consolidation` | Canonicalize prompt/template libraries |

## Workflow

### Phase 1: Load
1. Find all `.prompt.md` in `.github/prompts/`
2. Load known skills from hermes skills dir

### Phase 2: Verify (per file)
1. Parse frontmatter + body (separate code path from fixer)
2. Run all 13 checks
3. Collect issue codes

### Phase 3: Report
1. Print TOTAL=CLEAN=WITH_ISSUES
2. Print ISSUE TYPE COUNTS
3. Per-file issue list

## Verification Checklist

- [ ] Separate code path from fixer (no shared functions)
- [ ] All 13 checks execute
- [ ] Exit code 0 always (reporting tool)
- [ ] Issue codes stable for automation

## Pitfalls

- **MSYS paths**: Use `MSYS_NO_PATHCONV=1` prefix from git-bash
- **Not a fixer**: Does not modify files — verification only
- **Run after every fix**: `fix_canonical.py --apply` → `verify_canonical.py`