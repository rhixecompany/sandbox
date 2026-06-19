# PROMPTS-AUDIT Issues Context

**Purpose**: `prompts-audit` — Audit findings for all prompt files in `Prompts/` and `.github/prompts/`

**Generated**: 2026-06-17 | Source: `docs/audit_results.json` | Files: 219 | Total issues: 298

---

## Summary

| Severity | Count | % of Total |
|----------|-------|------------|
| HIGH     | 62    | 20.8%      |
| MEDIUM   | 224   | 75.2%      |
| LOW      | 12    | 4.0%       |

**Files with issues**: 189/219 (86.3%)
**Clean files**: 30/219 (13.7%)

---

## HIGH Severity Issues (62)

### Frontmatter: Unclosed fence — 29 files
Missing closing `---` in first 60 lines (YAML never terminates properly)

| File | Location |
|------|----------|
| `.github\prompts\code-review.prompt.md` | lines 1-60 |
| `.github\prompts\documentation.prompt.md` | lines 1-60 |
| `.github\prompts\nextjs-tailwind.prompt.md` | lines 1-60 |
| `.github\prompts\performance.prompt.md` | lines 1-60 |
| `.github\prompts\playwright-typescript.prompt.md` | lines 1-60 |
| `.github\prompts\prompts-strict-template.prompt.md` | lines 1-60 |
| `.github\prompts\refresh-agent-inventory.prompt.md` | lines 1-60 |
| `.github\prompts\run-session-agentsmd-workflow.prompt.md` | lines 1-60 |
| `.github\prompts\security.prompt.md` | lines 1-60 |
| `.github\prompts\session-agentsmd-full-workflow.prompt.md` | lines 1-60 |
| `.github\prompts\setup.prompt.md` | lines 1-60 |
| `.github\prompts\task-implementation.prompt.md` | lines 1-60 |
| `.github\prompts\tasksync.prompt.md` | lines 1-60 |
| `.github\prompts\testing.prompt.md` | lines 1-60 |
| `.github\prompts\typescript.prompt.md` | lines 1-60 |
| `.github\prompts\update-docs-on-code-change.prompt.md` | lines 1-60 |
| `Prompts\agents-fix.prompts.md` | lines 1-60 |
| `Prompts\bash-scripts-fix.prompts.md` | lines 1-60 |
| `Prompts\dev-init.prompts.md` | lines 1-60 |
| `Prompts\general.prompts.md` | lines 1-60 |
| `Prompts\prompts-fix.prompts.md` | lines 1-60 |
| `Prompts\repo.prompts.md` | lines 1-60 |
| `Prompts\skills-fix.prompts.md` | lines 1-60 |
| `Prompts\workspace-consolidate.prompts.md` | lines 1-60 |

### Frontmatter: Double fences (≥3 `---` in first 60 lines) — 15 files
Multiple opening/closing fences corrupt YAML parsing

| File | Fence Count |
|------|-------------|
| `.github\prompts\apple-appstore-reviewer.prompt.md` | 5 |
| `.github\prompts\bigquery-pipeline-audit.prompt.md` | 5 |
| `.github\prompts\create-specification.prompt.md` | 4 |
| `.github\prompts\features.prompt.md` | 4 |
| `.github\prompts\mcp-create-adaptive-cards.prompt.md` | 4 |
| `.github\prompts\mcp-create-declarative-agent.prompt.md` | 4 |
| `.github\prompts\mcp-deploy-manage-agents.prompt.md` | 4 |
| `.github\prompts\optimize-agentsMd.prompt.md` | 3 |
| `.github\prompts\plan-batchFixAllErrorsWarningsDeprecations.prompt.md` | 3 |
| `.github\prompts\plan-debugger.prompt.md` | 3 |
| `.github\prompts\plan-dev.prompt.md` | 4 |
| `.github\prompts\plan-features-seed.prompt.md` | 3 |
| `.github\prompts\plan-refactor.prompt.md` | 4 |
| `.github\prompts\plan-updateAiAgentSetupPrompt.prompt.md` | 3 |
| `.github\prompts\setup-enhanced.prompt.md` | 5 |

