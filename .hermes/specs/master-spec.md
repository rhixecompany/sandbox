---
title: Master Spec — SandBox Plan Ecosystem
description: Master specification linking all 51 plan files for cross-validation
date: 2026-09-07
author: Alexa
status: in_progress
profile: default
model: inclusionai/ling-3.0-flash
---

## Goal

Master specification that couples all plan files in `.hermes/plans/` for cross-validation. Every plan references this spec, and this spec references every plan back.

## Linked Plans


## Acceptance Criteria

- All 51 plans have complete frontmatter (7 fields)
- All plans have >=3 Phase sections with **Gate** markers
- All plans reference this spec via `## Linked Specs`
- This spec references all plans via `## Linked Plan`
- All plans pass plans-judge score >=99
