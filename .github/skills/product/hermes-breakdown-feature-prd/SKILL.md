---
name: hermes-breakdown-feature-prd
title: Hermes Breakdown Feature Prd
description: "Generate a Feature PRD (prd.md) from a feature idea or parent epic."
version: 1.0.0
author: Alexa
license: MIT
metadata:
  hermes:
    tags: [product, prd]
    related_skills: [hermes-breakdown-epic-pm]
---

# Hermes: Breakdown Feature PRD

## Overview

Use when you need a detailed Product Requirements Document for a specific feature. Produces prd.md including user stories, acceptance criteria, requirements, and dependencies.

## Inputs
- Parent epic or feature idea

## Outputs
- /docs/ways-of-work/plan/{epic-name}/{feature-name}/prd.md

## Usage
- delegate_task({"goal":"Write feature PRD for Quick Pay","context":"epic=/docs/.../epic.md\nidea=Enable one-click payments for saved cards","toolsets":["file"]})

## Verification
- prd.md has user stories and acceptance criteria.


## When to Use


- you need a detailed Product Requirements Document for a specific feature
- **Triggers**: "hermes breakdown feature prd" required for a project


