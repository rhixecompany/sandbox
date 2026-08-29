---
name: all-repo-docker-setup
title: Bulk Docker Setup Across Repositories
description: Iterate over a list of rhixecompany repositories, generate or repair Dockerfiles, build images, run security scans, and clean up unused Docker resources with a tracked plan.
trigger: /all-repo-docker-setup
version: 1.0.0
author: Hermes Agent
tags: [docker, devops, automation, infrastructure, security, tooling]
metadata:
  hermes:
    profile: devops
    priority: medium
  copilot:
    model_required: sonnet
  opencode:
    enabled: true
  codex:
    enabled: true
toolsets:
  - file
  - terminal
skills:
  - skill:using-superpowers
dependencies: []
formatter: markdown
license: MIT
---
## Table of Contents

## Goal

## Context

## Phases


# Bulk Docker Setup Across Repositories

> Iterate over every rhixecompany repository, generate or repair Dockerfiles, build images, security-scan them, and clean up unused Docker resources.


Systematically process all repositories under `rhixecompany` to ensure each has a valid Dockerfile or `docker-compose.yml`, builds successfully, passes security scanning, and has a documented cleanup plan. Unused Docker resources are reclaimed with a tracked report.

## Prerequisites

- `gh` CLI authenticated and able to list `rhixecompany` repos
- Docker daemon running and accessible
- `trivy` installed for security scanning
- `docker` CLI with `docker compose` plugin
- Write access to `~/Desktop/SandBox/projects/`

## Inputs

- The list of repositories from `gh repo list rhixecompany --limit 100 --json name,url`
- Existing Docker artifacts in each repo (Dockerfile, docker-compose.yml)
- Docker images built during the process

## Outputs

- A valid Dockerfile or `docker-compose.yml` in each repository (created or repaired)
- All images built successfully
- Security scan report per repository (Trivy output)
- A cleanup report listing freed disk space

## Steps

### 1. List repositories

1. List all rhixecompany repositories:
   ```bash
   gh repo list rhixecompany --limit 100 --json name,url
   ```
2. Clone each repository to `~/Desktop/SandBox/projects/`:
   ```bash
   git clone <repository_url> ./projects/<repository_name>
   ```

### 2. Generate or repair Docker configuration

For each repository:
1. Check for existing `Dockerfile` or `docker-compose.yml`
2. If no Docker configuration exists, generate one based on the project's language (Node.js, Python, Go, Rust, etc.)
3. If a Dockerfile exists but is broken, debug, fix, and update it to a smaller base image
4. Build the image to verify it works:
   ```bash
   docker build -t <image_name> .
   ```
5. If only `docker-compose.yml` exists, build with:
   ```bash
   docker-compose build
   ```

### 3. Security scan

Run Trivy scan on each built image:
```bash
trivy image --severity HIGH,CRITICAL <image_name>
```

Record findings and fix critical vulnerabilities by updating base images or dependencies.

### 4. Cleanup

1. Remove unused containers:
   ```bash
   docker container prune -f
   ```
2. Remove unused images:
   ```bash
   docker image prune -a -f
   ```
3. Remove unused volumes:
   ```bash
   docker volume prune -f
   ```
4. Remove build caches:
   ```bash
   docker buildx builder prune -f
   ```
5. Report freed space:
   ```bash
   docker system df
   ```

## Rules

- **Scope discipline** — Only operate on rhixecompany repositories
- **Minimal changes** — Fix the smallest issue needed to build successfully
- **Track everything** — Log results to `docker_setup.log` in each repo root
- **No Docker config found** — Log "No Docker configuration found for this repository" to `docker_setup.log` if neither file exists

## Verification

- Each repository has either a `Dockerfile` or `docker-compose.yml`
- All images build without errors
- No HIGH/CRITICAL vulnerabilities remain (or documented rationale for exceptions)
- Cleanup report is saved

## Out of Scope

- Modifying application code beyond Docker-related config
- Production deployment orchestration
