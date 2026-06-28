---
author: Hermes Agent
description: Use when creating optimized multi-stage Dockerfiles for any language
  or framework. Covers build optimization, security practices, and layer caching.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: multi-stage-dockerfile
tags:
- docker
- dockerfile
- multi-stage
- optimization
- containers
title: Multi-Stage Dockerfile
version: 1.0.0

---
# Multi-Stage Dockerfile

## Overview

Create optimized multi-stage Dockerfiles that produce smaller, more secure container images. Multi-stage builds separate build-time dependencies from runtime dependencies, resulting in leaner production images.

## When to Use

- Building Docker images for production deployment
- Optimizing image size (multi-stage can reduce size by 80%+)
- Separating build tools from runtime environment
- Creating reproducible build pipelines
- Implementing security scanning in the build process

## When NOT TO USE

- Simple single-file scripts that don't need compilation
- Development-only containers (use single-stage with all tools)
- When build time is more important than image size

## Skills Required

| Skill | Purpose |
|-------|---------|
| `docker-management` | Docker container management |

## Workflow

### Phase 1: Design Multi-Stage Structure

Plan your stages:
1. **Base/Dependencies** — Install system dependencies
2. **Builder** — Compile/build the application
3. **Test** — Run tests (optional, for CI)
4. **Runtime** — Minimal image with only what's needed to run

### Phase 2: Write the Dockerfile

**Node.js example:**
```dockerfile
# Stage 1: Dependencies
FROM node:20-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --only=production

# Stage 2: Builder
FROM node:20-alpine AS builder
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 3: Runtime
FROM node:20-alpine AS runtime
WORKDIR /app
RUN addgroup -g 1001 -S nodejs && adduser -S nextjs -u 1001
COPY --from=builder /app/dist ./dist
COPY --from=deps /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./
USER nextjs
EXPOSE 3000
CMD ["node", "dist/server.js"]
```

**Python example:**
```dockerfile
# Stage 1: Builder
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt
COPY . .
RUN python -m compileall .

# Stage 2: Runtime
FROM python:3.11-slim AS runtime
WORKDIR /app
RUN groupadd -r appuser && useradd -r -g appuser appuser
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app ./app
USER appuser
EXPOSE 8000
ENV PATH=/root/.local/bin:$PATH
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0"]
```

### Phase 3: Optimize

1. **Layer ordering:** Put rarely-changing layers first
2. **.dockerignore:** Exclude unnecessary files:
   ```
   node_modules
   .git
   .env
   *.md
   tests/
   ```
3. **Combine RUN commands:** Reduce layer count
4. **Use specific tags:** `python:3.11-slim` not `python:latest`

### Phase 4: Build & Verify

```bash
# Build the image
docker build -t myapp:latest .

# Check image size
docker images myapp:latest

# Run and test
docker run -p 3000:3000 myapp:latest

# Scan for vulnerabilities
docker scout cves myapp:latest
```

## Verification Checklist

- [ ] Multi-stage structure separates build from runtime
- [ ] Production image doesn't contain build tools
- [ ] .dockerignore excludes unnecessary files
- [ ] Non-root user configured for runtime
- [ ] Image size is reasonable (<200MB for most apps)
- [ ] No secrets in image layers
- [ ] Healthcheck configured if applicable

## Pitfalls

- **Copying everything:** Use specific `COPY` commands, not `COPY . .`
- **Running as root:** Always configure a non-root `USER` for production
- **Latest tags:** Pin base image versions for reproducibility
- **Secrets in build:** Use BuildKit secrets: `RUN --mount=type=secret,id=mysecret cat /run/secrets/mysecret`
- **Missing .dockerignore:** Without it, node_modules and .git get copied into the image
- **Not scanning vulnerabilities:** Run `docker scout cves` or Trivy on the final image
