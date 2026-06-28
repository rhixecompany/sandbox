---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Microsoft 365 Declarative Agents Development Kit
name: declarative-agents
description: Complete development kit for Microsoft 365 Copilot declarative agents with three comprehensive workflows (basic, advanced, validation), TypeSpec support, and Microsoft 365 Agents Toolkit integration
tags: []
---

## Goal

Complete development kit for Microsoft 365 Copilot declarative agents with three comprehensive workflows (basic, advanced, validation), TypeSpec support, and Microsoft 365 Agents Toolkit integration.

## Context

Use when you need to declarative agents for the current workspace or task.

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

## Workflow 1: Basic Agent Creation

**Perfect for**: New developers, simple agents, quick prototypes

I'll guide you through:

1. **Agent Planning**: Define purpose, target users, and core capabilities
2. **Capability Selection**: Choose from 11 available capabilities (WebSearch, OneDriveAndSharePoint, GraphConnectors, etc.)
3. **Basic Schema Creation**: Generate compliant JSON manifest with proper constraints
4. **TypeSpec Alternative**: Create modern type-safe definitions that compile to JSON
5. **Testing Setup**: Configure Agents Playground for local testing
6. **Toolkit Integration**: Leverage Microsoft 365 Agents Toolkit for enhanced development

## Workflow 2: Advanced Enterprise Agent Design

**Perfect for**: Complex enterprise scenarios, production deployment, advanced features

I'll help you architect:

1. **Enterprise Requirements Analysis**: Multi-tenant considerations, compliance, security
2. **Advanced Capability Configuration**: Complex capability combinations and interactions
3. **Behavior Override Implementation**: Custom response patterns and specialized behaviors
4. **Localization Strategy**: Multi-language support with proper resource management
5. **Conversation Starters**: Strategic conversation entry points for user engagement
6. **Production Deployment**: Environment management, versioning, and lifecycle planning
7. **Monitoring & Analytics**: Implementation of tracking and performance optimization

## Workflow 3: Validation & Optimization

**Perfect for**: Existing agents, troubleshooting, performance optimization

I'll perform:

1. **Schema Compliance Validation**: Full v1.5 specification adherence checking
2. **Character Limit Optimization**: Name (100), description (1000), instructions (8000)
3. **Capability Audit**: Verify proper capability configuration and usage
4. **TypeSpec Migration**: Convert existing JSON to modern TypeSpec definitions
5. **Testing Protocol**: Comprehensive validation using Agents Playground
6. **Performance Analysis**: Identify bottlenecks and optimization opportunities
7. **Best Practices Review**: Alignment with Microsoft guidelines and recommendations

## Core Features Across All Workflows

> ### Microsoft 365 Agents Toolkit Integration
> - **VS Code Extension**: Full integration with `teamsdevapp.ms-teams-vscode-exte

> **Full content:** `templates/declarative-agents/core_features_across_all_workf.md`

## Template References

Detailed templates in `templates/declarative-agents/`:
- `core_features_across_all_workf.md`