### Frontmatter: No YAML frontmatter at all — 17 files
Files starting with content instead of `---`

| File |
|------|
| `.github\prompts\comicwise-session.prompt.md` |
| `.github\prompts\debugger-prompt.md` |
| `.github\prompts\debugger.prompt.md` |
| `.github\prompts\pl.md` |
| `.github\prompts\plan-acpx-agent-stack-audit-copilot.prompt.md` |
| `.github\prompts\plan-acpx-agent-stack-audit-hermes.prompt.md` |
| `.github\prompts\plan-acpx-agent-stack-audit-shared.prompt.md` |
| `.github\prompts\plan-batchFixAllErrorsWarningsAndDeprecations.prompt.md` |
| `.github\prompts\plan-comicWiseImplementation.prompt.md` |
| `.github\prompts\plan-eslintPluginAuditAndUpdate.prompt.md` |
| `.github\prompts\plan-fullEslintVscodeAuthModernization.prompt.md` |
| `.github\prompts\plan-optimize.prompt.md` |
| `.github\prompts\plan-phase1ComprehensiveValidation.prompt.md` |
| `.github\prompts\plan-refactor.prompt.md` |
| `.github\prompts\plan-setup.prompt.md` |
| `.github\prompts\plan-updateAiAgentSetupPrompt2.prompt.md` |
| `.github\prompts\run.prompt.md` |

### Frontmatter: Parse error — 1 file
- `Prompts\repo-management.prompts.md`: YAML syntax error at line 33 (mixing mapping/sequence)

### Structural: Empty file — 1 file
- `.github\prompts\zod-schema-generation.prompt.md`: 0 bytes, completely empty

---

## MEDIUM Severity Issues (224)

### Structure: Duplicate headings — 168 occurrences
Most common duplicates: `Tasks` (27×), `Steps` (23×), `Goal` (15×), `Phase X` variants

| File | Duplicates |
|------|------------|
| `Prompts\dev-init.prompts.md` | 14 (Tasks×4, Conflict Log, Phase 5, etc.) |
| `.github\prompts\ai-prompt-engineering-safety-review.prompt.md` | 6 (Steps×3, Tasks×3) |
| `.github\prompts\tldr-prompt.prompt.md` | 4 (UNAMBIGUOUS/AMBIGUOUS QUERIES×2 each) |
| `Prompts\repo-management.prompts.md` | 1 (.github/workflows/ci.yml) |
| `Prompts\repo.prompts.md` | 1 (<Technology/Topic>) |
| `Prompts\skills-fix.prompts.md` | 0 (skipped) |
| `Prompts\workspace-consolidate.prompts.md` | 1 (Steps) |
| `.github\prompts\structured-autonomy-generate.prompt.md` | 1 (Goal) |
| `.github\prompts\structured-autonomy-plan.prompt.md` | 1 (Goal) |

### Structure: Heading level skip — 14 occurrences
`h1` → `h3` jumps (missing `h2`)

| File | Lines |
|------|-------|
| `Prompts\dev-init.prompts.md` | 320, 330, 340, 446, 473 |
| `Prompts\repo-management.prompts.md` | 214, 301 |
| `Prompts\skills-fix.prompts.md` | 182 |
| `Prompts\workspace-consolidate.prompts.md` | (included in duplicate) |

### Content: Missing required frontmatter field: description — 42 files
Files with valid YAML but no `description` field (mostly `.github/prompts/` agent-style files using `agent:` + `tools:` instead)

---

## LOW Severity Issues (12)

### Formatting: Trailing whitespace — 10 files
| File | Lines |
|------|-------|
| `.github\prompts\azure-resource-health-diagnose.prompt.md` | 263, 264 |
| `.github\prompts\comment-code-generate-a-tutorial.prompt.md` | 64 |
| `.github\prompts\cosmosdb-datamodeling.prompt.md` | 518, 981 |
| `.github\prompts\database.prompt.md` | 121, 122, 123 |
| `.github\prompts\mkdocs-translations.prompt.md` | 75, 110, 120... |
| `.github\prompts\plan-dev.prompt.md` | 24, 25, 83 |
| `.github\prompts\plan-features-seed.prompt.md` | 1169, 1170, 1171 |
| `.github\prompts\plan-updateAiAgentSetupPrompt.prompt.md` | 46, 108 |
| `.github\prompts\debugger-prompt.md` | (naming issue) |
| `.github\prompts\pl.md` | (naming issue) |

