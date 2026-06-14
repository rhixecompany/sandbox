# Batch 15 Judge Results — Skills Audit Pipeline

**Date:** 2026-06-14
**Profile:** default
**Batch:** 15 (Skills 99-105, 6 skills — 1 missing)
**Judge Skill:** skill-judge v1.1.0

---

## Summary

| # | Skill | Score | Rating | Status |
|---|-------|-------|--------|--------|
| 99 | glab | 42/100 | ⚠️ Needs work | Minimal, no commands |
| 100 | hermes-profiles | 81/100 | ✅ AI-ready | 386 lines (needs split) |
| 101 | hermes-setup | 79/100 | ✅ AI-ready | 382 lines (needs split) |
| 102 | jira | 42/100 | ⚠️ Needs work | Minimal, no commands |
| 103 | kanban-orchestrator | 78/100 | ✅ AI-ready | Excellent decomposition |
| 104 | kanban-worker | 79/100 | ✅ AI-ready | Complete handoff patterns |
| 105 | hermes-skill-library-maintenance | — | **MISSING** | File not found |

**Aggregate:** 4/6 AI-ready, 2/6 Need work, 1/7 MISSING

---

## Detailed Evaluations

### 99. glab — 42/100 ⚠️

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 11 | Missing `version`, `license`, `author`, `tags` (has `category`, `title`) |
| Structure (20) | 8 | 4 phases, when to use/not, tools, best practices; no Skills Required, no pitfalls, generic verification |
| Content (20) | 12 | Minimal: high-level workflow, no concrete commands, no auth examples, no error handling |
| DRY (20) | 20 | 81 lines (<250), clean |
| References (20) | -9 | No reference files; mentions CLI/API URLs but not formal refs |

**Priority Fixes:**
- High: Fix frontmatter; add Skills Required, phased workflow with real commands, pitfalls, specific verification
- Medium: Add concrete CLI examples, error handling
- Low: Add reference files

---

### 100. hermes-profiles — 81/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 20 | All fields: name, title, description, version, author, license, platforms, metadata.tags, related_skills |
| Structure (20) | 20 | Excellent: DRY rules, provider enumeration (4 sources), system maintenance, toolsets, operator policies, personality |
| Content (20) | 20 | Excellent: USER.md/SOUL.md/MEMORY.md separation, provider assembly table, recovery table, verification script |
| DRY (20) | 18 | 386 lines (>250 → 18) |
| References (20) | 3 | Cites external docs but no internal reference files |

**Priority Fixes:**
- High: **Split to <250 lines** (move provider tables, recovery table, verification to references)
- Medium: Add reference files for provider assembly, maintenance, verification

---

### 101. hermes-setup — 79/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 20 | All fields: name, title, description, version, author, license, platforms, metadata.tags, related_skills |
| Structure (20) | 20 | Excellent: 5 phases, fast path verification, expected healthy output table, common issues, Windows notes |
| Content (20) | 20 | Excellent: provider table (11 providers), MCP servers (5 examples), toolsets (18), profiles, verification report template |
| DRY (20) | 18 | 382 lines (>250 → 18) |
| References (20) | 1 | No reference files mentioned |

**Priority Fixes:**
- High: **Split to <250 lines** (extract provider table, MCP config, toolsets, issues table to references)
- Medium: Add reference files

---

### 102. jira — 42/100 ⚠️

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 11 | Missing `version`, `license`, `author`, `tags` (has `category`, `title`) |
| Structure (20) | 8 | 4 phases, when to use/not, tools, best practices; no Skills Required, no pitfalls, generic verification |
| Content (20) | 12 | Minimal: high-level workflow, no CLI commands, no MCP integration details, no error handling |
| DRY (20) | 20 | 81 lines (<250), clean |
| References (20) | -9 | No reference files; mentions CLI/API but not formal |

**Priority Fixes (Critical):**
- High: Fix frontmatter; add Skills Required, phased workflow with real commands, pitfalls, specific verification
- Medium: Add concrete CLI/MCP examples, error handling
- Low: Add reference files

---

### 103. kanban-orchestrator — 78/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 20 | All fields: name, title, description, version, platforms, metadata.tags, related_skills |
| Structure (20) | 20 | Excellent: Step 0 (discover profiles), anti-temptation rules, 5-step decomposition, common patterns, pitfalls, recovery |
| Content (20) | 20 | Excellent: task graph examples with Python code, dependency linking, tenant inheritance, stuck worker recovery |
| DRY (20) | 18 | 228 lines (<250), clean |
| References (20) | -1 | Cites `os.environ.get("HERMES_TENANT")` but no reference files |

**Priority Fixes:**
- High: Add reference files

---

### 104. kanban-worker — 79/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 20 | All fields: name, title, description, version, platforms, metadata.tags, related_skills |
| Structure (20) | 20 | Excellent: workspace handling, tenant isolation, summary/metadata shapes, claim verification, block reasons, heartbeats, retries, notifications |
| Content (20) | 20 | Excellent: coding/research/review handoff patterns, created_cards gate, retry diagnostics, CLI fallback, DO NOT rules |
| DRY (20) | 20 | 230 lines (<250), clean |
| References (20) | -1 | No reference files mentioned |

**Priority Fixes:**
- High: Add reference files

---

### 105. hermes-skill-library-maintenance — **MISSING**

File not found: `C:\Users\Alexa\AppData\Local\hermes\skills\devops\hermes-skill-library-maintenance\SKILL.md`

This skill appears to have been removed during deduplication.

---

## Cross-Batch Patterns (All 102 Skills Tracked)

| Issue | Frequency (of 102) |
|-------|-------------------|
| No Skills Required table | 102/102 (100%) |
| No verification checklist | 94/102 (92%) |
| Missing `version` in frontmatter | 54/102 (53%) |
| Missing `license` in frontmatter | 52/102 (51%) |
| Missing `tags` in frontmatter | 56/102 (55%) |
| Missing `author` in frontmatter | 51/102 (50%) |
| No phased workflow | 31/102 (30%) |
| No pitfalls section | 42/102 (41%) |
| SKILL.md >250 lines | 18/102 (18%) |
| Orphaned/unverified reference files | 46/102 (45%) |

---

## Remediation Priority (All 102 Skills)

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
| 13 | **datadog** | 44 | Minimal, generic |
| 14 | **glab** | 42 | Minimal, no commands |
| 15 | **jira** | 42 | Minimal, no commands |
| 16 | **validate-memories** | 45 | No structure, no refs |
| 17 | **asdf** | 48 | Missing frontmatter, structure |
| 18 | **make-repo-contribution** | 51 | Frontmatter + structure broken |
| 19 | **content-research-writer** | 51 | Generic checklist, minimal |
| 20 | **customize-opencode** | 53 | Broken frontmatter, minimal |
| 21 | **skill-creator** | 49 | Frontmatter malformed, orphaned refs |
| 22 | **fabric-lakehouse** | 56 | Missing structure, no examples |
| 23 | **customization-audit** | 54 | **822 lines** |
| 24 | **azure-devops-cli** | 52 | **2,426 lines** |
| 25 | **hermes-profiles** | 81 | 386 lines (needs split) |
| 26 | **hermes-setup** | 79 | 382 lines (needs split) |
| 27 | **dependabot** | 80 | 459 lines (needs split) |

---

## Next Steps

Continue with remaining batches per plan:
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
