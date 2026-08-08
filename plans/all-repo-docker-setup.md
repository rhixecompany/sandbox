# All Repository Docker Setup — Implementation Plan

## Overview

This plan implements comprehensive Docker setup across all 29 repositories in `./projects`. The plan follows the phased approach defined in the prompt with verification gates at each phase.

---

## Phase 0: Inventory & Baseline

### Tasks

- [ ] Verify Docker and docker-compose availability
- [ ] Verify GitHub CLI authentication
- [ ] Record git submodule status baseline
- [ ] Discover all repos in `./projects` with `.git` directories
- [ ] For each repo: record current branch, dirty files, existing Docker configs
- [ ] Create baseline report: `docker_baseline_report.md`

### Deliverables

- `docker_baseline_report.md` — Per-repo snapshot before changes

### Verification

- [ ] Docker version output captured
- [ ] gh auth status shows active token with repo/workflow scopes
- [ ] All 29 repos listed with baseline data

---

## Phase 1: Technology Stack Analysis (Parallel)

### Tasks

- [ ] Load `technology-stack-blueprint-generator` skill
- [ ] For each repo (parallel, max 3 concurrent via `delegate_task` orchestrator):
  - Detect primary language/framework
  - Parse dependency files (package.json, requirements.txt, pyproject.toml, Cargo.toml, go.mod, pom.xml, build.gradle, etc.)
  - Identify build system, runtime, ports, env vars, health endpoints
  - Generate `TECHNOLOGY_STACK.md` (or update)
  - Generate `DOCKER_REQUIREMENTS.md` summarizing Dockerfile needs
- [ ] Aggregate summary: `TECHNOLOGY_STACK_SUMMARY.md`

### Deliverables

- Per-repo `TECHNOLOGY_STACK.md`
- Per-repo `DOCKER_REQUIREMENTS.md`
- Root `TECHNOLOGY_STACK_SUMMARY.md`

### Verification

- [ ] All 29 repos have TECHNOLOGY_STACK.md
- [ ] All 29 repos have DOCKER_REQUIREMENTS.md
- [ ] Summary table matches discovered repos

---

## Phase 2: Dockerfile Creation / Optimization

### Tasks

- [ ] Load `multi-stage-dockerfile`, `context-map` skills
- [ ] For each repo:
  - **If NO Dockerfile**: Generate multi-stage Dockerfile + docker-compose.yml + .dockerignore
  - **If Dockerfile EXISTS**: Run context-map, analyze, optimize per best practices
  - **If docker-compose.yml EXISTS**: Validate and optimize for dev/prod profiles
- [ ] Language-specific templates from `templates/all-repo-docker-setup/dockerfile-templates.md`
- [ ] Compose templates from `templates/all-repo-docker-setup/compose-templates.md`

### Deliverables

- Per-repo optimized `Dockerfile`
- Per-repo `docker-compose.yml`
- Per-repo `.dockerignore`

### Verification

- [ ] All 29 repos have Dockerfile
- [ ] All 29 repos have docker-compose.yml
- [ ] All 29 repos have .dockerignore
- [ ] All Dockerfiles use multi-stage pattern
- [ ] All Dockerfiles specify non-root USER
- [ ] All Dockerfiles include HEALTHCHECK
- [ ] All base images are slim/alpine/distroless variants

---

## Phase 3: Build & Test (Parallel)

### Tasks

- [ ] For each repo (parallel, max 3 concurrent):
  - `docker build -t <repo>:local .`
  - `docker run --rm -d --name <repo>-test -p <port>:<port> <repo>:local`
  - Wait for healthcheck (max 30s)
  - Verify application responds
  - `docker stop <repo>-test`
  - Record image size, build time, startup time

### Deliverables

- Build test results: `build_test_results.json`
- Per-repo metrics: image size, build time, startup time

### Verification

- [ ] All 29 images build successfully (exit code 0)
- [ ] All 29 containers start within 30s
- [ ] All 29 healthchecks pass
- [ ] All 29 applications respond on exposed port
- [ ] Image sizes recorded (target: <500MB, <200MB for simple services)

---

## Phase 4: Security Scan & Remediation

### Tasks

- [ ] Load `dependency-security-remediation` skill
- [ ] For each built image:
  - Run trivy/grype scan via Docker or MCP docker server
  - Parse HIGH/CRITICAL vulnerabilities
  - Apply remediation: update base images, pin deps, remove packages
  - Rebuild and re-scan until HIGH/CRITICAL = 0
- [ ] Generate security report: `security_scan_report.md`

### Deliverables

- Per-repo scan results
- Remediation actions taken
- Final clean scan reports

### Verification

- [ ] All 29 images scanned
- [ ] Zero HIGH/CRITICAL vulnerabilities remaining
- [ ] Remediation documented per repo

