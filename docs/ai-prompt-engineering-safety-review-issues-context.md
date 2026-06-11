# ai-prompt-engineering-safety-review — Issues Catalog

Generated: 2026-05-25 | Files audited: 1 | Batch: 1 of 2

## Summary

**Total Issues**: 1 | **Critical**: 0 | **Major**: 1 | **Minor**: 0

## Critical Findings

*None.*

## Major Issues

### Issue #1: External Skills Not Verified

**Severity**: Major | **Category**: Dependency | **Type**: Missing Verification

**Location**: .github/prompts/ai-prompt-engineering-safety-review.prompt.md, frontmatter

**Description**:
The prompt declares two skills (`prompt-engineering`, `systematic-debugging`) that are not verified to exist in the project's skill registry.

**Details**:
- **Declared in**: `dependencies` and `skills` sections
- **References**: 
  - `prompt-engineering — Apply safety and quality patterns`
  - `systematic-debugging — Systematic issue detection`
- **Status**: Not found in `.opencode/` directory during audit
- **Usage**: Both skills are core to the workflow and cannot be skipped
  - `prompt-engineering` is needed for Phase 2 (improve the prompt)
  - `systematic-debugging` is needed for Phases 1 and 3 (analysis and validation)
- **Impact**: If skills are unavailable, the prompt cannot execute its intended review workflow

**Suggested Action**:
1. Verify existence of both skills in the system
2. If they exist, create reference entries in skill registry
3. If they don't exist, either:
   - Create the skills (especially `systematic-debugging` which appears used in this prompt)
   - Update prompt to remove the dependency
   - Document as future implementation need
4. Add skill availability check to pre-execution validation
5. Consider cross-reference with other prompts using these skills:
   - `boost-prompt.prompt.md` uses `prompt-engineering` and `writing-plans`
   - Other prompts may share these dependencies

**Cross-reference**: 
- `boost-prompt.prompt.md` has the same dependency on `skill:prompt-engineering` (Major issue #2 there)
- This suggests either both prompts need these skills to exist, or there's a widespread dependency verification gap

## Minor Issues

*None.*

## Formatting Issues

**Count**: 0 | **Status**: ✓ All clear

- YAML frontmatter is properly formatted
- Markdown tables are correctly structured
- Heading hierarchy is correct (H1-H4)
- Code blocks properly formatted
- No encoding issues or artifacts

## Content Issues

**Count**: 0 | **Status**: ✓ All clear

- All sections are complete and coherent
- Goals align with outputs
- Phase descriptions match headers
- Rules are clear and specific
- No contradictions or ambiguous instructions
- Risk framework is well-articulated (safety, bias, security, clarity)
- Rules follow logical priority (safety first)

## Structural Issues

**Count**: 0 | **Status**: ✓ All clear

- All declared sections present
- Proper 4-phase structure consistent with other prompts
- Tables are valid markdown
- Phase steps are clearly numbered
- Task/subtask patterns are consistent

## Cross-File Issues

**Count**: 0 | **Status**: ✓ All clear

- No broken references to other prompts
- No missing related files
- Backup references are consistent
- Complements but does not require other prompts (independent workflow)

## Related Prompts Health Check

| Prompt | Dependency Overlap | Notes |
| --- | --- | --- |
| boost-prompt.prompt.md | ✓ prompt-engineering | Same skill dependency |
| context-map.prompt.md | None | Independent workflow |
| prompt-builder.prompt.md | ✓ prompt-engineering | Same skill dependency |
| update-implementation-plan.prompt.md | None | Independent workflow |

**Finding**: Three prompts (`boost-prompt`, `ai-prompt-engineering-safety-review`, `prompt-builder`) all depend on `skill:prompt-engineering`. This is a systemic dependency that needs verification.

## Issue Statistics

| Category | Count | Severity Mix |
| --- | --- | --- |
| Formatting | 0 | — |
| Content | 0 | — |
| Structural | 0 | — |
| Cross-file | 0 | — |
| Dependencies | 1 | Major (2 skills unverified) |

## Remediation Priority

### P0 (Critical)
*None.*

### P1 (Major)
1. **Verify or document skill dependencies** — Required for full workflow execution
   - Affects: `prompt-engineering`, `systematic-debugging`
   - Time estimate: 1 hour
   - Note: This is a high-priority systemic issue affecting multiple prompts

### P2 (Minor)
*None.*

**Total Remediation Time**: ~1 hour

## Quality Assessment

| Aspect | Rating | Notes |
| --- | --- | --- |
| Clarity | Excellent | Risk framework is explicit and well-structured |
| Completeness | Excellent | All phases and steps well-defined |
| Consistency | Excellent | Matches template patterns |
| Safety | Excellent | Strong emphasis on harm, bias, and injection risks |
| Practicality | Excellent | Concrete rules, real-world risk focus |
| Dependencies | Needs Work | External skills unverified |

## Execution Readiness

| Checklist Item | Status |
| --- | --- |
| Frontmatter valid | ✓ Yes |
| Structure complete | ✓ Yes |
| Content coherent | ✓ Yes |
| Dependencies verified | ⚠️ No (2 skills unverified) |
| External tools ready | ✓ Yes (self-contained) |
| Fallback procedures | ✓ Yes (workflow can adapt) |

**Current Status**: ⚠️ MOSTLY READY  
**Blockers**: External skills not verified  
**Execution Risk**: Low-Medium (skills may not exist, but workflow is self-contained and can proceed with manual review)  
**Recommendation**: Can be used immediately with manual execution; formalize skill dependencies before automation

## Systemic Findings

### Shared Skill: prompt-engineering

The following prompts all depend on `skill:prompt-engineering`:
1. boost-prompt.prompt.md
2. ai-prompt-engineering-safety-review.prompt.md
3. prompt-builder.prompt.md

**Action**: Create a unified verification/remediation plan for this skill across all three prompts.

### Shared Skill: systematic-debugging

Only `ai-prompt-engineering-safety-review.prompt.md` depends on this skill among the batch-1 audited files. Check batch-2 files for additional references.

## Audit Notes

- File is excellent in terms of content quality and structure
- Clear risk framework and safety-first approach
- Well-articulated threat model
- Main concern: External dependencies are not verified
- Unlike `boost-prompt`, this prompt has no external tool dependencies (self-contained)
- Prompt can be executed manually even if skills are unavailable
- Recommended for immediate use pending skill verification

## Dependency Verification Checklist

- [ ] skill:prompt-engineering exists (shared with boost-prompt, prompt-builder)
- [ ] skill:systematic-debugging exists
- [ ] Both skills are accessible from prompts directory
- [ ] Verify skill output format matches prompt Phase 1-2 expectations

## Sign-Off

**Audit Date**: 2026-05-25  
**Auditor**: Systematic Debugging Audit Pass  
**Status**: PASS with 1 Major dependency issue (2 skills unverified)  
**Recommendation**: Use immediately with manual workflow, formalize skill dependencies for automation

## Notes for Batch 2

When auditing batch 2 files:
- Check if other prompts reference these skills
- Consider creating a master skill index
- Document skill availability status comprehensively
