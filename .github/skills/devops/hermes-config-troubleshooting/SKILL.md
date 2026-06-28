---
author: Hermes Agent
description: Diagnose Hermes config path resolution, hook discovery failures, and
  Windows-specific HERMES_HOME/profile overrides.
license: MIT
name: hermes-config-troubleshooting
tags:
- hermes
- config
- hooks
- windows
- troubleshooting
title: Hermes Config Troubleshooting
version: 1.0.0

---
# Hermes Config Troubleshooting

## When to Use

- `hermes hooks list` shows no hooks despite `hooks:` block in config
- `hermes plugins list` / `hermes mcp list` disagree with config file contents
- Config edits at `~/.hermes/config.yaml` appear ignored
- Windows path confusion between `~/.hermes` and `C:\Users\<user>\AppData\Local\hermes\`

## Symptoms

| Symptom | Likely cause |
|---------|--------------|
| `hermes hooks list`: "No shell hooks configured" | Config path mismatch or missing allowlist entries |
| `hermes doctor` clean but hooks don’t fire | `HERMES_HOME` overridden by profile/env |
| Config edits in workspace `.hermes/` not taking effect | Runtime uses profile data dir, not workspace |
| `shell-hooks-allowlist.json` missing | First-run consent not recorded; non-TTY skips registration |

## Diagnostic Steps

1. **Confirm active HERMES_HOME**
   - Run: `python -c "from hermes_constants import get_hermes_home; print(get_hermes_home())"`
   - Run: `python -c "from hermes_cli.config import get_config_path; print(get_config_path())"`
   - Compare against the config file you edited.

2. **Check both config paths**
   - `~/.hermes/config.yaml` (classic/default profile)
   - `C:\Users\<user>\AppData\Local\hermes\config.yaml` (active profile/runtime)
   - Only one is authoritative at runtime.

3. **Verify hook registration syntax**
   - `hooks:` must be top-level YAML with `enabled`, `events`, `script`
   - `script:` must be absolute Windows path (`C:\\Users\\...\\hook.sh`)

4. **Inspect allowlist state**
   - `~/.hermes/shell-hooks-allowlist.json` must contain `approvals:` entries for each `(event, command)` pair
   - Non-TTY sessions skip prompts; use `HERMES_ACCEPT_HOOKS=1` or `--accept-hooks`

5. **Profile override check**
   - `hermes profile list`
   - Named profiles set `HERMES_HOME` to `~/.hermes/profiles/<name>`
   - Workspace `.hermes/config.yaml` is NOT automatically the runtime config

## Windows-Specific Pitfalls

- `~/.hermes` does not exist until created; runtime may default to AppData profile dir
- Git Bash `$HOME` = `/c/Users/Alexa`, but Windows tools may read `%USERPROFILE%`
- Drive-letter paths in `script:` must use double backslashes or forward slashes
- Copying a config file into `~/.hermes/` does not change an already-running session

## Fix Patterns

**Pattern A: make AppData config the default**
- Copy `C:\Users\<user>\AppData\Local\hermes\config.yaml` → `~/.hermes/config.yaml`
- Verify with `hermes config check`
- Re-run `hermes hooks list` in a fresh session

**Pattern B: seed allowlist non-interactively**
- Write `~/.hermes/shell-hooks-allowlist.json` with `approvals: []`
- Set `HERMES_ACCEPT_HOOKS=1` for the session
- Use `hermes hooks test <event>` to validate

**Pattern C: align workspace docs with runtime**
- Document the actual active config path, not the assumption
- Update plan docs to reference `get_config_path()` output, not `~/.hermes/config.yaml`

## Verification

After any change:
1. `hermes config check` → version OK
2. `hermes hooks list` → shows expected hooks
3. `hermes hooks doctor` → passes syntax/allowlist/mtime checks
4. `hermes hooks test <event>` → synthetic payload succeeds


## Pitfalls

- **Stale cache:** Always re-read files from disk after editing; don't rely on cached context
- **Context limits:** Process in batches; write results after each batch
## Verification Checklist

- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has ≥3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md is under 250 lines
- [ ] No placeholder text

