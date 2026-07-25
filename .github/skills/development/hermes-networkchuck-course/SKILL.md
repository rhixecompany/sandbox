---
name: hermes-networkchuck-course
title: "Hermes Agent NetworkChuck Course"
description: "Use when following the NetworkChuck Academy Hermes course — covers 10-video curriculum: installation, CLI/TUI, messaging platforms, memory, skills, automations, homelab integrations, and safety evaluation."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [hermes, networkchuck, course, academy, tutorial, homelab, unifi, synology, vmware]
---
# Hermes Agent NetworkChuck Course

## Purpose

Structured learning path from NetworkChuck Academy Hermes course (10 videos, 5 hours) with Jeremy Cioara.

## When to Use

- Following the NetworkChuck Hermes course
- Learning Hermes for homelab automation
- Integrating with UniFi, Synology, VMware
- Understanding agent safety/permissions

## When NOT to Use

- Quick Hermes setup (use quickstart)
- Developer API integration (different focus)
- Non-homelab use cases

## Skills Required

| Skill | Purpose |
|-------|---------|
| `executing-plans` | Follow 10-video curriculum sequentially |
| `systematic-debugging` | Debug homelab integrations |

## Workflow

### Phase 1: Course Overview

**Instructors:** NetworkChuck + Jeremy Cioara
**Format:** 10 videos, 5 hours total
**Access:** NetworkChuck Academy subscription

**Key Differentiator:** Memory-driven architecture → self-improving over time

**Capabilities Covered:**
- Tools + external systems
- Cross-session memory
- Reusable skills creation
- Scheduled automations
- Messaging platforms (Telegram, Discord, Slack, WhatsApp, Signal)
- Persistent memory

### Phase 2: What You'll Learn

- Hermes vs chatbots/coding copilots
- Installation in supported environments
- CLI and messaging platform usage
- Memory, tools, skills, scheduled automations
- Homelab connections (UniFi, Synology, VMware)
- Network/storage/VM status summarization
- Agent safety and permissions evaluation

### Phase 3: Supported Environments

- Linux, macOS, WSL2
- Servers, cloud infrastructure
- Native Windows (early beta)

### Phase 4: Safety Principles

> "The goal is not to give an agent unlimited access; the goal is to connect useful tools in controlled ways."

- Permissions and approvals matter
- Boundaries and careful workflow design
- Controlled tool access

### Phase 5: Video Curriculum Map

| Video | Topic | Skills Practiced |
|-------|-------|------------------|
| 1 | Introduction & Philosophy | — |
| 2 | Installation & Setup | `hermes-setup` |
| 3 | CLI & TUI Basics | — |
| 4 | Messaging Gateway Setup | `hermes-config` |
| 5 | Memory System Deep Dive | `hermes-persistent-memory` |
| 6 | Skills & Learning Loop | `skill-creator`, `hermes-skill-library-maintenance` |
| 7 | Cron Jobs & Automations | `cronjob` |
| 8 | Homelab: UniFi Integration | `mcp-unifi`, `mcp-docker` |
| 9 | Homelab: Synology + VMware | `mcp-synology`, `mcp-vmware` |
| 10 | Safety, Permissions, Evaluation | `mcp-security-audit` |

### Phase 6: Homelab Integration Patterns

**UniFi:** Network device status, client list, bandwidth usage
**Synology:** Storage health, volume usage, SMART status
**VMware:** VM power state, resource usage, snapshot status

**Pattern:** MCP server per service → Hermes tools → scheduled summaries → messaging alerts

### Phase 7: Installation Code

```bash
# Linux/macOS
curl -fsSL https://get.hermes.dev | bash

# Windows (PowerShell as Admin)
# wget https://get.hermes.dev -OutFile install.ps1; ./install.ps1

# Verify
hermes --version
```

```python
# Test connection
import subprocess
def test_hermes():
    result = subprocess.run(["hermes", "--version"], capture_output=True, text=True)
    print(f"Version: {result.stdout.strip()}")
```

### Phase 8: Platform Detection

```python
import platform

def get_platform():
    system = platform.system().lower()
    if system == "windows":
        print("Windows: Use WSL2 for best Hermes experience")
        print("Native Windows in early beta - some features may be unstable")
    elif system == "linux":
        print("Linux: Full support - install via curl")
    elif system == "darwin":
        print("macOS: Full support - install via brew or curl")
    return system
```

### Phase 9: Error Handling

```python
# Common MCP connection errors
MCP_ERRORS = {
    "ECONNREFUSED": "MCP server not running - start it first",
    "ETIMEDOUT": "MCP server unreachable - check network",
    "401": "Authentication failed - check API keys",
    "403": "Permission denied - check MCP configuration",
}

def resolve_mcp_error(error: str) -> str:
    for key, message in MCP_ERRORS.items():
        if key in error:
            return message
    return f"Unknown error: {error} - check hermes logs"
```

## Pitfalls

- **Academy subscription required** — Not free content
- **Windows beta** — Some features unstable on native Windows
- **MCP servers separate** — Must install/configure UniFi/Synology/VMware MCPs
- **Permissions model** — Start restrictive; expand deliberately

## Verification Checklist

- [ ] Course access verified
- [ ] Hermes installed in target environment
- [ ] Memory system understood
- [ ] At least one skill created
- [ ] One cron automation running
- [ ] One homelab MCP connected (if applicable)

## References

- `references/course-notes.md` — Detailed video summaries
- `references/homelab-mcp-setup.md` — UniFi/Synology/VMware MCP configs
- `references/safety-checklist.md` — Agent evaluation framework
- `references/course-patterns.md` — Installation and platform guides

## Templates

- `templates/hermes-course-checklist.md` — Course tracking template

## Scripts

- `scripts/hermes-install-test.py` — Installation verification script