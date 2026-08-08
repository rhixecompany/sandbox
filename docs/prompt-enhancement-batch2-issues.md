# Prompt Enhancement Batch 2 - Audit Issues

## Audit Criteria (from enhance-markdown skill)

- Double frontmatter fences in first 60 lines → High
- `skills:` prose in YAML → Medium
- Merged YAML close: `---##` → High (split to standalone `---` + heading)
- `write_file` stream timeout on >~8K-token payloads → Medium (split writes)
- `toolsets:` entries that are not valid Hermes toolset names → Medium
- Orphaned thin wrappers: body <20 lines AND references a file that no longer exists → High
- Duplicate `toolsets:` entries in same frontmatter → Low
- Frontmatter has `name`, `title`, `description`, `tags`, `version`, `author`, `license` → Required
- `metadata.hermes.related_skills` matches prerequisite skills → Required
- `.prompt.md` extension used → Required
- Trigger matches filename stem → Required
- No merged YAML close (`---##` / `|---##`) → Required
- **NEW**: Frontmatter with blank/empty line values → Medium (YAML parsing issues)

## Issue Report by Prompt

### 1. cosmosdb-datamodeling.prompt.md

**Status**: ⚠️ MEDIUM - Frontmatter has blank/empty line values

- **ISSUE**: Multiple blank lines in frontmatter with just field names and empty values (lines 2, 4, 6, 9, 12, 15, 21, 23, 25, 27, 29, 32, 35, 38, 41, 44, 47, 50, 53, 55)
- Example: Line 2 is just `name: cosmosdb-datamodeling` followed by blank line 3, then line 4 is blank
- This is a YAML formatting issue that could cause parsing problems
- Skills list is empty `[]` but body references 5 skills
- Dependencies list is empty `[]` but body references multiple skills
- No `plan` field (but references templates/cosmosdb-datamodeling/ directory)

**Issues**:

- Blank/empty lines in frontmatter → Medium
- `skills: []` but body references skills → Low (inconsistent)
- `dependencies: []` but body references skills → Low (inconsistent)

### 2. oh-my-openagent-setup.prompt.md

**Status**: ✅ PASS - No issues found

- Frontmatter clean, no blank lines
- All required fields present
- Valid toolsets: file, terminal
- Trigger matches filename stem
- Skills and dependencies consistent

### 3. disk-space-cleanup.prompt.md

**Status**: ✅ PASS - No issues found

- Frontmatter clean, no blank lines
- All required fields present
- Valid toolsets: clarify, file, terminal
- Trigger matches filename stem
- Skills and dependencies consistent

### 4. pl.prompt.md

**Status**: ⚠️ MEDIUM - Frontmatter has blank/empty line values

- **ISSUE**: Multiple blank lines in frontmatter (lines 2, 4, 7, 9, 11, 14, 16, 19, 22, 25, 28, 31, 34, 37)
- Skills list is empty `[]` but body references 5 skills
- Dependencies list is empty `[]` but body references skills
- Plan references a specific plan file

**Issues**:

- Blank/empty lines in frontmatter → Medium
- `skills: []` but body references skills → Low (inconsistent)
- `dependencies: []` but body references skills → Low (inconsistent)

### 5. model-recommendation.prompt.md

**Status**: ⚠️ MEDIUM - Frontmatter has blank/empty line values

- **ISSUE**: Multiple blank lines in frontmatter (lines 2, 4, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48)
- Skills list is empty `[]` but body references 5 skills
- Dependencies list is empty `[]` but body references skills
- No plan field (references templates/model-recommendation/ directory)

**Issues**:

- Blank/empty lines in frontmatter → Medium
- `skills: []` but body references skills → Low (inconsistent)
- `dependencies: []` but body references skills → Low (inconsistent)

## Summary

| Prompt                | High | Medium | Low | Status       |
| --------------------- | ---- | ------ | --- | ------------ |
| cosmosdb-datamodeling | 0    | 1      | 2   | ⚠️ NEEDS FIX |
| oh-my-openagent-setup | 0    | 0      | 0   | ✅ PASS      |
| disk-space-cleanup    | 0    | 0      | 0   | ✅ PASS      |
| pl                    | 0    | 1      | 2   | ⚠️ NEEDS FIX |
| model-recommendation  | 0    | 1      | 2   | ⚠️ NEEDS FIX |

## Recommended Fixes (Phase 2)

### Fix 1: cosmosdb-datamodeling.prompt.md

1. Remove blank/empty lines from frontmatter (compact YAML)
2. Populate `skills:` array with skills referenced in body: using-superpowers, systematic-debugging, git-patch-management, executing-plans, verification-before-completion
3. Populate `dependencies:` array with same skills

### Fix 2: pl.prompt.md

1. Remove blank/empty lines from frontmatter (compact YAML)
2. Populate `skills:` array with skills referenced in body: using-superpowers, systematic-debugging, git-patch-management, executing-plans, verification-before-completion
3. Populate `dependencies:` array with same skills

### Fix 3: model-recommendation.prompt.md

1. Remove blank/empty lines from frontmatter (compact YAML)
2. Populate `skills:` array with skills referenced in body: using-superpowers, systematic-debugging, git-patch-management, executing-plans, verification-before-completion
3. Populate `dependencies:` array with same skills

### Fix Application Strategy

- Apply fixes using `patch` tool for targeted edits
- Verify each fix with `read_file` after application
- Update progress in `docs/prompt-enhancement-batch2-fix-progress.md`
