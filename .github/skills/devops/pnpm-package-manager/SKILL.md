---
name: pnpm-package-manager
title: "pnpm — Fast Node Package Manager"
description: "Guide for pnpm — disk-efficient Node package manager. Covers install, workspace management, and monorepo workflows."
version: 1.0.0
author: "Hermes Assistant"
tags: [node, pnpm, package-manager, monorepo]
---

# pnpm — Node Package Manager (Fast, Disk-Efficient)

## When to Use
- Installing Node.js dependencies (`pnpm install`)
- Managing monorepo workspaces (`pnpm -r`, `pnpm --filter`)
- Adding packages (`pnpm add`)
- Running package scripts (`pnpm run`, `pnpm exec`)

## Key Commands

| Command | Purpose |
|---------|---------|
| `pnpm install` | Install all dependencies |
| `pnpm add <pkg>` | Add dependency |
| `pnpm add -D <pkg>` | Add dev dependency |
| `pnpm remove <pkg>` | Remove dependency |
| `pnpm update` | Update all deps |
| `pnpm audit` | Check security |
| `pnpm ls` | List installed packages |
| `pnpm why <pkg>` | Why is this installed |
| `pnpm run <script>` | Run package script |
| `pnpm exec <cmd>` | Execute in project context |
| `pnpm dlx <pkg>` | Download + run package (like npx) |

### Workspace / Monorepo
| Command | Purpose |
|---------|---------|
| `pnpm -r <cmd>` | Run in all packages |
| `pnpm --filter <pkg> <cmd>` | Run in specific package |
| `pnpm publish` | Publish package |
| `pnpm list --depth=10` | Deep dependency tree |

## Pitfalls
- pnpm uses symlinked `node_modules` — don't assume flat structure
- Use `pnpm exec` instead of direct `node_modules/.bin/` paths
- `pnpm update` updates to latest within range — use `pnpm up --latest` for major bumps
- Workspaces require `pnpm-workspace.yaml`

## Verification
```bash
pnpm --version
pnpm audit
```
