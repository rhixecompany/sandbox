# xAI (Grok) Provider Workflow Implementation Plan

**Date:** 2026-08-16  
**Provider:** xai  
**Status:** pending  

---

## Goal

Implement the complete xai provider workflow: credential verification (XAI_API_KEY + SuperGrok OAuth), model selection (grok-4.3 1M context, grok-4.6, grok-4.3-fast), TTS configuration (voxtral-mini-tts-2603), direct-to-xAI tools, provider aliases, and MCP compatibility.

## Architecture

xAI/Grok has two auth paths: API key (direct) and SuperGrok OAuth (browser-based). One of two credentials failed (403). TTS is configured with voxtral-mini-tts-2603. Provider aliases provide multiple ways to reference the same provider.

## Tech Stack

- Hermes CLI
- XAI_API_KEY
- Grok models (grok-4.3, grok-4.3-fast, grok-4.6, voxtral-mini-tts-2603)

---

## Tasks

### Task 1: Verify Credentials

**Step 1: Check env var**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'cat "$(hermes config env-path 2>&1 | tail -1)" 2>&1 | grep -i xai'
```

**Step 2: List pooled credentials**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes auth list xai 2>&1'
```

**Step 3: Check doctor**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes doctor 2>&1 | grep -A2 xai'
```

**Step 4: Document** → `.hermes/plans/results/xai-auth.txt`

---

### Task 2: Verify Model Selection

**Step 1: List models**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes model 2>&1 | grep -A20 "xai"'
```

**Step 2: Test Grok model**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes chat -q "What is the meaning of life?" -m grok-4.3 2>&1'
```

**Step 3: Document** → `.hermes/plans/results/xai-model.txt`

---

### Task 3: Verify TTS Configuration

**Step 1: Check TTS config**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'cat ~/.hermes/config.yaml | grep -A10 "tts:"'
```

**Step 2: Verify voxtral-mini-tts-2603 is configured**

**Step 3: Document** → `.hermes/plans/results/xai-tts.txt`

---

### Task 4: Compile Workflow Report

**Step 1: Aggregate results**
**Step 2: Write report** → `.hermes/plans/results/xai-workflow-report.md`

---

## Dependencies

- Task 1 → Tasks 2-3 (parallel) → Task 4

## Verification

- [ ] Credentials verified (note: 1 of 2 failed with 403)
- [ ] Grok model tested
- [ ] TTS config documented
- [ ] Report compiled

## Approval Gate

Review this plan and results before proceeding to the next provider.
