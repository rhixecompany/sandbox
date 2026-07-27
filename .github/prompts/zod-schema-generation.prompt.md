---
name: zod-schema-generation
title: Zod Schema Generation
description: Generate Zod validation schemas from TypeScript types, database schemas, or JSON samples
  with full type safety.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - file
  - terminal
scripts: []
skills:
  - prompt-engineering
formatter: default
plan: ''
dependencies:
  - skill:prompt-engineering
tags:
  - data
  - database
  - generator
  - prompts
  - sql
  - typescript
trigger: /zod-schema-generation
---

## GoalGenerate Zod validation schemas from TypeScript types, database schemas, or JSON samples.## DescriptionThis prompt produces Zod v3+ schemas with proper type inference, custom error messages, and best practices for schema composition.## Phases### Phase 1: Input AnalysisAnalyze the source type/schema/JSON structure.### Phase 2: Schema GenerationGenerate corresponding Zod schemas with refinements.### Phase 3: VerificationValidate the generated schemas compile and provide correct type inference.