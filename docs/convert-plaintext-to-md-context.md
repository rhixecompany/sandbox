# convert-plaintext-to-md — Context Catalog

Generated: 2026-05-25 Audit Phase: 1 (Catalog & Dependency Scan)

Source file: `.github/prompts/convert-plaintext-to-md.prompt.md`

## Summary

A prompt for converting plaintext documentation files into properly formatted markdown with support for optional parameters, reference guides, and predefined transformation instructions. Hermes-compatible frontmatter with `trigger: /convert-plaintext-to-md`, structured into 4 execution phases with clear inputs, outputs, rules, and a parameters table.

## Purpose Slug Resolution

✅ Resolved: `convert-plaintext-to-md`

## Forward References (this file → others)

### External URLs
| Type | Reference | URL | Status |
| ---- | --------- | --- | ------ |
| URL | GitHub Markdown Syntax | https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax | External / Live |
| URL | Markdown Guide Extended Syntax | https://www.markdownguide.org/extended-syntax/ | External / Live |
| URL | Azure DevOps Markdown Guidance | https://learn.microsoft.com/en-us/azure/devops/project/wiki/markdown-guidance | External / Live |

### Skills Referenced
| Skill Name | Purpose | Path | Exists? |
| ---------- | ------- | ---- | ------- |
| writing-plans | Structured conversion plan for complex documents | .opencode/skills/writing-plans/ | ✅ Yes |
| simplify | Ensure output is concise and non-redundant | .opencode/skills/simplify/ | ✅ Yes |

### Plan/Spec Namespaces Referenced
None found in frontmatter or body.

### @agent references
None found.

### Trigger Namespaces
- `/convert-plaintext-to-md` (defined in frontmatter, line 2)

## Reverse References (others → this file)

### Direct Path References
| Source File | Type | Context | Line/Section |
| ----------- | ---- | ------- | ------------ |
| docs/convert-plaintext-to-md-context.md | Context Catalog | Self-referential (previous audit output) | N/A |
| docs/convert-plaintext-to-md-fix-issues-context.md | Fix Progress Log | References this prompt for remediation tracking | N/A |
| docs/convert-plaintext-to-md-issues-context.md | Issues Catalog | References this prompt for audit results | N/A |
| docs/convert-plaintext-to-md-verify-context.md | Verification Report | References this prompt for verification | N/A |

### Trigger References
None found via grep for `/convert-plaintext-to-md` outside of the prompt file itself and its audit artifacts.

### Cross-Repository References
| Source File | Type | Context |
| ----------- | ---- | ------- |
| Rhixe-company/comicwise/.references/awesome-copilot/docs/README.prompts.md | Reference Index | External copy / archived reference |
| Rhixe-company/comicwise/.references/awesome-copilot/prompts/convert-plaintext-to-md.prompt.md | Prompt Copy | External copy / archived reference |
| Rhixe-company/comicwise/.references/comicr/.github/prompts/convert-plaintext-to-md.prompt.md | Prompt Copy | External copy / archived reference |
| Rhixe-company/comicwise/.references/comicwise/prompts/convert-plaintext-to-md.prompt.md | Prompt Copy | External copy / archived reference |

**Note:** All Rhixe-company references are archived/external and not part of active workspace dependency chain.

## Plan System Integration

Plugin system unavailable — context provided by markdown audit only.

Companion debugging plan: `thoughts/plans/convert-plaintext-to-md-debug.md` (exists)

## File Inventory (all files in conversion chain)

### Primary Audit Target
| # | Path | Type | Format | Lines | Status |
| --- | ---- | ---- | ------ | ----- | ------ |
| 1 | .github/prompts/convert-plaintext-to-md.prompt.md | Prompt | Markdown + YAML frontmatter | 117 | ✅ Audit Complete |

### Related Audit Artifacts (Generated)
| # | Path | Type | Generated Date | Purpose |
| --- | ---- | ---- | -------------- | ------- |
| 2 | docs/convert-plaintext-to-md-context.md | Context Catalog | 2026-05-25 | Dependency & reference mapping |
| 3 | docs/convert-plaintext-to-md-issues-context.md | Issues Catalog | 2026-05-25 | Formatting/content/structural issues |
| 4 | docs/convert-plaintext-to-md-verify-context.md | Verification Report | 2026-05-25 (previous) | Previous audit verification |
| 5 | docs/convert-plaintext-to-md-fix-issues-context.md | Fix Progress Log | 2026-05-25 (previous) | Previous fix attempt log |

### Helper Plans (Discovered)
| # | Path | Type | Referenced In |
| --- | ---- | ---- | ------------- |
| 6 | thoughts/plans/convert-plaintext-to-md-debug.md | Markdown Plan | convert-plaintext-to-md-fix-issues-context.md |

## Structural Map

```
.github/prompts/convert-plaintext-to-md.prompt.md
├── YAML Frontmatter (lines 1-7)
│   ├── trigger: /convert-plaintext-to-md
│   ├── description: (multi-line)
│   └── tags: [hermes, copilot, opencode, markdown, conversion, documentation]
│
├── # Heading (line 9)
│   └── > Quote/intro (line 11)
│
├── ## Goal (line 13)
├── ## Context (line 17)
├── ## Inputs (line 21)
├── ## Outputs (line 28)
├── ## Rules (line 33)
├── ## Skills Required (line 44) [TABLE]
├── ## Phases (line 51)
│   ├── ### Phase 1: Intake (line 53)
│   ├── ### Phase 2: Execute (line 62)
│   ├── ### Phase 3: Verify (line 72)
│   └── ### Phase 4: Hand off (line 82)
├── ## Parameters (line 90) [TABLE]
├── ## Predefined Instructions (line 103) [TABLE]
└── ## Reference (line 113) [LINKS]
```

## Dependencies Summary

**Skills Used:** 2
- `writing-plans` (exists)
- `simplify` (exists)

**External URLs:** 3
- GitHub (docs.github.com) ✅
- MarkdownGuide.org ✅
- Microsoft Azure DevOps ✅

**Triggers:** 1
- `/convert-plaintext-to-md`

**Cross-references within workspace:** 4 artifact files (self-referential from previous audits)

**Reverse references:** None (no other active files reference this prompt via trigger or link)

---

**Audit Date:** 2026-05-25
**Audit Scope:** Frontmatter, external refs, skill dependencies, trigger definitions, cross-file refs
**Status:** ✅ Complete
