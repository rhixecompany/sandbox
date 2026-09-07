---
title: Docker Cleanup Plan
description: "Plan for cleaning up all unused Docker resources and AI agents"
date: 2026-09-07
author: Alexa
status: in_progress
profile: default
model: nemotron-3-ultra-free (opencode-zen)
---

# Docker Cleanup Plan

## Goal
Delete all unused Docker images, builds, containers, volumes, models, and MCP toolkit.

## Phase A: Inventory
### Tasks
- A1: Run `docker system df` to inventory all resources
- A2: List all Docker containers, images, volumes, networks
- A3: Identify AI agent containers and their status
- A4: Identify unused MCP toolkit resources

**Gate**: Complete inventory captured.

## Phase B: Cleanup
### Tasks
- B1: Remove all unused images (`docker image prune --all`)
- B2: Remove all stopped containers (`docker container prune`)
- B3: Remove all unused volumes (`docker volume prune`)
- B4: Remove build cache (`docker builder prune --all`)
- B5: Remove unused AI agent containers

**Gate**: All unused resources removed.

## Phase C: Verification
### Tasks
- C1: Verify disk space freed
- C2: Verify active resources unaffected
- C3: Update documentation

**Gate**: Verification complete.

## Linked Specs
- ../specs/hermes-ecosystem-reliability-spec.md
- ../specs/comprehensive-implementation-spec.md
