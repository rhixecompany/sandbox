# All Repository Docker Setup and Cleanup

## Goal

For each repository in the rhixecompany organization, perform a complete Docker setup, security hardening, and cleanup workflow across all repos.

## Workflow

1. **Clone Repositories**
   - Clone each repository from `rhixecompany` into `./projects`
   - Use: `git clone <repository_url>`
   - Navigate into each cloned repository

2. **Dockerfile Management**
   - Check if a `Dockerfile` exists
   - If missing: create a minimal, secure Dockerfile
   - If present: debug, fix, and update to use a smaller base image
   - Build the image: `docker build -t <image_name> .`

3. **Docker Compose Fallback**
   - If no `Dockerfile` exists, check for `docker-compose.yml`
   - If present: build with `docker-compose build`
   - If neither exists: log to `docker_setup.log` in repo root

4. **Security Scanning**
   - Scan the Docker image for vulnerabilities
   - Document findings in a security report
   - Suggest and implement remediation steps

5. **Cleanup Plan**
   - Create a structured cleanup plan for each repository
   - Include: unused containers, images, volumes, build caches
   - Implement the cleanup plan
   - Report what was freed

6. **Error Resolution**
   - Fix all container errors encountered during build/run
   - Validate containers start successfully
   - Document fixes applied

## Execution Rules

- Work through repositories systematically
- Dry-run cleanup before executing
- Preserve all logs and reports in each repository
- Report blockers honestly; never fabricate results
- LF-only Markdown writes
