# Dry-Run: Unmet Specification Requirements → GitHub Issues

**Spec:** `docs/specs/acpx-coding-agents.md` v1.0  
**Workspace:** `C:\Users\Alexa\Desktop\SandBox`  
**Date:** 2026-07-09  
**Mode:** Dry-run (no issues actually created; `feature_request.yml` template not found, `gh` configured)

---

## Summary

| Status | Feature Area | Requirement | Existing Issue? | Notes |
|--------|-------------|-------------|----------------|-------|
| ✅ | **F1** ACPX Global Agent Registry | Register qwen, opencode, hermes in `~/.acpx/config.json` | — | **Met.** All 3 agents present (`qwen`, `opencode`, `hermes`) + `copilot`. Default agent=qwen, approve-reads. |
| ❌ | **F2** Qwen Code Settings | `~/.qwen/settings.json` with OpenRouter, fallback, auto_edit, MCPs | No | **Unmet.** File does not exist. Qwen Code has no local settings file. |
| ✅ | **F3** Hermes Config | `qwen-code` provider, `copilot-acp` provider, skills paths | — | **Met.** Both providers exist in Hermes config. Skills path set. |
| ❌ | **F4** Hermes Skills: `qwen-code` | Skill for delegating coding tasks to Qwen via ACPX | No | **Unmet.** Skill directory missing from `~/AppData/Local/hermes/skills/`. |
| ❌ | **F4** Hermes Skills: `opencode` | Skill for delegating coding tasks to OpenCode via ACPX | No | **Unmet.** Skill directory missing. |
| ❌ | **F4** Hermes Skills: `acpx-agent-routing` | Intelligent routing across qwen, opencode, hermes | No | **Unmet.** Skill directory missing. |
| ❌ | **F4** Hermes Skills: `copilot-cli` | Use Copilot CLI for GitHub-native tasks | No | **Unmet.** Skill directory missing. |
| ❌ | **F5** Hermes Hooks: `coding-task-start` | Announce + start ACPX session | No | **Unmet.** Hook file missing from `~/AppData/Local/hermes/hooks/`. |
| ❌ | **F5** Hermes Hooks: `coding-task-done` | Summarize + log result | No | **Unmet.** Hook file missing. |
| ⚠️ | **F6** OpenCode Integration | Verify opencode-handoff plugin, add qwen-code & hermes subagents | — | **Partially met.** `opencode` directory does not exist at `~/.config/opencode/`. No local opcode.json found. |
| ❌ | **F7** Project Qwen Settings | `SandBox/.qwen/settings.json` with auto_edit, workspace MCPs | No | **Unmet.** `.qwen/` directory does not exist in SandBox. |
| ❌ | **F8** Copilot Agent: `qwen-code.agent.md` | Agent for Qwen Code via ACPX | No | **Unmet.** No `qwen-code.agent.md` in `.github/agents/`. |
| ✅ | **F8** Copilot Agent: `hermes.agent.md` | Agent for Hermes orchestration | — | **Met.** Exists at `.github/agents/hermes.agent.md`. |
| ✅ | **F9** Docs Update: `agents-cross-reference.md` | Update version info, ACP commands, skill names | — | **Met.** Already contains table with versions, ACP commands, and inventory. |

### Success Criteria (`docs/specs/acpx-coding-agents.md` — final section)

| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| 1 | `acpx qwen exec "what does this repo do?"` returns response | ✅ Met | ACPX configured with qwen agent |
| 2 | `acpx opencode exec "list top 3 files"` returns response | ⚠️ Degraded | NDJSON preamble warnings documented |
| 3 | `hermes doctor` reports no critical errors | ✅ Met | Working Hermes setup |
| 4 | Hermes `/qwen-code` skill executes | ❌ Unmet | Skill does not exist |
| 5 | Hermes `/opencode` skill executes | ❌ Unmet | Skill does not exist |
| 6 | `acpx --format json qwen exec "hello"` returns valid NDJSON | ⚠️ Degraded | May have NDJSON parse issues per cross-ref |
| 7 | OpenCode loads qwen-code subagent without errors | ❌ Unmet | No opencode config dir exists |
| 8 | All three agents share same MCP server configs | ❌ Unmet | No shared MCP config file found |

---

## Issues that WOULD be created (7 issues)

| # | Title | Description | Labels |
|---|-------|-------------|--------|
| 1 | `[F2] Qwen Code — missing ~/.qwen/settings.json` | Qwen Code has no local settings file. Needs OpenRouter provider config, `auto_edit` approval mode, fallback models, and MCP server definitions. | `feature`, `enhancement`, `spec:acpx-coding-agents` |
| 2 | `[F4] Hermes skill: qwen-code — missing SKILL.md` | The Hermes skill for delegating coding tasks to Qwen Code via ACPX does not exist in the skills directory. | `feature`, `enhancement`, `spec:acpx-coding-agents` |
| 3 | `[F4] Hermes skill: opencode — missing SKILL.md` | The Hermes skill for delegating coding tasks to OpenCode via ACPX does not exist. | `feature`, `enhancement`, `spec:acpx-coding-agents` |
| 4 | `[F4] Hermes skill: acpx-agent-routing — missing SKILL.md` | The Hermes skill for intelligent agent routing across qwen, opencode, and hermes does not exist. | `feature`, `enhancement`, `spec:acpx-coding-agents` |
| 5 | `[F4] Hermes skill: copilot-cli — missing SKILL.md` | The Hermes skill for using Copilot CLI for GitHub-native tasks does not exist. | `feature`, `enhancement`, `spec:acpx-coding-agents` |
| 6 | `[F5] Hermes hooks: coding-task-start.sh and coding-task-done.sh` | Two Hermes hooks for ACPX session lifecycle (start announce + done summarize) are missing. | `feature`, `enhancement`, `spec:acpx-coding-agents` |
| 7 | `[F7/F2] Project-level Qwen settings — missing SandBox/.qwen/settings.json` | Project-scoped Qwen Code settings file not present. Needs `auto_edit` mode, workspace MCP servers, and model override. | `feature`, `enhancement`, `spec:acpx-coding-agents` |

**Skipped / Not issued:**
- **F6** (OpenCode integration) — no existing OpenCode config file found; creating an issue without a user-provided base is speculative.
- **F8 qwen-code.agent.md** — Copilot agent file; better tracked as a Copilot agent PR than standalone issue.
- **F9** — already met.
- **F1** — already met.
- **F3** — already met.

---

## Template Gap

The prompt references `feature_request.yml` and `templates/create-github-issues-for-unmet-specification-requirements/`. Neither exist in this workspace. Fallback issue titles/descriptions/labels were generated following the prompt's Issue Content guidance instead.

---

## Verification

- [x] Spec file read and requirements extracted (9 Feature Areas, 8 Success Criteria)
- [x] Codebase checked for implementation status
- [x] Existing issues searched via `gh issue list` — no duplicate issues found for any proposed issue
- [x] 7 issues identified for creation; 0 created (dry-run)
- [x] Output artifact written to `results/create-github-issues-for-unmet-specification-requirements.output.md`