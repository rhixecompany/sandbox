---
name: "playwright-automation-fill-in-form.prompt"
title: "Playwright Form Fill Automation"
description: "Fill a form with Playwright MCP, stop before submission, and ask for a human review."
author: "Alexa"
created: "2026-05-25T10:50:21.952313Z"
compatibility: ["hermes", "copilot", "opencode"]
tags: ["playwright-automation-fill-in-form", "banking", "prompt"]
mcp_generator: null
skill_stub: true
---

## Goal

Fill a form with Playwright MCP, stop before submission, and ask for a human review.

## Context

Use when you need to playwright form fill automation for the current workspace or task.

## Inputs

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs

- A complete result that matches the prompt's purpose.
- A concise verification note when the task benefits from one.

## Rules

- Follow the prompt literally and prefer evidence from the current workspace.
- Keep the response structured, deterministic, and easy to act on.
- Avoid changing unrelated files or adding unnecessary scope.
- If something is unclear, state the assumption instead of guessing.

## Phases

### Phase 1: Intake
- Read the request and identify the exact scope.
- Locate the relevant files, diffs, or references.

### Phase 2: Execute
- Perform the requested work with the smallest safe change set.
- Keep the steps explicit and reproducible.

### Phase 3: Verify
- Check the result against the goal, rules, and inputs.
- Confirm the output is usable and complete.

### Phase 4: Hand off
- Return the final artifact or findings clearly.
- Stop once the requested result is delivered.

## Legacy Prompt Details
```text
## Description

Fill a form with Playwright MCP, stop before submission, and ask for a human review.

## Context

- Use the provided form URL and the provided field values.
- If a required value or file path is missing, ask for clarification before continuing.
- Never submit the form without explicit user approval.

## Skills Required

- `webapp-testing` — use browser automation to interact with the live form
- `systematic-debugging` — resolve selector and filling issues methodically
- `verification-before-completion` — confirm the form is ready for review before stopping

## Subagents

| Subagent | Role | Phase |
| --- | --- | --- |
| `@browser` | Performs the form interaction steps | Phase 2 |
| `@checker` | Confirms the filled state and captures issues | Phase 3 |

## Personas

### @browser
A careful browser operator who fills the form field by field.

### @checker
A reviewer who verifies the form is ready but not submitted.

## Rules

1. Navigate to the provided form URL first.
2. Fill each field exactly as requested.
3. Upload the provided image path only if it exists locally.
4. Do not submit the form.
5. Ask for a review before any submission step.
6. If a field cannot be found, stop and report the blocker.

## Phases

### Phase 1: Intake
**Goal:** confirm the form details before touching the page.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 1.1 | Read the requested URL and values | Input summary |
| 1.2 | Confirm any missing values or file paths | Clarification list |
| 1.3 | Decide whether the upload path is valid | Ready/not-ready status |

#### Tasks
- Validate the form inputs.
- Identify any missing detail early.
- Avoid guessing on ambiguous fields.

### Phase 2: Fill the form
**Goal:** enter the data into the form without submitting it.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 2.1 | Open the form URL | Loaded form |
| 2.2 | Fill each field in order | Completed inputs |
| 2.3 | Upload the image if valid | Uploaded attachment |

#### Tasks
- Enter the values exactly as provided.
- Keep the browser on the form page.
- Do not click submit.

### Phase 3: Verify state
**Goal:** confirm the form is ready for human review.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 3.1 | Re-check filled fields | Verification notes |
| 3.2 | Verify the upload state | Attachment status |
| 3.3 | Pause before submission | Review-ready state |

#### Tasks
- Confirm the form is filled correctly.
- Highlight any remaining issue.
- Stop before any submission action.

### Phase 4: Hand off
**Goal:** ask for review and wait for direction.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 4.1 | Summarize what was completed | Handoff note |
| 4.2 | State that the form was not submitted | Safety confirmation |
| 4.3 | Ask for review or next step | User response |

#### Tasks
- Report the filled fields.
- Confirm submission did not happen.
- Ask for approval before any further action.

## Steps

- Confirm input values.
- Open the form.
- Fill all fields carefully.
- Stop and request review.

## Tasks

- Validate inputs.
- Fill the form fields.
- Upload the image if valid.
- Pause before submit.

## Subtasks

- Check the URL.
- Verify each field label.
- Confirm the upload path exists.
- Report the ready-to-review state.

## Actions Summary

1. Open the form URL.
2. Fill the requested fields.
3. Upload the image if available.
4. Stop before submission.

```
