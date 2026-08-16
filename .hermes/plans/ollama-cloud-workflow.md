# Ollama-Cloud Provider Workflow Implementation Plan

**Date:** 2026-08-16  
**Provider:** ollama-cloud  
**Status:** pending  

---

## Goal

Implement the complete ollama-cloud provider workflow: credential verification (OLLAMA_API_KEY), model selection (dynamic discovery), context window compliance (≥64K), fallback chain position (last resort), and MCP compatibility.

## Architecture

Ollama Cloud is the last resort in the fallback chain. Verify credentials and model availability, confirm 64K context minimum, and test MCP compatibility.

## Tech Stack

- Hermes CLI
- OLLAMA_API_KEY
- nemotron-3-ultra model (default)

---

## Tasks

### Task 1: Verify Credentials

**Step 1: Check env var**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'cat "$(hermes config env-path 2>&1 | tail -1)" 2>&1 | grep -i ollama'
```

**Step 2: List pooled credentials**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes auth list ollama-cloud 2>&1'
```

**Step 3: Check doctor**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes doctor 2>&1 | grep -A2 ollama'
```

**Step 4: Document** → `.hermes/plans/results/ollama-cloud-auth.txt`

---

### Task 2: Verify Model Selection

**Step 1: List models**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes model 2>&1 | grep -A20 "ollama"'
```

**Step 2: Verify context window ≥ 64K**
- Check model context length in model list output

**Step 3: Test responsiveness**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes chat -q "Hello from ollama-cloud" 2>&1'
```

**Step 4: Document** → `.hermes/plans/results/ollama-cloud-model.txt`

---

### Task 3: Verify Fallback Position

**Step 1: Confirm ollama-cloud is last in chain**
Read fallback_providers config.

**Step 2: Document** → `.hermes/plans/results/ollama-cloud-fallback.txt`

---

### Task 4: Compile Workflow Report

**Step 1: Aggregate results**
**Step 2: Write report** → `.hermes/plans/results/ollama-cloud-workflow-report.md`

---

## Dependencies

- Task 1 → Task 2 → Task 3 → Task 4

## Verification

- [ ] Credentials verified
- [ ] Model context window ≥ 64K confirmed
- [ ] Fallback position documented
- [ ] Report compiled

## Approval Gate

Review this plan and results before proceeding to the next provider.
