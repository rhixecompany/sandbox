# Bash — Automation Toolkit
## Architecture

- **Blueprint**: [Bash Architecture](../docs/Project_Architecture/Bash_architecture.md)
- **Folders**: [Bash Folder Structure](../docs/Project_Architecture/Bash_folders.md)
- **Tech Stack**: [Bash Technology Stack](../docs/Project_Architecture/Bash_techstack.md)
- **Stack Type**: Bun/TypeScript


Bun 1.3.14+ + TypeScript strict + shell scripts.

## Conventions
- Use `bun run`, `bun install`
- Support `--help`, `--dry-run`
- Maintain wrapper parity for `.sh`, `.ps1`, `.bat`
- Logs to `logs/` with timestamps

## Commands
```bash
bun install --frozen-lockfile || bun install
bun run format && bun run typecheck && bun run lint:strict
bash tests/verify-dryrun.sh && bash test-all.sh
powershell -File orchestrator-unified.ps1 -Mode discover
```

## Notes
- Primary tooling root; `.github/` shared
- CI: `.github/workflows/bash-scripts-ci.yml`, `.github/workflows/copilot-setup-steps.yml`
