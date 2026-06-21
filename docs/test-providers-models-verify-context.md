# test-providers-models — Verification Report

> Generated: 2026-06-21 | Fresh rewrite — comprehensive provider benchmark
> Source: `test-providers-models.prompt.md` (Phase: 4 — Verify)

## Verification Gates

| Gate | Status |
|------|--------|
| Frontmatter parses as single YAML document | ✅ |
| Zero double-fence repeats in first 60 lines | ✅ (2 fences, correct) |
| Clean `skills:` list (identifiers only, no prose) | ✅ |
| Skills Required table matches frontmatter | ✅ |
| Trigger matches filename stem (`test-providers-models`) | ✅ |
| 6 providers from `hermes auth list` included | ✅ |
| All 7 phases (0-6) included with tier labels | ✅ |
| All dimensions covered (Profile, Persona, Tools, Skills, Scripts, Steps, Tasks, Actions) | ✅ |

## Content Coverage

| Dimension | Status | Details |
|-----------|--------|---------|
| **Providers** | ✅ All 6 | copilot, huggingface, nous, ollama-cloud, openai-api, openrouter |
| **Phases** | ✅ 7 phases | 0-6 with Needed/Recommended/Optional tiers |
| **Tiers** | ✅ 3 tiers | ✓ Needed (Phases 0-2), ☆ Recommended (Phases 3,4,6), ◇ Optional (Phase 5) |
| **Profiles** | ✅ Per phase | default, research-analyst, code-architect, adminbot |
| **Personas** | ✅ Per phase | OWL, System Admin, Research Analyst, Tech Lead, QA Engineer, DevOps, Developer |
| **Skills** | ✅ Needed + Recommended | 4 core + 2 supplementary |
| **Tools (MCP + CLI)** | ✅ Per phase | hermes CLI, terminal, fetch, execute_code, memory |
| **Scripts** | ✅ Phase 6 | `test_models.py` spec with CLI interface requirements |
| **Verification** | ✅ Per phase | Per-phase checklists + final verification checklist |

## Change Summary

| Aspect | Before (old) | After (new) |
|--------|-------------|-------------|
| Providers covered | 1 (openrouter only) | 6 (all from `hermes auth list`) |
| Phases | 4 (1-4) | 7 (0-6) with tier system |
| Skills listed | 3 | 6 (4 core + 2 recommended) |
| Profiles/personas | None specified | Per-phase profile + persona |
| Tools | Implicit | Explicit per-phase tool tables |
| Scripts | Referenced only | Full spec + CLI interface design |
| Verification | Single checklist | Per-phase + final checklist |
| Total lines | 154 | 468 |

## Assessment

The prompt is now a comprehensive, multi-provider benchmark specification
that covers all 6 authorized Hermes providers with 7 categorized phases,
per-phase profile/persona assignment, explicit tool and skill references,
and thorough verification gates. No further structural enhancements needed.
