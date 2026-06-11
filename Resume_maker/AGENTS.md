# AGENTS.md

## Project Overview

Resume Maker generates job-hunting documents (resume, cover letter, LinkedIn guide, and interview prep) from structured JSON data to Markdown and PDF outputs.

The project is Bun-first and centered around a single TypeScript entry file:

- index.ts

## Hermes and Copilot

- Use the nearest `AGENTS.md` for files in `Resume_maker/`; this file is the
  local fallback.
- `Resume_maker/.github/copilot-instructions.md` is the primary Copilot
  guidance file for this project.
- Root Hermes orchestration assets live in `../.github/agents/hermes.agent.md`
  and `../.github/prompts/`.
- Keep this file, the local Copilot instructions, and `package.json` aligned
  whenever the CLI behavior changes.

## Setup Commands

Run all commands from the Resume_maker directory.

```bash
cd Resume_maker
bun install
```

## Development Workflow

Primary entrypoint:

```bash
bun index.ts
```

Useful script aliases from package.json:

```bash
bun run start
bun run build
bun run help
```

Common CLI usage:

```bash
bun index.ts --input sample-input.json
bun index.ts -i alexander-input.json -o resume -f both
bun index.ts -p ../projects --skipProjects
bun index.ts --verbose
```

## Testing Instructions

There is no dedicated unit test suite in this subproject today. Verify behavior through:

- Type-checking
- Linting
- CLI smoke runs with sample input files

Recommended verification sequence:

```bash
cd Resume_maker
bun run typecheck
bun run lint
bun index.ts --help
bun index.ts -i sample-input.json -o verify-output -f markdown
```

## Code Style Guidelines

Use project-configured tools and keep edits minimal.

- TypeScript + JSON + Markdown formatting/linting are enforced through eslint + prettier.
- Prefer Bun commands over npm/pnpm/yarn for this project.
- Keep CLI option names and defaults synchronized between index.ts, README.md, and this file.

Lint and fix commands:

```bash
bun run lint
bun run lint:fix
bun run lint:md
bun run lint:spell
```

## Build and Output

This project is CLI-oriented and does not produce a separate compiled artifact by default.

Generated files are written under output/.

For PDF generation, use:

```bash
bun index.ts -i sample-input.json -o resume -f pdf
```

## Security Considerations

- Do not commit secrets or private personal data in input JSON files.
- Treat generated output as potentially sensitive personal information.
- Validate external JSON input through existing validation logic before extending generators.

## Pull Request Guidelines

- Keep changes scoped and avoid unrelated refactors.
- If CLI options, defaults, or output behavior changes, update README.md in the same PR.
- Include command output summary for typecheck/lint/smoke-run validation.

## Monorepo Notes

This AGENTS.md applies to Resume_maker/.

If editing files outside Resume_maker/, use the nearest AGENTS.md in that target directory.

## Troubleshooting

If a command fails:

- Re-run bun install.
- Confirm you are in Resume_maker/.
- Run bun run help to confirm current CLI flags.

If linting fails on generated or external files:

- Limit lint checks to project-tracked source and documentation files for the change scope.
