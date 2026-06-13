# Redis MCP Server (Official)

**Source:** https://github.com/redis/mcp-redis

## Overview

The **official Redis MCP Server** is a **natural language interface** designed for agentic applications to efficiently manage and search data in Redis. It integrates with **MCP (Model Context Protocol) clients**, enabling AI-driven workflows to interact with structured and unstructured data in Redis.

> **Key capability:** Ask questions like "Find all users who logged in last week" or "Show me the top 10 products by sales" using natural language.

## Features

| Category | Details |
|----------|---------|
| **Transport Protocols** | `stdio`, `streamable-http` |
| **Redis Data Types Supported** | `string`, `hash`, `list`, `set`, `sorted set`, `pub/sub`, `streams`, `JSON` |
| **Additional Tools** | `docs`, `MCP_DOCS_SEARCH_URL`, `query engine`, `server management` |

## Installation Methods

### 1. From PyPI (Recommended)

```json
{
  "mcpServers": {
    "RedisMCPServer": {
      "command": "uvx",
      "args": [
        "--from",
        "redis-mcp-server@latest",
        "redis-mcp-server",
        "--url",
        "redis://localhost:6379/0"
      ]
    }
  }
}
```

### 2. From GitHub

```bash
# Specific release (recommended)
uvx --from git+https://github.com/redis/mcp-redis.git@0.2.0 redis-mcp-server --url redis://localhost:6379/0

# Main branch (may have breaking changes)
uvx --from git+https://github.com/redis/mcp-redis.git@main redis-mcp-server --url redis://localhost:6379/0
```

### 3. Development Installation

```bash
git clone https://github.com/redis/mcp-redis.git
cd mcp-redis
uv sync
uv run redis-mcp-server --url redis://localhost:6379/0
```

### 4. Docker

```bash
# Build custom image
docker build -t mcp-redis .

# Or use official image
docker pull mcp/redis
```

**Claude Desktop Docker config:**
```json
{
  "mcpServers": {
    "RedisMCPServer": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "mcp/redis", "redis-mcp-server", "--url", "redis://host.docker.internal:6379/0"]
    }
  }
}
```

## URL Connection Formats

| Scheme | Format | Use Case |
|--------|--------|----------|
| **redis** | `redis://user:secret@localhost:6379/0?foo=bar&qux=baz` | Standard connections |
| **rediss** | `rediss://user:secret@localhost:6379/0?foo=bar&qux=baz` | Encrypted connections (Redis Cloud) |
| **rediss (verified)** | `rediss://user:secret@hostname:port?ssl_cert_reqs=required&ssl_ca_certs=path_to_certificate` | With certificate verification |
| **rediss (unverified)** | `rediss://user:secret@hostname:port?ssl_cert_reqs=none` | Skip certificate verification |

> **Note:** The database number (`/0`) refers to the [logical database](https://redis.io/docs/latest/commands/select/).

## Configuration

### Precedence Order

**Command line arguments > Environment variables > Default values**

### CLI Options

| Option | Description |
|--------|-------------|
| `--url` | Full Redis connection URL |
| `--host` | Redis hostname/IP |
| `--port` | Redis port |
| `--db` | Database number |
| `--username` | Username for ACL |
| `--password` | Password for ACL |
| `--ssl` | Enable SSL/TLS |
| `--ssl-ca-path` | CA certificate path |
| `--ssl-keyfile` | Client private key |
| `--ssl-certfile` | Client certificate |
| `--ssl-cert-reqs` | Certificate requirements |
| `--ssl-ca-certs` | Trusted CA certificates file |
| `--cluster-mode` | Enable Redis Cluster mode |

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `REDIS_HOST` | Redis IP/hostname | `"127.0.0.1"` |
| `REDIS_PORT` | Redis port | `6379` |
| `REDIS_DB` | Database number | `0` |
| `REDIS_USERNAME` | Default username | `"default"` |
| `REDIS_PWD` | Password | `""` |
| `REDIS_SSL` | Enable SSL/TLS | `False` |
| `REDIS_SSL_CA_PATH` | CA certificate path | `None` |
| `REDIS_SSL_KEYFILE` | Client private key file | `None` |
| `REDIS_SSL_CERTFILE` | Client certificate file | `None` |
| `REDIS_SSL_CERT_REQS` | Verify server certificate | `"required"` |
| `REDIS_SSL_CA_CERTS` | Trusted CA certs file | `None` |
| `REDIS_CLUSTER_MODE` | Enable cluster mode | `False` |

### Redis ACL Example

```bash
# Create read-only user
127.0.0.1:6379> ACL SETUSER readonlyuser on >mypassword ~* +@read -@write
```

## EntraID Authentication (Azure Managed Redis)

### Authentication Flows

| Flow | Variables Required | Use Case |
|------|-------------------|----------|
| **Service Principal** | `REDIS_ENTRAID_CLIENT_ID`, `REDIS_ENTRAID_CLIENT_SECRET`, `REDIS_ENTRAID_TENANT_ID` | Application-based auth |
| **Managed Identity** | `REDIS_ENTRAID_IDENTITY_TYPE` (`system_assigned`/`user_assigned`), `REDIS_ENTRAID_USER_ASSIGNED_CLIENT_ID` | Azure-hosted apps |
| **Default Azure Credential** | `REDIS_ENTRAID_SCOPES`, `REDIS_ENTRAID_RESOURCE` | Development (auto-discovery) |

### EntraID Configuration Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `REDIS_ENTRAID_AUTH_FLOW` | Auth flow type | `None` (disabled) |
| `REDIS_ENTRAID_CLIENT_ID` | Client ID | `None` |
| `REDIS_ENTRAID_CLIENT_SECRET` | Client secret | `None` |
| `REDIS_ENTRAID_TENANT_ID` | Tenant ID | `None` |
| `REDIS_ENTRAID_IDENTITY_TYPE` | `system_assigned` / `user_assigned` | `None` |
| `REDIS_ENTRAID_USER_ASSIGNED_CLIENT_ID` | User-assigned identity client ID | `None` |
| `REDIS_ENTRAID_SCOPES` | OAuth scopes | `None` |
| `REDIS_ENTRAID_RESOURCE` | Resource URL | `"https://redis.azure.com"` |

## Hermes Integration

For Hermes Agent (uvx mode - PyPI):

```yaml
mcp_servers:
  redis:
    command: "uvx"
    args: ["--from", "redis-mcp-server@latest", "redis-mcp-server", "--url", "redis://localhost:6379/0"]
    env:
      REDIS_URL: "redis://localhost:6379/0"
    tools:
      include: [get, set, delete, exists, keys, scan, incr, decr, lpush, lpop, lrange, sadd, srem, smembers, zadd, zrem, zrange]
```

For Docker mode:

```yaml
mcp_servers:
  redis:
    command: "docker"
    args: ["run", "-i", "--rm", "mcp/redis", "redis-mcp-server", "--url", "redis://host.docker.internal:6379/0"]
    env:
      REDIS_URL: "redis://host.docker.internal:6379/0"
    tools:
      include: [get, set, delete, exists, keys, scan, incr, decr, lpush, lpop, lrange, sadd, srem, smembers, zadd, zrem, zrange]
```

Then run:
```bash
hermes mcp test redis
/reload-mcp
```

## References

- GitHub: https://github.com/redis/mcp-redis
- PyPI: https://pypi.org/project/redis-mcp-server/
- Docker: mcp/redis
- Redis Docs: https://redis.io/docs/latest/integrate/redis-mcp/client-conf
- claudedirectory.org: https://www.claudedirectory.org/mcp-servers/redis