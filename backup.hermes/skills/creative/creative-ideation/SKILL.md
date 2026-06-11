---
name: creative-ideation
title: Creative Ideation — Constraint-Driven Project Generation
description: "Generate project ideas via creative constraints."
version: 1.0.0
author: SHL0MS
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Creative, Ideation, Projects, Brainstorming, Inspiration]
    category: creative
    requires_toolsets: []
---

# Creative Ideation

## When to use

Use when the user says 'I want to build something', 'give me a project idea', 'I'm bored', 'what should I make', 'inspire me', or any variant of 'I have tools but no direction'. Works for code, art, hardware, writing, tools, and anything that can be made.

Generate project ideas through creative constraints. Constraint + direction = creativity.

## How It Works

1. **Pick a constraint** from the library below — random, or matched to the user's domain/mood
2. **Interpret it broadly** — a coding prompt can become a hardware project, an art prompt can become a CLI tool
3. **Generate 3 concrete project ideas** that satisfy the constraint
4. **If they pick one, build it** — create the project, write the code, ship it

## The Rule

Every prompt is interpreted as broadly as possible. "Does this include X?" → Yes. The prompts provide direction and mild constraint. Without either, there is no creativity.

## Constraint Library

### For Developers

**Solve your own itch:**
Build the tool you wished existed this week. Under 50 lines. Ship it today.

**Automate the annoying thing:**
What's the most tedious part of your workflow? Script it away. Two hours to fix a problem that costs you five minutes a day.

**The CLI tool that should exist:**
Think of a command you've wished you could type. `git undo-that-thing-i-just-did`. `docker why-is-this-broken`. `npm explain-yourself`. Now build it.

**Nothing new except glue:**
Make something entirely from existing APIs, libraries, and datasets. The only original contribution is how you connect them.

**Frankenstein week:**
Take something that does X and make it do Y. A git repo that plays music. A Dockerfile that generates poetry. A cron job that sends compliments.

**Subtract:**
How much can you remove from a codebase before it breaks? Strip a tool to its minimum viable function. Delete until only the essence remains.

**High concept, low effort:**
A deep idea, lazily executed. The concept should be brilliant. The implementation should take an afternoon. If it takes longer, you're overthinking it.

### For Makers & Artists

**Blatantly copy something:**
Pick something you admire — a tool, an artwork, an interface. Recreate it from scratch. The learning is in the gap between your version and theirs.

**One million of something:**
One million is both a lot and not that much. One million pixels is a 1MB photo. One million API calls is a Tuesday. One million of anything becomes interesting at scale.

**Make something that dies:**
A website that loses a feature every day. A chatbot that forgets. A countdown to nothing. An exercise in rot, killing, or letting go.

**Do a lot of math:**
Generative geometry, shader golf, mathematical art, computational origami. Time to re-learn what an arcsin is.

### For Anyone

**Text is the universal interface:**
Build something where text is the only interface. No buttons, no graphics, just words in and words out. Text can go in and out of almost anything.

**Start at the punchline:**
Think of something that would be a funny sentence. Work backwards to make it real. "I taught my thermostat to gaslight me" → now build it.

**Hostile UI:**
Make something intentionally painful to use. A password field that requires 47 conditions. A form where every label lies. A CLI that judges your commands.

**Take two:**
Remember an old project. Do it again from scratch. No looking at the original. See what changed about how you think.

See `references/full-prompt-library.md` for 30+ additional constraints across communication, scale, philosophy, transformation, and more.

## Matching Constraints to Users

| User says | Pick from |
|-----------|-----------|
| "I want to build something" (no direction) | Random — any constraint |
| "I'm learning [language]" | Blatantly copy something, Automate the annoying thing |
| "I want something weird" | Hostile UI, Frankenstein week, Start at the punchline |
| "I want something useful" | Solve your own itch, The CLI that should exist, Automate the annoying thing |
| "I want something beautiful" | Do a lot of math, One million of something |
| "I'm burned out" | High concept low effort, Make something that dies |
| "Weekend project" | Nothing new except glue, Start at the punchline |
| "I want a challenge" | One million of something, Subtract, Take two |

## Output Format

```
## Constraint: [Name]
> [The constraint, one sentence]

### Ideas

1. **[One-line pitch]**
   [2-3 sentences: what you'd build and why it's interesting]
   ⏱ [weekend / week / month] • 🔧 [stack]

2. **[One-line pitch]**
   [2-3 sentences]
   ⏱ ... • 🔧 ...

3. **[One-line pitch]**
   [2-3 sentences]
   ⏱ ... • 🔧 ...
```

## Example

```
## Constraint: The CLI tool that should exist
> Think of a command you've wished you could type. Now build it.

## Attribution

Constraint approach inspired by [wttdotm.com/prompts.html](https://wttdotm.com/prompts.html). Adapted and expanded for software development and general-purpose ideation.

## When to Use

- When you need to use creative ideation for creative or design tasks
- When a project requires creative ideation output or integration
- When automating or generating creative ideation-style content
- **Triggers**: "Creative Ideation" required for a project

## Overview

The Skills\creative\creative Ideation\skill.md skill provides tools and workflows for managing skills\creative\creative ideation\skill.md operations efficiently.

## Verification Checklist

- [ ] Environment and dependencies are properly configured
- [ ] Creative Ideation output was generated successfully
- [ ] Output meets expected quality and style requirements
- [ ] Any errors during execution were resolved
- [ ] Final result is saved or delivered as expected
```
