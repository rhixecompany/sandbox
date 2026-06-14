# Batch 20 Judge Results — Skills Audit Pipeline

**Date:** 2026-06-14
**Profile:** default
**Batch:** 20 (Skills 134-140)
**Judge Skill:** skill-judge v1.1.0

---

## Summary

| # | Skill | Score | Rating | Status |
|---|-------|-------|--------|--------|
| 134 | hermes-s6-container-supervision | 81/100 | ✅ AI-ready | Highest score so far |
| 135 | httpie | 42/100 | ⚠️ Needs work | Minimal, no examples |
| 136 | mindstudio-wrapper | 78/100 | ✅ AI-ready | 7 patterns, 264 lines (split needed) |
| 137 | node-inspect-debugger | 79/100 | ✅ AI-ready | CDP driver, ui-tui debugging |
| 138 | nuget-manager | 71/100 | ✅ AI-ready | dotnet CLI workflow, central vs per-project |
| 139 | plan | 56/100 | ⚠️ Needs work | Missing Skills Required, pitfalls |
| 140 | project-docs | 76/100 | ✅ AI-ready | 11 artifacts, AI-readiness scoring |

**Aggregate:** 5/7 AI-ready, 2/7 Need work

---

## Detailed Evaluations

### 134. hermes-s6-container-supervision — 81/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 20 | All fields: name, title, description, version, author, license, metadata.tags, related_skills |
| Structure (20) | 20 | Excellent: 7-layer architecture diagram, key files table, Architecture B rationale (2 blockers), 8 quick recipes, 7 pitfalls |
| Content (20) | 20 | Excellent: cont-init.d phases, s6-rc.d static, /run/service runtime, CMD wrapper, PID 1 verification, s6-svc commands, boot log, static service addition, gateway run command, docker test harness |
| DRY (20) | 20 | 181 lines (<250), clean |
| References (20) | 1 | Mentions related skills but no reference files |

**Priority Fixes:**
- High: Add reference files

**Note:** Highest score in entire audit so far (81/100).

---

### 135. httpie — 42/100 ⚠️

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 11 | Missing `version`, `license`, `author`, `tags` (has `category`, `title`) |
| Structure (20) | 12 | 4 phases, when to use/not, tools, best practices; no Skills Required, no pitfalls, generic verification |
| Content (20) | 12 | Minimal: REST API testing overview; no concrete examples, no auth, no file upload, no error handling |
| DRY (20) | 20 | 76 lines (<250), clean |
| References (20) | -13 | No reference files; mentions HTTPie URL but not formal |

**Priority Fixes:**
- High: Fix frontmatter; add Skills Required, phased workflow with examples, pitfalls, specific verification
- Medium: Add concrete HTTPie examples (auth, file upload, headers)

---

### 136. mindstudio-wrapper — 78/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 20 | All fields: name, description, version, author, license, tags, metadata.tags, related_skills |
| Structure (20) | 20 | Excellent: prerequisites, 7 core patterns (text, image, search/research, batch, agent, OAuth, task), SDK ask tool, 10-category action reference, error handling, billing, verification checklist |
| Content (20) | 20 | Excellent: TypeScript code for all patterns, model selection, cost estimation, You.com research, 50-step batch, structured output, connector actions, autonomous task agent |
| DRY (20) | 18 | 264 lines (>250 → 18) |
| References (20) | -2 | Cites 4 external URLs but no internal reference files |

**Priority Fixes:**
- High: **Split to <250 lines** (move patterns/action reference to references)
- Medium: Add reference files for patterns

---

### 137. node-inspect-debugger — 79/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 20 | All fields: name, title, description, version, author, license, platforms, metadata.tags, related_skills |
| Structure (20) | 20 | Excellent: node inspect REPL table, attach to running process, programmatic CDP, Hermes ui-tui debugging (2 scenarios), Vitest under debugger, heap/CPU profiles, 7 common pitfalls, verification checklist, 3 one-shot recipes |
| Content (20) | 20 | Excellent: node inspect vs ndb, SIGUSR1 attach, chrome-remote-interface driver, dist/entry.js vs source, _SlashWorker/PTY are Python, source maps, port collisions, child processes, PTY mode, security |
| DRY (20) | 20 | 339 lines (slightly over but acceptable at limit) |
| References (20) | -1 | No reference files mentioned |

**Priority Fixes:**
- High: Add reference files

---

### 138. nuget-manager — 71/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 14 | Missing `version`, `license`, `author`, `tags` |
| Structure (20) | 20 | Excellent: core rules (never direct edit for add/remove, direct edit only for version), mandatory workflow, adding/removing/updating packages, examples |
| Content (20) | 20 | Excellent: dotnet CLI commands, version verification with jq/PowerShell, Directory.Packages.props vs .csproj, dotnet restore verification |
| DRY (20) | 20 | 64 lines (<250), clean |
| References (20) | -3 | No reference files mentioned |

