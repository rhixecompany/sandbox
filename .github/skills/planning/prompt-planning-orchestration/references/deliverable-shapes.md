# Deliverable Shapes — prompt-planning-orchestration

## PRIMARY OUTPUTS (4 files, ~3,500 lines)

1. **Comprehensive Plan** (~25 KB, 800-900 lines)
   - Location: `plan/` directory
   - Filename: `{workflow-name}-comprehensive-plan.md`
   - Content: Full specification with 6+ sections

2. **Code Samples** (~25 KB, 700-800 lines)
   - Location: `docs/` directory
   - Filename: `{workflow-name}-code-samples.py`
   - Content: Production-ready implementation

3. **Implementation Guide** (~32 KB, 1,200-1,400 lines)
   - Location: `docs/` directory
   - Filename: `{workflow-name}-implementation-guide.md`
   - Content: Step-by-step execution with scripts

4. **Supporting Docs** (2-3 files)
   - Location: `docs/` directory
   - Examples: execution-summary.md, index.md, navigation.md
   - Content: Quick refs, decision trees, file relationships

## SUPPORT FILES (optional, created during execution)

- `references/{detail}.md` — Phase-specific context, workarounds, pitfalls
- `templates/{scaffold}.md` — Starter files to copy and modify
- `scripts/{name}.sh` — Automation scripts created during guide phase

## Quality Checkpoints

### Plan Acceptance Criteria
- ✅ All phases specified (typically 6-8 phases for complex workflows)
- ✅ Each phase has input, process, output explicitly stated
- ✅ Success criteria defined per phase
- ✅ Safety/validation gates documented
- ✅ Rollback procedures for destructive operations
- ✅ Timeline realistic and detailed (2.5 hours typical for 6-phase)
- ✅ 800+ lines (sufficient detail, not hand-wavy)

### Code Acceptance Criteria
- ✅ One class per phase minimum
- ✅ Full type hints (Python 3.11+ syntax)
- ✅ Error handling (try/except, validation, clear messages)
- ✅ Data structures for inputs/outputs (dataclass, Dict, etc.)
- ✅ JSON serialization where relevant
- ✅ ~700-850 lines (substantive, not skeleton)
- ✅ Example invocation at module bottom

### Guide Acceptance Criteria
- ✅ Quick start section (5-15 minute entry point)
- ✅ Step-by-step tutorial for each phase
- ✅ Shell scripts provided and embedded (not just described)
- ✅ Pre/during/post execution checklists
- ✅ Troubleshooting section (6+ issue/solution pairs)
- ✅ Rollback procedures documented
- ✅ 1,200+ lines (comprehensive, not terse)
- ✅ Git integration points noted
