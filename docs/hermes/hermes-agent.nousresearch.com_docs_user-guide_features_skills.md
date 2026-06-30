# Source: <https://hermes-agent.nousresearch.com/docs/user-guide/features/skills>

# Skills System — Hermes Agent (summary)

Key purpose: Skills are on-demand knowledge documents the agent loads progressively to minimize tokens. They live primarily under `~/AppData/Local/hermes/skills/`, support external directories, bundles, hub installs, agent-managed creation, and security scanning.

---

## Key excerpts (original format)

SKILL.md frontmatter example:

```
---
name: my-skill
description: Brief description of what this skill does
version: 1.0.0
platforms: [macos, linux] # Optional — restrict to specific OS platforms
metadata:
 hermes:
 tags: [python, automation]
 category: devops
 fallback_for_toolsets: [web] # Optional — conditional activation (see below)
 requires_toolsets: [terminal] # Optional — conditional activation (see below)
 config: # Optional — config.yaml settings
 - key: my.setting
 description: "What this controls"
 default: "value"
 prompt: "Prompt for setup"
---

# Skill Title

## When to Use
Trigger conditions for this skill.

## Procedure
1. Step one
2. Step two

## Pitfalls
- Known failure modes and fixes

## Verification
How to confirm it worked.
```

Progressive disclosure (token-efficient loading):

```
Level 0: skills_list() → [{name, description, category}, ...] (~3k tokens)
Level 1: skill_view(name) → Full content + metadata (varies)
Level 2: skill_view(name, path) → Specific reference file (varies)
```

Media delivery directives and examples:

```
[[audio_as_voice]]
[[as_document]]
/home/user/.hermes/cache/chart-q4-2025.png
Here is your rendered chart:

/home/user/.hermes/cache/chart-q4-2025.png

[[as_document]]
```

Bundle YAML schema example:

```
~/AppData/Local/hermes/skill-bundles/<slug>.yaml
name: backend-dev
description: Backend feature work — review, test, PR workflow.
skills:
 - github-code-review
 - test-driven-development
 - github-pr-workflow
instruction: |
 Always start by writing failing tests, then implement.
 Open the PR through the standard workflow with co-author tags.
```

skill_manage actions (original keywords):

```
create, patch, edit, delete, write_file, remove_file
```

Common hub commands (excerpt):

```
hermes skills browse
hermes skills search kubernetes
hermes skills inspect openai/skills/k8s
hermes skills install openai/skills/k8s
hermes skills update
hermes skills audit
hermes skills uninstall k8s
hermes skills publish skills/my-skill --to github --repo owner/repo
```

Bundled-skill reset examples:

```
hermes skills reset google-workspace
hermes skills reset google-workspace --restore
hermes skills reset google-workspace --restore --yes
```

Blank-slate install snippet:

```
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash -s -- --no-skills
```

---

## Comprehensive summary (scannable, actionable)

### Where skills live

- Primary source: `~/AppData/Local/hermes/skills/` (read-write). Bundled skills copied on install. Agent/hub-installed/created skills go here.
- External directories supported: configure `skills.external_dirs` in `~/AppData/Local/hermes/config.yaml`:

  ```
  skills:
    external_dirs:
    - ~/.agents/skills
    - /home/shared/team-skills
    - ${SKILLS_REPO}/skills
  ```

  - External skills are indexed alongside local ones; a local skill shadows an external one of the same name.

### Starting with a blank slate (prevent bundled seeding)

- Install-time:

  ```
  curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash -s -- --no-skills
  ```

- Profile creation:

  ```
  hermes profile create research --no-skills
  ```

- On an existing profile:

  ```
  hermes skills opt-out            # stop future seeding (no deletion)
  hermes skills opt-out --remove   # also delete UNMODIFIED bundled skills
  hermes skills opt-in --sync      # undo and re-seed now
  ```

- These write `.no-bundled-skills` marker in profile directory; while present, bundled seeding is skipped.

### Using skills

- Every installed skill is a slash command in CLI or messaging:

  ```
  /gif-search funny cats
  /axolotl help me fine-tune Llama 3 on my dataset
  /github-pr-workflow create a PR for the auth refactor
  /plan design a rollout for migrating our auth provider
  /excalidraw
  ```

- Natural conversation access:

  ```
  hermes chat --toolsets skills -q "What skills do you have?"
  hermes chat --toolsets skills -q "Show me the axolotl skill"
  ```

- Example: `/plan [request]` loads instructions and saves output under `.hermes/plans/` relative to active workspace.

### Token-efficient loading (Progressive Disclosure)

- Level 0: index (names, descriptions, categories).
- Level 1: full skill content when needed.
- Level 2: specific reference files.

### SKILL.md & directory layout

```
/gif-search funny cats
/axolotl help me fine-tune Llama 3 on my dataset
/github-pr-workflow create a PR for the auth refactor
/plan design a rollout for migrating our auth provider
/excalidraw
```

- Natural conversation access:

  ```
  hermes chat --toolsets skills -q "What skills do you have?"
  hermes chat --toolsets skills -q "Show me the axolotl skill"
  ```

- Example: `/plan [request]` loads instructions and saves output under `.hermes/plans/` relative to active workspace.

### Token-efficient loading (Progressive Disclosure)

- Level 0: index (names, descriptions, categories).
- Level 1: full skill content when needed.
- Level 2: specific reference files.

### SKILL.md & directory layout

- Each skill must include a `SKILL.md` (frontmatter YAML controls metadata, platforms, hermes-specific metadata).
- Directory recommended structure:

  ```
  ~/AppData/Local/hermes/skills/
  ├── category/
  │   ├── skill-name/
  │   │   ├── SKILL.md
  │   │   ├── references/
  │   │   ├── templates/
  │   │   ├── scripts/
  │   │   └── assets/
  └── .hub/ (.hub state)
  ```

- `metadata.hermes` supports tags, categ

[... summary truncated for context management ...]