### Naming: Wrong extension — 2 files
- `.github\prompts\debugger-prompt.md` → should be `.prompt.md`
- `.github\prompts\pl.md` → should be `.prompt.md`

---

## Per-File Issue Counts (Top 20)

| File | HIGH | MEDIUM | LOW | Total |
|------|------|--------|-----|-------|
| `Prompts\dev-init.prompts.md` | 1 | 16 | 0 | 17 |
| `.github\prompts\ai-prompt-engineering-safety-review.prompt.md` | 0 | 6 | 0 | 6 |
| `.github\prompts\tldr-prompt.prompt.md` | 0 | 4 | 0 | 4 |
| `Prompts\repo-management.prompts.md` | 1 | 3 | 0 | 4 |
| `Prompts\repo.prompts.md` | 1 | 1 | 0 | 2 |
| `Prompts\skills-fix.prompts.md` | 1 | 1 | 0 | 2 |
| `Prompts\workspace-consolidate.prompts.md` | 1 | 1 | 0 | 2 |
| `.github\prompts\apple-appstore-reviewer.prompt.md` | 1 | 0 | 0 | 1 |
| `.github\prompts\bigquery-pipeline-audit.prompt.md` | 1 | 0 | 0 | 1 |
| `.github\prompts\code-review.prompt.md` | 1 | 0 | 0 | 1 |
| ... | | | | |

---

## Fix Plan Categories (Phase 2+)

| Category | Files | Action |
|----------|-------|--------|
| **Fix unclosed frontmatter** | 29 | Add missing `---` at proper position |
| **Fix double frontmatter fences** | 15 | Remove duplicate `---` markers |
| **Add missing frontmatter** | 17 | Insert valid YAML header with `description` |
| **Fix YAML parse error** | 1 | Fix `repo-management.prompts.md` line 33 |
| **Fix empty file** | 1 | Delete or populate `zod-schema-generation.prompt.md` |
| **Fix duplicate headings** | ~15 files | Deduplicate or rename headings |
| **Fix heading hierarchy** | ~5 files | Insert missing `h2` levels |
| **Fix extension** | 2 | Rename `debugger-prompt.md` → `.prompt.md`, `pl.md` → `.prompt.md` |
| **Trim trailing whitespace** | 10 | Auto-fix with formatter |

---

## Phase 2 Gate Check

**Batch 1 (Proof-of-Concept)**: Fix 7 highest-impact files first:

1. `Prompts\dev-init.prompts.md` — 17 issues (1H, 16M)
2. `Prompts\repo-management.prompts.md` — 4 issues (1H, 3M) + parse error
3. `.github\prompts\ai-prompt-engineering-safety-review.prompt.md` — 6M (duplicates)
4. `.github\prompts\apple-appstore-reviewer.prompt.md` — 1H (double fence)
5. `.github\prompts\bigquery-pipeline-audit.prompt.md` — 1H (double fence)
6. `Prompts\agents-fix.prompts.md` — 1H (unclosed fence)
7. `.github\prompts\zod-schema-generation.prompt.md` — 3H (empty + no FM + structural)

**Success Criteria for Batch 1**:
- All 7 files parse cleanly with `yaml.safe_load`
- Zero double-fence issues in first 60 lines
- No unclosed frontmatter fences
- Heading hierarchy valid

If Batch 1 passes cleanly, proceed with remaining 212 files in batches of 7.

---

## Notes

- **Systemic pattern**: All 8 `Prompts/*.prompts.md` files share the same unclosed frontmatter bug
- **Two formats**: `.github/prompts/` files with `agent:`/`tools:` style are mostly clean (valid FM where present)
- **Zombie file**: `zod-schema-generation.prompt.md` should be deleted or replaced
- **Naming**: Two files violate extension convention in `.github/prompts/`
