#!/usr/bin/env bash
git checkout -b skills-migration/batch-23
git add \
  "155|.opencode/skills/sandbox/reference/repo-inventory.md" \
  "156|.opencode/skills/sandbox/reference/workflow.md" \
  "157|.opencode/skills/sandbox/SKILL.md" \
  "158|.opencode/skills/shadcn/cli.md" \
  "159|.opencode/skills/shadcn/customization.md" \
  "160|.opencode/skills/shadcn/mcp.md" \
  "161|.opencode/skills/shadcn/rules/base-vs-radix.md" \

git commit -m "chore(skills): migrate batch 23 — normalize frontmatter and fix formatting (author: Alexa)"
# git push origin skills-migration/batch-23  # commented out — requires approval