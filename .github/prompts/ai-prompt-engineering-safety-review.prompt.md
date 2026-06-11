---
trigger: /ai-prompt-engineering-safety-review
description: >-
  Review a prompt for safety, bias, security, clarity, and effectiveness, then produce a safer improved version.
tags: [hermes, copilot, safety, security, bias, optimization]
dependencies:
  - command:/prompt-engineering
  - skill:systematic-debugging
  - command:/context-map
skills:
  - command:/prompt-engineering — Apply safety and quality patterns (optimizes prompts using research-backed patterns)
  - skill:systematic-debugging — Systematic issue detection (detects prompt safety and quality issues)
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

### Phase 1: Analyze the prompt

**Goal:** understand what the prompt asks for and where it may fail.

#### Steps

| Step | Action | Output |
| --- | --- | --- |
| 1.1 | Run `/context-map` for prompt sources, references, and related files | Context map |
| 1.2 | Classify the task and domain | Task summary |
| 1.3 | Review safety, bias, and security risks | Risk notes |
| 1.4 | Review clarity and completeness | Quality notes |

#### Tasks
- Identify the prompt's purpose
- Find unsafe or ambiguous instructions
- Capture missing context that affects quality
- If the prompt contains apparent PII, credentials, or secrets, redact them with placeholders (for example, `[API_KEY]`) in the revised prompt and flag this explicitly in the report

### Phase 2: Improve the prompt

**Goal:** rewrite the prompt into a safer, clearer version.

#### Steps

| Step | Action | Output |
| --- | --- | --- |
| 2.1 | Keep the original intent | Rewritten scope |
| 2.2 | Add missing constraints or safeguards | Improved prompt |
| 2.3 | Remove redundant or risky language | Cleaner draft |

#### Tasks
- Make the task easier to execute
- Reduce ambiguity
- Keep the rewrite concise

### Phase 3: Test the revised prompt

**Goal:** compare the revised prompt against the original for reliability and safety.

#### Steps

| Step | Action | Output |
| --- | --- | --- |
| 3.1 | Compare revised vs original on safety (better/equal/worse) | Safety comparison + one-sentence reason |
| 3.2 | Compare revised vs original on clarity (better/equal/worse) | Clarity comparison + one-sentence reason |
| 3.3 | Compare revised vs original on usability (better/equal/worse) | Usability comparison + one-sentence reason |

#### Tasks
- Look for remaining risky instructions
- Confirm the output shape is obvious
- Confirm the prompt still matches the user's goal
- For safety, clarity, and usability, state whether the revised prompt is better than, equal to, or worse than the original, with one sentence per dimension
- Do not repeat Phase 1 findings verbatim

### Phase 4: Verify and report

**Goal:** return a final review that is easy to use.

#### Steps

| Step | Action | Output |
| --- | --- | --- |
| 4.1 | Summarize the main issues | Review summary |
| 4.2 | Present the improved prompt | Revised prompt |
| 4.3 | List the most important changes | Improvement notes |

#### Tasks
- Keep the report direct
- Make the revised prompt reusable
- List the top 3-5 fixes, ranked by severity (safety issues first, then clarity, then style)

## Actions Summary

1. Analyze the prompt for safety and quality issues
2. Rewrite the prompt to reduce risk and improve clarity
3. Validate the revised prompt
4. Return the improved prompt and key notes
