# OpenRouter Provider Workflow Implementation Plan

**Date:** 2026-08-16  
**Provider:** openrouter  
**Status:** pending  

---

## Goal

Implement the complete openrouter provider workflow: credential verification, model selection (400+ models), provider routing configuration, fallback chain position, auxiliary model offload, MCP compatibility, and rate limit management.

## Architecture

Use the Hermes CLI to validate openrouter as the primary fallback. Test model selection across 400+ available models, provider routing configuration, and MCP server compatibility. This is the most complex provider workflow due to OpenRouter's meta-routing capabilities.

## Tech Stack

- Hermes CLI
- OPENROUTER_API_KEY
- Provider routing config in config.yaml
- MCP servers: all 21 enabled servers (test subset)

---

## Tasks

### Task 1: Verify Credentials

**Objective:** Confirm OPENROUTER_API_KEY is valid and check tier.

**Step 1: List pooled credentials**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes auth list openrouter 2>&1'
```

**Step 2: Check doctor connectivity**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes doctor 2>&1 | grep -A2 openrouter'
```

**Step 3: Test with simple query**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes chat -q "What is the capital of France?" 2>&1'
```

**Step 4: Document findings** → `.hermes/plans/results/openrouter-auth.txt`

---

### Task 2: Verify Model Selection

**Objective:** List available models and verify key models are accessible.

**Step 1: List models via OpenRouter**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes model 2>&1 | grep -A50 "openrouter"'
```

**Step 2: Verify key models**
- nvidia/nemotron-3-ultra-550b-a55b:free (default)
- nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free
- nvidia/nemotron-3-super-120b-a12b:free

**Step 3: Test model responsiveness**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes chat -q "Explain quantum computing in simple terms" 2>&1'
```

**Step 4: Document findings** → `.hermes/plans/results/openrouter-model.txt`

---

### Task 3: Verify Provider Routing

**Objective:** Review and test OpenRouter provider routing configuration.

**Step 1: Read config.yaml provider_routing section**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'cat ~/.hermes/config.yaml | grep -A30 "openrouter:"'
```

**Step 2: Document routing settings**
- sort, only, ignore, order settings
- require_parameters, data_collection settings

**Step 3: Test routing behavior**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes chat -q "List 5 programming languages" 2>&1'
```

**Step 4: Document findings** → `.hermes/plans/results/openrouter-routing.txt`

---

### Task 4: Verify Fallback Chain

**Objective:** Confirm openrouter is properly positioned as 2nd in fallback chain.

**Step 1: Review fallback_providers config**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'cat ~/.hermes/config.yaml | grep -A10 "fallback_providers:"'
```

**Step 2: Verify chain order**
Expected: opencode-zen → openrouter → gemini → ollama-cloud

**Step 3: Document findings** → `.hermes/plans/results/openrouter-fallback.txt`

---

### Task 5: Verify Auxiliary Model Offload

**Objective:** Check if openrouter is configured for auxiliary tasks.

**Step 1: Review auxiliary config**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'cat ~/.hermes/config.yaml | grep -A20 "auxiliary:"'
```

**Step 2: Document recommendations**
- Which auxiliary tasks should use openrouter?
- Cheapest model for each auxiliary task?

**Step 3: Write findings** → `.hermes/plans/results/openrouter-auxiliary.txt`

---

### Task 6: MCP Compatibility (Sample)

**Objective:** Test MCP servers with openrouter backing model.

**Step 1: Test sequential-thinking**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes mcp test sequential-thinking 2>&1'
```

**Step 2: Test github**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes mcp test github 2>&1'
```

**Step 3: Test fetch**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes mcp test fetch 2>&1'
```

**Step 4: Document findings** → `.hermes/plans/results/openrouter-mcp.txt`

---

### Task 7: Compile Workflow Report

**Objective:** Produce complete openrouter workflow report.

**Step 1: Aggregate all results**
Read all `.hermes/plans/results/openrouter-*.txt` files.

**Step 2: Write final report**
Create `.hermes/plans/results/openrouter-workflow-report.md` with all findings, recommendations, and open questions.

---

## Dependencies

- Task 1 → Task 2 → Tasks 3-6 (parallel) → Task 7

## Verification

- [ ] All CLI commands executed with captured output
- [ ] Results files written for each task
- [ ] Final workflow report compiles all findings
- [ ] Provider routing configuration documented

## Approval Gate

Review this plan and results before proceeding to the next provider.
