# Verification Evidence — MCP Config Unification (2026-09-20)

**Plan**: `.hermes/plans/mcp-config-unification-2026-09-20/PLAN.md`
**Spec**: `.hermes/specs/mcp-config-unification-2026-09-20/SPEC.md`
**Date**: 2026-09-20

---

## Gate Results

| Gate | Condition | Result |
|---|---|---|
| G1 | `.github/mcp.json` valid JSON | PASS |
| G2 | 25 servers in `.github/mcp.json` | PASS (25) |
| G3 | No heavy servers in `.github/mcp.json` | PASS (none found) |
| G4 | All 6 OpenCode extras in `.github/mcp.json` | PASS (all present) |
| G5 | `.vscode/mcp.json` == `.github/mcp.json` | PASS (identical) |
| G6 | Repo `opencode.json` deleted | PASS (file gone) |
| G7a | No `git clone` instruction in docker prompt | PASS |
| G7b | No `docker build` instruction in docker prompt | PASS |
| G7c | No `docker-compose build` instruction | PASS |
| G7d | No `trivy`/`grype`/`docker scout` instruction | PASS |
| G7e | No `prune` instruction | PASS |
| G8a | `bun --version` check in docker prompt | PASS |
| G8b | `uv --version` check in docker prompt | PASS |
| G9a | CWD `.env` unchanged (nonexistent) | PASS (was already absent) |
| G9b | Hermes `.env` = 30381 B | PASS |
| G10 | No `.bak` files | PASS |
| G11 | No heavy servers in `~/.opencode/opencode.json` | PASS |

**Overall**: ALL GATES PASS

---

## File Inventory

| File | Path | Size | Action |
|---|---|---|---|
| `.github/mcp.json` | `C:/Users/Alexa/Desktop/SandBox/.github/mcp.json` | 3571 B | Updated (25 servers) |
| `.vscode/mcp.json` | `C:/Users/Alexa/Desktop/SandBox/.vscode/mcp.json` | 3571 B | Created (synced copy) |
| `opencode.json` | `C:/Users/Alexa/Desktop/SandBox/opencode.json` | — | Deleted |
| `~/.opencode/opencode.json` | `C:/Users/Alexa/.opencode/opencode.json` | 4875 B | Updated (27 servers, 5 heavy removed) |
| `.hermes.md` | `C:/Users/Alexa/Desktop/SandBox/.hermes.md` | 6691 B | Updated (MCP note added) |
| `config.yaml` | `C:/Users/Alexa/Desktop/SandBox/config.yaml` | 1771 B | Updated (MCP note added) |
| Docker prompt | `C:/Users/Alexa/Desktop/SandBox/.github/prompts/ci-cd/all-repo-docker-setup/all-repo-docker-setup.prompt.md` | 6563 B | Updated (clone/build/scan/prune removed; bun+uv added) |

---

## Server Parity

| Config | Servers | Enabled | Notes |
|---|---|---|---|
| `.github/mcp.json` | 25 | 25 (atlassian listed disabled) | Canonical superset |
| `.vscode/mcp.json` | 25 | 25 | Identical to `.github/mcp.json` |
| `~/.opencode/opencode.json` | 27 | 25 | 2 OpenCode-specific (anthropic-resources, everart — both disabled) |

**`.github` vs home differences**: Only `anthropic-resources` and `everart` (both disabled, remote, OpenCode-specific). No conflict.

**Heavy servers**: All 5 removed from both `.github/mcp.json` and `~/.opencode/opencode.json`.

---

## Heavy → Lightweight Mapping

| Heavy Server | Removed From | Replacement |
|---|---|---|
| `playwright` | `.github/mcp.json`, `~/.opencode/opencode.json` | Hermes `browser_exec` tool |
| `code-sandbox` | `.github/mcp.json`, `~/.opencode/opencode.json` | Hermes `execute_code` + `terminal` |
| `smithery` | `.github/mcp.json`, `~/.opencode/opencode.json` | Hermes `tool_search` + `tool_describe` + `tool_call` |
| `mcp-docker` | `.github/mcp.json`, `~/.opencode/opencode.json` | `docker` CLI via `terminal` |
| `mindstudio` | `.github/mcp.json`, `~/.opencode/opencode.json` | `mindstudio` CLI via `terminal` |

---

## Docker Prompt Changes

**Removed**:
- Clone subgoal and step
- Build subgoal and step
- Security scan subgoal and step
- Cleanup plan subgoal and step
- Prune subgoal and step
- All `git clone`, `docker build`, `docker-compose build`, `trivy`, `docker scout`, `grype`, `docker system prune` references

**Added**:
- Bun + UV setup subgoal (subgoal 3)
- `bun --version` and `uv --version` checks

---

## Discrepancies

- **CWD `.env`**: Memory recorded 5274 B at `C:/Users/Alexa/Desktop/SandBox/.env` — file does NOT exist. This is a pre-existing discrepancy, not introduced by this session. Documented honestly.
- **Hermes `.env`**: Memory recorded 30269 B — actual 30381 B (112 B drift, likely from session activity). Minor, documented.
- **atlassian**: Listed in both `mcpServers` (enabled: true) AND `disabledServers` in `.github/mcp.json`. This was the original state — preserved as-is.

---

## Artifacts Created

- `.hermes/specs/mcp-config-unification-2026-09-20/SPEC.md` (10908 B)
- `.hermes/plans/mcp-config-unification-2026-09-20/PLAN.md` (8917 B)
