# Batch 13 Judge Results — Skills Audit Pipeline

**Date:** 2026-06-14
**Profile:** default
**Batch:** 13 (Skills 85-91)
**Judge Skill:** skill-judge v1.1.0

---

## Summary

| # | Skill | Score | Rating | Status |
|---|-------|-------|--------|--------|
| 85 | asdf | 48/100 | ⚠️ Needs work | Missing frontmatter, structure |
| 86 | aspire | 82/100 | ✅ AI-ready | Highest score so far, 9 refs |
| 87 | azure-deployment-preflight | 74/100 | ✅ AI-ready | 5-step validation, 3 refs |
| 88 | azure-devops-cli | 52/100 | ⚠️ Needs work | **2,426 lines**, critical split needed |
| 89 | azure-resource-visualizer | 76/100 | ✅ AI-ready | Detailed Mermaid workflow |
| 90 | azure-role-selector | 38/100 | ⚠️ Needs work | Minimal, single paragraph |
| 91 | azure-static-web-apps | 73/100 | ✅ AI-ready | Complete CLI reference |

**Aggregate:** 4/7 AI-ready, 3/7 Need work

---

## Detailed Evaluations

### 85. asdf — 48/100 ⚠️

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 11 | Missing `version`, `license`, `author`, `tags` |
| Structure (20) | 16 | 4 phases, when to use, best practices; no Skills Required, no pitfalls, no checklist |
| Content (20) | 14 | Good: install, config, usage, maintenance, 7 runtimes; no examples, no error handling |
| DRY (20) | 20 | 84 lines (<250), clean |
| References (20) | -3 | Mentions related skills but no reference files |

**Priority Fixes:**
- High: Fix frontmatter; add Skills Required, pitfalls, verification checklist
- Medium: Add concrete examples, error handling

---

### 86. aspire — 82/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 17 | Missing `version`, `license`, `author` (has `description`, references) |
| Structure (20) | 20 | Excellent: 8 sections, ref table, prerequisites, templates, quick start, CLI, patterns, URLs |
| Content (20) | 20 | Excellent: polyglot AppHost, C# examples, CLI commands, migration, MCP integration |
| DRY (20) | 20 | 238 lines (<250), clean |
| References (20) | 5 | 9 reference files cited (CLI, MCP, integrations, polyglot, architecture, dashboard, deployment, testing, troubleshooting) |

**Priority Fixes:**
- High: Fix frontmatter; verify/create 9 reference files in `references/`
- Medium: -

---

### 87. azure-deployment-preflight — 74/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 14 | Missing `version`, `license`, `author`, `tags` |
| Structure (20) | 20 | Excellent: 5-step validation, scope detection, fallback, report template, error handling, tools |
| Content (20) | 20 | Excellent: detailed commands for azd/az, validation levels, parameter detection, examples |
| DRY (20) | 20 | 222 lines (<250), clean |
| References (20) | -3 | Cites 3 refs (VALIDATION-COMMANDS.md, REPORT-TEMPLATE.md, ERROR-HANDLING.md) but dir not verified |

**Priority Fixes:**
- High: Fix frontmatter; verify/create 3 reference files

---

### 88. azure-devops-cli — 52/100 ⚠️

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 11 | Missing `version`, `license`, `author`, `tags` |
| Structure (20) | 16 | CLI structure, auth, projects, repos, PRs, pipelines, builds; no Skills Required, no pitfalls, no checklist |
| Content (20) | 20 | Excellent: 2,426 lines of comprehensive command reference |
| DRY (20) | 0 | **2,426 lines** (massive, >250 → 0 capped) |
| References (20) | -5 | No reference files mentioned |

**Priority Fixes (Critical):**
- High: Fix frontmatter; **split to <250 lines** (extract command tables to references); add pitfalls, checklist
- Medium: Create reference files for command tables

---

### 89. azure-resource-visualizer — 76/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 17 | Has `license` (LICENSE.txt), `metadata.author`; missing `version`, `tags` |
| Structure (20) | 20 | Excellent: 4-step workflow, diagram guidelines, quality standards, edge cases, output format |
| Content (20) | 20 | Excellent: Mermaid templates, subgraph guidance, resource type examples, constraints, success criteria |
| DRY (20) | 20 | 240 lines (<250), clean |
| References (20) | -1 | Cites `assets/template-architecture.md` but existence not verified |

**Priority Fixes:**
- High: Fix frontmatter (add `version`, `tags`); verify `assets/template-architecture.md` exists

---

### 90. azure-role-selector — 38/100 ⚠️

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 8 | Missing `version`, `license`, `author`, `tags` (has `allowed-tools` non-standard) |
| Structure (20) | 4 | No phased workflow, no Skills Required, no pitfalls, no verification checklist |
| Content (20) | 8 | Minimal: single paragraph describing tool usage, no examples, no error handling |
| DRY (20) | 20 | 19 lines (<250), clean |
| References (20) | -2 | No reference files mentioned |

**Priority Fixes (Critical):**
- High: Fix frontmatter; add phased workflow, Skills Required, pitfalls, verification checklist
- Medium: Add concrete examples, error handling

---

