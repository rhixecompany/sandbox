# DRY_RUN_SUPPORT=true
param(
    [switch]$DryRun
)
if ($env:DRY_RUN -eq 'true' -or $DryRun.IsPresent) {
    Write-Host "DRY-RUN: prepare git commit batch 1 (no side effects)"
    exit 0
}

git checkout -b skills-migration/batch-1
git add ".opencode/skills/agent-browser/SKILL.md"
git add ".opencode/skills/algorithmic-art/SKILL.md"
git add ".opencode/skills/asdf/references/plugin-install.md"
git add ".opencode/skills/asdf/SKILL.md"
git add ".opencode/skills/banking/reference/dal-patterns.md"
git add ".opencode/skills/banking/reference/idempotency-key-pattern.md"
git add ".opencode/skills/banking/reference/testing.md"

git commit -m "chore(skills): migrate batch 1 — normalize frontmatter and fix formatting (author: Alexa)"
# git push origin skills-migration/batch-1  # commented out — requires approval
