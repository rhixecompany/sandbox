---
title: Judge QA Rerun
description: Re-run skill judge on QA skills to verify quality
date: 2026-08-31
author: Hermes Agent
status: in_progress
profile: qa
model: default
---

# Judge QA Rerun

## Goal

Re-run skill judge on QA skills to verify quality scores remain high after changes.

## Context

This plan re-executes the skill judge on all QA skills to confirm they still pass the quality threshold (≥95).

## Risks

- Scores may drift if skills were modified
- Threshold changes may invalidate prior results

## Files to Create

- None

## Files to Modify

- judge_results/* (output reports)

## Phases

## Phase 1 — Inventory

Enumerate all QA skills to judge.

**Gate**: All QA skills enumerated

## Phase 2 — Execute

Run skill judge on each QA skill.

**Gate**: All skills judged

## Phase 3 — Verify

Confirm all scores ≥ threshold.

**Gate**: All pass

## Verification

- [ ] All QA skills judged
- [ ] All scores ≥ 95
- [ ] No regressions
