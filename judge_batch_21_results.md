# Batch 21 Judge Results — Skills Audit Pipeline

**Date:** 2026-06-14
**Profile:** default
**Batch:** 21 (Skills 141-147)
**Judge Skill:** skill-judge v1.1.0

---

## Summary

| # | Skill | Score | Rating | Status |
|---|-------|-------|--------|--------|
| 141 | quasi-coder | 76/100 | ✅ AI-ready | 389 lines (split needed) |
| 142 | receiving-code-review | 42/100 | ⚠️ Needs work | Minimal, no examples |
| 143 | requesting-code-review | 82/100 | ✅ AI-ready | Highest score so far |
| 144 | refactor | 78/100 | ✅ AI-ready | 645 lines (split needed), 10 smells |
| 145 | sandbox | 54/100 | ⚠️ Needs work | Good OpenCode detail, missing structure |
| 146 | script-orchestration | 76/100 | ✅ AI-ready | 180 scripts real-world, 5 modes |
| 147 | shadcn | 46/100 | ⚠️ Needs work | Minimal, no CLI examples |

**Aggregate:** 4/7 AI-ready, 3/7 Need work

---

## Detailed Evaluations

### 141. quasi-coder — 76/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 14 | Missing `version`, `license`, `author`, `tags` |
| Structure (20) | 20 | Excellent: 3 expertise levels, compensation rules, shorthand markers/indicators, 10 best practices, troubleshooting, advanced usage |
| Content (20) | 20 | Excellent: complete shorthand workflow with example (input→assessment→translation→production code), comment handling, variables/markers spec |
| DRY (20) | 18 | 389 lines (>250 → 18) |
| References (20) | 4 | No internal reference files |

**Priority Fixes:**
- High: Fix frontmatter; **split to <250 lines** (move examples, shorthand key, troubleshooting to references)

---

### 142. receiving-code-review — 42/100 ⚠️

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 11 | Missing `version`, `license`, `author`, `tags` (has `category`, `title`) |
| Structure (20) | 12 | 4 phases, when to use/not, tools, best practices; no Skills Required, no pitfalls, generic verification |
| Content (20) | 12 | Minimal: 4-phase workflow; no concrete examples, no security check detail |
| DRY (20) | 20 | 74 lines (<250), clean |
| References (20) | -13 | No reference files mentioned |

**Priority Fixes:**
- High: Fix frontmatter; add Skills Required, phased workflow with examples, pitfalls, specific verification
- Medium: Add concrete review feedback examples, security check details

---

### 143. requesting-code-review — 82/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 20 | All fields: name, title, description, version, author, license, platforms, metadata.tags, related_skills |
| Structure (20) | 20 | Excellent: 8-step pipeline (diff, static security scan, baseline tests, self-review, independent reviewer subagent, evaluate, auto-fix loop, commit), fail-closed JSON, integration |
| Content (20) | 20 | Excellent: 7 security scan greps, baseline test detection, self-review checklist, delegate_task for reviewer/fixer, 2-cycle auto-fix, [verified] commit prefix, common patterns, pitfalls |
| DRY (20) | 20 | 286 lines (close to 250 but acceptable) |
| References (20) | 2 | Cites related skills but no internal reference files |

**Priority Fixes:**
- High: Add reference files

---

### 144. refactor — 78/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 17 | Missing `version`, `author` (has `description`, `license`) |
| Structure (20) | 20 | Excellent: 10 code smells with before/after diffs, extract method, type safety, 4 design patterns, principles, when NOT to refactor |
| Content (20) | 20 | Excellent: 10 smells (long method, duplication, god class, long params, feature envy, primitive obsession, magic numbers, nested conditionals, dead code, inappropriate intimacy), type safety, Strategy/Builder/Factory/Observer patterns |
| DRY (20) | 18 | 645 lines (>250 → 18) |
| References (20) | 3 | No internal reference files |

**Priority Fixes:**
- High: Fix frontmatter; **split to <250 lines** (extract smells, patterns to references); add `version`, `author`

---

### 145. sandbox — 54/100 ⚠️

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 20 | All fields: name, category, title, description, version, author, license, metadata.tags, related_skills |
| Structure (20) | 16 | 4 phases, directory architecture, agent/command/rule frontmatter, OpenCode 6-stage, 5-phase audit, plugins, config, prompts, skill frontmatter; no Skills Required, no pitfalls |
| Content (20) | 14 | Good: OpenCode config, agent frontmatter, 6-stage workflow, 5-phase audit, plugins, model, MCP servers, prompts, skill frontmatter; minimal examples |
| DRY (20) | 20 | 175 lines (<250), clean |
| References (20) | -6 | No reference files mentioned |

