# SandBox

> A Hermes agent development workspace and Copilot configuration library that also hosts a multi-language project portfolio (Python, TypeScript, Go, Rust, Java, and more). It contains agent prompts, skill-generation tooling, documentation, and 16+ subprojects under `projects/`.

This workspace is not a single compiled application. Four concerns live side by side: a Copilot asset library (`.github/`), an agent prompt library (`prompts/`, 215 files), Hermes documentation (`docs/`, 249 files), and a portfolio of independent subprojects (`projects/`). Use this file as the entry point for understanding repository layout and locating essential documentation.

## Agent Configuration

- [AGENTS.md](AGENTS.md): Root guidance for AI coding agents (Copilot, Codex, Hermes). Read FIRST in this workspace.
- [.hermes.md](.hermes.md): Hermes Agent project overrides — profiles, MCP servers, hooks, plugins, provider chain, toolsets.
- [README.md](README.md): Workspace overview and subproject index.
- [SESSION_REPORT.md](SESSION_REPORT.md): Session history and handoff notes.

## Documentation

- [docs/ getting-started](docs/getting-started): Onboarding and setup guides for the workspace.
- [docs/guides](docs/guides): Operational guides for agents and tooling.
- [docs/user-guide](docs/user-guide): End-user documentation.
- [docs/specs](docs/specs): Technical specifications and interface contracts.
- [docs/catalogs](docs/catalogs): Model, skill, and server catalogs (e.g. `nvidia_nim_models.json`, `openrouter_models.json`).
- [docs/Project_Architecture](docs/Project_Architecture): System architecture documentation.
- [docs/skills-audit](docs/skills-audit): Skill audit reports and remediation records.
- [docs/awesome-hermes-agent](docs/awesome-hermes-agent): Curated Hermes reference materials.

## Prompts (Agent Library)

- [prompts/](prompts/): 215 reusable prompt files (`.prompt.md`) covering generation, review, debugging, cloud, and more.
- [prompts/templates/_index.md](prompts/templates/_index.md): Index of shared prompt templates.
- [prompts/templates/_shared](prompts/templates/_shared): Shared template fragments (e.g. `rules-core.md`).
- [prompts/templates/create-llms](prompts/templates/create-llms): Templates for the create-llms prompt.
- [create-llms.prompt.md](prompts/create-llms.prompt.md): Prompt that produced this `llms.txt`.

## Tooling & Scripts

- [generate_skills.py](generate_skills.py): Generates agent skills from prompt/template definitions.
- [_agents_fix_discover.py](_agents_fix_discover.py): Discovers agent files needing fixes.
- [_agents_fix_report.py](_agents_fix_report.py): Reports results of agent-fix runs.
- [lcs.py](lcs.py): Longest-common-subsequence utility.
- [greeting.py](greeting.py): Minimal example script.
- [requirements.txt](requirements.txt): Python dependency manifest.
- [package.json](package.json): Node/TypeScript package manifest for the workspace.

## Subprojects

- [projects/](projects/): 16+ independent subprojects across Python, TypeScript, Go, Rust, Java, etc.
- [projects/Bash/](projects/Bash/): TypeScript/Bun automation toolkit.
- [projects/Resume_maker/](projects/Resume_maker/): TypeScript/Bun resume PDF generator.
- [projects/mcp-servers/](projects/mcp-servers/): MCP server implementations.
- [projects/docs](projects/docs): Subproject-local documentation.

## Reference Data

- [skill_inventory.json](skill_inventory.json): Inventory of all skills in the workspace.
- [skill_name_to_path.json](skill_name_to_path.json): Skill name → file path mapping.
- [nvidia_nim_models.json](nvidia_nim_models.json): NVIDIA NIM model catalog.
- [openrouter_models.json](openrouter_models.json): OpenRouter model catalog.
- [opencode_zen_models.json](opencode_zen_models.json): opencode-zen model catalog.

## Optional

- [.github/](.github/): Copilot agents (174), instructions (186), plugins, workflows, and scripts.
- [docs/agents-context](docs/agents-context): Context material for agent definitions.
- [research/](research/): Research notes and API tutorials.
- [reports/](reports/): Inventory and migration reports.
- [benchmark_results/](benchmark_results/): Benchmark outputs and evaluations.
- [templates/](templates/): Misc workspace templates.
- [plan/](plan/): Planning artifacts.
- [MEMORY_DUMP.md](MEMORY_DUMP.md): Working memory snapshot.
- [SESSION_AUDIT_227.md](SESSION_AUDIT_227.md): Detailed session audit record.
