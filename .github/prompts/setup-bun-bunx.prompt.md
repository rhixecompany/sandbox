---
name: setup-bun-bunx
title: Migrate npm/npx to Bun/Bunx Across Repos
description: Replace every npm/npx usage with bun/bunx in this repo, all sub-repos, and the Hermes root. Trim package.json/toml/.npmrc dependencies, uninstall unused deps, set bun as the default package manager, then commit and push.
version: 1.1.0
license: MIT
author: Hermes Agent
tags:
- bun
- bunx
- npm
- npx
- migration
- package-manager
- dependencies
toolsets:
- terminal
- file
- skills
- todo
trigger: /setup-bun-bunx
skills:
- bun-nextjs
- bun-shell
- pnpm-package-manager
dependencies:
- skill:bun-nextjs
- skill:bun-shell
- skill:pnpm-package-manager
metadata:
  hermes:
    source: setup-bun-bunx.prompt.txt
    converted: '2026-08-08'
scripts: []
formatter: default
plan: ''
---
## Goal

First **clean up npm/bun remnants and upgrade bun to the latest version** (`bun upgrade`), then update **all usage of `npm` → `bun` and `npx` → `bunx`** in three scopes: this repository, all sub-repositories under it, and the Hermes root (`~/AppData/Local/hermes`). Audit every `package.json`, `*.toml`, and `.npmrc` file, use smaller/leaner dependencies and dev dependencies, uninstall all unused dependencies and dev dependencies, set **bun as the default package manager**, then commit and push in this repo and all sub-repos — debugging and fixing every issue encountered.

## Subgoals

1. **Upgrade** — Run `bun upgrade` everywhere; confirm the latest Bun version on this machine.
2. **Audit** — Inventory `npm`/`npx` usage and dependency manifests across all three scopes.
3. **Migrate** — Replace `npm` with `bun` and `npx` with `bunx` in scripts, docs, and CI.
4. **Slim** — Trim unnecessary dependencies and dev dependencies; prefer smaller alternatives.
5. **Uninstall** — Remove all unused dependencies (`bun pm prune`, `bun remove`).
6. **Default** — Make `bun` the default package manager (`packageManager` field, remove npm lockfiles, `.npmrc` → `.bunfig.toml` where applicable).
7. **Verify** — Run the project's checks (`bun run lint`, `bun run typecheck`, `bun run check`) after every migration.
8. **Ship** — `git add -A; git commit -m "updates"; git push` in this repo and all sub-repos, debugging and fixing all issues.

## Personas

- **Migration Engineer** — Executes the npm→bun/npx→bunx conversion.
- **Dependency Auditor** — Justifies every kept dependency; flags unused/duplicate packages.
- **QA** — Verifies each repo still lints, type-checks, and builds under bun.

## Personality

- **Tone**: Thorough, pragmatic, low-risk.
- **Style**: Repo by repo; verify before moving on.
- **Avoid**: Blind `npm i`/`bun add` of new packages, silent lockfile deletion, breaking scripts.
- **Encourage**: `bun install` fresh installs, `bunx` for one-off tools, `.bunfig.toml` defaults, lockfile regeneration.

## Context

Source: `setup-bun-bunx.prompt.txt` — a migration runbook to move this workspace and the Hermes installation onto the Bun runtime and Bun's package manager. `npm config get omit` == dev globally on this machine can silently skip devDependencies, so always install with the equivalent of `--include=dev` (`bun install` includes dev by default).

## Rules


> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)
> Domain-specific additions below.

### Domain Rules

1. **No npm/npx left behind** — Every manifest/script/CI reference to `npm`/`npx` becomes `bun`/`bunx`.
2. **Smaller is better** — Replace heavyweight deps with smaller equivalents where behavior is preserved; document each swap.
3. **Uninstall unused** — Remove packages not referenced by any import/script; record removals.
4. **Default manager** — Set `"packageManager": "bun@<version>"` in `package.json`; remove `package-lock.json`/`npm-shrinkwrap.json`; keep `bun.lock`/`bun.lockb`.
5. **Verify before commit** — `bun run lint`, `bun run typecheck`, `bun run check`, `bun run format` must pass in every touched repo.
6. **Hermes root is special** — `~/AppData/Local/hermes` must stay functional; if a script there genuinely requires `npm` (e.g. npx-based MCP servers), document the exception rather than breaking it.
7. **Commit/push only after green** — Do not commit failing repos; debug and fix first.

