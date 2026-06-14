# Batch 17 Judge Results — Skills Audit Pipeline

**Date:** 2026-06-14
**Profile:** default
**Batch:** 17 (Skills 113-119)
**Judge Skill:** skill-judge v1.1.0

---

## Summary

| # | Skill | Score | Rating | Status |
|---|-------|-------|--------|--------|
| 113 | secret-scanning | 76/100 | ✅ AI-ready | 3 refs, push protection bypass |
| 114 | service-integrations | 75/100 | ✅ AI-ready | 8 services, bash escaping fix |
| 115 | session-audit-report | 68/100 | ⚠️ Needs work | Missing frontmatter, structure |
| 116 | snowflake-semanticview | 71/100 | ✅ AI-ready | 11-step workflow, temp validation |
| 117 | terraform-azurerm-set-diff-analyzer | 48/100 | ⚠️ Needs work | Minimal, unverified refs |
| 118 | webhook-subscriptions | 74/100 | ✅ AI-ready | --deliver-only, 5 patterns |
| 119 | windows-maintenance-operations | 78/100 | ✅ AI-ready | 5-phase, safety guardrails |

**Aggregate:** 5/7 AI-ready, 2/7 Need work

---

## Detailed Evaluations

### 113. secret-scanning — 76/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 14 | Missing `version`, `license`, `author`, `tags` (comprehensive `description`) |
| Structure (20) | 20 | Excellent: core workflows (enable, blocked pushes, custom patterns, alerts), pre-commit scanning, reference files |
| Content (20) | 20 | Excellent: availability table, push protection bypass options (A/B/C), custom patterns with Copilot, alert types, remediation priority |
| DRY (20) | 20 | 242 lines (<250), clean |
| References (20) | 2 | Cites 3 refs (push-protection.md, custom-patterns.md, alerts-and-remediation.md) |

**Priority Fixes:**
- High: Fix frontmatter; verify 3 reference files

---

### 114. service-integrations — 75/100 ✅

| Dimension | Score | Findings |
|---|---|---|
| Frontmatter (20) | 20 | All fields: name, title, description, version, platforms, metadata.tags, related_skills |
| Structure (20) | 20 | Excellent: architecture, prerequisites, setup, common patterns (action-dispatching, skills, delivery), bash escaping, batch setup, service-specific table, testing, troubleshooting |
| Content (20) | 20 | Excellent: prompt templates, 8 service table with events, bash escaping fix, delivery targets, phase workflow, verification checklist |
| DRY (20) | 20 | 239 lines (<250), clean |
| References (20) | -5 | No reference files mentioned |

**Priority Fixes:**
- High: Add reference files

---

### 115. session-audit-report — 68/100 ⚠️

| Dimension | Score | Findings |
|---|---|---|
| Frontmatter (20) | 11 | Missing `version`, `license`, `author`, `tags` |
| Structure (20) | 16 | 4 steps, report template, placeholder, pitfalls; no Skills Required, no phased workflow, generic verification |
| Content (20) | 16 | Good: session search, extraction, report template with tables, changelog section, pitfalls; no error handling, no examples |
| DRY (20) | 20 | 110 lines (<250), clean |
| References (20) | -5 | No reference files mentioned |

**Priority Fixes:**
- High: Fix frontmatter; add Skills Required, phased workflow, specific verification checklist, error handling
- Medium: Add concrete examples, reference files

---

### 116. snowflake-semanticview — 71/100 ✅

| Dimension | Score | Findings |
|---|---|---|
| Frontmatter (20) | 14 | Missing `version`, `license`, `author`, `tags` |
| Structure (20) | 20 | Excellent: 11-step workflow, synonyms/comments required, validation pattern, example CLI template |
| Content (20) | 20 | Excellent: DDL drafting, temp validation, star schema, synonyms from Snowflake comments, sample queries |
| DRY (20) | 20 | 82 lines (<250), clean |
| References (20) | -3 | No reference files mentioned |

**Priority Fixes:**
- High: Fix frontmatter; add reference files

---

### 117. terraform-azurerm-set-diff-analyzer — 48/100 ⚠️

