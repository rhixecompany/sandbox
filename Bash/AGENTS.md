# Bash Automation Toolkit Context

This is the primary automation toolkit for the SandBox workspace.

## Architecture
- **Language**: TypeScript (strict mode) + shell scripts
- **Runtime**: Bun 1.3.14+
- **Package Manager**: Bun (not npm)
- **Testing**: Custom test runner (`bash tests/verify-dryrun.sh`, `bash test-all.sh`)

## Conventions
- Use `bun run` for TypeScript execution
- Support `--help` and `--dry-run` for operational scripts
- Preserve wrapper behavior across `.sh`, `.ps1`, and `.bat`
- Write logs to `logs/` with timestamped filenames
- Prefer Bun over npm for TypeScript execution

## Commands
```bash
# Install dependencies
bun install --frozen-lockfile || bun install

# Format & Lint
bun run format
bun run typecheck
bun run lint:strict

# Test
bash tests/verify-dryrun.sh
bash test-all.sh

# Orchestration
powershell -File orchestrator-unified.ps1 -Mode discover
powershell -File orchestrator-unified.ps1 -DryRun
```

## Important Notes
- Primary script/tooling root for the workspace
- Shared configuration under `.github/`
- CI workflows: `.github/workflows/bash-scripts-ci.yml`, `.github/workflows/copilot-setup-steps.yml`