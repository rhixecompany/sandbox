---
name: hermes-profile-documentation
title: Hermes Profile Documentation Architecture
description: Author and maintain Hermes profile documentation (USER.md, SOUL.md) using DRY principles. Each file owns one concern; single source of truth for profile state.
version: 1.0.0
author: Alexa
license: MIT
metadata:
  hermes:
    tags: [profiles, documentation, dry-principles, hermes-agent, standards]
    related_skills: [user-communication-preferences, hermes-complete-setup, hermes-agent]
---

# Hermes Profile Documentation Architecture

## Overview

Hermes profiles (default, code-architect, etc.) require consistent, maintainable documentation that evolves with the agent's state and behavior. This skill establishes a three-file architecture that enforces DRY (Don't Repeat Yourself) principles and keeps profile facts synchronized with execution standards.

**Problem solved:** Without this pattern, profile docs become inconsistent, duplicated across files, and difficult to maintain when profile state changes.

## When to Use

- Setting up or updating a Hermes profile (new profile creation, state refresh, after hermes status changes)
- Updating execution standards, communication preferences, or workflow conventions
- Consolidating profile documentation that has drifted or accumulated redundancy
- Creating reusable templates for future profile creation

## File Architecture (Single Source of Truth)

### USER.md — Profile Facts Only

**Purpose:** Identity, active model/provider, execution preferences tied to THIS profile.

**Must include:**
- Name, OS, shell, editor
- Active model and provider
- Configured profiles and auth status
- Execution preferences (delegation strategy, safety rules, approval requirements)
- Development standards reference (cross-link SOUL.md, don't duplicate)

**Must NOT include:**
- Code quality standards (SOUL.md)
- Commit style (SOUL.md)
- File operation rules (SOUL.md)
- Example exchanges or security practices (SOUL.md)

**Template structure:**
```markdown
# USER.md — [Name]'s Profile

## Identity
- **Name:** [name]
- **OS:** [OS]
- **Shell:** [shell preference]

## Active Model & Providers
- **Default Model:** [model] ([provider])
- **Providers:** [list]

## Execution Preferences
- [Preference 1]
- [Preference 2]

## Standards
See SOUL.md for code quality, commit style, response style.
```

### SOUL.md — Execution Standards Only

**Purpose:** Code quality, commit style, response style, security, tool usage, workspace conventions.

**Must include:**
- Identity & tone (role, communication style)
- Core rules (process, philosophy, guardrails)
- File operation rules (backup policy, modification protocol)
- Code quality standards (languages, formatting, linting)
- Commit style and verification order
- Response style (DO/DON'T)
- Security practices
- Workspace conventions

**Must NOT include:**
- Specific model name or provider state (USER.md)
- Personal identity facts (USER.md)
- Current profile state (USER.md)
- Session-specific notes (memory)

**Template structure:**
```markdown
# SOUL.md — Core Operating Principles

| Profile | Owner | See Also |
|---------|-------|----------|
| [name] | [owner] | USER.md |

## Identity & Tone

[Role description]

[3 communication traits as bullets]

## Core Rules

1. [Rule 1]
2. [Rule 2]
3. [Rule 3]

## File Operations

[Backup strategy]

**Protocol:** [Steps]

## Code Quality

**Languages:** [...] | **Formatting:** [...] | **Linting:** [...] | **Commit:** [...]

**Verification:** [Steps]

## Response Style

**✅ DO:** [...] | [...] | [...] | [...]

**❌ DON'T:** [...] | [...] | [...]

## Security

**✅ DO:** [...] | [...] | [...]

**❌ DON'T:** [...] | [...] | [...]

## Workspace

- **Root:** [path]
- **Config:** [path]
- **Secrets:** [path]

---

**Core Principle:** [One-sentence philosophy]
```

### SOUL.md.template — Reusable Starter

**Purpose:** Starter structure for creating new profiles.

**Update:** After discovering gaps in the standard structure or adding new profile types.

## DRY Enforcement Rules

1. **No cross-file duplication.** If a fact appears in USER.md, don't repeat it in SOUL.md. Use cross-references.

2. **One file, one concern:**
   - USER.md: What is the profile? What's its state? (Identity, model, providers, execution prefs)
   - SOUL.md: How should it behave? What are the standards? (Code quality, commit style, response style, security)
   - SOUL.md (profile-specific): Profile-specific identity only. Reference parent SOUL.md for shared standards. Do NOT duplicate parent standards.
   - No blending.

3. **Compact phrasing.** Use pipe-delimited headers, bullets, tables. No verbose narratives. Pipe-separated headers with minimal spacing.

4. **Single source of truth for state.** Run hermes status to refresh USER.md. Don't maintain stale state in multiple places.

5. **References, not copies.** When one file needs to reference another, use a one-line cross-link instead of copying content. E.g., "**See:** Parent SOUL.md for core principles (~/AppData/Local/hermes/SOUL.md)"

6. **Profile-specific SOUL.md pattern:** For non-default profiles, create minimal SOUL.md (template header + profile-specific identity) that references the default/parent SOUL.md. Examples:
   - adminbot: "Methodical, reliable, comprehensive" (admin focus)
   - code-architect: "Opinionated, strategic, rigorous" (architecture focus)
   - creative-director: "Visionary, expressive, collaborative" (creative focus)

## Common Pitfalls

- **Repeating code standards in USER.md.** USER.md is identity + state; SOUL.md is standards. Don't duplicate. Link instead.
- **Putting session notes in USER.md.** Notes belong in memory or session transcripts, not profile docs.
- **Forgetting to update USER.md when profile state changes.** After hermes profile list or hermes status, update USER.md immediately.
- **Creating SOUL.md without a template.** Use SOUL.md.template as starter; don't write from scratch each time.
- **Allowing docs to drift from configuration.** Docs are only useful if they reflect reality. Refresh after every material change.
- **Duplicating parent SOUL.md content in profile-specific SOUL.md.** Profile-specific SOUL.md should reference parent and add only profile-specific identity. Enforce DRY: no standard duplication.
- **Verbose explanations in profile docs.** Keep files compact. Use headers, bullets, pipes. No narrative beyond necessity. Preference: compact phrasing over readability.

## Workflow

### Creating a New Profile

1. Run hermes profile list and hermes status to capture current state
2. Create USER.md with identity, model, execution preferences
3. Create SOUL.md using SOUL.md.template as starter
4. Test: Load profile, verify behavior matches standards
5. Commit: `docs: add [profile-name] documentation`

### Updating Existing Profile Docs

1. Run hermes status to check current state
2. Update USER.md if model, provider, auth, or preferences changed
3. Update SOUL.md if execution standards or workflows changed
4. Use patch (not full rewrites) for targeted edits
5. Verify no duplication between files
6. Commit: `docs: update [profile-name] [what changed]`

## Verification Checklist

- [ ] USER.md reflects current profile state (run hermes status first)
- [ ] SOUL.md defines execution standards (no repetition from USER.md)
- [ ] SOUL.md.template exists as reusable starter
- [ ] No facts repeated across USER.md and SOUL.md
- [ ] USER.md references SOUL.md for standards
- [ ] SOUL.md references USER.md for profile facts
- [ ] Workspace paths are accurate
- [ ] Git status clean after docs update

## References

- `references/profile-refresh-checklist.md` — State refresh workflow
- `references/dry-violations.md` — Common DRY violations and fixes

