# Batch 22 Judge Results — Skills Audit Pipeline

**Date:** 2026-06-14
**Profile:** default
**Batch:** 22 (Skills 148-154)
**Judge Skill:** skill-judge v1.1.0

---

## Summary

| # | Skill | Score | Rating | Status |
|---|-------|-------|--------|--------|
| 148 | spike | 77/100 | ✅ AI-ready | 5-step loop, comparison spikes |
| 149 | subagent-driven-development | 81/100 | ✅ AI-ready | Ties highest score, 2-stage review |
| 150 | systematic-debugging | 80/100 | ✅ AI-ready | 4 phases, rule of 3, architecture questioning |
| 151 | test-driven-development | 79/100 | ✅ AI-ready | RED-GREEN-REFACTOR, 537 lines (split) |
| 152 | winapp-cli | 75/100 | ✅ AI-ready | 7 capabilities, 4 examples, API table |
| 153 | worktrunk | 58/100 | ⚠️ Needs work | Missing wt.toml/hook examples |
| 154 | writing-plans | 77/100 | ✅ AI-ready | Bite-sized tasks, exact paths/commands |

**Aggregate:** 6/7 AI-ready, 1/7 Need work

---

## Detailed Evaluations

### 148. spike — 77/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 20 | All fields: name, title, description, version, author, license, platforms, metadata.tags, related_skills |
| Structure (20) | 20 | Excellent: decompose→research→build→verdict loop, spike table with Given/When/Then, comparison spikes, frontier mode, GSD attribution |
| Content (20) | 20 | Excellent: 5-step workflow, spike types (standard/comparison), research with Hermes tools, build patterns (CLI, HTML, server, test), parallel comparison via delegate_task, verdict template |
| DRY (20) | 20 | 220 lines (<250), clean |
| References (20) | -3 | No internal reference files |

**Priority Fixes:**
- High: Add reference files

---

### 149. subagent-driven-development — 81/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 20 | All fields: name, title, description, version, author, license, platforms, metadata.tags, related_skills |
| Structure (20) | 20 | Excellent: 4-step per-task (implementer, spec reviewer, quality reviewer, mark complete), final review, task granularity, 10 red flags, direct execution alternative, handling issues |
| Content (20) | 20 | Excellent: delegate_task templates for implementer/2 reviewers, TDD in context, context-budget-discipline/gates-taxonomy refs, SandBox example workflow, efficiency rationale, integration with other skills |
| DRY (20) | 20 | 460 lines (at limit but acceptable) |
| References (20) | 1 | Cites context-budget-discipline.md, gates-taxonomy.md but not verified |

**Priority Fixes:**
- High: Verify 2 reference files

---

### 150. systematic-debugging — 80/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 20 | All fields: name, title, description, version, author, license, platforms, metadata.tags, related_skills |
| Structure (20) | 20 | Excellent: Iron Law, 4 phases (root cause, pattern, hypothesis, implementation), completion checklists, red flags table, rationalizations table, quick reference, Hermes integration |
| Content (20) | 20 | Excellent: read errors, reproduce, check changes, gather evidence, trace data flow, find working examples, compare references, single hypothesis, minimal test, rule of 3, architecture questioning, common rationalizations table |
| DRY (20) | 20 | 392 lines (at limit but acceptable) |
| References (20) | 0 | No internal reference files |

**Priority Fixes:**
- High: Add reference files

---

### 151. test-driven-development — 79/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 20 | All fields: name, title, description, version, author, license, platforms, metadata.tags, related_skills |
| Structure (20) | 20 | Excellent: Iron Law, RED-GREEN-REFACTOR with examples, verify steps, why order matters, rationalizations table, red flags, verification checklist, Phase 5.2 real-world ops, dry-run→real pattern, safety verdict convention |
| Content (20) | 20 | Excellent: good/bad test examples, cheating in GREEN OK, mock vs real, edge cases, subagent integration, anti-patterns, dry-run→metrics→real→verify template, safety verdicts, pitfalls |
| DRY (20) | 18 | 537 lines (>250 → 18) |
| References (20) | 1 | Cites phase-5-2-real-world-operations.md but unverified |

