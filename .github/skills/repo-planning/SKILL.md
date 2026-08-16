---
name: repo-planning
title: "Repo Planning: Plans + Specs for Every Repo"
description: "Generate PLAN.md+SPEC.md per repo via prompt-management."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [planning, specs, repos, submodules, prompt-management]
---

# Repo Planning

## Overview

Generate comprehensive plans and specs for the workspace root and every `projects/` subrepo, driven by the `repo-*.prompt.md` prompt family (repo-management, repo-research-pipeline, repo-story-time) and prompt-management conventions. Output: per-repo `PLAN.md` + `SPEC.md` with valid frontmatter, verified on disk.

## When to Use

- User asks to "create and verify comprehensive plan and specs for all, each repo and subrepos in ./"
- Running prompt-management over `repo-*.prompt.md` prompts
- Standing up per-repo planning artifacts before tooling implementation

## Workflow

### Phase 1 — Inventory repos
- Enumerate root + `projects/*/` (git submodules). Record per repo: name, language mix (from config files), entrypoints, existing PLAN.md/SPEC.md.

### Phase 2 — Resolve prompt inputs
- Read `.github/prompts/repo-management.prompt.md`, `repo-research-pipeline.prompt.md`, `repo-story-time.prompt.md` frontmatter + body. Use inline bodies as authoritative (per-prompt templates often absent — do not fabricate).
- Map each prompt's Outputs to per-repo artifacts.

### Phase 3 — Generate PLAN.md + SPEC.md per repo
- PLAN.md frontmatter: `name, title, description, version, status: not_started, created, tags`.
- SPEC.md frontmatter: `name, title, version, status, requirements: [], acceptance_criteria: []`.
- Keep each under ~120 lines; reference shared rules, don't duplicate.

### Phase 4 — Verify
- `yaml.safe_load` every generated frontmatter; confirm file presence per repo via `find`; record counts.

## Pitfalls

- **Per-prompt template dirs often missing** — treat inline body as spec; note skipped refs.
- **Don't fabricate repo metadata** — read configs on disk (package.json, pyproject.toml, Cargo.toml, *.csproj) before writing.
- **CRLF trap** — write LF in this repo (`.gitattributes` *.md eol=lf); never `.replace("\n","\r\n")` on already-CRLF text.
- **Batch size** — process repos sequentially or in ≤7-file batches; verify after each batch.
- **Subrepos are git submodules** — do not commit inside them unless asked.

## Verification Checklist

- [ ] Every repo has PLAN.md and SPEC.md on disk
- [ ] All frontmatter parses via yaml.safe_load
- [ ] Counts match inventory (no fabricated repos)
- [ ] Files written LF-only

## Related Skills

| Skill | Purpose |
|-------|---------|
| `prompt-management` | Create/update/execute the repo prompts |
| `plans-and-specs` | Plan+spec decomposition patterns |
| `tooling-implementation` | Tooling stack implementation after planning |
| `executing-plans` | Execute the master plan |

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
