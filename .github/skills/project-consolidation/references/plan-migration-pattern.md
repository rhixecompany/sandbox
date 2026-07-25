# Plan Migration Pattern

Locate and centralize implementation plans into `.hermes/plans/`.

## Sources
- `docs/**/*plan*.md`
- `plan/**/*.md`
- `thoughts/**/*.md`
- `.hermes/plans/**/*.md` (already-centralized plans)
- `.hermes/archived-plan-templates/**` (preserve unless explicitly migrated)

## Classification
| Source type | Action |
|---|---|
| `prompts/*.prompt.md` | Do NOT migrate; these are loader artifacts, not task plans |
| `.github/agents/*.agent.md` | Only migrate if it is a concrete implementation plan, not a reusable scaffold |
| `projects/*/.cursor/plans/*.plan.md` | Preserve in place unless project is being consolidated |

## Naming
Use timestamped migration prefix to avoid collisions while preserving provenance:
```
YYYY-MM-DD_HHMMSS-slugified-basename.md
```

## Body
- Prepend provenance:
  ```markdown
  <!-- migrated from: <absolute-source-path> -->
  ```
- Do NOT rewrite the migrated plan body.

## Status rule
Every migrated plan gets `status: not_started`. If frontmatter already exists, add/update only the `status` field.

## Verification
- Source file still exists until user approves deletion.
- Destination file exists under `.hermes/plans/`.
- Frontmatter parses as valid YAML after migration.
- `grep -c 'status: not_started' .hermes/plans/*.md` matches new plan count added in the run.