| Dimension | Score | Findings |
|---|---|---|
| Frontmatter (20) | 14 | Missing `version`, `author`, `tags` (has `description`, `license`) |
| Structure (20) | 12 | Background, prerequisites, usage, troubleshooting, detailed docs; no phased workflow, no Skills Required, no pitfalls, no verification |
| Content (20) | 12 | Good: Set-type issue explanation, Python script, troubleshooting; no examples, no CI/CD integration |
| DRY (20) | 20 | 48 lines (<250), clean |
| References (20) | 0 | Cites `scripts/analyze_plan.py`, `scripts/README.md`, `references/azurerm_set_attributes.md` but unverified |

**Priority Fixes:**
- High: Fix frontmatter; add phased workflow, Skills Required, pitfalls, verification; verify 2 refs + script
- Medium: Add concrete examples, CI/CD integration

---

### 118. webhook-subscriptions — 74/100 ✅

| Dimension | Score | Findings |
|---|---|---|
| Frontmatter (20) | 20 | All fields: name, title, description, version, platforms, metadata.tags |
| Structure (20) | 20 | Excellent: setup (3 options), commands, prompt templates, 5 patterns (GitHub, Stripe, CI/CD, generic), direct delivery, security, how it works, troubleshooting |
| Content (20) | 20 | Excellent: dot-notation payload, --deliver-only for zero-LLM, HMAC auth, subscription persistence |
| DRY (20) | 20 | 243 lines (<250), clean |
| References (20) | -6 | No reference files mentioned |

**Priority Fixes:**
- High: Add reference files

---

### 119. windows-maintenance-operations — 78/100 ✅

| Dimension | Score | Findings |
|---|---|---|
| Frontmatter (20) | 17 | Missing `version`, `license` (has `title`, `author`, `trigger`, `description`, `tags`) |
| Structure (20) | 20 | Excellent: 5-phase workflow (discovery→preview→execute→validate→recovery), safety guardrails, common targets table, 6 pitfalls, quick reference |
| Content (20) | 20 | Excellent: dry-run/approval pattern, 0 bytes free detection, reversible/irreversible classification, recovery docs, before/after metrics |
| DRY (20) | 20 | 300 lines (at limit but clean) |
| References (20) | 1 | Mentions scripts (disk-analysis.ps1, cache-clean.sh, clean_dependency_folders.sh) but unverified |

**Priority Fixes:**
- High: Fix frontmatter (add `version`, `license`); verify 3 script files

---

## Cross-Batch Patterns (All 116 Skills Tracked)

| Issue | Frequency (of 116) |
|-------|-------------------|
| No Skills Required table | 116/116 (100%) |
| No verification checklist | 106/116 (91%) |
| Missing `version` in frontmatter | 62/116 (53%) |
| Missing `license` in frontmatter | 60/116 (52%) |
| Missing `tags` in frontmatter | 64/116 (55%) |
| Missing `author` in frontmatter | 59/116 (51%) |
| No phased workflow | 38/116 (33%) |
| No pitfalls section | 48/116 (41%) |
| SKILL.md >250 lines | 20/116 (17%) |
| Orphaned/unverified reference files | 53/116 (46%) |

---

## Remediation Priority (All 116 Skills)

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
| 16 | **terraform-azurerm-set-diff-analyzer** | 48 | Minimal, unverified refs |
| 17 | **glab** | 42 | Minimal, no commands |
| 18 | **jira** | 42 | Minimal, no commands |
| 19 | **validate-memories** | 45 | No structure, no refs |
| 20 | **asdf** | 48 | Missing frontmatter, structure |
| 21 | **make-repo-contribution** | 51 | Frontmatter + structure broken |
| 22 | **content-research-writer** | 51 | Generic checklist, minimal |
| 23 | **customize-opencode** | 53 | Broken frontmatter, minimal |
| 24 | **skill-creator** | 49 | Frontmatter malformed, orphaned refs |
| 25 | **fabric-lakehouse** | 56 | Missing structure, no examples |
| 26 | **projects-multi-repo-init-normalize** | 56 | Missing structure, no error handling |
| 27 | **customization-audit** | 54 | **822 lines** |
| 28 | **azure-devops-cli** | 52 | **2,426 lines** |

---

## Next Steps

Continue with remaining batches per plan:
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
