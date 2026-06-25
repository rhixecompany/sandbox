# Project Folder Structure Blueprint

## Project: SandBox Root (Monorepo Workspace Root)

**Generated:** 2026-06-25  
**Project Type:** Multi-project Monorepo / Workspace Root  
**Auto-detected:** Yes (Root level — contains multiple project directories, prompts, docs, tools, and reports)

---

## Directory Tree

```
SandBox/
├── .editorconfig
├── .git/
├── .github/
│   ├── agents/          # 170+ GitHub Copilot agent definitions (.agent.md)
│   ├── hooks/           # Governance-audit, session-auto-commit, session-logger hooks
│   └── instructions/    # 200+ instruction files for various tech stacks
├── .gitignore
├── .gitmodules
├── .hermes/
├── .hermes.md
├── .markdownlintrc.json
├── .playwright-mcp/
├── .ruff_cache/
├── .tmp/
├── .vscode/
├── AGENTS.md            # Primary agent orchestration manifest
├── Bash/                # Bun/TypeScript automation toolkit (Target 2)
├── HERMES_PROFILE_REPORT.md
├── PROJECT_RULES.md
├── Resume_maker/        # Bun/TypeScript job docs generator (Target 3)
├── SESSION_REPORT.md
├── benchmark_output/
├── cli-tools.md
├── docs/
│   └── Project_Architecture/   # Architecture docs for workspace & projects
├── judge_results/
├── nvidia_nim_models.json
├── opencode_zen_models.json
├── openrouter_models.json
├── projects/            # 15 sub-projects (Banking, comicwise, Django, etc.)
├── prompts/             # 200+ prompt templates organized by function
├── reports/
├── research/
├── thoughts/
└── tool/
```

---

## Naming Conventions

| Convention | Pattern | Examples |
|---|---|---|
| **Directories** | kebab-case | `projects/`, `benchmark_output/`, `judge_results/` |
| **Config files** | dotted-prefix | `.editorconfig`, `.gitignore`, `.markdownlintrc.json` |
| **Documentation** | UPPER_SNAKE_CASE.md | `AGENTS.md`, `PROJECT_RULES.md`, `HERMES_PROFILE_REPORT.md` |
| **Agents** | descriptive-kebab.agent.md | `architect.agent.md`, `debug.agent.md` |
| **Instructions** | tech-stack.instructions.md | `angular.instructions.md`, `csharp.instructions.md` |

---

## File Placement Patterns

- **Root config**: Editor, linter, git configuration files at workspace root
- **Agent definitions**: `.github/agents/*.agent.md`
- **Instruction sets**: `.github/instructions/*.instructions.md`
- **Hook scripts**: `.github/hooks/<hook-name>/`
- **Project source**: `projects/<project-name>/`
- **Prompts & templates**: `prompts/` and `prompts/templates/`
- **Architecture docs**: `docs/Project_Architecture/`
- **Research**: `research/<topic>/`
- **Reports**: `reports/`

---

## Project Type Indicators

| Indicator | Value |
|---|---|
| Has `.gitmodules` | ✅ Monorepo with submodules |
| Has `AGENTS.md` | ✅ AI-agent-orchestrated workspace |
| Has `.github/agents/` | ✅ Extensive Copilot agent ecosystem |
| Has `.github/instructions/` | ✅ Language/framework instruction sets |
| Has `prompts/` dir | ✅ Extensive prompt template library |
| Multiple project dirs | ✅ Monorepo (projects/, Bash/, Resume_maker/) |

---

## Recommendations

1. ✅ **Structure is well-organized** for a multi-project monorepo.
2. ✅ **Separation of concerns** is clear: agents, instructions, prompts, projects are in distinct top-level directories.
3. ⚠️ Consider moving `Bash/` and `Resume_maker/` under `projects/` for consistency.
4. ✅ `.github/` layout follows GitHub best practices.
5. ⚠️ Large number of top-level config files — consider grouping into a `config/` directory.
