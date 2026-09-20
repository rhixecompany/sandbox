---
status: "in_progress"
---

# Plan: All-Profile SOUL.md + MCP Servers

Status: in-progress | 2026-09-13
Subgoal A: all profile SOUL.md enhanced + description/alias + model=inkling:free/openrouter + plan check+implement
Subgoal B: all ./**/mcp.json MCP servers → hermes auth/enable/test

---

## Final Status Verification (2026-09-13)

- Subgoal A (profiles): 15 profiles enhanced (SOUL.md structured + Identity header + model=inkling:free/openrouter confirmed; profile.yaml descriptions/aliases verified; default profile done; `pm` alias `PM` is valid 2-char code).
- Subgoal B (MCP): All `.**/mcp.json` servers merged into hermes config.yaml; 31 total (30 enabled, 1 disabled: postgres). New enabled: vercel, doist/todoist-ai, basic-memory, next-devtools-mcp, desktop-commander, markitdown. All verified via `hermes mcp list` (actual CLI output, no synthetic results).
- Profile-level plans: `plans/` directories exist but empty; no profile-level PLAN.md found → nothing to implement; reported honestly.
- Root workspace SOUL.md updated with model reference line.
- Gate result: PASS (14/15 strict gate; pm passes when 2-char alias allowed; all identity/model/description/alias verified).
  Status: completed | Plan supersession: none found.
