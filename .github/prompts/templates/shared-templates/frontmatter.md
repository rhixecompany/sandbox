---
name: shared-frontmatter
title: Shared Frontmatter Template
description: Canonical YAML frontmatter schema for all .github/prompts/*.prompt.md files. Use this as the single source of truth — every prompt must match this schema.
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [shared, frontmatter, schema, prompts]
---
## Goal

<!-- Shared template — see file body for goal content -->

## Context

<!-- Shared template — see file body for context content -->

## Workflow

<!-- Shared template — see file body for workflow content -->

## Verification

<!-- Shared template — see file body for verification content -->


# Shared Frontmatter Template

## Schema (required keys)

```yaml
---
name: <kebab-case-prompt-name>      # e.g. "hermes-diagnostic"
title: "<Human-Readable Title>"      # e.g. "Hermes Diagnostic + Log Analysis"
description: "<1-2 sentence purpose statement, ≤200 chars>"
version: <semver>                    # e.g. "1.0.0"
author: "<author or org>"            # e.g. "Hermes Agent"
license: <MIT|Apache-2.0|...>        # default: MIT
tags: [<category>, <feature>, ...]   # 2-5 tags from controlled vocabulary
metadata:
  hermes:
    tags: [<hermes-internal-tags>]   # optional, for hermes routing
---
```

## Controlled tag vocabulary

| Category | Allowed values |
|---|---|
| Domain | `hermes`, `github`, `code`, `data`, `devops`, `docs`, `design`, `test`, `security` |
| Operation | `create`, `update`, `fix`, `verify`, `audit`, `triage`, `remediate` |
| Skill | `mcp`, `skill`, `hook`, `plugin`, `prompt` |
| Layer | `meta`, `system`, `user`, `agent` |

## Validation rules

- `name` MUST be kebab-case and match the filename stem (without `.prompt.md`)
- `title` MUST be ≤80 chars
- `description` MUST be ≤200 chars and end with a period
- `version` MUST be semver (X.Y.Z)
- `tags` MUST contain 2-5 items from the controlled vocabulary
- `metadata.hermes.tags` is optional; if present, all values must also appear in top-level `tags`

## Bad example

```yaml
---
name: My Prompt
title: This Is A Very Long Title That Exceeds Eighty Characters And Should Be Shortened
description: no period at end
Version: 1.0
tags: [stuff, things, foo, bar, baz, qux]
---
```

## Good example

```yaml
---
name: hermes-diagnostic
title: "Hermes Diagnostic + Log Analysis"
description: "Run the full Hermes platform diagnostic battery plus log analysis. Emits report.md, report.json, and triage recommendations."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [hermes, devops, diagnostic, repair]
metadata:
  hermes:
    tags: [hermes, devops]
---
```

## References

- `references/frontmatter-validation.md` — automated validator script (planned)
- `../_index.md` — templates index