---
name: hermes-agent-diagnostics-configuration
title: Hermes Agent Diagnostics Configuration
description: "Hermes Agent health diagnostics, configuration verification, and fallback provider routing setup. Covers status checks, doctor repairs, model validation, and redundant failover chain configuration."
author: Alexa
version: 1.0.0
tags:
  - hermes
  - configuration
  - diagnostics
  - fallback-routing
  - reliability
  - agent-setup
---

# Hermes Agent Diagnostics & Configuration

## Verification Checklist

- [ ] Prerequisites verified and available
- [ ] Hermes Agent Diagnostics Configuration operations completed successfully
- [ ] Configuration or output verified against requirements
- [ ] No errors or warnings during execution
- [ ] Changes documented and committed if applicable

## Overview

Complete workflow for Hermes Agent health checks, configuration verification, and fallback routing setup. Used to validate agent state, fix issues, and configure automatic model failover for reliability.

## When to Use

- Agent startup or periodic health checks
- Troubleshooting agent connectivity or model issues
- Setting up fallback providers for redundancy
- Validating configuration after system changes
- Verifying API keys and authentication status
- Documenting agent configuration state

## Prerequisites

- Hermes Agent installed (v24+)
- API keys configured in .env (OpenRouter, Google Gemini recommended for fallbacks)
- Python 3.11+ with PyYAML available
- Terminal access (bash/git-bash on Windows)

## Workflow

### Phase 1: Health Diagnostics

1. **Run status check** (shows active model, environment, gateway)
   ```bash
   hermes status
   ```
   Expected output: model name, provider, config version, gateway PID

2. **Run insights** (shows session count, tool usage, health indicator)
   ```bash
   hermes insights
   ```
   Expected output: session count, tool call frequency, data points

3. **Run doctor debug** (checks for config issues, missing deps, security warnings)
   ```bash
   hermes doctor debug
   ```
   Expected output: list of issues (if any) or "all checks passed"

4. **Auto-fix issues** (if doctor found problems)
   ```bash
   hermes doctor --fix
   ```
   Expected: issues resolved, rerun doctor to confirm

### Phase 2: Active Model Verification

1. **Note the primary model from status output** (e.g., qwen3.6-plus-free)

2. **Identify provider and base URL** (e.g., opencode-zen → https://opencode.ai/zen/v1)

3. **Test URL accessibility** (verify endpoint responds)
   ```bash
   curl -s -I https://opencode.ai/zen/v1/models
   ```
   Expected: HTTP 200, Content-Type: application/json

4. **Test model in action** (optional, confirms working)
   ```bash
   echo "test prompt" | hermes -m <model-name> --pass-session-id
   ```
   Expected: agent loads, shows tools, responds to input

### Phase 3: Fallback Provider Configuration

**Prerequisite:** OpenRouter and Google Gemini API keys in .env

1. **Check current fallback chain**
   ```bash
   hermes fallback list
   ```
   Expected: shows primary model and any existing fallback entries

2. **Configure fallback providers** via Python script (non-interactive method):

   ```python
   import yaml
   import os
   import shutil

   # Get config path
   username = os.environ.get('USERNAME', 'Alexa')
   config_path = os.path.join(os.environ['APPDATA'], '..', 'Local', 'hermes', 'config.yaml')
   config_path = os.path.normpath(config_path)

   # Read current config
   with open(config_path, 'r') as f:
       config = yaml.safe_load(f)

   # Add provider credentials (env vars, not hardcoded)
   if config.get('providers') is None:
       config['providers'] = {}

   config['providers']['openrouter'] = {
       'api_key': '${OPENROUTER_API_KEY}'
   }
   config['providers']['google-gemini'] = {
       'api_key': '${GOOGLE_API_KEY}'
   }

   # Add fallback chain
   config['fallback_providers'] = [
       {
           'provider': 'openrouter',
           'model': 'meta-llama/llama-3.3-70b-instruct:free'
       },
       {
           'provider': 'google-gemini',
           'model': 'gemini-3.1-flash'
       }
   ]

   # Backup original
   backup_path = config_path.replace('.yaml', '.backup.yaml')
   shutil.copy(config_path, backup_path)

   # Write updated config
   with open(config_path, 'w') as f:
       yaml.dump(config, f, default_flow_style=False, sort_keys=False)

   print("✅ Fallback providers configured")
   ```

3. **Verify configuration applied**
   ```bash
   hermes fallback list
   ```
   Expected: primary model + 2 fallback entries in order

### Phase 4: Documentation & Reporting

1. **Generate summary** of current configuration (for handoff/auditing)
   ```bash
   hermes status | head -20
   hermes fallback list
   ```

2. **Create documentation files** with:
   - Configuration checklist
   - Fallback routing explanation
   - Quick reference commands
   - Cost analysis

## Pitfalls & Troubleshooting

### Issue: hermes doctor shows "Run hermes setup"
**Cause:** Config initialization incomplete  
**Fix:** Run `hermes doctor --fix` to resolve automatically

### Issue: Fallback routing not activating
**Cause:** API keys missing or .env not loaded  
**Fix:**
```bash
# Verify keys exist
cat ~/.env | grep -E "(OPENROUTER|GOOGLE_API)"
# Verify config syntax
cat ~/.appdata/Local/hermes/config.yaml | grep -A 10 "fallback_providers"
```

### Issue: URL endpoint returns non-200
**Cause:** Provider endpoint down or network issue  
**Fix:** Test with different provider, check network connectivity, verify VPN/proxy settings

### Issue: Python YAML config script fails with path errors
**Cause:** Path escaping or environment variable issues on Windows  
**Fix:**
- Use `os.path.normpath()` to normalize Windows paths
- Use `os.environ['APPDATA']` instead of hardcoded paths
- Wrap string literals in raw strings (r"...") to avoid escape sequences
- Test with `os.path.exists(config_path)` before reading

### Issue: Config edit reverted after restart
**Cause:** Protected config file preventing direct writes  
**Fix:** Use Python script approach (higher privilege) or use `hermes config` CLI if available

## Best Practices

1. **Always backup config before changes**
   ```bash
   cp ~/.appdata/Local/hermes/config.yaml ~/.appdata/Local/hermes/config.backup.yaml
   ```

2. **Use environment variables for secrets**, never hardcode API keys in config

3. **Test URL endpoints before declaring provider ready**
   ```bash
   curl -s -I https://opencode.ai/zen/v1/models
   ```

4. **Verify fallback chain in order** — first entry is first fallback tried if primary fails

5. **Document configuration state** — generate reference files for auditing and handoff

6. **Run health checks weekly** to catch drift early
   ```bash
   hermes doctor
   ```

## Reference Files

- `references/fallback-routing-setup.md` — Python script for non-interactive fallback config, path handling patterns, URL validation, troubleshooting table
- `references/hermes-common-diagnostics.md` — Expected outputs for hermes status/insights/doctor/fallback commands, URL endpoint validation, troubleshooting decision tree, maintenance schedule

## Related Skills

- `hermes-agent` (Hermes setup and configuration basics)
- `devops` (General DevOps diagnostics and troubleshooting)

## See Also

- Hermes Docs: https://hermes-agent.nousresearch.com/docs
- Fallback Routing: https://hermes-agent.nousresearch.com/docs/user-guide/features/fallback-providers
