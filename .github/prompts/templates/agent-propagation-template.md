# Agent Propagation Template

**Propagation Date**: {{TIMESTAMP}}
**Session**: {{SESSION_ID}}
**Propagator**: {{PROPAGATOR}}

## Primary Model & Fallback Chain (Source of Truth)

| Setting | Value |
|---|---|
| Primary Provider | {{PRIMARY_PROVIDER}} |
| Primary Model | {{PRIMARY_MODEL}} |
| Fallback Providers | {{FALLBACK_PROVIDERS}} |

## Files to Update

### Hermes Profiles

| File | Status | Current Model Ref | Target Model Ref | Command |
|---|---|---|---|---|
| `~/AppData/Local/hermes/profiles/default/SOUL.md` | {{DEFAULT_SOUL_STATUS}} | {{DEFAULT_SOUL_CURR}} | {{DEFAULT_SOUL_TARGET}} | {{DEFAULT_SOUL_CMD}} |
| `~/AppData/Local/hermes/profiles/default/memories/USER.md` | {{DEFAULT_USER_STATUS}} | {{DEFAULT_USER_CURR}} | {{DEFAULT_USER_TARGET}} | {{DEFAULT_USER_CMD}} |
| `~/AppData/Local/hermes/profiles/default/memories/MEMORY.md` | {{DEFAULT_MEM_STATUS}} | {{DEFAULT_MEM_CURR}} | {{DEFAULT_MEM_TARGET}} | {{DEFAULT_MEM_CMD}} |
| `~/AppData/Local/hermes/profiles/alexa/SOUL.md` | {{ALEXA_SOUL_STATUS}} | {{ALEXA_SOUL_CURR}} | {{ALEXA_SOUL_TARGET}} | {{ALEXA_SOUL_CMD}} |
| `~/AppData/Local/hermes/profiles/alexa/memories/USER.md` | {{ALEXA_USER_STATUS}} | {{ALEXA_USER_CURR}} | {{ALEXA_USER_TARGET}} | {{ALEXA_USER_CMD}} |
| `~/AppData/Local/hermes/profiles/alexa/memories/MEMORY.md` | {{ALEXA_MEM_STATUS}} | {{ALEXA_MEM_CURR}} | {{ALEXA_MEM_TARGET}} | {{ALEXA_MEM_CMD}} |
| `~/AppData/Local/hermes/profiles/code-architect/SOUL.md` | {{CA_SOUL_STATUS}} | {{CA_SOUL_CURR}} | {{CA_SOUL_TARGET}} | {{CA_SOUL_CMD}} |
| `~/AppData/Local/hermes/profiles/code-architect/memories/USER.md` | {{CA_USER_STATUS}} | {{CA_USER_CURR}} | {{CA_USER_TARGET}} | {{CA_USER_CMD}} |
| `~/AppData/Local/hermes/profiles/code-architect/memories/MEMORY.md` | {{CA_MEM_STATUS}} | {{CA_MEM_CURR}} | {{CA_MEM_TARGET}} | {{CA_MEM_CMD}} |
| ... (all profiles) | | | | |

### Workspace Context Files

| File | Status | Current Model Ref | Target Model Ref | Command |
|---|---|---|---|---|
| `C:\Users\Alexa\Desktop\SandBox\.hermes.md` | {{HERMES_MD_STATUS}} | {{HERMES_MD_CURR}} | {{HERMES_MD_TARGET}} | {{HERMES_MD_CMD}} |
| `C:\Users\Alexa\Desktop\SandBox\AGENTS.md` | {{AGENTS_MD_STATUS}} | {{AGENTS_MD_CURR}} | {{AGENTS_MD_TARGET}} | {{AGENTS_MD_CMD}} |
| `C:\Users\Alexa\Desktop\SandBox\.github\copilot-instructions.md` | {{COPILOT_INST_STATUS}} | {{COPILOT_INST_CURR}} | {{COPILOT_INST_TARGET}} | {{COPILOT_INST_CMD}} |
| `C:\Users\Alexa\Desktop\SandBox\CLAUDE.md` | {{CLAUDE_MD_STATUS}} | {{CLAUDE_MD_CURR}} | {{CLAUDE_MD_TARGET}} | {{CLAUDE_MD_CMD}} |

### External Agent Configs

| File | Status | Current Model Ref | Target Model Ref | Command |
|---|---|---|---|---|
| `~/.opencode/mcp.json` | {{OPENCODE_STATUS}} | {{OPENCODE_CURR}} | {{OPENCODE_TARGET}} | {{OPENCODE_CMD}} |
| `~/.codex/mcp.json` | {{CODEX_STATUS}} | {{CODEX_CURR}} | {{CODEX_TARGET}} | {{CODEX_CMD}} |

## Propagation Rules Checklist

- [ ] Only models with `working=true` from ranking are used
- [ ] `hermes config set` CLI used for Hermes config (not raw YAML)
- [ ] Profile SOUL.md files updated with new model references
- [ ] Profile USER.md/MEMORY.md files updated if they contain model refs
- [ ] Workspace context files (.hermes.md, AGENTS.md, etc.) updated
- [ ] External agent configs updated if they reference models
- [ ] No secrets/tokens introduced in any file
- [ ] All changes recorded with file path and command used
- [ ] Git diff shows only intended changes

## Commands Executed

```bash
{{COMMAND_1}}
{{COMMAND_2}}
{{COMMAND_3}}
...
```

## Verification After Propagation

```bash
# Verify Hermes profiles
hermes profile list

# Verify workspace files
grep -r "{{PRIMARY_MODEL}}" C:\Users\Alexa\Desktop\SandBox\.hermes.md C:\Users\Alexa\Desktop\SandBox\AGENTS.md

# Verify external agents (if accessible)
cat ~/.opencode/mcp.json | grep -i model
cat ~/.codex/mcp.json | grep -i model
```

## Rollback Plan

If propagation causes issues:

```bash
# Restore from git
git checkout HEAD -- {{AFFECTED_FILES}}

# Or restore Hermes config
hermes config set model.provider "{{OLD_PROVIDER}}"
hermes config set model.default "{{OLD_MODEL}}"
hermes config set fallback_providers '{{OLD_FALLBACK}}'
```

## Notes

{{PROPAGATION_NOTES}}

---

*Fill in during Phase 6 execution. Save as `propagation/agent-propagation-{{TIMESTAMP}}.md`*