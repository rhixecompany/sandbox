# boost-prompt — Issues Catalog

Generated: 2026-05-25 | Files audited: 1 | Batch: 1 of 2

## Summary

**Total Issues**: 3 | **Critical**: 1 | **Major**: 2 | **Minor**: 0

## Critical Findings

### Issue #1: Undocumented Joyride Dependency (Critical)

**Severity**: Critical | **Category**: External Dependency | **Type**: Missing Tool Verification

**Location**: .github/prompts/boost-prompt.prompt.md, Phase 3 (lines 81-95)

**Description**:
The prompt relies on Joyride VS Code extension for clipboard operations, but this dependency is not formally declared in the frontmatter. The code example uses Joyride's vscode clipboard API without verification that the extension is available or installed.

**Details**:
- **Declared**: Only mentioned in description and tags
- **Used in**: Phase 3, Step 1 — `(vscode/env.clipboard.writeText "...")`
- **Implicit requirements**: Joyride must be installed, `joyride_request_human_input` must be available
- **Fallback**: No fallback procedure documented if Joyride is unavailable
- **Impact**: Prompt fails silently if Joyride is not installed; clipboard operation fails

**Suggested Action**:
1. Add explicit `tool:joyride` or `dependency: joyride` to frontmatter
2. Add a section documenting Joyride installation requirements
3. Provide a fallback for users without Joyride (e.g., "copy this text manually")
4. Add version requirements for Joyride
5. Test clipboard operation as part of pre-execution validation

**Evidence**:
- Line 4: Tags mention "joyride" but not formally as a dependency
- Lines 68, 86-91: Joyride functions referenced without declaration
- No error handling for missing Joyride

## Major Issues

### Issue #2: External Skills Not Verified

**Severity**: Major | **Category**: Dependency | **Type**: Missing Verification

**Location**: .github/prompts/boost-prompt.prompt.md, frontmatter

**Description**:
The prompt declares two skills (`prompt-engineering`, `writing-plans`) that are not verified to exist in the project's skill registry.

**Details**:
- **Declared in**: `dependencies` and `skills` sections
- **References**: 
  - `prompt-engineering — Research-backed prompt optimization patterns`
  - `writing-plans — Structured prompt authoring`
- **Status**: Not found in `.opencode/` directory
- **Impact**: If skills are unavailable, the prompt cannot execute its intended workflow

**Suggested Action**:
1. Verify existence of both skills in the system
2. If they exist, create reference entries in skill registry
3. If they don't exist, either:
   - Create the skills
   - Update prompt to remove the dependency
   - Document as future implementation need
4. Add skill availability check to pre-execution validation

### Issue #3: Implicit Tool Dependencies Not Documented

**Severity**: Major | **Category**: Dependency | **Type**: Incomplete Declaration

**Location**: .github/prompts/boost-prompt.prompt.md, Phase 1 & 3

**Description**:
The prompt uses `joyride_request_human_input` function (Phase 1, step 2) without declaring it as a formal tool dependency. This creates execution fragility.

**Details**:
- **First used**: Line 68 — Phase 1, Step 2
- **API call**: `joyride_request_human_input` (undefined parameters, no documentation)
- **Second use**: Phase 3, Step 1 — vscode clipboard API
- **Documentation**: No docs on function signature, return value, error handling
- **Impact**: Execution fails if Joyride is unavailable; parameters are unclear

**Suggested Action**:
1. Add formal documentation for `joyride_request_human_input` function
2. Document API signature: parameters, return types, error conditions
3. Provide example usage within the prompt
4. Add error handling instructions
5. Document what happens if the function fails

## Minor Issues

*None.*

## Formatting Issues

**Count**: 0 | **Status**: ✓ All clear

- YAML frontmatter is properly formatted
- Markdown tables are correctly structured
- Code block uses proper syntax highlighting (clojure)
- Line breaks and spacing are consistent

## Content Issues

**Count**: 0 (Excluding dependency issues above)

- Phase descriptions are clear and actionable
- Goals align with outputs
- Rules are explicit and rule #1 ("No code") is emphasized

**Note**: The critical safety rule stating "DO NOT WRITE ANY CODE" is well-positioned (line 27, within 15% of execution) and effective in preventing misuse.

## Structural Issues

**Count**: 0 | **Status**: ✓ All clear

- All declared sections present
- Proper heading hierarchy
- Phase structure consistent
- 4-phase pattern matches related prompts

## Cross-File Issues

**Count**: 0 | **Status**: ✓ All clear

- No broken references to other prompts
- No missing related files
- References in backup files are consistent

## Related Prompts Health Check

| Prompt | Status | Notes |
| --- | --- | --- |
| context-map.prompt.md | Good | No dependency on boost-prompt |
| ai-prompt-engineering-safety-review.prompt.md | Good | Similar pattern, separate workflow |
| prompt-builder.prompt.md | Similar | Also uses prompt-engineering skill |

## Issue Statistics

| Category | Count | Severity Mix |
| --- | --- | --- |
| Formatting | 0 | — |
| Content | 0 | — |
| Structural | 0 | — |
| Cross-file | 0 | — |
| Dependencies | 3 | 1 Critical, 2 Major |

## Remediation Priority

### P0 (Critical)
1. **Formalize Joyride dependency** — Required for Phase 3 execution
   - Time estimate: 30 min

### P1 (Major)
2. **Verify or document skill dependencies** — Required for Phase 1-2 execution
   - Time estimate: 45 min
3. **Document joyride_request_human_input API** — Required for Phase 1 execution
   - Time estimate: 30 min

### P2 (Minor)
*None.*

**Total Remediation Time**: ~1.5 hours

## Audit Notes

- File is well-structured with clear phases
- Content is professional and actionable
- Main concern: External dependencies are not formally declared
- Safety rule ("no code") is well-positioned
- Joyride integration is a strength but creates a critical unverified dependency
- Ready for use pending critical/major dependency remediation

## Dependency Verification Checklist

- [ ] skill:prompt-engineering exists
- [ ] skill:writing-plans exists
- [ ] Joyride VS Code extension available
- [ ] joyride_request_human_input function available
- [ ] vscode.env.clipboard API available
- [ ] Fallback procedure defined for missing Joyride

## Sign-Off

**Audit Date**: 2026-05-25  
**Auditor**: Systematic Debugging Audit Pass  
**Status**: PASS with 3 dependency issues noted (1 Critical, 2 Major)  
**Recommendation**: Execute P0 critical remediation before use, then P1 major items

## Execution Readiness

**Current Status**: ⚠️ NOT READY  
**Blockers**: Critical Joyride dependency not formalized; external skills unverified  
**Re-audit Date**: After dependency remediation
