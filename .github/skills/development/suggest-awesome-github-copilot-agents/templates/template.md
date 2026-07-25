# Agent Coverage Scan Template

## Repository Info

- **Repo**: {{ repo_name }}
- **Scan Date**: {{ date }}

## Local Custom Agents Found

| File | Description | Status vs Remote |
|-----|-------------|------------------|
| {{ file }} | {{ desc }} | {{ up-to-date / outdated / new }} |

## Suggested Agents

| Awesome-Copilot Agent | Description | Rationale |
|------------------------|-------------|-----------|
| {{ name }} | {{ }} | {{ why this is relevant }} |

## Recommended Actions

- [ ] Install {{ count }} new custom agent(s):
  - {{ list of files }}
- [ ] Update {{ count }} outdated agent(s):
  - {{ list of files with noted differences }}
- [ ] No changes needed (all agents up-to-date)

## Notes

{{ additional context or caveats }}