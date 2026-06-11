# Dev Init Conversion Pass Report

Date: 2026-05-27
Source Prompt: [Prompts/dev-init.prompts.md](../Prompts/dev-init.prompts.md)

## Summary

First conversion pass coverage is complete for the initial plaintext batch discovered in Prompts.

- Plaintext files found: 7
- Matching markdown targets found: 7
- Missing markdown targets: 0

## Source to Target Matrix

| Source file | Markdown target | Target exists | Source lines | Target lines | Initial assessment |
|---|---|---:|---:|---:|---|
| [Prompts/agents-fix.prompts.txt](../Prompts/agents-fix.prompts.txt) | [Prompts/agents-fix.prompts.md](../Prompts/agents-fix.prompts.md) | Yes | 7 | 84 | Converted and expanded |
| [Prompts/bash-scripts-fix.prompts.txt](../Prompts/bash-scripts-fix.prompts.txt) | [Prompts/bash-scripts-fix.prompts.md](../Prompts/bash-scripts-fix.prompts.md) | Yes | 155 | 155 | Converted and aligned |
| [Prompts/commands-fix.prompts.txt](../Prompts/commands-fix.prompts.txt) | [Prompts/commands-fix.prompts.md](../Prompts/commands-fix.prompts.md) | Yes | 7 | 86 | Converted and expanded |
| [Prompts/dev-init.prompts.txt](../Prompts/dev-init.prompts.txt) | [Prompts/dev-init.prompts.md](../Prompts/dev-init.prompts.md) | Yes | 1 | 96 | Converted and expanded |
| [Prompts/general.prompts.txt](../Prompts/general.prompts.txt) | [Prompts/general.prompts.md](../Prompts/general.prompts.md) | Yes | 4 | 85 | Converted and expanded |
| [Prompts/repo.prompts.txt](../Prompts/repo.prompts.txt) | [Prompts/repo.prompts.md](../Prompts/repo.prompts.md) | Yes | 11 | 151 | Converted and expanded |
| [Prompts/skills-fix.prompts.txt](../Prompts/skills-fix.prompts.txt) | [Prompts/skills-fix.prompts.md](../Prompts/skills-fix.prompts.md) | Yes | 8 | 92 | Converted and expanded |

## Quality Gate Snapshot

- Frontmatter presence: Pass for pilot files and existing markdown set shape.
- Required template dependency check: Pass (all referenced templates exist under .github/prompts).
- Immediate blocker status: None for phase start.

## Notes

- Line-count differences are expected where plaintext shorthand was expanded into structured markdown prompts.
- Full semantic equivalence review is tracked in the constraint checklist and pilot verification artifacts.

## Related Artifacts

- [docs/dev-init-implementation-plan.md](dev-init-implementation-plan.md)
- [docs/dev-init-conversion-inventory.md](dev-init-conversion-inventory.md)
