#!/bin/bash
# Auto-extracted from: cli.md
# Source block language: bash
hermes worktree list              # audit: age, size, verdict, reason per tree
hermes worktree prune             # remove safe trees + delete merged branches
hermes worktree prune --dry-run   # show the plan without changing anything
hermes worktree prune --trees-only     # leave local branches alone
hermes worktree prune --branches-only  # leave worktrees alone
