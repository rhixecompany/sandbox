# Approval Gate — Run All Goals Implementation

**Requestor**: Alexa
**Owner(s)**: Alexa
**Scope**: All files under `.github/prompts/general/run-all-goals/`, `.hermes/plans/`
**PRIMARY SOURCE**: tree.prompt.txt (cleanup-first execution)

## Justification
User explicitly authorized "create and run everything including goals and subgoals" with all destructive operations approved. tree.prompt.txt defines the cleanup-first pipeline.

### tree.prompt.txt Authorization Items
- `delete and cleanup .enhance,.goals,.hermes_diagnostics,.mcp,.*_cache,.worktrees,hermes-memory-safety,judge_results,logs,session-state,thoughts folders` (GOAL 1)
- `search,delete and cleanup *.json,*-report.md files expect for package.json,pyrightconfig.json` (GOAL 1)
- `update,refactor, and verify .editorconfig,.git-blame-ignore-revs,.gitattributes,.gitignore,.gitmodules,.markdownlint-cli2.jsonc,.markdownlint.jsonc,.pre-commit-config.yaml,.prettierignore,.prettierrc.json,*.toml,*.yaml` (GOAL 2)
- `search,delete and cleanup *.log,*.txt skip *.prompt.txt files` (GOAL 1)
- `convert,update,refactor, and verify *.mjs files into mts files` (GOAL 3)
- `cleanup, update, refactor, and verify *.md files including PLAN.md,SOUL.md,SPEC.md,USER.md and all files in docs` (GOAL 3)
- `update, refactor, and verify *.py,*.mjs,*.mts files including main.py,*.py files create a src directory an migrate files into src` (GOAL 3)
- `update, refactor, and verify requirements.txt,tsconfig.json` (GOAL 2)
- `update, refactor, and verify package.json,pyrightconfig.json,*.json files` (GOAL 2)

### General Authorization
- `hermes doctor --fix` (diagnostic repair)
- `hermes chat --yolo --oneshot` (model testing)
- `git push -u origin clean-development development production` (git operations)

## Rollback Plan
- `git checkout -- .github/prompts/general/run-all-goals/`
- `git checkout -- .hermes/plans/run-all-goals-implementation.md`
- `git checkout -- .hermes/scripts/`

## Verification Steps
1. Run `python scripts/verify_run_all_goals.py` — all checks PASS
2. Run `python scripts/test_run_all_goals.py` — all tests PASS (including tree-specific tests)
3. Run judge skills — all scores >= 99
4. Verify agent sync — 5 AI agents identical configs
5. Verify tree.prompt.txt as PRIMARY source in all artifacts
6. Verify mjs->mts conversion complete
7. Verify .enhance/.goals/.hermes_diagnostics deleted
8. Verify config files updated

## Authorization
- [x] User explicitly authorized all destructive operations
- [x] tree.prompt.txt authorization for all cleanup, config, mjs->mts operations
- [x] No further confirmation gates needed
- [x] SOUL.md Rule 6 compliance: all artifacts verified by real tool output
- [x] Cleanup-first approach verified: tree.prompt.txt phases 1-7 before agent sync and judge verification

Approval granted: 2026-09-10T13:27:00+00:00
Updated for tree-primary: 2026-09-10
