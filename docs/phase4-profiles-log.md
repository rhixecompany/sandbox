# Phase 4 – Profiles & Workspace Markdown

## Executed
- Verified `sample.prompt.md` profile list and target profile names.
- Checked available profile CLI: `list`, `use`, `create`, `delete`, `describe`, `show`, `alias`, `rename`, `export`, `import`, `install`, `update`, `info`.
- Attempted profile creation using `hermes profile create <profile name>` for listed names.
- **FIXED:** `hermes profile create <name> --clone-all` now works (was timing out before, now completes in ~5s).
- Created 7 profiles with full clone from `default`:
  - `default` (primary, model: gpt-5.4-mini via Codex)
  - `adminbot` (pre-existing, model: stepfun/step-3.7-flash:free)
  - `code-architect` (implementation tasks)
  - `research-analyst` (research/synthesis tasks)
  - `creative-director` (creative work)
  - `exec-assistant` (administrative workflows)
  - `patient-tutor` (teaching/explanations)

## What `--clone-all` Copies (Verified)
| Component | Copied? | Details |
|-----------|---------|---------|
| `.env` | ✅ | API keys, secrets (24KB) |
| `config.yaml` | ✅ | Full config including hooks, plugins, MCP servers (18KB) |
| `hooks/` | ✅ | 3 hooks: governance-audit, session-auto-commit, session-logger |
| `plugins/` | ✅ | 5 plugins: awesome-hermes-agent, disk-cleanup, memory/honcho, model-providers/openrouter, security-guidance |
| `skills/` | ✅ | All 289 skills from .github/skills/ (not just 73 bundled) |
| `mcp_servers` | ✅ | 10 MCP servers with tool filtering |
| `SOUL.md` | ✅ | Personality file (643 bytes) |
| `memories/` | ✅ | Memory directory structure |
| Wrapper scripts | ✅ | `.bat` files in `~/.local/bin/` |

## Profile List (Verified)
```bash
hermes profile list
```
Output:
```
Profile            Model                      Gateway      Alias            Distribution
───────────────    ───────────────────────────    ───────────    ───────────    ────────────────────
◆default           gpt-5.4-mini                 stopped      —                —
 adminbot           stepfun/step-3.7-flash:free  stopped      adminbot         —
 code-architect     gpt-5.4-mini                 stopped      code-architect   —
 creative-director  gpt-5.4-mini                 stopped      creative-director —
 exec-assistant     gpt-5.4-mini                 stopped      exec-assistant   —
 patient-tutor      gpt-5.4-mini                 stopped      patient-tutor    —
 research-analyst   gpt-5.4-mini                 stopped      research-analyst —
```

## Next
Proceed to Phase 5 – Docs Inventory (complete). Phase 6 – Configuration Hierarchy Audit updated to reflect full clone capability.