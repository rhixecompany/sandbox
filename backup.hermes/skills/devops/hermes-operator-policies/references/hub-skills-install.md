# Hermes Hub Skills Installation

## Quick Reference

```bash
# Install a hub skill (non-interactive)
hermes skills install <identifier> --yes

# Search for skills
hermes skills search <query> --limit 10

# List installed skills
hermes skills list

# Inspect before installing
hermes skills inspect <identifier>
```

## Install Flow

1. **Fetch** — Downloads skill from hub to `.hub/quarantine/<name>/`
2. **Security scan** — Analyzes SKILL.md + all files for 8 threat categories
3. **Verdict** — SAFE, DANGEROUS, or BLOCKED per finding. Official/builtin source overrides even DANGEROUS verdicts to ALLOWED
4. **Install** — Copies from quarantine into `skills/<name>/`

## Security Scan Verdicts

| Verdict | Meaning |
|---------|---------|
| SAFE | No findings above MEDIUM. Installs cleanly. |
| DANGEROUS + ALLOWED | Findings exist but source is trusted (official/builtin). Confirmation prompt unless `--yes` used. |
| BLOCKED | Community source + DANGEROUS verdict = blocked. `--force` does not override. |

## PITFALL: Interactive Prompt Cancels Install

`hermes skills install <id>` prompts `Confirm [y/N]:`. In automation or batch context, this **silently cancels** the install. Always pass `--yes` (or `-y`):

```bash
# BAD — hangs waiting for input
hermes skills install official/devops/docker-management

# GOOD — non-interactive
hermes skills install official/devops/docker-management --yes
```

## PITFALL: Platform Filtering on Windows

Skills declaring `platforms: [linux, macos]` in SKILL.md frontmatter install to disk successfully but **do not appear in `hermes skills list`** on Windows. The skill is physically at `skills/<name>/` but Hermes filters it from the active set.

Check for this if a skill installs cleanly but doesn't show up:

```bash
# Verify on disk
ls ~/AppData/Local/hermes/skills/<name>/SKILL.md

# Check platform declaration
grep platforms: ~/AppData/Local/hermes/skills/<name>/SKILL.md
```

Workaround: edit the SKILL.md to include `windows` in the platforms list — but this may cause runtime issues if the skill's scripts are Linux/macOS-only.

## Scan Category Summary

The scanner checks 8 categories. Common hits for hub skills:
- **exfiltration** — reading env vars for tokens, making outbound HTTP requests with auth headers
- **persistence** — writing config files, registering auto-start items
- **privilege_escalation** — group membership changes, sudoing
- **supply_chain** — downloading packages from registries
- **network** — connecting to hosts or binding ports
- **execution** — dynamic code evaluation patterns
- **credential_theft** — accessing credential stores
- **data_loss** — destructive file operations

Skills dealing with APIs/tokens commonly flag exfiltration. Official builtin source overrides the block — the scan is informational for trusted sources.
