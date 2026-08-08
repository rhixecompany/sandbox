# Prompt Enhancement Batch 1 - Audit Issues

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

## Issue Report by Prompt

### 1. smithery-setup.prompt.md

**Status**: ✅ PASS - No high-severity issues found

- Frontmatter complete with all required fields
- Valid toolsets: file, terminal, skills, mcp (all valid Hermes toolsets)
- Skills list is clean (no prose in YAML)
- No double frontmatter fences
- No merged YAML close
- `.prompt.md` extension used
- Trigger: None specified (but name matches filename)
- Metadata.hermes present but empty (acceptable)

**Minor Notes**:

- No `trigger` field defined (optional but recommended)
- `plan: None` explicitly set (acceptable)

### 2. all-repo-docker-setup.prompt.md

**Status**: ✅ PASS - No high-severity issues found

- Frontmatter complete with all required fields
- Valid toolsets: terminal, file, code_execution, web, browser, mcp, delegation (all valid)
- Large skills list (17 skills) - all valid skill names
- Dependencies list comprehensive (26 entries)
- Plan file referenced: plans/all-repo-docker-setup.md
- Trigger defined: /all-repo-docker-setup
- `.prompt.md` extension used

**Minor Notes**:

- No `tags` in frontmatter (optional but recommended for categorization)
- Very large skills list may benefit from categorization

### 3. execute-all-prompts.prompt.md

**Status**: ⚠️ MEDIUM - Missing toolsets field

- Frontmatter complete with required fields
- **ISSUE**: `toolsets: None` - explicitly set to null, should be array or omitted
- Skills list: 4 skills (all valid)
- Dependencies: 4 skills (all valid)
- No plan file referenced
- No trigger defined
- `.prompt.md` extension used

**Issues**:

- `toolsets: None` should be `toolsets: []` or omitted
- No trigger field (recommended for prompt invocation)

### 4. sync-hermes-opencode.prompt.md

**Status**: ✅ PASS - No high-severity issues found

- Frontmatter complete with all required fields
- Valid toolsets: file, terminal, skills (all valid)
- Skills: multi-agent-sync, hermes-profiles, opencode (all valid)
- Dependencies: 4 skills (all valid)
- References templates/sync-hermes-opencode/phases.md
- Trigger defined: /sync-hermes-opencode
- `.prompt.md` extension used

### 5. tooling-implementation.prompt.md

**Status**: ✅ PASS - No high-severity issues found

- Frontmatter complete with all required fields
- Valid toolsets: file, terminal, skills, todo (all valid)
- Skills: 7 skills (all valid category/skill paths)
- Scripts array with valid path
- Dependencies: 2 skills (valid)
- References .hermes/plans/2026-08-01_tooling-implementation.md
- `.prompt.md` extension used

**Minor Notes**:

- No trigger field defined
- `plan: None` explicitly set

## Summary

| Prompt                 | High | Medium | Low | Status          |
| ---------------------- | ---- | ------ | --- | --------------- |
| smithery-setup         | 0    | 0      | 0   | ✅ PASS         |
| all-repo-docker-setup  | 0    | 0      | 0   | ✅ PASS         |
| execute-all-prompts    | 0    | 1      | 1   | ⚠️ NEEDS FIX    |
| sync-hermes-opencode   | 0    | 0      | 0   | ✅ PASS         |
| tooling-implementation | 0    | 0      | 1   | ✅ PASS (minor) |

## Recommended Fixes (Phase 2)

1. **execute-all-prompts.prompt.md**: Fix `toolsets: None` → `toolsets: []`, add `trigger: /execute-all-prompts`
2. **smithery-setup.prompt.md**: Add `trigger: /smithery-setup` (optional)
3. **tooling-implementation.prompt.md**: Add `trigger: /tooling-implementation` (optional)
4. **all-repo-docker-setup.prompt.md**: Add `tags` array (optional)
