---
agent: "agent"
description: "Create GitHub Pull Request for feature request from specification file using pull_request_template.md template."
tools:
  [
    "search/codebase",
    "search",
    "github",
    "create_pull_request",
    "update_pull_request",
    "get_pull_request_diff"
  ]
---

## Goal

Create GitHub Pull Request for feature request from specification file using pull_request_template.md template.

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
# Create GitHub Pull Request from Specification

Create GitHub Pull Request for the specification at `${workspaceFolder}/.github/pull_request_template.md` .

## Process

1. Analyze specification file template from '${workspaceFolder}/.github/pull_request_template.md' to extract requirements by 'search' tool.
2. Create pull request draft template by using 'create_pull_request' tool on to `${input:targetBranch}`. and make sure don't have any pull request of current branch was exist `get_pull_request`. If has continue to step 4, and skip step 3.
3. Get changes in pull request by using 'get_pull_request_diff' tool to analyze information that was changed in pull Request.
4. Update the pull request body and title created in the previous step using the 'update_pull_request' tool. Incorporate the information from the template obtained in the first step to update the body and title as needed.
5. Switch from draft to ready for review by using 'update_pull_request' tool. To update state of pull request.
6. Using 'get_me' to get username of person was created pull request and assign to `update_issue` tool. To assign pull request
7. Response URL Pull request was create to user.

## Requirements

- Single pull request for the complete specification
- Clear title/pull_request_template.md identifying the specification
- Fill enough information into pull_request_template.md
- Verify against existing pull requests before creation
