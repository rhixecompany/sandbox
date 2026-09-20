# Cross-Agent Initialization Plan

**Status:** COMPLETE  
**Run:** `init-copilot-hermes-opencode-cursor-agent-20260919T194300Z`

## Phases

1. **Prepare:** create this run and initialize all three artifacts.
2. **Audit:** inspect root and every `projects/*` agent adapter for stale references, missing Copilot surfaces, or policy conflicts.
3. **Implement:** update the canonical contract and only the adapters that need alignment; create missing project Copilot guidance.
4. **Verify:** run structure, reference, markdownlint, diff, and relevant project-local checks.
5. **Close:** record evidence, blockers, changed scope, and mark spec/plan/prompt complete only if all gates pass.

## Validation Matrix
| Gate          | Command or method                                                              | Required |
| ------------- | ------------------------------------------------------------------------------ | -------- |
| Structure     | Required root/project adapter and artifact paths exist                         | Yes      |
| References    | Resolve local Markdown links and reject stale `$HERMES_HOME.md` paths          | Yes      |
| Markdown      | `bunx markdownlint-cli2 --config .markdownlint-cli2.jsonc` on changed Markdown | Yes      |
| Diff          | `git diff --check`                                                             | Yes      |
| Project-local | Run local lint/type/test checks for materially changed projects                | Yes      |
## Current Status

- Audit completed: project adapters consistently delegated to root but used stale Hermes paths.
- Implementation in progress: bulk adapter alignment and missing MCP TypeScript Copilot adapter created.

## Final Status

- Root and project Copilot adapters were aligned to `../../.hermes.md` and the canonical root `AGENTS.md`.
- `projects/mcp-server-typescript/copilot-instructions.md` was created because that autonomous project had no Copilot adapter.
- Project-specific commands and overrides were preserved.
- Changed-file validation passed: markdownlint, `git diff --check`, structure checks, stale-reference checks, and local-link checks.
- Documentation-only changes did not require project code lint/type/test runs.
- Known blocker: broad recursive context lint reports 11 pre-existing issues outside the changed adapter set; no unrelated files were modified.
