# Bash — Architecture Overview

## Overview
Automation toolkit for workspace management, written in TypeScript and running on Bun. Provides orchestration, cleanup, and migration scripts for the SandBox monorepo.

## Key Components
- **src/core/** — Core orchestration logic (AST transformers, workflow engines)
- **scripts/** — Utility scripts for various automation tasks
- **docs/** — Reference documentation for orchestration patterns

## Technology
- Runtime: Bun 1.3.14+
- Language: TypeScript
- Key deps: yaml, zod for config parsing and validation

Last updated: 2026-06-28
