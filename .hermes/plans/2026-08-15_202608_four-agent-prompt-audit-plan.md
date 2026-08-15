# Comprehensive Audit & Enhancement of .github/prompts/*.md for Multi-Agent Support — PLAN

## Goal
Execute the spec at `.hermes/plans/2026-08-15_202608_four-agent-prompt-audit-spec.md` — audit, standardize, enhance, and verify all 226 `.github/prompts/*.prompt.md` files for Hermes, Copilot, OpenCode, and Codex.

## Pre-Flight Checks
- [ ] `bun run check` passes on root (workspace health)
- [ ] Git working tree clean or changes staged (backup point)
- [ ] `analyze_prompts.py --all` runs and establishes baseline
- [ ] Legacy prompts located at `C:\Users\Alexa\AppData\Local\hermes\prompts\` (226 files)

## Phase 0: Baseline & Discovery (Task 0.1–0.5)

### Task 0.1 — Run analyzer baseline
- **Action**: `cd .github/prompts && python .enhance/analyze_prompts.py --all`
- **Output**: Baseline counts for YAML validity, section coverage, DRY compliance
- **Gate**: Analyzer runs without errors

### Task 0.2 — Inventory legacy prompts
- **Action**: List all 226 files in `C:\Users\Alexa\AppData\Local\hermes\prompts\`, compute SHA-256 body hashes
- **Output**: `legacy_inventory.json` — filename, hash, size, first-line preview for each
- **Gate**: 226 files cataloged

### Task 0.3 — Cross-reference filenames
- **Action**: Compare legacy filenames against SandBox `.github/prompts/*.prompt.md`
- **Output**: 3 categories: same-name-different-body / same-name-same-body / legacy-only
- **Gate**: Categorization complete

### Task 0.4 — Read shared templates
- **Action**: Read `templates/_shared/frontmatter-template.md`, `skills-table-core.md`, `personas.md`, `personality.md`, `rules-core.md`, `best-practices.md`, `verification-checklist.md`
- **Output**: Understanding of canonical schema and DRY patterns
- **Gate**: Templates understood

### Task 0.5 — Sample prompt review
- **Action**: Read 5 prompts with full 4-agent metadata + 5 with no frontmatter + 2 with duplicate frontmatter (comprehensive-prompt-enhancer, debugger-prompt)
- **Output**: Understanding of current patterns and edge cases
- **Gate**: Sample reviewed

## Phase 1: Legacy Prompt Migration (AC1) (Task 1.1–1.4)

### Task 1.1 — Build migration script
- **Action**: Create `migrate_legacy_prompts.py` in `.enhance/`
- **Details**:
  - Reads all 226 legacy prompts from `C:\Users\Alexa\AppData\Local\hermes\prompts\`
  - For each, finds corresponding SandBox prompt by filename
  - If SandBox prompt exists: compare bodies; if legacy body is a subset/superset, merge; if different topic, create new prompt with disambiguated name
  - If no SandBox prompt: create new `.prompt.md` with canonical frontmatter
  - Generates canonical frontmatter per schema (Task 0.4 templates)
  - **IDEMPOTENT**: safe to re-run; skips files already migrated
- **Output**: Migrated prompts in `.github/prompts/`
- **Estimate**: 2-3 hours (script) + 1 hour (review)

### Task 1.2 — Execute migration
- **Action**: Run `python .enhance/migrate_legacy_prompts.py --apply`
- **Output**: Migrated files in `.github/prompts/`
- **Gate**: No errors; files created

### Task 1.3 — Migration review
- **Action**: Spot-check 10 migrated prompts (5 same-name merges, 5 new files)
- **Output**: Confirmation that content is correct, frontmatter is valid
- **Gate**: Spot-check passes

### Task 1.4 — Archive superseded legacy prompts
- **Action**: Move legacy prompts that were superseded or redundant to `templates/archived/` with justification note
- **Output**: Archived files with `ARCHIVED.md` justification
- **Gate**: Zero legacy prompts remain unaccounted for

## Phase 2: Deduplication (AC2) (Task 2.1–2.3)

### Task 2.1 — Compute body hashes
- **Action**: `python .enhance/analyze_prompts.py --hashes` (or custom script)
- **Output**: `body_hashes.json` — SHA-256 of normalized body for all 226+ prompts
- **Gate**: Hashes computed

### Task 2.2 — Identify duplicates
- **Action**: Group prompts by hash; identify exact duplicate bodies
- **Output**: `duplicates.json` — groups of files with identical bodies
- **Gate**: Duplicates identified

### Task 2.3 — Consolidate duplicates
- **Action**: For each duplicate group:
  - Keep the file with better frontmatter (more complete, better trigger)
  - Add cross-reference comment to other files: `<!-- DUPLICATE OF: <file> -->`
  - `git rm` the duplicate files (or keep as symlink reference)
- **Output**: Duplicate files removed/consolidated
- **Gate**: Zero duplicate bodies remain

## Phase 3: Frontmatter Standardization (AC3) (Task 3.1–3.4)

### Task 3.1 — Bulk frontmatter generation script
- **Action**: Create `update_frontmatter_4agent.py` in `.enhance/`
- **Details**:
  - Reads each `.prompt.md`, preserves body, extracts existing valid frontmatter fields
  - Generates canonical frontmatter per schema
  - Populates 4-agent metadata using heuristics
  - Writes updated frontmatter + original body
  - **IDEMPOTENT**: re-running produces zero changes on already-standardized files
- **Output**: Script ready to run

### Task 3.2 — Execute bulk standardization
- **Action**: `python .enhance/update_frontmatter_4agent.py --apply`
- **Output**: All 226+ prompts have canonical frontmatter with 4-agent metadata
- **Estimate**: 1-2 hours (script) + verification

### Task 3.3 — Fix special cases
- **Action**: Manual review and fix for:
  - `comprehensive-prompt-enhancer.prompt.md` — duplicate frontmatter (use second occurrence)
  - `debugger-prompt.prompt.md` — Copilot-style frontmatter cleanup
  - 67 no-frontmatter prompts — verify generated frontmatter is correct
  - Any prompts where auto-generated metadata is wrong
- **Output**: Fixed special cases
- **Estimate**: 1-2 hours

### Task 3.4 — Validate YAML
- **Action**: `python -c "import yaml; [yaml.safe_load(open(f)) for f in Path('.github/prompts').glob('*.prompt.md')]"`
- **Output**: Zero YAML parse errors
- **Gate**: All YAML valid

## Phase 4: Agent Metadata Enrichment (AC6) (Task 4.1–4.3)

### Task 4.1 — Profile assignment audit
- **Action**: Review all `metadata.hermes.profile` values; fix misclassifications
- **Details**: Use domain heuristic; ensure profiles are from valid set
- **Output**: Correct profile assignments

### Task 4.2 — MCP servers audit
- **Action**: Review `metadata.hermes.mcp_servers` values; add missing servers referenced in prompt content
- **Details**: Scan prompt body for MCP tool references (e.g., `mcp__github__`, `mcp__filesystem__`)
- **Output**: Complete MCP server lists

### Task 4.3 — Context size & extensions audit
- **Action**: Review `context_size` values (small/medium/large) and Copilot `extensions`
- **Details**: Body length heuristic; add GitHub.copilot for PR-related prompts
- **Output**: Correct context sizes and extensions

## Phase 5: Reference Integrity (AC5) (Task 5.1–5.3)

### Task 5.1 — Extract all references
- **Action**: `python verify_references.py` — scan all prompts for file references
- **Output**: `references.json` — all references found, resolved status
- **Gate**: References extracted

### Task 5.2 — Fix broken references
- **Action**: For each broken reference:
  - If target moved: update path
  - If target deleted: remove reference or update to valid alternative
  - If to shared template that doesn't exist: create it or remove reference
- **Output**: All references resolve
- **Estimate**: 1-2 hours

### Task 5.3 — Trigger uniqueness check
- **Action**: Verify no two prompts share the same `trigger:` value
- **Output**: Trigger uniqueness confirmed
- **Gate**: All triggers unique

## Phase 6: YAML/JSON Validation (AC4) (Task 6.1–6.4)

### Task 6.1 — Full YAML validation
- **Action**: `python -c "import yaml; [yaml.safe_load(open(f)) for f in Path('.github/prompts').glob('*.prompt.md')]"`
- **Output**: Zero parse errors
- **Gate**: All YAML valid

### Task 6.2 — JSON validation in bodies
- **Action**: Scan for embedded JSON blocks (```json ... ```) and inline `{...}`; validate each
- **Output**: Zero JSON parse errors
- **Gate**: All JSON valid

### Task 6.3 — Fix duplicate frontmatter
- **Action**: `python .enhance/fix_prompt_artifacts.py --apply` (or manual patch for comprehensive-prompt-enhancer)
- **Output**: Zero duplicate frontmatter blocks
- **Gate**: No duplicate frontmatter

### Task 6.4 — Fix duplicate tags format
- **Action**: Normalize tags like `typescript - prompts - enhancement - library` to proper YAML list `[typescript, prompts, enhancement, library]`
- **Output**: All tags are proper YAML lists
- **Gate**: No space-separated tag strings

## Phase 7: Index & Docs Updates (AC7) (Task 7.1–7.3)

### Task 7.1 — Update `index.md`
- **Action**: Update prompt count, add multi-agent note
- **Details**: Count prompts after all phases; update "220+" to actual count
- **Gate**: Count matches

### Task 7.2 — Update `copilot-instructions.md`
- **Action**: Update prompt library count from "190+" to actual
- **Gate**: Count matches

### Task 7.3 — Update `_index.md`
- **Action**: Update generation date, add 4-agent metadata coverage stat
- **Gate**: Date current

## Phase 8: Quality Gates (AC8) (Task 8.1–8.4)

### Task 8.1 — markdownlint
- **Action**: `bun run markdownlint`
- **Output**: Pass or list of errors
- **Gate**: Zero markdownlint errors (or accept pre-existing known issues)

### Task 8.2 — format:check
- **Action**: `bun run format:check`
- **Output**: Pass or list of formatting issues
- **Gate**: Zero formatting issues

### Task 8.3 — cspell
- **Action**: `cspell lint "**/*.md"`
- **Output**: Pass or list of typos
- **Gate**: Zero cspell errors (or words added to dictionary)

