# Skill Audit: `1password`

**Category:** (root)  
**Path:** `C:\Users\Alexa\AppData\Local\hermes\profiles\adminbot\skills\1password\SKILL.md`  
**Audited:** 2026-06-04  
**Grade:** A  
**Issues:** 0 critical / 0 major / 0 minor  

---

## Frontmatter Check

```yaml
name: 1password
description: Set up and use 1Password CLI (op). Use when installing the CLI, enabling desktop app integration, signing in, and reading/injecting secrets for commands.
version: 1.0.0
author: arceus77-7, enhanced by Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [security, secrets, 1password, op, cli]
    category: security
setup:
  help: "Create a service account at https://my.1password.com → Settings → Service Accounts"
  collect_secrets:
    - env_var: OP_SERVICE_ACCOUNT_TOKEN
      prompt: "1Password Service Account Token"
      provider_url: "https://developer.1password.com/docs/service-accounts/"
      secret: true
```

## Issues Found

_No issues — skill passes all checks._

## Sections Present

- • `## Requirements`
- ✅ `## When to Use`
- • `## Authentication Methods`
- • `## Setup`
- • `## Hermes Execution Pattern (desktop app flow)`
- • `## Common Operations`
- • `## Guardrails`
- • `## CI / Headless note`
- • `## References`

## Recommendations

- None. Skill is well-formed.
