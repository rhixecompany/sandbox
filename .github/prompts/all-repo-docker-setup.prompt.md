---
name: all-repo-docker-setup
title: All Repository Docker Setup and Cleanup
description: For each repository in the rhixecompany org, clone to ./projects, build
  or update Dockerfiles/images, run security scans, create cleanup plans, fix container
  errors, and clean up unused Docker resources.
version: 1.1.0
license: MIT
author: Hermes Agent
tags:
- debugging
- docker
- fix
- frontend
- ml
- performance
- prompts
- security
- typescript
toolsets: null
trigger: /all-repo-docker-setup
skills: null
dependencies:
- skill:docker-management
- skill:disk-space-cleanup
metadata:
  hermes:
    source: all-repo-docker-setup.prompt.txt
    converted: '2026-08-08'
scripts: []
formatter: default
plan: ''
---

## Goal

For **each repository in the rhixecompany org**, perform a complete Docker setup pass: clone the repo, ensure a working `Dockerfile` (create it if missing), build the image, run a security scan, suggest and implement a cleanup plan, fix all container errors, and finish by cleaning up unused Docker resources and reporting what was freed.

## Subgoals

1. **Clone** — Clone every rhixecompany repository into `./projects`.
2. **Dockerfile** — Create, debug, fix, or optimize a `Dockerfile` in every repo (prefer smaller images).
3. **Build** — Build the Docker image successfully (`docker build` or `docker-compose build`).
4. **Secure** — Security-scan images and fix/flag findings.
5. **Cleanup plan** — Suggest, create, and implement a cleanup plan for container errors and bloat.
6. **Prune** — Remove unused containers, images, volumes, and build caches.
7. **Report** — Log per-repo status and summarize what was freed.

## Personas

- **DevOps Engineer** — Performs the clone/build/scan/prune workflow on every repo.
- **Security Reviewer** — Validates scan results and flags unresolved findings.
- **Reporter** — Produces the final cleanup report (what was freed, image sizes, remaining risks).

## Personality

- **Tone**: Direct, methodical, safety-conscious.
- **Style**: One repo at a time; record each result in `docker_setup.log`.
- **Avoid**: Skipping repos, running scans on unverified images, silent failures.
- **Encourage**: Distroless/multi-stage builds, `.dockerignore`, `docker scout`/`trivy` scans, pruning only after verification.

## Context

The source is `all-repo-docker-setup.prompt.txt` — an operational runbook for applying a standardized Docker lifecycle across the org's repositories. It is authoritative for the work items and reporting format.

## Rules


> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)
> Domain-specific additions below.

### Domain Rules

1. **One repo at a time** — Clone, build, scan, and report per repository before moving to the next.
2. **Verify before destructive ops** — Never `docker system prune -a` without confirming the image list first.
3. **Log everything** — Create/update `docker_setup.log` in the repo root with the exact message for repos with no Docker config.
4. **DRY** — Reuse one logging and reporting format across all repos.
5. **Small images** — Prefer multi-stage builds and minimal base images (e.g. `alpine`, `distroless`); justify every change.
6. **Never skip** — If a repo has neither `Dockerfile` nor `docker-compose.yml`, record that explicitly (do not silently skip).

## Steps

For each repo **in the list of repositories by rhixecompany**:

1. Clone the repository to `./projects`:

   ```bash
   git clone <repository_url> ./projects/<repository_name>
   ```

2. Navigate into the cloned repository:

   ```bash
   cd ./projects/<repository_name>
   ```

3. Check if a `Dockerfile` exists:
   - **If it does not exist** — create a minimal, correct `Dockerfile` (multi-stage where possible; set a small base image).
   - **If it does exist** — debug and fix it, update it to a smaller image where safe, then build:

     ```bash
     docker build -t <image_name> .
     ```

4. If no `Dockerfile` exists but `docker-compose.yml` does, build with:

   ```bash
   docker-compose build
   ```

5. If neither `Dockerfile` nor `docker-compose.yml` exists, log the exact message and create the log file in the repo root:

   ```bash
   printf 'No Docker configuration found for this repository.\n' > docker_setup.log
   ```

6. Security scan the built image (e.g. `trivy image`, `docker scout cves`, `grype`) and implement or suggest fixes for High/Critical findings.
7. Suggest, create, and implement a cleanup plan for the repo's Docker assets (`.dockerignore`, removal of junk blobs, multi-stage consolidation, unused deps).
8. Fix all container errors found during build/run verification.
9. Clean up unused Docker resources with a **specific plan** (no blanket `prune -a` without review):
   - Remove unused containers
   - Remove unused images
   - Remove unused volumes
   - Remove unused build caches
   - Report what was freed

## Verification

- Each repo has a working, successful `docker build` (or a recorded reason why not).
- A `docker_setup.log` exists where required and states the exact message.
- Every small-image/multistage change is justified and the image runs.
- Final cleanup report lists containers/images/volumes/build cache removed and total bytes freed.
- No `docker` errors remaining in the cloned repos.

## Output Format

Per repo, report:

```
repo: <name>
dockerfile: <created|fixed|optimized|missing>
image: <name>:<tag>
security: <scanner> — <high> high / <crit> critical
cleanup: <items removed>
```

Then a global summary of all `docker system prune` results.

## MCP Servers & Tools

- **Docker MCP** — container/image/compose management across repos.
- **Terminal** — docker CLI builds, scans, and logs.
- **File tools** — Dockerfile/docker-compose.yml inspection and patches.
- **GitHub MCP** — repo discovery and clone workflows.


## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.


## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section
