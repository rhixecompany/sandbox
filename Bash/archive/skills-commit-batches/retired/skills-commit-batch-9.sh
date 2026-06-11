#!/usr/bin/env bash
git checkout -b skills-migration/batch-9
git add \
  "57|.opencode/skills/claude-api/typescript/claude-api/tool-use.md" \
  "58|.opencode/skills/claude-api/typescript/managed-agents/README.md" \
  "59|.opencode/skills/clonedeps/codemap.md" \
  "60|.opencode/skills/clonedeps/README.md" \
  "61|.opencode/skills/clonedeps/SKILL.md" \
  "62|.opencode/skills/code-docs/references/go_google_style.md" \
  "63|.opencode/skills/code-docs/references/python_google_style.md" \

git commit -m "chore(skills): migrate batch 9 — normalize frontmatter and fix formatting (author: Alexa)"
# git push origin skills-migration/batch-9  # commented out — requires approval