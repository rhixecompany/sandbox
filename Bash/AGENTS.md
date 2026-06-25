# Bash — Automation Toolkit

## Architecture
- **Type:** Multi-phase automation toolkit (Bun/TypeScript + PowerShell + Bash)
- **Pattern:** Phase-Based Orchestration — 6-phase pipeline: Discovery → Clone → Triage → Debug → Remediation → Cross-Reference
- **Entry Points:** TypeScript scripts (`src/`), PowerShell orchestrator (`scripts/`), multi-wrapper (`.ps1`, `.sh`, `.bat`)
- **Reference:** [Workflow Analysis](docs/Project_Architecture/Workflow_Analysis.md), [Exemplars](docs/Project_Architecture/exemplars.md)

Bun 1.3.14+ + TypeScript strict + multi-platform shell wrappers (`.ps1`, `.sh`, `.bat`). Primary tooling root for the SandBox workspace; shares `.github/` CI workflows.

## Stack
- **Runtime:** Bun 1.3.14+
- **Language:** TypeScript (strict), PowerShell 5.1+, Bash
- **Linting:** ESLint flat config (`eslint.config.mts`)
- **Testing:** Vitest (TypeScript), `test-all.sh`, `tests/verify-dryrun.sh`
- **CI:** `.github/workflows/bash-scripts-ci.yml`

## Commands
```bash
bun install --frozen-lockfile || bun install
bun run format && bun run typecheck && bun run lint:strict
bash tests/verify-dryrun.sh && bash test-all.sh
powershell -File orchestrator-unified.ps1 -Mode discover
```

## Conventions
- All destructive ops support `--help` and `--dry-run` for safe preview
- Multi-wrapper parity: `.sh`, `.ps1`, `.bat` for every script
- Logs to `logs/` with timestamps; no `.bak`/`.backup` copies
- TypeScript strict mode; no `any` without explicit justification
- Vitest for unit tests; shell tests via `test-all.sh`

## Notes
- Orchestrator supports modes: `discover`, `clone`, `triage`, `debug`, `remediation`, `cross-ref`
- `.github/` CI workflows shared across workspace
- Cache cleaning via `bun run cache-clean` (dry-run supported)
