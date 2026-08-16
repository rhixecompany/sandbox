# Community Skill Installation Patterns

## Multi-Source Search

Search all sources simultaneously with `--source all`:

```bash
hermes skills search "prompt" --source all
```

Returns results from all registered sources in one table.

## Source Trust Levels

| Source       | Trust Level | Auto-Allowed | Notes |
|-------------|-------------|:-----------:|-------|
| `official`  | official    | Yes | Nous Research curated |
| `openai`    | trusted     | Yes | OpenAI's skill registry |
| `skills-sh` | community   | SAFE only | agentskills.io registry |
| `clawhub`   | community   | SAFE only | mindstudio-ai registry |
| `lobehub`   | community   | SAFE only | lobehub registry |

**Identifier format per source:**

| Source | Format | Example |
|--------|--------|---------|
| `official` | `official/category/skill` | `official/mlops/instructor` |
| `skills-sh` | `skills-sh/org/repo/skill` | `skills-sh/wshobson/agents/skill-name` |
| `clawhub` | `clawhub/skill-name` | `clawhub/implementation-plan` |
| `openai` | `openai/path/.../skill` | `openai/skills/.../skill-name` |

## Community Scan Blocking Pattern

Skills in certain categories (prompt engineering, prompt optimization) are
disproportionately blocked by the security scanner. Common triggers:

- **References to agent config files** — how-to docs inevitably mention them.
  The scanner reads any mention as a modification attempt (false positive).
- **System prompt examples** — robustness test patterns in documentation trigger
  injection rules even though they are educational examples, not actual payloads.

**Workarounds when blocked:**
- `--force` cannot override DANGEROUS verdicts for community sources.
- Search for the same topic under `official` or `openai` sources instead.
- Create a local skill via `skill_manage(action='create')`.
- Try the same skill from a different registry source.

**Skills that tend to pass (SAFE):**
- Pure technique docs with no agent-config references
- Domain-specific examples (crypto, trading, API-specific)
- Generic planning templates and workflows
- Skills from `openai` or `official` sources (trusted/auto-allowed)

## Quick Install Reference

```bash
# Search all sources
hermes skills search "<topic>" --source all

# Inspect before installing (shows security verdict, file list)
hermes skills inspect <identifier>

# Install from any source (auto-detects the registry)
hermes skills install <identifier> -y

# Batch install from a list
for id in \
  skills-sh/org/repo/skill-a \
  skills-sh/org/repo/skill-b \
  clawhub/skill-c; do
  hermes skills install "$id" -y
done
```
