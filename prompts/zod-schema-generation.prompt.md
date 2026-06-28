---
license: MIT
author: Hermes Agent
version: 1.0.0
name: "zod-schema-generation"
title: "Zod Schema Generation"
description: "Generate Zod validation schemas from TypeScript types, database schemas, or JSON samples with full type safety."
trigger: /zod-schema-generation
tags:
  - hermes
  - zod
  - schema
  - validation
  - typescript
dependencies:
  - skill:prompt-engineering
skills:
  - prompt-engineering
---

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
