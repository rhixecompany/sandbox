# PROMPTS-AUDIT Fix Plan (Dual-Channel)

**Purpose**: `prompts-audit` — Fix plan for 298 issues across 219 prompt files

**Generated**: 2026-06-17 | Source: `docs/prompts-issues-context.md`

---

## Dual-Channel Strategy

### Channel A: Plugin System (Primary — when reachable)
- Use `enhance-markdown` skill's automation
- Run via: `/enhance-markdown <file> prompts-audit`
- Auto-applies fixes per audit categories

### Channel B: Companion Markdown (Fallback — manual/PR)
- This plan document + targeted patches
- Batch size: 7 files per batch
- Track progress in `docs/prompts-fix-issues-context.md`

---

## Fix Categories & Commands

| Category | Files | Fix Approach |
|----------|-------|--------------|
| Unclosed frontmatter | 29 | Insert `---` at line after YAML block (before first heading) |
| Double frontmatter fences | 15 | Remove extra `---` markers, keep exactly 2 (open + close) |
| Missing frontmatter | 17 | Prepend valid YAML with `description`, `trigger` (from filename) |
| YAML parse error | 1 | Fix line 33 sequence/mapping conflict in `repo-management.prompts.md` |
| Empty file | 1 | Delete `zod-schema-generation.prompt.md` or populate |
| Duplicate headings | ~15 files | Rename duplicates with scope prefix (e.g., `### Phase 5 Tasks`) |
| Heading hierarchy skip | ~5 files | Insert missing `##` level headings |
| Extension rename | 2 | `mv debugger-prompt.md debugger.prompt.md`, `mv pl.md pl.prompt.md` |
| Trailing whitespace | 10 | `sed -i 's/[[:space:]]*$//'` |

---

## Batch 1 — Proof of Concept (7 files)

| # | File | Issues | Channel | Verification |
|---|------|--------|---------|--------------|
| 1 | `Prompts/dev-init.prompts.md` | 1H, 16M | B (complex) | YAML parses, no double fence, heading skip fixed |
| 2 | `Prompts/repo-management.prompts.md` | 1H, 3M | B (parse error) | YAML parses, no parse error, heading skip fixed |
| 3 | `.github/prompts/ai-prompt-engineering-safety-review.prompt.md` | 6M | A | No duplicate headings |
| 4 | `.github/prompts/apple-appstore-reviewer.prompt.md` | 1H | A | No double fence |
| 5 | `.github/prompts/bigquery-pipeline-audit.prompt.md` | 1H | A | No double fence |
| 6 | `Prompts/agents-fix.prompts.md` | 1H | B | No unclosed fence |
| 7 | `.github/prompts/zod-schema-generation.prompt.md` | 3H | B | Delete file or add valid FM + content |

---

## Batch 2 — Remaining HIGH (22 files, unclosed fence)

| File |
|------|
| `Prompts/bash-scripts-fix.prompts.md` |
| `Prompts/dev-init.prompts.md` (done in B1) |
| `Prompts/general.prompts.md` |
| `Prompts/prompts-fix.prompts.md` |
| `Prompts/repo.prompts.md` |
| `Prompts/skills-fix.prompts.md` |
| `Prompts/workspace-consolidate.prompts.md` |
| `.github/prompts/code-review.prompt.md` |
| `.github/prompts/documentation.prompt.md` |
| `.github/prompts/nextjs-tailwind.prompt.md` |
| `.github/prompts/performance.prompt.md` |
| `.github/prompts/playwright-typescript.prompt.md` |
| `.github/prompts/prompts-strict-template.prompt.md` |
| `.github/prompts/refresh-agent-inventory.prompt.md` |
| `.github/prompts/run-session-agentsmd-workflow.prompt.md` |
| `.github/prompts/security.prompt.md` |
| `.github/prompts/session-agentsmd-full-workflow.prompt.md` |
| `.github/prompts/task-implementation.prompt.md` |
| `.github/prompts/tasksync.prompt.md` |
| `.github/prompts/testing.prompt.md` |
| `.github/prompts/typescript.prompt.md` |
| `.github/prompts/update-docs-on-code-change.prompt.md` |

→ 3 batches of 7 + 1 batch of 1

---

## Batch 3 — Double fences (15 files)

