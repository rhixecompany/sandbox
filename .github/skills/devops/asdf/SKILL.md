---
name: asdf
title: Asdf
description: "Use when installing or configuring asdf version manager, managing multiple runtime versions (Node.js, Python, Go), or migrating from nvm/pyenv/rbenv."
version: 1.0.0
author: "Hermes Agent"
license: MIT
tags: 
metadata:
  hermes:
    tags: [imported]
---
# Asdf

## Overview

Universal version manager for multiple runtimes (Node.js, Python, Go, Terraform, etc.). Use this skill to install asdf, manage runtime versions with `.tool-versions`, configure plugins, and migrate from nvm, pyenv, or rbenv.

## When to Use

- Installing or configuring asdf
- Managing multiple runtime versions across teams
- Migrating from nvm, pyenv, rbenv
- Creating or updating `.tool-versions`
- Configuring asdf plugins for uncommon or legacy runtimes
- Standardizing developer environment versions

## When NOT to Use

- Docker-only project environments without local runtime needs
- Strict EOL or vendor lock-in version tooling that must remain unchanged
- One-off local experiments without team sharing

## Skills Required

| Skill | Purpose |
|-------|---------|
| `git-helper` | Branch and environment versioning discipline |
| `task-management` | Track runtime-migration tasks and validation steps |

## Workflow

### Phase 1: Install Asdf

1. Install runtime dependencies for asdf plugins if required.
2. Install asdf in the expected location for the platform.
3. Add shell integration for asdf shims and activation.
4. Verify `asdf --version`.

### Phase 2: Configure Plugins and Runtimes

1. Review supported runtimes for the project.
2. Add the runtime plugins needed.
3. Install the runtime versions required by `.tool-versions`.
4. Rehash when versions change.

Example commands:

```bash
asdf plugin-add nodejs https://github.com/asdf-vm/asdf-nodejs.git
asdf install nodejs latest
asdf install golang latest

asdf local nodejs latest golang latest
asdf reshim nodejs
```

### Phase 3: Use .tool-versions for Reproducible Runtimes

1. Create or update `.tool-versions` from known-good runtime versions.
2. Commit `.tool-versions` so teammates and CI use the same versions.
3. Avoid per-developer invisible version overrides unless explicitly documented.

Example `.tool-versions`:

```text
nodejs 20.11.0
python 3.12.2
golang 1.22.3
```

### Phase 4: Migrate from Other Version Managers

1. Identify current version manager rationale and pinned versions.
2. Map version-manager commands to asdf equivalents.
3. Replace boot scripts or shell initialization.
4. Validate workflows after migration with core tasks.

### Phase 5: Maintain Versions

1. Update plugins and runtime versions in `.tool-versions`.
2. Prune unused local versions.
3. Re-run project validation after version changes.
4. Share migration rationale and exceptions in the repo docs.

## Verification Checklist

- [ ] Asdf installed and active in the shell
- [ ] Plugin list matches runtime requirements
- [ ] `.tool-versions` present and version valid
- [ ] `asdf install` completes without errors
- [ ] Project commands run successfully with the expected runtime versions
- [ ] Migrated users can reproduce the same runtime set

## Pitfalls

- Adding plugins without confirming supported tool versions leads to unexpected incompatibilities.
- Forgetting `.tool-versions` or `.tool-versions` in `.gitignore` breaks team reproducibility.
- Running `asdf reshim` after changing tool versions avoids stale shims.
- Overusing global version overrides reduces reproducibility; prefer `.tool-versions`.
