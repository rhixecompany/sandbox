---
status: completed
---

# Prompt Enhancement Batch 1 - Fix Plan

## Phase 2: Fix Planning (enhance-markdown skill)

### Entry Check

- [x] `docs/prompt-enhancement-batch1-context.md` exists
- [x] `docs/prompt-enhancement-batch1-issues.md` exists

### Fix Plan

#### Fix 1: execute-all-prompts.prompt.md (HIGH PRIORITY)

**Issues**:

- `toolsets: None` → should be `toolsets: []` or valid array
- Missing `trigger` field

**Changes**:

1. Change `toolsets: None` to `toolsets: []`
2. Add `trigger: /execute-all-prompts` after `formatter: default`

#### Fix 2: smithery-setup.prompt.md (LOW PRIORITY - optional)

**Issues**:

- Missing `trigger` field

**Changes**:

1. Add `trigger: /smithery-setup` after `formatter: default`

#### Fix 3: tooling-implementation.prompt.md (LOW PRIORITY - optional)

**Issues**:

- Missing `trigger` field

**Changes**:

1. Add `trigger: /tooling-implementation` after `formatter: default`

#### Fix 4: all-repo-docker-setup.prompt.md (LOW PRIORITY - optional)

**Issues**:

- Missing `tags` array in frontmatter

**Changes**:

1. Add `tags` array with relevant categories

### Fix Application Strategy

- Apply fixes using `patch` tool for targeted edits
- Verify each fix with `read_file` after application
- Update progress in `docs/prompt-enhancement-batch1-fix-progress.md`

### Gate Criteria for Phase 2 Completion

- [ ] Fix 1 applied and verified (execute-all-prompts)
- [ ] Fix 2 applied and verified (smithery-setup) - optional
- [ ] Fix 3 applied and verified (tooling-implementation) - optional
- [ ] Fix 4 applied and verified (all-repo-docker-setup) - optional
- [ ] All modified files pass frontmatter validation
- [ ] Progress documented

### Next Phase

Phase 3: Execute Remaining Fixes (if any additional issues discovered)
Phase 4: Verify - Re-run audit checks on all 5 prompts
