---
license: MIT
author: Hermes Agent
version: 1.0.0
title: ai-prompt-engineering-safety-review
name: ai-prompt-engineering-safety-review
trigger: /ai-prompt-engineering-safety-review
description: >-
  Review a prompt for safety, bias, security, clarity, and effectiveness, then produce a safer improved version.
tags: []
  - hermes
  - copilot
  - safety
  - security
  - bias
  - optimization
dependencies:
  - skill:/prompt-engineering
  - skill:systematic-debugging
  - skill:/context-map
skills:
  - prompt-engineering
  - systematic-debugging
---

# ai-prompt-engineering-safety-review

> Review an input prompt for safety, bias, security, clarity, and effectiveness, then return a stronger version.

## Goal

Review an input prompt for safety, bias, security, clarity, and effectiveness, then return a stronger version.

## Context

- Use when the user wants a prompt reviewed or improved before reuse
- Prefer concrete recommendations over theory
- Keep the rewritten prompt aligned with the original intent and required constraints; clarity edits must not remove necessary requirements
- Call out safety or security issues explicitly

## Inputs

- The original prompt
- Optional task context or target domain
- Optional constraints, output format, or policy requirements
- If no prompt is provided, or if the input is not recognizable as a prompt (for example, raw code, a URL, or plain data), respond with: "No prompt detected. Please provide the prompt text you want reviewed."

## Outputs

- A prompt analysis report
- A revised prompt
- A short checklist of safety and quality improvements

## Rules

1. Check harmful content, misinformation, and illegal activity risk first
2. Check bias, privacy, and prompt-injection risk
3. Assess clarity, specificity, constraints, and output format
4. If the prompt's primary purpose is to produce harmful, illegal, or unethical output and no safe rewrite is possible, stop and return only a refusal explaining why the prompt cannot be improved
5. Preserve the useful task intent when rewriting
6. Add safeguards only when a specific risk was identified in Phase 1 analysis; do not add generic safety disclaimers unrelated to identified risks
7. Keep the improved prompt shorter and clearer when possible, but never at the expense of required intent or constraints

## Skills Required

| Skill | Purpose |
| --- | --- |
| `context-map` | Preflight mapping for prompt sources, references, and impacted files |
| `prompt-engineering` | Research-backed prompt optimization patterns (scope analysis, clarity assessment) |
| `systematic-debugging` | Systematic detection of prompt safety and quality issues (risk detection, bias, clarity checks) |

## Phases

> ### Phase 1: Analyze the prompt
> **Goal:** understand what the prompt asks for and where it may fail.

> **Full content:** `templates/ai-prompt-engineering-safety-review/phases.md`

## Actions Summary

1. Analyze the prompt for safety and quality issues
2. Rewrite the prompt to reduce risk and improve clarity
3. Validate the revised prompt
4. Return the improved prompt and key notes


## Template References

Detailed templates in `templates/ai-prompt-engineering-safety-review/`:
- `phases.md`
