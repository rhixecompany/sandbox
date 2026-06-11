---
description: "Transform this Python script into a polished, beginner-friendly project by refactoring the code, adding clear instructional comments, and generating a complete markdown tutorial."
agent: "agent"
---

## Goal

Transform this Python script into a polished, beginner-friendly project by refactoring the code, adding clear instructional comments, and generating a complete markdown tutorial.

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
Transform this Python script into a polished, beginner-friendly project by refactoring the code, adding clear instructional comments, and generating a complete markdown tutorial.

1. **Refactor the code**
   - Apply standard Python best practices
   - Ensure code follows the PEP 8 style guide
   - Rename unclear variables and functions if needed for clarity

1. **Add comments throughout the code**
   - Use a beginner-friendly, instructional tone
   - Explain what each part of the code is doing and why it's important
   - Focus on the logic and reasoning, not just syntax
   - Avoid redundant or superficial comments

1. **Generate a tutorial as a `README.md` file**  
   Include the following sections:
   - **Project Overview:** What the script does and why it's useful
   - **Setup Instructions:** Prerequisites, dependencies, and how to run the script
   - **How It Works:** A breakdown of the code logic based on the comments
   - **Example Usage:** A code snippet showing how to use it
   - **Sample Output:** (Optional) Include if the script returns visible results
   - Use clear, readable Markdown formatting
