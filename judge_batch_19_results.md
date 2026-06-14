# Batch 19 Judge Results — Skills Audit Pipeline

**Date:** 2026-06-14
**Profile:** default
**Batch:** 19 (Skills 127-133)
**Judge Skill:** skill-judge v1.1.0

---

## Summary

| # | Skill | Score | Rating | Status |
|---|-------|-------|--------|--------|
| 127 | code-docs | 42/100 | ⚠️ Needs work | Minimal, no examples |
| 128 | codemap | 42/100 | ⚠️ Needs work | Minimal, no output format |
| 129 | context7 | 71/100 | ✅ AI-ready | MCP config, tools table |
| 130 | debugging-hermes-tui-commands | 76/100 | ✅ AI-ready | 3-layer arch, 5 issues, verification |
| 131 | executing-plans | 80/100 | ✅ AI-ready | 316 lines, bulk sweeps, MSYS pitfalls |
| 132 | fluentui-blazor | 78/100 | ✅ AI-ready | 10 critical rules, all with code |
| 133 | hermes-agent-skill-authoring | 77/100 | ✅ AI-ready | In-repo vs user-local, validator |

**Aggregate:** 5/7 AI-ready, 2/7 Need work

---

## Detailed Evaluations

### 127. code-docs — 42/100 ⚠️

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 11 | Missing `version`, `license`, `author`, `tags` (has `category`, `title`) |
| Structure (20) | 12 | 4 phases, when to use/not, tools, best practices; no Skills Required, no pitfalls, generic verification |
| Content (20) | 12 | Minimal: Google Style overview, docstring conventions; no concrete examples, no Terraform/Go specifics |
| DRY (20) | 20 | 82 lines (<250), clean |
| References (20) | -13 | No reference files; mentions external guides but not formal |

**Priority Fixes:**
- High: Fix frontmatter; add Skills Required, phased workflow with examples, pitfalls, specific verification
- Medium: Add concrete Python/Go/Terraform docstring examples

---

### 128. codemap — 42/100 ⚠️

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 11 | Missing `version`, `license`, `author`, `tags` (has `category`, `title`) |
| Structure (20) | 12 | 4 phases, when to use/not, tools, best practices; no Skills Required, no pitfalls, generic verification |
| Content (20) | 12 | Minimal: scan/build hierarchy/document/generate; no concrete tree examples, no Mermaid diagram examples, no output format |
| DRY (20) | 20 | 78 lines (<250), clean |
| References (20) | -13 | No reference files mentioned |

**Priority Fixes:**
- High: Fix frontmatter; add Skills Required, phased workflow with examples, pitfalls, specific verification
- Medium: Add concrete tree/ASCII/Mermaid examples, output format

---

### 129. context7 — 71/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 14 | Missing `version`, `license`, `author`, `tags` |
| Structure (20) | 20 | Excellent: 4 phases, prerequisites, config, testing, available tools table, when to use/not, best practices |
| Content (20) | 20 | Excellent: MCP config, API key handling, literal key string warning, resolve/query tools, version-specific queries |
| DRY (20) | 20 | 112 lines (<250), clean |
| References (20) | -3 | No reference files mentioned |

**Priority Fixes:**
- High: Fix frontmatter; add reference files

---

### 130. debugging-hermes-tui-commands — 76/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 20 | All fields: name, title, description, version, author, license, platforms, metadata.tags, related_skills |
| Structure (20) | 20 | Excellent: 3-layer arch, 4 investigation steps, fix for missing autocomplete, 5 common issues, debugging tactics, 6 pitfalls, 5-step verification |
| Content (20) | 20 | Excellent: Python registry, gateway, Ink frontend, CommandDef, cli_only/gateway_only, subcommands, aliases, nanostore patching, rebuild requirement |
| DRY (20) | 20 | 157 lines (<250), clean |
| References (20) | -4 | No reference files mentioned |

**Priority Fixes:**
- High: Add reference files

---

### 131. executing-plans — 80/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 14 | Missing `version`, `license`, `author`, `tags` (has comprehensive `tags`) |
| Structure (20) | 20 | Excellent: 4 phases, auto-advance, batch ≤7, patch-first, artifact-driven, bulk sweeps (execute_code + sed), multi-pattern, cross-project, resumability, cross-platform remediation, verification independence |
| Content (20) | 20 | Excellent: Python bulk sweep template, sed fallback, drift detection (shebangs, error handling, ShellCheck, versions, exit codes), MSYS pitfalls, shared log rotation, modular refactoring (8 modules, 85% reduction), verification independence |
| DRY (20) | 18 | 316 lines (>250 → 18) |
| References (20) | 8 | Cites 2 refs (codebase-remediation-patterns.md, cross-scope-script-remediation.md) |

**Priority Fixes:**
- High: Fix frontmatter; **split to <250 lines** (extract bulk sweep, cross-platform, verification to refs); verify 2 refs

---

### 132. fluentui-blazor — 78/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 17 | Missing `version`, `license`, `author` (has `description`, `metadata`) |
| Structure (20) | 20 | Excellent: 10 critical rules (providers, services, icons, list binding, autocomplete, dialog, toast, design tokens, FluentEditForm), each with code examples |
| Content (20) | 20 | Excellent: provider list, service registration with ServiceLifetime, icon pattern (Icons.Variant.Size.Name), OptionText/OptionValue, ValueText, IDialogContentComponent, IToastService, OnAfterRenderAsync, FluentEditForm vs EditForm |
| DRY (20) | 20 | 235 lines (<250), clean |
| References (20) | 1 | Cites 4 refs (SETUP.md, LAYOUT-AND-NAVIGATION.md, DATAGRID.md, THEMING.md) |

