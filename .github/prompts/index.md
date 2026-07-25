# .github/prompts

Canonical prompt library for this repository.

## Structure

| Path | Contents |
| ------ | ---------- |
| `.github/prompts/agents/` | Copilot custom agent definitions |
| `.github/prompts/instructions/` | Copilot instruction files |
| `.github/prompts/skills/` | Repository-local skills |
| `.github/prompts/archived/` | Archived prompt and plan templates |

## Usage Rules

- Treat `.github/prompts/` as the single source of truth for prompt-family content.
- New prompt assets belong under `.github/prompts/`, not under legacy `.github/agents/`, `.github/instructions/`, `.github/skills/`, or root `prompts/`.
- When updating a prompt, also update its cross-references.
- Dedupe exact duplicate prompt/instruction bodies; keep one canonical copy and cross-link instead of duplicating content.
- Use `projects/Bash/` for automation validation commands.
