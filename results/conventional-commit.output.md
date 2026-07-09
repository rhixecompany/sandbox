# Conventional Commit — Output

**Mode:** REAL artifact (analysis of actual uncommitted workspace changes)
**Repo:** `C:\Users\Alexa\Desktop\SandBox` — branch `development`
**Generated:** 2026-07-09

## Change Summary (from `git status` / `git diff --stat`)

- 72 files changed, **1185 insertions(+), 1284 deletions(-)**
- Rewrote/expanded `AGENTS.md`, `SESSION_REPORT.md`, `docs/dedupe-report.md`
- Updated 7 `.github/agents/*.agent.md` definitions + `.vscode/mcp.json`
- Deleted 45 `judge_results/batch_*_results.md` files (dedupe cleanup)
- Normalized `.vscode/extensions.json` across ~10 subprojects
- Added helper scripts: `lcs.py`, `projects/Banking/bin/utils/get-connection-string.ts`

## Recommended Commit Message

```
chore(repo): consolidate agent docs and prune judge batch results

Rewrite root AGENTS.md into full agent-guidance doc and refresh
.github/agents definitions, mcp.json, and session/dedupe reports.
Remove 45 stale judge_results batch files superseded by summary.md.
Normalize .vscode/extensions.json across subprojects and add
lcs.py plus Banking connection-string helper.

BREAKING CHANGE: none
```

## Structured XML Form

```xml
<commit>
  <type>chore</type>
  <scope>repo</scope>
  <description>consolidate agent docs and prune judge batch results</description>
  <body>
    Rewrite root AGENTS.md into full agent-guidance doc and refresh
    .github/agents definitions, mcp.json, and session/dedupe reports.
    Remove 45 stale judge_results batch files superseded by summary.md.
    Normalize .vscode/extensions.json across subprojects and add
    lcs.py plus Banking connection-string helper.
  </body>
  <footer>none</footer>
</commit>
```

## Alternative (split into focused commits)

1. `docs(agents): rewrite AGENTS.md and refresh .github/agents definitions`
2. `chore(judge): remove 45 stale batch result files (superseded by summary.md)`
3. `chore(vscode): normalize extensions.json recommendations across subprojects`
4. `feat(banking): add get-connection-string helper util`

## Validation

- ✅ Type is a valid Conventional Commits type (`chore`)
- ✅ Description ≤ 72 chars, imperative mood, no trailing period
- ✅ Body wraps at ~72 cols, explains what + why
- ✅ Footer declares no breaking change
- Note: change set is broad; the split-commit option is preferred for a cleaner history.
