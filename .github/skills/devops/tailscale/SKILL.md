---
name: tailscale
title: "Tailscale Tailnet Management"
description: "Use when managing Tailscale tailnet via API v2 — device inventory, ACLs, auth keys, DNS config, and node maintenance."
version: 1.0.0
author: "Hermes Agent"
tags: [tailscale, vpn, networking, tailnet, acl, management]
---

# Tailscale Tailnet Management

## When to Use

- Listing devices on a Tailscale tailnet
- Viewing or applying ACL/tailnet policies
- Managing auth keys for joining new machines
- Configuring DNS settings on the tailnet
- Scripted API access for tailnet automation

## Prerequisites

- Tailscale installed (Windows: `C:\Program Files\Tailscale\tailscale.exe`)
- Tailscale API key (`tskey-api-...`) from admin console
- Tailnet identifier (email for personal, `org.ts.net` for business)

## Local Node Commands

```bash
# Status
"/c/Program Files/Tailscale/tailscale.exe" status

# Machine info
"/c/Program Files/Tailscale/tailscale.exe" whois <ip>

# Join machine
tailscale up --auth-key <auth-key>
```

## API v2 Endpoints

All calls use `https://api.tailscale.com/api/v2/` with `Authorization: Bearer <api-key>` header.

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/tailnet/{tailnet}/devices` | GET | List all devices |
| `/tailnet/{tailnet}/acl` | GET | Read ACL policy |
| `/tailnet/{tailnet}/acl` | POST | Apply ACL from JSON |
| `/tailnet/{tailnet}/keys` | GET | List auth keys |
| `/tailnet/{tailnet}/keys` | POST | Create auth key |
| `/tailnet/{tailnet}/dns` | GET | DNS configuration |
| `/device/{id}/key` | PATCH | Disable key expiry |

## API Key Storage

Store API credentials locally for scripted access. **Never commit credentials to repos.**

```bash
# ~/.tailscale/credentials.sh — source before API calls
export TAILSCALE_API_KEY="tskey-api-..."    # For API v2 calls
export TAILSCALE_AUTH_KEY="tskey-auth-..."  # For joining new machines
chmod 600 ~/.tailscale/credentials.sh
```

| Key Type | Prefix | Purpose |
|----------|--------|---------|
| API key | `tskey-api-` | Tailscale API v2 calls (ACLs, devices, keys, DNS) |
| Auth key | `tskey-auth-` | Join new machines to tailnet via `tailscale up --auth-key` |
| OAuth client | `tskey-client-` | Expiring, scoped tokens for CI/CD |

```bash
source ~/.tailscale/credentials.sh
# Now TAILSCALE_API_KEY is available for curl or tailscale-mgr.py
```

## Python Manager Script

Use `~/.local/bin/tailscale-mgr.py` — a full CLI wrapping all endpoints:

```bash
source ~/.tailscale/credentials.sh

tailscale-mgr devices       # list nodes
tailscale-mgr acl           # show policies
tailscale-mgr acl-apply f.json  # apply ACL
tailscale-mgr auth-keys     # list keys
tailscale-mgr whois <ip>    # device details
```

## Tailnet Types

| Aspect | Personal | Business |
|--------|----------|----------|
| ACL default | Allow all | Tag/group-based |
| Users | 1 | Multi-user |
| Tailnet ID | Email | `org.ts.net` |

## Pitfalls

| Pitfall | Mitigation |
|---------|------------|
| API key scope insufficient | Create key with ACL read/write from admin console |
| MSYS2 path issues on Windows | Use `cygpath -w` for paths to Windows Python |
| Auth key single-use vs reusable | Reusable for CI/CD; single-use for ephemeral machines |
| Device key expiry disconnects nodes | Disable via API: PATCH device with `keyExpiryDisabled: true` |
