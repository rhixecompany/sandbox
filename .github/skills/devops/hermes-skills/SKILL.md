---
name: hermes-skills
title: Hermes Skills — Discovery, Creation, Hub Installation & Management
description: "Use when discovering, creating, installing, or managing Hermes skills from official hub, skills.sh registry, or ClawHub."
version: 1.1.0
author: Hermes Agent
license: MIT
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
   version: 1.1.0
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
- **Category column source**: `hermes skills list --source local` populates the Category column from the frontmatter `category:` field under `metadata.hermes`, NOT from the directory structure. A skill in `skills/devops/` with no `category:` field shows empty category.
- **Count mismatch: `hermes skills list` vs `find`**: `hermes skills list --source local` shows ~196 entries (its own inventory). `find skills/ -name SKILL.md` shows ~348. The difference comes from category subdirectory copies — many skills exist in both a flat directory AND a category subdirectory (e.g., `accelerate/` and `mlops/huggingface-accelerate/`). Both are real SKILL.md files on disk. Always use `find` for path enumeration; `hermes skills list` for the CLI-managed inventory.
- **`hermes skills browse` truncates names/identifiers** → The table ellipsizes (`…`) long names and identifiers. Use `hermes skills inspect <identifier>` for full details, or parse the output with care (identifiers wrap across lines).
- **Audit marks installed official skills as BLOCKED** → `hermes skills audit` re-scans installed skills as "community" source. Skills reading env vars (API tokens), running shell commands, or installing packages get flagged DANGEROUS. This is expected — BLOCKED audit status is informational, NOT a functional disablement. Skills remain enabled and usable.
- **`--force` doesn't override DANGEROUS verdicts** → It only works for CAUTION. DANGEROUS verdicts on community skills are always blocked. For official skills already installed, this doesn't matter (they're already functional).
- **`skills-sh` and `browse-sh` sources show identical official skill lists** → Different source flags, same underlying registry. Prefer `--source official` for the curated Nous Research set.
- **Windows "not supported on this platform" after successful install** → Some official skills (e.g. `mpp-agent`, `stripe-projects`) install without error but `skill_view()` returns `"not supported on this platform"`. This is a platform-gate in the skill's metadata or code — the install succeeds but the skill is inert. Check with `skill_view()` immediately after install; if unsupported, `skill_manage(action='delete')` to remove the dead entry.
- **Skill registered in DB but missing from disk** → `hermes skills install <name>` may print `"already installed"` even when the skill directory has no `SKILL.md` (filesystem was cleaned or the install was interrupted). The skill is tracked in the Hermes internal registry but has no executable files. Fix with `--force`: `hermes skills install <name> --force -y` reinstalls the files. Verify on disk after.
- **`hermes skills search` ignores `|` as regex OR** → The pipe character `|` is treated as a literal string, not a Boolean OR. If `hermes skills search "foo\|bar"` returns "No skills found", the engine is searching for the literal string `foo|bar`. Run separate search calls per term instead of using regex alternation.
- **`hermes skills inspect --json` fails** → The `--json` flag is documented in the help text but `hermes skills inspect <id> --json` errors with `unrecognized arguments`. Use the default table output or pipe through `grep` for scripting.

## Skills.sh Hub Workflow (agentskills.io ecosystem)

The `skills.sh` source provides access to the agentskills.io registry with 1000+ community skills. Key differences from official hub:

| Aspect | Official Hub | skills.sh Hub |
|--------|--------------|---------------|
| Source flag | `--source official` (default) | `--source skills.sh` |
| Trust level | official/builtin | community |
| Security scan | auto-allowed | SAFE/CAUTION/DANGEROUS verdict |
| Identifier format | `official/category/skill` | `skills-sh/org/repo/skill` |
| Examples | `official/github/github-auth` | `skills-sh/agents365-ai/365-skills/drawio-skill` |

**Search & Install Pattern:**
```bash
# Search (fuzzy match across skills.sh registry)
hermes skills search "drawio"
hermes skills search "youtube-skills"
hermes skills search "black-forest-labs"
hermes skills search "pydantic-ai"
hermes skills search "mindstudio"

# Inspect (shows security verdict, file list, upstream repo)
hermes skills inspect skills-sh/agents365-ai/365-skills/drawio-skill
hermes skills inspect skills-sh/zeropointrepo/youtube-skills/youtube-full

# Install (quarantine → scan → install)
hermes skills install skills-sh/agents365-ai/365-skills/drawio-skill -y
hermes skills install skills-sh/zeropointrepo/youtube-skills/youtube-full -y

# The -y flag skips confirmation; without it, you get:
#   "Install 'drawio-skill'? Confirm [y/N]: "
```

**Security Scan Results Observed (2026-06-13):**
```
drawio-skill:    Verdict: SAFE → Decision: ALLOWED (community source, safe verdict)
youtube-full:    Verdict: SAFE → Decision: ALLOWED (community source, safe verdict)
```

**Installed Skill Structures:**
```
drawio-skill/
  agents/openai.yaml       # Agent definitions for OpenAI
  README.md                # Usage documentation
  SKILL.md                 # Skill definition (triggers: draw.io, diagrams.net, flowcharts, architecture, ML diagrams)
  skill-card.md            # Summary card
  _meta.json               # Hub metadata

youtube-full/
  references/auth-setup.md # Auth setup guide
  skill-card.md            # Summary card
  SKILL.md                 # Skill definition (triggers: YouTube search, transcripts, channels, playlists)
  _meta.json               # Hub metadata
```

**Reference: Awesome-Hermes-Agent as Discovery Layer**

The `awesome-hermes-agent` plugin (https://github.com/0xNyk/awesome-hermes-agent) is a curated list that references many skills.sh skills. Workflow:

1. Browse the awesome list README for category-organized recommendations with maturity tags (production/beta/experimental)
2. Use `hermes skills search <keyword>` to find the skills.sh identifier
3. `hermes skills inspect <identifier>` to verify
4. `hermes skills install <identifier> -y` to install

This session discovered and installed:
- `drawio-skill` (from `skills-sh/agents365-ai/365-skills/drawio-skill`) — referenced in awesome list under "production" drawio-skill
- `youtube-full` (from `skills-sh/zeropointrepo/youtube-skills/youtube-full`) — referenced in awesome list under "production" youtube-skills (fixes VPS YouTube blocking via TranscriptAPI)

## ClawHub Registry

ClawHub is a separate skill registry (mindstudio-ai specific). Search pattern:
```bash
hermes skills search "mindstudio"  # Returns mindstudio-http-request-block-skill, mindstudio-interface-designer-skill, mindstudio-to-api-custom-function-builder, mindstudio-generate-text-block-prompting-skill
hermes skills inspect clawhub/mindstudio-http-request-block-skill
hermes skills install clawhub/mindstudio-http-request-block-skill -y
```

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
- `references/audit-findings-2026-06-11.md` — Session-specific audit findings and immediate remediation checklist (created during 2026-06-11 audit run)
- `references/skills_install_templates.md` — Templates for verification scripts and batch install wrappers (added 2026-06-11)
- `references/audit-results.md` — Understanding audit BLOCKED vs ALLOWED verdicts

---

## Skills Required

| Skill | Purpose | When Needed |
|-------|---------|-------------|
| `terminal` | CLI commands execution | All `hermes skills` commands |
| `file` | Read/write skill files | Creating custom skills, editing SKILL.md |
| `skills` | Skill discovery & loading | `/skills`, `hermes skills view`, `/skillname` |
