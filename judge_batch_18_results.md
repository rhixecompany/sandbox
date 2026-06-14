# Batch 18 Judge Results — Skills Audit Pipeline

**Date:** 2026-06-14
**Profile:** default
**Batch:** 18 (Skills 120-126)
**Judge Skill:** skill-judge v1.1.0

---

## Summary

| # | Skill | Score | Rating | Status |
|---|-------|-------|--------|--------|
| 120 | work-on-ticket | 42/100 | ⚠️ Needs work | Minimal, no commands |
| 121 | workspace-audit | 76/100 | ✅ AI-ready | Batch scan, 5 reports, REST/GraphQL diff |
| 122 | banking | 58/100 | ⚠️ Needs work | Good practices, no code examples |
| 123 | bash-scripts-audit-remediation | 79/100 | ✅ AI-ready | 281 lines, 22 refs, wrapper norm |
| 124 | caveman-unified | 54/100 | ⚠️ Needs work | Missing frontmatter, no wenyan |
| 125 | claude-api | 56/100 | ⚠️ Needs work | No SDK examples, no cache_control |
| 126 | clonedeps | 48/100 | ⚠️ Needs work | Minimal, no clone commands |

**Aggregate:** 2/7 AI-ready, 5/7 Need work

---

## Detailed Evaluations

### 120. work-on-ticket — 42/100 ⚠️

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 11 | Missing `version`, `license`, `author`, `tags` (has `category`, `title`) |
| Structure (20) | 8 | 4 phases, when to use/not, tools, best practices; no Skills Required, no pitfalls, generic verification |
| Content (20) | 12 | Minimal: high-level workflow, no Jira CLI commands, no git commands, no error handling |
| DRY (20) | 20 | 82 lines (<250), clean |
| References (20) | -9 | No reference files; mentions related skills but not formal |

**Priority Fixes:**
- High: Fix frontmatter; add Skills Required, phased workflow with real commands, pitfalls, specific verification
- Medium: Add concrete Jira/git commands, error handling
- Low: Add reference files

---

### 121. workspace-audit — 76/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 20 | All fields: name, title, description, version, author, license, platforms, metadata.tags, related_skills |
| Structure (20) | 20 | Excellent: technique with execute_code, gh API field names table, ignore file scanning, batch scan loops, submodule dirty state, doc refresh workflow |
| Content (20) | 20 | Excellent: Python batch scan, bash loops, REST vs GraphQL diff, submodule recursion, dirty state categorization, 5 standard report files |
| DRY (20) | 20 | 197 lines (<250), clean |
| References (20) | -4 | No reference files mentioned |

**Priority Fixes:**
- High: Add reference files

---

### 122. banking — 58/100 ⚠️

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 20 | All fields: name, title, description, version, author, license, metadata.tags, related_skills |
| Structure (20) | 16 | 4 phases, when to use/not, tools, best practices; no Skills Required, no pitfalls |
| Content (20) | 14 | Good: tech stack, idempotency, soft deletes, transaction safety, Plaid/Dwolla; no concrete code examples, no error handling for payment failures |
| DRY (20) | 20 | 110 lines (<250), clean |
| References (20) | -2 | No reference files mentioned |

**Priority Fixes:**
- High: Add Skills Required, pitfalls, verification checklist
- Medium: Add concrete API route examples, idempotency implementation patterns
- Low: Add reference files

---

### 123. bash-scripts-audit-remediation — 79/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 14 | Missing `version`, `license`, `author`, `tags` |
| Structure (20) | 20 | Excellent: 5-phase + 6-phase migration, priority 1 safety audit, utility-first pattern, wrapper normalization, batch workflow, 25 pitfalls |
| Content (20) | 20 | Excellent: 7-file batches, shellcheck/PowerShell fixes, TypeScript migration, 20+ reference files, cross-platform wrapper standardization |
| DRY (20) | 18 | 281 lines (>250 → 18) |
| References (20) | 7 | Cites 22 reference files |

**Priority Fixes:**
- High: Fix frontmatter; **split to <250 lines** (extract reference tables); verify 22 reference files
- Medium: -