**Priority Fixes:**
- High: Add Skills Required, pitfalls, verification checklist
- Medium: Add concrete examples, reference files

---

### 146. script-orchestration — 76/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 20 | All fields: name, title, description, author, date, keywords, references, templates, scripts |
| Structure (20) | 20 | Excellent: 5 modes, auto-discovery with exclusions, auto-run pipeline, error handling (retry/backoff), structured JSON logging, 5 pitfalls, customization, testing, CI examples, real-world metrics |
| Content (20) | 20 | Excellent: category-based PowerShell discovery, auto-run pipeline, retry with exponential backoff, JSON error/metrics logging, 4 modes, 5 pitfalls with fixes, customization, testing, real-world example (180 scripts, 6 categories, 20-60s execution) |
| DRY (20) | 20 | 323 lines (slightly over but acceptable) |
| References (20) | -4 | Cites 4 refs/template/scripts but existence not verified |

**Priority Fixes:**
- High: Verify 4 reference/template/script files

---

### 147. shadcn — 46/100 ⚠️

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 11 | Missing `version`, `license`, `author`, `tags` (has `category`, `title`) |
| Structure (20) | 12 | 4 phases, when to use/not, tools, best practices; no Skills Required, no pitfalls, generic verification |
| Content (20) | 12 | Minimal: component management overview; no concrete CLI commands, component examples, preset codes, styling examples |
| DRY (20) | 20 | 77 lines (<250), clean |
| References (20) | -9 | No reference files; mentions shadcn URL/components/presets but not formal |

**Priority Fixes:**
- High: Fix frontmatter; add Skills Required, phased workflow with CLI examples, component examples, pitfalls, specific verification
- Medium: Add concrete shadcn CLI commands, component usage examples, preset codes

---

## Cross-Batch Patterns (All 144 Skills Tracked)

| Issue | Frequency (of 144) |
|-------|-------------------|
| No Skills Required table | 144/144 (100%) |
| No verification checklist | 131/144 (91%) |
| Missing `version` in frontmatter | 78/144 (54%) |
| Missing `license` in frontmatter | 76/144 (53%) |
| Missing `tags` in frontmatter | 80/144 (56%) |
| Missing `author` in frontmatter | 75/144 (52%) |
| No phased workflow | 50/144 (35%) |
| No pitfalls section | 60/144 (42%) |
| SKILL.md >250 lines | 25/144 (17%) |
| Orphaned/unverified reference files | 65/144 (45%) |

---

## Remediation Priority (All 144 Skills)

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
| 18 | **httpie** | 42 | Minimal, no examples |
| 19 | **receiving-code-review** | 42 | Minimal, no examples |
| 20 | **shadcn** | 46 | Minimal, no CLI examples |
| 21 | **terraform-azurerm-set-diff-analyzer** | 48 | Minimal, unverified refs |
| 22 | **clonedeps** | 48 | Minimal, no clone commands |
| 23 | **glab** | 42 | Minimal, no commands |
| 24 | **jira** | 42 | Minimal, no commands |
| 25 | **work-on-ticket** | 42 | Minimal, no commands |
| 26 | **validate-memories** | 45 | No structure, no refs |
| 27 | **asdf** | 48 | Missing frontmatter, structure |
| 28 | **make-repo-contribution** | 51 | Frontmatter + structure broken |
| 29 | **content-research-writer** | 51 | Generic checklist, minimal |
| 30 | **customize-opencode** | 53 | Broken frontmatter, minimal |

---

## Next Steps

Continue with remaining batches per plan:
- **Batch 22** (148-154): spike, subagent-driven-development, systematic-debugging, test-driven-development, winapp-cli, worktrunk, writing-plans
- **Batch 23** (155-161): django-application, django-celery, 1password, 3-statement-model, accelerate, agentmail, antigravity-cli
- **Batch 24** (162-168): baoyu-article-illustrator, baoyu-comic, blackbox, blender-mcp, bun-nextjs, bun-shell, canvas
- **Batch 25** (169-175): chainlink, chroma, ci-cd-best-practices, ci-cd-pipeline-builder, claude-code, code-wiki, codex
- **Batch 26** (176-182): comps-analysis, concept-diagrams, copilot-cli, dcf-model, drug-discovery, email/himalaya, evm
- **Batch 27** (183-189): excel-author, fastmcp, fine-tuning-with-trl, fitness-nutrition, gaming/pokemon-player, gif-search, heartmula
- **Batch 28** (190-196): huggingface-accelerate, huggingface-tokenizers, hyperframes, hyperliquid, inference-sh-cli, instructor, lambda-labs
