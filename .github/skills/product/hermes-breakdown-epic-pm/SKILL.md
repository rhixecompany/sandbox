---
name: hermes-breakdown-epic-pm
title: Hermes Breakdown Epic Pm
description: "Generate a complete Epic PRD (epic.md) from a high-level idea or feature request."
version: 1.0.0
author: Alexa
license: MIT
metadata:
  hermes:
    tags: [product, prd, planning]
    related_skills: [hermes-breakdown-plan]
---

# Hermes: Breakdown Epic PRD

## Overview

Use when you need a detailed Epic-level Product Requirements Document. Produces epic.md with Goal, Personas, Journeys, Requirements, Metrics, and Out-of-Scope.

## Inputs
- Epic idea text or path to a short descriptor

## Outputs
- /docs/ways-of-work/plan/{epic-name}/epic.md

## Usage
- delegate_task({"goal":"Draft Epic PRD for 'Merchant Onboarding'","context":"Idea: allow merchants to connect bank accounts via Plaid","toolsets":["file"]})

## Verification
- epic.md exists and contains required sections.


## When to Use


- you need a detailed Epic-level Product Requirements Document
- **Triggers**: "hermes breakdown epic pm" required for a project


