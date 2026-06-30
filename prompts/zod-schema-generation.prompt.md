---
license: MIT
author: Hermes Agent
version: 1.0.0
name: "zod-schema-generation"
title: "Zod Schema Generation"
description: "Generate Zod validation schemas from TypeScript types, database schemas, or JSON samples with full type safety."
trigger: zod-schema-generation
tags:
  - data
  - database
  - generator
  - prompts
  - security
  - sql
  - typescript
  - hermes
  - zod
  - schema
  - validation
  - typescript
dependencies:
  - skill:prompt-engineering
skills:
  - prompt-engineering
metadata:
  hermes:
    related_skills: []
    tags:
    - zod-schema-generation.prompt

---


## Actions

- Follow the prompt workflow as specified.
- Produce the requested deliverable(s) in the exact structure requested.
- Validate output against acceptance criteria before finishing.
metadata:
  hermes:
    related_skills: []
    tags:
    - zod-schema-generation.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - zod-schema-generation.prompt

## Goal
Generate Zod validation schemas from TypeScript types, database schemas, or JSON samples.

## Description
This prompt produces Zod v3+ schemas with proper type inference, custom error messages, and best practices for schema composition.

## Phases
### Phase 1: Input Analysis
Analyze the source type/schema/JSON structure.
### Phase 2: Schema Generation
Generate corresponding Zod schemas with refinements.
### Phase 3: Verification
Validate the generated schemas compile and provide correct type inference.

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
