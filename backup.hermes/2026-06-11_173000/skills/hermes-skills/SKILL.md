---
name: hermes-skills
description: Skill discovery, creation, hub installation, and management
version: 1.0.0
platforms: [macos, linux, windows]
metadata:
  hermes:
    tags: [hermes, skills, skill-management]
    category: skills
    requires_toolsets: [terminal, file, skills]
    config:
      - key: hermes.skill.skills.enabled
        description: "Enable skills management skill"
        default: "true"
---

# Hermes Skills Management Skill

## When to Use
- Discovering available skills
- Creating custom skills
- Installing skills from agentskills.io hub
- Managing skill lifecycle (update, delete, curator)

## Procedure
1. **List Available Skills**:
   ```bash
   /skills                    # In chat - browse installed
   hermes skills list         # CLI
   hermes skills view <name>  # View specific skill
   ```

2. **Use a Skill** (slash command):
   ```bash
   /gif-search funny cats
   /axolotl help me fine-tune Llama 3
   /github-pr-workflow create PR for auth refactor
   /plan design rollout for auth migration
   /excalidraw                # Loads and prompts for intent
   ```

3. **Install from Hub** (agentskills.io / official registry):
   ```bash
   /skill install                # Interactive picker
   hermes skills install <name>  # CLI (note: plural 'skills')
   hermes skills install <name> --yes   # Skip confirmation (batch mode)
   ```
   - **Security scan runs automatically** on every install. Official/builtin sources are auto-allowed. Community sources with DANGEROUS verdicts are BLOCKED (cannot be overridden with `--force`). Community sources with CAUTION verdicts require `--force`.
   - **Batch install pattern:** Use a bash loop with `--yes` for bulk installs. See `references/batch-install.md`.
   - **Correct command is `hermes skills install`** (plural), NOT `hermes skill install`.

4. **Create Custom Skill**:
   ```bash
   hermes skill create my-skill
   # Scaffolds ~/.hermes/skills/my-skill/ with SKILL.md + references/
   ```

5. **SKILL.md Format** (required fields):
   ```yaml
   ---
   name: my-skill
   description: Brief description
   version: 1.0.0
   platforms: [macos, linux, windows]
   metadata:
     hermes:
       tags: [category]
       category: devops
       requires_toolsets: [terminal]
   ---
   # Skill Title
   ## When to Use
   - Trigger condition
   
   ## Procedure
   1. Step one
   2. Step two
   
   ## Pitfalls
   - Known failure: fix
   
   ## Verification
   How to confirm it worked
   ```

6. **Manage Skills**:
   ```bash
   /skill update              # Check for updates
   hermes skills opt-out      # Stop bundled skill seeding
   hermes skills opt-out --remove  # Also remove unmodified bundled
   hermes skills opt-in --sync # Re-enable seeding
   ```

## Pitfalls
- **Skill not showing in `/skills`** → Check `platforms` field; verify SKILL.md syntax; restart Hermes
- **Slash command not working** → Ensure skill directory name matches `name` field; restart Hermes
- **Hub install fails** → Check network; verify `agentskills.io` reachable
- **Version conflict** → Run `/skill update` or manually delete and reinstall
- **`hermes skill install` (singular) fails** → The command is `hermes skills install` (plural). This is the #1 gotcha.
- **`hermes skills browse` truncates names/identifiers** → The table ellipsizes (`…`) long names and identifiers. Use `hermes skills inspect <identifier>` for full details, or parse the output with care (identifiers wrap across lines).
- **Audit marks installed official skills as BLOCKED** → `hermes skills audit` re-scans installed skills as "community" source. Skills reading env vars (API tokens), running shell commands, or installing packages get flagged DANGEROUS. This is expected — BLOCKED audit status is informational, NOT a functional disablement. Skills remain enabled and usable.
- **`--force` doesn't override DANGEROUS verdicts** → It only works for CAUTION. DANGEROUS verdicts on community skills are always blocked. For official skills already installed, this doesn't matter (they're already functional).
- **`skills-sh` and `browse-sh` sources show identical official skill lists** → Different source flags, same underlying registry. Prefer `--source official` for the curated Nous Research set.

## Verification
- `hermes skills list` returns the skill
- `/skillname` loads and works
- `hermes skills view <name>` returns full content
- References load with `hermes skills view <name> "references/file.md"`

## References
- `references/commands.md` — CLI commands reference (browse, search, install, audit)
- `references/skill-format.md` — Complete SKILL.md specification
- `references/curator.md` — Autonomous curator (7-day cycle)
- `references/batch-install.md` — Bulk install pattern for many skills at once
- `references/audit-results.md` — Understanding audit BLOCKED vs ALLOWED verdicts