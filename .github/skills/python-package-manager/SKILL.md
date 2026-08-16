---
author: Hermes Agent
description: Manage Python virtual environments, dependencies, and package operations across Hermes workspace and projects. Supports pip, uv, poetry, and conda with unified interface.
category: devops
license: MIT
metadata:
  hermes:
    related_skills:
    - uv-package-manager
    - pnpm-package-manager
    - hermes-setup
    tags:
    - python
    - packages
    - venv
    - dependencies
    - pip
    - uv
name: python-package-manager
tags:
- python
- packages
- venv
- dependencies
- pip
- uv
- poetry
- conda
title: Python Package Manager
version: 1.0.0
---
# Python Package Manager

## Overview

Unified interface for Python virtual environment and package management across Hermes workspace. Supports pip, uv, poetry, and conda with consistent commands and environment detection.

## When to Use

- Creating/managing venvs for projects
- Installing/syncing dependencies
- Locking/unlocking requirements
- Cross-project dependency analysis

## Supported Tools

| Tool | Use Case | Lock File |
|------|----------|-----------|
| `uv` | Fast installs, venv management | `uv.lock` |
| `pip` | Standard pip operations | `requirements.txt` |
| `poetry` | Full project management | `poetry.lock` |
| `conda` | Binary packages, ML envs | `environment.yml` |

## Workflow

### Phase 1: Environment Setup

```bash
# Create venv with uv (fastest)
python $LOCALAPPDATA/hermes/scripts/configure_hermes.py --venv --tool uv

# Or with conda
python $LOCALAPPDATA/hermes/scripts/configure_hermes.py --venv --tool conda
```

### Phase 2: Dependency Sync

```bash
# Sync from pyproject.toml / requirements.txt
python $LOCALAPPDATA/hermes/scripts/merge_config.py --sync-deps

# Lock dependencies
python $LOCALAPPDATA/hermes/scripts/batch_update_hermes_paths.py --lock
```

### Phase 3: Analysis

```bash
# Check for unused deps
python $LOCALAPPDATA/hermes/scripts/trim_banking.py --unused-deps

# Cross-project diff
python $LOCALAPPDATA/hermes/scripts/diff_skills.py --deps
```

## Script Reference

**Location:** `~/AppData/Local/hermes/scripts/`

| Script | Purpose |
|--------|---------|
| `configure_hermes.py` | Venv creation, tool selection |
| `merge_config.py` | Config merging, dep sync |
| `batch_update_hermes_paths.py` | Path normalization, locking |
| `trim_banking.py` | Unused dep detection |
| `diff_skills.py` | Cross-project dep diff |


## Pitfalls

- **None identified yet** — Review edge cases and failure modes for this skill's domain.
- **Assumptions** — Verify platform compatibility (Windows/Mac/Linux) before relying on default paths.
- **State management** — Terminal state persists across calls; exported vars and working directory carry forward.
- **Error handling** — Always validate tool output before proceeding to the next step.

## Related Skills

- `uv-package-manager` — uv-specific operations
- `pnpm-package-manager` — Node.js equivalent
- `hermes-setup` — Initial Hermes environment setup

## Verification Checklist

- [ ] Prerequisites and environment are properly configured
- [ ] Python Package Manager operations completed successfully
- [ ] Output meets expected quality and requirements
- [ ] Any errors during execution were resolved
- [ ] Changes are documented and committed if applicable

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
