---
name: audit-227
title: Audit 227
description: Node.js script that walks the prompts directory and Hermes install path to count prompt and memory files
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - javascript
  - audit
  - prompts
  - memories
  - node
---

# Audit 227

## Overview

Wrapper skill for the `audit-227.js` script in `~/AppData/Local/hermes/scripts/`. This Node.js script walks the SandBox `prompts/` directory and the Hermes install directory to count prompt files (`.prompt.md`) and memory/profile files (`USER.md`, `SOUL.md`, `MEMORY.md`, and files under `profiles/` or `memories/`).

## Script Reference

**Location:** `~/AppData/Local/hermes/scripts/audit-227.js`

**Extension:** `node`

**Usage:**
```bash
node audit-227.js
```

## When to Use

- To get a quick count of prompt files and memory/profile files
- Before running `validate-prompt-inventory` to understand scope
- To check if prompts or memories have been properly installed

## When NOT to Use

- For detailed frontmatter validation — use `validate-prompts`
- For session auditing — use `session-audit-227`
- For skill auditing — use `skills-audit`

## Workflow

### Phase 1: Execute
```bash
node $LOCALAPPDATA/hermes/scripts/audit-227.js
```

### Phase 2: Review
Output shows:
- `PROMPT_COUNT` — number of `.prompt.md` files in SandBox prompts/
- `MEMORY_COUNT` — number of markdown files under profiles/, memories/, USER.md, SOUL.md, MEMORY.md
- `COMBINED_COUNT` — sum of both
- A sample listing (first 8 of each)


### Phase 3: Phase 3

Document results, record any issues found, and verify output matches expected format.


### Phase 4: Final Review

Confirm all changes complete and produce summary report.

## Verification Checklist

- [ ] Script runs without Node.js errors
- [ ] PROMPT_COUNT matches `ls ~/Desktop/SandBox/prompts/*.prompt.md | wc -l`
- [ ] MEMORY_COUNT is reasonable (>0 if profiles/alexa exists)
- [ ] Sample paths look correct
- [ ] No .git directories are traversed

## Skills Required

| Skill | Purpose |
|-------|--------|
| `script-execution` | Run the script with appropriate runtime |
| `file-operations` | Read and write target files |
| `validation` | Verify output is correct |

## Pitfalls
- The script uses `require('fs')` and `require('path')` — Node.js built-ins only
- Root prompt path is hardcoded to `C:/Users/Alexa/Desktop/SandBox/prompts`
- Hermes root path uses `USERPROFILE` env var with fallback to `C:\Users\Alexa`
- Only the first 8 entries of each list are printed (sample)