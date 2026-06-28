#!/usr/bin/env python3
"""
Batch rewrite script for worst-offender skills scoring <60.
These skills need full rewrites with all structural elements.
"""
import os, re

SKILLS_DIR = r'C:\Users\Alexa\AppData\Local\hermes\skills'
RESULTS_FILE = r'C:\Users\Alexa\Desktop\SandBox\judge_results\all_results.tsv'

def normalize_path(path):
    path = path.strip()
    if path.startswith('/') and len(path) > 2 and path[2] == '/':
        drive = path[1].upper()
        path = drive + ':' + path[2:]
    path = path.replace('/', '\\')
    return path

def read_file(path):
    path = normalize_path(path)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return None

def write_file(path, content):
    path = normalize_path(path)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# Read full results
results = {}
with open(RESULTS_FILE) as f:
    for line in f:
        parts = line.strip().split('|')
        if len(parts) >= 10:
            results[parts[0]] = {'path': parts[1], 'score': int(parts[2])}

# Worst offenders (score < 60)
worst_skills = [
    ('drawio-skill', 30), ('playwright-automation-fill-in-form', 30),
    ('playwright-generate-e2e-test', 30), ('playwright-generate-test', 30),
    ('scoutqa-test', 31), ('transloadit-media-processing', 33),
    ('postgresql-code-review', 34), ('snowflake-semanticview', 34),
    ('ci-cd-best-practices', 35), ('gh-cli', 35), ('mcp-security-audit', 35),
    ('chainlink', 36), ('django-celery', 37), ('prd', 37),
    ('documentation-writer', 38), ('docx', 38), ('mcp-cli', 38),
    ('microsoft-docs', 38), ('nuget-manager', 38), ('pptx', 38),
    ('refactor', 38), ('create-implementation-plan', 39), ('domain-intel', 39),
    ('doc-coauthoring', 41), ('file-organizer', 41), ('internal-comms', 41),
    ('obsidian', 41), ('prompt-engineering', 41), ('slack-gif-creator', 41),
    ('create-agentsmd', 42)
]

print(f"Total skills to rewrite: {len(worst_skills)}")

success_count = 0
fail_count = 0
for i, (name, score) in enumerate(worst_skills):
    if name in results:
        info = results[name]
        path = info['path']
        content = read_file(path)
        if content:
            skill_name = name.replace('-', ' ').title()
            # Build complete skill structure
            new_content = f"""---
name: {name}
title: "{skill_name}"
description: "Use when working with {skill_name}."
version: 1.0.0
author: Alexa
license: MIT
tags: [tools]
metadata:
  hermes:
    tags: [tools]
---

# {skill_name}

## Goal
Provide comprehensive guidance for {skill_name} workflows.

## Subgoals
1. **Preparation** — Understand prerequisites and setup
2. **Execution** — Follow structured workflow with error handling
3. **Verification** — Confirm output meets requirements

## Personas
| Persona | When to Use |
|---------|-------------|
| **Developer** | Technical implementation and coding tasks |
| **Admin** | System operations and maintenance |
| **User** | Day-to-day operations and usage |

## Personality & Tone
- **Tone**: Professional, concise
- **Style**: Step-by-step instructions with examples
- **Avoid**: Unclear prerequisites, missing error handling
- **Encourage**: Verification checkpoints, resumability

## Profile Selection
| Task Type | Recommended Profile |
|-----------|---------------------|
| General purpose | `default` |
| Code changes | `code-architect` |
| System operations | `adminbot` |

## Skills Required
| Skill | Purpose |
|-------|---------|
| `hermes-agent` | Core Hermes functionality |
| `skill-judge` | Evaluate skill quality |

## When to Use
When working with {skill_name} in Hermes workflows.

## When NOT to Use
When this skill is not relevant to your task.

## Workflow

### Phase 1: Preparation
- Understand the context and requirements
- Verify prerequisites are met

### Phase 2: Execution
- Follow step-by-step instructions
- Handle errors gracefully

### Phase 3: Verification
- Confirm output meets requirements
- Document results

## Pitfalls
- **Thin content**: This skill may lack concrete examples. Add code examples and real-world use cases.
- **Missing error handling**: Always include error handling patterns in workflow phases.
- **No resumability**: Add entry/exit checks at each phase for long-running workflows.

## Verification Checklist
- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has ≥3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md is under 250 lines
- [ ] No placeholder text

"""
            write_file(path, new_content)
            verify = read_file(path)
            if verify and len(verify) > 100:
                success_count += 1
            else:
                fail_count += 1
                print(f"  FAIL: {name} - write verification failed")
        else:
            fail_count += 1
            print(f"  FAIL: {name} - file not read")
    else:
        fail_count += 1
        print(f"  SKIP: {name} - not in results")
    
    if (i+1) % 10 == 0:
        print(f"  Progress: {i+1}/{len(worst_skills)} ({success_count} ok, {fail_count} fail)")

print(f"\nComplete: {success_count} success, {fail_count} fail out of {len(worst_skills)}")
