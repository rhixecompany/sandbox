---
name: package-manager-migration
title: Package Manager Migration (npm/pnpm → bun)
description: 'Use when migrating JS/TS repos from npm/pnpm to bun.'
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - bun
  - npm
  - pnpm
  - package-manager
  - migration
  - ci
  - github-actions
metadata:
  hermes:
    tags: [package-manager, migration, bun, npm, ci]
---

# Package Manager Migration

Class-level workflow for migrating a JS/TS repository (or a multi-repo workspace) from `npm`/`pnpm`/`yarn` to `bun` — and symmetrically to any target manager. The detailed npm→bun path was proven on a 20-manifest workspace incl. Hermes root, 2026-08-08; the CI gotchas are the durable value.

## When to Use

- User asks: "replace npm with bun / npx with bunx", "make bun the default package manager", "use bun in this repo and sub-repos", or references a `/setup-bun-bunx` class prompt.
- A repo has both `npm` and `bun` lockfiles and needs a clean default.
- CI workflows still use `setup-node` + `npm ci` while manifests are bun-first.

## When NOT to Use

- Single-file `npm i` → `bunx` substitutions inside one script (just edit it).
- Installing bun itself (that's `bun-package-manager` / docs territory).
- Migrating Python/Rust toolchains (`uv-package-manager`, etc.).

## Workflow

### 1. Scope the inventory (before touching anything)

1. `bun --version` and `node --version` available on the box.
2. Enumerate manifests: `find . -name package.json -not -path '*/node_modules/*' -not -path '*/.git/*'`.
3. Enumerate lockfiles per dir: `package-lock.json`, `pnpm-lock.yaml`, `bun.lock`, `bun.lockb`, `.npmrc`, `bunfig.toml`.
4. Grep npm/npx usage in: manifest scripts, `.github/workflows/*.yml` (root AND sub-repos), README/AGENTS command blocks, scripts.
5. Identify which sub-repos are their own git repos (`-d "$d/.git"`) — decide per-repo commit scope.
6. **Hermes root special case**: Hermes itself (`~/AppData/Local/hermes`) has NO `package.json` — "npm/npx" hits there are VS Code launch/task *template strings* inside Python scripts and MCP `.bat` wrappers that genuinely need `npx.cmd`. Document exceptions; do NOT blanket-rewrite them. Rule: only rewrite actual manifests/scripts, not string templates.

### 2. Migrate manifests (text-level, NOT JSON round-trip)

Prefer regex on the raw file over `json.loads/dumps` — round-tripping destroys formatting (tabs, key order) across many files. Isolate the `"scripts"` block and apply, in order:

| Source | Replacement |
|---|---|
| `npm run` | `bun run` |
| `npx <cmd>` | `bunx <cmd>` |
| `npm ci` | `bun install --frozen-lockfile` |
| `npm install` / `npm i` | `bun install` |
| `npm test` / `npm start` | `bun run test` / `bun run start` |
| `npm run` chains in one `&&` string | replace each occurrence |
| bare `npm-check-updates` CLI | `bunx npm-check-updates` (package name stays) |
| pnpm-invoked schema tools | `pnpm <x>` → `bunx <x>` (fix double `bunx bunx` after) |

Validate JSON after each write (`json.loads(newraw)`) before saving.

Pitfall: `npm-check-updates` is both a package name and a CLI. Replacing bare `npm` only corrupts `npm-check-updates` (hyphen-adjacent match). Sequence replacements so script bodies keep the package name and only invocation prefixes change; then fix `bunx bunx` dupes.

### 3. Pin the manager version

Add to every manifest: `"packageManager": "bun@<exact-version>"` (use `bun --version`, e.g. `bun@1.3.14`). If a repo declares `pnpm@9.12.3`, overwrite it — the point is a single default.

### 4. Swap lockfiles

- `bun.lock*` exists AND `package-lock.json` also exists → **delete** the npm lock (stale).
- Only `package-lock.json` exists → `bun install` once to generate `bun.lock` (bun migrates from package-lock.json); delete the npm lock after a successful install.
- Cookie-cutter / Jinja manifests (`{{cookiecutter.project_slug}}/package.json`): delete npm locks but DO NOT run `bun install` inside a template.
- `.npmrc` (`legacy-peer-deps=true`): bun ignores `.npmrc`; prefer `bunfig.toml`. Remove `.npmrc` only if nothing else references it.
- `bun install` on huge legacy CRA trees can exceed the 300s foreground cap — run heavy installs in **background** with `notify_on_complete=true`.

### 5. CI workflows (root + every sub-repo's `.github/workflows/`)

The single most error-prone step. `oven-sh/setup-bun@v2` is a near drop-in for `actions/setup-node@v4` BUT:

- `setup-bun` does **NOT** accept `node-version:` — remove the line or the step fails input validation.
- `with:` must not be left empty — delete a now-empty `with:` block entirely.
- `cache: "npm"` → `cache: "bun"`.
- npm cache blocks (manual `actions/cache` steps) are path + key coupled:
  - `path: ~/.npm` → `path: ~/.bun/install/cache`
  - `key: …-npm-ci-$…$(hashFiles('package-lock.json'))` → `-bun-ci-` + `hashFiles('bun.lock')`
  - restore-keys prefixes likewise `npm-ci-` → `bun-ci-`.
- Command swaps per the table in Step 2 (same word boundaries).
- **After batch edits, `yaml.safe_load` every workflow** — a single leftover `node-version` paired with `setup-bun` is a silent CI breaker.

### 6. Verify

Per touched repo (after `bun install` once):
```bash
bun install
bun run lint
bun run typecheck
bun run check
grep -rInE '\b(npm|npx)\b' --include='*.json' --include='*.md' --include='*.yml' . | grep -v node_modules
```

Document exceptions (Hermes MCP stdio servers needing npx; template-string VS Code configs) in the repo, don't hide them.

### 7. Commit & push (per-repo, after green)

`git add -A; git commit -m "updates"; git push` per repo. On Windows, sub-repo worktrees with read-only `.git` pack files can block `git`/`rmtree` — use MSYS `rm -rf` for cleanup.

## Pitfalls

- **Blanket `setup-node`→`setup-bun` leaves broken steps**: the old `with:` may carry `node-version: "22"` and `cache: "npm"` (right for node, fatal for bun). Handle the `with:` block, not just the `uses:` line.
- **Recursive `node_modules` loops blow up recursive globs**: a repo with `comicbook/node_modules/comicbook/…` recursion causes `pathlib.glob("**/…")` WinError 1921. Use a pruned `os.walk`:
  ```python
  dirnames[:] = [d for d in dirnames if d not in ("node_modules",".git",".venv","site-packages",".next","dist")]
  ```
- **`write_file` stream cap on large content** — prefer `execute_code`/Python file I/O for big rewrites.
- **`.disabled` workflows and `*.lock.yml` bot config**: don't rewrite stub `.disabled` / bot-lock JSON (they list `package-lock.json` as a protected file name — a label, not usage).
- **Comments/strings**: scope replacements to scripts blocks to avoid false hits on prose.

## References

- `references/npm-to-bun-migration-session-2026-08-08.md` — worked transcript: manifest inventory, exact regex recipes, CI before/after, verification results.

## Verification Checklist

- [ ] Prerequisites and environment are properly configured
- [ ] Package Manager Migration (npm/pnpm → bun) operations completed successfully
- [ ] Output meets expected quality and requirements
- [ ] Any errors during execution were resolved
- [ ] Changes are documented and committed if applicable

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
