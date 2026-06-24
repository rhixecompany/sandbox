# Plan: Prompt Migration — Debug, Fix, Enhance, Validate, Verify

## Goal

Migrate, debug, fix, enhance, validate, and verify all 224 `.prompt.md` files (plus their supporting templates/shared references) from `.github/prompts/` to `./prompts/`, processing in batches of 7 files at a time, ordered by source modification time (newest first). Use the `/enhance-markdown` 4-phase framework.

## Current Context

| Metric | Value |
|--------|-------|
| Source root | `.github/prompts/` |
| Destination root | `./prompts/` |
| `.prompt.md` files | 224 (identical in both locations) |
| Supporting `.md` files | 890 (templates, shared refs, READMEs) |
| Template dirs | `_shared/` (best-practices, goals, personas, personality, phases, frontmatter, skill-refs, verification-checklist) + per-prompt template dirs |
| Current sync state | **Byte-identical** — every file exists in both locations with identical content |
| Dest timestamps | All bulk-timestamped (1782329244-5) — no real modification history |
| Source timestamps | Spread: newest = `test-providers-models` (~2.5h ago), oldest = `dataverse-python-advanced-patterns` (~4d ago) |

## Assumptions

1. The destination `./prompts/` is the **canonical target** — all fixes/enhancements land here
2. The source `.github/prompts/` is the **upstream origin** — drift-check against this
3. Both dirs are in sync now, but the process validates every file independently
4. Each `.prompt.md` may reference shared templates under `templates/_shared/` — those are migrated/enhanced alongside
5. The `enhance-markdown` skill provides the batch processing framework (batches of 7, phased audit-fix-verify)

## Proposed Approach

### Process Model: `/enhance-markdown` 4-Phase Framework

| Phase | Name | Activity |
|-------|------|----------|
| **P1** | Catalog & Audit | Scan all 224 prompt files for issues, categorize by severity, produce context docs |
| **P2** | Fix Planning | Create fix plan with prioritized batch list, apply proof-of-concept batch (7 files) |
| **P3** | Execute Remaining Fixes | Apply remaining 31 batches (7 files each) with progress tracking |
| **P4** | Verify | Re-audit all modified files, confirm zero high-severity issues, write verification report |

### Batch Ordering

Process **batches of 7 `.prompt.md` files** in **descending source modification time** (newest first):

| Batch # | Files (slug) | Source mtime range |
|---------|------------|-------------------|
| 1 | test-providers-models, workspace-consolidate, repo-management, repo, agents-system-prompt-context-fix, update-docs-on-code-change, typescript | newest |
| 2 | tasksync, task-implementation, session-agentsmd-full-workflow, security, run-session-agentsmd-workflow, refresh-agent-inventory, prompts-strict-template | 1782097433 |
| 3 | playwright-typescript, performance, nextjs-tailwind, write-coding-standards-from-file, what-context-needed, update-specification, update-oo-component-documentation | 1782097195 cluster |
| ... | *(continue descending through all 224 files)* | ... |
| 32 | java-docs, dataverse-python-quickstart, dataverse-python-advanced-patterns | oldest |

**Total batches:** 32 (224 ÷ 7 = 32, last batch may be smaller)

## Step-by-Step Plan

### Phase 0: Pre-Flight & Artifact Setup

**Entry check:** If `docs/prompt-migration-context.md` exists → ask user: resume or fresh?

1. Create artifact directory structure:
   - `docs/prompt-migration-context.md` — dependency catalog
   - `docs/prompt-migration-issues-context.md` — audit findings
   - `thoughts/plans/prompt-migration-debug.md` — fix plan
   - `docs/prompt-migration-fix-issues-context.md` — progress log
   - `docs/prompt-migration-verify-context.md` — verification report

2. Resolve purpose slug: **`prompt-migration`**

3. Determine batch processing mode:
   - TXT→MD conversion: NOT needed (all files already `.prompt.md`)
   - Hermes prompt normalization: YES (all files are Hermes prompts)
   - General audit/fix/enhance: YES

4. Load prerequisite skills:
   - `enhance-markdown` (primary framework)
   - `plans-and-specs` (plan creation)
   - `systematic-debugging` (issue detection)
   - `verification-before-completion` (verification gates)

### Phase 1: Catalog & Audit (All 224 Files)

**Skip if:** `docs/prompt-migration-issues-context.md` exists.