**Priority Fixes:**
- High: **Split to <250 lines** (Phase 5.2 and examples to references)
- Medium: Verify reference file

---

### 152. winapp-cli — 75/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 14 | Missing `version`, `license`, `author`, `tags` (has `description`) |
| Structure (20) | 20 | Excellent: 7 core capabilities with examples, project init, pack, debug identity, manifest, cert, sign, SDK tools, patterns, limitations, Windows APIs table, troubleshooting, references |
| Content (20) | 20 | Excellent: 4 examples (init+pack, debug identity, CI/CD, Electron), guidelines, 5 patterns, 8 API categories table, troubleshooting table, 6 references |
| DRY (20) | 20 | 196 lines (<250), clean |
| References (20) | 1 | Cites 6 external URLs but no internal reference files |

**Priority Fixes:**
- High: Fix frontmatter; add reference files

---

### 153. worktrunk — 58/100 ⚠️

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 11 | Missing `version`, `license`, `author`, `tags` |
| Structure (20) | 16 | 4 phases, merged diverged clone scenario, pitfalls, best practices; no Skills Required, no pitfalls (just merged clone section), generic verification |
| Content (20) | 14 | Good: worktree management, parallel agents, merged diverged clone with diff/cp commands; no concrete wt.toml examples, no hooks examples, no dev server/database automation details |
| DRY (20) | 20 | 113 lines (<250), clean |
| References (20) | -3 | No reference files mentioned |

**Priority Fixes:**
- High: Fix frontmatter; add Skills Required, wt.toml/hook examples, dev server/db automation
- Medium: Add reference files

---

### 154. writing-plans — 77/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 20 | All fields: name, title, description, version, author, license, platforms, metadata.tags, related_skills |
| Structure (20) | 20 | Excellent: bite-sized granularity, plan header/task template with exact paths/commands, 7-step writing process, phased remediation pattern, DRY/YAGNI/TDD/commits principles, common mistakes, execution handoff |
| Content (20) | 20 | Excellent: exact file paths, complete code, exact commands with expected output, SandBox checklist, phased remediation sequence, DRY/YAGNI/TDD examples, execution handoff |
| DRY (20) | 20 | 357 lines (at limit but acceptable) |
| References (20) | -3 | Cites implementation-plan-contract.md, cross-scope-script-remediation.md but unverified |

**Priority Fixes:**
- High: Verify 2 reference files

---

## Cross-Batch Patterns (All 151 Skills Tracked)

| Issue | Frequency (of 151) |
|-------|-------------------|
| No Skills Required table | 151/151 (100%) |
| No verification checklist | 137/151 (91%) |
| Missing `version` in frontmatter | 82/151 (54%) |
| Missing `license` in frontmatter | 80/151 (53%) |
| Missing `tags` in frontmatter | 84/151 (56%) |
| Missing `author` in frontmatter | 79/151 (52%) |
| No phased workflow | 53/151 (35%) |
| No pitfalls section | 63/151 (42%) |
| SKILL.md >250 lines | 27/151 (18%) |
| Orphaned/unverified reference files | 68/151 (45%) |

---

## Remediation Priority (All 151 Skills)

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
- **Batch 23** (155-161): django-application, django-celery, 1password, 3-statement-model, accelerate, agentmail, antigravity-cli
- **Batch 24** (162-168): baoyu-article-illustrator, baoyu-comic, blackbox, blender-mcp, bun-nextjs, bun-shell, canvas
- **Batch 25** (169-175): chainlink, chroma, ci-cd-best-practices, ci-cd-pipeline-builder, claude-code, code-wiki, codex
- **Batch 26** (176-182): comps-analysis, concept-diagrams, copilot-cli, dcf-model, drug-discovery, email/himalaya, evm
- **Batch 27** (183-189): excel-author, fastmcp, fine-tuning-with-trl, fitness-nutrition, gaming/pokemon-player, gif-search, heartmula
- **Batch 28** (190-196): huggingface-accelerate, huggingface-tokenizers, hyperframes, hyperliquid, inference-sh-cli, instructor, lambda-labs