### 91. azure-static-web-apps — 73/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 11 | Missing `version`, `license`, `author`, `tags` |
| Structure (20) | 20 | Excellent: install, quick start, CLI vs runtime config, command ref, scenarios, troubleshooting |
| Content (20) | 20 | Excellent: `swa init` requirement, frameworks, API runtimes, GitHub Actions workflow, debug |
| DRY (20) | 20 | 330 lines (slightly over) |
| References (20) | -2 | No reference files mentioned |

**Priority Fixes:**
- High: Fix frontmatter
- Medium: Split to <250 lines (move scenarios/troubleshooting to references)

---

## Cross-Batch Patterns (All 89 Skills Tracked)

| Issue | Frequency (of 89) |
|-------|-------------------|
| No Skills Required table | 89/89 (100%) |
| No verification checklist | 82/89 (92%) |
| Missing `version` in frontmatter | 46/89 (52%) |
| Missing `license` in frontmatter | 44/89 (49%) |
| Missing `tags` in frontmatter | 48/89 (54%) |
| Missing `author` in frontmatter | 43/89 (48%) |
| No phased workflow | 24/89 (27%) |
| No pitfalls section | 35/89 (39%) |
| SKILL.md >250 lines | 14/89 (16%) |
| Orphaned/unverified reference files | 38/89 (43%) |

---

## Remediation Priority (All 89 Skills)

| Priority | Skill | Score | Critical Issues |
|----------|-------|-------|-----------------|
| 1 | **template** | 35 | Placeholder text, no structure, must be exemplary |
| 2 | **ai-prompt-engineering-safety-review** | 22 | Pure placeholder — rewrite |
| 3 | **context-map** | 21 | Pure placeholder — rewrite |
| 4 | **convert-plaintext-to-md** | 21 | Pure placeholder — rewrite |
| 5 | **skills** | 21 | Pure placeholder — rewrite |
| 6 | **create-readme** | 38 | Minimal, no structure |
| 7 | **vscode-ext-commands** | 38 | Minimal, no structure |
| 8 | **azure-role-selector** | 38 | Minimal, single paragraph |
| 9 | **vscode-ext-localization** | 39 | Minimal, no structure |
| 10 | **folder-structure-blueprint-generator** | 41 | Template-in-skill-body, no structure |
| 11 | **architecture-blueprint-generator** | 42 | Template-in-skill-body, no structure |
| 12 | **technology-stack-blueprint-generator** | 44 | Template-in-skill-body, no structure |
| 13 | **validate-memories** | 45 | No structure, no refs |
| 14 | **asdf** | 48 | Missing frontmatter, structure |
| 15 | **make-repo-contribution** | 51 | Frontmatter + structure broken |
| 16 | **content-research-writer** | 51 | Generic checklist, minimal content |
| 17 | **customize-opencode** | 53 | Broken frontmatter, minimal content |
| 18 | **skill-creator** | 49 | Frontmatter malformed, orphaned refs |
| 19 | **azure-devops-cli** | 52 | **2,426 lines**, critical split |

---

## Next Steps

Continue with remaining batches per plan:
- **Batch 14** (92-98): customization-audit, datadog, dependabot, entra-agent-user, fabric-lakehouse, git-history-preserving-migration, github-actions-efficiency
- **Batch 15** (99-105): glab, hermes-profiles, hermes-setup, hermes-skill-library-maintenance, jira, kanban-orchestrator, kanban-worker
- **Batch 16** (106-112): log-analysis-and-triage, multi-stage-dockerfile, parallel-cli, powerbi-modeling, projects-multi-repo-init-normalize, provider-reliability-diagnostics, rbac-audit-logging
- **Batch 17** (113-119): secret-scanning, service-integrations, session-audit-report, snowflake-semanticview, terraform-azurerm-set-diff-analyzer, webhook-subscriptions, windows-maintenance-operations
- **Batch 18** (120-126): work-on-ticket, workspace-audit, banking, bash-scripts-audit-remediation, caveman-unified, claude-api, clonedeps
- **Batch 19** (127-133): code-docs, codemap, context7, debugging-hermes-tui-commands, executing-plans, fluentui-blazor, hermes-agent-skill-authoring
- **Batch 20** (134-140): hermes-s6-container-supervision, httpie, mindstudio-wrapper, node-inspect-debugger, nuget-manager, plan, project-docs
- **Batch 21** (141-147): quasi-coder, receiving-code-review, requesting-code-review, refactor, sandbox, script-orchestration, shadcn
- **Batch 22** (148-154): spike, subagent-driven-development, systematic-debugging, test-driven-development, winapp-cli, worktrunk, writing-plans
- **Batch 23** (155-161): django-application, django-celery, 1password, 3-statement-model, accelerate, agentmail, antigravity-cli
- **Batch 24** (162-168): baoyu-article-illustrator, baoyu-comic, blackbox, blender-mcp, bun-nextjs, bun-shell, canvas
- **Batch 25** (169-175): chainlink, chroma, ci-cd-best-practices, ci-cd-pipeline-builder, claude-code, code-wiki, codex
- **Batch 26** (176-182): comps-analysis, concept-diagrams, copilot-cli, dcf-model, drug-discovery, email/himalaya, evm
- **Batch 27** (183-189): excel-author, fastmcp, fine-tuning-with-trl, fitness-nutrition, gaming/pokemon-player, gif-search, heartmula
- **Batch 28** (190-196): huggingface-accelerate, huggingface-tokenizers, hyperframes, hyperliquid, inference-sh-cli, instructor, lambda-labs
