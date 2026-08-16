---
name: hermes-script-fix-prompt-library
title: Prompt Library Frontmatter Repair
description: "Fixes prompt frontmatter; parses YAML, preserves body."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [hermes, scripts, devops, prompts, frontmatter, repair]
metadata:
  hermes:
    tags: [hermes, scripts, devops, prompts, frontmatter]
    related_skills: [prompt-library-maintenance, writing-skills]
    script_path: "C:\\Users\\Alexa\\AppData\\Local\\hermes\\scripts\\fix_canonical.py"
---

# Prompt Library Frontmatter Repair Skill

## Overview

Deterministic prompt frontmatter repair for `.github/prompts/*.prompt.md`. Parses ONLY the YAML frontmatter (yaml.safe_load), preserves the body byte-for-byte, and rewrites frontmatter from the edited dict. Safe: default audit (no writes); pass `--apply` to mutate.

## When to Use

- After bulk prompt edits that may have broken frontmatter
- Before committing prompt library changes
- CI gate for prompt quality
- Fixing "MISSING:name" / "TRIGGER≠/slug" verification failures

## Script Interface

**Path:** `$LOCALAPPDATA/hermes/scripts/fix_canonical.py`

```bash
# Audit all prompts (default, no writes)
MSYS_NO_PATHCONV=1 python3 fix_canonical.py --all

# Audit specific files
MSYS_NO_PATHCONV=1 python3 fix_canonical.py --files fix_prompt_library.py,another.prompt.md

# Apply fixes (mutates files)
MSYS_NO_PATHCONV=1 python3 fix_canonical.py --all --apply

# Write JSON report
MSYS_NO_PATHCONV=1 python3 fix_canonical.py --all --apply --report fixes.json
```

## Rules Enforced

1. **Universal required**: name, title, description, version, author, license, tags, trigger
2. **Local required**: scripts, skills, formatter, plan, toolsets
3. **Trigger normalization**: `trigger: /<slug>` (must match filename)
4. **Dependency classification**: skill:/tool:/prompt: with MCP→tool: remapping
5. **Skill list sync**: DEPS skill: == skills list (DEPS==SKILLS invariant)
6. **MCP removal**: mcp-* entries removed from skills list
7. **Toolset normalization**: VS Code map → Hermes toolsets; mcp added if tool:mcp- dep present
8. **Legacy section strip**: "## Legacy Prompt Details" removed

## Skills Required

| Skill | Purpose |
|---|---|
| `prompt-library-maintenance` | Batch frontmatter validation + toolset normalization |
| `writing-skills` | Create clear skill prose and structure |

## Workflow

### Phase 1: Parse
1. Load all `.prompt.md` from `.github/prompts/`
2. Extract YAML frontmatter via regex + yaml.safe_load
3. Preserve body exactly

### Phase 2: Repair (per file)
1. Ensure all universal/local required fields exist
2. Normalize trigger to `/slug`
3. Classify dependencies (skill:/tool:/prompt:)
4. Sync skills list with skill: deps
5. Normalize toolsets via VS Code map
6. Strip Legacy Prompt Details section

### Phase 3: Output
1. If `--apply`, write new frontmatter + preserved body
2. Print MODE=TOTAL=CHANGED summary
3. Per-file action list if changed

## Verification Checklist

- [ ] Body preserved byte-for-byte (no reformatting)
- [ ] `--all` processes every `.prompt.md`
- [ ] `--apply` only writes when actions non-empty
- [ ] JSON report valid if `--report` given
- [ ] Exit code 0 on success

## Pitfalls

- **MSYS paths**: Use `MSYS_NO_PATHCONV=1` prefix from git-bash
- **YAML dump width**: Uses width=4096 to prevent line wrapping
- **Sort keys false**: Preserves field order (name→trigger→...)
- **Default mode is AUDIT**: No files modified without `--apply`