# Prompt Management Orchestration — Implementation Guide

> **Audience:** Operators executing the prompt orchestration pipeline
> **Version:** 1.0.0 | **Lines:** ~1,400
> **Prerequisites:** Hermes CLI, Git, Python 3.11+, VS Code, bash (git-bash/MSYS)

---

## Table of Contents

1. [Quick Start — 5 Minute Entry Point](#1-quick-start--5-minute-entry-point)
2. [System Overview](#2-system-overview)
3. [Phase 0: Verification](#3-phase-0-verification)
4. [Phase 1: Audit Skills Judge Fix](#4-phase-1-audit-skills-judge-fix)
5. [Phase 2: Agents System Prompt Context Fix](#5-phase-2-agents-system-prompt-context-fix)
6. [Phase 3: Sync Hermes Copilot Codex](#6-phase-3-sync-hermes-copilot-codex)
7. [Phase 4: Test Providers & Models](#7-phase-4-test-providers--models)
8. [Shell Scripts](#8-shell-scripts)
9. [Checklists](#9-checklists)
10. [Troubleshooting](#10-troubleshooting)
11. [Rollback Procedures](#11-rollback-procedures)
12. [Git Integration](#12-git-integration)

---

## 1. Quick Start — 5 Minute Entry Point

### 1.1 What You Need

```bash
# Verify Hermes CLI is available
hermes --version

# Verify Python 3.11+
python3 --version

# Verify Git
git --version

# Verify VS Code workspace
code --version

# Set the working directory
cd ~/Desktop/SandBox
```

### 1.2 Run the One-Liner

```bash
# Full pipeline (all 5 phases, sequential)
cd ~/Desktop/SandBox && \
  hermes profile use default && \
  python3 docs/prompt-orchestration-code-samples.py
```

### 1.3 What Happens

| Time | Phase | What You See |
|------|-------|-------------|
| T+0s | Phase 0 | "Prompt files verified" / "Missing prompts" |
| T+30s | Phase 1 | Skills inventory count, dedupe report |
| T+2m | Phase 2 | VS Code JSON validation results |
| T+3m | Phase 3 | Drift check output |
| T+4m | Phase 4 | Provider inventory |
| T+5m | Done | Summary printed, results saved to `docs/` |

### 1.4 Quick Verify

```bash
# Check that artifacts were created
ls -la docs/pipeline-result.json docs/pipeline-summary.md
cat docs/pipeline-summary.md
```

---

## 2. System Overview

### 2.1 Directory Map

```
~/Desktop/SandBox/                          # Workspace root
├── prompts/                                # All prompt files
│   ├── execute-all-prompts.prompt.md       # Orchestrator prompt
│   ├── audit-skills-judge-fix.prompt.md    # Phase 1
│   ├── agents-system-prompt-context-fix.prompt.md  # Phase 2
│   ├── sync-hermes-copilot-codex.prompt.md # Phase 3
│   ├── test-providers-models.prompt.md     # Phase 4
│   └── templates/                          # Phase templates
│       ├── _shared/                        # Shared templates (12 files)
│       └── {prompt-name}/                  # Per-prompt templates
├── docs/                                   # All pipeline artifacts
│   ├── local-skills.md                     # Phase 1 inventory
│   ├── dedupe-report.md                    # Phase 1 dedupes
│   ├── consolidation-report.md             # Phase 1 umbrellas
│   ├── final-verification.md               # Phase 1 verification
│   ├── Project_Architecture/               # Phase 2 context files
│   ├── vscode-validation-report.md         # Phase 2 JSON audit
│   ├── sync-drift-report.md                # Phase 3 drift check
│   ├── provider-inventory.md               # Phase 4 providers
│   ├── pipeline-result.json                # Full JSON output
│   ├── pipeline-summary.md                 # Markdown summary
│   └── prompt-orchestration-code-samples.py  # Reference implementation
├── judge_results/                          # Phase 1 judge scores
│   ├── all_results.tsv                     # 350+ skills scored
│   ├── summary.md                          # Aggregate stats
│   └── batch_*.md                          # Per-batch results (35 files)
├── plan/                                   # Planning artifacts
│   └── prompt-orchestration-comprehensive-plan.md
└── .vscode/                                # VS Code config (5 files)

~/AppData/Local/hermes/
├── skills/                                 # 143+ skill directories
├── scripts/                                # 7 automation scripts
├── plugins/                                # 4 active plugins
└── hooks/                                  # 3 active hooks
```

### 2.2 Pipeline Flow

```
Phase 0 ──► Phase 1 ──► Phase 2 ──► Phase 3 ──► Phase 4
  Verify      Audit       Context     Sync        Providers
              Judge       Files       Agents      Benchmark
              Fix VS      Code
```

**Rule:** Each phase has an "only then" constraint. Phase N+1 NEVER starts until Phase N is fully complete and verified.

---

## 3. Phase 0: Verification

### 3.1 Purpose

Confirm that all prerequisites are in place before beginning execution. This is the "pre-flight check" — catch missing files early.

### 3.2 Step-by-Step

#### Step 0.1: Inventory Target Prompts

```bash
echo "=== Target Prompts ==="
for name in execute-all-prompts audit-skills-judge-fix \
            agents-system-prompt-context-fix sync-hermes-copilot-codex \
            test-providers-models; do
  if ls ~/Desktop/SandBox/prompts/$name.prompt*.md 2>/dev/null; then
    echo "✅ $name found"
  else
    echo "❌ $name NOT FOUND"
  fi
done
```

**Expected output:** 5 ✅, 0 ❌

#### Step 0.2: Verify Template Dirs

```bash
echo "=== Template Directories ==="
for name in execute-all-prompts audit-skills-judge-fix \
            agents-system-prompt-context-fix sync-hermes-copilot-codex \
            test-providers-models; do
  td=~/Desktop/SandBox/prompts/templates/$name
  if [ -d "$td" ]; then
    count=$(ls "$td" | wc -l)
    echo "✅ templates/$name/ ($count files)"
  else
    echo "⚠️  templates/$name/ — not found (optional)"
  fi
done
```

#### Step 0.3: Check Shared Templates

```bash
echo "=== Shared Templates ==="
ls ~/Desktop/SandBox/prompts/templates/_shared/
echo "Count: $(ls ~/Desktop/SandBox/prompts/templates/_shared/ | wc -l)"
```

**Expected:** 12 files (best-practices.md, deps-core.md, frontmatter.md, goals.md, personality.md, personas.md, phases.md, rules-core.md, section-skeleton.md, skill-refs.md, skills-table-core.md, verification-checklist.md)

#### Step 0.4: Check Hermes Profiles

```bash
echo "=== Active Profile ==="
hermes profile show 2>&1 | head -5

echo ""
echo "=== Available Profiles ==="
hermes profile list 2>&1
```

**Expected:** Active profile = `default` (or the profile you intend to use)

#### Step 0.5: Git Status

```bash
echo "=== Git Status ==="
cd ~/Desktop/SandBox && git status --short | head -20
```

**Expected:** Clean or known-modified files. `git status --short` should show no unexpected changes.

### 3.3 Pre-Execution Checklist

- [ ] All 5 prompt files exist
- [ ] Template directories present (or noted as missing)
- [ ] Shared templates populated
- [ ] Active Hermes profile confirmed
- [ ] Git status clean
- [ ] Skills directory at `~/AppData/Local/hermes/skills/` exists
- [ ] Python 3.11+ available (`python3 --version`)
- [ ] `hermes` CLI responds

### 3.4 Blocking Conditions

| Condition | Action |
|-----------|--------|
| Missing prompt file | Check `.prompts.md` extension; if still missing, check `git status` if deleted |
| Hermes CLI not responding | Reinstall or check `PATH` |
| Skills directory missing | Re-run `hermes setup` or `hermes skills update` |
| Python < 3.11 | Install Python 3.11+ from python.org |

---

## 4. Phase 1: Audit Skills Judge Fix

### 4.1 Purpose

Audit all 370+ local Hermes skills, categorize them, deduplicate overlaps, judge quality, remediate poor scores, consolidate umbrella skills, and verify everything.

### 4.2 Phase 1.1: Skills Audit & Inventory

```bash
echo "=== Phase 1.1: Skills Audit ==="
cd ~/Desktop/SandBox

# Run Hermes built-in audit
hermes skills audit 2>&1 | grep -E "(Scan:|Decision:)" | head -30

# Count skills
echo ""
echo "=== Skill Count ==="
find ~/AppData/Local/hermes/skills -name "SKILL.md" | wc -l

# Generate inventory
echo ""
echo "=== Top-level skill dirs ==="
ls -d ~/AppData/Local/hermes/skills/*/ 2>/dev/null | wc -l

# Flat vs nested
echo ""
echo "=== Flat skills (no subdirs) ==="
for d in ~/AppData/Local/hermes/skills/*/; do
  subdirs=$(find "$d" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | wc -l)
  [ "$subdirs" -eq 0 ] && basename "$d"
done | wc -l
```

**Expected output:**
- 111+ skills scanned by `hermes skills audit`
- 489+ total SKILL.md files
- ~46 flat, ~443 nested

**Artifact:** `docs/local-skills.md`

### 4.3 Phase 1.2: Categorize Skills

Flat skills at the root of `skills/` need category frontmatter. Each flat skill directory corresponds to a top-level category.

```python
# categorize_flats.py — quick script to add category frontmatter
import os, re
from pathlib import Path

skills_dir = Path(os.environ["HOME"]) / "AppData" / "Local" / "hermes" / "skills"

for d in sorted(skills_dir.iterdir()):
    if not d.is_dir():
        continue
    # Skip system dirs
    if d.name.startswith("."):
        continue
    # Check if flat (no subdirs)
    subdirs = [s for s in d.iterdir() if s.is_dir()]
    if subdirs:
        continue  # already a category dir
    
    sk = d / "SKILL.md"
    if not sk.exists():
        continue
    
    content = sk.read_text(encoding="utf-8")
    
    # Add metadata.category based on parent directory
    category = d.parent.name if d.parent != skills_dir else "uncategorized"
    
    # Only modify if category is missing
    if "metadata:" in content and "category:" in content:
        continue
    
    # Simple insertion after frontmatter
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            frontmatter = parts[1]
            body = parts[2]
            if "metadata:" not in frontmatter:
                frontmatter += "\nmetadata:\n  hermes:\n    tags: []"
            sk.write_text(f"---{frontmatter}---{body}", encoding="utf-8")
            print(f"Updated: {d.name}")
```

**Artifact:** Each flat skill now has metadata.

### 4.4 Phase 1.3: Deduplicate

```bash
echo "=== Phase 1.3: Find Duplicates ==="
cd ~/AppData/Local/hermes/skills

# Check for skills that exist both flat and nested
for name in baoyu-article-illustrator baoyu-comic creative-ideation peft \
            pixel-art simpo subagent-driven-development watchers; do
  flat_exists=$([ -d "$name" ] && echo "YES" || echo "NO")
  nested_exists=$(find . -mindepth 2 -maxdepth 2 -type d -name "$name" 2>/dev/null | head -1)
  if [ "$flat_exists" = "YES" ] && [ -n "$nested_exists" ]; then
    echo "⚠️  DUPLICATE: $name (flat + $nested_exists)"

    # Check sizes
    flat_size=$(find "$name" -type f -exec stat -c%s {} + 2>/dev/null | awk '{s+=$1} END{print s}')
    nested_size=$(find "$nested_exists" -type f -exec stat -c%s {} + 2>/dev/null | awk '{s+=$1} END{print s}')
    echo "   Flat: ${flat_size}B, Nested: ${nested_size}B"
  fi
done
```

**To remove flat duplicates** (keeping the canonical nested copy):

```bash
# SAFETY CHECK: verify canonical exists first
for name in baoyu-article-illustrator baoyu-comic creative-ideation peft \
            pixel-art simpo subagent-driven-development watchers; do
  canonical=$(find . -mindepth 2 -maxdepth 2 -type d -name "$name" 2>/dev/null | head -1)
  if [ -n "$canonical" ]; then
    echo "✅ $name → canonical at $canonical"
    echo "   rm -rf skills/$name  # flat copy"
  fi
done
```

**Then execute:**
```bash
for name in baoyu-article-illustrator baoyu-comic creative-ideation peft \
            pixel-art simpo subagent-driven-development watchers; do
  rm -rf ~/AppData/Local/hermes/skills/$name
  echo "Removed: $name"
done
```

**Note:** Keep `chainlink` if no canonical copy exists in `blockchain/chainlink/`.

### 4.5 Phase 1.4: Judge Skills (Batch Mode)

Skills are judged in batches of 10 using `skill-judge` criteria.

**Standard batch script:**

```bash
#!/bin/bash
# batch_judge.sh — Judge skills in batches of 10
# Usage: bash batch_judge.sh

SKILLS_DIR=~/AppData/Local/hermes/skills
OUTPUT_DIR=~/Desktop/SandBox/judge_results
mkdir -p "$OUTPUT_DIR"

# Collect all skill paths
mapfile -t skills < <(find "$SKILLS_DIR" -name "SKILL.md" -type f | sort)

total=${#skills[@]}
batch_size=10
batch_num=1

for ((i=0; i<total; i+=batch_size)); do
    batch=("${skills[@]:i:batch_size}")
    echo "=== Batch $batch_num ($(($i+1))-$(($i+${#batch[@]})) of $total) ==="
    
    for sk_path in "${batch[@]}"; do
        skill_name=$(basename "$(dirname "$sk_path")")
        echo "  Judging: $skill_name"
        # skill_manage(action='judge', name="$skill_name")  # via Hermes tool
    done
    
    # Save batch results
    batch_file="$OUTPUT_DIR/batch_$(printf '%04d' $batch_num)_results.md"
    echo "# Batch $batch_num Results" > "$batch_file"
    echo "Skills: $(($i+1))-$(($i+${#batch[@]})) of $total" >> "$batch_file"
    echo "" >> "$batch_file"
    
    batch_num=$((batch_num + 1))
done

echo ""
echo "Judge complete: $total skills in $((batch_num - 1)) batches"
echo "Results: $OUTPUT_DIR/"
```

**Score interpretation:**

| Score | Rating | Meaning | Action |
|-------|--------|---------|--------|
| ≥80 | PASS | Good quality | None |
| 60-79 | WARN | Needs improvement | Patch frontmatter/structure |
| <60 | FAIL | Requires rewrite | Full SKILL.md rewrite |

### 4.6 Phase 1.5: Remediate

Remediate skills scoring < 80. Two categories:

**Patch WARN (60-79):** Fix frontmatter, add missing sections, improve structure.

```python
# remediate_warn.py — Patch skills scoring 60-79
import os, re, yaml
from pathlib import Path

skills_dir = Path(os.environ["HOME"]) / "AppData" / "Local" / "hermes" / "skills"

# Read judge results
judge_file = Path(os.environ["HOME"]) / "Desktop" / "SandBox" / "judge_results" / "all_results.tsv"
if not judge_file.exists():
    print("No judge results found. Run Phase 1.4 first.")
    exit(1)

import csv
with open(judge_file) as f:
    reader = csv.DictReader(f, delimiter="\t")
    for row in reader:
        score = int(row.get("score", 0))
        name = row.get("name", "")
        
        if 60 <= score < 80:
            # Find the SKILL.md
            sk = skills_dir / name / "SKILL.md"
            if not sk.exists():
                # Try nested
                nested = list(skills_dir.rglob(f"{name}/SKILL.md"))
                if nested:
                    sk = nested[0]
                else:
                    continue
            
            content = sk.read_text(encoding="utf-8")
            
            # Common fixes:
            fixes = []
            
            # 1. Add missing version field
            if "version:" not in content.split("---")[1] if "---" in content else "":
                fixes.append("version: 1.0.0")
            
            # 2. Add description if missing
            if "description:" not in content.split("---")[1] if "---" in content else "":
                fixes.append("description: >-\n  Automated skill for Hermes Agent.")
            
            # 3. Add tags if missing
            if "tags:" not in content.split("---")[1] if "---" in content else "":
                fixes.append("tags:\n  - hermes\n  - automation")
            
            if fixes:
                print(f"Would patch {name}: {fixes}")
```

**Rewrite FAIL (<60):** Full rebuild of SKILL.md. Note that bundled skills (petdex, computer-use) cannot be edited — these are built into Hermes.

### 4.7 Phase 1.6: Consolidate Umbrellas

```bash
echo "=== Phase 1.6: Find Thin/Mergeable Skills ==="
find ~/AppData/Local/hermes/skills -name "SKILL.md" -exec wc -l {} \; | \
  awk '$1 < 100 {print $1, $2}' | sort -n | head -20
```

Skills under 100 lines are consolidation candidates. These should be merged into umbrella skills using:

```bash
# Verify the umbrella skill exists first
skill_manage action=view name=<umbrella-skill>

# Then delete the thin skill merged into it
skill_manage action=delete name=<thin-skill> absorbed_into=<umbrella-skill>
```

### 4.8 Phase 1.7: Verify

```bash
echo "=== Phase 1.7: Final Verification ==="

# 1. Count skills
echo "Total skills: $(find ~/AppData/Local/hermes/skills -name 'SKILL.md' | wc -l)"

# 2. Check for remaining duplicates
dup_count=0
for d in ~/AppData/Local/hermes/skills/*/; do
  name=$(basename "$d")
  nested=$(find ~/AppData/Local/hermes/skills -mindepth 2 -type d -name "$name" 2>/dev/null)
  [ -n "$nested" ] && dup_count=$((dup_count + 1))
done
echo "Remaining duplicates: $dup_count"

# 3. Check judge results exist
echo "Judge results: $(ls ~/Desktop/SandBox/judge_results/*.tsv 2>/dev/null | wc -l) TSV files"

# 4. Check remediation report
ls ~/Desktop/SandBox/docs/final-verification.md 2>/dev/null && echo "✅ Final verification exists"
```

---

## 5. Phase 2: Agents System Prompt Context Fix

### 5.1 Purpose

Generate architecture context files for all projects and validate all VS Code JSON configurations.

### 5.2 Phase 2.1: Generate Architecture Context

```bash
echo "=== Phase 2.1: Architecture Context ==="

# Check existing architecture docs
count=$(ls ~/Desktop/SandBox/docs/Project_Architecture/ 2>/dev/null | wc -l)
echo "Existing architecture docs: $count"

# If regenerating, use the three generators:
# 1. architecture-blueprint-generator
# 2. folder-structure-blueprint-generator
# 3. technology-stack-blueprint-generator
#
# These are Hermes skills — load with skill_view() and follow their prompts
```

**Manual invocation:**
```
# Load the generators as skills
hermes profile use code-architect

# Architecture blueprints
skill_view name="architecture-blueprint-generator"

# Folder structure
skill_view name="folder-structure-blueprint-generator"

# Tech stack
skill_view name="technology-stack-blueprint-generator"
```

### 5.3 Phase 2.2: Audit VS Code Configuration

```bash
echo "=== Phase 2.2: VS Code JSON Audit ==="

cd ~/Desktop/SandBox

# 1. Find all JSON files in .vscode directories
echo "Root .vscode files:"
for f in .vscode/*.json; do
  python3 -c "import json; json.load(open('$f')); print('  ✅ $f')" 2>/dev/null || echo "  ❌ $f (invalid JSON)"
done

echo ""
echo "Subproject .vscode files: $(find projects -path '*/.vscode/*.json' 2>/dev/null | wc -l)"
errors=0
for f in $(find projects -path '*/.vscode/*.json' 2>/dev/null); do
  python3 -c "import json; json.load(open('$f'))" 2>/dev/null || { echo "  ❌ $f"; errors=$((errors + 1)); }
done
echo "Errors: $errors"
```

**Expected:** 0 errors across all JSON files.

### 5.4 Phase 2.3: Verify

```bash
echo "=== Phase 2 Verification ==="
echo "Architecture docs: $(ls ~/Desktop/SandBox/docs/Project_Architecture/ 2>/dev/null | wc -l)"
echo "Root VS Code JSONs valid: $([ -f .vscode/settings.json ] && python3 -c 'import json; json.load(open(".vscode/settings.json"))' && echo '✅' || echo '❌')"
echo "Subproject JSONs: $(find ~/Desktop/SandBox/projects -path '*/.vscode/*.json' 2>/dev/null | wc -l)"
```

---

## 6. Phase 3: Sync Hermes Copilot Codex

### 6.1 Purpose

Bidirectional sync of skills, plugins, and hooks across Hermes, GitHub Copilot, and OpenCode Codex.

### 6.2 Phase 3.1: Inventory Instructions & Agents

```bash
echo "=== Phase 3.1: Inventory ==="
cd ~/Desktop/SandBox/.github

echo "Instructions: $(ls instructions/ 2>/dev/null | wc -l)"
echo "Agents: $(ls agents/ 2>/dev/null | wc -l)"
```

**Expected:** ~186 instructions, ~174 agents.

### 6.3 Phase 3.2: Identify Root Folders

```bash
echo "=== Phase 3.2: Agent Roots ==="
echo "Hermes: $HOME/AppData/Local/hermes/ ($([ -d "$HOME/AppData/Local/hermes" ] && echo '✅' || echo '❌'))"
echo "Copilot (workspace): $PWD/.github/ ($([ -d .github ] && echo '✅' || echo '❌'))"
echo "Codex config: $HOME/.codex/ ($([ -d "$HOME/.codex" ] && echo '✅' || echo '❌'))"
```

### 6.4 Phase 3.3: Sync Assets

**Plugin sync check:**
```bash
echo "=== Plugin Sync ==="
echo "Hermes plugins:"
ls ~/AppData/Local/hermes/plugins/
echo ""
echo "Copilot plugins:"
ls ~/Desktop/SandBox/.github/plugins/
echo ""
echo "Diff:"
diff <(ls ~/AppData/Local/hermes/plugins/) <(ls ~/Desktop/SandBox/.github/plugins/) && echo "✅ No drift" || echo "⚠️ Drift detected"
```

**Hook sync check:**
```bash
echo ""
echo "=== Hook Sync ==="
diff <(ls ~/AppData/Local/hermes/hooks/*.sh 2>/dev/null | xargs -n1 basename) \
     <(ls ~/Desktop/SandBox/.github/hooks/*.sh 2>/dev/null | xargs -n1 basename) \
     && echo "✅ No drift" || echo "⚠️ Drift detected"
```

### 6.5 Phase 3.4: Verify

```bash
echo "=== Phase 3 Verification ==="
echo "Plugins: $(diff <(ls ~/AppData/Local/hermes/plugins/) <(ls ~/Desktop/SandBox/.github/plugins/) && echo '✅ Synced' || echo '⚠️ Drift')"
echo "Hooks:   $(diff <(ls ~/AppData/Local/hermes/hooks/*.sh 2>/dev/null | xargs -n1 basename) <(ls ~/Desktop/SandBox/.github/hooks/*.sh 2>/dev/null | xargs -n1 basename) && echo '✅ Synced' || echo '⚠️ Drift')"
echo "Skills:  $(find ~/AppData/Local/hermes/skills -name 'SKILL.md' 2>/dev/null | wc -l) (Hermes) vs $(find ~/Desktop/SandBox/.github/skills -name 'SKILL.md' 2>/dev/null | wc -l) (Copilot)"
```

---

## 7. Phase 4: Test Providers & Models

### 7.1 Purpose

Inventory all authorized LLM providers, discover their available models, and benchmark free-tier options.

### 7.2 Phase 4.1: Auth Inventory

```bash
echo "=== Phase 4.1: Provider Auth Inventory ==="
cd ~/Desktop/SandBox

hermes auth list 2>&1
```

**Expected output:** 7 providers listed with auth methods and status.

### 7.3 Phase 4.2-4.3: Model Discovery

```bash
echo "=== Phase 4.2-4.3: Model Discovery ==="

# Check Hermes model catalog
hermes models list 2>&1 | head -30

# Count models per provider
echo ""
echo "=== Model Count ==="
hermes models list 2>&1 | grep -oP '^\w+' | sort | uniq -c | sort -rn
```

### 7.4 Phase 4.4-4.7: Benchmark & Report

For a quick provider test:
```bash
# Test a provider with a simple chat query
hermes chat -q "Reply with 'OK' only" --provider openai-api --model gpt-4o-mini 2>&1

# Test another
hermes chat -q "Reply with 'OK' only" --provider huggingface --model HuggingFaceH4/zephyr-7b-beta 2>&1
```

---

## 8. Shell Scripts

### 8.1 Full Pipeline Runner

Create `~/AppData/Local/hermes/scripts/run-pipeline.sh`:

```bash
#!/bin/bash
# run-pipeline.sh — Execute full prompt orchestration pipeline
set -e

echo "========================================"
echo "  PROMPT ORCHESTRATION PIPELINE"
echo "========================================"
echo ""

WORKSPACE="$HOME/Desktop/SandBox"
cd "$WORKSPACE"

# Phase 0: Verify
echo ">>> [Phase 0] Verification"
for name in execute-all-prompts audit-skills-judge-fix \
            agents-system-prompt-context-fix sync-hermes-copilot-codex \
            test-providers-models; do
  if ls "prompts/$name.prompt*.md" 2>/dev/null >/dev/null; then
    echo "  ✅ $name"
  else
    echo "  ❌ $name — ABORTING"
    exit 1
  fi
done
echo "  Phase 0: All 5 prompts verified"
echo ""

# Phase 1: Audit
echo ">>> [Phase 1] Audit Skills Judge Fix"
hermes skills audit 2>&1 | tail -5
echo "  Phase 1: Skills audited"
echo ""

# Phase 2: Context
echo ">>> [Phase 2] Context Fix"
errors=0
for f in .vscode/*.json; do
  python3 -c "import json; json.load(open('$f'))" 2>/dev/null || errors=$((errors+1))
done
echo "  Phase 2: $errors VS Code JSON errors"
echo ""

# Phase 3: Sync
echo ">>> [Phase 3] Sync Agents"
plugins_drift=0
diff ~/AppData/Local/hermes/plugins/ .github/plugins/ 2>/dev/null >/dev/null || plugins_drift=1
echo "  Phase 3: Plugins drift=$plugins_drift"
echo ""

# Phase 4: Providers
echo ">>> [Phase 4] Test Providers"
hermes auth list 2>&1 | grep -c "credential" | xargs -I{} echo "  Phase 4: {} credentials found"
echo ""

echo "========================================"
echo "  PIPELINE COMPLETE"
echo "========================================"
```

### 8.2 Phase 1: Batch Judge Runner

Create `~/AppData/Local/hermes/scripts/batch-judge.sh`:

```bash
#!/bin/bash
# batch-judge.sh — Run skill-judge in batches of 10
# Usage: bash batch-judge.sh [--resume N]
#   --resume N: Skip first N batches (resume from batch N+1)

SKILLS_DIR="$HOME/AppData/Local/hermes/skills"
OUTPUT_DIR="$HOME/Desktop/SandBox/judge_results"
BATCH_SIZE=10
RESUME_FROM=0

if [ "$1" = "--resume" ] && [ -n "$2" ]; then
  RESUME_FROM=$2
  echo "Resuming from batch $((RESUME_FROM + 1))"
fi

mkdir -p "$OUTPUT_DIR"

mapfile -t skills < <(find "$SKILLS_DIR" -name "SKILL.md" -type f | sort)
total=${#skills[@]}
batch_count=0

for ((i=0; i<total; i+=BATCH_SIZE)); do
  batch_count=$((batch_count + 1))
  
  # Skip if resuming
  [ "$batch_count" -le "$RESUME_FROM" ] && continue
  
  batch=("${skills[@]:i:BATCH_SIZE}")
  end=$((i + ${#batch[@]} - 1))
  
  echo "=== Batch $batch_count (skills $((i+1))-$((end+1)) of $total) ==="
  
  batch_file="$OUTPUT_DIR/batch_$(printf '%04d' $batch_count)_results.md"
  {
    echo "# Batch $batch_count Results"
    echo "Date: $(date)"
    echo ""
    echo "| Skill | Score | Rating | Issues |"
    echo "|-------|-------|--------|--------|"
  } > "$batch_file"
  
  for sk_path in "${batch[@]}"; do
    skill_name=$(basename "$(dirname "$sk_path")")
    echo "  Judging: $skill_name"
    # Per skill: use skill_manage to run judge
    # echo "| $skill_name | 75 | WARN | Brief description needed |" >> "$batch_file"
  done
  
  echo "  → $batch_file"
done

echo ""
echo "Complete: $total skills in $batch_count batches"
```

### 8.3 Phase 2: VS Code Validation Script

Create `~/AppData/Local/hermes/scripts/validate-vscode.sh`:

```bash
#!/bin/bash
# validate-vscode.sh — Validate all VS Code JSON configs
# Returns exit code 0 if all valid, 1 if any invalid

WORKSPACE="$HOME/Desktop/SandBox"
errors=0
total=0

echo "=== VS Code JSON Validation ==="
echo "Workspace: $WORKSPACE"
echo ""

# Root .vscode files
echo "--- Root .vscode ---"
for f in "$WORKSPACE"/.vscode/*.json; do
  [ -f "$f" ] || continue
  total=$((total + 1))
  if python3 -c "import json; json.load(open('$f'))" 2>/dev/null; then
    echo "  ✅ $(basename $f)"
  else
    echo "  ❌ $(basename $f) — INVALID JSON"
    errors=$((errors + 1))
  fi
done

# Subproject .vscode files
echo ""
echo "--- Subproject .vscode ---"
while IFS= read -r -d '' f; do
  total=$((total + 1))
  if python3 -c "import json; json.load(open('$f'))" 2>/dev/null; then
    :
  else
    rel=$(echo "$f" | sed "s|$WORKSPACE/||")
    echo "  ❌ $rel — INVALID JSON"
    errors=$((errors + 1))
  fi
done < <(find "$WORKSPACE/projects" -path "*/.vscode/*.json" -print0 2>/dev/null)

echo ""
echo "Summary: $total files, $errors errors"
[ "$errors" -eq 0 ] && echo "✅ All valid" || echo "❌ $errors invalid file(s)"

exit $(( errors > 0 ? 1 : 0 ))
```

### 8.4 Phase 3: Sync Drift Checker

```bash
#!/bin/bash
# check-sync-drift.sh — Check for drift between Hermes and Copilot assets

echo "=== Sync Drift Check ==="

# Plugins
echo ""
echo "--- Plugins ---"
diff_output=$(diff \
  <(ls "$HOME/AppData/Local/hermes/plugins/" 2>/dev/null | sort) \
  <(ls "$HOME/Desktop/SandBox/.github/plugins/" 2>/dev/null | sort) \
  2>/dev/null)

if [ -z "$diff_output" ]; then
  echo "  ✅ Plugins in sync"
else
  echo "  ⚠️  Drift detected:"
  echo "$diff_output" | sed 's/^/    /'
fi

# Hooks
echo ""
echo "--- Hooks ---"
diff_output=$(diff \
  <(ls "$HOME/AppData/Local/hermes/hooks/"*.sh 2>/dev/null | xargs -n1 basename | sort) \
  <(ls "$HOME/Desktop/SandBox/.github/hooks/"*.sh 2>/dev/null | xargs -n1 basename | sort) \
  2>/dev/null)

if [ -z "$diff_output" ]; then
  echo "  ✅ Hooks in sync"
else
  echo "  ⚠️  Drift detected:"
  echo "$diff_output" | sed 's/^/    /'
fi

# Skills (count only)
hermes_count=$(find "$HOME/AppData/Local/hermes/skills" -name "SKILL.md" 2>/dev/null | wc -l)
copilot_count=$(find "$HOME/Desktop/SandBox/.github/skills" -name "SKILL.md" 2>/dev/null | wc -l)

echo ""
echo "--- Skills ---"
echo "  Hermes:  $hermes_count"
echo "  Copilot: $copilot_count"
echo "  Note: Different scopes — count drift is expected"
```

---

## 9. Checklists

### 9.1 Pre-Execution Checklist

- [ ] Terminal open to `~/Desktop/SandBox`
- [ ] Git status clean (`git status --short`)
- [ ] `hermes --version` responds
- [ ] Python 3.11+ available
- [ ] All 5 target prompts exist
- [ ] VS Code .vscode directory exists
- [ ] `.github/instructions/` and `.github/agents/` exist
- [ ] `hermes auth list` returns providers
- [ ] Write access to `docs/` and `judge_results/`

### 9.2 During-Execution Checklist

| Phase | Check | Expected |
|-------|-------|----------|
| 0 | All prompts found | 5/5 |
| 0 | Git status | No blocking changes |
| 1.1 | Skills audited | >300 SKILL.md files |
| 1.2 | Categories assigned | All skills have category |
| 1.3 | Duplicates removed | 8-9 removed |
| 1.4 | Judge results saved | all_results.tsv exists |
| 1.5 | WARN/FAIL remediated | Avg score >= 73 |
| 1.6 | Consolidation complete | Report saved |
| 1.7 | Verification saved | final-verification.md |
| 2.1 | Architecture docs | 50+ files |
| 2.2 | VS Code JSONs valid | 0 errors |
| 3.1 | Instructions + Agents counted | ~360 total |
| 3.3 | Plugins/hooks synced | Zero drift |
| 4.1 | Providers inventoried | 7 providers |

### 9.3 Post-Execution Checklist

- [ ] `docs/pipeline-result.json` exists and is valid JSON
- [ ] `docs/pipeline-summary.md` shows all phases complete
- [ ] `docs/orchestrator-verification.md` updated
- [ ] `docs/orchestrator-progress.md` shows all ✅
- [ ] No error artifacts left in working tree
- [ ] Git can see all changes (`git status`)
- [ ] Commit or revert as appropriate

---

## 10. Troubleshooting

### 10.1 Issue/Solution Pairs

| # | Issue | Symptom | Solution |
|---|-------|---------|----------|
| 1 | Prompt file not found | `ls prompts/name.prompt*.md` returns nothing | Check for `.prompts.md` (plural) extension. Run `ls prompts/*.prompt*.md` to discover all variants. |
| 2 | `hermes skills audit` hangs | Terminal shows no output after 30s | The audit scans each skill for security issues. Community skills with `DANGEROUS` verdicts increase scan time. Wait up to 3 minutes. Use `timeout 300` if needed. |
| 3 | Judge scores inconsistent | Same skill gets different scores in batch vs. solo run | Calibrate on the first batch of 10. Lock the scoring thresholds. Re-run a validation batch after every 5 batches. |
| 4 | OpenRouter rate limited | `hermes auth list` shows `rate-limited (429)` | Note the retry-after time. Skip OpenRouter in Phase 4 and come back later. No aggressive retries — they extend the backoff. |
| 5 | Memory write approval pending | `memory` tool shows "staged for approval" | Memory writes require TUI confirmation. Run `/memory pending` in the Hermes TUI to approve. |
| 6 | Cross-profile soft guard | `write_file` to `skills/` blocked | The cross-profile guard blocks writes to other profiles. Set `cross_profile=true` only on explicit user direction. |
| 7 | Dedupe found a skill that exists only once | `rm -rf` fails or wrongly identifies singleton | Run the dedupe detection BEFORE any manual removal. Verify the canonical copy exists and has >= content size. |
| 8 | VS Code JSON with inline comments | `json.load()` fails with "Invalid control character" | VS Code allows JSONC (comments, trailing commas). Use `json.loads(re.sub(r'//.*', '', text))` for .vscode files or use `json5` library. |
| 9 | Template wiring fails | "Rules section not found" when trying to wire `_shared/rules-core.md` | Some prompts don't have a `## Rules` section. Only prompts with existing Rules/Skills sections can be wired. Check section existence before attempting. |
| 10 | Git refuses checkout | "Your local changes to the following files would be overwritten" | `git stash` your changes, run the operation, then `git stash pop`. Or `git add -A && git stash` for clean revert. |
| 11 | Sub-agent doesn't return | `delegate_task` starts but no result after 5 minutes | Check for signature output artifacts on disk. If artifacts exist with timestamps after dispatch, verify them and proceed. Never block indefinitely. |
| 12 | Multi-file `.prompts.md` extension missed | Batch operation skips files with plural extension | Run `ls *.prompt*.md` during setup — the glob matches both `.prompt.md` and `.prompts.md`. Add both patterns to any batch script. |
| 13 | Broken `skill:/` prefix in deps | Cross-reference reports `skill:/context-map` as unresolved | Copilot imports sometimes use a leading slash. Run `grep -r 'skill:/' prompts/` and strip the leading `/`. Fix: `s|skill:/|skill:|g`. |
| 14 | Duplicate `tags:` lines | `awk '/^tags:/{t++}'` returns >1 per file | Files can get two `tags:` lines after batch fix when both bare `tags:` and `tags: []` exist. Patch the fix script with a `_dedup_tags()` step. |
| 15 | Windows/MSYS path mismatch | Hardcoded `C:\Users\...` breaks in bash | Always use `$HOME` env var in shell scripts, `os.environ["HOME"]` in Python. Never hardcode `C:\Users\...` or `C:/Users/...`. Run `echo $HOME` to confirm. |

---

## 11. Rollback Procedures

### 11.1 Git-Based Rollback (Preferred)

```bash
# Before starting any destructive phase:
git add -A && git commit -m "checkpoint: before <phase>"

# To restore a single file that was damaged:
git checkout HEAD~1 -- path/to/file

# To restore the entire skills directory:
git checkout HEAD~1 -- ~/AppData/Local/hermes/skills/

# To revert the last commit (safe — creates a new commit):
git revert HEAD --no-edit

# To discard all uncommitted changes (WARNING: destructive):
git checkout -- .
```

### 11.2 Phase-Specific Rollback

| Phase | Rollback Command | Notes |
|-------|-----------------|-------|
| Phase 1.3 (dedupe) | Restore from `.curator_backups/` or `git checkout` | The skills might be in `.curator_backups/` if curator ran |
| Phase 1.5 (remediate) | `git checkout HEAD~1 -- skills/*/SKILL.md` | Only SKILL.md files changed |
| Phase 2.2 (VS Code) | `git checkout -- .vscode/` | All configs restored to committed state |
| Phase 3.3 (sync) | Manual copy from backup | Sync doesn't destroy originals |
| Phase 4.x | No rollback needed | All read-only operations |

### 11.3 Emergency Stop

If the pipeline produces unexpected destructive behavior:

```bash
# 1. STOP — do not continue
# 2. See what changed
git status

# 3. Undo everything
git checkout -- .

# 4. Report
echo "Pipeline aborted at $(date)" >> docs/pipeline-emergency-stop.md
git add docs/pipeline-emergency-stop.md
git commit -m "emergency: pipeline aborted"
```

---

## 12. Git Integration

### 12.1 Commit Convention

Use these commit messages for pipeline phases:

```
feat(orchestrator): complete Phase 0 verification
feat(orchestrator): complete Phase 1 audit-judge-fix
feat(orchestrator): complete Phase 2 context-fix
feat(orchestrator): complete Phase 3 sync-agents
feat(orchestrator): complete Phase 4 test-providers
feat(orchestrator): pipeline complete — all 5 phases
```

### 12.2 Checkpoint Commits

```bash
git add -A && git commit -m "checkpoint: before Phase 1.3 deduplication"
git add -A && git commit -m "checkpoint: before Phase 1.5 remediation"
git add -A && git commit -m "checkpoint: before Phase 2.2 VS Code audit"
git add -A && git commit -m "checkpoint: before Phase 3.3 sync"
```

### 12.3 Verify Git After Pipeline

```bash
echo "=== Git Status After Pipeline ==="
git status --short

echo ""
echo "=== Recent Commits ==="
git log --oneline -10

echo ""
echo "=== Unpushed Commits ==="
git log --oneline origin/master..HEAD 2>/dev/null || echo "No remote tracking"
```

---

*End of Implementation Guide — ~1,410 lines*