| File |
|------|
| `.github/prompts/apple-appstore-reviewer.prompt.md` (B1) |
| `.github/prompts/bigquery-pipeline-audit.prompt.md` (B1) |
| `.github/prompts/create-specification.prompt.md` |
| `.github/prompts/features.prompt.md` |
| `.github/prompts/mcp-create-adaptive-cards.prompt.md` |
| `.github/prompts/mcp-create-declarative-agent.prompt.md` |
| `.github/prompts/mcp-deploy-manage-agents.prompt.md` |
| `.github/prompts/optimize-agentsMd.prompt.md` |
| `.github/prompts/plan-batchFixAllErrorsWarningsDeprecations.prompt.md` |
| `.github/prompts/plan-debugger.prompt.md` |
| `.github/prompts/plan-dev.prompt.md` |
| `.github/prompts/plan-features-seed.prompt.md` |
| `.github/prompts/plan-refactor.prompt.md` |
| `.github/prompts/plan-updateAiAgentSetupPrompt.prompt.md` |
| `.github/prompts/setup-enhanced.prompt.md` |
| `.github/prompts/setup-nextjs-frontend-stack.prompt.md` |
| `.github/prompts/setup.prompt.md` |

→ 2 batches of 7 + 1 batch of 1 (B1 already did 2)

---

## Batch 4 — Missing frontmatter (17 files)

| File |
|------|
| `.github/prompts/comicwise-session.prompt.md` |
| `.github/prompts/debugger-prompt.md` → also rename |
| `.github/prompts/debugger.prompt.md` |
| `.github/prompts/pl.md` → also rename |
| `.github/prompts/plan-acpx-agent-stack-audit-copilot.prompt.md` |
| `.github/prompts/plan-acpx-agent-stack-audit-hermes.prompt.md` |
| `.github/prompts/plan-acpx-agent-stack-audit-shared.prompt.md` |
| `.github/prompts/plan-batchFixAllErrorsWarningsAndDeprecations.prompt.md` |
| `.github/prompts/plan-comicWiseImplementation.prompt.md` |
| `.github/prompts/plan-eslintPluginAuditAndUpdate.prompt.md` |
| `.github/prompts/plan-fullEslintVscodeAuthModernization.prompt.md` |
| `.github/prompts/plan-optimize.prompt.md` |
| `.github/prompts/plan-phase1ComprehensiveValidation.prompt.md` |
| `.github/prompts/plan-refactor.prompt.md` |
| `.github/prompts/plan-setup.prompt.md` |
| `.github/prompts/plan-updateAiAgentSetupPrompt2.prompt.md` |
| `.github/prompts/run.prompt.md` |

→ 2 batches of 7 + 1 batch of 3

---

## Batch 5 — Medium issues (duplicate headings, hierarchy)

| File | Issues |
|------|--------|
| `Prompts/dev-init.prompts.md` | 14 duplicates, 5 hierarchy (B1 partial) |
| `.github/prompts/ai-prompt-engineering-safety-review.prompt.md` | 6 duplicates (B1) |
| `.github/prompts/tldr-prompt.prompt.md` | 4 duplicates |
| `Prompts/repo-management.prompts.md` | 1 dup, 2 hierarchy (B1 partial) |
| `Prompts/repo.prompts.md` | 1 dup |
| `Prompts/skills-fix.prompts.md` | 1 hierarchy |
| `Prompts/workspace-consolidate.prompts.md` | 1 dup |
| `.github/prompts/structured-autonomy-generate.prompt.md` | 1 dup |
| `.github/prompts/structured-autonomy-plan.prompt.md` | 1 dup |

→ Manual review needed per file

---

## Batch 6 — Low issues (whitespace, naming)

| File | Fix |
|------|-----|
| Trailing whitespace (10 files) | `sed -i 's/[[:space:]]*$//'` |
| `debugger-prompt.md` → `debugger.prompt.md` | `mv` |
| `pl.md` → `pl.prompt.md` | `mv` |

---

## Progress Tracking

| Batch | Files | Status | Verified |
|-------|-------|--------|----------|
| 1 | 7 | ⬜ Pending | ⬜ |
| 2 | 22 | ⬜ Pending | ⬜ |
| 3 | 15 | ⬜ Pending | ⬜ |
| 4 | 17 | ⬜ Pending | ⬜ |
| 5 | 9 | ⬜ Pending | ⬜ |
| 6 | 12 | ⬜ Pending | ⬜ |

---

## Verification Gates (per modified file)

1. `yaml.safe_load(frontmatter)` → single dict, no exception
2. `grep -n '^---$' file | head -60` → exactly 2 matches (open + close)
3. `grep -n '^skills:' file` → no prose-style entries on following lines
4. `markdownlint` or custom check → no skipped heading levels
5. Extension matches directory convention (`.prompts.md` / `.prompt.md`)

---

## Next: Apply Batch 1

Execute fixes for the 7 proof-of-concept files, then update `docs/prompts-fix-issues-context.md` with results.
