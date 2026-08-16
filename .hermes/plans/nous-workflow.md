# Nous Portal Provider Workflow Implementation Plan

**Date:** 2026-08-16  
**Provider:** nous  
**Status:** pending  

---

## Goal

Implement the complete nous provider workflow: OAuth credential verification, model selection (300+ via Nous Portal), base_url verification, model catalog accessibility, and MCP compatibility.

## Architecture

Nous Portal uses OAuth (device_code flow) and serves as the foundation provider with base_url `https://inference-api.nousresearch.com/v1`. The current active model is upstage/solar-pro4:free. 300+ models available via portal.

## Tech Stack

- Hermes CLI
- Nous Portal OAuth (hermes auth)
- Model catalog: https://hermes-agent.nousresearch.com/docs/api/model-catalog.json

---

## Tasks

### Task 1: Verify OAuth Credentials

**Step 1: List OAuth credentials**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes auth list nous 2>&1'
```

**Step 2: Check doctor**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes doctor 2>&1 | grep -A2 nous'
```

**Step 3: Document** → `.hermes/plans/results/nous-auth.txt`

---

### Task 2: Verify Model Selection

**Step 1: List models**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes model 2>&1 | grep -A20 "nous"'
```

**Step 2: Test model responsiveness**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes chat -q "Hello from Nous Portal" 2>&1'
```

**Step 3: Document** → `.hermes/plans/results/nous-model.txt`

---

### Task 3: Verify Base URL Configuration

**Step 1: Check config.yaml**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'cat ~/.hermes/config.yaml | grep -B2 -A5 "inference-api.nousresearch"'
```

**Step 2: Verify model_catalog URL accessibility**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'curl -s -o /dev/null -w "%{http_code}" https://hermes-agent.nousresearch.com/docs/api/model-catalog.json 2>&1'
```
Expected: 200

**Step 3: Document** → `.hermes/plans/results/nous-baseurl.txt`

---

### Task 4: Compile Workflow Report

**Step 1: Aggregate results**
**Step 2: Write report** → `.hermes/plans/results/nous-workflow-report.md`

---

## Dependencies

- Task 1 → Task 2 → Task 3 → Task 4

## Verification

- [ ] OAuth token verified
- [ ] Model tested
- [ ] Base URL + model catalog verified
- [ ] Report compiled

## Approval Gate

Review this plan and results before proceeding to the next provider.
