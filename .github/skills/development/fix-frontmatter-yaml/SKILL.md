---
name: fix-frontmatter-yaml
title: Fix Frontmatter YAML
description: Node.js CJS script that repairs unclosed frontmatter fences in specific prompt files by inserting missing closing '---' delimiters
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - javascript
  - node
  - frontmatter
  - fix
  - cjs
---

# Fix Frontmatter YAML

## Overview

Wrapper skill for the `fix-frontmatter-yaml.cjs` script in `~/AppData/Local/hermes/scripts/`. This Node.js CommonJS script scans 9 specific prompt files, detects unclosed YAML frontmatter (a `---` opening without a matching `---` closing), and inserts the missing closing fence before the first content line (starting with `#`, `- `, or `> `).

## Script Reference

**Location:** `~/AppData/Local/hermes/scripts/fix-frontmatter-yaml.cjs`

**Extension:** `node`

**Usage:**
```bash
cd ~/Desktop/SandBox
node $LOCALAPPDATA/hermes/scripts/fix-frontmatter-yaml.cjs
```

**Output:** `docs/frontmatter-yaml-repair-report.json`

## When to Use

- After detecting unclosed frontmatter in prompt files via `verify-frontmatter` or `prompt-audit-all`
- When prompt files show `missing-frontmatter-end` issues
- Before running `validate-prompts` to ensure all frontmatter is parseable

## When NOT to Use

- For batch repair across all prompts — use `fix-prompts` or `fix-prompts-comprehensive` instead
- When you need to verify frontmatter without modifying files

## Workflow

### Phase 1: Setup
```bash
cd ~/Desktop/SandBox
node $LOCALAPPDATA/hermes/scripts/fix-frontmatter-yaml.cjs
```

### Phase 2: Review
The script outputs a JSON report to stdout and writes it to `docs/frontmatter-yaml-repair-report.json`. The report has three arrays: `patched`, `skipped`, `errors`.

### Phase 3: Verify
Run `verify-frontmatter` or `validate-prompts` to confirm fixes.


### Phase 4: Documentation & Handoff

Document results, record any issues found, and verify output matches expected format.


### Phase 5: Final Review

Confirm all changes complete and produce summary report.

## Verification Checklist

- [ ] Script runs without Node.js errors
- [ ] `docs/frontmatter-yaml-repair-report.json` is created
- [ ] Patched files are listed in the `patched` array
- [ ] Skipped files (already correct) are listed
- [ ] No files appear in the `errors` array
- [ ] After patching, each file's frontmatter is valid YAML

## Skills Required

| Skill | Purpose |
|-------|--------|
| `script-execution` | Run the script with appropriate runtime |
| `file-operations` | Read and write target files |
| `validation` | Verify output is correct |

## Pitfalls
- Only targets 9 specific files listed in the `targets` array
- The repair logic finds the first non-frontmatter line (starting with `#`, `- `, or `> `) and inserts `---` before it
- If a file has no such line, the `---` is appended at the end — which may not be correct
- Always verify the patched output before committing changes
- The script modifies files in-place