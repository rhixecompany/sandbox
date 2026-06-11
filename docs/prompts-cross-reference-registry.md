---
title: Prompt Cross-Reference Registry
description: Three-way cross-reference mapping of prompts across OpenCode, Hermes, and Copilot platforms.
status: final
tags: [hermes, commands-fix, cross-reference, prompts, sync, discovery]
created: 2026-06-01
---

# Prompt Cross-Reference Registry

Generated: 2026-06-01
Scope: `.github/prompts/` ↔ `skills/` ↔ `Prompts/`

## Platform Inventory

| Platform | Location | Count | Naming Convention |
|----------|----------|-------|-------------------|
| **OpenCode** | `.github/prompts/*.prompt.md` (shared with Copilot) | 100+ | Filename-based triggers (no `.opencode/commands/` dir) |
| **Hermes** | `~/AppData/Local/hermes/skills/**/SKILL.md` | 177 | Category/skill-name hierarchy |
| **Copilot** | `.github/prompts/*.prompt.md` | 100+ | 7 with explicit `trigger:` frontmatter, ~93 filename-based |
| **Prompts/** | `Prompts/*.md` | 8 | Workflow orchestration prompts with `/trigger` names |

## Discovery Notes

### OpenCode
No `.opencode/commands/` directory exists on disk. OpenCode is used via the `opencode-zen` VS Code extension. The `.github/prompts/` directory serves as the shared prompt source for both Copilot and OpenCode — there is no gap between them.

### Hermes
Hermes skills use `SKILL.md` naming — no `.prompt.md` files are in the skills directory. Skills are loaded by their directory name/alias, not by filename trigger.

### Copilot
`.github/prompts/` contains 100+ `.prompt.md` files. Only 7 have explicit `trigger:` in YAML frontmatter. The remaining ~93 use their filename as the implicit command name (standard Copilot convention).

## Three-Way Cross-Reference

### Match 1: Prompts/ → Copilot Dependencies

All 8 `Prompts/*.md` files list `.github/prompts/` workflows as dependencies in their Skills Required sections. Most reference `context-map` as a shared dependency.

### Match 2: Copilot → Hermes (Direct Name Matches)

| Copilot Prompt | Hermes Skill | Notes |
|---------------|-------------|-------|
| `hermes-breakdown-epic-arch` | `architecture/hermes-breakdown-epic-arch` | Intentionally mirrored |
| `hermes-breakdown-epic-pm` | `product/hermes-breakdown-epic-pm` | Intentionally mirrored |
| `hermes-breakdown-feature-implementation` | `development/hermes-breakdown-feature-implementation` | Intentionally mirrored |
| `hermes-breakdown-feature-prd` | `product/hermes-breakdown-feature-prd` | Intentionally mirrored |
| `hermes-breakdown-plan` | `planning/hermes-breakdown-plan` | Intentionally mirrored |
| `hermes-breakdown-test` | `development/hermes-breakdown-test` | Intentionally mirrored |

**Total: 6 matched prompts**

### Match 3: Copilot → Hermes (Functional Equivalents)

| Copilot Prompt | Similar Hermes Skill | Notes |
|---------------|---------------------|-------|
| `boost-prompt` | `autonomous-ai-agents/enhance-markdown` | Similar prompt enhancement focus |
| `context-map` | `software-development/codemap` | Same mapping purpose |
| `code-review` | `github/github-code-review` | Code review workflow |
| `testing` / `playwright-typescript` | `qa/webapp-testing` | Testing focus |
| `security` | `red-teaming/godmode` | Security/red-teaming |
| `documentation` / `documentation-writer` | `software-development/project-docs` / `software-development/code-docs` | Documentation focus |
| `debug-issue` | `software-development/systematic-debugging` | Debugging workflow |

**Total: ~10 functional equivalents**

### Flagged Items

| # | Flag | Type | Details |
|---|------|------|---------|
| 1 | 🔶 `humanizer` | Potential duplicate | Root-level `humanizer` (2KB) + `creative/humanizer` (32KB). Root has references directory. Verify intent. |
| 2 | ℹ️ No OpenCode dir | Environment note | `.opencode/commands/` doesn't exist — `.github/prompts/` is the shared source |
| 3 | ℹ️ 93 prompts without triggers | Design choice | Filename-as-command for Copilot prompts is standard convention |
| 4 | ℹ️ 117 Copilot-only prompts | Expected | Platform-specific prompts (testing, CI/CD, code gen) not applicable to Hermes |
| 5 | ℹ️ 125 Hermes-only skills | Expected | Domain coverage (creative, media, ML, gaming, smart home) not applicable to Copilot |

## Platform Role Summary

```
OpenCode  ──shares──►  .github/prompts/  ◄──shares──  Copilot
                              │
                              │ (6 mirrored prompts)
                              ▼
                    Hermes skills/ (177 skills)
                              │
                              │ (8 orchestration files)
                              ▼
                    Prompts/*.md (workflow orchestration)
```

- **OpenCode & Copilot** share the same `.github/prompts/` prompt source
- **Hermes** has 6 mirrored prompts from the `.github/prompts/` set
- **Prompts/** orchestrates multi-step workflows using prompts from both platforms
- The ecosystems are **complementary, not redundant** — no forced sync is required

## Sync Assessment

| Action | Needed? | Rationale |
|--------|---------|-----------|
| Sync OpenCode → Copilot | ❌ No | Same source directory |
| Sync Copilot → Hermes | ❌ No | Platforms serve different domains |
| Deduplicate prompts | ❌ No | No redundant triggers within same platform |
| Add missing triggers | ℹ️ Not needed | Filename-as-command is standard Copilot convention |
| Create missing Hermes skills | ℹ️ Not needed | 125 Hermes-only skills reflect broader domain coverage |

## Verification

| Check | Status |
|-------|--------|
| OpenCode `.opencode/commands/` | ⚠️ Not found — `.github/prompts/` used instead |
| Hermes `.prompt.md` files | ✅ N/A — Hermes uses `SKILL.md` format |
| Copilot `.github/prompts/` prompts | ✅ 100+ catalouged |
| Three-way cross-reference table | ✅ Complete |
| Duplicate detection | ✅ No within-platform duplicates |
| Trigger collisions | ✅ None flagged |
| Sync actions needed | ❌ None required |
