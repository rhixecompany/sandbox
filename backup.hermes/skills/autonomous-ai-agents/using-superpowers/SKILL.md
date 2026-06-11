---
name: using-superpowers
title: Using Superpowers
description: "Use when starting any conversation. Establishes how to find and use skills, requiring Skill tool invocation before any response."
---

## Description

Establish how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions. Foundational skill for accessing all other skills.

## When to Use

- Starting any conversation
- Before any response or action
- When unsure which skill applies
- Establishing skill workflow
- Learning about available skills

## When NOT to Use

- Already in active skill workflow
- Non-skill related work
- Real-time execution without planning

## Workflow

### Phase 1: Identify Task

- Understand user request
- Determine task type
- Note any constraints
- Plan approach

### Phase 2: Check Available Skills

- Review available skills
- Identify relevant skills
- Note skill descriptions
- Plan skill invocation

### Phase 3: Invoke Skills

- Load relevant skills
- Review skill content
- Understand workflow
- Plan execution

### Phase 4: Execute & Respond

- Follow skill workflow
- Execute task
- Provide response
- Document decisions

## Tools & References

- **Related Skills**: All other skills
- **Skill Tool**: Load and access skills
- **Skill List**: Available skills in system
- **Documentation**: Skill descriptions and workflows
- **Library hygiene reference**: `references/skill-library-hygiene.md`

## Skill Library Hygiene

- Prefer patching an existing umbrella skill before creating a new one.
- Add durable detail to `references/`, `templates/`, or `scripts/` instead of bloating `SKILL.md`.
- Create new skills only at the class level; avoid one-off task artifacts and session-specific names.
- When a session reveals a reusable fix, workflow, or user preference, capture it immediately as a pitfall, step, or reference file so future sessions start ahead.
- When auditing markdown prompt libraries, use code-aware scans: ignore fenced code blocks for TODO/FIXME and heading-depth checks, and confirm exact duplicate file contents before deleting duplicates.
- If the user explicitly asks to review the conversation and update the library, treat it as a maintenance pass: leave the library better than you found it, and prefer the smallest reusable improvement over a no-op.
- If two skills overlap, note the overlap in the reply and let the curator consolidate later.

## Best Practices

- Check for skills before responding
- Invoke relevant skills early
- Follow skill workflows exactly
- Document skill usage
- Learn from skill patterns
- Share skill knowledge
- Maintain skill library
- Keep skills class-level; use references for session-specific detail