### Task 8.4 — bun run check (full gate)
- **Action**: `bun run check`
- **Output**: All 4 checks pass
- **Gate**: `bun run check` passes on `.github/prompts/`

## Phase 9: Git Cleanup (AC9) (Task 9.1–9.2)

### Task 9.1 — Remove backup artifacts
- **Action**: `find .github/prompts -name "*.bak" -o -name "*.backup" -o -name "*.old" -o -name "*.orig" | xargs rm -f`
- **Gate**: Zero backup artifacts

### Task 9.2 — Commit in batches
- **Action**: Git commits per the commit sequence in spec
- **Output**: Meaningful conventional commits with `[B]`/`[I]` markers
- **Gate**: All changes committed; `git status` clean

## Parallelization Opportunities

| Wave | Tasks | Notes |
|------|-------|-------|
| **Sequential (must be ordered)** | Phase 0 → Phase 1 → Phase 2 → Phase 3 | Migration must happen before dedup; dedup before frontmatter standardization |
| **Parallel within Phase 3** | Task 3.2 (bulk script) + Task 3.3 (special cases) | Special cases can be fixed while bulk script runs |
| **Parallel within Phase 4** | Task 4.1 + Task 4.2 + Task 4.3 | Independent audits |
| **Parallel within Phase 8** | Task 8.1 + Task 8.2 + Task 8.3 | Independent lint checks |

