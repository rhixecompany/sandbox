# Hermes Agent & MCP Configuration Guide

**Author:** Alexa  
**Date:** May 25, 2026  
**Status:** Complete Configuration Reference  
**Scope:** Global + Project-Level Setup

---

## Table of Contents

1. [Overview](#overview)
2. [Hermes Agent Architecture](#hermes-agent-architecture)
3. [Model Context Protocol (MCP) Fundamentals](#model-context-protocol-mcp-fundamentals)
4. [Global Configuration](#global-configuration)
5. [Project-Level Configuration](#project-level-configuration)
6. [MCP Server Migration](#mcp-server-migration)
7. [Verification & Validation](#verification--validation)
8. [Docker MCP Servers](#docker-mcp-servers)
9. [Troubleshooting](#troubleshooting)

---

## Overview

### What is Hermes Agent?

Hermes Agent is an open-source CLI AI assistant framework by Nous Research that:
- Connects to multiple LLM providers (OpenRouter, Gemini, OpenCode Zen, etc.)
- Integrates with messaging platforms (Telegram, Discord, Slack, Signal, Matrix)
- Provides specialized tools (browser automation, file operations, terminal execution)
- Supports Model Context Protocol (MCP) for extensible capabilities
- Manages profiles for isolated agent configurations
- Runs cron jobs for scheduled automation

**Current Setup (May 25, 2026):**
- Model: gpt-5.4-mini (OpenAI Codex provider)
- Base URL: https://opencode.ai/zen/v1/chat/completions
- Fallback chain: Llama 70B → Gemini Flash
- Status: Production ready

### What is Model Context Protocol (MCP)?

MCP is an open standard for AI applications to connect to external data sources and tools. Think of it as "USB-C for AI" — a unified interface that:
- Standardizes tool and resource discovery
- Uses JSON-RPC 2.0 for all communication
- Supports three core primitives:
  - **Tools**: Executable functions with parameters and schemas
  - **Resources**: Data endpoints with URIs and MIME types
  - **Prompts**: Template instructions for specific workflows

**Transport Options:**
- **stdio**: Local subprocess communication (low overhead, secure via OS processes)
- **HTTP/SSE**: Remote or multi-client servers (flexible, requires HTTPS for production)

---

## Hermes Agent Architecture

### Installation Layout

| Component | Windows Native Location | Purpose |
|-----------|-------------------------|---------|
| Code | `%LOCALAPPDATA%\hermes\hermes-agent\` | Core application |
| Data/Config | `%LOCALAPPDATA%\hermes\` | Profiles, skills, sessions, memories |
| Binary | `%USERPROFILE%\.local\bin\hermes` (symlink) | CLI entry point |
| Git Bash | `%LOCALAPPDATA%\hermes\git\` | PortableGit (portable POSIX shell) |

### Core Configuration Files

**Global Configuration** (`~/AppData/Local/hermes/config.yaml`)
```yaml
model:
  default: gpt-5.4-mini
  provider: openai-codex  # or openrouter, google-gemini, etc.
  base_url: https://opencode.ai/zen/v1/chat/completions

terminal:
  backend: local  # or: docker, ssh, singularity, modal

gateway:
  enabled: true
  platforms:
    telegram:
      enabled: true
      token: "your_bot_token"
    discord:
      enabled: true
      token: "your_bot_token"

tools:
  browser: true
  terminal: true
  file_operations: true

mcp:
  servers:
    - name: docker
      transport: stdio
      command: docker-mcp-server
    - name: github
      transport: stdio
      command: npx @modelcontextprotocol/server-github
```

**Environment File** (`~/AppData/Local/hermes/.env` or project `.env`)
```bash
# LLM Provider Keys
OPENROUTER_API_KEY=sk-...
GOOGLE_API_KEY=AIza...
OPENAI_API_KEY=sk-...

# Tool API Keys
EXA_API_KEY=...
FIRECRAWL_API_KEY=...
FAL_KEY=...

# Tool Configuration
TERMINAL_ENV=local
HERMES_DOCKER_BINARY=/usr/bin/docker
```

---

## Model Context Protocol (MCP) Fundamentals

### Protocol Layers

```
┌─────────────────────────────────────┐
│   Hermes Agent (Client)             │
│   - Discovers MCP server capabilities
│   - Calls tools, reads resources
│   - Sends prompts to servers
└──────────────┬──────────────────────┘
               │ JSON-RPC 2.0
               │
┌──────────────▼──────────────────────┐
│   MCP Transport Layer               │
│   - stdio (local subprocess)         │
│   - HTTP/SSE (remote/multi-client)  │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│   MCP Server                        │
│   - Tools (functions)               │
│   - Resources (data endpoints)      │
│   - Prompts (templates)             │
└─────────────────────────────────────┘
```

### Server Lifecycle

**Phase 1: Initialization**
```json
Client → Server: initialize
  { protocolVersion: "2024-11-05", capabilities: {...}, clientInfo: {...} }
Server → Client: capabilities
  { protocolVersion: "2024-11-05", serverInfo: {...}, tools: [...], resources: [...] }
Client → Server: initialized
```

**Phase 2: Message Exchange**
- Client calls `tools/call`
- Client reads `resources/read`
- Client retrieves `prompts/get`
- Bidirectional notifications and logging

**Phase 3: Termination**
```json
Client → Server: shutdown
```

### MCP Message Format (JSON-RPC 2.0)

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "execute_command",
    "arguments": { "command": "ls -la" }
  }
}
```

### Transport: stdio vs HTTP

#### stdio Transport
- **Best for:** Local development, single-client scenarios
- **Security:** OS-level process isolation
- **Setup:** Command launched as subprocess
- **Example:**
  ```yaml
  servers:
    - name: filesystem
      transport: stdio
      command: npx @modelcontextprotocol/server-filesystem
      args: ["/path/to/root"]
  ```

#### HTTP/SSE Transport
- **Best for:** Remote servers, multi-client scenarios
- **Security:** HTTPS mandatory, OAuth 2.0 recommended
- **Setup:** Independent server process
- **Example:**
  ```yaml
  servers:
    - name: remote-server
      transport: http
      url: https://api.example.com/mcp
      auth:
        type: bearer
        token: sk-...
  ```

---

## Global Configuration

### Step 1: Verify Installation

```bash
# Check Hermes version
hermes --version

# Check installed tools
hermes tools list

# Verify MCP server availability
hermes mcp list

# Check configuration
hermes config get model.default
hermes config get mcp.servers
```

### Step 2: Configure LLM Model

```bash
# Interactive model selection
hermes model

# Direct configuration
hermes config set model.default gpt-5.4-mini
hermes config set model.provider openai-codex
hermes config set model.base_url https://opencode.ai/zen/v1/chat/completions
```

**Supported Providers:**
- OpenRouter (default)
- Google Gemini
- OpenCode Zen
- OpenCode Go
- Ollama
- Kimi (Moonshot)
- GLM (ZhipuAI)
- Hugging Face
- MiniMax

### Step 3: Configure API Keys

```bash
# Create/update .env file
cat > ~/AppData/Local/hermes/.env << 'EOF'
# Primary LLM
OPENROUTER_API_KEY=sk-or-v1-...
# or
OPENCODE_ZEN_API_KEY=sk-...
GOOGLE_API_KEY=AIza...

# Tools
EXA_API_KEY=...
FIRECRAWL_API_KEY=...
FAL_KEY=...

# Optional: Override base URLs
OPENCODE_ZEN_BASE_URL=https://opencode.ai/zen/v1
EOF

# Verify keys are loaded
hermes config validate
```

### Step 4: Configure Tools

```bash
# Enable/disable specific tools
hermes config set tools.browser true
hermes config set tools.terminal true
hermes config set tools.file_operations true
hermes config set tools.web_search true

# View current tool configuration
hermes config get tools
```

### Step 5: Set Terminal Backend

```bash
# Default: local
hermes config set terminal.backend local

# Docker (if available)
hermes config set terminal.backend docker
hermes config set terminal.docker_image nikolaik/python-nodejs:python3.11-nodejs20

# SSH
hermes config set terminal.backend ssh
hermes config set terminal.ssh_host user@host.com
```

---

## Project-Level Configuration

### Step 1: Create Project `.env`

```bash
# In project root
cat > .env << 'EOF'
# Hermes Configuration for This Project
HERMES_PROFILE=default

# Override model for this project
LLM_MODEL=gpt-5.4-mini

# Tool configuration
TERMINAL_ENV=local

# MCP Servers (project-specific)
MCP_DOCKER_ENABLED=true
MCP_GITHUB_ENABLED=true
MCP_FILESYSTEM_ENABLED=true
EOF
```

### Step 2: Create Project `hermes.yaml`

```bash
# In project root
cat > hermes.yaml << 'EOF'
# Hermes Project Configuration
name: Sandbox
description: Multi-project agentic workflow

# Project-specific MCP servers
mcp:
  servers:
    - name: docker
      transport: stdio
      command: docker-mcp-server
      args: []
    - name: github
      transport: stdio
      command: npx @modelcontextprotocol/server-github
      args: []
    - name: filesystem
      transport: stdio
      command: npx @modelcontextprotocol/server-filesystem
      args: ["/workspace"]

# Tool defaults for this project
tools:
  terminal:
    backend: local
    timeout: 300
    working_directory: .
  browser:
    headless: true
    timeout: 60
  file_operations:
    root_directory: .

# Cron job definitions
cron:
  jobs: []  # Add as needed

# Skills management
skills:
  custom_path: ./skills
  auto_load: true
EOF
```

### Step 3: Verify Project Configuration

```bash
# Load project context
cd /path/to/project
hermes config load hermes.yaml

# Validate MCP servers
hermes mcp list

# Test tool connectivity
hermes test-tools

# Check environment
hermes config get --all
```

---

## MCP Server Migration

### Discovery Phase

```bash
# List all available MCP servers
hermes mcp list

# Get server details
hermes mcp info docker
hermes mcp info github

# Check server status
hermes mcp status
```

### Migration Strategy

**Phase 1: Backup Current Configuration**
```bash
# Create backup
cp -r ~/AppData/Local/hermes/config.yaml ~/AppData/Local/hermes/config.yaml.backup.$(date +%s)
cp -r hermes.yaml hermes.yaml.backup.$(date +%s)
```

**Phase 2: Identify Servers to Migrate**
```bash
# List loaded MCP servers
hermes mcp list

# Categorize by:
# - Transport type (stdio vs HTTP)
# - Status (active vs inactive)
# - Dependencies (package manager)
```

**Phase 3: Install Package Manager Dependencies**

For **bun** (your configured package manager):
```bash
# Install bun globally (if not present)
curl -fsSL https://bun.sh/install | bash

# Verify installation
bun --version

# Install MCP server packages
bun install @modelcontextprotocol/server-filesystem
bun install @modelcontextprotocol/server-github
bun add @modelcontextprotocol/server-git
```

**Phase 4: Update Configuration**

```yaml
# ~/AppData/Local/hermes/config.yaml
mcp:
  servers:
    - name: filesystem
      transport: stdio
      command: bun run --script "npx @modelcontextprotocol/server-filesystem"
      args: ["/workspace"]
      
    - name: github
      transport: stdio
      command: bun run --script "npx @modelcontextprotocol/server-github"
      env:
        GITHUB_TOKEN: ${GITHUB_TOKEN}
      
    - name: git
      transport: stdio
      command: bun run --script "npx @modelcontextprotocol/server-git"
      args: ["/workspace/.git"]
```

**Phase 5: Test Each Server**

```bash
# Test individual server
hermes mcp test filesystem

# Full health check
hermes mcp healthcheck

# Monitor startup
hermes mcp debug --verbose
```

**Phase 6: Validate Integration**

```bash
# Ensure tools are discoverable
hermes tools list

# Test a tool from migrated server
hermes execute --tool "filesystem/read_file" --args '{"path": "README.md"}'

# Verify no regressions
hermes verify-mcp-servers
```

---

## Docker MCP Servers

### Inspection via Docker Gateway

```bash
# Start Docker MCP Gateway with adminbot profile
docker mcp gateway run --profile adminbot

# In another terminal, discover available tools
hermes mcp list --transport http --url http://localhost:3000

# List Docker-specific tools
hermes tools list | grep -i docker
```

### Available Docker MCP Tools

The Docker MCP server exposes ~40 tools including:

**Container Management:**
- `docker/container/list`
- `docker/container/create`
- `docker/container/start`
- `docker/container/stop`
- `docker/container/restart`
- `docker/container/logs`
- `docker/container/stats`
- `docker/container/exec`
- `docker/container/remove`

**Image Management:**
- `docker/image/list`
- `docker/image/pull`
- `docker/image/push`
- `docker/image/build`
- `docker/image/remove`
- `docker/image/inspect`

**Volume Management:**
- `docker/volume/list`
- `docker/volume/create`
- `docker/volume/remove`
- `docker/volume/inspect`

**Network Management:**
- `docker/network/list`
- `docker/network/create`
- `docker/network/remove`
- `docker/network/inspect`

**Compose & Orchestration:**
- `docker/compose/up`
- `docker/compose/down`
- `docker/compose/status`
- `docker/compose/logs`

**Database Operations:**
- `docker/db/query`
- `docker/db/backup`
- `docker/db/restore`
- `docker/db/status`

### Docker Server Configuration

**Option 1: Local stdio Transport**
```yaml
mcp:
  servers:
    - name: docker
      transport: stdio
      command: docker-mcp-server
      env:
        DOCKER_HOST: unix:///var/run/docker.sock
```

**Option 2: HTTP Transport via Gateway**
```yaml
mcp:
  servers:
    - name: docker-gateway
      transport: http
      url: http://localhost:3000/mcp
      session_id: adminbot
      env:
        PROFILE: adminbot
```

### Running Docker Commands via MCP

```bash
# List containers
hermes execute --tool "docker/container/list" --args '{}'

# Get container logs
hermes execute --tool "docker/container/logs" --args '{"service": "postgres", "lines": 50}'

# Execute command in container
hermes execute --tool "docker/container/exec" --args '{
  "service": "app",
  "command": "npm run test"
}'

# Database query
hermes execute --tool "docker/db/query" --args '{
  "service": "postgres",
  "query": "SELECT * FROM users LIMIT 10"
}'
```

---

## Verification & Validation

### Comprehensive Verification Checklist

#### 1. Global Configuration Verification

```bash
#!/bin/bash
echo "=== Hermes Global Configuration Verification ==="

# Check installation
echo "✓ Hermes version:"
hermes --version

# Check config file exists
echo "✓ Config file location:"
ls -la ~/AppData/Local/hermes/config.yaml

# Validate configuration
echo "✓ Configuration validation:"
hermes config validate

# Check environment
echo "✓ Environment variables:"
env | grep -E "HERMES|OPENROUTER|GOOGLE|OPENCODE"

# Verify tools
echo "✓ Available tools:"
hermes tools list | head -20

# Check profiles
echo "✓ Available profiles:"
ls -la ~/AppData/Local/hermes/profiles/
```

#### 2. Project Configuration Verification

```bash
#!/bin/bash
cd /path/to/project

echo "=== Project Configuration Verification ==="

# Check project files
echo "✓ Project config files:"
ls -la {hermes.yaml,.env,AGENTS.md} 2>/dev/null || echo "Missing project files"

# Validate project configuration
echo "✓ Project configuration:"
hermes config load hermes.yaml

# Check working directory
echo "✓ Working directory:"
pwd

# List project files
echo "✓ Project structure:"
find . -maxdepth 2 -type f -name "*.md" -o -name "*.yaml" -o -name ".env"
```

#### 3. MCP Server Verification

```bash
#!/bin/bash
echo "=== MCP Server Verification ==="

# List discovered servers
echo "✓ MCP Servers:"
hermes mcp list

# Check each server status
echo "✓ Server status:"
for server in docker github filesystem git; do
  hermes mcp status "$server" && echo "✓ $server: OK" || echo "✗ $server: FAILED"
done

# Test tool discovery
echo "✓ Tool discovery:"
hermes tools list | wc -l

# Verify transport types
echo "✓ Transport verification:"
hermes mcp list --format json | jq '.servers[] | {name, transport, status}'
```

#### 4. Docker MCP Verification

```bash
#!/bin/bash
echo "=== Docker MCP Verification ==="

# Check Docker installation
echo "✓ Docker:"
docker --version

# Check Docker daemon
echo "✓ Docker daemon status:"
docker ps >/dev/null 2>&1 && echo "Running" || echo "Not running"

# List containers
echo "✓ Active containers:"
docker ps -q | wc -l

# Test Docker MCP connection
echo "✓ Docker MCP tools:"
hermes execute --tool "docker/container/list" --args '{}' | jq '.containers | length'
```

#### 5. Integrated Verification

```bash
#!/bin/bash
echo "=== Integrated Verification ==="

# Test end-to-end: Query model through configured LLM
echo "✓ LLM Connectivity:"
hermes chat "What is 2+2?" --max-tokens 10

# Test tool integration
echo "✓ Tool Integration:"
hermes test-tools --verbose

# Test MCP integration
echo "✓ MCP Integration:"
hermes mcp healthcheck

# Test profile switching
echo "✓ Profile Management:"
hermes profile list

# Verify skills loading
echo "✓ Skills:"
hermes skills list | head -10
```

---

## Troubleshooting

### Common Issues & Solutions

#### Issue 1: MCP Server Fails to Load

**Symptoms:** `Error: Failed to initialize MCP server 'docker'`

**Solution:**
```bash
# Check server command exists
which docker-mcp-server || npm list -g docker-mcp-server

# Verify command syntax
hermes mcp debug --server docker --verbose

# Check environment variables
env | grep -i docker

# Reinstall if needed
npm install -g docker-mcp-server
# or with bun
bun install -g docker-mcp-server
```

#### Issue 2: Tool Not Found

**Symptoms:** `Tool 'docker/container/list' not found`

**Solution:**
```bash
# Reload MCP servers
hermes mcp reload

# Verify tool discovery
hermes mcp list --verbose

# Check server status
hermes mcp status docker

# View available tools
hermes execute --tool "mcp/list_tools" --server docker
```

#### Issue 3: Authentication Failures

**Symptoms:** `401 Unauthorized` or `Invalid API key`

**Solution:**
```bash
# Verify API keys in .env
cat ~/AppData/Local/hermes/.env | grep API_KEY

# Check environment variable loading
hermes config get model.provider
hermes config get model.base_url

# Validate LLM connectivity
hermes test-llm

# Update keys if needed
echo "OPENROUTER_API_KEY=sk-..." >> ~/AppData/Local/hermes/.env
hermes config reload
```

#### Issue 4: Docker MCP Connection Refused

**Symptoms:** `Error: connect ECONNREFUSED 127.0.0.1:3000`

**Solution:**
```bash
# Ensure Docker daemon is running
docker ps  # Should return container list

# Start Docker MCP gateway
docker mcp gateway run --profile adminbot

# Verify gateway is listening
netstat -an | grep 3000  # Windows
ss -an | grep 3000       # Linux

# Check firewall rules
# Allow localhost:3000 if firewall is enabled
```

#### Issue 5: Performance Issues

**Symptoms:** Slow tool execution, timeouts

**Solution:**
```bash
# Increase timeout values
hermes config set terminal.timeout 600
hermes config set tools.browser.timeout 120

# Check system resources
hermes system-info

# Monitor MCP server performance
hermes mcp profile --sample-size 100

# Enable logging for diagnostics
hermes mcp debug --verbose --log-level debug
```

### Debug Mode

```bash
# Enable verbose logging
hermes --verbose

# Enable debug logging
hermes --debug

# Monitor MCP communication
hermes mcp debug --log-level trace

# Profile tool execution
hermes --profile-tools

# Save logs for analysis
hermes chat "test" --log-file /tmp/hermes-debug.log 2>&1
```

### Configuration Validation

```bash
# Full configuration audit
hermes config audit

# Validate YAML syntax
hermes config validate --file ~/AppData/Local/hermes/config.yaml

# Test LLM connection
hermes test-llm --verbose

# Test all tools
hermes test-tools --all

# Health check all systems
hermes healthcheck --full
```

---

## Best Practices

### Security

1. **API Keys:** Never commit `.env` files; use `.gitignore`
2. **HTTP Transport:** Always use HTTPS for remote MCP servers
3. **OAuth 2.0:** Enable for production MCP servers
4. **Environment Isolation:** Use separate `.env` files per profile
5. **Access Control:** Restrict MCP server permissions by tool

### Performance

1. **Resource Limits:** Set appropriate timeouts for tools
2. **Caching:** Enable MCP resource caching when available
3. **Parallelization:** Run independent tools concurrently
4. **Monitoring:** Log and monitor MCP server performance
5. **Profiling:** Identify bottlenecks with performance tools

### Maintenance

1. **Regular Updates:** Keep Hermes and MCP servers updated
2. **Backup Configuration:** Backup `config.yaml` before changes
3. **Test Before Deploy:** Validate changes in isolated profile
4. **Documentation:** Document custom MCP servers and tools
5. **Monitoring:** Set up alerts for MCP server failures

---

## References

- **Hermes Agent Docs:** https://hermes-agent.nousresearch.com/docs
- **MCP Specification:** https://modelcontextprotocol.io/
- **MCP TypeScript SDK:** https://github.com/modelcontextprotocol/typescript-sdk
- **MCP Python SDK:** https://github.com/modelcontextprotocol/python-sdk
- **GitHub MCP Server:** https://github.com/modelcontextprotocol/servers/tree/main/src/github
- **Docker MCP Server:** https://github.com/docker/docker-mcp-server

---

**Last Updated:** May 25, 2026  
**Status:** Production Ready  
**Version:** 1.0.0