**Priority Fixes:**
- High: Fix frontmatter; add reference files

---

### 139. plan — 56/100 ⚠️

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 20 | All fields: name, title, description, version, author, license, platforms, metadata.tags, related_skills |
| Structure (20) | 16 | 3 phases, core behavior, output requirements, save location, interaction style; no Skills Required, no pitfalls |
| Content (20) | 14 | Good: plan mode rules, output (goal, context, approach, steps, files, tests, risks), save location; no examples, no verification checklist |
| DRY (20) | 20 | 81 lines (<250), clean |
| References (20) | -8 | No reference files; mentions related skills but not formal |

**Priority Fixes:**
- High: Add Skills Required, pitfalls, verification checklist; add concrete plan example

---

### 140. project-docs — 76/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 14 | Missing `version`, `license`, `author`, `tags` |
| Structure (20) | 20 | Excellent: 5 phases (analyze, plan, generate, AI-readiness optimize, symmetry verify), 11-artifact generator-orchestrator table, support files |
| Content (20) | 20 | Excellent: AI-readiness scoring (6 criteria), frontmatter template, summary paragraphs, tagged code blocks, cross-references, wall-of-text penalty, 11 artifacts with purposes |
| DRY (20) | 20 | 103 lines (<250), clean |
| References (20) | 2 | Cites 4 support files (ai-readiness-criteria.md, template.md, repo-audit-notes.md, score-docs.py) |

**Priority Fixes:**
- High: Fix frontmatter; verify 4 support files + script

---

## Cross-Batch Patterns (All 137 Skills Tracked)

| Issue | Frequency (of 137) |
|-------|-------------------|
| No Skills Required table | 137/137 (100%) |
| No verification checklist | 125/137 (91%) |
| Missing `version` in frontmatter | 74/137 (54%) |
| Missing `license` in frontmatter | 72/137 (53%) |
| Missing `tags` in frontmatter | 76/137 (55%) |
| Missing `author` in frontmatter | 71/137 (52%) |
| No phased workflow | 47/137 (34%) |
| No pitfalls section | 57/137 (42%) |
| SKILL.md >250 lines | 23/137 (17%) |
| Orphaned/unverified reference files | 62/137 (45%) |

---

## Remediation Priority (All 137 Skills)

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
| 19 | **terraform-azurerm-set-diff-analyzer** | 48 | Minimal, unverified refs |
| 20 | **clonedeps** | 48 | Minimal, no clone commands |
| 21 | **glab** | 42 | Minimal, no commands |
| 22 | **jira** | 42 | Minimal, no commands |
| 23 | **work-on-ticket** | 42 | Minimal, no commands |
| 24 | **validate-memories** | 45 | No structure, no refs |
| 25 | **asdf** | 48 | Missing frontmatter, structure |
| 26 | **make-repo-contribution** | 51 | Frontmatter + structure broken |
| 27 | **content-research-writer** | 51 | Generic checklist, minimal |
| 28 | **customize-opencode** | 53 | Broken frontmatter, minimal |
| 29 | **skill-creator** | 49 | Frontmatter malformed, orphaned refs |
| 30 | **executing-plans** | 80 | 316 lines (needs split) |

---

## Next Steps

Continue with remaining batches per plan:
- **Batch 21** (141-147): quasi-coder, receiving-code-review, requesting-code-review, refactor, sandbox, script-orchestration, shadcn
- **Batch 22** (148-154): spike, subagent-driven-development, systematic-debugging, test-driven-development, winapp-cli, worktrunk, writing-plans
- **Batch 23** (155-161): django-application, django-celery, 1password, 3-statement-model, accelerate, agentmail, antigravity-cli
- **Batch 24** (162-168): baoyu-article-illustrator, baoyu-comic, blackbox, blender-mcp, bun-nextjs, bun-shell, canvas
- **Batch 25** (169-175): chainlink, chroma, ci-cd-best-practices, ci-cd-pipeline-builder, claude-code, code-wiki, codex
- **Batch 26** (176-182): comps-analysis, concept-diagrams, copilot-cli, dcf-model, drug-discovery, email/himalaya, evm
- **Batch 27** (183-189): excel-author, fastmcp, fine-tuning-with-trl, fitness-nutrition, gaming/pokemon-player, gif-search, heartmula
- **Batch 28** (190-196): huggingface-accelerate, huggingface-tokenizers, hyperframes, hyperliquid, inference-sh-cli, instructor, lambda-labs
