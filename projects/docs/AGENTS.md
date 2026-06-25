# docs — Documentation Reference

## Architecture
- **Type:** Documentation-only repository
- **Pattern:** Static Markdown documentation
- **Entry Point:** N/A (read-only reference)
- **Reference:** [Workflow Analysis](docs/Project_Architecture/Workflow_Analysis.md), [Exemplars](docs/Project_Architecture/exemplars.md)

Contains no executable code. Serves as a centralized reference for dependency audit findings, research appendices, shared VS Code configuration, and architecture blueprints.

## Contents
- `README.md` — project overview and navigation
- `DEPENDENCY_AUDIT.md` — dependency audit findings across the workspace
- `RESEARCH_APPENDIX.md` — supplementary research documentation
- `docs/Project_Architecture/` — architecture workflow analysis and exemplars
- `.vscode/` — shared VS Code workspace settings, launch configs, extensions, tasks

## Commands
```bash
# No build/run commands — static documentation only
# Markdown linting (inherited from root workspace):
cd ../.. && npx markdownlint-cli2 "projects/docs/**/*.md"
```

## Conventions
- GitHub-Flavored Markdown (GFM)
- Keep docs DRY — reference rather than duplicate
- Update `DEPENDENCY_AUDIT.md` when dependencies change
- VS Code settings in `.vscode/` are shared across workspace

## Notes
- Pure documentation; no CI/CD pipeline needed
- Cross-reference with root `AGENTS.md` and individual project AGENTS.md files