1. **Two-way dependency scan** (forward + reverse):
   - Forward: For each `.prompt.md`, extract:
     - `dependencies:` list (prompt: refs, skill: refs, tool: refs)
     - `skills:` list (skill names + inline descriptions)
     - `trigger:` value
     - File path references (relative paths to templates)
     - `/command` references in markdown body
   - Reverse: For each file, search which other files reference it (by trigger, path, or name)
   - Write catalog → `docs/prompt-migration-context.md`

2. **Batch audit** — For each file, check:

   | Severity | Issue | Rule |
   |----------|-------|------|
   | HIGH | Double frontmatter fences | 3+ `---` in first 60 lines |
   | HIGH | Missing required frontmatter | No `trigger:`, `description:`, `tags:`, `dependencies:`, `skills:` |
   | HIGH | YAML parse error | `yaml.safe_load` fails |
   | MEDIUM | Broken `dependencies:` format | `prompt:` refs use wrong path |
   | MEDIUM | `skills:` descriptions in YAML | Dependency-style prose in YAML list |
   | MEDIUM | Broken `tags:` format | Not valid YAML list |
   | LOW | Missing version or author | Optional but recommended |
   | LOW | Stale skill references | References to deleted/renamed skills |
   | INFO | Cross-reference drift | Template file changed but prompt not updated |
   | INFO | Orphaned template files | Template dir with no corresponding `.prompt.md` |

3. **Sample audit** (first 7 files in batch order) for proof-of-concept
4. **Write findings** → `docs/prompt-migration-issues-context.md`

### Phase 2: Fix Planning + Batch 1 Proof-of-Concept

**Skip if:** `thoughts/plans/prompt-migration-debug.md` exists.

1. **Categorize issues** from Phase 1 into fix types:
   - **Type A: Frontmatter fixes** — missing/incorrect YAML fields
   - **Type B: Content fixes** — broken paths, stale refs, formatting
   - **Type C: Enhancement** — add version/author, normalize cross-references
   - **Type D: Structural** — reorder sections, fix template compliance

2. **Write fix plan** → `thoughts/plans/prompt-migration-debug.md`
   - Per-batch fix checklist
   - Priority order (HIGH → MEDIUM → LOW → INFO)
   - Template sync strategy (update `templates/_shared/` once, then reapply)

3. **Write fix context** → `docs/prompt-migration-fix-issues-context.md`

4. **Apply Batch 1** (proof-of-concept — 7 newest files):
   - `test-providers-models.prompt.md`
   - `workspace-consolidate.prompt.md`
   - `repo-management.prompt.md`
   - `repo.prompt.md`
   - `agents-system-prompt-context-fix.prompt.md`
   - `update-docs-on-code-change.prompt.md`
   - `typescript.prompt.md`

   For each file in batch:
   - a. Read full content
   - b. Validate YAML frontmatter
   - c. Check `dependencies:` paths resolve
   - d. Check `skills:` entries valid
   - e. Apply fixes per issue catalog
   - f. Normalize template references
   - g. Write enhanced file → `./prompts/<filename>`

5. **Gate check:** If Batch 1 produces no issues and all files clean → Phase 2 complete; skip to Phase 4 verification.

### Phase 3: Execute Remaining Fixes (Batches 2–32)

For each batch (7 files each, in descending source mtime order):

1. Load batch files from `.github/prompts/`
2. Apply same fix checklist as Batch 1
3. Write enhanced file to `./prompts/`
4. Update progress log in `docs/prompt-migration-fix-issues-context.md`

**Template sync:** Shared templates under `templates/_shared/` and `templates/<prompt-name>/` should be processed together with their parent `.prompt.md`. If a template has issues, fix it once and note it in the batch that covers its parent prompt.

**Batch 31–32** will be shorter (remaining files if not divisible by 7).

### Phase 4: Verification

1. **Re-run audit** on all 224 modified `.prompt.md` files in `./prompts/`
2. **Verify gates** (per file):
   - [ ] YAML frontmatter parses as single document (`yaml.safe_load`)
   - [ ] Zero double-fence repeats in first 60 lines
   - [ ] `trigger:` matches expected `/command` pattern
   - [ ] `description:` present and substantive (>10 chars)
   - [ ] `dependencies:` all paths resolve (relative to `./prompts/`)
   - [ ] `skills:` no dependency-style prose (inline descriptions in list items only)
   - [ ] No broken/missing template references
   - [ ] Section structure follows template standards (when applicable)

3. **Cross-reference check:**
   - Verify all `prompt:` dependency paths point to existing files in `./prompts/`
   - Verify all `skill:` entries reference known skills
   - Verify all template directories have their corresponding `.prompt.md`

4. **Write verification report** → `docs/prompt-migration-verify-context.md`
5. **Fail if:** Any modified file still shows HIGH severity issues

