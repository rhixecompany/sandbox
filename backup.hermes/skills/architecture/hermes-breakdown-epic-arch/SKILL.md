---
name: hermes-breakdown-epic-arch
title: Hermes Breakdown Epic Arch
description: "Generate a high-level Epic Architecture Specification (arch.md) from an Epic PRD."
version: 1.0.0
author: Alexa
license: MIT
metadata:
  hermes:
    tags: [architecture, design, planning]
    related_skills: [hermes-breakdown-plan]
---

# Hermes: Breakdown Epic Architecture

## When to Use

- When working with hermes breakdown epic arch tools or services
- When automating or managing hermes breakdown epic arch tasks
- When troubleshooting hermes breakdown epic arch configurations
- **Triggers**: "Hermes Breakdown Epic Arch", "hermes breakdown epic arch" related operations

## Overview

Use when you need a concise, reproducible technical architecture specification for an Epic. Produces mermaid diagrams, component lists, enablers, and stack justification.

## Inputs
- /docs/ways-of-work/plan/{epic-name}/epic.md (required)
- Optional constraints or existing diagrams

## Outputs
- /docs/ways-of-work/plan/{epic-name}/arch.md

## Usage (delegate_task)

delegate_task({"goal":"Generate arch.md for payments epic","context":"epic=/docs/ways-of-work/plan/payments/epic.md\nconstraints=on-prem","toolsets":["file"]})

## Verification
- arch.md exists and includes a mermaid system diagram and enablers list.



