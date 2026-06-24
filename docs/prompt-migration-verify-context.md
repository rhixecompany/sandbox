# Prompt Migration — Verification Report

Generated: 2026-06-24
Audited: 224 `.prompt.md` files in `./prompts/`

## Summary

| Metric | Value |
|--------|-------|
| Total files | 224 |
| YAML frontmatter valid | **208 files (100% of frontmatter-capable)** |
| No frontmatter (plain MD, by design) | 15 files |
| Empty file | 1 file (`zod-schema-generation.prompt.md`) |
| **True YAML parse failures** | **0** ✅ |
| Files modified from source | 44 files |

## YAML Verification

**PASS** — All 208 files with YAML frontmatter parse correctly via `yaml.safe_load`.

- 5 files previously flagged as "YAML fail" were reclassified: they have `---` horizontal rules in the body (lines 5-18), not frontmatter. These are plain markdown files by design.
- 15 files have no frontmatter at all (no `---` opening fence at line 1). These are chat transcripts, implementation plans, and specifications — plain markdown that uses `.prompt.md` naming.

## Issues Fixed (44 files modified)

### HIGH: YAML Syntax Errors — 5 files

Fixed the `---` bleed pattern where the YAML closing fence was glued to the last value:

| File | Fix |
|------|-----|
| `workspace-consolidate.prompt.md` | `project---` → `project` + `---` on new line |
| `general.prompt.md` | `acpx-executor---` → `acpx-executor` + `---` |
| `prompts-fix.prompt.md` | `copilot-cli---` → `copilot-cli` + `---` |
| `dev-init.prompt.md` | Indented `---`/`>` moved outside frontmatter |
| `bash-scripts-fix.prompt.md` | `script-orchestration---` → `script-orchestration` + `---` |

### HIGH: Broken Dependency Paths — 8 issues across 7 files

Fixed `prompt:.github/prompts/...` → `prompt:...` (paths that resolve incorrectly from `./prompts/`):

- `repo-management`, `repo`, `skills-fix`, `agents-fix`, `workspace-consolidate`, `dev-init`, `general`, `prompts-fix`, `bash-scripts-fix`

### MEDIUM: Missing Frontmatter Fields — 39 files enhanced

Added missing `trigger:`, `title:`, and `tags:` to prompt files that had only `name: + description:`:

- **Batch 1** (7 files): `test-providers-models`, `workspace-consolidate`, `repo-management`, `repo`, `agents-system-prompt-context-fix`, `update-docs-on-code-change`, `typescript`
- **Batch 2** (7 files): `tasksync`, `task-implementation`, `session-agentsmd-full-workflow`, `security`, `run-session-agentsmd-workflow`, `refresh-agent-inventory`, `prompts-strict-template`
- **Bulk enhancement** (25 files): `testing`, `performance`, `nextjs-tailwind`, `code-review`, `documentation`, `editorconfig`, `rust-mcp-server-generator`, `playwright-*`, `dataverse-python-*`, `java-refactoring-*`, `structured-autonomy-*`, `remember-interactive-programming`, `refactor-method-complexity-reduce`, `generator-orchestrator`, `dotnet-upgrade`, `apple-appstore-reviewer`, `playwright-typescript`

### Bugs Corrected in Bulk Enhancement — 4 files

Fixed `.prompt` suffix in `name`/`trigger` fields in `playwright-generate-test`, `playwright-explore-website`, `playwright-automation-fill-in-form`.
Fixed space-containing trigger and name in `editorconfig`.

## Remaining Items (Not Fixed — By Design)

### 15 Files Without Frontmatter

These are plain markdown documents that serve as chat transcripts, implementation plans, or specifications. Adding synthetic frontmatter would alter their purpose:

`run`, `plan-setup`, `plan-optimize`, `plan-fullEslintVscodeAuthModernization`, `plan-updateAiAgentSetupPrompt2`, `plan-phase1ComprehensiveValidation`, `plan-comicWiseImplementation`, `optimization`, `debugger`, `comicwise-session`, `plan-eslintPluginAuditAndUpdate`, `plan-acpx-agent-stack-audit-shared`, `plan-acpx-agent-stack-audit-hermes`, `plan-acpx-agent-stack-audit-copilot`, `Initial`

### 1 Empty File

`zod-schema-generation.prompt.md` — 0 bytes. Needs content or removal.

### 1 Non-Hermes Schema File

`java-docs.prompt.md` — Has valid YAML with Copilot-native fields (`agent:`, `tools:`, `description:`). Valid for its platform, just not Hermes-standard.

## Gates

| Gate | Status |
|------|--------|
| YAML parse: all frontmatter files pass | ✅ 208/208 |
| Zero double-fence repeats in first 60 lines | ✅ (limit was false positives from body dividers) |
| All fixed dep paths resolve | ✅ 8/8 fixed |
| No body fences mistaken for frontmatter | ✅ (15 plain-MD files correctly identified) |
| Cross-ref integrity | ⚠️ 187 files still missing `dependencies:` and `skills:` fields (MEDIUM) |
| All modified files verified | ✅ 44 files pass YAML check |
