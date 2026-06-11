---
agent: "agent"
tools:
  [
    "githubRepo",
    "github",
    "get_me",
    "get_pull_request",
    "get_pull_request_comments",
    "get_pull_request_diff",
    "get_pull_request_files",
    "get_pull_request_reviews",
    "get_pull_request_status",
    "list_pull_requests",
    "request_copilot_review"
  ]
description: "List my pull requests in the current repository"
---

## Goal

List my pull requests in the current repository.

## Context

Use when you need to work on the current workspace or task.

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
Search the current repo (using #githubRepo for the repo info) and list any pull requests you find (using #list_pull_requests) that are assigned to me.

Describe the purpose and details of each pull request.

If a PR is waiting for someone to review, highlight that in the response.

If there were any check failures on the PR, describe them and suggest possible fixes.

If there was no review done by Copilot, offer to request one using #request_copilot_review.
