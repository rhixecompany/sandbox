#!/usr/bin/env python3
"""Generate standardized SKILL.md files for all 63 skills."""

import os
from pathlib import Path

# Skill descriptions mapping
SKILL_DESCRIPTIONS = {
    'agent-browser': 'Browser automation CLI for AI agents. Automate web interactions, fill forms, take screenshots, extract data, test web apps.',
    'algorithmic-art': 'Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration.',
    'asdf': 'Universal version manager for multiple runtimes (Node.js, Python, Go, Terraform, etc.).',
    'banking': 'Next.js 16 fintech banking app with PostgreSQL, Drizzle ORM, NextAuth v4, Plaid/Dwolla integrations.',
    'brand-guidelines': 'Applies Anthropic official brand colors and typography to artifacts.',
    'canvas-design': 'Create beautiful visual art in .png and .pdf documents using design philosophy.',
    'caveman': 'Ultra-compressed communication mode. Cuts token ~75% while keeping technical accuracy.',
    'caveman-commit': 'Ultra-compressed commit message generator. Conventional Commits format.',
    'caveman-review': 'Ultra-compressed code review comments. Each comment one line: location, problem, fix.',
    'caveman-compress': 'Compress memory files into caveman-speak (~75% token reduction).',
    'claude-api': 'Build, debug, and optimize Claude API / Anthropic SDK apps with prompt caching.',
    'clonedeps': 'Clone important project dependency source code into local workspace for inspection.',
    'code-docs': 'Google Style documentation for Python, Go, Terraform.',
    'codemap': 'Generate comprehensive hierarchical codemaps for unfamiliar repositories.',
    'content-research-writer': 'Collaborative writing partner for research-assisted content creation.',
    'context7': 'Retrieve up-to-date documentation for software libraries and frameworks.',
    'customize-opencode': 'Configure opencode itself: opencode.json, .opencode/, agents, skills, plugins.',
    'datadog': 'Datadog observability for debugging and incident triage.',
    'dispatching-parallel-agents': 'Use when facing 2+ independent tasks that can be worked on without shared state.',
    'doc-coauthoring': 'Guide for co-authoring documentation, proposals, technical specs, decision docs.',
    'docx': 'Create, read, edit, or manipulate Word documents (.docx files).',
    'executing-plans': 'Execute written implementation plans in separate session with review checkpoints.',
    'file-organizer': 'Create effective file organization with decision trees for archive strategy.',
    'finishing-a-development-branch': 'Guide completion of development work with structured merge/PR options.',
    'frontend-design': 'Create distinctive, production-grade frontend interfaces with high design quality.',
    'git-helper': 'Git workflow assistance, branch management, and commit message optimization.',
    'glab': 'Expert guidance for using GitLab CLI (glab) to manage GitLab resources.',
    'httpie': 'CLI HTTP client for APIs. REST requests, debugging services, testing endpoints.',
    'humanizer': 'Identify and remove AI-generated writing patterns to make text sound authentic.',
    'internal-comms': 'Resources for writing internal communications using company formats.',
    'jira': 'Jira ticket operations via CLI or MCP.',
    'marp-slide': 'Create professional Marp presentation slides with 7 themes.',
    'mcp-builder': 'Guide for creating high-quality MCP (Model Context Protocol) servers.',
    'meeting-insights-analyzer': 'Analyze meeting transcripts to uncover behavioral patterns and communication insights.',
    'mermaid-diagrams': 'Create software diagrams using Mermaid syntax.',
    'pdf': 'Read, extract, combine, split, encrypt, or OCR PDF files.',
    'plans-and-specs': 'Instructions for using planning plugin tools.',
    'pptx': 'Create, read, edit, or manipulate PowerPoint presentation files (.pptx).',
    'project-docs': 'Generate complete documentation structures (README, ARCHITECTURE, GUIDES).',
    'receiving-code-review': 'Handle code review feedback with technical rigor and verification.',
    'requesting-code-review': 'Verify work meets requirements before merging.',
    'shadcn': 'Manage shadcn components and projects.',
    'simplify': 'Simplify code for clarity without changing behavior.',
    'skill-creator': 'Create new skills, modify existing skills, and measure skill performance.',
    'skill-judge': 'Evaluate Agent Skill design quality against specifications.',
    'slack-gif-creator': 'Knowledge and utilities for creating animated GIFs optimized for Slack.',
    'subagent-driven-development': 'Execute implementation plans with independent tasks in current session.',
    'task-management': 'Task management CLI for tracking and managing feature subtasks.',
    'template-skill': 'Starting template when creating a new skill.',
    'theme-factory': 'Toolkit for styling artifacts with themes.',
    'using-git-worktrees': 'Ensure isolated workspace exists via native tools or git worktree fallback.',
    'using-superpowers': 'Establish how to find and use skills.',
    'verification-before-completion': 'Verify work is complete before committing or creating PRs.',
    'web-artifacts-builder': 'Create elaborate multi-component HTML artifacts using React, Tailwind, shadcn/ui.',
    'webapp-testing': 'Toolkit for interacting with and testing local web applications using Playwright.',
    'work-on-ticket': 'Fetch Jira ticket details, create git branch, initiate task planning.',
    'worktrunk': 'Worktrunk (wt) git worktree management and parallel AI agent execution.',
    'writing-clearly-and-concisely': 'Improve prose clarity using Strunk principles and AI anti-pattern detection.',
    'writing-plans': 'Use when you have a spec or requirements for a multi-step task.',
    'writing-skills': 'Create new skills, edit existing skills, or verify skills work.',
    'xlsx': 'Create, read, edit, or fix spreadsheet files (.xlsx, .csv, .tsv).',
}

TEMPLATE = """# {skill_name}

## Description

{description}

## When to Use

Use this skill when:
- [Primary use case 1]
- [Primary use case 2]
- [Primary use case 3]

**Triggers**: "[Trigger phrase 1]", "[Trigger phrase 2]", "[Trigger phrase 3]"

## When NOT to Use

- For code review (use requesting-code-review instead)
- For debugging (use systematic-debugging instead)
- [Other exclusions]

## Workflow

### Phase 1: Preparation
- Understand requirements
- Gather context
- Identify constraints

### Phase 2: Execution
- Execute main task
- Verify results
- Document decisions

### Phase 3: Verification
- Test outcomes
- Get feedback
- Refine as needed

## Tools & References

**Related Skills**:
- [Related skill 1]
- [Related skill 2]

## Best Practices

- **[Practice 1]**: [Description]
- **[Practice 2]**: [Description]
- **[Practice 3]**: [Description]
"""

def generate_skill_file(skill_name, description):
    """Generate a standardized SKILL.md file."""
    content = TEMPLATE.format(
        skill_name=skill_name,
        description=description
    )
    return content

def main():
    """Generate all skill files."""
    base_path = Path('.opencode/skills')
    
    created = 0
    for skill_name, description in SKILL_DESCRIPTIONS.items():
        skill_dir = base_path / skill_name
        skill_file = skill_dir / 'SKILL.md'
        
        # Skip if already exists
        if skill_file.exists():
            print(f"Skipping {skill_name} (already exists)")
            continue
        
        # Create directory if needed
        skill_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate and write file
        content = generate_skill_file(skill_name, description)
        skill_file.write_text(content)
        created += 1
        print(f"Created {skill_name}")
    
    print(f"\nTotal created: {created}")

if __name__ == '__main__':
    main()
