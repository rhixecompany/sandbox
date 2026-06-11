#!/usr/bin/env bash
git checkout -b skills-migration/batch-18
git add \
  "120|.opencode/skills/marp-slide/references/theme-selection.md" \
  "121|.opencode/skills/marp-slide/SKILL.md" \
  "122|.opencode/skills/mcp-builder/reference/design-principles.md" \
  "123|.opencode/skills/mcp-builder/reference/evaluation.md" \
  "124|.opencode/skills/mcp-builder/reference/mcp_best_practices.md" \
  "125|.opencode/skills/mcp-builder/reference/node_mcp_server.md" \
  "126|.opencode/skills/mcp-builder/reference/python_mcp_server.md" \

git commit -m "chore(skills): migrate batch 18 — normalize frontmatter and fix formatting (author: Alexa)"
# git push origin skills-migration/batch-18  # commented out — requires approval