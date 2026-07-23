# Rules

> Extracted from `update-implementation-plan.prompt.md`.

## Rules

1. Use only evidence from the current workspace and the user request
2. Change only the implementation plan sections directly affected by new requirements
3. If the target file does not exist, create it at `<workspace_root>/plan/<purpose>-<component>-<version>.md` using status `Planned`
4. Use these section names: `Introduction`, `Requirements & Constraints`, `Implementation Steps`, `Alternatives`, `Dependencies`, `Files`, `Testing`, `Risks & Assumptions`, `Related Specifications / Further Reading`
5. Use the status badge template: `https://img.shields.io/badge/status-<url_encoded_status>-<color>`

### Naming Constraints for Template Variables

When creating plan file names, follow these conventions:

- **`<purpose>`**: Use lowercase hyphen-separated slugs (e.g., `feature-auth-refactor`, `bugfix-memory-leak`). Max 30 characters.
- **`<component>`**: Use lowercase hyphen-separated module/component names (e.g., `database`, `ui-components`, `auth-service`). Max 20 characters.
- **`<version>`**: Use semantic version format (e.g., `v1`, `v2`, `v1-draft`). Max 10 characters.
- **Avoid:** Spaces, special characters (!@#$%), and uppercase letters in variable values.
- **Result:** Final file names will be filesystem-safe with only alphanumeric characters and hyphens.

### Status Mapping

|| Status | shields.io color |
|| --- | --- |
|| Completed | brightgreen |
|| In progress | yellow |
|| Planned | blue |
|| Deprecated | red |
|| On Hold | orange |

### Status Usage Guidance

- **Planned** (blue): Use for newly created plans before implementation begins. Initial status for all new implementation plans.
- **In progress** (yellow): Use when implementation has begun. Update status when first implementation step is started.
- **Completed** (brightgreen): Use when all implementation steps are finished and verified. Plan is ready for reference/archive.
- **On Hold** (orange): Use when implementation is temporarily paused due to blockers, resource constraints, or priority changes.
- **Deprecated** (red): Use when plan is no longer relevant due to scope change, cancellation, or superseding by newer plan.
