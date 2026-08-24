# Update, Enhance, Verify Context Files + Test Providers Models Prompt
**Date:** 2026-08-24
**Profile:** default
**Model:** stepfun/step-3.7-flash:free
**Status:** approved

## Goal
Make a verified, DRY, best-practice pass over:
- Hermes default profile docs: `SOUL.md`, `USER.md`, `MEMORY.md`
- All Hermes profile memory files under `~/AppData/Local/hermes/profiles/*/memories/`
- Agent context files: `.hermes.md`, `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, `.github/copilot-instructions.md`
- Prompt file: `.github/prompts/test-providers-models.prompt.md`

Constraints:
- Update only files whose content actually needs improvement.
- Preserve single-source-of-truth relationships; avoid duplicated rules.
- For Hermes config/provider changes, use `hermes config set` only.
- Any change touching >3 files must use a written plan, approval artifact, and verification gate.

## Current State
- `SOUL.md` exists and is large; contains core rules + multi-file change protocol.
- `USER.md` and `MEMORY.md` are pointer files in the workspace; canonical copies likely live under `~/AppData/Local/hermes/profiles/default/`.
- `.hermes.md`, `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, `.github/copilot-instructions.md` exist in workspace root.
- Many subprojects have local `copilot-instructions.md`; these are deferred references, not full policy docs.
- `test-providers-models.prompt.md` exists with embedded verified working model set + ranking algorithm + config commands.

## Proposed Approach
1. Inventory exact Hermes profile memory files and compare with workspace pointers.
2. Audit each target for drift, duplication, and outdated config references.
3. Define canonical owner for each rule and convert duplicates to cross-references.
4. Update `test-providers-models.prompt.md` to enforce only working models + agent config updates.
5. Create reusable sync/verification scripts under `scripts/`.
6. Verify all changes with lint/format/docs checks and a final provider probe.

## Milestones
- M1 — Inventory & diff complete
- M2 — Canonical ownership mapped
- M3 — Updates applied
- M4 — Verification passed
- M5 — Report + next steps

## Timeline
- Day 1: inventory + diff + ownership mapping
- Day 2: patch updates + script creation
- Day 3: verification + report

## Resource Allocation
- Primary: Hermes agent orchestration
- Subagents: 1 provider-model verification subagent, 1 repo-doc audit subagent
- Tools: `hermes config`, `mcp-filesystem`, `mcp-ast-grep`, `mcp-memory`, `execute_code`

## Phases

### Phase 1 — Inventory
- List all target files.
- Read canonical profile memory files under `~/AppData/Local/hermes/profiles/*/memories/`.
- Capture current `hermes config show` and `hermes auth list`.
- Output: `.hermes/plans/verification/context-files-inventory-2026-08-24.md`

### Phase 2 — Diff & Ownership Mapping
- Identify duplicated rules across `SOUL.md` / `.hermes.md` / `AGENTS.md`.
- Map each rule to one canonical file.
- Produce a change matrix: file → action → risk.

### Phase 3 — Apply Changes
- Update files in smallest logical batches.
- Convert duplicated sections into one-liner cross-references.
- Update provider/model references in `.hermes.md`, `AGENTS.md`, and the prompt file to match live verified state.

### Phase 4 — Verification
- Run doc lint/format checks.
- Re-run `test-providers-models.prompt.md` verification gates.
- Confirm Hermes config via `hermes config check`.

### Phase 5 — Report
- Deliver a scannable summary with file paths, change counts, and verification evidence.

## Files Likely to Change
- `C:\Users\Alexa\Desktop\SandBox\SOUL.md`
- `C:\Users\Alexa\Desktop\SandBox\.hermes\profiles\default\memories\USER.md`
- `C:\Users\Alexa\Desktop\SandBox\.hermes\profiles\default\memories\MEMORY.md`
- `C:\Users\Alexa\Desktop\SandBox\.hermes.md`
- `C:\Users\Alexa\Desktop\SandBox\AGENTS.md`
- `C:\Users\Alexa\Desktop\SandBox\CLAUDE.md`
- `C:\Users\Alexa\Desktop\SandBox\.cursorrules`
- `C:\Users\Alexa\Desktop\SandBox\.github\copilot-instructions.md`
- `C:\Users\Alexa\Desktop\SandBox\.github\prompts\test-providers-models.prompt.md`
- `C:\Users\Alexa\Desktop\SandBox\scripts\sync_context_docs.py` (new)
- `C:\Users\Alexa\Desktop\SandBox\scripts\verify_context_docs.py` (new)

## Verification
- [ ] `hermes config check` passes
- [ ] All duplicated rule blocks reduced to cross-references
- [ ] `test-providers-models.prompt.md` matches live verified model set
- [ ] No secrets or tokens introduced
- [ ] Documentation lint/format clean

## Risks
- Profile pointer drift between workspace and Hermes profile dirs.
- Subagent config changes diverging from live Hermes config.
- Duplicate rule propagation across multiple instruction files.

## Approval
Plan approved for execution.
