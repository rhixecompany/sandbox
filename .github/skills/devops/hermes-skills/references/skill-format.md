# SKILL.md Format Specification

## Frontmatter (Required)
```yaml
---
name: my-skill                    # lowercase, hyphens/underscores, max 64 chars
description: Brief description    # One sentence, shown in skills_list()
version: 1.0.0                    # Semver
platforms: [macos, linux, windows] # Optional: restrict OS platforms
metadata:
  hermes:
    tags: [python, automation]    # Optional: for grouping
    category: devops              # Optional: category
    fallback_for_toolsets: [web]  # Optional: conditional activation
    requires_toolsets: [terminal] # Optional: conditional activation
    config:                       # Optional: config.yaml settings
      - key: my.setting
        description: "What this controls"
        default: "value"
        prompt: "Prompt for setup"
---
```

## Platform Values
| Value | Matches |
|-------|---------|
| `macos` | macOS (Darwin) |
| `linux` | Linux |
| `windows` | Windows |

When set, skill is **automatically hidden** from system prompt, `skills_list()`, and slash commands on incompatible platforms.

## Body Sections (Required)
```markdown
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

## Media Delivery
- Bare absolute paths auto-detected and delivered natively (Telegram photo, Discord attachment)
- `[[audio_as_voice]]` promotes audio to voice-message bubbles
- `[[as_document]]` forces document-style delivery (no recompression)

## Best Practices
1. Single responsibility — one skill = one workflow/task type
2. Actionable steps — numbered procedures, not conceptual overviews
3. Pitfalls section — document known failures and fixes
4. Verification steps — how to confirm success
5. Token efficiency — keep SKILL.md under ~500 lines; large refs go to `references/`