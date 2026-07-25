---
name: verify-frontmatter
title: Verify Frontmatter
description: Node.js CJS script that analyzes YAML frontmatter fences in 9 specific prompt files for unclosed fences and double fence issues
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - javascript
  - node
  - validation
  - frontmatter
  - cjs
---

# Verify Frontmatter

## Overview

Wrapper skill for the `verify-frontmatter.cjs` script in `~/AppData/Local/hermes/scripts/`. This Node.js script checks 9 specific prompt files for YAML frontmatter fence issues: unclosed fences (opening `---` without closing) and double fences (more than one `---` marker per section). Results are printed to stdout and saved to `docs/frontmatter-gate-report.json`.

## Script Reference

**Location:** `~/AppData/Local/hermes/scripts/verify-frontmatter.cjs`

**Extension:** `node`

**Usage:**
```bash
cd ~/Desktop/SandBox
node $LOCALAPPDATA/hermes/scripts/verify-frontmatter.cjs
```

**Output:** `docs/frontmatter-gate-report.json`

## When to Use

- As a frontmatter "gate check" before running fix scripts
- To detect double frontmatter fences (common copy-paste error)
- To verify that `fix-frontmatter-yaml` successfully repaired files
- As a pre-commit check for prompt file quality

## When NOT to Use

- For bulk frontmatter scanning across all prompts — use `prompt-audit-all`
- For detailed field-level validation — use `validate-prompts`

## Workflow

### Phase 1: Execute
```bash
cd ~/Desktop/SandBox
node $LOCALAPPDATA/hermes/scripts/verify-frontmatter.cjs
```

### Phase 2: Review
Output shows JSON with file status and detected issues. Files that don't exist show `exists: false`.

### Phase 3: Fix issues
- `unclosed frontmatter` — run `fix-frontmatter-yaml`
- `double fences` — manually remove the extra opening `---` section


### Phase 4: Documentation & Handoff

Document results, record any issues found, and verify output matches expected format.


### Phase 5: Final Review

Confirm all changes complete and produce summary report.

## Verification Checklist

- [ ] Script runs without errors
- [ ] `docs/frontmatter-gate-report.json` is generated
- [ ] All 9 target files are checked
- [ ] Missing files show `exists: false`
- [ ] Issues are clearly reported per file
- [ ] Output JSON is valid and parseable

## Skills Required

| Skill | Purpose |
|-------|--------|
| `script-execution` | Run the script with appropriate runtime |
| `file-operations` | Read and write target files |
| `validation` | Verify output is correct |

## Pitfalls
- Only checks 9 specific files listed in the targets array
- Analyzes only the first 60 characters of the file for opening fence count — long leading content may confuse detection
- Multiple `---` lines in content (not frontmatter) may be falsely flagged as double fences
- `hasDoubleFence` is true when `openCount > 2 && !unclosed` — this may not catch all double fence variations
- The script is read-only — it never modifies files