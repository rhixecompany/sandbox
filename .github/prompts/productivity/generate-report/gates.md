# Gates for Create Feature

## Gate 1: Preparation Complete
- **Criteria**: All Phase 1 tasks verified
- **Check**: ls .hermes/plans/create-feature-plan.md && pytest tests/ -v
- **Pass Condition**: Plan exists, tests failing (RED state)
- **Fail Action**: Re-analyze requirements, recreate plan

## Gate 2: Execution Complete
- **Criteria**: All Phase 2 tasks verified
- **Check**: pytest tests/ -v && lint checks
- **Pass Condition**: All tests passing, lint clean
- **Fail Action**: Fix failing tests, address lint issues

## Gate 3: Verification Complete
- **Criteria**: All gates pass
- **Check**: Full test suite + integration tests
- **Pass Condition**: All ACs met
- **Fail Action**: Re-execute failed phases

## Gate 4: Completion Verified
- **Criteria**: All artifacts created, validated
- **Check**: git diff --stat && CI status
- **Pass Condition**: Zero errors, all ACs met
- **Fail Action**: Full rollback
