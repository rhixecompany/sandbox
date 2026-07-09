#!/usr/bin/env bash
git checkout -b skills-migration/batch-20
git add \
  "134|.opencode/skills/mermaid-diagrams/references/architecture-diagrams.md" \
  "135|.opencode/skills/mermaid-diagrams/references/c4-diagrams.md" \
  "136|.opencode/skills/mermaid-diagrams/references/class-diagrams.md" \
  "137|.opencode/skills/mermaid-diagrams/references/erd-diagrams.md" \
  "138|.opencode/skills/mermaid-diagrams/references/flowcharts.md" \
  "139|.opencode/skills/mermaid-diagrams/references/sequence-diagrams.md" \
  "140|.opencode/skills/mermaid-diagrams/SKILL.md" \

git commit -m "chore(skills): migrate batch 20 — normalize frontmatter and fix formatting (author: Alexa)"
# git push origin skills-migration/batch-20  # commented out — requires approval