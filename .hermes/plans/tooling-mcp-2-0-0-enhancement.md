# Plan: Enhance Tooling MCP Servers → mcp==2.0.0 + uv/uvx/uvm

Profile: adminbot | Workspace: ~/Desktop/SandBox | Date: 2026-09-10
Root: SESSION_REPORT.md verified; 5 mandatory skills loaded; using-superpowers loaded.

## Scope (multi-file >=14 skill stack invoked conceptually)
- Upgrade all tooling MCP servers (python-quality, tooling-config, tooling-lint) to `mcp==2.0.0`
- Update virtualenv `~/myvenv` (C:\Users\Alexa\myvenv) with uv/uvx/uvm
- Fix all debts/bugs/warnings/errors across hermes, opencode, copilot, codex configs
- Verify with actual tool outputs, not descriptions

## Phase Checklist (Strict Sequential — "only then")

Phase A: Discovery / State Audit (current)
- [x] Read SESSION_REPORT.md, SOUL.md, USER.md, MEMORY.md, .hermes.md
- [x] Read current package versions (requirements.txt shows mcp==1.29.1, mcp-types==2.0.0)
- [x] Inspect .mcp/, .opencode/, .copilot/, .vscode/mcp.json
- [x] Inspect hermes profiles, scripts
- [ ] Run uv --version, uvx --version; verify ~/myvenv exists

Phase B: Virtualenv + Package Upgrade
- [ ] Create/update ~/myvenv via uv
- [ ] `uv pip install -U "mcp==2.0.0"` in venv
- [ ] Update requirements.txt (mcp==2.0.0)
- [ ] Update .env / .opencode references

Phase C: MCP Server Config Updates (all 4 profiles/tools)
- [ ] Update .opencode/opencode.json (mcp server commands / PYTHONPATH / UV)
- [ ] Update .vscode/mcp.json
- [ ] Update hermes profile config.yaml MCP server args (YAML list format per MEMORY.md rule)
- [ ] Update .hermes.md references
- [ ] Update .omo/templates/myvenv-reference.md

Phase D: Cross-Profile Sync (hermes, copilot, codex, open/oh-my-opencode)
- [ ] Sync config.yaml, .env, PYTHONPATH, MCP_VERSION=2.0.0, UV_USE=true, UVM_ACTIVE=~/myvenv
- [ ] Verify with verify_sync.py / multi-agent-sync (65 checks)
- [ ] Fix any debt: missing frontmatter, broken links, stale model refs

Phase E: Debug / Fix Every Debt, Bug, Issue, Warning
- [ ] Inspect .enhance/, scripts/, skills/
- [ ] Run ruff format+check --fix
- [ ] Run bun lint / format:check / markdownlint / typecheck
- [ ] Fix any errors found (limit 3 attempts/file per SOUL.md)
- [ ] Inspect session-logger, hooks, desktop plugins for errors
- [ ] Inspect logs/ for warnings

Phase F: Verification Gates (must pass before claim complete)
- [ ] `hermes config check` passes
- [ ] `hermes profile use adminbot` routed correctly
- [ ] `hermes mcp list` shows updated tooling servers with mcp==2.0.0
- [ ] `python -c "import mcp; print(mcp.__version__)"` reports 2.0.0 in ~/myvenv
- [ ] `uv --version`, `uvx --version`, `uvm --version` verified
- [ ] No fabricated output; all claims backed by tool output
- [ ] SESSION_REPORT.md updated with findings

## Constraints / Non-Negotiable
- No inline scripts; use scripts/ dir (SOUL.md Rule 4)
- No destructive branch/commit/delete unless explicitly told (SOUL.md Rule 11)
- No secrets printed (Rule 12)
- Never invent package version data; verify via uv pip list / python -c
- Stop at verification gate failures; don't autopilot through
- If same file edit fails twice, switch to full rewrite (SOUL.md)

## Debts / Warnings to Resolve (inferred from workspace context)
- requirements.txt: mcp==1.29.1 (needs 2.0.0)
- mcp-types==2.0.0 present but mcp package behind
- Memory: `config.yaml mcp_servers args must be YAML list` — audit all mcp server arg lists
- .hermes.md references `~/myvenv` but no verified ~/myvenv exists (check C:\Users\Alexa\myvenv)
- OpenCode v4.19.4 / Zen pool references may need refresh
- Hooks/plugins audit may reveal missing event coverage
