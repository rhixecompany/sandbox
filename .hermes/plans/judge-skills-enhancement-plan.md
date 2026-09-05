# Judge Skills Enhancement Plan

## Overview
Enhance specs-judge, plans-judge, and prompts-judge to enforce new structural rules and achieve scores ≥98.

## Phase 1: specs-judge Enhancement

### New Requirements
1. **Plan must have/use at least one spec** — Every plan in `.hermes/plans/` must reference at least one spec in `.hermes/specs/` via `## Linked Plan` section or inline reference
2. **Multi-spec support** — Plans can reference multiple specs; specs can be linked to multiple plans
3. **Enhanced cross-ref validation** — Verify that referenced spec files actually exist on disk
4. **Scoring updates** — Increase cross-ref weight to enforce spec-plan coupling

### Changes to judge.py
- Add `plans_dir` parameter to check plan↔spec linkage from both directions
- New dimension: "Spec-Plan Coupling" (replaces or augments Cross-refs)
- Verify every plan has ≥1 spec reference
- Verify every spec has ≥1 plan reference (bidirectional)
- Score 0 if plan has no spec reference
- Score 0 if spec has no plan reference

### Changes to rubric.md
- New dimension: Spec-Plan Coupling (20 pts)
- Plan has ≥1 `## Linked Spec` or spec reference: 20 pts
- Spec has ≥1 `## Linked Plan` or plan reference: 20 pts
- Missing both directions: 0 pts

## Phase 2: plans-judge Enhancement

### New Requirements
1. **Plan must have/use at least one spec** — Same as specs-judge but from plan perspective
2. **Multi-spec support** — Plans can link to multiple specs
3. **Enhanced spec reference validation** — Verify spec files exist
3. **Phase gating on spec linkage** — Each phase should reference which spec(s) it implements

### Changes to judge.py
- Add `specs_dir` parameter for cross-validation
- Check for `## Linked Specs` section (plural) or multiple `## Linked Spec` entries
- Validate each referenced spec file exists
- New scoring dimension: "Spec Coupling" (20 pts)

### Changes to rubric.md
- New dimension: Spec Coupling (20 pts)
- `## Linked Specs` section with ≥1 valid spec path: 20 pts
- Inline spec references to valid files: 15 pts
- No spec references: 0 pts

## Phase 3: prompts-judge Enhancement

### New Requirements
1. **Prompt categorization** — Every `.prompt.md` must have a `category:` frontmatter field matching its parent directory structure
2. **Parent directory exists** — Prompt must live in `.github/prompts/<category>/` subdirectory (not directly in `.github/prompts/`)
3. **Template co-location** — All templates used by a prompt must be in `templates/<trigger>/` directory
4. **Script co-location** — All scripts used by a prompt must be in `scripts/<trigger>/` directory
5. **Trigger/folder match** — The `trigger:` field (without leading `/`) must exactly match the folder name in `templates/<trigger>/` and `scripts/<trigger>/`
6. **Assets verification** — Skills, scripts, specs, plans referenced in prompt must exist on disk
7. **Verification gates** — Only pass if all above checks pass AND plans-judge AND prompts-judge pass

### Changes to judge.py
- Add category validation (frontmatter `category:` matches parent dir name)
- Check prompt is in `.github/prompts/<category>/` not `.github/prompts/`
- Verify all `templates/` references point to `templates/<trigger>/`
- Verify all `scripts/` references point to `scripts/<trigger>/`
- Extract all skill/script/spec/plan references and verify existence
- Run plans-judge and prompts-judge as subprocesses, require PASS
- Score 0 if any hard requirement fails

### Changes to rubric.md
- New dimensions: Category Enforcement, Asset Co-location, Asset Verification, Cross-judge Gates
- Each dimension: PASS=20, FAIL=0 (hard gates)

## Phase 4: Fix Issues & Achieve ≥98 Score

### For each judge:
1. Run current judge on test data
2. Identify all issues/warnings/errors
3. Fix root causes in judge code and reference files
4. Create test fixtures that score 100
5. Verify all three judges score ≥98 on their respective corpuses

## Phase 5: Integration Testing
- Run all three judges in sequence
- Verify cross-validation works
- Ensure no circular dependencies
- Document any remaining edge cases

## Verification Gates
- [ ] specs-judge scores ≥98 on `.hermes/specs/`
- [ ] plans-judge scores ≥98 on `.hermes/plans/`
- [ ] prompts-judge scores ≥98 on `.github/prompts/`
- [ ] All hard gates pass (no FAIL ratings)
- [ ] Cross-validation between specs↔plans works
- [ ] Prompt asset verification works
- [ ] Template/script co-location enforced
- [ ] Category enforcement works