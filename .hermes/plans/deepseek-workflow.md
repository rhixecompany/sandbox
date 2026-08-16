# Deepseek Provider Workflow Implementation Plan

**Date:** 2026-08-16  
**Provider:** deepseek  
**Status:** pending  

---

## Goal

Implement the complete deepseek provider workflow: credential verification (DEEPSEEK_API_KEY), model selection (deepseek-v4-flash-free via opencode-zen + direct models), bug #21725 workaround, and MCP compatibility.

## Architecture

Deepseek has a critical bug (#21725): the provider ignores api_key in config.yaml and only reads DEEPSEEK_API_KEY env var. The active model deepseek-v4-flash-free is accessed via opencode-zen, not directly. Need to work around the bug and document the dual access path.

## Tech Stack

- Hermes CLI
- DEEPSEEK_API_KEY
- DeepSeek API

---

## Tasks

### Task 1: Verify API Key

**Step 1: Check env var**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'cat "$(hermes config env-path 2>&1 | tail -1)" 2>&1 | grep -i deepseek'
```

**Step 2: List pooled credentials**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes auth list deepseek 2>&1'
```

**Step 3: Check doctor**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes doctor 2>&1 | grep -A2 deepseek'
```

**Step 4: Document** → `.hermes/plans/results/deepseek-auth.txt`

---

### Task 2: Verify Model Access

**Step 1: List models**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes model 2>&1 | grep -A20 "deepseek"'
```

**Step 2: Test model**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes chat -q "Hello from DeepSeek" 2>&1'
```

**Step 3: Document** → `.hermes/plans/results/deepseek-model.txt`

---

### Task 3: Document Provider Relationship

**Step 1: Analyze how deepseek provider relates to opencode-zen**
- deepseek-v4-flash-free is hosted by opencode-zen
- Direct deepseek provider may offer different models (deepseek-chat, deepseek-coder)

**Step 2: Write analysis** → `.hermes/plans/results/deepseek-relationship.txt`

---

### Task 4: Compile Workflow Report

**Step 1: Aggregate results**
**Step 2: Write report** → `.hermes/plans/results/deepseek-workflow-report.md`

---

## Dependencies

- Task 1 → Task 2 → Task 3 → Task 4

## Verification

- [ ] API key verified
- [ ] Model access tested
- [ ] Provider relationship documented
- [ ] Report compiled

## Approval Gate

Review this plan and results before proceeding to the next provider.
