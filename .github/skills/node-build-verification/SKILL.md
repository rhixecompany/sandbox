---
name: node-build-verification
title: Node Build Verification and Repair
description: Verify or repair Node.js/npm builds before claiming done.
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [node, npm, build, verification, esm, javascript, typescript]
metadata:
  hermes:
    tags: [node, npm, build, verification, esm, javascript, typescript]
---
# Node Build Verification and Repair

## Overview

Use when a Node.js/npm project (or a JS/TS tree inside a monorepo or mirror) needs its build verified before you claim completion: missing `node_modules`, failing `npm run build`, ESM import errors, or regenerated artifacts that need evidence.

## When to Use

- A JS/TS project build fails and you need root cause, not a workaround
- A freshly cloned/mirrored tree has no `node_modules` installed
- `npm run build` fails with `ERR_MODULE_NOT_FOUND` or `does not provide an export named 'default'`
- You edited a config/JSON file in a JS tree and must verify the project's own build still passes
- Regenerated artifacts (README, marketplace.json) need evidence of what the build changed

## Workflow

### Phase 1: Install dependencies (only if missing)

- Check first: `ls node_modules` (or `git check-ignore node_modules` to confirm it's local-only).
- Missing → `npm ci --no-audit --no-fund` (NOT `npm install` — ci is deterministic from the lockfile and fails loudly on drift).
- If there is no lockfile, `npm install` is acceptable; note it.

### Phase 2: Run the canonical build

- `npm run build` — do not invent a different command; the project's `package.json` scripts define it.
- Capture both the exit code and the tail of output. With a pipe (`... | tail`), read `${PIPESTATUS[0]}` for npm's real exit code — `$?` after a pipe reports tail's exit.

### Phase 3: Diagnose failures

- **Missing deps**: `ERR_MODULE_NOT_FOUND: Cannot find package 'x'` → Phase 1 was skipped or `node_modules` is stale; re-run `npm ci`.
- **ESM default-export error**: `The requested module 'x' does not provide an export named 'default'` → the installed package is ESM-only (named exports, no default). Fix the import site: `import * as x from "pkg"` instead of `import x from "pkg"`, preserving call sites (`x.load(...)`, `x.JSON_SCHEMA`). Verify the export shape first: `node -e "import('pkg').then(m=>console.log(typeof m.load, 'default' in m))"`.
- **JSON/trailing-comma errors in configs**: fix at the source and re-run the workspace's canonical config validator (e.g. `validate_vscode_json.py`) before the build.

### Phase 4: Re-run and confirm

- Re-run the build until `exit 0`.
- Capture the success tail (e.g. `✓ Successfully generated ...`) as evidence.
- Check what the build regenerated on disk and whether those outputs are gitignored (see Pitfalls).

## Pitfalls

- **PATCH TOOL NO-OP**: if you `patch` a file and it reports `files_modified` but the diff is absent or behavior doesn't change, you likely swapped `old_string`/`new_string`. Re-read the file and re-apply with correct arguments — do not assume the first patch landed.
- **Heredoc with `&`**: appending markdown via terminal heredoc/echo that contains `&` or `&&` (e.g. "Verify & Implement") trips the shell backgrounding guard (`Foreground command uses '&' backgrounding`). Use the `patch` tool or `write_file` for such appends.
- **Gitignored build outputs**: build scripts often regenerate README/marketplace/manifest files. Before worrying that a build "polluted" the repo, run `git check-ignore <path>` and `git status --short` on that subtree — mirror trees (e.g. `hermes-profiles/`) are frequently fully gitignored, so regenerated artifacts and `node_modules` stay local and never appear in git status.
- **Lifecycle-script failures on reinstall**: after a cleanup/monorepo sweep, `npm ci`/`bun install` can fail on postinstall scripts (phantomjs binary fetch, db:migrate hooks). Retry with `--ignore-scripts` (`npm ci --ignore-scripts --no-audit --no-fund`, `bun install --ignore-scripts`) — dev tooling installs fine without postinstall side effects.
- **Piped exit codes**: always use `${PIPESTATUS[0]}` (bash) when checking the exit of a command piped to `tail`/`grep`.
- **Don't pin versions blindly**: if a build fails after an upgrade, read the actual error before touching `package.json`.

## Verification Checklist

- [ ] `node_modules` present (or `npm ci` succeeded)
- [ ] `npm run build` exits 0 with success output captured
- [ ] ESM import failures fixed with namespace import, call sites preserved
- [ ] Regenerated artifacts checked against gitignore before claiming repo state
- [ ] Evidence (exit code + tail) recorded

## References

- `references/esm-interop-build-repair.md` — js-yaml 5.2.0 ESM case study, patch-swap incident, and exact repair commands
- `references/batch-dep-restore-after-cleanup.md` — background loops to restore node_modules + venvs across all repos after a cleanup phase (bun/npm auto-detect, `--ignore-scripts`, uv on Windows, post-restore integrity sweep)

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
