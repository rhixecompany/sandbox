---
description: Create and verify Dockerfiles only — no build, no scan, no prune. Setup bun + uv. One repo at a time.
trigger: /all-repo-docker-setup
category: ci-cd
profile: alexa
personality: Direct, methodical, safety-conscious
model: nemotron-3-ultra-free (opencode-zen / openrouter)
---

# All Repository Dockerfile Create & Verify

For **each repository in the rhixecompany org** that has a local copy, perform a Docker setup pass: ensure a working `Dockerfile` exists (create it if missing), verify it is syntactically correct, and record the result. **Do NOT build images, run security scans, or prune Docker resources.**

Additionally, ensure **bun** and **uv** are installed and available in the environment.

## Goal

Standardize Dockerfiles across repositories without the cost of building images — create or verify Dockerfiles, validate syntax, and ensure the toolchain (bun + uv) is ready.

## Subgoals

1. **Dockerfile** — Create or verify a `Dockerfile` in every repo (prefer smaller images; multi-stage where possible).
2. **Verify** — Validate each Dockerfile syntax (e.g., `docker parse`, or manual review of `FROM`/`RUN`/`COPY`/`ENTRYPOINT` structure).
3. **Bun + UV Setup** — Ensure `bun` and `uv` are installed and available; install if missing.
4. **Report** — Log per-repo Dockerfile status and toolchain availability.

## Personas

- **DevOps Engineer** — Performs the clone/file-creation/verify workflow on every repo.
- **Toolchain Manager** — Ensures bun and uv are installed and working.
- **Reporter** — Produces the final status report (Dockerfile state per repo, bun/uv versions).

## Personality

- **Tone**: Direct, methodical, safety-conscious.
- **Style**: One repo at a time; record each result in `docker_setup.log`.
- **Avoid**: Building images, running scans on unverified images, silent failures, blanket prune commands.
- **Encourage**: Multi-stage builds, `.dockerignore`, minimal base images (e.g. `alpine`, `distroless`), bun+uv availability checks.

## Context

The source is `all-repo-docker-setup.prompt.txt` — an operational runbook for applying a standardized Dockerfile lifecycle across the org's repositories. This version is scoped to **create and verify only** — no image builds, no security scans, no resource pruning.

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)
> Domain-specific additions below.

### Domain Rules

1. **One repo at a time** — Check, create/verify, and report per repository before moving to the next.
2. **No builds** — Never run `docker build` or `docker-compose build`. Only create or verify Dockerfile contents.
3. **No scans** — Do not run `trivy`, `docker scout`, `grype`, or any image scanner.
4. **No prune** — Do not run `docker system prune` or any cleanup commands.
5. **Verify before creating** — Check if a `Dockerfile` already exists and is valid before creating a new one.
6. **Log everything** — Create/update `docker_setup.log` in the repo root with the exact status for each repo.
7. **DRY** — Reuse one logging and reporting format across all repos.
8. **Small images** — Prefer multi-stage builds and minimal base images (e.g. `alpine`, `distroless`); justify every change.
9. **Bun + UV required** — Before processing repos, verify `bun --version` and `uv --version` succeed. Install if missing.
10. **Never skip** — If a repo has neither `Dockerfile` nor `docker-compose.yml`, record that explicitly (do not silently skip).

## Steps

For each repo **in the list of repositories by rhixecompany** that has a local copy in `./projects`:

### 1. Navigate into the repo

```bash
cd ./projects/<repository_name>
```

### 2. Check Dockerfile presence

- **If `Dockerfile` exists** — verify its syntax:
  - Check `FROM` line is valid
  - Check `RUN`, `COPY`, `ENTRYPOINT`/`CMD` structure
  - Optionally run `docker build --dry-run .` if available (no actual build)
  - Log result
- **If `Dockerfile` does not exist** — create a minimal, correct `Dockerfile`:
  - Use a small base image (`alpine`, `distroless`, or language-specific slim variant)
  - Multi-stage where applicable
  - Include `.dockerignore` if helpful
  - Log as `created`

### 2. If no `Dockerfile` but `docker-compose.yml` exists

- Verify `docker-compose.yml` syntax (e.g., `docker compose config` dry-run)
- Log result
- Do NOT build

### 5. If neither exists

```bash
printf 'No Docker configuration found for this repository.\n' > docker_setup.log
```

### 3. Bun + UV Setup (run once before processing repos)

```bash
# Check bun
bun --version || echo "bun not found — install with: npm install -g bun"

# Check uv
uv --version || echo "uv not found — install with: curl -LsSf https://astral.sh/uv/install.sh | sh"
```

If either tool is missing, install it and re-verify.

### 7. Report

Per repo, record:

```
repo: <name>
dockerfile: <created|verified|missing|docker-compose-verified>
bun: <version or not-installed>
uv: <version or not-installed>
```

Then a global summary of Dockerfile status and toolchain availability.

## Verification

- Each repo has a recorded Dockerfile status (created, verified, missing, or docker-compose-verified).
- A `docker_setup.log` exists where required and states the exact message.
- Every new Dockerfile uses a small base image and is syntactically valid.
- `bun --version` and `uv --version` both succeed.
- No `docker build`, `docker-compose build`, `docker scan`, `trivy`, `grype`, or `docker system prune` commands were run.

## Output Format

Per repo:

```
repo: <name>
dockerfile: <created|verified|missing|docker-compose-verified>
bun: <version>
uv: <version>
```

Global summary: Dockerfile counts by status + bun/uv versions.

## MCP Servers & Tools

- **Terminal** — file inspection, bun/uv version checks, Dockerfile syntax verification.
- **File tools** — Dockerfile/docker-compose.yml inspection and creation.
- **GitHub MCP** — repo discovery and clone workflows (if needed).

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.

## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section