**Priority Fixes:**
- High: Fix frontmatter (add `version`, `license`, `author`); verify 4 reference files

---

### 133. hermes-agent-skill-authoring — 77/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 20 | All fields: name, title, description, version, author, license, platforms, metadata.tags, related_skills |
| Structure (20) | 20 | Excellent: 2 locations (user-local vs in-repo), required frontmatter (name, description ≤1024), size limits (100k), peer-matched structure, directory placement, workflow, cross-referencing, editing, recategorizing, linked references |
| Content (20) | 20 | Excellent: validator constraints from skill_manager_tool.py, category from directory not frontmatter, user-local vs in-repo resolution, related_skills union, patch/write_file for edits, move + category frontmatter for recategorizing |
| DRY (20) | 20 | 159 lines (<250), clean |
| References (20) | -3 | Cites 3 refs but existence not verified |

**Priority Fixes:**
- High: Verify 3 reference files

---

## Cross-Batch Patterns (All 130 Skills Tracked)

| Issue | Frequency (of 130) |
|-------|-------------------|
| No Skills Required table | 130/130 (100%) |
| No verification checklist | 119/130 (92%) |
| Missing `version` in frontmatter | 70/130 (54%) |
| Missing `license` in frontmatter | 68/130 (52%) |
| Missing `tags` in frontmatter | 72/130 (55%) |
| Missing `author` in frontmatter | 67/130 (52%) |
| No phased workflow | 44/130 (34%) |
| No pitfalls section | 54/130 (42%) |
| SKILL.md >250 lines | 22/130 (17%) |
| Orphaned/unverified reference files | 59/130 (45%) |

---

## Remediation Priority (All 130 Skills)

| Priority | Skill | Score | Critical Issues |
|----------|-------|-------|-----------------|
| 1 | **template** | 35 | Placeholder text, no structure, must be exemplary |
| 2 | **ai-prompt-engineering-safety-review** | 22 | Pure placeholder — rewrite |
| 3 | **context-map** | 21 | Pure placeholder — rewrite |
| 4 | **convert-plaintext-to-md** | 21 | Pure placeholder — rewrite |
| 5 | **skills** | 21 | Pure placeholder — rewrite |
| 6 | **rbac-audit-logging** | 18 | Pure placeholder — rewrite |
| 7 | **create-readme** | 38 | Minimal, no structure |
| 8 | **vscode-ext-commands** | 38 | Minimal, no structure |
| 9 | **azure-role-selector** | 38 | Minimal, single paragraph |
| 10 | **vscode-ext-localization** | 39 | Minimal, no structure |
| 11 | **folder-structure-blueprint-generator** | 41 | Template-in-skill-body, no structure |
| 12 | **architecture-blueprint-generator** | 42 | Template-in-skill-body, no structure |
| 13 | **technology-stack-blueprint-generator** | 44 | Template-in-skill-body, no structure |
| 14 | **datadog** | 44 | Minimal, generic |
| 15 | **multi-stage-dockerfile** | 44 | Minimal, no examples |
| 16 | **code-docs** | 42 | Minimal, no examples |
| 17 | **codemap** | 42 | Minimal, no output format |
| 18 | **terraform-azurerm-set-diff-analyzer** | 48 | Minimal, unverified refs |
| 19 | **clonedeps** | 48 | Minimal, no clone commands |
| 20 | **glab** | 42 | Minimal, no commands |
| 21 | **jira** | 42 | Minimal, no commands |
| 22 | **work-on-ticket** | 42 | Minimal, no commands |
| 23 | **validate-memories** | 45 | No structure, no refs |
| 24 | **asdf** | 48 | Missing frontmatter, structure |
| 25 | **make-repo-contribution** | 51 | Frontmatter + structure broken |
| 26 | **content-research-writer** | 51 | Generic checklist, minimal |
| 27 | **customize-opencode** | 53 | Broken frontmatter, minimal |
| 28 | **skill-creator** | 49 | Frontmatter malformed, orphaned refs |
| 29 | **executing-plans** | 80 | 316 lines (needs split) |
| 30 | **bash-scripts-audit-remediation** | 79 | 281 lines (needs split) |

---

## Next Steps

Continue with remaining batches per plan:
- **Batch 20** (134-140): hermes-s6-container-supervision, httpie, mindstudio-wrapper, node-inspect-debugger, nuget-manager, plan, project-docs
- **Batch 21** (141-147): quasi-coder, receiving-code-review, requesting-code-review, refactor, sandbox, script-orchestration, shadcn
- **Batch 22** (148-154): spike, subagent-driven-development, systematic-debugging, test-driven-development, winapp-cli, worktrunk, writing-plans
- **Batch 23** (155-161): django-application, django-celery, 1password, 3-statement-model, accelerate, agentmail, antigravity-cli
- **Batch 24** (162-168): baoyu-article-illustrator, baoyu-comic, blackbox, blender-mcp, bun-nextjs, bun-shell, canvas
- **Batch 25** (169-175): chainlink, chroma, ci-cd-best-practices, ci-cd-pipeline-builder, claude-code, code-wiki, codex
- **Batch 26** (176-182): comps-analysis, concept-diagrams, copilot-cli, dcf-model, drug-discovery, email/himalaya, evm
- **Batch 27** (183-189): excel-author, fastmcp, fine-tuning-with-trl, fitness-nutrition, gaming/pokemon-player, gif-search, heartmula
- **Batch 28** (190-196): huggingface-accelerate, huggingface-tokenizers, hyperframes, hyperliquid, inference-sh-cli, instructor, lambda-labs
