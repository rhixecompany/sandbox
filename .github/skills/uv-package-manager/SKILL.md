---
name: uv-package-manager
title: "uv Python Package Manager"
description: "Guide for using uv — the fast Python package and project manager. Covers project init, dependency management, virtual envs, tool installation, and pip-compatible commands."
version: 1.0.0
author: "Hermes Assistant"
tags: [python, uv, package-manager, pip]
license: MIT
---
# uv — Python Package Manager (Fast)

## Overview

Automated reasoning and workflow tool for `uv-package-manager`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## When to Use
- Creating new Python projects (`uv init`)
- Adding/removing dependencies (`uv add`, `uv remove`)
- Running scripts in isolated envs (`uv run`)
- Installing CLI tools from PyPI (`uv tool install`)
- Managing Python versions (`uv python install`)
- pip-compatible operations (`uv pip install`)

## Key Commands

### Project Management
| Command | Purpose |
|---------|---------|
| `uv init <name>` | Create new Python project |
| `uv add <pkg>` | Add dependency |
| `uv remove <pkg>` | Remove dependency |
| `uv sync` | Sync env with lockfile |
| `uv lock` | Update lockfile |
| `uv run <script>` | Run script in project env |
| `uv build` | Build sdist + wheel |
| `uv publish` | Upload to index |

### Tool Management (CLI tools)
| Command | Purpose |
|---------|---------|
| `uv tool install <pkg>` | Install CLI tool |
| `uv tool run <pkg>` | Run tool once |
| `uv tool list` | List installed tools |
| `uv tool upgrade <pkg>` | Upgrade tool |
| `uv tool uninstall <pkg>` | Uninstall tool |

### Python Management
| Command | Purpose |
|---------|---------|
| `uv python list` | List managed Pythons |
| `uv python install <version>` | Install Python version |
| `uv python pin <version>` | Pin project Python |
| `uv venv` | Create virtual env |

### pip-Compatible
| Command | Purpose |
|---------|---------|
| `uv pip install <pkg>` | Install like pip |
| `uv pip freeze` | List installed |
| `uv pip compile requirements.in` | Generate lock |
| `uv pip sync requirements.txt` | Sync from file |

### Other
| Command | Purpose |
|---------|---------|
| `uv cache clean` | Clear cache |
| `uv tree` | Show dependency tree |
| `uv audit` | Check for vulnerabilities |
| `uv export` | Export lock to alternate format |

## Pitfalls
- PEP 668: On system Python, use `uv venv` first — `uv pip install` without a venv will fail on managed systems
- `uv add` automatically syncs — no need to run `uv sync` separately
- Use `uv tool run` (or `uvx`) for one-off commands instead of `uv tool install`
- Lockfiles are project-scoped — `uv.lock` stays with `pyproject.toml`

## Verification
```bash
uv --version
uv tool list
uv python list
```

## Skills Required

| Skill | Purpose |
|-------|---------|
| `hermes-agent` | Core Hermes functionality |
| `skill-judge` | Evaluate skill quality |

## Verification Checklist

- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has >=3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md under 250 lines
- [ ] No placeholder text

## Workflow

### Phase 1: Preparation

Set up required environment, dependencies, and configuration for "uv Python Package Manager".

### Phase 2: Execution

Run the primary "uv Python Package Manager" operations according to the defined requirements.

### Phase 3: Verification

Verify output, handle any errors, and confirm results meet expectations.

### Phase 4: Completion

Document results, clean up resources, and finalize any deliverables.

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
