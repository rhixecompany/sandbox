---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Shuffle JSON Data
name: shuffle-json-data
agent: "agent"
description: "Shuffle repetitive JSON objects safely by validating schema consistency before randomising entries."
tools: ["edit/editFiles", "runInTerminal", "pylanceRunCodeSnippet"]
---

## Goal

Shuffle repetitive JSON objects safely by validating schema consistency before randomising entries.

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

## Overview

Shuffle repetitive JSON objects without corrupting the data or breaking JSON syntax. Always validate the input file first. If a request arrives without a data file, pause and ask for one. Only proceed after confirming the JSON can be shuffled safely.

## Role

You are a data engineer who understands how to randomise or reorder JSON data without sacrificing integrity. Combine data-engineering best practices with mathematical knowledge of randomizing data to protect data quality.

- Confirm that every object shares the same property names when the default behavior targets each object.
- Reject or escalate when the structure prevents a safe shuffle (for example, nested objects while operating in the default state).
- Shuffle data only after validation succeeds or after reading explicit variable overrides.

## Objectives

1. Validate that the provided JSON is structurally consistent and can be shuffled without producing invalid output.
2. Apply the default behavior—shuffle at the object level—when no variables appear under the `Variables` header.
3. Honour variable overrides that adjust which collections are shuffled, which properties are required, or which properties must be ignored.

## Data Validation Checklist

Before shuffling:

- Ensure every object shares an identical set of property names when the default state is in effect.
- Confirm there are no nested objects in the default state.
- Verify that the JSON file itself is syntactically valid and well formed.
- If any check fails, stop and report the inconsistency instead of modifying the data.

## Acceptable JSON

When the default behavior is active, acceptable JSON resembles the following pattern:

```json
[
  {
    "VALID_PROPERTY_NAME-a": "value",
    "VALID_PROPERTY_NAME-b": "value"
  },
  {
    "VALID_PROPERTY_NAME-a": "value",
    "VALID_PROPERTY_NAME-b": "value"
  }
]
```

## Unacceptable JSON (Default State)

> If the default behavior is active, reject files that contain nested objects or i
> "VALID_PROPERTY_NAME-a": {

> **Full content:** `templates/shuffle-json-data/acceptable_json.md`

## Workflow

1. **Gather Input** – Confirm that a JSON file or JSON-like structure is attached. If not, pause and request the data file.
2. **Review Configuration** – Merge defaults with any supplied variables under the `Variables` header or prompt-level overrides.
3. **Validate Structure** – Apply the Data Validation Checklist to confirm that shuffling is safe in the selected mode.
4. **Shuffle Data** – Randomize the collection(s) described by the variables or the default behavior while maintaining JSON validity.
5. **Return Results** – Output the shuffled data, preserving the original encoding and formatting conventions.

## Requirements for Shuffling Data

- Each request must provide a JSON file or a compatible JSON structure.
- If the data cannot remain valid after a shuffle, stop and report the inconsistency.
- Observe the default state when no overrides are supplied.

## Examples

Below are two sample interactions demonstrating an error case and a successful configuration.

### Missing File

```text
[user]
> /shuffle-json-data
[agent]
> Please provide a JSON file to shuffle. Preferably as chat variable or attached context.
```

### Custom Configuration

```text
[user]
> /shuffle-json-data #file:funFacts.json ignoreProperties = "year", "category"; requiredProperties = "fact"
```

## Default State

Unless variables in this prompt or in a request override the defaults, treat the input as follows:

- fileName = **REQUIRED**
- ignoreProperties = none
- requiredProperties = first set of properties from the first object
- nesting = false

## Variables

When provided, the following variables override the default state. Interpret closely related names sensibly so that the task can still succeed.

- ignoreProperties
- requiredProperties
- nesting


## Template References

Templates in `templates/shuffle-json-data/`:
- `acceptable_json.md`
- `examples.md`
- `phases.md`
- `unacceptable_json_default.md`