---

### 124. caveman-unified — 54/100 ⚠️

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 11 | Missing `version`, `license`, `author`, `tags` (has `category`, `title`) |
| Structure (20) | 16 | 3 phases, 4 compression levels, 3 specialized domains, tools, best practices, examples; no Skills Required, no pitfalls |
| Content (20) | 16 | Good: lite/full/ultra/wenyan levels, commit/compress/review domains, before/after example; no wenyan examples, no edge case handling |
| DRY (20) | 20 | 146 lines (<250), clean |
| References (20) | -9 | No reference files mentioned |

**Priority Fixes:**
- High: Fix frontmatter; add Skills Required, pitfalls, wenyan examples
- Medium: Add reference files

---

### 125. claude-api — 56/100 ⚠️

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 20 | All fields: name, title, description, version, author, license, metadata.tags, related_skills |
| Structure (20) | 16 | 4 phases, when to use/not, tools, best practices; no Skills Required, no pitfalls, generic verification |
| Content (20) | 14 | Good: model selection, prompt caching, caching verification, migration; no concrete SDK code examples, no cache_control block examples |
| DRY (20) | 20 | 92 lines (<250), clean |
| References (20) | -4 | No reference files mentioned |

**Priority Fixes:**
- High: Add Skills Required, pitfalls, verification checklist
- Medium: Add concrete SDK code examples, cache_control block patterns
- Low: Add reference files

---

### 126. clonedeps — 48/100 ⚠️

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 11 | Missing `version`, `license`, `author`, `tags` |
| Structure (20) | 12 | 4 phases, when to use/not, tools, best practices; no Skills Required, no pitfalls, generic verification |
| Content (20) | 12 | Minimal: high-level workflow, no concrete clone commands, no .gitignore patterns, no version pinning examples |
| DRY (20) | 20 | 79 lines (<250), clean |
| References (20) | -7 | No reference files mentioned |

**Priority Fixes:**
- High: Fix frontmatter; add Skills Required, phased workflow with real commands, pitfalls, specific verification
- Medium: Add concrete git clone/submodule commands, .gitignore patterns, version tagging
- Low: Add reference files

---

## Cross-Batch Patterns (All 123 Skills Tracked)

| Issue | Frequency (of 123) |
|-------|-------------------|
| No Skills Required table | 123/123 (100%) |
| No verification checklist | 113/123 (92%) |
| Missing `version` in frontmatter | 66/123 (54%) |
| Missing `license` in frontmatter | 64/123 (52%) |
| Missing `tags` in frontmatter | 68/123 (55%) |
| Missing `author` in frontmatter | 63/123 (51%) |
| No phased workflow | 41/123 (33%) |
| No pitfalls section | 51/123 (41%) |
| SKILL.md >250 lines | 21/123 (17%) |
| Orphaned/unverified reference files | 56/123 (46%) |

---

## Remediation Priority (All 123 Skills)

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
| 17 | **clonedeps** | 48 | Minimal, no clone commands |
| 18 | **glab** | 42 | Minimal, no commands |
| 19 | **jira** | 42 | Minimal, no commands |
| 20 | **work-on-ticket** | 42 | Minimal, no commands |
| 21 | **validate-memories** | 45 | No structure, no refs |
| 22 | **asdf** | 48 | Missing frontmatter, structure |
| 23 | **make-repo-contribution** | 51 | Frontmatter + structure broken |
| 24 | **content-research-writer** | 51 | Generic checklist, minimal |
| 25 | **customize-opencode** | 53 | Broken frontmatter, minimal |
| 26 | **skill-creator** | 49 | Frontmatter malformed, orphaned refs |
| 27 | **fabric-lakehouse** | 56 | Missing structure, no examples |
| 28 | **projects-multi-repo-init-normalize** | 56 | Missing structure, no error handling |
| 29 | **customization-audit** | 54 | **822 lines** |
| 30 | **azure-devops-cli** | 52 | **2,426 lines** |

---

## Next Steps

Continue with remaining batches per plan:
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
