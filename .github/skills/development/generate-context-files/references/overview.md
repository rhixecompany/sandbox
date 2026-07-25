# generate_context_files.py — Overview

## Purpose
Generates context files for Hermes agent sessions. This script produces structured context summaries — such as project structures, dependency trees, and configuration snapshots — that help the agent maintain awareness of the project environment across sessions.

## Usage

```bash
python generate_context_files.py [--dir PATH] [--type TYPE] [--output PATH] [--depth N] [--include PATTERN] [--exclude PATTERN] [--format FORMAT]
```

### Options

| Option         | Description                                                    |
|---------------|----------------------------------------------------------------|
| `--dir`       | Project directory to analyze                                   |
| `--type`      | Context type: `tree` (directory tree), `config` (config summary), `env` (environment), `deps` (dependencies), `all` |
| `--output`    | Output file path (default: context.md or similar)              |
| `--depth`     | Directory tree depth limit (default: 3)                        |
| `--include`   | Glob pattern to include in context (repeatable)              |
| `--exclude`   | Glob pattern to exclude (repeatable, e.g., `node_modules,venv,__pycache__`) |
| `--format`    | Output format: `markdown`, `json`, `yaml` (default: `markdown`) |

## Behavior

- Analyzes the project directory to build structured context representations.
- For type `tree`: generates an indented directory tree of relevant files/folders.
- For type `config`: extracts key settings from supported config files (package.json, pyproject.toml, config.yaml).
- For type `dependencies`: reads dependency manifests and summarizes the package stack.
- For type `env`: captures basic environment details.
- Respects `.gitignore` patterns by default unless overridden.
- Outputs a file that can be loaded into agent context for faster project onboarding.

## Example

**Generate a directory tree context:**
```bash
python generate_context_files.py --dir ./myproject --type tree --depth 4 --output context_tree.md
```

**Generate full context with all types:**
```bash
python generate_context_files.py --dir ./myproject --type all --output project_context.md
```

**Generate JSON context for tooling:**
```bash
python generate_context_files.py --dir . --type all --format json --output context.json
```

## Dependencies

- Python 3.7+
- No external dependencies

## See Also

- Hermes context file loading mechanisms
- `hermes config` for context file settings