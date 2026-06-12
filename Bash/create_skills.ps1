# DRY_RUN_SUPPORT=true
﻿$skills = @(
    'agent-browser', 'algorithmic-art', 'asdf', 'banking', 'caveman', 'caveman-commit',
    'caveman-review', 'caveman-compress', 'claude-api', 'clonedeps', 'code-docs', 'codemap',
    'content-research-writer', 'context7', 'customize-opencode', 'datadog',
    'dispatching-parallel-agents', 'doc-coauthoring', 'docx', 'executing-plans',
    'file-organizer', 'finishing-a-development-branch', 'git-helper', 'glab', 'httpie',
    'humanizer', 'internal-comms', 'jira', 'marp-slide', 'mcp-builder',
    'meeting-insights-analyzer', 'mermaid-diagrams', 'pdf', 'plans-and-specs', 'pptx',
    'project-docs', 'receiving-code-review', 'requesting-code-review', 'shadcn', 'simplify',
    'skill-creator', 'skill-judge', 'slack-gif-creator', 'subagent-driven-development',
    'task-management', 'template-skill', 'theme-factory', 'using-git-worktrees',
    'using-superpowers', 'verification-before-completion', 'web-artifacts-builder',
    'webapp-testing', 'work-on-ticket', 'worktrunk', 'writing-clearly-and-concisely',
    'writing-plans', 'writing-skills', 'xlsx'
)

$template = @"
# {0}

## Description

Standardized skill for {0}.

## When to Use

Use this skill when:
- Primary use case 1
- Primary use case 2
- Primary use case 3

## When NOT to Use

- When not applicable
- For other purposes

## Workflow

### Phase 1: Preparation
- Understand requirements
- Gather context

### Phase 2: Execution
- Execute main task
- Verify results

## Best Practices

- Practice 1
- Practice 2
- Practice 3
"@

$count = 0
foreach ($skill in $skills) {
    $skillPath = ".opencode/skills/$skill/SKILL.md"
    if (-not (Test-Path $skillPath)) {
        $skillDir = Split-Path -Parent $skillPath
        if (-not (Test-Path $skillDir)) {
            New-Item -ItemType Directory -Path $skillDir -Force | Out-Null
        }
        $content = $template -f $skill
        Set-Content -Path $skillPath -Value $content
        $count++
    }
}

Write-Host "Created $count SKILL.md files"
Set-StrictMode -Version Latest
