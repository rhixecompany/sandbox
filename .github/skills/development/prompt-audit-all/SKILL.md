---
name: prompt-audit-all
title: Prompt Audit All
description: Node.js CJS script that audits all .prompt.md files for frontmatter issues (missing start/end, empty frontmatter, JSON frontmatter, null bytes)
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - javascript
  - node
  - audit
  - prompts
  - frontmatter
---

# Prompt Audit All

## Overview

Wrapper skill for the `prompt-audit-all.cjs` script in `~/AppData/Local/hermes/scripts/`. This Node.js script scans all `.prompt.md` files in the `prompts/` directory and checks for common frontmatter issues: missing opening `---`, missing closing `---`, empty frontmatter, JSON-like frontmatter, null bytes in content, and non-standard file extensions.

## Script Reference

**Location:** `~/AppData/Local/hermes/scripts/prompt-audit-all.cjs`

**Extension:** `node`

**Usage:**
```bash
node prompt-audit-all.cjs
```

**Target directory:** `~/Desktop/SandBox/prompts`

## When to Use

- For bulk frontmatter issue detection across all prompts
- Before running `fix-frontmatter-yaml` or other repair scripts
- As a pre-validation step to identify which files need fixing
- To detect corrupted files (null bytes) or misnamed files (`.prompt.txt`)

## When NOT to Use

- For detailed frontmatter field validation — use `validate-prompts`
- For individual file analysis — use `verify-frontmatter`

## Workflow

### Phase 1: Execute
```bash
cd ~/Desktop/SandBox
node $LOCALAPPDATA/hermes/scripts/prompt-audit-all.cjs
```

### Phase 2: Review
Output shows `PROMPT_COUNT`, `ISSUE_COUNT`, and `ISSUE {file} :: {reason}` for each problematic file.

### Phase 3: Fix
Address each issue category:
- `missing-frontmatter-start` → add `---` at top
- `missing-frontmatter-end` → run `fix-frontmatter-yaml`
- `frontmatter-is-json` → convert to YAML
- `null-bytes` → re-save file cleanly
- `non-standard-extension` → rename to `.prompt.md`


### Phase 4: Documentation & Handoff

Document results, record any issues found, and verify output matches expected format.


### Phase 5: Final Review

Confirm all changes complete and produce summary report.

## Verification Checklist

- [ ] Script runs without Node.js errors
- [ ] PROMPT_COUNT matches expected file count
- [ ] ISSUE_COUNT is 0 (or all issues are expected)
- [ ] Each issue includes a file path and reason(s)
- [ ] Null byte detection flags genuinely corrupted files only

## Skills Required

| Skill | Purpose |
|-------|--------|
| `script-execution` | Run the script with appropriate runtime |
| `file-operations` | Read and write target files |
| `validation` | Verify output is correct |

## Pitfalls
- Only processes files directly in `prompts/` directory, not subdirectories
- `non-standard-extension` check hardcodes `pl.md` and `.prompt.txt` as known non-standard names
- Frontmatter-is-json detects if frontmatter starts with `{` or `[` — this may false-positive on YAML content that happens to start with those characters
- Null byte detection checks for `\ufffd` (replacement char) and `\u0000` (null char) — legitimate unicode may trigger false positives