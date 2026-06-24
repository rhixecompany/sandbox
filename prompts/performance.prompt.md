---
name: "performance"
description: "Comprehensive performance prompt focused on measurable improvements and safe optimizations."
---

## Goal
Use when "Comprehensive performance prompt focused on measurable improvements and safe optimizations." to accomplish the associated tasks and objectives.


## Description

Improve application performance through measured, high-impact optimizations across data access, rendering, and caching paths.

## Context

Use this prompt when performance issues are suspected or when implementing features that can affect latency, throughput, bundle size, or query cost.

## Skills Required

- Performance profiling and bottleneck analysis
- Query and caching strategy optimization
- Frontend bundle and rendering optimization

## Subagents

| Subagent | Role | When to Use |
| --- | --- | --- |
| Performance Analyst | Identifies bottlenecks and baseline metrics | Always |
| Data Optimizer | Improves DB/query and pagination behavior | Data-heavy changes |
| Frontend Optimizer | Reduces client bundle and render cost | UI-heavy changes |

## Personas

- Performance Analyst: Requires evidence before recommending optimization.
- Data Optimizer: Prioritizes caching, pagination, and query efficiency.
- Frontend Optimizer: Minimizes JS shipped to clients and avoids unnecessary hydration.

## Rules

- Measure before optimizing and report baseline and delta when possible.
- Prioritize highest-impact bottlenecks first.
- Use pagination for large result sets.
- Prefer server-side execution where possible to reduce client bundle size.
- Avoid speculative micro-optimizations without evidence.

## Phases

> ### Phase 1: Baseline and Bottleneck Discovery
> ### Phase 2: Targeted Optimization

> **Full content:** `templates/performance/phases.md`

## Steps

1. Collect baseline metrics and identify hotspots.
2. Rank bottlenecks by user impact and frequency.
3. Implement minimal optimizations for top-ranked bottlenecks.
4. Re-measure and compare against baseline.
5. Document gains, limits, and next candidates.

## Tasks

- Task 1.1 — Establish baseline metrics for key paths.
- Task 1.2 — Identify and rank bottlenecks with evidence.
- Task 1.3 — Optimize queries, caching, rendering, or bundles where needed.
- Task 1.4 — Re-run measurements and verify non-regression.
- Task 1.5 — Record impact and future optimization backlog.

## Subtasks

- Subtask 1.1.1 — Capture latency, throughput, and resource usage indicators.
- Subtask 1.2.1 — Distinguish CPU, IO, and network constraints.
- Subtask 1.3.1 — Add pagination and caching for expensive read paths.
- Subtask 1.4.1 — Validate no change in correctness or security behavior.
- Subtask 1.5.1 — Summarize measurable wins and remaining bottlenecks.

## Actions Summary

1. Measure first.
2. Optimize the biggest bottlenecks only.
3. Re-measure and validate correctness.
4. Report measurable outcomes.


## Template References

Templates in `templates/performance/`:
- `phases.md`
