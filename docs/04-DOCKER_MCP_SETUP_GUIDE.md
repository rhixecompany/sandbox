# Docker MCP Server Setup & Configuration Guide

**Document Type:** Docker & MCP Integration Guide  
**Version:** 1.0  
**Created:** May 25, 2026  
**Purpose:** Complete setup for Docker MCP servers in Hermes Agent

---

## Table of Contents

1. [Docker MCP Overview](#docker-mcp-overview)
2. [Architecture](#architecture)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Available Tools](#available-tools)
6. [Usage Examples](#usage-examples)
7. [Troubleshooting](#troubleshooting)

---

## Docker MCP Overview

### What is Docker MCP?

Docker MCP (Model Context Protocol) Server provides AI agents with safe, controlled access to Docker operations through a standardized interface.

**Features:**
- 40+ Docker management tools
- Container lifecycle management
- Image building and pulling
- Compose orchestration
- Database operations (PostgreSQL, MySQL, MongoDB)
- Volume and network management
- Real-time logging and stats

**Benefits:**
- Agents can orchestrate containers
- Safe, permission-scoped access
- No need for direct Docker socket exposure
- Production-ready security model

### Two Docker MCP Servers

#### 1. Standard Docker MCP Server

```
🏗️ Basic Docker operations
├─ Container management
├─ Image management
├─ Volume management
├─ Network management
└─ Compose support
```

**Type:** stdio  
**Status:** ✓ Available  
**Tools:** 30+

#### 2. Docker MCP Gateway (adminbot profile)

```
🔐 Advanced admin features
├─ Container composition
├─ Health monitoring
├─ Database backups
├─ Advanced networking
└─ Resource optimization
```

**Type:** stdio  
**Status:** ⚠ Windows-specific (requires WSL2)  
**Tools:** 40+

---

## Architecture

### Communication Flow

```
┌──────────────────────┐
│   Hermes Agent       │
│  (Tool Caller)       │
└──────────┬───────────┘
           │
      ┌────▼─────────┐
      │  MCP Client  │
      └────┬─────────┘
           │
     ┌─────▼─────────────────┐
     │   JSON-RPC 2.0        │
     │   (stdio/HTTP)        │
     └─────┬─────────────────┘
           │
     ┌─────▼──────────────────┐
     │ Docker MCP Server      │
     └─────┬──────────────────┘
           │
     ┌─────▼──────────────────┐
     │  Docker Daemon Socket  │
     │  /var/run/docker.sock  │
     └─────┬──────────────────┘
           │
     ┌─────▼──────────────────┐
     │  Docker Infrastructure │
     │  - Containers          │
     │  - Images              │
     │  - Volumes             │
     │  - Networks            │
     └────────────────────────┘
```

### Transport Mechanism

1. **Hermes** sends tool call via JSON-RPC
2. **MCP Server** validates and translates to Docker API
3. **Docker** executes operation
4. **MCP Server** formats response back through JSON-RPC
5. **Hermes** receives result and acts on it

---

## Installation

### Prerequisites

```bash
# Docker or Podman installed
docker --version
# Expected: Docker version 24.0+

# Hermes installed
hermes --version
# Expected: Hermes Agent v0.14.0+

# Bun package manager (optional, for custom servers)
bun --version
```

### Install Docker (if not present)

**macOS:**
```bash
brew install docker
# Or: Download Docker Desktop
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install docker.io
sudo usermod -aG docker $USER
```

**Windows (WSL2):**
```powershell
# Enable WSL2
wsl --install

# In WSL2:
sudo apt update
sudo apt install docker.io
```

### Install Docker MCP Server

**Option 1: Via npm (Recommended)**

```bash
npm install -g @modelcontextprotocol/server-docker
```

**Option 2: From source**

```bash
git clone https://github.com/modelcontextprotocol/servers
cd servers/src/docker
npm install
npm run build
```

**Option 3: Via Docker image**

```bash
docker pull nousresearch/docker-mcp:latest
```

### Verify Installation

```bash
hermes mcp list | grep docker
```

Expected output:
```
✓ docker              stdio   - Docker management (40+ tools)
✓ docker-adminbot     stdio   - Docker admin features
```

---

## Configuration

### Global Configuration

**Location:** `~/.hermes/config.yaml`

```yaml
mcp_servers:
  docker:
    type: "stdio"
    command: "docker"
    enabled: true
    env:
      DOCKER_BINARY: "/usr/bin/docker"
      DOCKER_HOST: "unix:///var/run/docker.sock"
```

### Environment Variables

```bash
# Docker binary path
HERMES_MCP_DOCKER_BINARY=/usr/bin/docker
# Or for Podman
HERMES_MCP_DOCKER_BINARY=/usr/bin/podman

# Docker socket path
DOCKER_HOST=unix:///var/run/docker.sock

# For remote Docker
DOCKER_HOST=tcp://192.168.1.100:2375

# Docker credentials (for private registries)
DOCKER_USERNAME=your_username
DOCKER_PASSWORD=your_password
```

### CLI Configuration

```bash
# Enable Docker MCP
hermes config set mcp_servers.docker.enabled true

# Set Docker binary
hermes config set terminal.docker.binary /usr/bin/docker

# Set Docker image
hermes config set terminal.docker.image nikolaik/python-nodejs:python3.11-nodejs20
```

### For SSH Backend

When using SSH remote execution:

```yaml
# ~/.hermes/config.yaml
terminal:
  backend: "ssh"
  ssh:
    host: "192.168.1.100"
    user: "agent"
    key: "~/.ssh/id_rsa"

mcp_servers:
  docker:
    type: "stdio"
    env:
      DOCKER_HOST: "unix:///var/run/docker.sock"
```

---

## Available Tools

### Container Management (8 tools)

| Tool | Purpose |
|------|---------|
| `docker_container_list` | List all containers |
| `docker_container_start` | Start a stopped container |
| `docker_container_stop` | Stop a running container |
| `docker_container_restart` | Restart a container |
| `docker_container_remove` | Remove a container |
| `docker_container_logs` | View container logs |
| `docker_container_stats` | Get resource usage |
| `docker_container_exec` | Execute command inside container |

### Image Management (5 tools)

| Tool | Purpose |
|------|---------|
| `docker_image_list` | List all images |
| `docker_image_build` | Build image from Dockerfile |
| `docker_image_pull` | Pull from registry |
| `docker_image_push` | Push to registry |
| `docker_image_remove` | Remove image |

### Volume Management (4 tools)

| Tool | Purpose |
|------|---------|
| `docker_volume_list` | List all volumes |
| `docker_volume_create` | Create volume |
| `docker_volume_remove` | Remove volume |
| `docker_volume_inspect` | Get volume details |

### Network Management (4 tools)

| Tool | Purpose |
|------|---------|
| `docker_network_list` | List all networks |
| `docker_network_create` | Create network |
| `docker_network_remove` | Remove network |
| `docker_network_inspect` | Get network details |

### Docker Compose (4 tools)

| Tool | Purpose |
|------|---------|
| `docker_compose_up` | Start services |
| `docker_compose_down` | Stop services |
| `docker_compose_ps` | List services |
| `docker_compose_logs` | View service logs |

### Database Operations (5+ tools)

| Tool | Purpose |
|------|---------|
| `docker_db_query` | Execute SQL query |
| `docker_db_backup` | Create database backup |
| `docker_db_restore` | Restore from backup |
| `docker_db_status` | Get database status |
| `docker_db_export` | Export database data |

### Resource & Health (4 tools)

| Tool | Purpose |
|------|---------|
| `docker_container_healthcheck` | Check container health |
| `docker_resource_usage` | Get system resource usage |
| `docker_cleanup` | Remove unused resources |
| `docker_prune` | Clean up dangling images/volumes |

---

## Usage Examples

### List All Containers

```bash
hermes chat "List all Docker containers and show their status"
```

**Behind the scenes:**
```json
{
  "tool": "docker_container_list",
  "args": {}
}
```

**Returns:**
```
✓ web-app (RUNNING)
✓ database-prod (RUNNING)
✓ cache-layer (EXITED)
└ 3 containers total
```

### Start a Container

```bash
hermes chat "Start the 'database-prod' container"
```

**Behind the scenes:**
```json
{
  "tool": "docker_container_start",
  "args": {"container_id": "database-prod"}
}
```

### View Logs

```bash
hermes chat "Show the last 50 lines of logs from the 'web-app' container"
```

**Behind the scenes:**
```json
{
  "tool": "docker_container_logs",
  "args": {
    "container_id": "web-app",
    "tail": 50,
    "follow": false
  }
}
```

### Execute Command Inside Container

```bash
hermes chat "Run 'npm list' inside the web-app container"
```

**Behind the scenes:**
```json
{
  "tool": "docker_container_exec",
  "args": {
    "container_id": "web-app",
    "command": "npm list"
  }
}
```

### Build Image

```bash
hermes chat "Build a Docker image from the Dockerfile in current directory, tag it as 'myapp:latest'"
```

**Behind the scenes:**
```json
{
  "tool": "docker_image_build",
  "args": {
    "dockerfile": "Dockerfile",
    "tag": "myapp:latest",
    "context": "."
  }
}
```

### Database Backup

```bash
hermes chat "Create a backup of the PostgreSQL database in the 'postgres-prod' container"
```

**Behind the scenes:**
```json
{
  "tool": "docker_db_backup",
  "args": {
    "container_id": "postgres-prod",
    "database": "production",
    "format": "sql"
  }
}
```

### Docker Compose Operations

```bash
hermes chat "Start all services defined in docker-compose.yml"
```

**Behind the scenes:**
```json
{
  "tool": "docker_compose_up",
  "args": {
    "detach": true,
    "build": false
  }
}
```

---

## Advanced Configuration

### Multi-Host Docker

```yaml
# ~/.hermes/config.yaml
mcp_servers:
  docker-local:
    type: "stdio"
    command: "docker"
    env:
      DOCKER_HOST: "unix:///var/run/docker.sock"
  
  docker-prod:
    type: "stdio"
    command: "docker"
    env:
      DOCKER_HOST: "tcp://prod.example.com:2375"
```

**Usage:**
```bash
hermes chat "List containers on prod: docker list prod-prod-docker"
```

### Podman Integration

```bash
# Set Podman as backend
hermes config set mcp_servers.docker.env.DOCKER_BINARY /usr/bin/podman

# Verify
hermes chat "List containers"
```

### Docker Registry Authentication

```bash
# For private registries
export DOCKER_USERNAME=myuser
export DOCKER_PASSWORD=mypass

hermes chat "Pull image from private registry"
```

---

## Troubleshooting

### Issue: "docker: command not found"

**Solution:**
```bash
# Install Docker
brew install docker          # macOS
sudo apt install docker.io   # Linux

# Or specify path
hermes config set terminal.docker.binary /usr/local/bin/docker
```

### Issue: "Permission denied while trying to connect to Docker daemon"

**Solution:**
```bash
# Add user to docker group (Linux)
sudo usermod -aG docker $USER
newgrp docker

# Or run with sudo
sudo hermes chat "List containers"
```

### Issue: "Cannot connect to Docker daemon"

**Solution:**
```bash
# Check if Docker is running
docker ps

# Start Docker
docker daemon     # Linux
open -a Docker    # macOS

# Check socket path
ls -la /var/run/docker.sock
```

### Issue: "MCP server not responding"

**Solution:**
```bash
# Restart MCP
hermes mcp restart

# Check status
hermes mcp list

# View logs
tail -f ~/.hermes/hermes.log | grep docker
```

### Issue: "Out of disk space"

**Solution:**
```bash
# Clean up unused resources
hermes chat "Clean up Docker: remove unused images, containers, and volumes"

# Or manually
docker system prune -a
docker volume prune
```

---

## Security Considerations

### ✅ Best Practices

- Run Docker MCP in isolated environment
- Use SSH backend for remote Docker
- Implement rate limiting on operations
- Enable audit logging
- Restrict container access via AppArmor/SELinux
- Use read-only filesystems where possible
- Validate all tool arguments

### ❌ Avoid

- Running Docker MCP with root privileges
- Exposing Docker socket unprotected
- Storing credentials in code
- Running untrusted containers
- Mounting host filesystems unnecessarily

### Security Hardening

```bash
# Enable Docker content trust
export DOCKER_CONTENT_TRUST=1

# Use signature verification
docker pull --disable-content-trust=false myimage

# Run containers with security options
hermes chat "Run container with --security-opt=no-new-privileges and --read-only"
```

---

## Performance Optimization

### Caching

```yaml
# ~/.hermes/config.yaml
mcp_servers:
  docker:
    env:
      DOCKER_CACHE_ENABLED: "true"
      DOCKER_CACHE_TTL: "300"
```

### Parallel Operations

```bash
# Execute multiple operations
hermes chat "Parallel: start container-a AND start container-b"
```

### Resource Limits

```bash
# Set agent limits
hermes config set terminal.timeout_seconds 120
hermes config set agent_settings.tool_output_max_bytes 50000
```

---

## Summary Checklist

- [ ] Docker installed and running
- [ ] Docker MCP server installed
- [ ] Hermes configured with Docker MCP
- [ ] API keys configured if using registries
- [ ] Docker socket permissions verified
- [ ] SSH key configured for remote (if applicable)
- [ ] Security policies in place
- [ ] Logging enabled for auditing

---

**Document Version:** 1.0  
**Last Updated:** May 25, 2026  
**Author:** Alexa
