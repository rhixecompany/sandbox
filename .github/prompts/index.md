# .github/prompts

Canonical prompt library for this repository.

## Structure

| Path | Contents |
|| ------ | ---------- ||
| `.github/prompts/*.prompt.md` | Canonical prompts (220+) |
| `.github/prompts/templates/` | Extracted prompt bodies by trigger |
| `.github/prompts/.enhance/` | Enhancement and validation tooling |
| `.github/prompts/archived/` | Deprecated prompt and plan templates |

## Thin Shell Pattern

Each `.prompt.md` is a thin shell with preserved frontmatter. The full workflow body lives in `templates/{trigger}/README.md`.

```text
.github/prompts/
├── <trigger>.prompt.md
└── templates/
    └── <trigger>/
        └── README.md
```

Shared rules are referenced from `templates/_shared/rules-core.md`.

## Usage Rules

- Treat `.github/prompts/` as the single source of truth for prompt-family content.
- New prompt assets belong under `.github/prompts/`, not under legacy `.github/agents/`, `.github/instructions/`, `.github/skills/`, or root `prompts/`.
- When updating a prompt, also update its cross-references and corresponding template body.
- Dedupe exact duplicate prompt/instruction bodies; keep one canonical copy and cross-link instead of duplicating content.
- Use `projects/Bash/` for automation validation commands.
- All prompt markdown uses LF line endings.

## New Prompts

- `all-repo-docker-setup.prompt.md` — org-wide Docker setup, build, scan, cleanup
- `smithery-setup.prompt.md` — Smithery MCP connection and OAuth setup
- `hermes-comprehensive-setup.prompt.md` — end-to-end Hermes/OpenCode setup and validation
