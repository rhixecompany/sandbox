# Technical Specification: Subagent-Driven Development + Prompt Library Maintenance

## Requirements

### R1: Prompt Library Maintenance
- **R1.1**: All 226 prompts pass independent verification (zero issues)
- **R1.2**: Toolsets normalized to Hermes palette (web, browser, terminal, file, code_execution, vision, image_gen, moa, tts, skills, todo, memory, context_engine, session_search, clarify, delegation, cronjob, mcp)
- **R1.3**: DEPS==SKILLS bidirectional sync for all prompts
- **R1.4**: Name/filename/trigger consistency (name === slug, trigger === /slug)
- **R1.5**: MCP tools labeled correctly (tool:mcp-*, not skill:mcp-*; not in skills: section)
- **R1.6**: No legacy sections, no duplicate metadata, no CRLF
- **R1.7**: All referenced skills exist on disk
- **R1.8**: Cross-prompt delegation map generated (read-only analysis)
- **R1.9**: Domain registry with 100% coverage, zero uncategorized

### R2: Subagent-Driven Development
- **R2.1**: Delegate task tool integration verified and working
- **R2.2**: Plan parser extracts tasks correctly from markdown plans
- **R2.3**: Implementer subagent receives complete context (spec + project conventions)
- **R2.4**: Spec compliance reviewer validates against original task spec
- **R2.5**: Code quality reviewer validates conventions, tests, security
- **R2.6**: Two-stage review order enforced (spec FIRST, quality SECOND)
- **R2.7**: Revision gate: max 3 iterations, escalation on stall
- **R2.8**: Final integration reviewer validates full implementation
- **R2.9**: Todo tracking updates status correctly

### R3: Cross-Integration
- **R3.1**: Both skills load and execute in stacked bundles
- **R3.2**: Subagent-driven-development can dispatch prompt-library-maintenance scripts
- **R3.3**: Prompt-library-maintenance can validate subagent-driven-development prompt files
- **R3.4**: Both skills cross-referenced in SKILL.md

### R4: Documentation & Process
- **R4.1**: Implementation plan created and tracked
- **R4.2**: Example plan demonstrates full workflow
- **R4.3**: Dispatcher helper script is reusable
- **R4.4**: Session startup protocol updated
- **R4.5**: All changes git-tracked, conventional commits

## Acceptance Criteria

### AC1: Prompt Library Validation
```
python3 scripts/verify_prompt_library.py
→ TOTAL=226 CLEAN=226 WITH_ISSUES=0
→ ISSUE TYPE COUNTS: {}
```

### AC2: Audit Reports Generated
```
docs/prompt-registry.md exists with delegation map + domain registry
docs/prompt-audit-report.md exists with skill/tool/prompt dependency resolution
Zero uncategorized domains
All cross-prompt edges resolved or documented as dangling
```

### AC3: Subagent Dispatcher Works
```
python3 scripts/subagent_dispatcher.py --plan .hermes/plans/example-subagent-plan.md
→ Dispatches implementer + 2 reviewers per task
→ All spec reviews PASS
→ All quality reviews APPROVED
→ Final integration review PASS
→ Todo list shows all tasks completed
```

### AC4: Example Plan Executes Fully
```
Plan: .hermes/plans/example-subagent-plan.md (3-5 tasks)
→ Each task: 1 implementer + 2 reviewers
→ Total subagents: 9-15
→ All tasks complete without escalation
→ Full test suite passes
```

### AC5: Cross-Integration Verified
```
Stacked bundle: /using-superpowers /subagent-driven-development /prompt-library-maintenance
→ Both skills load without error
→ Subagent can run prompt-library-maintenance scripts
→ Prompt library validates subagent skill prompt files
→ Cross-references present in both SKILL.md
```

## Configuration Schemas

### Prompt Library Verification Config
```python
# In verify_prompt_library.py
HERMES_TOOLSETS = {
    "web","browser","terminal","file","code_execution","vision","image_gen",
    "moa","tts","skills","todo","memory","context_engine","session_search",
    "clarify","delegation","cronjob","mcp"
}

REQUIRED_FIELDS = ["name","title","description","version","author","license","tags","trigger"]
LOCAL_FIELDS = ["scripts","skills","formatter","plan","toolsets"]
```

