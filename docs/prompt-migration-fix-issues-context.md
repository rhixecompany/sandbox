# Prompt Migration Fix Progress

## Phase 3a Complete: All YAML Syntax Errors Fixed

Fixed 5 files with YAML syntax errors (all `---` glued to last YAML value):
- `workspace-consolidate.prompt.md` — ✅ Fixed: `project---` split into `project` + `---`
- `general.prompt.md` — ✅ Fixed: `acpx-executor---` split
- `prompts-fix.prompt.md` — ✅ Fixed: `copilot-cli---` split
- `dev-init.prompt.md` — ✅ Fixed: `---` fence + `>` block moved outside frontmatter
- `bash-scripts-fix.prompt.md` — ✅ Fixed: `script-orchestration---` split

Plus added `---` closing fence to files missing it (general, prompts-fix).

### Remaining "YAML errors" — By Design (16 files)

These are not broken syntax, they're plain markdown without YAML frontmatter:
- Plain markdown plans/transcripts (14 files): `run`, `plan-setup`, `plan-optimize`, etc.
- Empty file (1): `zod-schema-generation.prompt.md`
- Non-Hermes YAML schema (1): `java-docs.prompt.md` — has valid YAML with `agent:`, `tools:` fields

These are NOT parse errors — they lack frontmatter or use a different schema. Adding synthetic frontmatter would change their semantics. Flagged for user review.

## Phase 3b: Enhancement Batches — Remaining Tasks

Now proceeding with the standard batch process (7 files per batch, newest first) for missing fields and enhancements. The broken dep paths are also all fixed (8/8).

| Batch | Status | Files |
|-------|--------|-------|
| 1 (yaml-fix batch) | ✅ COMPLETE | test-providers-models, workspace-consolidate, repo-management, repo, agents-system-prompt-context-fix, update-docs-on-code-change, typescript |
| Dep path fixes | ✅ COMPLETE | repo-management, repo, skills-fix, agents-fix, workspace-consolidate, dev-init, general, prompts-fix, bash-scripts-fix |
| YAML syntax errors | ✅ COMPLETE | workspace-consolidate, general, prompts-fix, dev-init, bash-scripts-fix |
| 2 (next 7) | PENDING | tasksync, task-implementation, session-agentsmd-full-workflow, security, run-session-agentsmd-workflow, refresh-agent-inventory, prompts-strict-template |
| 3–32 | PENDING | Remaining files in mtime order |
