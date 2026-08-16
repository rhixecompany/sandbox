# OpenCode-Zen Provider Workflow Implementation Plan

**Date:** 2026-08-16  
**Provider:** opencode-zen  
**Status:** pending  

---

## Goal

Implement the complete opencode-zen provider workflow: credential verification (2 keys), model selection, MCP compatibility, fallback chain position, and rate limit management.

## Architecture

Use the Hermes CLI (`hermes auth`, `hermes model`, `hermes doctor`) to validate each aspect of the opencode-zen provider. The primary model is `deepseek-v4-flash-free` via `https://opencode.ai/zen/v1`. Two credentials in pool: vault primary (OPENCODE_ZEN_API_KEY) + zen-backup (manual). fill_first strategy.

## Tech Stack

- Hermes CLI (hermes-agent installed)
- OPENCODE_ZEN_API_KEY (vault primary + zen-backup)
- MCP servers: sequential-thinking, github, filesystem (test subset)

---

## Tasks

### Task 1: Verify Credentials

**Objective:** Confirm both API keys in the credential pool are valid.

**Files:** N/A (CLI commands)

**Step 1: List pooled credentials**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes auth list opencode-zen 2>&1'
```
Expected: 2 keys listed (vault primary + backup)

**Step 2: Check doctor connectivity**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes doctor 2>&1 | grep -A2 opencode'
```
Expected: opencode-zen shows connectivity status

**Step 3: Document findings**
- Write results to `.hermes/plans/results/opencode-zen-auth.txt`

---

### Task 2: Verify Model Selection

**Objective:** Confirm deepseek-v4-flash-free is selectable and responsive.

**Step 1: List available models**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes model 2>&1 | head -30'
```
Expected: opencode-zen provider with deepseek-v4-flash-free listed

**Step 2: Test model responsiveness**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes chat -q "What is 2+2? Answer in one word." -m deepseek-v4-flash-free 2>&1'
```
Expected: Correct answer from model

**Step 3: Document findings**
- Write results to `.hermes/plans/results/opencode-zen-model.txt`

---

### Task 3: Verify MCP Compatibility (Sample)

**Objective:** Test that MCP servers work with opencode-zen backing model.

**Step 1: Test sequential-thinking MCP**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes mcp test sequential-thinking 2>&1'
```
Expected: MCP server responds

**Step 2: Test github MCP**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes mcp test github 2>&1'
```
Expected: MCP server responds

**Step 3: Document findings**
- Write results to `.hermes/plans/results/opencode-zen-mcp.txt`

---

### Task 4: Verify Fallback Chain

**Objective:** Confirm the fallback chain works (opencode-zen → openrouter → gemini → ollama-cloud).

**Step 1: Review fallback config**
Read `.hermes/plans/specs/opencode-zen-workflow-spec.md` for fallback chain details.

**Step 2: Document fallback behavior**
- Write analysis to `.hermes/plans/results/opencode-zen-fallback.txt`

---

### Task 5: Compile Workflow Report

**Objective:** Produce a complete opencode-zen workflow report.

**Step 1: Aggregate all results**
Read all `.hermes/plans/results/opencode-zen-*.txt` files.

**Step 2: Write final report**
Create `.hermes/plans/results/opencode-zen-workflow-report.md` with:
- Credential status
- Model status
- MCP compatibility
- Fallback chain status
- Open questions and recommendations

---

## Dependencies

- Task 1 must complete before Task 2 (credentials needed for model testing)
- Task 2 must complete before Task 3 (model needed for MCP testing)
- Tasks 1-4 feed into Task 5

## Verification

- [ ] All CLI commands executed with captured output
- [ ] Results files written for each task
- [ ] Final workflow report compiles all findings
- [ ] Any provider issues documented with recommendations

## Approval Gate

Review this plan and results before proceeding to the next provider.
