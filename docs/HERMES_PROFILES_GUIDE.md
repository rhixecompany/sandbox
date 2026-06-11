# Hermes Profiles Guide

Created: May 26, 2026

## Overview

Five specialized Hermes Agent profiles for different workflows and tasks.

## Profiles

### 1. code-architect
**Use for:** Heavy refactoring, system design, debugging, test coverage

**Persona:** Senior Staff Software Engineer
- Optimizes for system stability, test coverage, elegant architecture
- Prioritizes truth and technical correctness
- Tests are the spec
- Concise, surgical, pragmatic voice

**Command:** `code-architect chat`

---

### 2. research-analyst
**Use for:** Document processing, URL summarization, deep-dive content creation

**Persona:** Objective Research Analyst
- Synthesizes data, uncovers patterns
- Must cite sources
- Skeptical of unproven claims
- Structure beats prose (tables/bullets)
- Academic, authoritative voice

**Command:** `research-analyst chat`

---

### 3. exec-assistant
**Use for:** Main orchestrator - scheduling, task coordination, workflow management

**Persona:** Proactive Chief of Staff
- Hyper-organized, eliminates inefficiencies
- Anticipates next steps
- Enforces policies and rules
- Polite, firm, action-oriented voice

**Command:** `exec-assistant chat`

---

### 4. patient-tutor
**Use for:** Learning new skills, frameworks, codebase onboarding

**Persona:** Patient Socratic Mentor
- Guides to answers without giving them away
- Meets user at their experience level
- Gives hints and asks questions
- Encouraging, inquisitive, thoughtful voice
- Never provides complete copy-paste solutions

**Command:** `patient-tutor chat`

---

### 5. creative-director
**Use for:** Marketing, strategic thinking, campaigns, narrative crafting

**Persona:** Award-winning Creative Director & Brand Strategist
- Witty, confident, bold, slightly provocative
- Uses wordplay, light sarcasm, metaphors
- Focuses on "why" behind projects
- Always provides alternative angles
- Punchy formatting with bold emphasis

**Command:** `creative-director chat`

---

## Quick Start

Each profile needs initial setup:

```bash
# Configure API keys and model
<profile-name> setup

# Start chatting
<profile-name> chat

# Start gateway (for Telegram/Discord)
<profile-name> gateway start
```

## Profile Locations

All profiles stored at:
```
C:\Users\Alexa\AppData\Local\hermes\profiles\
├── code-architect/
├── research-analyst/
├── exec-assistant/
├── patient-tutor/
└── creative-director/
```

Each contains:
- `SOUL.md` - Personality definition
- `config.yaml` - Configuration
- `.env` - API keys (after setup)
- `skills/` - 90+ bundled skills
- `memories/` - Profile-specific memories

## Usage Examples

### Code Architect
```bash
code-architect chat "Review this authentication system for security issues"
code-architect chat "Refactor this monolithic function into testable units"
```

### Research Analyst
```bash
research-analyst chat "Summarize these 5 research papers on LLM architectures"
research-analyst chat "Extract key findings from this documentation"
```

### Executive Assistant
```bash
exec-assistant chat "Schedule team standup and draft agenda"
exec-assistant chat "Coordinate these 3 parallel tasks across profiles"
```

### Patient Tutor
```bash
patient-tutor chat "Help me understand React hooks"
patient-tutor chat "Guide me through this codebase architecture"
```

### Creative Director
```bash
creative-director chat "Brainstorm campaign ideas for developer tools launch"
creative-director chat "Critique this product landing page copy"
```

## Switching Profiles

```bash
# List all profiles
hermes profile list

# Switch active profile
hermes profile switch code-architect

# Run specific profile without switching
code-architect chat "your prompt"
```

## Memory Isolation

Each profile has separate memories:
- Personal notes in `profiles/<name>/memories/memory.md`
- User profile in `profiles/<name>/memories/user.md`
- Memories DO NOT cross profiles unless explicitly shared

## Best Practices

1. **Match task to profile**
   - Technical work → code-architect
   - Research/writing → research-analyst
   - Coordination → exec-assistant
   - Teaching → patient-tutor
   - Strategy/creative → creative-director

2. **Configure each profile**
   - Run `<profile> setup` before first use
   - Set appropriate model per profile (e.g., GPT-4 for code-architect)
   - Customize SOUL.md if needed

3. **Profile delegation**
   - Use exec-assistant as orchestrator
   - Delegate subtasks to specialist profiles
   - Example: exec-assistant coordinates → code-architect implements

## Customization

Edit SOUL.md for any profile:
```bash
# Open in default editor
code $HOME/AppData/Local/hermes/profiles/code-architect/SOUL.md
```

Update profile description:
```bash
hermes profile describe code-architect "New description here"
```

## Verification

Check profile status:
```bash
hermes profile list
hermes profile info code-architect
```

Test profile personality:
```bash
code-architect chat "Hello, introduce yourself"
```

---

## Related Documentation

- [HERMES_DOCUMENTATION_INDEX.md](HERMES_DOCUMENTATION_INDEX.md) - Complete Hermes reference
- [06-HERMES_AGENT_OFFICIAL_REFERENCE_2026.md](06-HERMES_AGENT_OFFICIAL_REFERENCE_2026.md) - CLI commands
- [HERMES_PROJECT_SETUP.md](HERMES_PROJECT_SETUP.md) - Project usage guide
