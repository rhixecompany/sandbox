#!/usr/bin/env bash
git checkout -b skills-migration/batch-15
git add \
  "99|.opencode/skills/internal-comms/examples/3p-updates.md" \
  "100|.opencode/skills/internal-comms/examples/company-newsletter.md" \
  "101|.opencode/skills/internal-comms/examples/faq-answers.md" \
  "102|.opencode/skills/internal-comms/examples/general-comms.md" \
  "103|.opencode/skills/internal-comms/SKILL.md" \
  "104|.opencode/skills/jira/references/commands.md" \
  "105|.opencode/skills/jira/references/mcp.md" \

git commit -m "chore(skills): migrate batch 15 — normalize frontmatter and fix formatting (author: Alexa)"
# git push origin skills-migration/batch-15  # commented out — requires approval