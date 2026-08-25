---
title: "Dependency & Toolchain Update — All Projects"
description: "Update all dependencies, devDependencies, and tooling configs to latest versions across root, packages/, and projects/"
date: 2026-08-25
version: 1.0.0
author: Hermes Agent
tags: [dependencies, tooling, bun, eslint, prettier, typescript, python, mcp]
---

# Dependency & Toolchain Update Plan

## Goal
Update all dependencies, devDependencies, and tooling configurations to latest stable versions across:
- **Root workspace** (`package.json`, tooling configs)
- **packages/** (openrouter-client, openrouter-client-py)
- **projects/** (17 sub-projects, excluding node_modules)
- **MCP tooling** (tooling-config, tooling-lint, python-quality)

## Current State Summary

### Root Workspace
- **package.json**: Bun 1.3.14, TypeScript 5.9.0, ESLint 10.0.1, Prettier 3.9.6, markdownlint-cli2 0.19.1, cspell 10.0.1
- **bun.lock**: Present
- **Tooling configs**: .eslint.config.js/mjs, .prettierrc.json, .markdownlint.jsonc, .markdownlint-cli2.jsonc, .pre-commit-config.yaml (pre-commit-hooks v5.0.0), .ruff.toml, pyrightconfig.json

### packages/
1. **openrouter-client** (TypeScript): @openrouter/sdk ^1.0.0, TypeScript ^5.0.0, Bun types ^1.0.0
2. **openrouter-client-py** (Python): openrouter >=1.0.0, pytest >=7.0 (optional), requires Python >=3.11

### projects/ (17 sub-projects, excluding node_modules)
- Banking (Next.js)
- Bash (OpenCode agent)
- comicwise
- cookiecutter-django-tailwind
- Django-Scrapy-Selenium
- ecom
- mcp-server-typescript
- profile
- Python-projects
- Resume_maker
- rhixe_scans
- selenium_webdriver
- university-libary-jsm
- xamehi
- xamehi.tv
- youtube-downloader
- mcp-servers

### MCP Tooling Skills
- **tooling-config**: gitignore, editorconfig, pre-commit, git-cliff
- **tooling-lint**: ESLint, Prettier, CSpell, Markdownlint, Mypy
- **python-quality**: Ruff, Pyright/Pylance

---

## Phase 1: Discovery & Inventory

### Task 1.1: Audit Root Dependencies
- [ ] Check current versions in root package.json
- [ ] Run `bun outdated` to see available updates
- [ ] Document current vs latest versions

### Task 1.2: Audit packages/ Dependencies
- [ ] Check openrouter-client package.json
- [ ] Check openrouter-client-py pyproject.toml
- [ ] Run `bun outdated` in each

### Task 1.3: Audit projects/ Dependencies
- [ ] Find all package.json in projects/ (excluding node_modules)
- [ ] Run `bun outdated` for each project
- [ ] Document which projects need updates

### Task 1.4: Audit Tooling Configs
- [ ] Check .eslint.config.js / .eslint.config.mjs
- [ ] Check .prettierrc.json
- [ ] Check .markdownlint.jsonc / .markdownlint-cli2.jsonc
- [ ] Check .pre-commit-config.yaml (pre-commit-hooks version)
- [ ] Check .ruff.toml
- [ ] Check pyrightconfig.json

---

## Phase 2: Root Workspace Updates

### Task 2.1: Update Root package.json
```json
// Update to latest stable versions:
- "typescript": "^5.x" (latest 5.x)
- "eslint": "^10.x" (latest 10.x)
- "@eslint/js": "^10.x"
- "typescript-eslint": "^8.x" (latest 8.x)
- "prettier": "^3.x" (latest 3.x)
- "markdownlint-cli2": "^0.19.x" (latest 0.x)
- "cspell": "^10.x" (latest 10.x)
- "globals": "^17.x"
- "@types/node": "^24.x"
- "@types/bun": "latest"
```
- [ ] Update package.json
- [ ] Run `bun install` to update bun.lock
- [ ] Run `bun run check` to verify

### Task 2.2: Update Tooling Configs
- [ ] **ESLint**: Ensure flat config (`eslint.config.mjs`) with proper ignores for submodules
- [ ] **Prettier**: Verify .prettierrc.json, add `projects/` to .prettierignore
- [ ] **Markdownlint**: Sync .markdownlint.jsonc and .markdownlint-cli2.jsonc with recommended rules (disable MD013, MD024, MD025, MD041, MD060 for prompt-heavy repo)
- [ ] **CSpell**: Update cspell.json with domain terms
- [ ] **pre-commit**: Update .pre-commit-config.yaml to latest hook versions (pre-commit-hooks v5.0.0+)
- [ ] **Ruff**: Update .ruff.toml with target-version py311, line-length 120
- [ ] **Pyright**: Verify pyrightconfig.json with proper excludes

---

## Phase 3: packages/ Updates

### Task 3.1: openrouter-client (TypeScript)
- [ ] Update @openrouter/sdk to latest
- [ ] Update TypeScript to latest 5.x
- [ ] Update @types/bun to latest
- [ ] Run `bun install` and `bun run typecheck`

### Task 3.2: openrouter-client-py (Python)
- [ ] Update openrouter to latest
- [ ] Update pytest to latest (optional)
- [ ] Verify Python >=3.11 compatibility
- [ ] Run `uv pip install -e .` and tests

---

## Phase 4: projects/ Updates (17 projects)

### Strategy
For each project, apply consistent updates:
1. Run `bun outdated` to identify updates
2. Update dependencies & devDependencies to latest compatible versions
3. Update tooling configs if project has custom ones
4. Run `bun install` and validate with lint/typecheck

### Task 4.1: TypeScript/Node Projects
Projects likely using TypeScript/Next.js/Node:
- Banking
- Bash (OpenCode)
- comicwise
- mcp-server-typescript
- university-libary-jsm
- xamehi
- xamehi.tv
- Resume_maker
- rhixe_scans
- selenium_webdriver
- ecom
- cookiecutter-django-tailwind
- mcp-servers

**Common updates per project:**
- [ ] typescript: ^5.x
- [ ] eslint: ^10.x
- [ ] @types/node: ^24.x
- [ ] @types/bun: latest
- [ ] prettier: ^3.x
- [ ] markdownlint-cli2: ^0.19.x
- [ ] cspell: ^10.x
- [ ] Framework-specific updates (next, react, etc.)

### Task 4.2: Python Projects
- Python-projects
- Django-Scrapy-Selenium

**Common updates per project:**
- [ ] Update pyproject.toml / requirements.txt
- [ ] Run `uv pip install --upgrade`
- [ ] Run ruff check && pyright

---

## Phase 5: MCP Tooling Validation

### Task 5.1: tooling-config MCP
- [ ] Run `gitignore_validate`, `editorconfig_validate`, `gitmodules_validate`
- [ ] Run `precommit_init` if needed
- [ ] Run `precommit_install` and `pre-commit run --all-files`
- [ ] Run `changelog_generate`

### Task 5.2: tooling-lint MCP
- [ ] Run `eslint_check` on root and projects
- [ ] Run `prettier_check` on root and projects
- [ ] Run `cspell_check` on root and projects
- [ ] Run `markdownlint_check` on root and projects
- [ ] Run `mypy_check` on Python projects

### Task 5.3: python-quality MCP
- [ ] Run `python_check_all` on root and Python projects
- [ ] Run `python_fix` where needed
- [ ] Verify .ruff.toml and pyrightconfig.json are up to date

---

## Phase 6: Validation & Verification

### Task 6.1: Root Validation
- [ ] `bun run lint` passes
- [ ] `bun run format:check` passes
- [ ] `bun run markdownlint` passes
- [ ] `bun run spellcheck` passes
- [ ] `bun run typecheck` passes
- [ ] `bun run check` passes (full pipeline)

### Task 6.2: packages/ Validation
- [ ] openrouter-client: `bun run typecheck` passes
- [ ] openrouter-client: `bun test` passes
- [ ] openrouter-client-py: `pytest` passes

### Task 6.3: projects/ Validation
- [ ] Each project: run lint, typecheck, tests
- [ ] Document any breaking changes or manual fixes needed

### Task 6.4: Git Commit
- [ ] `git add -A`
- [ ] `git commit -m "chore(deps): update all dependencies and tooling to latest versions"`
- [ ] `git push -u origin development production`
- [ ] Verify CI passes on both branches

---

## Risks & Trade-offs

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Breaking changes in major versions (ESLint 10→11, TypeScript 5→6) | Medium | High | Pin to latest minor of current major; test incrementally |
| Submodule node_modules conflicts | High | Medium | Add `projects/**/node_modules` to root .eslintignore and .prettierignore |
| Python package compatibility (ruff/pyright versions) | Low | Medium | Use uv for isolated installs; pin compatible versions |
| Pre-commit hooks slow on first run | High | Low | Run once manually; document SKIP= for CI |
| 3926 package.json files (many in node_modules) | High | High | **Exclude node_modules** — only update project-level package.json |

---

## Open Questions

1. Should we update Bun itself (`bun upgrade`)?
2. Should we update to ESLint v11 (beta) or stay on v10?
3. Should we update TypeScript to v6 (beta) or stay on v5?
4. Are there any projects that MUST stay on specific versions?
5. Should we add renovate/dependabot for automated future updates?

---

## Success Criteria

- [ ] All root dependencies updated to latest stable
- [ ] All packages/ dependencies updated
- [ ] All 17 projects/ dependencies updated (excluding node_modules)
- [ ] All tooling configs updated and aligned
- [ ] Root `bun run check` passes
- [ ] All MCP tooling validation passes
- [ ] Git commit pushed to development and production
- [ ] No regressions in tests

---

## Implementation Order

1. **Phase 1** (Discovery) — ~30 min
2. **Phase 2** (Root) — ~15 min
3. **Phase 3** (packages/) — ~10 min
4. **Phase 4** (projects/) — ~60 min (parallel where possible)
5. **Phase 5** (MCP validation) — ~15 min
6. **Phase 6** (Final validation) — ~20 min

**Estimated total: ~2.5 hours**

---

## Notes

- Use `bun install` (not `bun add`) for lockfile updates after package.json changes
- For projects with custom tooling configs, preserve them but align with root conventions
- Use subagent-driven-development for parallel project updates
- Document any manual fixes required per project