## Time Estimates

| Phase | Tasks | Estimated Time |
|-------|-------|---------------|
| 0: Baseline & Discovery | 0.1–0.5 | 1 hour |
| 1: Legacy Migration | 1.1–1.4 | 3-4 hours (script + review) |
| 2: Deduplication | 2.1–2.3 | 1 hour |
| 3: Frontmatter Standardization | 3.1–3.4 | 2-3 hours |
| 4: Agent Metadata Enrichment | 4.1–4.3 | 1-2 hours |
| 5: Reference Integrity | 5.1–5.3 | 1-2 hours |
| 6: YAML/JSON Validation | 6.1–6.4 | 1 hour |
| 7: Index & Docs | 7.1–7.3 | 30 min |
| 8: Quality Gates | 8.1–8.4 | 1-2 hours (includes fixes) |
| 9: Git Cleanup | 9.1–9.2 | 30 min |
| **Total** | | **~14-20 hours** |

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Legacy body merge creates corrupted prompts | Medium | High | Per-file review for prompts with complex bodies; script has --dry-run |
| 67 no-frontmatter prompts lose body content | Low | High | Script preserves body exactly; verify after |
| Bulk frontmatter script corrupts files | Low | High | Dry-run first; verify sample; git rollback ready |
| markdownlint introduces many new errors | Medium | Medium | Fix in batches; prioritize MD001/MD002/MD003 |
| Trigger uniqueness violations after migration | Low | High | Check triggers after migration; rename if needed |
| Memory exhaustion during large script operations | Low | Medium | Process in batches; use execute_code for large loops |

## Success Criteria Summary

| AC | Checkpoint |
|----|-----------|
| AC1 | `C:\Users\Alexa\AppData\Local\hermes\prompts\` has 0 `.prompt.md` files (all migrated or archived) |
| AC2 | `body_hashes.json` shows 226+ unique hashes; 0 duplicate groups |
| AC3 | All `.prompt.md` files parse with canonical schema; `analyze_prompts.py --all` shows 0 CRITICAL |
| AC4 | `yaml.safe_load` passes all files; `bun run check` passes |
| AC5 | `verify_references.py` shows 0 broken references |
| AC6 | Every prompt has non-empty `metadata.hermes`, `metadata.copilot`, `metadata.opencode`, `metadata.codex` |
| AC7 | `index.md` count = actual file count; `copilot-instructions.md` count = actual count |
| AC8 | `bun run markdownlint` + `format:check` + `cspell` all pass |
| AC9 | `git status --short` shows clean; commits have `[B]`/`[I]` markers |