---

## Phase 5: Docker Cleanup Plan

### Tasks

- [ ] Per-repo cleanup: `docker system prune -f --volumes --filter "label=project=<repo>"`
- [ ] Per-repo builder prune: `docker builder prune -f --filter "label=project=<repo>"`
- [ ] Global cleanup:
  - `docker container prune -f`
  - `docker image prune -a -f --filter "until=24h"`
  - `docker volume prune -f`
  - `docker builder prune -a -f`
- [ ] Record space freed: `docker system df -v`
- [ ] Generate cleanup report: `docker_cleanup_report.md`

### Deliverables

- `docker_cleanup_report.md` with per-category space freed

### Verification

- [ ] Cleanup commands executed without error
- [ ] Space freed reported for containers, images, volumes, build cache
- [ ] Report generated

---

## Phase 6: Fix Container Errors (Systematic)

### Tasks

- [ ] Load `systematic-debugging` skill
- [ ] For each repo with failures (build or runtime):
  - **Understand**: Collect logs, errors, stack traces
  - **Hypothesize**: Form minimal hypotheses (one variable)
  - **Test**: Apply single change, rebuild, verify
  - **Fix**: Implement root cause fix
- [ ] Common patterns: port conflicts, permissions, missing deps, healthcheck failures, OOM, cache issues
- [ ] Document fixes: `container_fixes_log.md`

### Deliverables

- `container_fixes_log.md` — Per-repo error, hypothesis, fix, verification

### Verification

- [ ] All previously failing repos now pass build + runtime tests
- [ ] Root cause documented for each fix
- [ ] No symptom-only patches

---

## Phase 7: Git Commit & Push (Orchestrated)

### Tasks

- [ ] Load `git-multi-repo-orchestration` skill and plan
- [ ] Phase 1: Commit per repo to `development`
  - Conventional commits: `feat(docker): add multi-stage Dockerfile for <repo>`
  - Include Dockerfile, docker-compose.yml, .dockerignore, DOCKER_REQUIREMENTS.md
- [ ] Phase 2: Submodule sync (if applicable)
- [ ] Phase 3: Open PRs for review (review-then-merge)
- [ ] Phase 4: Sync `development` → `production` (FF-only)
- [ ] **User approval required before each batch commit/push**

### Deliverables

- Conventional commits on `development` branch per repo
- PRs opened for review
- Production branch synced

### Verification

- [ ] All repos committed with conventional messages
- [ ] Submodules clean (no `+` prefix)
- [ ] PRs review-then-merged (or open for review)
- [ ] Production synced to development
- [ ] Final sweep: 0 unexpected dirty repos

---

## Phase 8: Documentation & Final Verification

### Tasks

- [ ] Generate per-repo `DOCKER_SETUP_REPORT.md`
- [ ] Generate root `DOCKER_WORKSPACE_REPORT.md`
- [ ] Run final verification checklist (all 12 gates)
- [ ] Archive all artifacts

### Deliverables

- 29x `projects/<repo>/DOCKER_SETUP_REPORT.md`
- `DOCKER_WORKSPACE_REPORT.md`
- Final verification checklist (all ✅)

### Verification

- [ ] All 12 verification gates pass
- [ ] Reports complete and accurate
- [ ] User sign-off on completion

---

## Parallel Execution Strategy

| Phase   | Parallelism | Max Concurrent | Tool                         |
| ------- | ----------- | -------------- | ---------------------------- |
| Phase 1 | Repo-level  | 3              | `delegate_task` orchestrator |
| Phase 2 | Repo-level  | 3              | `delegate_task` orchestrator |
| Phase 3 | Repo-level  | 3              | `delegate_task` orchestrator |
| Phase 4 | Repo-level  | 3              | `delegate_task` orchestrator |
| Phase 6 | Repo-level  | 3              | `delegate_task` orchestrator |

---

## Risk Mitigation

| Risk                          | Mitigation                                   |
| ----------------------------- | -------------------------------------------- |
| Docker daemon unavailable     | Pre-check in Phase 0; error with remediation |
| Build failures                | Systematic debugging (Phase 6); single retry |
| Security scan false positives | Manual review before remediation             |
| Git push conflicts            | Fetch/rebase; approval for force-push        |
| Subagent timeouts             | Increase timeout; reduce batch size          |
| Partial completion            | Entry checks (artifact files) enable resume  |

---

## Success Criteria

- [ ] All 29 repos have working Dockerfile + docker-compose.yml
- [ ] All images build, run, pass healthchecks
- [ ] Zero HIGH/CRITICAL vulnerabilities
- [ ] Cleanup executed, space reported
- [ ] All changes committed to `development` with conventional commits
- [ ] Comprehensive documentation generated
- [ ] User approval obtained for all git operations
