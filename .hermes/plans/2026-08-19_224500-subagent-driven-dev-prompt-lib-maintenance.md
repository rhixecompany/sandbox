# Implementation Plan: Subagent-Driven Development + Prompt Library Maintenance

## Goal
Fully implement and verify the integration of `subagent-driven-development` and `prompt-library-maintenance` skills with all best practices, DRY principles, and user preferences (Alexa's working style: systematic, skill-driven, stacked bundles, comprehensive prompts with best practices from codebase + all MCP servers/skills).

## Current Context
- **User**: Alexa — pragmatic senior engineer, direct, substance over filler
- **Profiles**: 7 profiles (default + 6 aliases), routing: code→architect, research→analyst, design→creative, planning→exec, teaching→tutor, ops→alexa
- **Models**: nemotron-3-ultra-free (opencode-zen) primary, deepseek-v4-flash-free fallback
- **Workspace**: ~/Desktop/SandBox (rhixecompany/sandbox, 17 projects)
- **Prompt Library**: 226 prompts at ~/AppData/Local/hermes/prompts/ (1 issue: repo-init.prompt.md missing `scripts` field)
- **Skills**: 600+ skills at ~/AppData/Local/hermes/skills/, including both target skills
- **MCP Servers**: 21 configured (filesystem, github, ast-grep, memory, playwright, sequential-thinking, context7, fetch, tavily, neon, docker, honcho, mindstudio, code-sandbox, python-quality, tooling-lint, tooling-config, sentry, smithery, parallel-search, parallel-task)
- **Honcho**: Active (hybrid mode, per-directory strategy, mapped to SandBox)

## Approach
Phase-based execution with strict sequential gates. Each phase must pass verification before proceeding. Uses subagent-driven-development's 2-stage review (spec compliance → code quality) for implementation tasks.

## Phase 1: Prerequisite Validation (Pre-flight Gate)
**Gate Type**: Pre-flight — blocks if any prerequisite unmet

| Task | Description | Verification |
|------|-------------|--------------|
| 1.1 | Verify both skills load without error | `skill_view` returns valid content |
| 1.2 | Verify prompt library validation script runs clean | `python3 scripts/verify_prompt_library.py` → TOTAL=226 CLEAN=226 |
| 1.3 | Verify prompt library audit script runs | `python3 scripts/audit_prompt_library.py` → produces docs/ report |
| 1.4 | Verify fix script dry-run mode | `python3 scripts/fix_prompt_library.py --dry-run` → no unexpected mutations |
| 1.5 | Check delegate_task tool availability | Tool listed in available tools |
| 1.6 | Verify Honcho session mapping for SandBox | `hermes honcho sessions` shows SandBox mapped |

## Phase 2: Prompt Library Maintenance Implementation
**Gate Type**: Revision — loops back with specific feedback (max 3 iterations)

### 2.1 Fix Single Remaining Issue
- **Issue**: `repo-init.prompt.md` missing `scripts` field in frontmatter
- **Action**: Run fix script with `--apply --files repo-init.prompt.md`
- **Verification**: Re-run validator → TOTAL=226 CLEAN=226 WITH_ISSUES=0

### 2.2 Full Library Audit
- Run `audit_prompt_library.py` to generate:
  - Cross-prompt delegation map
  - Domain registry (stem-based, 100% coverage)
  - Skill/tool/prompt dependency resolution report
- **Output**: `docs/prompt-registry.md`, `docs/prompt-audit-report.md`
- **Verification**: Reports exist, no uncategorized domains, all edges resolved

### 2.3 Toolset Normalization Pass
- Normalize any remaining VS Code/Copilot toolsets to Hermes palette
- Ensure `mcp` toolset present where `tool:mcp-*` dependencies exist
- Remove `search` toolset (use `web` instead)
- **Verification**: Independent verifier (`verify_prompt_library.py`) reports CLEAN=226

### 2.4 Name/Filename/Trigger Consistency
- Verify all `name:` fields match filename slug
- Verify all `trigger:` fields match `/<slug>`
- Fix any plural `triggers:` → singular `trigger:`
- **Verification**: Validator reports zero NAME≠SLUG, TRIGGER≠/slug issues

### 2.5 DEPS==SKILLS Bidirectional Sync
- Every `skill:` dep in `dependencies:` must be in `skills:` and vice versa
- Remove self-referencing skill deps
- Relabel MCP tools from `skill:mcp-*` → `tool:mcp-*`
- Remove MCP tools from `skills:` section
- **Verification**: Validator reports zero SKILL_DEP_ONLY, SKILL_LIST_ONLY, MCP_AS_SKILL_DEP, MCP_IN_SKILLS

### 2.6 Legacy Section Cleanup
- Remove any `## Legacy Prompt Details` sections from bodies
- **Verification**: Validator reports zero LEGACY_SECTION issues

### 2.7 Final Validation
- Run independent verifier → TOTAL=226 CLEAN=226 WITH_ISSUES=0
- Run audit again for updated reports
- **Gate**: All verification checklist items PASS

## Phase 3: Subagent-Driven Development Implementation
**Gate Type**: Revision — 2-stage review per task (spec compliance → code quality)

### 3.1 Create Master Implementation Plan
- Create plan file at `.hermes/plans/subagent-dev-implementation.md`
- Break into granular tasks (2-5 min each)
- Define dependencies and acceptance criteria
- Link to this spec

### 3.2 Task 1: Verify Delegate Task Integration
- **Spec**: `delegate_task` tool available, accepts goal/context/toolsets
- **Implementation**: Test dispatch with minimal context
- **Spec Review**: Tool responds, returns structured output
- **Quality Review**: No errors, proper context isolation

### 3.3 Task 2: Create Example Plan File
- **Spec**: Plan with 3-5 granular tasks following skill template
- **Location**: `.hermes/plans/example-subagent-plan.md`
- **Spec Review**: Tasks are right-sized (2-5 min), have full context
- **Quality Review**: Clear must-haves, testable acceptance criteria

### 3.4 Task 3: Implement Subagent Dispatcher Helper
- **Spec**: Python script that reads plan, extracts tasks, dispatches subagents with proper context
- **Location**: `scripts/subagent_dispatcher.py`
- **Features**: 
  - Parse plan markdown for tasks
  - Build implementer context with project conventions
  - Dispatch spec reviewer with original task spec
  - Dispatch quality reviewer with file list
  - Track todo list status
- **Spec Review**: Script handles all 3 subagent types, respects gates
- **Quality Review**: Error handling, logging, clean CLI

### 3.5 Task 4: Integration Test with Real Plan
- **Spec**: Run dispatcher on example plan, all tasks complete
- **Subagents**: 1 implementer + 2 reviewers per task
- **Verification**: All spec reviews PASS, all quality reviews APPROVED
- **Final Integration Review**: All components work together

## Phase 4: Cross-Integration Verification
**Gate Type**: Pre-flight — validates integration before marking complete

| Task | Description |
|------|-------------|
| 4.1 | Verify subagent-driven-development can use prompt-library-maintenance skills in context |
| 4.2 | Verify prompt-library-maintenance scripts can be dispatched via subagents |
| 4.3 | Test full workflow: plan → dispatch → review → verify → commit |
| 4.4 | Update skill references in both SKILL.md files to cross-link |
| 4.5 | Add both skills to user's stacked bundles for session startup |

## Phase 5: Documentation & Knowledge Transfer
**Gate Type**: Revision — review for completeness

| Deliverable | Location |
|-------------|----------|
| Updated subagent-driven-development SKILL.md | Cross-reference prompt-library-maintenance |
| Updated prompt-library-maintenance SKILL.md | Cross-reference subagent-driven-development |
| Combined workflow reference | `references/subagent-prompt-workflow.md` |
| Session startup protocol update | `references/session-startup-protocol.md` |

## Timeline Estimate
- Phase 1: 10 min (validation)
- Phase 2: 30 min (prompt library fixes + audit)
- Phase 3: 45 min (subagent dev implementation + test)
- Phase 4: 15 min (cross-integration)
- Phase 5: 10 min (documentation)
- **Total**: ~1 hour 50 min

## Risks & Mitigations
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Delegate task tool unavailable | Low | High | Fallback to manual execution with same review process |
| Context window pressure | Medium | Medium | Use context-budget-discipline.md rules, checkpoint at DEGRADING tier |
| Subagent review loop stalls | Low | Medium | Escalation gate after 3 iterations |
| Prompt library file count mismatch | Low | Low | Use `find`/`ls` to verify counts before scripts |

## Files Likely to Change
| File | Change Type |
|------|-------------|
| `~/AppData/Local/hermes/prompts/repo-init.prompt.md` | Fix frontmatter |
| `~/AppData/Local/hermes/prompts/*.prompt.md` | Toolset normalization, DEPS==SKILLS sync |
| `.hermes/plans/subagent-dev-implementation.md` | New plan file |
| `.hermes/plans/example-subagent-plan.md` | New example plan |
| `scripts/subagent_dispatcher.py` | New helper script |
| `docs/prompt-registry.md` | Audit output |
| `docs/prompt-audit-report.md` | Audit output |
| Both SKILL.md files | Cross-references |

## Success Criteria
- [ ] Prompt library: 226/226 prompts pass independent verification
- [ ] Subagent-driven-development: dispatcher script works, example plan executes fully
- [ ] Cross-integration: both skills work together in stacked bundles
- [ ] All verification checklists PASS
- [ ] No backup files created (git for rollback)
- [ ] All changes committed with conventional commit messages

---

*Plan created: 2026-08-19 22:45:00*
*Profile: exec-assistant (planning/coordination)*
*Model: nemotron-3-ultra-free (opencode-zen)*