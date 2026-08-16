# ESM Interop + Build Repair Case Study

Session: 2026-07-31 — awesome-copilot plugin mirror build repair (hermes-profiles/plugins/awesome-copilot).

## Problem

`npm run build` failed immediately:

```
Error [ERR_MODULE_NOT_FOUND]: Cannot find package 'js-yaml' imported from ...eng/yaml-parser.mjs
```

Two distinct causes stacked:

1. **Deps never installed** in the mirror tree (no `node_modules`) → `npm ci` fixed (8 packages, 10s).
2. **ESM default-export incompatibility**: after install, still failing:

```
SyntaxError: The requested module 'js-yaml' does not provide an export named 'default'
```

## Root cause

js-yaml 5.2.0 installed as ESM-only — 63 named exports (`load`, `dump`, `JSON_SCHEMA`, ...) but NO default export. The script did `import yaml from "js-yaml"` which requires a default export.

Diagnosis command (confirm export shape before touching code):

```bash
node -e "import('js-yaml').then(m=>{console.log('load:', typeof m.load, '| JSON_SCHEMA:', typeof m.JSON_SCHEMA); console.log('has default:', 'default' in m)})"
```

## Fix

```diff
- import yaml from "js-yaml";
+ import * as yaml from "js-yaml";
```

Namespace import preserves all call sites (`yaml.load(...)`, `yaml.JSON_SCHEMA`). Check for other occurrences first:

```bash
grep -rn 'js-yaml' eng/ *.mjs | grep -v node_modules
```

## Verification

- `npm run build` → `✓ Successfully generated marketplace.json with 96 plugins (67 local, 29 external)` — exit 0.
- Mirror tree is gitignored (`hermes-profiles/` line 70 of .gitignore, 0 tracked files) → regenerated README/marketplace.json and `node_modules` stay local, no repo pollution.

## Patch-tool incident (agent-side lesson)

First repair attempt FAILED SILENTLY: the `patch` call had `old_string`/`new_string` swapped — it reported `files_modified` with no diff, and the file on disk was unchanged (build still failed). The error was caught only by re-reading the file:

```
1|import fs from "fs";
2|import * as yaml from "js-yaml";   # already namespace? NO — this was the DISPLAYED old content
```

**Lesson**: after any `patch` that reports success, verify the diff or re-read the file before proceeding. A "successful" patch with no diff = wrong argument order, not a no-op.
