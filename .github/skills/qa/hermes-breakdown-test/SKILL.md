---
name: hermes-breakdown-test
title: Hermes Breakdown Test
description: "Generate Test Strategy, test issues checklist, and QA plan from Feature artifacts based on ISTQB and ISO25010."
version: 1.0.0
author: Alexa
license: MIT
metadata:
  hermes:
    tags: [qa, testing, istqb, iso25010]
    related_skills: [hermes-breakdown-plan]
---

# Hermes: Breakdown Test

## Overview

Use when you need a comprehensive test strategy and QA plan for a feature or epic. Produces test-strategy.md, test-issues-checklist.md, and qa-plan.md.

## Inputs
- Feature PRD path (recommended)

## Outputs
- /docs/ways-of-work/plan/{epic}/{feature}/test-strategy.md
- /docs/ways-of-work/plan/{epic}/{feature}/test-issues-checklist.md
- /docs/ways-of-work/plan/{epic}/{feature}/qa-plan.md

## Usage
- delegate_task({"goal":"Create test strategy for feature X","context":"feature_prd=/docs/.../prd.md","toolsets":["file"]})

## Verification
- test-strategy.md includes ISTQB technique mapping and ISO25010 coverage matrix.


## When to Use


- you need a comprehensive test strategy and QA plan for a feature or epic
- **Triggers**: "hermes breakdown test" required for a project


