# Prompt Enhancement Batch 2 - Fix Plan

## Phase 2: Fix Planning (enhance-markdown skill)

### Entry Check

- [x] `docs/prompt-enhancement-batch2-context.md` exists
- [x] `docs/prompt-enhancement-batch2-issues.md` exists

### Fix Plan

#### Fix 1: cosmosdb-datamodeling.prompt.md (MEDIUM PRIORITY)

**Issues**:

- Blank/empty lines in frontmatter (YAML formatting)
- Empty `skills: []` but body references 5 skills
- Empty `dependencies: []` but body references 5 skills

**Changes**:

1. Compact frontmatter - remove blank lines
2. Add `skills:` array with: using-superpowers, systematic-debugging, git-patch-management, executing-plans, verification-before-completion
3. Add `dependencies:` array with same skills

#### Fix 2: pl.prompt.md (MEDIUM PRIORITY)

**Issues**:

- Blank/empty lines in frontmatter (YAML formatting)
- Empty `skills: []` but body references 5 skills
- Empty `dependencies: []` but body references 5 skills

**Changes**:

1. Compact frontmatter - remove blank lines
2. Add `skills:` array with: using-superpowers, systematic-debugging, git-patch-management, executing-plans, verification-before-completion
3. Add `dependencies:` array with same skills

#### Fix 3: model-recommendation.prompt.md (MEDIUM PRIORITY)

**Issues**:

- Blank/empty lines in frontmatter (YAML formatting)
- Empty `skills: []` but body references 5 skills
- Empty `dependencies: []` but body references 5 skills

**Changes**:

1. Compact frontmatter - remove blank lines
2. Add `skills:` array with: using-superpowers, systematic-debugging, git-patch-management, executing-plans, verification-before-completion
3. Add `dependencies:` array with same skills

### Fix Application Strategy

- Apply fixes using `patch` tool for targeted edits
- Verify each fix with `read_file` after application
- Update progress in `docs/prompt-enhancement-batch2-fix-progress.md`

### Gate Criteria for Phase 2 Completion

- [ ] Fix 1 applied and verified (cosmosdb-datamodeling)
- [ ] Fix 2 applied and verified (pl)
- [ ] Fix 3 applied and verified (model-recommendation)
- [ ] All modified files pass frontmatter validation
- [ ] Progress documented

### Next Phase

Phase 3: Execute Remaining Fixes (if any additional issues discovered)
Phase 4: Verify - Re-run audit checks on all 5 prompts
