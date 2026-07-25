# Remediation Patterns — 2026-06-04 Session

Concrete patterns discovered during the skills-fix session. Reference when running future audits.

## Issue Codes (Expanded)

| Code | Pattern | Severity | Fix |
|------|---------|----------|-----|
| F1 | Missing YAML frontmatter block | Critical | Add frontmatter with name and description |
| F2 | Missing required frontmatter key | Critical | Add the key |
| F3 | Goal section with duplicate "Use when" | Critical | Remove duplicate prefix |
| F3b | Goal section with quoted description boilerplate | Critical | Extract clean description |
| F3c | Frontmatter closing delimiter glued to Goal heading | Critical | Insert newline, then apply F3b fix |
| C1 | Stale pip install patterns | Major | Informational supply_chain warning |
| C2 | Unclosed code fence | Major | Append closing fence |
| S1 | Missing When to Use or Workflow section | Minor | Add section or accept variant |
| S2 | Heading level jump | Minor | Insert intermediate heading |
| R1 | Duplicate section heading | Moderate | Remove duplicate, merge content |

## F3c Fix Procedure (Glued Frontmatter)

The F3c pattern: frontmatter closing delimiter directly adjacent to ## Goal with no newline.

Two-step fix:
1. Separate the delimiter by replacing the glued pattern with a newline
2. Apply standard F3b fix to extract the clean description

## Reorganization Pattern

Skills at skills/name/ (root level) should be moved to skills/category/name/.

Detection: iterate os.listdir and flag any entry that is a directory containing SKILL.md directly.

Common category mappings:
- agent-browser, agent-governance, copilot-cli, opencode -> autonomous-ai-agents/
- algorithmic-art, brand-guidelines, canvas-design -> creative/
- asdf, aspire, azure-*, dependabot -> devops/
- chrome-devtools, create-*, vscode-* -> development/
- gh-cli, git-commit, github-* -> github/
- brainstorming, plans-and-specs -> planning/
- adversarial-ux-test, playwright-* -> qa/
- banking, fluentui-blazor, nuget-manager -> software-development/

## Windows Path Separator Pitfall

os.walk() on Windows returns backslash paths. Always use os.path.join() for construction and normalize with replace for string matching.

## Batch Size

Process skills in batches of 7 for audit display, but use execute_code with os.walk for bulk operations to avoid the 50-tool-call limit.

## Verification Checklist

After any bulk fix pass:
1. Re-run audit and confirm F=0, C less than or equal to 5
2. Spot-check 5 random fixed skills by reading files directly (not skill_view which is cached)
3. git diff --stat to review scope
4. Commit with chore: skill library audit and remediation date
