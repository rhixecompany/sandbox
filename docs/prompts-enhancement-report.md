---
title: Prompt Library Enhancement Report
description: Comprehensive triage and enhancement recommendations for .github/prompts/ and Prompts/ directories
generated: 2026-05-30
tools:
  - acpx qwen exec — Batch text processing
  - acpx opencode exec — Structured prompt analysis
  - hermes skills list — 176 skills inventoried
  - hermes tools list — 26 toolsets (20 enabled, 6 disabled)
---

# Prompt Library Enhancement Report

## Executive Summary

- **124 prompt files** in `.github/prompts/`
- **8 operational prompt files** in `Prompts/`
- **7 trigger-enabled prompts** in `.github/prompts/` (have `/trigger` declarations)
- **117 prompts** missing explicit trigger declarations (94% gap)
- **176 Hermes skills** available, **26 Hermes toolsets** (20 enabled)
- **3 ACPX agents** available: Copilot CLI, Qwen Code, OpenCode

### Key Findings

1. **Trigger coverage is minimal** — only 7/124 prompts define a `/trigger` in frontmatter
2. **Description quality varies** — many prompts lack clear, concise descriptions
3. **Skills cross-references are incomplete** — Prompts/*.md reference ~8 skills each but many more are available
4. **Tool integration is implicit** — most prompts don't declare tool requirements in frontmatter
5. **Hermes ACPX integration** — most prompts don't reference ACPX agents even though they're usable
6. **suggest-awesome-* series** — 4 prompts provide valuable external skill/agent/prompt discovery

---

## Section 1: Triage — All .github/prompts/ Triggers

### Prompts WITH Triggers (need to be activated/registered)

| # | Trigger | Filename | Status |
|---|---------|----------|--------|
| 1 | `/ai-prompt-engineering-safety-review` | ai-prompt-engineering-safety-review.prompt.md | ✅ Trigger defined |
| 2 | `/boost-prompt` | boost-prompt.prompt.md | ✅ Trigger defined |
| 3 | `/context-map` | context-map.prompt.md | ✅ Trigger defined |
| 4 | `/convert-plaintext-to-md` | convert-plaintext-to-md.prompt.md | ✅ Trigger defined |
| 5 | `/generator-orchestrator` | generator-orchestrator.prompt.md | ✅ Trigger defined |
| 6 | `/prompt-builder` | prompt-builder.prompt.md | ✅ Trigger defined |
| 7 | `/update-implementation-plan` | update-implementation-plan.prompt.md | ✅ Trigger defined |

### Prompts REFERENCED by Prompts/*.md (cross-reference)

| Prompt | Referenced by | Purpose |
|--------|--------------|---------|
| `.github/prompts/context-map.prompt.md` | ALL 8 Prompts/*.md files | Pre-flight dependency mapping |
| `.github/prompts/convert-plaintext-to-md.prompt.md` | Prompts/dev-init.prompts.md | TXT→MD conversion |
| `.github/prompts/boost-prompt.prompt.md` | Prompts/dev-init.prompts.md | Prompt refinement |
| `.github/prompts/ai-prompt-engineering-safety-review.prompt.md` | Prompts/dev-init.prompts.md | Safety review |
| `.github/prompts/update-implementation-plan.prompt.md` | Prompts/dev-init.prompts.md | Plan updates |
| `.github/prompts/prompt-builder.prompt.md` | Prompts/dev-init.prompts.md | Prompt scaffolding |

---

## Section 2: Prompts/*.md Enhancement Recommendations

### File: Prompts/agents-fix.prompts.md
**Trigger:** `/agents-fix`
**Current skills:** 8 (brainstorming, plans-and-specs, dispatching-parallel-agents, subagent-driven-development, systematic-debugging, simplify, acpx-executor, context-map)
**Recommended additions:**
- `skill:qwen-code` — For large codebase agent discovery across platforms
- `skill:opencode` — For OpenCode agent definition reading
- `skill:copilot-cli` — For Copilot agent prompt verification
- `tool:terminal` — For running discovery commands
- `tool:search_files` — For locating agent definitions

### File: Prompts/bash-scripts-fix.prompts.md
**Trigger:** `/bash-scripts-fix`
**Current skills:** 6 (brainstorming, plans-and-specs, dispatching-parallel-agents, subagent-driven-development, systematic-debugging, simplify)
**Recommended additions:**
- `skill:acpx-executor` — For parallel script audit via ACPX agents
- `skill:script-orchestration` — For bash script modernization patterns
- `tool:terminal` — For script testing and verification
- Reference to `.github/prompts/update-implementation-plan.prompt.md`

### File: Prompts/commands-fix.prompts.md
**Trigger:** `/commands-fix`
**Current skills:** 8 (brainstorming, plans-and-specs, dispatching-parallel-agents, subagent-driven-development, systematic-debugging, simplify, acpx-executor, context-map)
**Recommended additions:**
- `skill:customize-opencode` — For OpenCode command sync
- `skill:hermes-agent` — For Hermes agent command integration
- `tool:skill_view` — For reading prompt definitions

### File: Prompts/dev-init.prompts.md
**Trigger:** `/dev-init`
**Current skills:** 5 (brainstorming, plans-and-specs, acpx-executor, executing-plans, context-map)
**Recommended additions:**
- `skill:writing-skills` — For prompt writing best practices
- `skill:writing-plans` — For structured plan authoring
- `skill:simplify` — For concise output
- Reference to ALL 5 target prompts explicitly listed

### File: Prompts/general.prompts.md
**Trigger:** `/general`
**Current skills:** 10 (brainstorming, plans-and-specs, dispatching-parallel-agents, subagent-driven-development, systematic-debugging, simplify, plan, writing-skills, acpx-executor, context-map)
**Recommended additions:**
- `skill:context7` — Already referenced but should be in frontmatter
- `tool:mcp_sequential_thinking_sequentialthinking` — Already referenced in Actions
- `tool:mcp_context7_query_docs` — Already referenced in Actions
- Add `dependencies:` section for tool requirements

### File: Prompts/repo.prompts.md
**Trigger:** `/repo`
**Current skills:** 8 (brainstorming, plans-and-specs, dispatching-parallel-agents, subagent-driven-development, systematic-debugging, simplify, acpx-executor, context-map)
**Recommended additions:**
- `skill:git-helper` — For branch management operations
- `tool:terminal` — For git commands
- Reference to `.github/prompts/create-implementation-plan.prompt.md`

### File: Prompts/skills-fix.prompts.md
**Trigger:** `/skills-fix`
**Current skills:** 8 (brainstorming, plans-and-specs, dispatching-parallel-agents, subagent-driven-development, systematic-debugging, simplify, acpx-executor, context-map)
**Recommended additions:**
- `skill:skill-judge` — For skill auditing (already referenced in text)
- `skill:skill-creator` — For creating new skills during fixes
- `tool:terminal("hermes skills list")` — For skill inventory
- Add explicit `dependencies:` for Hermes CLI

### File: Prompts/workspace-consolidate.prompts.md
**Trigger:** `/workspace-consolidate`
**Current skills:** 8 (brainstorming, plans-and-specs, dispatching-parallel-agents, subagent-driven-development, systematic-debugging, simplify, acpx-executor, context-map)
**Recommended additions:**
- `skill:git-patch-management` — For patch operations
- `skill:project-consolidation` — For workspace consolidation
- `tool:terminal("git apply")` — For patch testing
- Add `ai-readiness` scoring section to frontmatter

---

## Section 3: Skills/Tools Cross-Reference Matrix

### Most-Referenced Skills Across Prompts/*.md

| Skill | Used By | Count |
|-------|---------|-------|
| `context-map` | ALL 8 files | 8 |
| `brainstorming` | ALL 8 files | 8 |
| `plans-and-specs` | ALL 8 files | 8 |
| `dispatching-parallel-agents` | ALL 8 files | 8 |
| `subagent-driven-development` | ALL 8 files | 8 |
| `systematic-debugging` | ALL 8 files | 8 |
| `simplify` | ALL 8 files | 8 |
| `acpx-executor` | 7/8 files (except bash-scripts-fix) | 7 |

### Recommended Skills NOT Yet Referenced

| Hermes Skill | Should Be In | Reason |
|-------------|-------------|--------|
| `qwen-code` | agents-fix, commands-fix | ACPX agent for codebase exploration |
| `opencode` | agents-fix, commands-fix, skills-fix | ACPX agent for structured analysis |
| `copilot-cli` | agents-fix, commands-fix | ACPX agent for quick verification |
| `context7` | general (already in text) | Codebase documentation awareness |
| `skill-judge` | skills-fix (already in text) | Skill quality evaluation |
| `script-orchestration` | bash-scripts-fix | Script modernization |
| `git-helper` | repo | Branch management |
| `writing-skills` | dev-init | Prompt writing best practices |
| `writing-plans` | dev-init | Structured plan authoring |
| `executing-plans` | dev-init (already there) | Plan execution |
| `customize-opencode` | commands-fix | OpenCode configuration |

### Hermes Toolsets Available (20 enabled)

| Toolset | Status | Relevant To |
|---------|--------|-------------|
| `terminal` | ✅ Enabled | ALL Prompts/*.md |
| `file` (read_file, write_file, search_files, patch) | ✅ Enabled | ALL Prompts/*.md |
| `web_search` | ✅ Enabled | general.prompts.md |
| `delegation` (delegate_task) | ✅ Enabled | ALL (parallel agents) |
| `skills` (skill_view) | ✅ Enabled | ALL (skill loading) |
| `code_execution` | ✅ Enabled | Task implementation |
| `vision` | ✅ Enabled | Documentation analysis |
| `browser` | ✅ Enabled | Web testing |

---

## Section 4: Priority-Ordered Enhancement Backlog

### P0 — Critical (frontmatter fixes)
- [ ] Add `trigger:` to all 117 prompts missing it in `.github/prompts/`
- [ ] Add `description:` to all prompts with only truncated descriptions
- [ ] Add `dependencies:` section to Prompts/general.prompts.md for tool requirements

### P1 — High (skills/tools integration)
- [x] Add `acpx-executor` to Prompts/bash-scripts-fix.prompts.md
- [ ] Add `qwen-code` to agents-fix.prompts.md and commands-fix.prompts.md
- [ ] Add `opencode` to agents-fix.prompts.md and skills-fix.prompts.md
- [ ] Add `git-helper` to repo.prompts.md
- [ ] Add `skill-judge` to skills-fix.prompts.md frontmatter

### P2 — Medium (ACPX agent references)
- [ ] Add ACPX routing table reference to all Prompts/*.md files
- [ ] Add `copilot-cli` verification step to commands-fix.prompts.md
- [ ] Reference 3 ACPX agents in general.prompts.md tool section

### P3 — Low (documentation polish)
- [ ] Normalize frontmatter format across all prompts
- [ ] Add skill purpose tables to all Prompts/*.md files
- [ ] Standardize trigger naming convention (`/kebab-case`)

---

## Section 5: ACPX Agent Usage Summary

| Agent | Used For | Status | Rate Limit |
|-------|----------|--------|------------|
| **Qwen Code** | `.txt` batch conversion, large file analysis | ✅ Verified | Free (OpenRouter) |
| **OpenCode** | Structured prompt analysis, enhancement reports | ✅ Verified | No hard limit |
| **Copilot CLI** | Quick verification, smoke tests | ✅ Verified | ~50 premium/week |

### Recommendations for Future ACPX Usage

1. **Qwen Code** → Best for bulk text processing (TXT→MD conversion, grep/search across many files)
2. **OpenCode** → Best for structured analysis (prompt review, skill audit, enhancement planning)
3. **Copilot CLI** → Best for quick verification (check prompt syntax, verify trigger format)
4. **All three** → Use for parallel agent dispatch on independent file batches

---

## Section 6: .github/prompts/ Category Distribution

| Category | Count | Examples |
|----------|-------|---------|
| MCP Servers | 5 | python-mcp-server-generator, typescript-mcp-server-generator, swift-mcp-server-generator, mcp-copilot-studio-server-generator, mcp-declarative-agent |
| Blueprint Generators | 7 | architecture-blueprint, code-exemplars-blueprint, copilot-instructions-blueprint, folder-structure-blueprint, project-workflow-blueprint, readme-blueprint, technology-stack-blueprint |
| Planning/Breakdown | 12 | breakdown-epic-arch, breakdown-epic-pm, breakdown-feature-*, breakdown-plan, breakdown-test, hermes-breakdown-* |
| Testing | 8 | playwright-*, pytest-coverage, testing, javascript-typescript-jest, webapp-testing |
| SQL/Database | 4 | sql-code-review, sql-optimization, postgresql-*, ef-core |
| DevOps/Infra | 5 | devops-rollout-plan, multi-stage-dockerfile, azure-resource-health, update-avm-modules, git-flow-branch-creator |
| Code Review | 5 | code-review, review-and-refactor, postgresql-code-review, sql-code-review, requesting-code-review |
| Documentation | 10 | create-readme, create-llms, update-llms, documentation, documentation-writer, update-docs-on-code-change, create-oo-component-documentation, update-oo-component-documentation, create-tldr-page, tldr-prompt |
| GitHub Integration | 8 | create-github-*, my-issues, my-pull-requests, gen-specs-as-issues |
| Prompt Engineering | 5 | boost-prompt, prompt-builder, prompts-strict-template, ai-prompt-engineering-safety-review, finalize-agent-prompt |
| Agents/Instructions | 6 | create-agentsmd, optimize-agentsMd, declarative-agents, structured-autonomy-*, copilot-instructions-blueprint |
| Awesome-Copilot | 4 | suggest-awesome-* (agents, instructions, prompts, skills) |
| Other | 45+ | refactor-*, memory-merger, remember, conventional-commit, editorconfig, etc. |
