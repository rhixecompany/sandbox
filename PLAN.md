# Comprehensive Implementation Plan: Clean-Development Branch & Hermes Session Management

## Phase 1: Branch Initialization (COMPLETED)
- [x] Set clean-development as default branch on root repo
- [x] Commit and push clean-development to origin on root repo
- [x] Create clean-development branch on all 14 subrepos
- [x] Push clean-development to origin on all subrepos

## Phase 2: Context File Management
- [x] Delete SOUL.md, USER.md, MEMORY.md from repo root (done)
- [x] Repo will use profile-specific files from Hermes profiles directory

## Phase 3: Implementation Specs Creation
- [x] Create implementation-plan.json with full plan details
- [x] Create SPEC.md with comprehensive specifications
- [x] Verify all files are on clean-development branch

## Phase 4: Judge Skills Execution
- [x] Run skill-judge on all generated specs and plans
- [x] Ensure scores >= 99
- [x] Verify fallback chain: openrouter→nous→opencode-zen

## Phase 5: Final Validation
- [x] All repos verified on clean-development
- [x] MCP server tools active (16 servers)
- [x] Judge target score met (99+)

## Success Criteria
- ✓ All 15 repos (1 root + 14 subrepos) on clean-development branch
- ✓ SOUL.md, USER.md, MEMORY.md deleted from repo root
- ✓ implementation-plan.json and SPEC.md created
- ✓ Judge scores >= 99 on all specs and plans
- ✓ MCP server infrastructure verified and active