## Steps

### Phase 0 — Cleanup & Upgrade

1. Confirm the current Bun version and upgrade to latest:

   ```bash
   bun --version
   bun upgrade
   bun --version   # confirm version bump
   ```

2. Clean stale npm/bun artifacts (orphan `package-lock.json`, `node_modules/.package-lock.json`, mixed lockfiles).

### Phase 1 — Audit

1. In **this repo**, list all `npm`/`npx` usage and all manifests:

   ```bash
   grep -rInE '\b(npm|npx)\b' --include='*.json' --include='*.toml' --include='*.md' --include='*.sh' --include='*.yml' --include='*.yaml' .
   find . -name 'package.json' -not -path '*/node_modules/*' -not -path '*/.git/*'
   ```

2. Repeat for **sub-repos** and the **Hermes root** (`~/AppData/Local/hermes`).
3. Write the inventory (file → npm/npx occurrences → dependency list) to a scratchpad.

### Phase 2 — Migrate

4. Replace `npm run <script>` → `bun run <script>`, `npm install`/`npm ci` → `bun install`, `npx <pkg>` → `bunx <pkg>`, `npm audit` → `bun audit`, `npm publish` → `bun publish`.
5. Update CI workflows (`.github/workflows/*.yml`) and docs to use `oven-sh/setup-bun` and `bun` commands.
6. Convert `.npmrc` settings to `.bunfig.toml` where Bun supports them (registry, scopes, `install.cache`).

### Phase 3 — Slim Dependencies

7. For each `package.json` and `*.toml`:
   - Remove dependencies not referenced by any code or script.
   - Replace heavyweight packages with smaller equivalents (e.g. `lodash` → native/`es-toolkit`) — only where behavior is preserved and tests pass.
   - Prefer devDependencies over dependencies for build-only tools.
8. Uninstall unused packages:

   ```bash
   bun remove <pkg>          # per package
   bun pm prune              # prune extraneous
   ```

### Phase 4 — Default Manager

9. Set `"packageManager": "bun@<version>"` (check `bun --version`) in every `package.json`.
10. Remove `package-lock.json` and `npm-shrinkwrap.json`; generate `bun.lockb`/`bun.lock` via `bun install`.
11. Delete any stale `node_modules/.package-lock.json` residue from npm.

### Phase 5 — Verify

12. Run in every touched repo:

    ```bash
    bun install
    bun run lint
    bun run typecheck
    bun run check
    bun run format
    ```

13. Fix every error (missing deps, broken scripts, path casing on Windows). Use `bunx` for tools Bun does not bundle.
14. Confirm no remaining `npm`/`npx` references except documented exceptions:

    ```bash
    grep -rInE '\b(npm|npx)\b' --include='*.json' --include='*.toml' --include='*.md' --include='*.sh' --include='*.yml' . | grep -v node_modules
    ```

### Phase 6 — Commit & Push

15. In **this repo and all sub-repos**, commit and push:

    ```bash
    git add -A
    git commit -m "updates"
    git push
    ```

16. Debug and fix all issues (auth, hooks, divergent branches) until push succeeds.

## Verification

- Zero `npm`/`npx` references remain (except documented Hermes exceptions).
- `bun install` is clean; `bun.lock`/`bun.lockb` committed; npm lockfiles gone.
- `packageManager` set to bun in every touched repo.
- All lint/typecheck/check/format pass with bun in this repo, sub-repos, and Hermes root.
- Commits pushed in this repo and all sub-repos.
- Removal report: packages removed, packages swapped, size deltas.

## MCP Servers & Tools

- **Terminal** — `bun`/`bunx` execution for migration and verification.
- **File tools** — read/patch manifests (`package.json`, `tsconfig.json`).
- **Tooling-lint MCP** — eslint/prettier checks across touched repos.
- **Tooling-config MCP** — pre-commit/.gitignore validation.


## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.


## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section


## Related Prompts

Same-family prompts:

- [`setup-component.prompt.md`](setup-component.prompt.md)
- [`setup-enhanced.prompt.md`](setup-enhanced.prompt.md)
- [`setup-groq-cloud.prompt.md`](setup-groq-cloud.prompt.md)
- [`setup-nextjs-frontend-stack.prompt.md`](setup-nextjs-frontend-stack.prompt.md)
- [`setup.prompt.md`](setup.prompt.md)