## Files Likely to Change

| Path | Type | Change Type |
|------|------|-------------|
| `./prompts/*.prompt.md` | 224 prompt files | Fix+enhance |
| `./prompts/templates/_shared/*.md` | Shared templates | Fix (if needed) |
| `./prompts/templates/<name>/*.md` | Per-prompt templates | Fix (if needed) |
| `docs/prompt-migration-context.md` | Artifact | New |
| `docs/prompt-migration-issues-context.md` | Artifact | New |
| `thoughts/plans/prompt-migration-debug.md` | Artifact | New |
| `docs/prompt-migration-fix-issues-context.md` | Artifact | New |
| `docs/prompt-migration-verify-context.md` | Artifact | New |

**Not changing:** `.github/prompts/` files (source is read-only reference), any non-prompt file outside scope.

## Validation Criteria

| Gate | Pass Condition |
|------|---------------|
| YAML parse | All 224 files pass `yaml.safe_load` on frontmatter |
| No double fences | Zero files show 3+ `---` in first 60 lines |
| Dep paths resolve | All `prompt:` and relative paths in dependencies resolve |
| Skills valid | All `skills:` entries reference known Hermes skills |
| Template sync | All template dirs have corresponding `.prompt.md` |
| Section completeness | All files have `Goal`, `Description` (or equivalent), `Phases` sections |
| Cross-ref integrity | No stale references to deleted/renamed prompts or skills |

## Risks, Tradeoffs, and Open Questions

### Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| Batch 0 time cost | ~45-90min of context window for 32 batches | Use `delegate_task` for parallel batch processing where possible |
| Template drift | Shared templates may be referenced by multiple prompts | Fix templates first, then propagate; batch parent prompt last |
| Skill reference churn | Skills may have been renamed or deleted since prompts were written | Cross-reference against `hermes skills list` or `skills_list()` |
| Large file write timeouts | `write_file` may time out on very large prompts | Keep per-file writes under ~8K tokens; split large prompts if needed |
| Resumability loss | Process crash mid-way loses batch progress | Log every completed batch in `docs/prompt-migration-fix-issues-context.md` |
| Intent preservation | Automated fixes may alter prompt semantics | Type-C/D fixes only; no semantic rewrites without user review |

### Tradeoffs

- **Batch-of-7**: Balances context efficiency vs. overhead. Smaller batches = more turns but more precise. Larger batches = faster but riskier.
- **Source freshness order**: Newest-first means recently added/updated prompts get attention first. Oldest prompts may have accumulated more drift.
- **Template sync**: Syncing templates eagerly before all prompts may miss edge cases in some prompts. Syncing lazily (per-prompt) is slower but safer.

### Open Questions

1. Should we migrate the source `.github/prompts/` to have canonical symlinks to `../prompts/` after migration, or keep them as-is?
2. For prompts referencing skills that no longer exist — auto-remove the reference, or flag for user review?
3. Some prompts have inline `system: |` blocks (YAML multiline strings) — should these be extracted to separate files?
4. What is the target template standard? The `prompts-strict-template.prompt.md` defines one, but existing prompts vary widely in structure.
5. Should we consolidate duplicate template directories (e.g., `_shared/` exists in both `.github/prompts/` and `./prompts/`)?

## Resumption Points

| After Phase | Resume Artifact | Action |
|-------------|----------------|--------|
| P1 partial | `docs/prompt-migration-context.md` exists | Skip P1 catalog, resume at audit step |
| P1 complete | `docs/prompt-migration-issues-context.md` exists | Skip to P2 |
| P2 partial | `thoughts/plans/prompt-migration-debug.md` exists | Resume fix application at next unprocessed batch |
| P2 complete | `docs/prompt-migration-fix-issues-context.md` has Batch 1 | Skip to P3 |
| P3 partial | Progress log in fix-issues-context.md | Resume at next unprocessed batch |
| P4 | `docs/prompt-migration-verify-context.md` exists | Migration complete |

## Execution Commands (for the agent to run)

When proceeding to execution phase, the agent should:

```bash
# Pre-flight: ensure directories exist
mkdir -p docs thoughts/plans

# Load prerequisite skills (via skill_view in context)
# ... enhance-markdown, plans-and-specs, systematic-debugging, verification-before-completion

# For each batch (7 files):
# 1. Read source files from .github/prompts/
# 2. Validate frontmatter (yaml.safe_load)
# 3. Check dependencies, skills, tags
# 4. Apply fixes
# 5. Write to ./prompts/
# 6. Verify

# Final verification: re-run audit on all 224 files
```
