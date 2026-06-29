# Prompt Orchestration — Decision Trees

> Quick decision trees for common workflow choices during prompt orchestration execution.

---

## 1. Which Phase to Run?

```
Start
│
├── Is this the first execution?
│   ├── Yes → Phase 0 (Verification)
│   └── No  → Has Phase 0 passed before?
│       ├── Yes → Are all artifacts from previous run still fresh?
│       │   ├── Yes → Skip to the phase you need
│       │   └── No  → Has something changed (skills, files, config)?
│       │       ├── Yes → Re-run Phase 0 first
│       │       └── No  → Re-run the phase with stale artifacts
│       └── No  → Phase 0 (Verification)
│
After Phase 0 → Phase 1 (Audit Judge Fix)
After Phase 1 → Phase 2 (Context Fix)
After Phase 2 → Phase 3 (Sync Agents)
After Phase 3 → Phase 4 (Test Providers)
```

## 2. Prompt File Extension Resolution

```
ls prompts/<name>.prompt*.md
│
├── Found <name>.prompt.md?         (singular)
│   └── Yes → Use this file
│
├── Found <name>.prompts.md?        (plural — uncommon)
│   └── Yes → Use this file (note: check content format)
│
├── Found BOTH?
│   └── Both exist → Compare sizes, use the larger one, flag for deduplication
│
└── Found NEITHER?
    └── Not found → Check git: `git checkout HEAD -- prompts/<name>.prompt*.md`
```

## 3. Skill Deduplication Decision

```
Found skill with same name in 2 locations
│
├── Is canonical copy in a category subdirectory (e.g., skills/creative/skillname/)?
│   ├── Yes → Keep canonical, remove flat copy
│   └── No  → Is one copy clearly larger/better?
│       ├── Yes → Keep larger, remove smaller
│       └── No  → Compare: newer, more refs, better frontmatter → keep that one
│
└── Is the flat copy the ONLY copy?
    ├── Yes → Keep it (no deduplication needed)
    └── No  → Chainlink case: no canonical dir exists
        └── Keep it where it is
```

## 4. Judge Score Remediation Decision

```
Skill score < 80
│
├── Score < 60 (FAIL)
│   ├── Is this a bundled/builtin skill?
│   │   ├── Yes → Cannot edit. Note as "bundled — blocked"
│   │   └── No  → Full rewrite of SKILL.md
│   └── After rewrite → re-run judge (expect ≥60)
│
├── Score 60-79 (WARN)
│   ├── Missing frontmatter fields (name, title, version)?
│   │   ├── Yes → Patch frontmatter
│   │   └── No  → Check next
│   ├── Missing sections (description, rules, phases)?
│   │   ├── Yes → Add missing sections
│   │   └── No  → Check next
│   ├── Broken skill references?
│   │   ├── Yes → Fix refs (strip leading `/`, correct names)
│   │   └── No  → Check next
│   ├── Missing tags or categories?
│   │   ├── Yes → Add metadata and tags
│   │   └── No  → Improve prose/structure for clarity
│   └── After patch → re-run judge (expect ≥80 or improved)
│
└── Score ≥ 80 (PASS) → No action needed
```

## 5. Safety Gate Decision

```
Safety gate triggered
│
├── Verdict: PASS
│   └── Continue to next step
│
├── Verdict: WARN
│   ├── Is this a known/expected warning?
│   │   ├── Yes → Log it, continue
│   │   └── No  → Investigate before proceeding
│   └── After investigation → continue or escalate
│
└── Verdict: BLOCK
    ├── Can the issue be fixed immediately?
    │   ├── Yes → Fix, re-check gate
    │   └── No  → Stop pipeline, report issue
    └── Fix applied → re-check gate → PASS/WARN/BLOCK
```

## 6. Which Execution Mode to Use?

```
I need to run a prompt
│
├── Is it a single standalone prompt?
│   ├── Yes → Use delegate_task (preferred for standalone)
│   └── No  → Is it part of a 3+ sequential chain?
│       ├── Yes → Execute directly in main agent
│       │         (delegate_task can stall for long chains)
│       └── No  → Use delegate_task
│
└── After execution
    ├── Sub-agent returned? → Process result
    └── Sub-agent didn't return after 5 min?
        ├── Check for signature artifacts on disk
        │   ├── Artifacts exist with recent timestamp?
        │   │   ├── Yes → Verify and proceed
        │   │   └── No  → Re-delegate with simpler goal
        │   └── No artifacts → Re-delegate with simpler goal
        └── Never block indefinitely
```

## 7. Phase 4 Provider Selection

```
I need to test a provider
│
├── Check auth status: `hermes auth list`
│
├── Status = "active"
│   ├── Test basic chat
│   ├── Query model list
│   └── Run benchmark
│
├── Status = "rate_limited (429)"
│   ├── Note the retry-after time
│   ├── Skip this provider for now
│   └── Schedule a cron job for retry
│
├── Status = "exhausted" (OAuth)
│   ├── Check remaining lockout time
│   ├── Wait or skip
│   └── Re-authenticate if needed
│
└── Status = "missing_auth"
    └── Configure provider: `hermes config set providers.<name>.api_key`
```

## 8. Rollback Decision

```
Something went wrong
│
├── Is it a single file that was corrupted?
│   ├── Yes → `git checkout HEAD -- path/to/file`
│   └── No  → Was it a whole phase?
│       ├── Yes → `git revert <phase-commit>`
│       └── No  → Check next
│
├── Multiple files changed and it's all wrong?
│   ├── `git checkout -- .` (discard all working tree changes)
│   └── `git reset --hard HEAD` (nuclear — discard all, even staged)
│
├── Skills have been deleted?
│   ├── Check `.curator_backups/` in skills dir
│   ├── Or `git checkout HEAD~1 -- ~/AppData/Local/hermes/skills/`
│   └── Last resort: re-run `hermes skills update` to re-download
│
└── Always report what happened after any rollback:
    `echo "Rolled back: <reason>" >> docs/pipeline-rollback-log.md`
```

## 9. JSON Validation Failure Decision

```
JSON file failed validation
│
├── Is it a VS Code .vscode JSON (settings, tasks, launch)?
│   ├── VS Code allows trailing commas and comments (JSONC).
│   ├── Try: `python3 -c "import json5; json5.load(open('$f'))"`
│   └── If still fails → read the file, fix the syntax error manually
│
├── Is it an MCP JSON?
│   ├── MCP configs are strict JSON. No trailing commas.
│   └── Fix: remove trailing commas, close all brackets
│
└── Is it a machine-generated JSON (e.g., pipeline result)?
    └── Check encoding: `file --mime-encoding file.json`
        ├── UTF-8 → JSON parse error → regenerate
        └── Not UTF-8 → `iconv -f UTF-16 -t UTF-8 file.json > file-fixed.json`
```

---

## Summary Decision: Is the Pipeline Complete?

```
All 5 phases attempted
│
├── Phase 0 passed? → (yes/no)
├── Phase 1 passed? → (yes/no)
├── Phase 2 passed? → (yes/no)
├── Phase 3 passed? → (yes/no)
└── Phase 4 passed? → (yes/no)
│
├── All ✅ → Pipeline COMPLETE
├── Any ❌ → Pipeline FAILED — check the failing phase
└── Phase 0 ❌ → Pipeline BLOCKED — fix prerequisites first
```
