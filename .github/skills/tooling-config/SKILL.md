---
name: tooling-config
title: "Repo Hygiene: gitignore, editorconfig, pre-commit, git-cliff"
description: "Use when setting up gitignore, editorconfig, pre-commit."
version: 1.0.0
author: "Hermes Agent"
tags: [gitignore, editorconfig, pre-commit, git-cliff, gitmodules, repo-hygiene, mcp]
license: MIT
---
# Repo Hygiene Tooling (tooling-config)

## Overview

Standardized workflow for repository hygiene: ignore rules, editor normalization, submodule validation, pre-commit hooks, and changelog generation. Integrates with the **`tooling-config` MCP server**.

## When to Use

- Scaffolding a new repo's hygiene files
- Auditing missing/broken `.gitignore`, `.editorconfig`, `.gitmodules`, pre-commit, or cliff config
- Rolling out tooling across a multi-repo workspace / submodules
- Installing or running pre-commit hooks

## Quick Reference

| File/Tool | MCP Tool | Purpose |
|-----------|----------|---------|
| `.gitignore` | `gitignore_init` / `gitignore_validate` | Ignore rules (Python/JS defaults) |
| `.editorconfig` | `editorconfig_init` / `editorconfig_validate` | Editor normalization |
| `.gitmodules` | `gitmodules_validate` | Submodule integrity |
| pre-commit | `precommit_init` / `precommit_install` / `precommit_run` | Git hooks |
| git-cliff | `changelog_init` / `changelog_generate` | Changelog from conventional commits |

### CLI Equivalents

```bash
pre-commit install && pre-commit run --all-files
git-cliff -o CHANGELOG.md
```

## 1. INIT — Scaffold Configs

- `gitignore_init(project_root=...)` → `.gitignore` (Python/JS common ignores).
- `editorconfig_init(project_root=...)` → `.editorconfig` (utf-8, lf, 2/4-space).
- `precommit_init(project_root=...)` → `.pre-commit-config.yaml` (basic hooks: ruff, prettier, markdownlint, git-cliff).
- `changelog_init(project_root=...)` → `cliff.toml` for git-cliff.
- **Never overwrite existing configs** — init only where files are missing; custom `.gitignore`/`.editorconfig` entries are repo-specific and must be preserved.

## 2. VALIDATE — Audit Existing Configs

`gitignore_validate`, `editorconfig_validate`, `gitmodules_validate` — run at the repo root (`.gitmodules` lives at the superproject root only).

## 3. INSTALL & RUN — Pre-Commit

```bash
pre-commit install       # once per clone
pre-commit run --all-files
```

`precommit_install` writes to `.git/hooks/` — local only, never committed. Hooks may be slow on first run (downloads environments).

## 4. PITFALLS

| Pitfall | Severity | Mitigation |
|---------|----------|------------|
| Overwriting a custom `.gitignore` loses repo-specific rules | High | Init only if missing; append otherwise |
| pre-commit hook envs download on first run (slow/offline fails) | Medium | Run `pre-commit install` once; use `SKIP=` to bypass |
| `.editorconfig` with `end_of_line = crlf` fights `.gitattributes` lf | Medium | Keep `lf`; set `core.autocrlf` consistently |
| git-cliff needs conventional commits; messy history yields noisy changelog | Medium | Configure `cliff.toml` `commit_parsers` for your prefixes |
| Submodules: configs must be committed in each submodule repo, not the superproject | High | `gitmodules_validate` at root; commit per submodule |
| Local tools not on global PATH | Medium | `_find_tool` checks `node_modules/.bin` in project root before failing — run `bun install`/`npm install` first |

## 5. Verification Checklist

- [ ] `.gitignore` exists per repo (no init overwrites)
- [ ] `.editorconfig` exists per repo
- [ ] `.pre-commit-config.yaml` exists per repo
- [ ] `cliff.toml` exists per repo
- [ ] `gitignore_validate` / `editorconfig_validate` / `gitmodules_validate` clean
- [ ] `pre-commit run --all-files` passes (or documented failures)
- [ ] `changelog_generate` produces CHANGELOG.md

## Related Skills

| Skill | Purpose |
|-------|---------|
| `devops/tooling-implementation` | Umbrella: full tooling stack workspace-wide |
| `software-development/python-quality` | Python lint/format/typecheck |
| `software-development/tooling-lint` | JS/TS/Markdown linting |
| `github/finishing-a-development-branch` | Commit/PR hygiene after tooling rollout |

## Verification Checklist

- [ ] Prerequisites and environment are properly configured
- [ ] "Repo Hygiene: gitignore, editorconfig, pre-commit, git-cliff" operations completed successfully
- [ ] Output meets expected quality and requirements
- [ ] Any errors during execution were resolved
- [ ] Changes are documented and committed if applicable

## Workflow

### Phase 1: Preparation

Set up required environment, dependencies, and configuration for "Repo Hygiene: gitignore, editorconfig, pre-commit, git-cliff".

### Phase 2: Execution

Run the primary "Repo Hygiene: gitignore, editorconfig, pre-commit, git-cliff" operations according to the defined requirements.

### Phase 3: Verification

Verify output, handle any errors, and confirm results meet expectations.

### Phase 4: Completion

Document results, clean up resources, and finalize any deliverables.

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