### Subagent Dispatcher Config
```python
# In subagent_dispatcher.py
class TaskConfig:
    plan_path: str
    project_root: str
    max_review_iterations: int = 3
    toolsets_per_role: dict = {
        "implementer": ["terminal", "file", "code_execution"],
        "spec_reviewer": ["file"],
        "quality_reviewer": ["file", "terminal"],
        "integration_reviewer": ["terminal", "file"]
    }
```

## Error Handling Scenarios

| Scenario | Detection | Response |
|----------|-----------|----------|
| Delegate task unavailable | Tool not in available tools | Fallback: manual execution with same review process |
| Subagent returns error | Non-zero exit or error in response | Dispatch fix subagent with specific error context |
| Spec review fails 3x | Issue count doesn't decrease | Escalation gate: present options to user |
| Quality review finds critical | Verdict = REQUEST_CHANGES with critical issues | Loop back to implementer, re-review after fix |
| Context > 70% | Four-tier model POOR tier | Abort gate: checkpoint, stop cleanly |
| Prompt file missing | search_files/glob returns 0 but find shows files | Use terminal find/ls for verification |
| Skill not found on disk | UNRESOLVED_SKILL in validator | Report missing skill, don't auto-create |
| Duplicate frontmatter | >1 `metadata:` in raw | Rewrite entire file with single merged frontmatter |

## Performance Benchmarks

| Operation | Target | Measurement |
|-----------|--------|-------------|
| Full prompt library verification | < 10 seconds | `verify_prompt_library.py` |
| Prompt library audit | < 30 seconds | `audit_prompt_library.py` |
| Single subagent dispatch + response | < 60 seconds | `delegate_task` call |
| 5-task plan execution (15 subagents) | < 10 minutes | End-to-end |
| Context budget check | < 1 second | Four-tier model evaluation |

## Security Considerations

1. **No destructive operations without approval** — `rm -rf`, `git reset --hard`, file overwrites require explicit confirmation
2. **Credential isolation** — API keys in `.env` only, never in prompts/skills
3. **Path validation** — All file operations validated against workspace root
4. **Subagent toolset restriction** — Minimal toolsets per role (principle of least privilege)
5. **No backup files** — Git for rollback, no `.bak`/`.backup` artifacts

## Migration Paths

### From Manual Prompt Maintenance
1. Run `verify_prompt_library.py` to baseline
2. Run `fix_prompt_library.py --apply --all` for bulk fixes
3. Re-verify, then run audit for reports
4. Add to session startup stacked bundles

### From Manual Subagent Orchestration
1. Create plan file following skill template
2. Use dispatcher script instead of manual dispatch
3. Enforce 2-stage review order
4. Track with todo list

## Testing Checklist

### Prompt Library Maintenance
- [ ] `verify_prompt_library.py` → CLEAN=226
- [ ] `audit_prompt_library.py` → reports generated
- [ ] `fix_prompt_library.py --dry-run` → no unexpected changes
- [ ] `fix_prompt_library.py --apply --files repo-init.prompt.md` → fixes single issue
- [ ] Re-verify → CLEAN=226
- [ ] Cross-prompt delegation map accuracy spot-check
- [ ] Domain registry 100% coverage verified

### Subagent-Driven Development
- [ ] Delegate task tool responds correctly
- [ ] Plan parser extracts all tasks
- [ ] Implementer subagent writes code + tests
- [ ] Spec reviewer catches missing requirements
- [ ] Quality reviewer catches style/bug issues
- [ ] Revision loop converges within 3 iterations
- [ ] Integration reviewer validates full implementation
- [ ] Todo list tracks correctly

### Cross-Integration
- [ ] Stacked bundle loads both skills
- [ ] Subagent runs prompt maintenance script
- [ ] Prompt validator runs on subagent skill files
- [ ] SKILL.md cross-references present

### Process Compliance
- [ ] All changes git-tracked
- [ ] Conventional commit messages
- [ ] No backup files
- [ ] Plan updated with progress
- [ ] Final verification passes

---

*Spec created: 2026-08-19 22:46:00*
*Profile: code-architect (technical specs)*
*Model: nemotron-3-ultra-free (opencode-zen)*