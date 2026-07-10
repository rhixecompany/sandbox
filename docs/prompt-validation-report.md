# Prompt Validation Report

- Files checked: 215
- Files with failures: 211
- Missing dependencies: 3551
- Broken references: 3209
- Fixed items: 0

## Failures by category

### frontmatter

- None

### dependencies

- `prompts\add-educational-comments.prompt.md`
  - Missing inline ref: Line Number Referencing = yes
  - Missing inline ref: Note <number>
  - Missing inline ref: Note 1
  - Missing inline ref: Repetitiveness
  - Missing inline ref: Line Number Referencing = yes
  - Missing inline ref: Please provide a file or files to add educational comments to. Preferably as chat variable or attached context.
  - Missing inline ref: Line Numer
  - Missing inline ref: 1-3
  - Missing inline ref: ordered
  - Missing inline ref: templates/add-educational-comments/configuration_reference.md
  - Missing inline ref: text
[user]

> /add-educational-comments
[agent]
> Please provide a file or files to add educational comments to. Preferably as chat variable or attached context.

- Missing inline ref:

### Custom Configuration

- Missing inline ref:

Interpret

- Missing inline ref:  as
- Missing inline ref:  and adjust behavior accordingly while maintaining all rules above.

## Final Checklist

- Ensure the transformed file satisfies the 125% rule without exceeding limits.
- Keep encoding, end-of-line style, and indentation unchanged.
- Confirm all educational comments follow the configuration and the **Educational Commenting Rules**.
- Provide clarifying suggestions only when they aid learning.
- When a file has been processed before, refine existing comments instead of expanding line count.

## Template References

Detailed templates in

- `prompts\agents-fix.prompt.md`
  - Missing skill: brainstorming
  - Missing skill: plans-and-specs
  - Missing skill: dispatching-parallel-agents
  - Missing skill: subagent-driven-development
  - Missing skill: systematic-debugging
  - Missing skill: simplify
  - Missing skill: acpx-executor
  - Missing skill: copilot-cli-quickstart
  - Missing reference: introspection-only-general
  - Missing reference: no-git-delete
  - Missing reference: no-net-fetch
  - Missing reference: skills-tools-preflight-check
  - Missing reference: brainstorming
  - Missing reference: plans-and-specs
  - Missing reference: dispatching-parallel-agents
  - Missing reference: subagent-driven-development
  - Missing reference: systematic-debugging
  - Missing reference: simplify
  - Missing reference: acpx-executor
  - Missing reference: copilot-cli-quickstart
  - Missing inline ref: search_files(pattern="*.md", target="files")
  - Missing inline ref: read_file(path)
  - Missing inline ref: patch(path, old_string, new_string)
  - Missing inline ref: write_file(path, content)
  - Missing inline ref: delegate_task(goal, toolsets)
  - Missing inline ref: skill_view(name="acpx-executor")
- `prompts\agents-generator.prompt.md`
  - Missing inline ref: AGENTS.md
  - Missing inline ref: big picture
  - Missing inline ref: why
  - Missing inline ref: **/{.github/copilot-instructions.md,AGENT.md,AGENTS.md,CLAUDE.md,.cursorrules,.windsurfrules,.clinerules,.cursor/rules/**,.windsurf/rules/**,.clinerules/**,README.md}
  - Missing inline ref: AGENTS.md
  - Missing inline ref: write tests
  - Missing inline ref: handle errors
  - Missing inline ref: <file>
  - Missing inline ref: src/scripts/*.ts
  - Missing inline ref: ./*.ps1
  - Missing inline ref: ./*.sh
  - Missing inline ref: AGENTS.md
- `prompts\agents-system-prompt-context-fix.prompt.md`
  - Missing skill: using-superpowers
  - Missing skill: user-communication-preferences
  - Missing skill: plans-and-specs
  - Missing skill: architecture-blueprint-generator
  - Missing skill: folder-structure-blueprint-generator
  - Missing skill: technology-stack-blueprint-generator
  - Missing skill: vscode-workspace-configurator
  - Missing reference: using-superpowers
  - Missing reference: user-communication-preferences
  - Missing reference: plans-and-specs
  - Missing reference: architecture-blueprint-generator
  - Missing reference: folder-structure-blueprint-generator
  - Missing reference: technology-stack-blueprint-generator
  - Missing reference: vscode-workspace-configurator
  - Missing inline ref: AGENTS.md
  - Missing inline ref: .prompt.md
  - Missing inline ref: $HOME/Desktop/SandBox
  - Missing inline ref: architecture-blueprint-generator
  - Missing inline ref: folder-structure-blueprint-generator
  - Missing inline ref: technology-stack-blueprint-generator
  - Missing inline ref: .vscode
  - Missing inline ref: .vscode/
  - Missing inline ref: AGENTS.md
  - Missing inline ref: phases.md
- `prompts\ai-prompt-engineering-safety-review.prompt.md`
  - Missing skill: prompt-engineering
  - Missing skill: systematic-debugging
  - Missing skill: context-map
  - Missing reference: prompt-engineering
  - Missing reference: systematic-debugging
  - Missing inline ref: context-map
  - Missing inline ref: prompt-engineering
  - Missing inline ref: systematic-debugging
  - Missing inline ref: templates/ai-prompt-engineering-safety-review/phases.md
  - Missing inline ref: templates/ai-prompt-engineering-safety-review/
  - Missing inline ref: phases.md
- `prompts\apple-appstore-reviewer.prompt.md`
  - Missing inline ref: templates/apple-appstore-reviewer/inputs_you_should_look_for.md
  - Missing inline ref: templates/apple-appstore-reviewer/review_method_follow_this_orde.md
  - Missing inline ref: templates/apple-appstore-reviewer/output_requirements_your_repor.md
  - Missing inline ref: templates/apple-appstore-reviewer/common_rejection_hotspots_use_.md
  - Missing inline ref: templates/apple-appstore-reviewer/
  - Missing inline ref: inputs_you_should_look_for.md
  - Missing inline ref: output_requirements__your_repo.md
  - Missing inline ref: common_rejection_hotspots__use.md
- `prompts\arch-linux-triage.prompt.md`
  - Missing inline ref: systemctl
  - Missing inline ref: journalctl
  - Missing inline ref: pacman
  - Missing inline ref: templates/arch-linux-triage/
  - Missing inline ref: inputs.md
  - Missing inline ref: instructions.md
  - Missing inline ref: output_format.md
- `prompts\architecture-blueprint-generator.prompt.md`
  - Missing inline ref: templates/architecture-blueprint-generator/generated_prompt.md
  - Missing inline ref: templates/architecture-blueprint-generator/
  - Missing inline ref: generated_prompt.md
- `prompts\aspnet-minimal-api-openapi.prompt.md`
  - Missing inline ref: MapGroup()
  - Missing inline ref: [Required]
  - Missing inline ref: Results<T1, T2>
  - Missing inline ref: TypedResults
  - Missing inline ref: Results
  - Missing inline ref: WithName
  - Missing inline ref: [Description()]
  - Missing inline ref: templates/aspnet-minimal-api-openapi/
  - Missing inline ref: api_organization.md
  - Missing inline ref: openapi_documentation.md
  - Missing inline ref: request_and_response_type.md
  - Missing inline ref: type_handling.md
- `prompts\audit-skills-judge-fix.prompt.md`
  - Missing skill: using-superpowers
  - Missing skill: user-communication-preferences
  - Missing skill: plans-and-specs
  - Missing skill: skill-judge
  - Missing skill: hermes-skills
  - Missing skill: skill-creator
  - Missing skill: writing-skills
  - Missing reference: using-superpowers
  - Missing reference: user-communication-preferences
  - Missing reference: plans-and-specs
  - Missing reference: skill-judge
  - Missing reference: hermes-skills
  - Missing reference: skill-creator
  - Missing reference: writing-skills
  - Missing inline ref: hermes skills audit
  - Missing inline ref: skill_manage(action='delete', absorbed_into=...)
  - Missing inline ref: ~/AppData/Local/hermes/scripts/
  - Missing inline ref: .prompt.md
  - Missing inline ref: ~/AppData/Local/hermes/skills/
  - Missing inline ref: docs/local-skills.md
  - Missing inline ref: docs/categorization-plan.md
  - Missing inline ref: docs/dedupe-report.md
  - Missing inline ref: judge_results/all_results.tsv
  - Missing inline ref: judge_results/summary.md
  - Missing inline ref: judge_results/remediation_report.md
  - Missing inline ref: docs/consolidation-report.md
  - Missing inline ref: docs/final-verification.md
  - Missing inline ref: using-superpowers
  - Missing inline ref: user-communication-preferences
  - Missing inline ref: plans-and-specs
  - Missing inline ref: skill-judge
  - Missing inline ref: hermes-skills
  - Missing inline ref: skill-creator
  - Missing inline ref: writing-skills
  - Missing inline ref: ~/AppData/Local/hermes/scripts/
  - Missing inline ref: docs/local-skills.md
  - Missing inline ref: docs/dedupe-report.md
  - Missing inline ref: judge_results/all_results.tsv
  - Missing inline ref: docs/consolidation-report.md
  - Missing inline ref: docs/final-verification.md
  - Missing inline ref: ~/AppData/Local/hermes/scripts/
  - Missing inline ref: batch_skill_judge.py
  - Missing inline ref: batch_remediate.py
  - Missing inline ref: batch_remediate_42_59.py
  - Missing inline ref: batch_rewrite_worst.py
  - Missing inline ref: dedupe_skills.py
  - Missing inline ref: consolidate_skills.py
  - Missing inline ref: merge_skill.py
  - Missing inline ref: audit_prompts.py
  - Missing inline ref: skill_inventory.json
  - Missing inline ref: skill_name_to_path.json
  - Missing inline ref: judge_results/
  - Missing inline ref: SESSION_REPORT.md
  - Missing inline ref: skill_view()
  - Missing inline ref: skill_manage()
  - Missing inline ref: default
  - Missing inline ref: write_file
  - Missing inline ref: patch
  - Missing inline ref: absorbed_into
  - Missing inline ref: read_file(path)
  - Missing inline ref: old_string
  - Missing inline ref: os.environ["HOME"]
  - Missing inline ref: os.environ["USERPROFILE"]
  - Missing inline ref: phases.md
- `prompts\az-cost-optimize.prompt.md`
  - Missing inline ref: azmcp-*
  - Missing inline ref: templates/az-cost-optimize/workflow_steps.md
  - Missing inline ref: templates/az-cost-optimize/cost_optimization_brief_title.md
  - Missing inline ref:

  - Missing inline ref:

  - Missing inline ref:
-
- `prompts\azure-resource-health-diagnose.prompt.md`
  - Missing inline ref: azmcp-*
  - Missing inline ref: templates/azure-resource-health-diagnose/workflow_steps.md
  - Missing inline ref: bash

  # Critical fixes to restore service

   [Azure CLI commands with explanations]

  - Missing inline ref:

  - Missing inline ref: bash

  # Performance and reliability improvements

   [Azure CLI commands with explanations]

  - Missing inline ref: bash

  # Architectural and preventive measures

   [Azure CLI commands and configuration changes]

  - Missing inline ref:

- `prompts\bash-scripts-fix.prompt.md`
  - Missing skill: brainstorming
  - Missing skill: plans-and-specs
  - Missing skill: dispatching-parallel-agents
  - Missing skill: subagent-driven-development
  - Missing skill: systematic-debugging
  - Missing skill: simplify
  - Missing skill: acpx-executor
  - Missing skill: script-orchestration
  - Missing reference: introspection-only-general
  - Missing reference: no-git-delete
  - Missing reference: no-net-fetch
  - Missing reference: skills-tools-preflight-check
  - Missing reference: brainstorming
  - Missing reference: plans-and-specs
  - Missing reference: dispatching-parallel-agents
  - Missing reference: subagent-driven-development
  - Missing reference: systematic-debugging
  - Missing reference: simplify
  - Missing reference: acpx-executor
  - Missing reference: script-orchestration
  - Missing inline ref: projects/Bash/**
  - Missing inline ref: Bash/**
  - Missing inline ref: docs/bash-scripts-fix-review-findings.md
  - Missing inline ref: docs/prompt-verify-context.md
  - Missing inline ref: docs/bash-scripts-fix-review-findings.md
  - Missing inline ref: .sh
  - Missing inline ref: .ps1
  - Missing inline ref: .bat
  - Missing inline ref: .ts
  - Missing inline ref: search_files(pattern="*.sh", target="files")
  - Missing inline ref: search_files(pattern="*.ps1", target="files")
  - Missing inline ref: search_files(pattern="*.bat", target="files")
  - Missing inline ref: terminal("bash -n <script>")
  - Missing inline ref: terminal("pwsh -NoProfile -Command ...")
  - Missing inline ref: write_file(path, content)
  - Missing inline ref: patch(path, old_string, new_string)
  - Missing inline ref: delegate_task(goal, toolsets)
  - Missing inline ref: skill_view(name="acpx-executor")
  - Missing inline ref: _archive/bash-scripts-fix.prompts.txt
  - Missing inline ref: _archive/bash-scripts-fix.prompts.txt
  - Missing inline ref: docs/bash-scripts-list-context.md
  - Missing inline ref: projects/Bash/upgrade.sh
  - Missing inline ref: projects/Bash/Banking/scripts/orchestrator.sh/.bat/.ps1
  - Missing inline ref: projects/Bash/comicwise/dev.sh/.ps1
- `prompts\bigquery-pipeline-audit.prompt.md`
  - Missing inline ref: client.query
  - Missing inline ref: load_table_from_*
  - Missing inline ref: extract_table
  - Missing inline ref: copy_table
  - Missing inline ref: client.query
  - Missing inline ref: QueryJobConfig.maximum_bytes_billed
  - Missing inline ref: maximum_bytes_billed
  - Missing inline ref: client.query
  - Missing inline ref: --mode
  - Missing inline ref: dry_run
  - Missing inline ref: execute
  - Missing inline ref: dry_run
  - Missing inline ref: execute
  - Missing inline ref: --env=prod --confirm
  - Missing inline ref: argparse
  - Missing inline ref: GENERATE_DATE_ARRAY
  - Missing inline ref: MAX_CHUNKS
  - Missing inline ref: --override
  - Missing inline ref: FOR SYSTEM_TIME AS OF
  - Missing inline ref: DATE(ts)
  - Missing inline ref: CAST(...)
  - Missing inline ref: SELECT *
  - Missing inline ref: REGEXP
  - Missing inline ref: JSON_EXTRACT
  - Missing inline ref: INSERT
  - Missing inline ref: MERGE
  - Missing inline ref: entity_id + date + model_version
  - Missing inline ref: QUALIFY ROW_NUMBER() OVER (PARTITION BY <key>) = 1
  - Missing inline ref: WRITE_TRUNCATE
  - Missing inline ref: WRITE_APPEND
  - Missing inline ref: run_id
  - Missing inline ref: run_id
  - Missing inline ref: run_id, env, mode, date_range, tables written, total BQ jobs, total bytes
  - Missing inline ref: run_id
  - Missing inline ref: run_id
  - Missing inline ref: run_id = run_id or datetime.utcnow().strftime('%Y%m%dT%H%M%S')
  - Missing inline ref: templates/bigquery-pipeline-audit/
  - Missing inline ref: a_cost_exposure_what_will.md
  - Missing inline ref: c_backfill_and_loop_desig.md
  - Missing inline ref: e_safe_writes_and_idempot.md
- `prompts\boost-prompt.prompt.md`
  - Missing skill: writing-skills
  - Missing skill: writing-plans
  - Missing skill: joyride
  - Missing skill: context-map
  - Missing skill: prompt-engineering
  - Missing reference: writing-skills
  - Missing reference: writing-plans
  - Missing inline ref: /context-map
  - Missing inline ref: context-map
  - Missing inline ref: writing-skills
  - Missing inline ref: writing-plans
  - Missing inline ref: templates/boost-prompt/tools_required.md
  - Missing inline ref: templates/boost-prompt/phases.md
  - Missing inline ref: templates/boost-prompt/
  - Missing inline ref: phases.md
  - Missing inline ref: tools_required.md
- `prompts\breakdown-epic-arch.prompt.md`
  - Missing inline ref: templates/breakdown-epic-arch/output_format.md
  - Missing inline ref:

## Template References

Templates in

- Missing inline ref:
-
- `prompts\breakdown-epic-pm.prompt.md`
  - Missing inline ref:

## Template References

Templates in

- Missing inline ref:
-
- `prompts\breakdown-feature-implementation.prompt.md`
  - Missing inline ref: templates/breakdown-feature-implementation/output_format.md
  - Missing inline ref:

  - Missing inline ref:

## Template References

Detailed templates in

- `prompts\breakdown-feature-prd.prompt.md`
  - Missing inline ref:

## Template References

Templates in

- Missing inline ref:
-
- `prompts\breakdown-plan.prompt.md`
  - Missing inline ref: /docs/ways-of-work/plan/{epic-name}/{feature-name}.md
  - Missing inline ref: /docs/ways-of-work/plan/{epic-name}/{feature-name}/technical-breakdown.md
  - Missing inline ref: /docs/ways-of-work/plan/{epic-name}/{feature-name}/implementation-plan.md
  - Missing inline ref: plan-test
  - Missing inline ref: plan-epic-arch
  - Missing inline ref: plan-feature-prd
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref:

### Feature Issue Template

- Missing inline ref: ,
- Missing inline ref: ,
- Missing inline ref: ,
- Missing inline ref:

## Epic

# {epic-issue-number}

## Estimate

{Story points or t-shirt size}

- Missing inline ref:

### User Story Issue Template

- Missing inline ref: ,
- Missing inline ref: ,
- Missing inline ref: ,
- Missing inline ref:

### Technical Enabler Issue Template

- Missing inline ref: ,
- Missing inline ref: ,
- Missing inline ref: ,
- Missing inline ref:

## Template References

Detailed templates in

- Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\breakdown-test.prompt.md`
  - Missing inline ref: /docs/ways-of-work/plan/{epic-name}/{feature-name}.md
  - Missing inline ref: /docs/ways-of-work/plan/{epic-name}/{feature-name}/technical-breakdown.md
  - Missing inline ref: /docs/ways-of-work/plan/{epic-name}/{feature-name}/implementation-plan.md
  - Missing inline ref: /docs/ways-of-work/plan/{epic-name}/{feature-name}/project-plan.md
  - Missing inline ref:

## GitHub Issue Templates for Testing

### Test Strategy Issue Template

- Missing inline ref: ,
- Missing inline ref: ,
- Missing inline ref: ,
- Missing inline ref:

### Playwright Test Implementation Issue Template

- Missing inline ref: ,
- Missing inline ref: ,
- Missing inline ref:

### Quality Assurance Issue Template

- Missing inline ref: ,
- Missing inline ref: ,
- Missing inline ref:

## Template References

Detailed templates in

- `prompts\centos-linux-triage.prompt.md`
  - Missing inline ref: systemctl
  - Missing inline ref: journalctl
  - Missing inline ref: dnf
  - Missing inline ref: yum
  - Missing inline ref: firewalld
  - Missing inline ref: templates/centos-linux-triage/
  - Missing inline ref: inputs.md
  - Missing inline ref: instructions.md
  - Missing inline ref: output_format.md
- `prompts\code-exemplars-blueprint-generator.prompt.md`
  - Missing inline ref: templates/code-exemplars-blueprint-generator/generated_prompt.md
  - Missing inline ref: templates/code-exemplars-blueprint-generator/
  - Missing inline ref: generated_prompt.md
- `prompts\code-review.prompt.md`
  - Missing inline ref: templates/code-review/phases.md
  - Missing inline ref: templates/code-review/
  - Missing inline ref: phases.md
- `prompts\comicwise-development.prompt.md`
  - Missing inline ref:

## Essential Commands

| Command           | Purpose                         | Must Pass   |
| ----------------- | ------------------------------- | ----------- |
|

- Missing inline ref:         | Start dev server (Turbopack)    | —           |
|
- Missing inline ref:  | TypeScript validation           | ✅ 0 errors |
|
- Missing inline ref:    | ESLint + Prettier auto-fix      | ✅ All pass |
|
- Missing inline ref:        | Vitest unit tests (jsdom)       | ✅ 241/241  |
|
- Missing inline ref:       | Production build (Webpack)      | ✅ Success  |
|
- Missing inline ref:    | All quality gates at once       | ✅ All pass |
|
- Missing inline ref:     | Apply schema changes (dev only) | —           |
|
- Missing inline ref:   | Drizzle visual browser          | —           |
|
- Missing inline ref:    | Populate database               | —           |

## Data Flow Architecture

- Missing inline ref:

## Coding Rules (Enforced)

> ### Type Safety & Code Quality
>
> 1. **No
>
- Missing inline ref:

## Path Aliases (tsconfig.json)

- Missing inline ref: typescript
@/*→ ./src/*
ui         → ./src/components/ui/*
database   → ./src/database/*
schemas    → ./src/schemas/*
env        → ./src/lib/env.ts
hooks      → ./src/hooks/*
appConfig  → ./appConfig.ts
lib        → ./src/lib/*
types      → ./src/types/*
components → ./src/components/*
utils      → ./src/lib/utils.ts
assets     → ./src/assets/*
styles     → ./src/styles/*
tests      → ./src/tests/*

- Missing inline ref:

## Database Schema Facts

- **
  - Missing inline ref: ** =
  - Missing inline ref:  — aggregate with
  - Missing inline ref: . The
  - Missing inline ref:  column =
  - Missing inline ref:  (1–5 stars)
- **
  - Missing inline ref: ** =
  - Missing inline ref:  (UUID string), not integer
- **
  - Missing inline ref: ** = composite PK on
  - Missing inline ref:  → use
  - Missing inline ref:  for upserts
- **
  - Missing inline ref: ** =
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref:  and
  - Missing inline ref:  tables have
  - Missing inline ref: ,
  - Missing inline ref:  (no cascade);
  - Missing inline ref:  (
  - Missing inline ref:

## Quality Gate (Must Pass Before Commits)

- Missing inline ref:

## Environment Variables

**Required** (in

- Missing inline ref:

**Optional** (see

- Missing inline ref: ,
- Missing inline ref:
-
  - Missing inline ref: , etc.
-
  - Missing inline ref:  (override default)

All validated via

- Missing inline ref:  at startup using Zod.

## Reference Documentation

| File | Purpose | Scope |
| --- | --- | --- |
|

- Missing inline ref:  | Complete guide (2500+ lines) | Global |
|
- Missing inline ref:  | Quick reference (400 lines) | Session shortcuts |
|
- Missing inline ref:  | Auto-loaded by file pattern (15+ files) | Specific file types |
|
- Missing inline ref:  | 26 sections with patterns & examples | Development reference |
|
- Missing inline ref:  | Phase planning & task tracking | Project roadmap |
|
- Missing inline ref:  | This project's quick setup guide | Quick start |

## Common Troubleshooting

| Issue | Solution |
| --- | --- |
| Type errors (TS2307) | Check import path aliases in

- Missing inline ref:  |
| N+1 query errors | Add
- Missing inline ref:  to DAL queries |
| Action throws instead of returns | Wrap in try-catch, return
- Missing inline ref:  |
| Styling not applying | Check Tailwind v4 syntax (
- Missing inline ref:  not
- Missing inline ref: ) |
| DB connection fails | Verify
- Missing inline ref:  and run
- Missing inline ref:  to test |
| Tests fail in CI but pass locally | Check mocks in
- Missing inline ref:  |
| Hydration mismatch | Use
- Missing inline ref:  hook not
- Missing inline ref:  in server code |

## When Stuck

1. **Architecture questions** — Check

- Missing inline ref:  (2500+ lines) or ask about system design

1. **Component issues** — Reference

- Missing inline ref:

1. **Database/ORM** — Review DAL examples (eager loading with

- Missing inline ref: )

1. **Type errors** — Use

- Missing inline ref:  not
- Missing inline ref: , import types with
- Missing inline ref:

1. **Tests failing** — Check mocks in

- Missing inline ref:

1. **Performance** — Reference

- Missing inline ref:  or
- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\comment-code-generate-a-tutorial.prompt.md`
  - Missing inline ref: templates/comment-code-generate-a-tutorial/
  - Missing inline ref: legacy_prompt_details.md
  - Missing inline ref: phases.md
- `prompts\containerize-aspnet-framework.prompt.md`
  - Missing inline ref: templates/containerize-aspnet-framework/containerization_settings.md
  - Missing inline ref: progress.md
  - Missing inline ref: templates/containerize-aspnet-framework/execution_process.md
  - Missing inline ref:

If the build fails, review the error messages and make necessary adjustments to the Dockerfile or project configuration. Report success/failure.

## Progress Tracking

Maintain a

- Missing inline ref: ,
- Missing inline ref: , etc. with your actual file names

1. Adjust the Windows Server and .NET Framework versions as needed
2. Modify the dependency installation steps based on your requirements and remove any unnecessary ones
3. Add or remove stages as needed for your specific workflow

## Notes on Stage Naming

> - The
>
- Missing inline ref:  syntax gives each stage a name
>
> - Use
>
- Missing inline ref:

## Template References

Detailed templates in

- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\containerize-aspnetcore.prompt.md`
  - Missing inline ref: templates/containerize-aspnetcore/containerization_settings.md
  - Missing inline ref: progress.md
  - Missing inline ref: templates/containerize-aspnetcore/execution_process.md
  - Missing inline ref:

If the build fails, review the error messages and make necessary adjustments to the Dockerfile or project configuration. Report success/failure.

## Progress Tracking

Maintain a

- Missing inline ref: ,
- Missing inline ref:

## Notes on Stage Naming

- The
  - Missing inline ref:  syntax gives each stage a name
- Use
  - Missing inline ref:  to copy files from a previous stage
- You can have multiple intermediate stages that aren't used in the final image
- The
  - Missing inline ref:  stage is the one that becomes the final container image

## Security Best Practices

- Always run as a non-root user in production
- Use specific image tags instead of
  - Missing inline ref:
- Minimize the number of installed packages
- Keep base images updated
- Use multi-stage builds to exclude build dependencies from the final image

## Template References

Detailed templates in

- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\context-map.prompt.md`
  - Missing skill: codemap
  - Missing reference: codemap
  - Missing inline ref: codemap
  - Missing inline ref: templates/context-map/phases.md
  - Missing inline ref: templates/context-map/
  - Missing inline ref: phases.md
- `prompts\conventional-commit.prompt.md`
  - Missing inline ref: templates/conventional-commit/
  - Missing inline ref: legacy_prompt_details.md
  - Missing inline ref: phases.md
- `prompts\convert-plaintext-to-md.prompt.md`
  - Missing skill: enhance-markdown
  - Missing skill: context-map
  - Missing reference: enhance-markdown
  - Missing inline ref: pre=<name>
  - Missing inline ref: .md
  - Missing inline ref: {{file}}.md
  - Missing inline ref: --stop
  - Missing inline ref: /context-map
  - Missing inline ref: exit()
  - Missing inline ref: kill
  - Missing inline ref: quit
  - Missing inline ref: {{file}}
  - Missing inline ref: {{file}}.md
  - Missing inline ref: {{file}}.md
  - Missing inline ref: guide
  - Missing inline ref: instructions
  - Missing inline ref: instructions
  - Missing inline ref: context-map
  - Missing inline ref: writing-plans
  - Missing inline ref: simplify
  - Missing inline ref: templates/convert-plaintext-to-md/phases.md
  - Missing inline ref: {{file}}.md
  - Missing inline ref: finalize
  - Missing inline ref: .md
  - Missing inline ref: instructions
  - Missing inline ref: platform={{name}}
  - Missing inline ref: --header [1-4]
  - Missing inline ref: -p, --pattern <name|file>
  - Missing inline ref: api-doc
  - Missing inline ref: changelog
  - Missing inline ref: .md
  - Missing inline ref: -s, --stop <N|eof>
  - Missing inline ref: {{file}}.md
  - Missing inline ref: eof
  - Missing inline ref: rm-head-digits
  - Missing inline ref: mv-head-level(x, y)
  - Missing inline ref: x
  - Missing inline ref: y
  - Missing inline ref: rm-indent(x)
  - Missing inline ref: x
  - Missing inline ref: pre=<name>
  - Missing inline ref: templates/convert-plaintext-to-md/
  - Missing inline ref: phases.md
- `prompts\copilot-instructions-blueprint-generator.prompt.md`
  - Missing inline ref:

## Documentation Requirements

${DOCUMENTATION_LEVEL == "Minimal" ?

- Missing inline ref: templates/copilot-instructions-blueprint-generator/testing_approach.md
- Missing inline ref: templates/copilot-instructions-blueprint-generator/technology-specific_guidelines.md
- Missing inline ref: - Follow Semantic Versioning patterns as applied in the codebase

- Match existing patterns for documenting breaking changes
- Follow the same approach for deprecation notices
  - Missing inline ref: - Follow Calendar Versioning patterns as applied in the codebase

- Match existing patterns for documenting changes
- Follow the same approach for highlighting significant changes
  - Missing inline ref: - Match the exact versioning pattern observed in the codebase

- Follow the same changelog format used in existing documentation
- Apply the same tagging conventions used in the project
  - Missing inline ref: templates/copilot-instructions-blueprint-generator/project-specific_guidance.md
  - Missing inline ref: templates/copilot-instructions-blueprint-generator/
  - Missing inline ref: code_quality_standards.md
  - Missing inline ref: project-specific_guidance.md
  - Missing inline ref: technology-specific_guidelines.md
  - Missing inline ref: testing_approach.md
- `prompts\cosmosdb-datamodeling.prompt.md`
  - Missing inline ref: cosmosdb_requirements.md
  - Missing inline ref: cosmosdb_data_model.md
  - Missing inline ref:  for accuracy ✅

  - Missing inline ref:

## Template References

Detailed section templates in

- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\create-agentsmd.prompt.md`
  - Missing inline ref: AGENTS.md
  - Missing inline ref: templates/create-agentsmd/file_structure_and_content_gui.md
  - Missing inline ref: ,
  - Missing inline ref:
- [Review requirements]

## Additional Notes

- [Any project-specific context]
- [Common gotchas or troubleshooting tips]
- [Performance considerations]

  - Missing inline ref: markdown

# Sample AGENTS.md file

## Dev environment tips

- Use
  - Missing inline ref:  to jump to a package instead of scanning with
  - Missing inline ref: .
- Run
  - Missing inline ref:  to add the package to your workspace so Vite, ESLint, and TypeScript can see it.
- Use
  - Missing inline ref:  to spin up a new React + Vite package with TypeScript checks ready.
- Check the name field inside each package's package.json to confirm the right name—skip the top-level one.

## Testing instructions

- Find the CI plan in the .github/workflows folder.
- Run
  - Missing inline ref:  to run every check defined for that package.
- From the package root you can just call
  - Missing inline ref: .
- Fix any test or type errors until the whole suite is green.
- After moving files or changing imports, run
  - Missing inline ref:  and
  - Missing inline ref:  before committing.

- `prompts\create-architectural-decision-record.prompt.md`
  - Missing inline ref: /docs/adr/
  - Missing inline ref: adr-NNNN-[title-slug].md
  - Missing inline ref: adr-0001-database-selection.md
  - Missing inline ref:

  - Missing inline ref:

## Template References

Templates in

- Missing inline ref:
-
- `prompts\create-github-action-workflow-specification.prompt.md`
  - Missing inline ref:

  - Missing inline ref:

## Input/Output Contracts

### Inputs

- Missing inline ref:

## Outputs

- Missing inline ref:

## Template References

Detailed templates in

- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\create-github-issue-feature-from-specification.prompt.md`
  - Missing inline ref: search_issues
  - Missing inline ref: create_issue
  - Missing inline ref: update_issue
  - Missing inline ref: feature_request.yml
  - Missing inline ref: templates/create-github-issue-feature-from-specification/
  - Missing inline ref: phases.md
- `prompts\create-github-issues-feature-from-implementation-plan.prompt.md`
  - Missing inline ref: search_issues
  - Missing inline ref: create_issue
  - Missing inline ref: update_issue
  - Missing inline ref: feature_request.yml
  - Missing inline ref: chore_request.yml
  - Missing inline ref: templates/create-github-issues-feature-from-implementation-plan/
  - Missing inline ref: phases.md
- `prompts\create-github-issues-for-unmet-specification-requirements.prompt.md`
  - Missing inline ref: search_issues
  - Missing inline ref: create_issue
  - Missing inline ref: feature_request.yml
  - Missing inline ref: /spec/
  - Missing inline ref: templates/create-github-issues-for-unmet-specification-requirements/
  - Missing inline ref: phases.md
- `prompts\create-github-pull-request-from-specification.prompt.md`
  - Missing inline ref: get_pull_request
  - Missing inline ref: update_issue
  - Missing inline ref: templates/create-github-pull-request-from-specification/
  - Missing inline ref: phases.md
- `prompts\create-implementation-plan.prompt.md`
  - Missing inline ref: /plan/
  - Missing inline ref: [purpose]-[component]-[version].md
  - Missing inline ref: upgrade|refactor|feature|data|infrastructure|process|architecture|design
  - Missing inline ref: upgrade-system-command-4.md
  - Missing inline ref: feature-auth-module-1.md
  - Missing inline ref: templates/create-implementation-plan/status.md
  - Missing inline ref: templates/create-implementation-plan/2_implementation_steps.md
  - Missing inline ref:

## Template References

Detailed templates in

- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\create-llms.prompt.md`
  - Missing inline ref: llms.txt
  - Missing inline ref: llms.txt
  - Missing inline ref: templates/create-llms/analysis_and_planning_phase.md
  - Missing inline ref: llms.txt
  - Missing inline ref: templates/create-llms/implementation_requirements.md
  - Missing inline ref: templates/create-llms/execution_steps.md
  - Missing inline ref: /llms.txt
  - Missing inline ref:

## Success Criteria

The created

- Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\create-oo-component-documentation.prompt.md`
  - Missing inline ref: /docs/components/
  - Missing inline ref: [component-name]-documentation.md
  - Missing inline ref: csharp
// Basic usage example
var component = new ComponentName();
component.DoSomething();

  - Missing inline ref:

### Advanced Usage

- Missing inline ref: csharp
// Advanced configuration patterns
var options = new ComponentOptions();
var component = ComponentFactory.Create(options);
await component.ProcessAsync(data);

- Missing inline ref:

- Missing inline ref:

## Template References

Detailed templates in

- `prompts\create-readme.prompt.md`
  - Missing inline ref: templates/create-readme/
  - Missing inline ref: phases.md
- `prompts\create-specification.prompt.md`
  - Missing inline ref: templates/create-specification/best_practices_for_ai-rea.md
  - Missing inline ref: templates/create-specification/8_dependencies__external_.md
  - Missing inline ref: code
    // Code snippet or data example demonstrating the correct application of the guidelines, including edge cases

  - Missing inline ref:

## 10. Validation Criteria

[List the criteria or tests that must be satisfied for compliance with this specification.]

## 11. Related Specifications / Further Reading

[Link to related spec 1] [Link to relevant external documentation]

- Missing inline ref:

## Template References

Templates in

- Missing inline ref:
-
- `prompts\create-spring-boot-java-project.prompt.md`
  - Missing inline ref: artifactId
  - Missing inline ref: packageName
  - Missing inline ref: bootVersion
  - Missing inline ref: shell
java -version

  - Missing inline ref:

## Download Spring Boot project template

- Run following command in terminal to download a Spring Boot project template

  - Missing inline ref:

## Unzip the downloaded file

- Run following command in terminal to unzip the downloaded file

  - Missing inline ref:

## Remove the downloaded zip file

- Run following command in terminal to delete the downloaded zip file

  - Missing inline ref: shell
rm -f starter.zip

  - Missing inline ref:

## Change directory to the project root

- Run following command in terminal to change directory to the project root

  - Missing inline ref:

## Add additional dependencies

- Insert
  - Missing inline ref:  and
  - Missing inline ref:  dependency into
  - Missing inline ref:  file

  - Missing inline ref: xml
<dependency>
  <groupId>org.springdoc</groupId>
  <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
  <version>2.8.6</version>
</dependency>

<dependency>
  <groupId>com.tngtech.archunit</groupId>
  <artifactId>archunit-junit5</artifactId>
  <version>1.2.1</version>
  <scope>test</scope>
</dependency>

- Missing inline ref:

## Add SpringDoc, Redis, JPA and MongoDB configurations

> - Insert SpringDoc configurations into
>
- Missing inline ref:

## Add

- Missing inline ref:  with Redis, PostgreSQL and MongoDB services

- Create
  - Missing inline ref: ,
  - Missing inline ref:  and
  - Missing inline ref: .
  - redis service should have
    - password
  - Missing inline ref:
    - mapping port 6379 to 6379
    - mounting volume
  - Missing inline ref:  to
  - Missing inline ref:
  - postgresql service should have
    - password
  - Missing inline ref:
    - mapping port 5432 to 5432
    - mounting volume
  - Missing inline ref:  to
  - Missing inline ref:
  - mongo service should have
    - initdb root username
  - Missing inline ref:
    - initdb root password
  - Missing inline ref:
    - mapping port 27017 to 27017
    - mounting volume
  - Missing inline ref:  to
  - Missing inline ref:

## Add

- Missing inline ref:  file

- Insert
  - Missing inline ref: ,
  - Missing inline ref:  and
  - Missing inline ref:  directories in
  - Missing inline ref:  file

## Run Maven test command

- Run maven clean test command to check if the project is working

  - Missing inline ref: shell
./mvnw clean test

  - Missing inline ref:

## Run Maven run command (Optional)

- (Optional)
  - Missing inline ref:  to start the services,
  - Missing inline ref:  to run the Spring Boot project,
  - Missing inline ref:  to stop the services.

## Let's do this step by step

## Template References

Templates in

- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\create-spring-boot-kotlin-project.prompt.md`
  - Missing inline ref: artifactId
  - Missing inline ref: packageName
  - Missing inline ref: bootVersion
  - Missing inline ref: shell
java -version

  - Missing inline ref:

## Download Spring Boot project template

- Run following command in terminal to download a Spring Boot project template

  - Missing inline ref:

## Unzip the downloaded file

- Run following command in terminal to unzip the downloaded file

  - Missing inline ref:

## Remove the downloaded zip file

- Run following command in terminal to delete the downloaded zip file

  - Missing inline ref: shell
rm -f starter.zip

  - Missing inline ref:

## Unzip the downloaded file

- Run following command in terminal to unzip the downloaded file

  - Missing inline ref:

## Add additional dependencies

> - Insert
>
- Missing inline ref:  and
- Missing inline ref:

## Template References

Templates in

- Missing inline ref:
-
- `prompts\create-technical-spike.prompt.md`
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\create-tldr-page.prompt.md`
  - Missing inline ref: tldr
  - Missing inline ref: git
  - Missing inline ref: nmcli
  - Missing inline ref: distrobox-create
  - Missing inline ref: #fetch
  - Missing inline ref: tldr
  - Missing inline ref: tldr
  - Missing inline ref: -h
  - Missing inline ref: --help
  - Missing inline ref: /?
  - Missing inline ref: --tldr
  - Missing inline ref: --man
  - Missing inline ref: --help
  - Missing inline ref: --tldr
  - Missing inline ref: templates/create-tldr-page/usage.md
  - Missing inline ref: markdown

# command

> Short, snappy description. Some subcommands such as

- Missing inline ref:

- Missing inline ref:

## Template References

Detailed templates in

- Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\csharp-async.prompt.md`
  - Missing inline ref: GetDataAsync()
  - Missing inline ref: GetData()
  - Missing inline ref: Task<T>
  - Missing inline ref: Task
  - Missing inline ref: ValueTask<T>
  - Missing inline ref: void
  - Missing inline ref: ConfigureAwait(false)
  - Missing inline ref: Task.FromException()
  - Missing inline ref: Task.WhenAll()
  - Missing inline ref: Task.WhenAny()
  - Missing inline ref: .Wait()
  - Missing inline ref: .Result
  - Missing inline ref: .GetAwaiter().GetResult()
  - Missing inline ref: templates/csharp-async/
  - Missing inline ref: common_pitfalls.md
  - Missing inline ref: exception_handling.md
  - Missing inline ref: implementation_patterns.md
  - Missing inline ref: performance.md
  - Missing inline ref: return_types.md
- `prompts\csharp-docs.prompt.md`
  - Missing inline ref: <summary>
  - Missing inline ref: <remarks>
  - Missing inline ref: <see langword>
  - Missing inline ref: null
  - Missing inline ref: true
  - Missing inline ref: false
  - Missing inline ref: int
  - Missing inline ref: bool
  - Missing inline ref: <c>
  - Missing inline ref: <example>
  - Missing inline ref: <code>
  - Missing inline ref: <code>
  - Missing inline ref: <example>
  - Missing inline ref: language
  - Missing inline ref: <code language="csharp">
  - Missing inline ref: <see cref>
  - Missing inline ref: <seealso>
  - Missing inline ref: <inheritdoc/>
  - Missing inline ref: <param>
  - Missing inline ref: <see langword="true" />
  - Missing inline ref: <see langword="false" />
  - Missing inline ref: <paramref>
  - Missing inline ref: <typeparam>
  - Missing inline ref: <typeparamref>
  - Missing inline ref: <returns>
  - Missing inline ref: <see langword="true" />
  - Missing inline ref: <see langword="false" />
  - Missing inline ref: <summary>
  - Missing inline ref: <value>
  - Missing inline ref: <see langword="false" />
  - Missing inline ref: <see langword="true" />
  - Missing inline ref: <see langword="false" />
  - Missing inline ref: <exception cref>
  - Missing inline ref: templates/csharp-docs/
  - Missing inline ref: methods.md
- `prompts\csharp-mcp-server-generator.prompt.md`
  - Missing inline ref: templates/csharp-mcp-server-generator/implementation_details.md
  - Missing inline ref: templates/csharp-mcp-server-generator/
  - Missing inline ref: implementation_details.md
- `prompts\csharp-mstest.prompt.md`
  - Missing inline ref: [ProjectName].Tests
  - Missing inline ref: dotnet test
  - Missing inline ref: [TestClass]
  - Missing inline ref: [TestMethod]
  - Missing inline ref: [DataTestMethod]
  - Missing inline ref: MethodName_Scenario_ExpectedBehavior
  - Missing inline ref: csharp
[TestClass]
public sealed class CalculatorTests
{
    [TestMethod]
    public void Add_TwoPositiveNumbers_ReturnsSum()
    {
        // Arrange
        var calculator = new Calculator();

        // Act
        var result = calculator.Add(2, 3);

        // Assert
        Assert.AreEqual(5, result);
    }
}

  - Missing inline ref:

## Test Lifecycle

> - **Prefer constructors over
>
- Missing inline ref: ** - enables
- Missing inline ref:  fields an
>
> - Use
>
- Missing inline ref: ,
- Missing inline ref: , and
- Missing inline ref: templates/csharp-mstest/modern_assertion_apis.md
- Missing inline ref: templates/csharp-mstest/data-driven_tests.md
- Missing inline ref: TestContext
- Missing inline ref: templates/csharp-mstest/testcontext.md
- Missing inline ref: templates/csharp-mstest/advanced_features.md
- Missing inline ref: templates/csharp-mstest/common_mistakes_to_avoid.md
- Missing inline ref: [TestCategory("Category")]
- Missing inline ref: [TestProperty("Name", "Value")]
- Missing inline ref: [TestProperty("Bug", "12345")]
- Missing inline ref: [Priority(1)]
- Missing inline ref: templates/csharp-mstest/
- Missing inline ref: advanced_features.md
- Missing inline ref: common_mistakes_to_avoid.md
- Missing inline ref: data-driven_tests.md
- Missing inline ref: modern_assertion_apis.md
- Missing inline ref: test_lifecycle.md
- Missing inline ref: testcontext.md
- `prompts\csharp-nunit.prompt.md`
  - Missing inline ref: [ProjectName].Tests
  - Missing inline ref: CalculatorTests
  - Missing inline ref: Calculator
  - Missing inline ref: dotnet test
  - Missing inline ref: [TestFixture]
  - Missing inline ref: [Test]
  - Missing inline ref: MethodName_Scenario_ExpectedBehavior
  - Missing inline ref: [SetUp]
  - Missing inline ref: [TearDown]
  - Missing inline ref: [OneTimeSetUp]
  - Missing inline ref: [OneTimeTearDown]
  - Missing inline ref: [SetUpFixture]
  - Missing inline ref: [TestCase]
  - Missing inline ref: [TestCaseSource]
  - Missing inline ref: [Values]
  - Missing inline ref: [ValueSource]
  - Missing inline ref: [Random]
  - Missing inline ref: [Range]
  - Missing inline ref: [Combinatorial]
  - Missing inline ref: [Pairwise]
  - Missing inline ref: Assert.That
  - Missing inline ref: Is.EqualTo
  - Missing inline ref: Is.SameAs
  - Missing inline ref: Contains.Item
  - Missing inline ref: Assert.AreEqual
  - Missing inline ref: CollectionAssert
  - Missing inline ref: StringAssert
  - Missing inline ref: Assert.Throws<T>
  - Missing inline ref: Assert.ThrowsAsync<T>
  - Missing inline ref: [Category("CategoryName")]
  - Missing inline ref: [Order]
  - Missing inline ref: [Author("DeveloperName")]
  - Missing inline ref: [Description]
  - Missing inline ref: [Explicit]
  - Missing inline ref: [Ignore("Reason")]
  - Missing inline ref: templates/csharp-nunit/
  - Missing inline ref: assertions.md
  - Missing inline ref: data-driven_tests.md
  - Missing inline ref: mocking_and_isolation.md
  - Missing inline ref: project_setup.md
  - Missing inline ref: standard_tests.md
  - Missing inline ref: test_organization.md
  - Missing inline ref: test_structure.md
- `prompts\csharp-tunit.prompt.md`
  - Missing inline ref: [ProjectName].Tests
  - Missing inline ref: CalculatorTests
  - Missing inline ref: Calculator
  - Missing inline ref: dotnet test
  - Missing inline ref: [Test]
  - Missing inline ref: [Fact]
  - Missing inline ref: MethodName_Scenario_ExpectedBehavior
  - Missing inline ref: [Before(Test)]
  - Missing inline ref: [After(Test)]
  - Missing inline ref: [Before(Class)]
  - Missing inline ref: [After(Class)]
  - Missing inline ref: [Before(Assembly)]
  - Missing inline ref: [After(Assembly)]
  - Missing inline ref: [Before(TestSession)]
  - Missing inline ref: [After(TestSession)]
  - Missing inline ref: await Assert.That()
  - Missing inline ref: [DependsOn]
  - Missing inline ref: [Arguments]
  - Missing inline ref: [InlineData]
  - Missing inline ref: [MethodData]
  - Missing inline ref: [MemberData]
  - Missing inline ref: [ClassData]
  - Missing inline ref: ITestDataSource
  - Missing inline ref: [Arguments]
  - Missing inline ref: await Assert.That(value).IsEqualTo(expected)
  - Missing inline ref: await Assert.That(value).IsSameReferenceAs(expected)
  - Missing inline ref: await Assert.That(value).IsTrue()
  - Missing inline ref: await Assert.That(value).IsFalse()
  - Missing inline ref: await Assert.That(collection).Contains(item)
  - Missing inline ref: await Assert.That(collection).DoesNotContain(item)
  - Missing inline ref: await Assert.That(value).Matches(pattern)
  - Missing inline ref: await Assert.That(action).Throws<TException>()
  - Missing inline ref: await Assert.That(asyncAction).ThrowsAsync<TException>()
  - Missing inline ref: .And
  - Missing inline ref: await Assert.That(value).IsNotNull().And.IsEqualTo(expected)
  - Missing inline ref: .Or
  - Missing inline ref: await Assert.That(value).IsEqualTo(1).Or.IsEqualTo(2)
  - Missing inline ref: .Within(tolerance)
  - Missing inline ref: [Repeat(n)]
  - Missing inline ref: [Retry(n)]
  - Missing inline ref: [ParallelLimit<T>]
  - Missing inline ref: [Skip("reason")]
  - Missing inline ref: [DependsOn(nameof(OtherTest))]
  - Missing inline ref: [Timeout(milliseconds)]
  - Missing inline ref: [Category("CategoryName")]
  - Missing inline ref: [DisplayName("Custom Test Name")]
  - Missing inline ref: TestContext
  - Missing inline ref: [WindowsOnly]
  - Missing inline ref: [NotInParallel]
  - Missing inline ref: [ParallelLimit<T>]
  - Missing inline ref: [Repeat(n)]
  - Missing inline ref: [ParallelLimit<T>]
  - Missing inline ref: [Fact]
  - Missing inline ref: [Test]
  - Missing inline ref: [Theory]
  - Missing inline ref: [Test]
  - Missing inline ref: [Arguments]
  - Missing inline ref: [InlineData]
  - Missing inline ref: [Arguments]
  - Missing inline ref: [MemberData]
  - Missing inline ref: [MethodData]
  - Missing inline ref: Assert.Equal
  - Missing inline ref: await Assert.That(actual).IsEqualTo(expected)
  - Missing inline ref: Assert.True
  - Missing inline ref: await Assert.That(condition).IsTrue()
  - Missing inline ref: Assert.Throws<T>
  - Missing inline ref: await Assert.That(action).Throws<T>()
  - Missing inline ref: [Before(Test)]
  - Missing inline ref: [After(Test)]
  - Missing inline ref: IClassFixture<T>
  - Missing inline ref: [Before(Class)]
  - Missing inline ref: [After(Class)]
  - Missing inline ref: templates/csharp-tunit/
  - Missing inline ref: migration_from_xunit.md
- `prompts\csharp-xunit.prompt.md`
  - Missing inline ref: [ProjectName].Tests
  - Missing inline ref: CalculatorTests
  - Missing inline ref: Calculator
  - Missing inline ref: dotnet test
  - Missing inline ref: [Fact]
  - Missing inline ref: MethodName_Scenario_ExpectedBehavior
  - Missing inline ref: IDisposable.Dispose()
  - Missing inline ref: IClassFixture<T>
  - Missing inline ref: ICollectionFixture<T>
  - Missing inline ref: [Theory]
  - Missing inline ref: [InlineData]
  - Missing inline ref: [MemberData]
  - Missing inline ref: [ClassData]
  - Missing inline ref: DataAttribute
  - Missing inline ref: Assert.Equal
  - Missing inline ref: Assert.Same
  - Missing inline ref: Assert.True
  - Missing inline ref: Assert.False
  - Missing inline ref: Assert.Contains
  - Missing inline ref: Assert.DoesNotContain
  - Missing inline ref: Assert.Matches
  - Missing inline ref: Assert.DoesNotMatch
  - Missing inline ref: Assert.Throws<T>
  - Missing inline ref: await Assert.ThrowsAsync<T>
  - Missing inline ref: [Trait("Category", "CategoryName")]
  - Missing inline ref: ITestOutputHelper
  - Missing inline ref: Skip = "reason"
  - Missing inline ref: templates/csharp-xunit/
  - Missing inline ref: assertions.md
  - Missing inline ref: data-driven_tests.md
  - Missing inline ref: mocking_and_isolation.md
  - Missing inline ref: project_setup.md
  - Missing inline ref: standard_tests.md
  - Missing inline ref: test_organization.md
  - Missing inline ref: test_structure.md
- `prompts\database.prompt.md`
  - Missing inline ref: templates/database/
  - Missing inline ref: common_patterns.md
- `prompts\dataverse-python-production-code.prompt.md`
  - Missing inline ref: templates/dataverse-python-production-code/error_handling_structure.md
  - Missing inline ref: templates/dataverse-python-production-code/client_management_pattern.md
  - Missing inline ref:

## OData Optimization

- Always include
  - Missing inline ref:  parameter to limit columns
- Use
  - Missing inline ref:  on server (lowercase logical names)
- Use
  - Missing inline ref: ,
  - Missing inline ref:  for pagination
- Use
  - Missing inline ref:

## Template References

Templates in

- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\dataverse-python-usecase-builder.prompt.md`
  - Missing inline ref:

## Template References

Detailed templates in

- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\debian-linux-triage.prompt.md`
  - Missing inline ref: systemctl
  - Missing inline ref: journalctl
  - Missing inline ref: apt
  - Missing inline ref: dpkg
  - Missing inline ref: templates/debian-linux-triage/
  - Missing inline ref: inputs.md
  - Missing inline ref: instructions.md
  - Missing inline ref: output_format.md
- `prompts\debug-issue.prompt.md`
  - Missing inline ref: templates/debug-issue/
  - Missing inline ref: inputs.md
  - Missing inline ref: output.md
  - Missing inline ref: steps.md
- `prompts\declarative-agents.prompt.md`
  - Missing inline ref:

## Template References

Detailed templates in

- `prompts\dev-imp.prompt.md`
  - Missing inline ref:
discover generators → user selects subset → implement each sequentially
  → (only then) verify implementation status
  → (only then) code-review all changed files
  → (only then) debug and fix all issues
  → (only then) re-verify all fixes
  → (only then) generate implementation report

  - Missing inline ref: .

## Profile

- Missing inline ref:

## Personality

Analytical, thorough, quality-focused. Reports should be "crispy" — concise, structured, scannable with clear pass/fail indicators, table summaries, and actionable bullet items.

## Tools

-
  - Missing inline ref:  — run generators, git operations, tests, linters
-
  - Missing inline ref:  — read/write prompt and project files
-
  - Missing inline ref:  and optionally
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref:

### Report Style ("Crispy")

- Compact tables for structured data
- Emoji indicators for status (✅ ❌ ⚠️ ➕ 📝)
- No prose paragraphs where bullets suffice
- Total line count under 80 lines typical
- Clear pass/fail at a glance

## Edge Cases & Pitfalls

| Situation | Handling |
|-----------|----------|
| No generator prompts found | Report "No generators available", proceed to Phase 6 with partial report |
| Generator fails mid-run | Log the error, mark as ❌, continue to next generator |
| User selects 0 generators | Confirm intent, proceed to Phase 6 with empty report |
| Target project doesn't exist yet | Scaffold minimal project structure before running generators |
| Code review finds 0 issues | Skip Phase 5 (no fixes needed), go directly to Phase 6 |
| Build/tests fail post-fix | Loop back to Phase 5 until passing or escalate to user |
| PWD has no git repo | Use

- Missing inline ref:  before first generator run to enable change tracking |

## Verification Checklist

- [ ] Generators discovered and selectable
- [ ] Selected generators all ran to completion
- [ ] Implementation verified (build + tests pass)
- [ ] Code review performed on all changed files
- [ ] All critical/important issues fixed
- [ ] Fixes re-verified (no regressions)
- [ ]
- `prompts\dev-init.prompt.md`
  - Missing skill: brainstorming
  - Missing skill: plans-and-specs
  - Missing skill: writing-skills
  - Missing skill: writing-plans
  - Missing skill: acpx-executor
  - Missing skill: executing-plans
  - Missing skill: simplify
  - Missing reference: introspection-only-general
  - Missing reference: no-git-delete
  - Missing reference: no-net-fetch
  - Missing reference: skills-tools-preflight-check
  - Missing reference: context-map
  - Missing reference: convert-plaintext-to-md
  - Missing reference: boost-prompt
  - Missing reference: ai-prompt-engineering-safety-review
  - Missing reference: update-implementation-plan
  - Missing reference: prompt-builder
  - Missing reference: brainstorming
  - Missing reference: plans-and-specs
  - Missing reference: writing-skills
  - Missing reference: writing-plans
  - Missing reference: acpx-executor
  - Missing reference: executing-plans
  - Missing reference: simplify
  - Missing inline ref: prompts/context-map
  - Missing inline ref: prompts/convert-plaintext-to-md
  - Missing inline ref: prompts/boost-prompt
  - Missing inline ref: prompts/ai-prompt-engineering-safety-review
  - Missing inline ref: prompts/update-implementation-plan
  - Missing inline ref: prompts/prompt-builder
  - Missing inline ref: Prompts/*.md
  - Missing inline ref: docs/dev-init-comprehensive-plan.md
  - Missing inline ref: docs/dev-init-spec.md
  - Missing inline ref: docs/prompts-cross-reference-registry.md
  - Missing inline ref: docs/prompt-conversion-enhancement-plan.md
  - Missing inline ref: projects/Bash/archive/artifacts/context-maps/dev-init.context.json
  - Missing inline ref: Prompts/*.txt
  - Missing inline ref: Prompts/*.md
  - Missing inline ref: prompts/*.prompt.md
  - Missing inline ref: context-map
  - Missing inline ref: context-map
  - Missing inline ref: convert-plaintext-to-md
  - Missing inline ref: boost-prompt
  - Missing inline ref: ai-prompt-engineering-safety-review
  - Missing inline ref: update-implementation-plan
  - Missing inline ref: prompt-builder
  - Missing inline ref: brainstorming
  - Missing inline ref: plans-and-specs
  - Missing inline ref: writing-skills
  - Missing inline ref: writing-plans
  - Missing inline ref: acpx-executor
  - Missing inline ref: executing-plans
  - Missing inline ref: simplify
  - Missing inline ref: Prompts/*.txt
  - Missing inline ref: Prompts/*.md
  - Missing inline ref: boost-prompt
  - Missing inline ref: ai-prompt-engineering-safety-review
  - Missing inline ref: update-implementation-plan
  - Missing inline ref: prompt-builder
  - Missing inline ref: context-map
  - Missing inline ref: brainstorming
  - Missing inline ref: plans-and-specs
  - Missing inline ref: Prompts/*.txt
  - Missing inline ref: Prompts/*.md
  - Missing inline ref: prompts/*.prompt.md
  - Missing inline ref: context-map
  - Missing inline ref: Prompts/*.txt
  - Missing inline ref: .md
  - Missing inline ref: context-map
  - Missing inline ref: read_file("prompts/context-map.prompt.md")
  - Missing inline ref: skill_view(name="brainstorming")
  - Missing inline ref: skill_view(name="plans-and-specs")
  - Missing inline ref: skill_view(name="acpx-executor")
  - Missing inline ref: search_files(pattern, target)
  - Missing inline ref: delegate_task(goal, toolsets)
  - Missing inline ref: /enhance-markdown
  - Missing inline ref: _archive/dev-init.prompts.txt
  - Missing inline ref: /enhance-markdown
  - Missing inline ref: bash
/enhance-markdown <file> [slug]       # audit + enhance mode
/enhance-markdown --txt-to-md [file]  # TXT→MD conversion mode (batch or single)

  - Missing inline ref:
IF docs/prompt-conversion-enhancement-plan.md EXISTS → read it, skip to Step 5.3
ELSE IF docs/dev-init-comprehensive-plan.md EXISTS → plan exists, skip to Step 5.2
ELSE → run Phase 1–4 first, then return here

  - Missing inline ref:

### Step 5.1 — Load Plan Artifacts

- Missing inline ref: bash
read_file("docs/dev-init-comprehensive-plan.md")
read_file("docs/dev-init-spec.md")
read_file("projects/Bash/archive/artifacts/context-maps/dev-init.context.json")

- Missing inline ref:

### Step 5.2 — Run

- Missing inline ref:

1. Load

- Missing inline ref:

1. Map all

- Missing inline ref:  →
- Missing inline ref:  pairs

1. Map all

- Missing inline ref:  dependencies

1. Write

- Missing inline ref:

### Step 5.3 — Run

- Missing inline ref:

For each

- Missing inline ref:

1. Write to

- Missing inline ref:  (overwrite if exists)

### Step 5.4 — Run

- Missing inline ref:

For each

- Missing inline ref:

For each

- Missing inline ref:  and
- Missing inline ref:

1. Scaffold new

- Missing inline ref:  files from template

1. Populate with content from plan artifacts

### Step 5.7 — Run

- Missing inline ref:

1. Load

- Missing inline ref:

1. Update

- Missing inline ref:  →
- Missing inline ref:  (Step 5.3)
- [ ] Boost all
  - Missing inline ref:

### Step 6.2 — Cross-Reference Validation

- Missing inline ref:

### Step 6.3 — Conflict Detection

- Missing inline ref:

### Step 6.4 — Quality Scoring

Score each

- Missing inline ref:

### Tasks

- [ ] Structural audit all
  - Missing inline ref:  files
- [ ] Validate all cross-references resolve
- [ ] Detect duplicate triggers/titles
- [ ] Score each file against quality criteria
- [ ] Write verification report to
  - Missing inline ref: markdown

# Prompts Cross-Reference Registry

## Prompts/\*.md (Conversion Targets)

| File                  | Trigger     | Status | Score | Depends On                           |
| --------------------- | ----------- | ------ | ----- | ------------------------------------ |
| skills-fix.prompts.md | /skills-fix | ✅     | 85    | context-map, skill-judge             |
| dev-init.prompts.md   | /dev-init   | ✅     | 90    | context-map, convert-plaintext-to-md |
| ...                   | ...         | ...    | ...   | ...                                  |

## prompts/\*.prompt.md (Workflow Prompts)

| File                              | Purpose             | Used By             |
| --------------------------------- | ------------------- | ------------------- |
| context-map.prompt.md             | Dependency mapping  | All dev-init phases |
| convert-plaintext-to-md.prompt.md | TXT→MD conversion   | Phase 5.3           |
| boost-prompt.prompt.md            | Quality enhancement | Phase 5.4           |
| ...                               | ...                 | ...                 |

## Conflict Log

| Conflict | Files | Resolution |
| -------- | ----- | ---------- |
| ...      | ...   | ...        |

- Missing inline ref:

### Step 7.2 — Final Verification

- Missing inline ref: bash

# Count total prompts

ls Prompts/*.prompts.md | wc -l
ls prompts/*.prompt.md | wc -l

# Verify registry matches disk

# Every file on disk is in registry

# Every registry entry exists on disk

- Missing inline ref:

### Tasks

- [ ] Build cross-reference registry
- [ ] Verify registry matches disk state
- [ ] Commit all changes with
- `prompts\dev.prompt.md`
  - Missing inline ref: templates/dev/
  - Missing inline ref: phase_1.md
- `prompts\development.prompt.md`
  - Missing inline ref: templates/Developement/comprehensive_setup_guide_for_.md
  - Missing inline ref: **/*.ts
  - Missing inline ref: **/*.tsx
  - Missing inline ref: **/*.mjs
  - Missing inline ref: **/*.json
  - Missing inline ref: **/*.mts
  - Missing inline ref: **/*.json
  - Missing inline ref: **/*.md
  - Missing inline ref: **/*.txt
  - Missing inline ref: **/*.yml
  - Missing inline ref: **/*.ps1
  - Missing inline ref: **/*.sh
  - Missing inline ref: **/*/Dockerfile
  - Missing inline ref: src/**
  - Missing inline ref: scripts/**
  - Missing inline ref: templates/Developement/tasks.md
  - Missing inline ref: templates/Developement/
  - Missing inline ref: comprehensive_setup_guide_for_.md
  - Missing inline ref: tasks.md
  - Missing inline ref: tasks_.md
- `prompts\devops-rollout-plan.prompt.md`
  - Missing inline ref: templates/devops-rollout-plan/input_requirements.md
  - Missing inline ref: templates/devops-rollout-plan/output_format.md
  - Missing inline ref: templates/devops-rollout-plan/
  - Missing inline ref: input_requirements.md
  - Missing inline ref: output_format.md
  - Missing inline ref: phases.md
- `prompts\documentation-writer.prompt.md`
  - Missing inline ref: templates/documentation-writer/
  - Missing inline ref: phases.md
- `prompts\documentation.prompt.md`
  - Missing inline ref: templates/documentation/phases.md
  - Missing inline ref: templates/documentation/
  - Missing inline ref: phases.md
- `prompts\dotnet-best-practices.prompt.md`
  - Missing inline ref: public class MyClass(IDependency dependency)
  - Missing inline ref: CommandHandler<TOptions>
  - Missing inline ref: _resourceManager.GetString("MessageKey")
  - Missing inline ref: templates/dotnet-best-practices/
  - Missing inline ref: asyncawait_patterns.md
  - Missing inline ref: code_quality.md
  - Missing inline ref: configuration__settings.md
  - Missing inline ref: dependency_injection__ser.md
  - Missing inline ref: design_patterns__architec.md
  - Missing inline ref: documentation__structure.md
  - Missing inline ref: error_handling__logging.md
  - Missing inline ref: performance__security.md
  - Missing inline ref: resource_management__loca.md
  - Missing inline ref: semantic_kernel__ai_integ.md
  - Missing inline ref: testing_standards.md
- `prompts\dotnet-design-pattern-review.prompt.md`
  - Missing inline ref: CommandHandler<TOptions>
  - Missing inline ref: ICommandHandler<TOptions>
  - Missing inline ref: CommandHandlerOptions
  - Missing inline ref: SetupCommand(IHost host)
  - Missing inline ref: ArgumentNullException
  - Missing inline ref: {Core|Console|App|Service}.{Feature}
  - Missing inline ref: templates/dotnet-design-pattern-review/
  - Missing inline ref: improvement_focus_areas.md
  - Missing inline ref: required_design_patterns.md
  - Missing inline ref: review_checklist.md
- `prompts\dotnet-upgrade.prompt.md`
  - Missing inline ref: .NET Framework
  - Missing inline ref: .NET Core
  - Missing inline ref: .NET Standard
  - Missing inline ref: .csproj
  - Missing inline ref: TargetFramework
  - Missing inline ref: packages.config
  - Missing inline ref: PackageReference
  - Missing inline ref: TargetFramework
  - Missing inline ref: net8.0
  - Missing inline ref: WebHostBuilder
  - Missing inline ref: HostBuilder
  - Missing inline ref: UseDotNet@2
  - Missing inline ref: NuGetToolInstaller
  - Missing inline ref: .NET Upgrade Assistant
  - Missing inline ref: Startup.cs
  - Missing inline ref: Program.cs
  - Missing inline ref: Upgrade to .NET [Version]
  - Missing inline ref: .NET Upgrade Assistant
  - Missing inline ref: dotnet list package --outdated
  - Missing inline ref: dotnet migrate
  - Missing inline ref: graph.json
  - Missing inline ref: templates/dotnet-upgrade/
- `prompts\editorconfig.prompt.md`
  - Missing inline ref: .editorconfig
  - Missing inline ref: .editorconfig
  - Missing inline ref: .editorconfig
  - Missing inline ref: *
  - Missing inline ref: **.js
  - Missing inline ref: **.py
  - Missing inline ref: .editorconfig
  - Missing inline ref: .editorconfig
  - Missing inline ref: templates/editorconfig/execution.md
  - Missing inline ref: root = true
  - Missing inline ref: [*]
  - Missing inline ref: indent_style = space
  - Missing inline ref: indent_size = 2
  - Missing inline ref: end_of_line = lf
  - Missing inline ref: charset = utf-8
  - Missing inline ref: trim_trailing_whitespace = true
  - Missing inline ref: insert_final_newline = true
  - Missing inline ref: [*.md]
  - Missing inline ref: trim_trailing_whitespace = false
  - Missing inline ref: templates/editorconfig/
  - Missing inline ref: execution.md
  - Missing inline ref: phases.md
- `prompts\ef-core.prompt.md`
  - Missing inline ref: templates/ef-core/
  - Missing inline ref: phases.md
- `prompts\execute-acpx-agents-feature-specs.prompt.md`
  - Missing inline ref: .hermes/plans/acpx-agents-feature-specs.md
  - Missing inline ref: .hermes/plans/acpx-agents-feature-specs.md
- `prompts\execute-all-prompts.prompt.md`
  - Missing skill: using-superpowers
  - Missing skill: user-communication-preferences
  - Missing skill: plans-and-specs
  - Missing skill: executing-plans
  - Missing skill: verification-before-completion
  - Missing reference: using-superpowers
  - Missing reference: user-communication-preferences
  - Missing reference: plans-and-specs
  - Missing reference: executing-plans
  - Missing reference: verification-before-completion
  - Missing inline ref: ~/AppData/Local/hermes/scripts/
  - Missing inline ref: docs/orchestrator-progress.md
  - Missing inline ref: $HOME/Desktop/SandBox
  - Missing inline ref: docs/orchestrator-progress.md
  - Missing inline ref: docs/orchestrator-verification.md
  - Missing inline ref: using-superpowers
  - Missing inline ref: user-communication-preferences
  - Missing inline ref: plans-and-specs
  - Missing inline ref: executing-plans
  - Missing inline ref: verification-before-completion
  - Missing inline ref: docs/orchestrator-progress.md
  - Missing inline ref: templates/execute-all-prompts/phases.md
  - Missing inline ref: docs/orchestrator-progress.md
  - Missing inline ref: docs/orchestrator-verification.md
  - Missing inline ref: hermes chat -q --provider
  - Missing inline ref: templates/execute-all-prompts/
  - Missing inline ref: phases.md
- `prompts\execute-dev-init-spec.prompt.md`
  - Missing inline ref: .hermes/plans/dev-init-spec.md
  - Missing inline ref: .hermes/plans/dev-init-spec.md
- `prompts\execute-hermes-configuration-spec.prompt.md`
  - Missing inline ref: .hermes/plans/hermes-configuration-spec.md
  - Missing inline ref: .hermes/plans/hermes-configuration-spec.md
- `prompts\execute-multi-agent-research.prompt.md`
  - Missing inline ref: .hermes/plans/2026-06-16_multi-agent-research.md
  - Missing inline ref: .hermes/plans/2026-06-16_multi-agent-research.md
- `prompts\features.prompt.md`
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\fedora-linux-triage.prompt.md`
  - Missing inline ref: systemctl
  - Missing inline ref: journalctl
  - Missing inline ref: dnf
  - Missing inline ref: firewalld
  - Missing inline ref: templates/fedora-linux-triage/
  - Missing inline ref: inputs.md
  - Missing inline ref: instructions.md
  - Missing inline ref: output_format.md
- `prompts\finalize-agent-prompt.prompt.md`
  - Missing inline ref:

## Template References

Templates in

- `prompts\first-ask.prompt.md`
  - Missing inline ref: templates/first-ask/
  - Missing inline ref: legacy_prompt_details.md
  - Missing inline ref: phases.md
- `prompts\folder-structure-blueprint-generator.prompt.md`
  - Missing inline ref: templates/folder-structure-blueprint-generator/configuration_variables.md
  - Missing inline ref: templates/folder-structure-blueprint-generator/generated_prompt.md
  - Missing inline ref: templates/folder-structure-blueprint-generator/
  - Missing inline ref: configuration_variables.md
  - Missing inline ref: generated_prompt.md
- `prompts\gen-specs-as-issues.prompt.md`
  - Missing inline ref: templates/gen-specs-as-issues/3_prioritization_phase.md
  - Missing inline ref: templates/gen-specs-as-issues/4_specification_developme.md
  - Missing inline ref: templates/gen-specs-as-issues/55_work_distribution_opti.md
  - Missing inline ref: templates/gen-specs-as-issues/
  - Missing inline ref: templates/gen-specs-as-issues/
  - Missing inline ref: 1_project_understanding_p.md
  - Missing inline ref: 2_gap_analysis_phase.md
  - Missing inline ref: 3_prioritization_phase.md
  - Missing inline ref: 4_specification_developme.md
  - Missing inline ref: 55_work_distribution_opti.md
  - Missing inline ref: 5_github_issue_creation_p.md
  - Missing inline ref: 6_final_review_phase.md
  - Missing inline ref: inputs.md
  - Missing inline ref: phases.md
  - Missing inline ref: rules.md
- `prompts\general.prompt.md`
  - Missing skill: brainstorming
  - Missing skill: plans-and-specs
  - Missing skill: dispatching-parallel-agents
  - Missing skill: subagent-driven-development
  - Missing skill: systematic-debugging
  - Missing skill: simplify
  - Missing skill: context7
  - Missing skill: plan
  - Missing skill: writing-skills
  - Missing skill: acpx-executor
  - Missing reference: introspection-only-general
  - Missing reference: no-git-delete
  - Missing reference: no-net-fetch
  - Missing reference: skills-tools-preflight-check
  - Missing reference: context-map
  - Missing reference: brainstorming
  - Missing reference: plans-and-specs
  - Missing reference: dispatching-parallel-agents
  - Missing reference: subagent-driven-development
  - Missing reference: systematic-debugging
  - Missing reference: simplify
  - Missing reference: context7
  - Missing reference: plan
  - Missing reference: writing-skills
  - Missing reference: acpx-executor
  - Missing inline ref: context-map
  - Missing inline ref: prompts/context-map.prompt.md
- `prompts\generate-custom-instructions-from-codebase.prompt.md`
  - Missing inline ref:
${MIGRATION_TYPE="Framework Version|Architecture Refactoring|Technology Migration|Dependencies Update|Pattern Changes"}
<!-- Type of migration or evolution -->

${SOURCE_REFERENCE="branch|commit|tag"}
<!-- Source reference point (before state) -->

${TARGET_REFERENCE="branch|commit|tag"}
<!-- Target reference point (after state) -->

${ANALYSIS_SCOPE="Entire project|Specific folder|Modified files only"}
<!-- Scope of analysis -->

${CHANGE_FOCUS="Breaking Changes|New Conventions|Obsolete Patterns|API Changes|Configuration"}
<!-- Main aspect of changes -->

${AUTOMATION_LEVEL="Conservative|Balanced|Aggressive"}
<!-- Level of automation for Copilot suggestions -->

${GENERATE_EXAMPLES="true|false"}
<!-- Include transformation examples -->

${VALIDATION_REQUIRED="true|false"}
<!-- Require validation before application -->

- Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\generate-docs.prompt.md`
  - Missing inline ref: templates/generate-docs/
  - Missing inline ref: phases.md
- `prompts\generator-orchestrator.prompt.md`
  - Missing inline ref: prompts
  - Missing inline ref: prompts
  - Missing inline ref: mode
  - Missing inline ref: full | quick | custom
  - Missing inline ref: templates/generator-orchestrator/rules.md
  - Missing inline ref: templates/generator-orchestrator/phases.md
  - Missing inline ref: templates/generator-orchestrator/steps.md
  - Missing inline ref: mode=full
  - Missing inline ref: validation-level=strict
  - Missing inline ref: templates/generator-orchestrator/
  - Missing inline ref: phases.md
  - Missing inline ref: rules.md
  - Missing inline ref: steps.md
- `prompts\git-flow-branch-creator.prompt.md`
  - Missing inline ref: templates/git-flow-branch-creator/
  - Missing inline ref: legacy_prompt_details.md
- `prompts\github-copilot-starter.prompt.md`
  - Missing inline ref: .github/copilot-instructions.md
  - Missing inline ref: templates/github-copilot-starter/configuration_files_to_create.md
  - Missing inline ref:

  - Missing inline ref:
project-root/
├── .github/
│   ├── copilot-instructions.md
│   ├── instructions/
│   │   ├── [language].instructions.md
│   │   ├── testing.instructions.md
│   │   ├── documentation.instructions.md
│   │   ├── security.instructions.md
│   │   ├── performance.instructions.md
│   │   └── code-review.instructions.md
│   ├── prompts/
│   │   ├── setup-component.prompt.md
│   │   ├── write-tests.prompt.md
│   │   ├── code-review.prompt.md
│   │   ├── refactor-code.prompt.md
│   │   ├── generate-docs.prompt.md
│   │   └── debug-issue.prompt.md
│   ├── agents/
│   │   ├── architect.agent.md
│   │   ├── reviewer.agent.md
│   │   └── debugger.agent.md
│   └── workflows/
│       └── copilot-setup-steps.yml

  - Missing inline ref:

## Execution Steps

1. **Analyze the provided technology stack**
2. **Create the directory structure**
3. **Generate main copilot-instructions.md with project-wide standards**
4. **Create language-specific instruction files using awesome-copilot references**
5. **Generate reusable prompts for common development tasks**
6. **Set up specialized chat modes for different development scenarios**
7. **Create the GitHub Actions workflow for Coding Agent** (

- Missing inline ref:

## Template References

Detailed templates in

- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\go-mcp-server-generator.prompt.md`
  - Missing inline ref:
myserver/
├── go.mod
├── go.sum
├── main.go
├── tools/
│   ├── tool1.go
│   └── tool2.go
├── resources/
│   └── resource1.go
├── config/
│   └── config.go
├── README.md
└── main_test.go

  - Missing inline ref:

## go.mod Template

- Missing inline ref: go
module github.com/yourusername/{{PROJECT_NAME}}

go 1.23

require (
    github.com/modelcontextprotocol/go-sdk v1.0.0
)

- Missing inline ref:

## tools/registry.go Template

- Missing inline ref: go
package tools

import "github.com/modelcontextprotocol/go-sdk/mcp"

func RegisterTools(server *mcp.Server) {
    RegisterTool1(server)
    RegisterTool2(server)
    // Register additional tools here
}

- Missing inline ref:

## config/config.go Template

- Missing inline ref:

## README.md Template

- Missing inline ref: markdown

# {{PROJECT_NAME}}

A Model Context Protocol (MCP) server built with Go.

## Description

{{PROJECT_DESCRIPTION}}

## Installation

\

- Missing inline ref:

## License

MIT

- Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\hermes-breakdown-epic-arch.prompt.md`
  - Missing inline ref: /docs/ways-of-work/plan/{epic-name}/epic.md
  - Missing inline ref: /docs/ways-of-work/plan/{epic-name}/arch.md
  - Missing inline ref: templates/hermes-breakdown-epic-arch/phases.md
  - Missing inline ref: templates/hermes-breakdown-epic-arch/
  - Missing inline ref: phases.md
- `prompts\hermes-breakdown-epic-pm.prompt.md`
  - Missing inline ref: /docs/ways-of-work/plan/{epic-name}/epic.md
  - Missing inline ref: templates/hermes-breakdown-epic-pm/phases.md
  - Missing inline ref: templates/hermes-breakdown-epic-pm/
  - Missing inline ref: phases.md
- `prompts\hermes-breakdown-feature-implementation.prompt.md`
  - Missing inline ref: /docs/ways-of-work/plan/{epic-name}/{feature-name}/prd.md
  - Missing inline ref: technical-breakdown.md
  - Missing inline ref: /docs/ways-of-work/plan/{epic-name}/{feature-name}/implementation-plan.md
  - Missing inline ref: templates/hermes-breakdown-feature-implementation/phases.md
  - Missing inline ref: templates/hermes-breakdown-feature-implementation/
  - Missing inline ref: phases.md
- `prompts\hermes-breakdown-feature-prd.prompt.md`
  - Missing inline ref: prd.md
  - Missing inline ref: /docs/ways-of-work/plan/{epic-name}/{feature-name}/prd.md
  - Missing inline ref: templates/hermes-breakdown-feature-prd/phases.md
  - Missing inline ref: templates/hermes-breakdown-feature-prd/
  - Missing inline ref: phases.md
- `prompts\hermes-breakdown-plan.prompt.md`
  - Missing inline ref: /docs/ways-of-work/plan/{epic-name}/epic.md
  - Missing inline ref: /docs/ways-of-work/plan/{epic-name}/{feature-name}/prd.md
  - Missing inline ref: technical-breakdown.md
  - Missing inline ref: implementation-plan.md
  - Missing inline ref: test-strategy.md
  - Missing inline ref: /docs/ways-of-work/plan/{epic-name}/{feature-name}/project-plan.md
  - Missing inline ref: /docs/ways-of-work/plan/{epic-name}/{feature-name}/issues-checklist.md
  - Missing inline ref: templates/hermes-breakdown-plan/phases.md
  - Missing inline ref: templates/hermes-breakdown-plan/
  - Missing inline ref: phases.md
- `prompts\hermes-breakdown-test.prompt.md`
  - Missing inline ref: technical-breakdown.md
  - Missing inline ref: implementation-plan.md
  - Missing inline ref: /docs/ways-of-work/plan/{epic}/{feature}/test-strategy.md
  - Missing inline ref: /docs/ways-of-work/plan/{epic}/{feature}/test-issues-checklist.md
  - Missing inline ref: /docs/ways-of-work/plan/{epic}/{feature}/qa-plan.md
  - Missing inline ref: templates/hermes-breakdown-test/phases.md
  - Missing inline ref: templates/hermes-breakdown-test/
  - Missing inline ref: phases.md
- `prompts\java-add-graalvm-native-image-support.prompt.md`
  - Missing inline ref: templates/java-add-graalvm-native-image-support/your_approach.md
  - Missing inline ref: templates/java-add-graalvm-native-image-support/framework-specific_considerati.md
  - Missing inline ref: --no-fallback
  - Missing inline ref: resource-config.json
  - Missing inline ref: --gc=serial
  - Missing inline ref: --gc=epsilon
  - Missing inline ref: templates/java-add-graalvm-native-image-support/
  - Missing inline ref: framework-specific_considerati.md
  - Missing inline ref: your_approach.md
- `prompts\java-docs.prompt.md`
  - Missing inline ref: @param
  - Missing inline ref: @return
  - Missing inline ref: @throws
  - Missing inline ref: @exception
  - Missing inline ref: @see
  - Missing inline ref: {@inheritDoc}
  - Missing inline ref: @param <T>
  - Missing inline ref: {@code}
  - Missing inline ref: <pre>{@code ... }</pre>
  - Missing inline ref: @since
  - Missing inline ref: @version
  - Missing inline ref: @author
  - Missing inline ref: @deprecated
- `prompts\java-junit.prompt.md`
  - Missing inline ref: src/test/java
  - Missing inline ref: junit-jupiter-api
  - Missing inline ref: junit-jupiter-engine
  - Missing inline ref: junit-jupiter-params
  - Missing inline ref: mvn test
  - Missing inline ref: gradle test
  - Missing inline ref: Test
  - Missing inline ref: CalculatorTest
  - Missing inline ref: Calculator
  - Missing inline ref: @Test
  - Missing inline ref: methodName_should_expectedBehavior_when_scenario
  - Missing inline ref: @BeforeEach
  - Missing inline ref: @AfterEach
  - Missing inline ref: @BeforeAll
  - Missing inline ref: @AfterAll
  - Missing inline ref: @DisplayName
  - Missing inline ref: @ParameterizedTest
  - Missing inline ref: @ValueSource
  - Missing inline ref: @MethodSource
  - Missing inline ref: Stream
  - Missing inline ref: Collection
  - Missing inline ref: @CsvSource
  - Missing inline ref: @CsvFileSource
  - Missing inline ref: @EnumSource
  - Missing inline ref: org.junit.jupiter.api.Assertions
  - Missing inline ref: assertEquals
  - Missing inline ref: assertTrue
  - Missing inline ref: assertNotNull
  - Missing inline ref: assertThat(...).is...
  - Missing inline ref: assertThrows
  - Missing inline ref: assertDoesNotThrow
  - Missing inline ref: assertAll
  - Missing inline ref: @Mock
  - Missing inline ref: @InjectMocks
  - Missing inline ref: @Tag
  - Missing inline ref: @Tag("fast")
  - Missing inline ref: @Tag("integration")
  - Missing inline ref: @TestMethodOrder(MethodOrderer.OrderAnnotation.class)
  - Missing inline ref: @Order
  - Missing inline ref: @Disabled
  - Missing inline ref: @Nested
  - Missing inline ref: templates/java-junit/
  - Missing inline ref: assertions.md
  - Missing inline ref: data-driven_parameterized.md
  - Missing inline ref: mocking_and_isolation.md
  - Missing inline ref: project_setup.md
  - Missing inline ref: standard_tests.md
  - Missing inline ref: test_organization.md
  - Missing inline ref: test_structure.md
- `prompts\java-mcp-server-generator.prompt.md`
  - Missing inline ref: templates/java-mcp-server-generator/project_generation.md
  - Missing inline ref: templates/java-mcp-server-generator/maven_pomxml_template.md
  - Missing inline ref: templates/java-mcp-server-generator/gradle_buildgradlekts_template.md
  - Missing inline ref: templates/java-mcp-server-generator/mcpserverapplicationjava_templ.md
  - Missing inline ref: templates/java-mcp-server-generator/tooldefinitionsjava_template.md
  - Missing inline ref: templates/java-mcp-server-generator/toolhandlersjava_template.md
  - Missing inline ref:

## README.md Template

- Missing inline ref: bash
mvn clean package

- Missing inline ref:

- Missing inline ref:

### Gradle

- Missing inline ref: bash
./gradlew build

- Missing inline ref:

## Run

### Maven

- Missing inline ref: bash
java -jar target/my-mcp-server-1.0.0.jar

- Missing inline ref:

### Gradle

- Missing inline ref: bash
./gradlew run

- Missing inline ref:

## Testing

### Maven

- Missing inline ref: bash
mvn test

- Missing inline ref:

### Gradle

- Missing inline ref: bash
./gradlew test

- Missing inline ref:

## Integration with Claude Desktop

Add to

- Missing inline ref:

## License

MIT

- Missing inline ref:

## Generation Instructions

1. **Ask for project name and package**
2. **Choose build tool** (Maven or Gradle)
3. **Generate all files** with proper package structure
4. **Use Reactive Streams** for async handlers
5. **Include comprehensive logging** with SLF4J
6. **Add tests** for all handlers
7. **Follow Java conventions** (camelCase, PascalCase)
8. **Include error handling** with proper responses
9. **Document public APIs** with Javadoc
10. **Provide both sync and async** examples

- Missing inline ref:

## Template References

Detailed section templates in

- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\java-refactoring-extract-method.prompt.md`
  - Missing inline ref: java
public FactLineBuilder setC_BPartner_ID_IfValid(final int bpartnerId) {
    assertNotBuild();
    if (bpartnerId > 0) {
        setC_BPartner_ID(bpartnerId);
    }
    return this;
}

  - Missing inline ref: java
public FactLineBuilder bpartnerIdIfNotNull(final BPartnerId bpartnerId) {
    if (bpartnerId != null) {
        return bpartnerId(bpartnerId);
    } else {
        return this;
    }
}
public FactLineBuilder setC_BPartner_ID_IfValid(final int bpartnerRepoId) {
    return bpartnerIdIfNotNull(BPartnerId.ofRepoIdOrNull(bpartnerRepoId));
}

  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\java-refactoring-remove-parameter.prompt.md`
  - Missing inline ref: java
public Backend selectBackendForGroupCommit(long tableId, ConnectContext context, boolean isCloud)
        throws LoadException, DdlException {
    if (!Env.getCurrentEnv().isMaster()) {
        try {
            long backendId = new MasterOpExecutor(context)
                    .getGroupCommitLoadBeId(tableId, context.getCloudCluster(), isCloud);
            return Env.getCurrentSystemInfo().getBackend(backendId);
        } catch (Exception e) {
            throw new LoadException(e.getMessage());
        }
    } else {
        return Env.getCurrentSystemInfo()
                .getBackend(selectBackendForGroupCommitInternal(tableId, context.getCloudCluster(), isCloud));
    }
}

  - Missing inline ref: java
public Backend selectBackendForGroupCommit(long tableId, ConnectContext context)
        throws LoadException, DdlException {
    if (!Env.getCurrentEnv().isMaster()) {
        try {
            long backendId = new MasterOpExecutor(context)
                    .getGroupCommitLoadBeId(tableId, context.getCloudCluster());
            return Env.getCurrentSystemInfo().getBackend(backendId);
        } catch (Exception e) {
            throw new LoadException(e.getMessage());
        }
    } else {
        return Env.getCurrentSystemInfo()
                .getBackend(selectBackendForGroupCommitInternal(tableId, context.getCloudCluster()));
    }
}

  - Missing inline ref: java
NodeImpl( long id, long firstRel, long firstProp )
{
     this( id, false );
}

  - Missing inline ref: java
NodeImpl( long id)
{
     this( id, false );
}

  - Missing inline ref:
-
- `prompts\java-springboot.prompt.md`
  - Missing inline ref: pom.xml
  - Missing inline ref: build.gradle
  - Missing inline ref: spring-boot-starter-web
  - Missing inline ref: spring-boot-starter-data-jpa
  - Missing inline ref: com.example.app.order
  - Missing inline ref: com.example.app.user
  - Missing inline ref: com.example.app.controller
  - Missing inline ref: com.example.app.service
  - Missing inline ref: private final
  - Missing inline ref: @Component
  - Missing inline ref: @Service
  - Missing inline ref: @Repository
  - Missing inline ref: @Controller
  - Missing inline ref: @RestController
  - Missing inline ref: application.yml
  - Missing inline ref: application.properties
  - Missing inline ref: @ConfigurationProperties
  - Missing inline ref: application-dev.yml
  - Missing inline ref: application-prod.yml
  - Missing inline ref: @Valid
  - Missing inline ref: @NotNull
  - Missing inline ref: @Size
  - Missing inline ref: @ControllerAdvice
  - Missing inline ref: @ExceptionHandler
  - Missing inline ref: @Service
  - Missing inline ref: @Transactional
  - Missing inline ref: JpaRepository
  - Missing inline ref: CrudRepository
  - Missing inline ref: @Query
  - Missing inline ref: private static final Logger logger = LoggerFactory.getLogger(MyClass.class);
  - Missing inline ref: logger.info("Processing user {}...", userId);
  - Missing inline ref: @SpringBootTest
  - Missing inline ref: @WebMvcTest
  - Missing inline ref: @DataJpaTest
  - Missing inline ref: templates/java-springboot/
  - Missing inline ref: configuration.md
  - Missing inline ref: data_layer_repositories.md
  - Missing inline ref: dependency_injection__com.md
  - Missing inline ref: logging.md
  - Missing inline ref: project_setup__structure.md
  - Missing inline ref: security.md
  - Missing inline ref: service_layer.md
  - Missing inline ref: testing.md
  - Missing inline ref: web_layer_controllers.md
- `prompts\javascript-typescript-jest.prompt.md`
  - Missing inline ref: expect(value).toBe(expected)
  - Missing inline ref: expect(value).toEqual(expected)
  - Missing inline ref: expect(value).toBeTruthy()
  - Missing inline ref: expect(value).toBeFalsy()
  - Missing inline ref: expect(value).toBeGreaterThan(3)
  - Missing inline ref: expect(value).toBeLessThanOrEqual(3)
  - Missing inline ref: expect(value).toMatch(/pattern/)
  - Missing inline ref: expect(value).toContain('substring')
  - Missing inline ref: expect(array).toContain(item)
  - Missing inline ref: expect(array).toHaveLength(3)
  - Missing inline ref: expect(object).toHaveProperty('key', value)
  - Missing inline ref: expect(fn).toThrow()
  - Missing inline ref: expect(fn).toThrow(Error)
  - Missing inline ref: expect(mockFn).toHaveBeenCalled()
  - Missing inline ref: expect(mockFn).toHaveBeenCalledWith(arg1, arg2)
  - Missing inline ref: templates/javascript-typescript-jest/
  - Missing inline ref: legacy_prompt_details.md
  - Missing inline ref: phases.md
- `prompts\kotlin-mcp-server-generator.prompt.md`
  - Missing inline ref:
myserver/
├── build.gradle.kts
├── settings.gradle.kts
├── gradle.properties
├── src/
│   ├── main/
│   │   └── kotlin/
│   │       └── com/example/myserver/
│   │           ├── Main.kt
│   │           ├── Server.kt
│   │           ├── config/
│   │           │   └── Config.kt
│   │           └── tools/
│   │               ├── Tool1.kt
│   │               └── Tool2.kt
│   └── test/
│       └── kotlin/
│           └── com/example/myserver/
│               └── ServerTest.kt
└── README.md

  - Missing inline ref:

## settings.gradle.kts Template

- Missing inline ref: kotlin
rootProject.name = "{{PROJECT_NAME}}"

- Missing inline ref:

## Main.kt Template

- Missing inline ref: kotlin
package com.example.myserver

import io.modelcontextprotocol.kotlin.sdk.server.StdioServerTransport
import kotlinx.coroutines.runBlocking
import io.github.oshai.kotlinlogging.KotlinLogging

private val logger = KotlinLogging.logger {}

fun main() = runBlocking {
    logger.info { "Starting MCP server..." }

    val config = loadConfig()
    val server = createServer(config)

    // Use stdio transport
    val transport = StdioServerTransport()

    logger.info { "Server '${config.name}' v${config.version} ready" }
    server.connect(transport)
}

- Missing inline ref:

## Config.kt Template

- Missing inline ref:

## tools/ToolRegistry.kt Template

- Missing inline ref: kotlin
package com.example.myserver.tools

import io.modelcontextprotocol.kotlin.sdk.server.Server

fun Server.registerTools() {
    registerTool1()
    registerTool2()
    // Register additional tools here
}

- Missing inline ref:

## README.md Template

- Missing inline ref:

## Multiplatform

This project uses Kotlin Multiplatform and can target JVM, Wasm, and iOS. See

- Missing inline ref:  for platform configuration.

## License

MIT

- Missing inline ref: kotlin
val transport = StdioServerTransport()
server.connect(transport)

- Missing inline ref:

### SSE Transport (Ktor)

- Missing inline ref: kotlin
embeddedServer(Netty, port = 8080) {
    mcp {
        Server(/*...*/) { "Description" }
    }
}.start(wait = true)

- Missing inline ref:

## Multiplatform Configuration

For multiplatform projects, add to

- Missing inline ref:

## Template References

Detailed templates in

- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\kotlin-springboot.prompt.md`
  - Missing inline ref: pom.xml
  - Missing inline ref: build.gradle
  - Missing inline ref: kotlin-maven-plugin
  - Missing inline ref: org.jetbrains.kotlin.jvm
  - Missing inline ref: kotlin-jpa
  - Missing inline ref: open
  - Missing inline ref: spring-boot-starter-web
  - Missing inline ref: spring-boot-starter-data-jpa
  - Missing inline ref: com.example.app.order
  - Missing inline ref: com.example.app.user
  - Missing inline ref: private val
  - Missing inline ref: val
  - Missing inline ref: var
  - Missing inline ref: @Service
  - Missing inline ref: @Repository
  - Missing inline ref: @RestController
  - Missing inline ref: application.yml
  - Missing inline ref: @ConfigurationProperties
  - Missing inline ref: data class
  - Missing inline ref: application-dev.yml
  - Missing inline ref: application-prod.yml
  - Missing inline ref: data class
  - Missing inline ref: equals()
  - Missing inline ref: hashCode()
  - Missing inline ref: toString()
  - Missing inline ref: copy()
  - Missing inline ref: @Valid
  - Missing inline ref: @NotNull
  - Missing inline ref: @Size
  - Missing inline ref: @ControllerAdvice
  - Missing inline ref: @ExceptionHandler
  - Missing inline ref: @Service
  - Missing inline ref: @Transactional
  - Missing inline ref: open
  - Missing inline ref: kotlin-jpa
  - Missing inline ref: ?
  - Missing inline ref: JpaRepository
  - Missing inline ref: CrudRepository
  - Missing inline ref:  or
  - Missing inline ref:  or
  - Missing inline ref:  to manage the lifecycle of coroutines.

## Template References

Templates in

- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\mcp-copilot-studio-server-generator.prompt.md`
  - Missing inline ref: templates/mcp-copilot-studio-server-generator/instructions.md
  - Missing inline ref: templates/mcp-copilot-studio-server-generator/expected_output.md
  - Missing inline ref:

## Template References

Templates in

- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\mcp-create-adaptive-cards.prompt.md`
  - Missing inline ref: templates/mcp-create-adaptive-cards/adaptive_card_types.md
  - Missing inline ref:

## Template References

Detailed templates in

- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\mcp-create-declarative-agent.prompt.md`
  - Missing inline ref: templates/mcp-create-declarative-agent/requirements.md
  - Missing inline ref: templates/mcp-create-declarative-agent/mcp_server_integration.md
  - Missing inline ref: response_semantics
  - Missing inline ref:

### Add Adaptive Cards (Optional)

See the

- Missing inline ref:  prompt for adding visual card templates.

## Environment Configuration

Create

- Missing inline ref:  or
- Missing inline ref: env
OAUTH_REFERENCE_ID=your-oauth-reference-id
CLIENT_ID=your-client-id
CLIENT_SECRET=your-client-secret

- Missing inline ref:

### Jira MCP Server

- Missing inline ref:

### Custom Service

- Missing inline ref:

## Template References

Detailed templates in

- Missing inline ref:
-
- `prompts\mcp-deploy-manage-agents.prompt.md`
  - Missing inline ref: templates/mcp-deploy-manage-agents/agent_types.md
  - Missing inline ref: templates/mcp-deploy-manage-agents/deployment_workflows.md
  - Missing inline ref:

## Template References

Detailed templates in

- Missing inline ref:
-
- `prompts\memory-merger.prompt.md`
  - Missing inline ref: /memory-merger >domain [scope]
  - Missing inline ref: global
  - Missing inline ref: user
  - Missing inline ref: workspace
  - Missing inline ref: ws
  - Missing inline ref: global
  - Missing inline ref: user
  - Missing inline ref: <global-prompts>
  - Missing inline ref: workspace
  - Missing inline ref: ws
  - Missing inline ref: <workspace-instructions>
  - Missing inline ref: <workspace-root>/.github/instructions/
  - Missing inline ref: <global-prompts>
  - Missing inline ref: <workspace-instructions>
  - Missing inline ref:
/memory-merger >domain-name [scope]

  - Missing inline ref:

-
  - Missing inline ref:  - Required. The domain to merge (e.g.,
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref: )
-
  - Missing inline ref: ,
  - Missing inline ref:  (both mean global),
  - Missing inline ref: , or
  - Missing inline ref: . Defaults to
  - Missing inline ref:  - merges global prompt engineering memories
-
  - Missing inline ref:  - merges workspace clojure memories
-
  - Missing inline ref:  →
  - Missing inline ref:  →
  - Missing inline ref:

## Example

- Missing inline ref:

## Template References

Templates in

- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\mkdocs-translations.prompt.md`
  - Missing inline ref: es
  - Missing inline ref: fr
  - Missing inline ref: pt-BR
  - Missing inline ref: ko
  - Missing inline ref: docs/docs/en
  - Missing inline ref: docs/docs/includes/en
  - Missing inline ref: docs/docs/en
  - Missing inline ref: docs/docs/includes/en
  - Missing inline ref: git checkout -b docs-translation-<language>
  - Missing inline ref: docs/docs/
  - Missing inline ref: es
  - Missing inline ref: fr
  - Missing inline ref: pt-BR
  - Missing inline ref: en
  - Missing inline ref: includes/en/introduction-event.md
  - Missing inline ref: includes/es/introduction-event.md
  - Missing inline ref: es
  - Missing inline ref: mkdocs.yml
  - Missing inline ref: locale
  - Missing inline ref: i18n
  - Missing inline ref: nav_translations
  - Missing inline ref: admonition_translations
  - Missing inline ref: templates/mkdocs-translations/translation_rules.md
  - Missing inline ref: docs/docs/includes/en
  - Missing inline ref: docs/docs/includes/
  - Missing inline ref: templates/mkdocs-translations/
  - Missing inline ref: folder_structure_and_outp.md
  - Missing inline ref: phases.md
  - Missing inline ref: translation_rules.md
- `prompts\model-recommendation.prompt.md`
  - Missing inline ref: .agent.md
  - Missing inline ref: .prompt.md
  - Missing inline ref: .agent.md
  - Missing inline ref: .prompt.md
  - Missing inline ref: templates/model-recommendation/workflow.md
  - Missing inline ref:

  - Missing inline ref:

## Template References

Detailed section templates in

- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\multi-agent-research-template.prompt.md`
  - Missing inline ref: {{workspace_root}}
  - Missing inline ref:  (resolves to
  - Missing inline ref: ) |
|
  - Missing inline ref:  |
  - Missing inline ref:  |
|
  - Missing inline ref:  |
  - Missing inline ref:  \|
  - Missing inline ref:  \|
  - Missing inline ref:  |
|
  - Missing inline ref:  | the active agent's planning or update command |
|
  - Missing inline ref:  | the active agent's search command |
|
  - Missing inline ref:  | the active agent's content extraction command |
|
  - Missing inline ref:  | the active agent's file read/write command |

## Agent Mapping

| Agent | Approach | Notes |
|-------|----------|-------|
| Codex | Use terminal commands and workspace-local file edits. | |
| Copilot | Use the equivalent Copilot workflow tools available in the current environment. | |
| Hermes | Use Hermes CLI commands exactly as written in the target steps. | |
| Fallback | If a capability is missing, choose the closest safe equivalent and note the substitution before continuing. | |

## Shared Rules

> These are guiding principles, not actionable tasks.

- [ ] If a plan already exists, update it before starting anything else.
- [ ] Research first, then extract, then write docs, then plan, then implement, then verify.
- [ ] Preserve the current research targets unless the user explicitly changes them.
- [ ] Keep each stage reversible and easy to resume.
- [ ] Write extracted findings to Markdown under
  - Missing inline ref:  if a plan already exists; update it.
- [ ] Execute Hermes skills browse to list everything available.
- [ ] Search and filter the top 50 best skills that are not already installed or available.
- [ ] Execute Hermes skills search with the skill name to find skills by keyword.
- [ ] Install all matching skills after a security scan.
- [ ] Run
  - Missing inline ref: .
- [ ] Run
  - Missing inline ref: .
- [ ] Identify all available profiles.
- [ ] Create profiles with
  - Missing inline ref: .
- [ ] Confirm the clones copy config, keys,
  - Missing inline ref:  ->
  - Missing inline ref:  ->
  - Missing inline ref:  ->
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref: )
- [ ] Frontmatter has recommended fields (
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref: )
- [ ]
  - Missing inline ref:  table is present and populated
- [ ] Phase headings use H2 (
  - Missing inline ref: ) not H3
- [ ] All phase task lists use
  - Missing inline ref:  checkbox format
- [ ] Phase 3 URLs are markdown links with descriptive titles
- [ ] Phase 2 "After research" uses Steps/Tasks structure
- [ ] Agent Mapping, Output Requirements, Verification Gates are markdown tables
- [ ] Core Workflow references phases (no duplicate detail)
- [ ] Template variables table uses inline code for paths
- [ ] No
  - Missing inline ref:  field in frontmatter
- [ ] Trigger matches filename stem convention
- [ ] File uses
  - Missing inline ref:  extension ✅ (renamed from
  - Missing inline ref: )

## Template References

Detailed templates in

- `prompts\multi-stage-dockerfile.prompt.md`
  - Missing inline ref: AS
  - Missing inline ref: python
  - Missing inline ref: .dockerignore
  - Missing inline ref: &&
  - Missing inline ref: USER
  - Missing inline ref: templates/multi-stage-dockerfile/
  - Missing inline ref: phases.md
- `prompts\my-issues.prompt.md`
  - Missing inline ref: templates/my-issues/
  - Missing inline ref: phases.md
- `prompts\my-pull-requests.prompt.md`
  - Missing inline ref: templates/my-pull-requests/
  - Missing inline ref: phases.md
- `prompts\next-intl-add-language.prompt.md`
  - Missing inline ref: templates/next-intl-add-language/
  - Missing inline ref: legacy_prompt_details.md
  - Missing inline ref: phases.md
- `prompts\nextjs-tailwind.prompt.md`
  - Missing inline ref: templates/nextjs-tailwind/phases.md
  - Missing inline ref: templates/nextjs-tailwind/
  - Missing inline ref: phases.md
- `prompts\openapi-to-application-code.prompt.md`
  - Missing inline ref: templates/openapi-to-application-code/generation_process.md
- `prompts\optimize-agentsMd.prompt.md`
  - Missing inline ref:

## Template References

Detailed templates in

- `prompts\performance.prompt.md`
  - Missing inline ref: templates/performance/phases.md
  - Missing inline ref: templates/performance/
  - Missing inline ref: phases.md
- `prompts\php-mcp-server-generator.prompt.md`
  - Missing inline ref:
{project-name}/
├── composer.json
├── .gitignore
├── README.md
├── server.php
├── src/
│   ├── Tools/
│   │   └── {ToolClass}.php
│   ├── Resources/
│   │   └── {ResourceClass}.php
│   ├── Prompts/
│   │   └── {PromptClass}.php
│   └── Providers/
│       └── {CompletionProvider}.php
└── tests/
    └── ToolsTest.php

  - Missing inline ref:

## Requirements

- PHP 8.2 or higher
- Composer

## Installation

- Missing inline ref: bash
composer install

- Missing inline ref:

- Missing inline ref:

## Usage

### Start Server (Stdio)

- Missing inline ref: bash
php server.php

- Missing inline ref:

### Configure in Claude Desktop

- Missing inline ref:

## Testing

- Missing inline ref: bash
vendor/bin/phpunit

- Missing inline ref: ,
- Missing inline ref: ,
- Missing inline ref:

## Resource Patterns

### Static Resource

- Missing inline ref:

### Dynamic Resource

- Missing inline ref:

## Running the Server

- Missing inline ref: bash

# Install dependencies

composer install

# Run tests

vendor/bin/phpunit

# Start server

php server.php

# Test with inspector

npx @modelcontextprotocol/inspector php server.php

- Missing inline ref:

## Claude Desktop Configuration

- Missing inline ref:

Now generate the complete project based on user requirements!

## Template References

Detailed templates in

- Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\plan-audit.prompt.md`
  - Missing skill: context-map
  - Missing skill: systematic-debugging
  - Missing skill: verification-before-completion
  - Missing skill: brainstorming
  - Missing skill: simplify
  - Missing skill: subagent-driven-development
  - Missing reference: context-map
  - Missing reference: systematic-debugging
  - Missing reference: verification-before-completion
  - Missing reference: brainstorming
  - Missing reference: simplify
  - Missing reference: subagent-driven-development
  - Missing inline ref: plan-acpx-agent-stack-audit-hermes
  - Missing inline ref: plan-acpx-agent-stack-audit-shared
  - Missing inline ref: plan-acpx-agent-stack-audit-copilot
  - Missing inline ref: hermes
  - Missing inline ref: copilot
  - Missing inline ref: shared
  - Missing inline ref: all
  - Missing inline ref: find ~/AppData/Local/hermes/skills/ -name "SKILL.md"
  - Missing inline ref: ls ~/AppData/Local/hermes/plugins/
  - Missing inline ref: grep -A5 'mcp_servers' ~/AppData/Local/hermes/config.yaml
  - Missing inline ref: .github/copilot-instructions.md
  - Missing inline ref: .github/agents/
  - Missing inline ref: .github/copilot-agent.md
  - Missing inline ref: docs/agent-stack-audit-report.md
  - Missing inline ref: docs/agent-stack-audit-report.md
- `prompts\plan-batch-fix.prompt.md`
  - Missing skill: systematic-debugging
  - Missing skill: subagent-driven-development
  - Missing skill: simplify
  - Missing skill: verification-before-completion
  - Missing skill: brainstorming
  - Missing reference: systematic-debugging
  - Missing reference: subagent-driven-development
  - Missing reference: simplify
  - Missing reference: verification-before-completion
  - Missing reference: brainstorming
  - Missing inline ref: plan-batch-fix-all-scan
  - Missing inline ref: plan-batch-fix-errors-warnings
  - Missing inline ref: tsc --noEmit
  - Missing inline ref: eslint .
  - Missing inline ref: pylint
  - Missing inline ref: cargo check
  - Missing inline ref:  approach.

1. Re-run the scan on the fixed files to confirm fix.
2.

- `prompts\plan-execute.prompt.md`
  - Missing skill: plans-and-specs
  - Missing skill: subagent-driven-development
  - Missing skill: verification-before-completion
  - Missing skill: writing-plans
  - Missing reference: plans-and-specs
  - Missing reference: subagent-driven-development
  - Missing reference: verification-before-completion
  - Missing reference: writing-plans
  - Missing inline ref: execute-plan-*
  - Missing inline ref: execute-*plan*
  - Missing inline ref: prompts/plan-xxx.prompt.md
  - Missing inline ref: .hermes/plans/xxx.md
  - Missing inline ref: git add && git commit
  - Missing inline ref: read_file
  - Missing inline ref: .hermes/plans/docs/<plan-name>-progress.md
- `prompts\plan-generate.prompt.md`
  - Missing skill: plans-and-specs
  - Missing skill: writing-plans
  - Missing skill: simplify
  - Missing skill: brainstorming
  - Missing skill: systematic-debugging
  - Missing skill: verification-before-completion
  - Missing reference: plans-and-specs
  - Missing reference: writing-plans
  - Missing reference: simplify
  - Missing reference: brainstorming
  - Missing reference: systematic-debugging
  - Missing reference: verification-before-completion
  - Missing inline ref: .prompt.md
  - Missing inline ref: .hermes/plans/
  - Missing inline ref: plan-execute
  - Missing inline ref: context-map
  - Missing inline ref: brainstorming
  - Missing inline ref: systematic-debugging
  - Missing inline ref:  or
  - Missing inline ref: .

1. Use

- Missing inline ref:  skill for structured plan writing.

1. Apply

- Missing inline ref: , validate frontmatter.

1. Run the plan through

- Missing inline ref:  for smoke-testing.

## Verification Checklist

- [ ] Goal is clearly stated and scoped
- [ ] All phases have explicit verification gates
- [ ] Every
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref:
- [ ] If
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref: ,
- `prompts\playwright-automation-fill-in-form.prompt.md`
  - Missing inline ref: webapp-testing
  - Missing inline ref: systematic-debugging
  - Missing inline ref: verification-before-completion
  - Missing inline ref: @browser
  - Missing inline ref: @checker
  - Missing inline ref: templates/playwright-automation-fill-in-form/phases.md
  - Missing inline ref:

## Template References

Templates in

- `prompts\playwright-explore-website.prompt.md`
  - Missing inline ref: webapp-testing
  - Missing inline ref: verification-before-completion
  - Missing inline ref: systematic-debugging
  - Missing inline ref: @explorer
  - Missing inline ref: @scribe
  - Missing inline ref: @tester
  - Missing inline ref: templates/playwright-explore-website/phases.md
  - Missing inline ref:

## Template References

Templates in

- `prompts\playwright-generate-test.prompt.md`
  - Missing inline ref: webapp-testing
  - Missing inline ref: test-driven-development
  - Missing inline ref: systematic-debugging
  - Missing inline ref: verification-before-completion
  - Missing inline ref: @investigator
  - Missing inline ref: @author
  - Missing inline ref: @runner
  - Missing inline ref: templates/playwright-generate-test/phases.md
  - Missing inline ref:

## Template References

Templates in

- `prompts\playwright-typescript.prompt.md`
  - Missing inline ref: templates/playwright-typescript/phases.md
  - Missing inline ref: templates/playwright-typescript/
  - Missing inline ref: phases.md
- `prompts\postgresql-code-review.prompt.md`
  - Missing inline ref: templates/postgresql-code-review/postgresql-specific_review_are.md
  - Missing inline ref: templates/postgresql-code-review/postgresql-specific_anti-patte.md
  - Missing inline ref: sql
-- ✅ Check if extension exists before creating
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";

-- ✅ Use extensions appropriately
-- UUID generation
SELECT uuid_generate_v4();

-- Password hashing
SELECT crypt('password', gen_salt('bf'));

-- Fuzzy text matching
SELECT word_similarity('postgres', 'postgre');

- Missing inline ref:

## 🛡️ PostgreSQL Security Review

### Row Level Security (RLS)

- Missing inline ref:

### Privilege Management

- Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\postgresql-optimization.prompt.md`
  - Missing inline ref: templates/postgresql-optimization/postgresql-specific_features.md
  - Missing inline ref: templates/postgresql-optimization/postgresql_performance_tuning.md
  - Missing inline ref: templates/postgresql-optimization/postgresql_advanced_data_types.md
  - Missing inline ref: templates/postgresql-optimization/postgresql_extensions__tools.md
  - Missing inline ref: sql
-- Identify slow queries
SELECT query, calls, total_time, mean_time, rows
FROM pg_stat_statements
ORDER BY total_time DESC
LIMIT 10;

-- Check index usage
SELECT schemaname, tablename, indexname, idx_scan, idx_tup_read, idx_tup_fetch
FROM pg_stat_user_indexes
WHERE idx_scan = 0;

- Missing inline ref:

## 🎯 Optimization Output Format

### Query Analysis Results

- Missing inline ref: sql
CREATE INDEX idx_table_column ON table(column);

- Missing inline ref:

## Template References

Detailed templates in

- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\power-apps-code-app-scaffold.prompt.md`
  - Missing inline ref: templates/power-apps-code-app-scaffold/task.md
  - Missing inline ref: templates/power-apps-code-app-scaffold/implementation_guidelines.md
  - Missing inline ref: pac code push
  - Missing inline ref: templates/power-apps-code-app-scaffold/
  - Missing inline ref: implementation_guidelines.md
  - Missing inline ref: task.md
- `prompts\power-bi-dax-optimization.prompt.md`
  - Missing inline ref: templates/power-bi-dax-optimization/analysis_framework.md
  - Missing inline ref: templates/power-bi-dax-optimization/optimization_process.md
  - Missing inline ref: templates/power-bi-dax-optimization/common_optimization_patte.md
  - Missing inline ref: templates/power-bi-dax-optimization/example_output_format.md
  - Missing inline ref: templates/power-bi-dax-optimization/additional_services.md
  - Missing inline ref: templates/power-bi-dax-optimization/
  - Missing inline ref: additional_services.md
  - Missing inline ref: analysis_framework.md
  - Missing inline ref: common_optimization_patte.md
  - Missing inline ref: example_output_format.md
  - Missing inline ref: optimization_process.md
  - Missing inline ref: request_instructions.md
- `prompts\power-bi-model-design-review.prompt.md`
  - Missing inline ref: templates/power-bi-model-design-review/review_framework.md
  - Missing inline ref: templates/power-bi-model-design-review/detailed_review_process.md
  - Missing inline ref: templates/power-bi-model-design-review/review_output_structure.md
  - Missing inline ref: templates/power-bi-model-design-review/review_checklist_templates.md
  - Missing inline ref: templates/power-bi-model-design-review/specialized_review_types.md
  - Missing inline ref: templates/power-bi-model-design-review/
  - Missing inline ref: detailed_review_process.md
  - Missing inline ref: review_checklist_templates.md
  - Missing inline ref: review_framework.md
  - Missing inline ref: review_output_structure.md
  - Missing inline ref: specialized_review_types.md
- `prompts\power-bi-performance-troubleshooting.prompt.md`
  - Missing inline ref: templates/power-bi-performance-troubleshooting/troubleshooting_methodology.md
  - Missing inline ref: templates/power-bi-performance-troubleshooting/diagnostic_tools_and_technique.md
  - Missing inline ref: templates/power-bi-performance-troubleshooting/solution_framework.md
  - Missing inline ref: templates/power-bi-performance-troubleshooting/troubleshooting_workflows.md
  - Missing inline ref: templates/power-bi-performance-troubleshooting/performance_monitoring_setup.md
  - Missing inline ref: templates/power-bi-performance-troubleshooting/communication_and_documentatio.md
  - Missing inline ref: templates/power-bi-performance-troubleshooting/
  - Missing inline ref: communication_and_documentatio.md
  - Missing inline ref: diagnostic_tools_and_technique.md
  - Missing inline ref: performance_monitoring_setup.md
  - Missing inline ref: solution_framework.md
  - Missing inline ref: troubleshooting_methodology.md
  - Missing inline ref: troubleshooting_workflows.md
- `prompts\power-bi-report-design-consultation.prompt.md`
  - Missing inline ref: templates/power-bi-report-design-consultation/design_consultation_framework.md
  - Missing inline ref: templates/power-bi-report-design-consultation/visualization_design_process.md
  - Missing inline ref: templates/power-bi-report-design-consultation/design_review_and_validation.md
  - Missing inline ref: templates/power-bi-report-design-consultation/visualization_recommendations_.md
  - Missing inline ref: templates/power-bi-report-design-consultation/
  - Missing inline ref: design_consultation_framework.md
  - Missing inline ref: design_review_and_validation.md
  - Missing inline ref: visualization_design_process.md
  - Missing inline ref: visualization_recommendations_.md
- `prompts\power-platform-mcp-connector-suite.prompt.md`
  - Missing inline ref: apiDefinition.swagger.json
  - Missing inline ref: apiProperties.json
  - Missing inline ref: script.csx
  - Missing inline ref: readme.md
  - Missing inline ref: /mcp
  - Missing inline ref: $ref
  - Missing inline ref: ["string", "number"]
  - Missing inline ref: x-ms-agentic-protocol
  - Missing inline ref: POST /mcp
  - Missing inline ref: iconBrandColor
  - Missing inline ref: templates/power-platform-mcp-connector-suite/validation_checklist.md
  - Missing inline ref:

## Template References

Detailed templates in

- `prompts\project-workflow-analysis-blueprint-generator.prompt.md`
  - Missing inline ref:
${PROJECT_TYPE="Auto-detect|.NET|Java|Spring|Node.js|Python|React|Angular|Microservices|Other"}
<!-- Primary technology stack -->

${ENTRY_POINT="API|GraphQL|Frontend|CLI|Message Consumer|Scheduled Job|Custom"}
<!-- Starting point for the flow -->

${PERSISTENCE_TYPE="Auto-detect|SQL Database|NoSQL Database|File System|External API|Message Queue|Cache|None"}
<!-- Data storage type -->

${ARCHITECTURE_PATTERN="Auto-detect|Layered|Clean|CQRS|Microservices|MVC|MVVM|Serverless|Event-Driven|Other"}
<!-- Primary architecture pattern -->

${WORKFLOW_COUNT=1-5}
<!-- Number of workflows to document -->

${DETAIL_LEVEL="Standard|Implementation-Ready"}
<!-- Level of implementation detail to include -->

${INCLUDE_SEQUENCE_DIAGRAM=true|false}
<!-- Generate sequence diagram -->

${INCLUDE_TEST_PATTERNS=true|false}
<!-- Include testing approach -->

- Missing inline ref:

## Template References

Detailed templates in

- `prompts\projects-init.prompt.md`
  - Missing skill: enhance-markdown
  - Missing skill: hermes-skills
  - Missing skill: skill-creator
  - Missing reference: enhance-markdown
  - Missing reference: hermes-skills
  - Missing reference: skill-creator
  - Missing inline ref: prompts/
  - Missing inline ref: projects-init.prompt.txt
  - Missing inline ref: pwd
  - Missing inline ref: docs/
  - Missing inline ref: prompts/
  - Missing inline ref: prompts/
  - Missing inline ref: ~/AppData/Local/hermes/skills/
  - Missing inline ref: enhance-markdown
  - Missing inline ref: hermes-skills
  - Missing inline ref: skill-creator
  - Missing inline ref: rm
  - Missing inline ref: pwd
  - Missing inline ref: docs/**
  - Missing inline ref: templates/projects-init/phase_1_triage_documentat.md
  - Missing inline ref: prompts/
  - Missing inline ref: pwd
  - Missing inline ref: prompts/
  - Missing inline ref: templates/projects-init/phase_2_migrate_prompts.md
  - Missing inline ref: prompts/
  - Missing inline ref: prompts/**
  - Missing inline ref: templates/projects-init/phase_3_create_skills__up.md
  - Missing inline ref: pwd
  - Missing inline ref: docs/**
  - Missing inline ref: pwd
  - Missing inline ref: prompts/
  - Missing inline ref: prompts/
  - Missing inline ref: prompts/
  - Missing inline ref: templates/projects-init/
  - Missing inline ref: templates/projects-init/
  - Missing inline ref: actions_summary.md
  - Missing inline ref: context.md
  - Missing inline ref: description.md
  - Missing inline ref: phase_1_triage_documentat.md
  - Missing inline ref: phase_2_migrate_prompts.md
  - Missing inline ref: phase_3_create_skills__up.md
  - Missing inline ref: rules.md
  - Missing inline ref: skills_required.md
- `prompts\prompt-builder.prompt.md`
  - Missing inline ref: .prompt.md
  - Missing inline ref: .prompt.md
  - Missing inline ref: ask
  - Missing inline ref: agent
  - Missing inline ref: edit
  - Missing inline ref: .prompt.md
  - Missing inline ref: .prompt.md
  - Missing inline ref: /context-map
  - Missing inline ref: codebase
  - Missing inline ref: search
  - Missing inline ref: editFiles
  - Missing inline ref: fetch
  - Missing inline ref: runCommands
  - Missing inline ref: runCommands
  - Missing inline ref: editFiles
  - Missing inline ref: codebase
  - Missing inline ref: search
  - Missing inline ref: editFiles
  - Missing inline ref: .prompt.md
  - Missing inline ref: ask
  - Missing inline ref: edit
  - Missing inline ref: agent
  - Missing inline ref: ask
  - Missing inline ref: edit
  - Missing inline ref: agent
  - Missing inline ref: context-map
  - Missing inline ref: writing-plans
  - Missing inline ref: writing-skills
  - Missing inline ref: prompt-engineering
  - Missing inline ref: templates/prompt-builder/phases.md
  - Missing inline ref: edit
  - Missing inline ref: .prompt.md
  - Missing inline ref: templates/prompt-builder/
  - Missing inline ref: phases.md
- `prompts\prompt-management.prompt.md`
  - Missing skill: brainstorming
  - Missing skill: plans-and-specs
  - Missing skill: writing-plans
  - Missing skill: simplify
  - Missing skill: systematic-debugging
  - Missing skill: dispatching-parallel-agents
  - Missing skill: subagent-driven-development
  - Missing skill: test-driven-development
  - Missing skill: skill-creator
  - Missing skill: writing-skills
  - Missing skill: test-skill
  - Missing skill: verification-before-completion
  - Missing reference: brainstorming
  - Missing reference: plans-and-specs
  - Missing reference: writing-plans
  - Missing reference: simplify
  - Missing reference: systematic-debugging
  - Missing reference: dispatching-parallel-agents
  - Missing reference: subagent-driven-development
  - Missing reference: test-driven-development
  - Missing reference: skill-creator
  - Missing reference: writing-skills
  - Missing reference: verification-before-completion
  - Missing inline ref: prompts/
  - Missing inline ref: frontmatter
  - Missing inline ref: name/title/version/description/tags
  - Missing inline ref: prompts/
  - Missing inline ref: name
  - Missing inline ref: title
  - Missing inline ref: dependencies
  - Missing inline ref: .prompt.md
  - Missing inline ref: name
  - Missing inline ref: title
  - Missing inline ref: description
  - Missing inline ref: version
  - Missing inline ref: tags
  - Missing inline ref: version
  - Missing inline ref: tags
  - Missing inline ref: prompts/
  - Missing inline ref: prompts/*.prompt.md
  - Missing inline ref: templates/<prompt-name>/
  - Missing inline ref: *.prompt.md
  - Missing inline ref: name
  - Missing inline ref: title
  - Missing inline ref: description
  - Missing inline ref: version
  - Missing inline ref: tags
  - Missing inline ref: dependencies
  - Missing inline ref: skills
  - Missing inline ref: frontmatter_valid
  - Missing inline ref: references_exist
  - Missing inline ref: potential_duplicate
  - Missing inline ref: docs/prompt-inventory.md
  - Missing inline ref: last_updated
  - Missing inline ref: name
  - Missing inline ref: title
  - Missing inline ref: prompts/*.prompt.md
  - Missing inline ref: dependencies
  - Missing inline ref: docs/prompt-inventory.md
  - Missing inline ref: deleted
  - Missing inline ref: references_updated
  - Missing inline ref:
|
  - Missing inline ref:  | <one-line purpose> |

  - Missing inline ref:

or

- Missing inline ref:

### <prompt-name>

| Skill | Purpose |
...

- Missing inline ref:

### 3.4 Register templates

Update

- Missing inline ref:
- Frontmatter uses keys from
  - Missing inline ref:
  - skills under
  - Missing inline ref:

### 4.3 Keep templates drivable

Each prompt must remain directly executable as a standalone prompt file.

### 4.4 Apply atomic changes

Use

- Missing inline ref:  for in-place updates. Use
- Missing inline ref:  from prompt
- Missing inline ref:  and
- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:  or
  - Missing inline ref:  is non-empty
-
  - Missing inline ref:  is semver-like
- all
  - Missing inline ref:  dependencies exist
- all
  - Missing inline ref:  dependencies are valid Hermes tools
- all
  - Missing inline ref:
-
  - Missing inline ref:
- updated
  - Missing inline ref:  files using templates
- updated
  - Missing inline ref:
- any newly created skills/scripts under
- `prompts\prompts-fix.prompt.md`
  - Missing skill: brainstorming
  - Missing skill: plans-and-specs
  - Missing skill: dispatching-parallel-agents
  - Missing skill: subagent-driven-development
  - Missing skill: systematic-debugging
  - Missing skill: simplify
  - Missing skill: acpx-executor
  - Missing skill: hermes-agent
  - Missing skill: copilot-cli-quickstart
  - Missing inline ref: search_files(pattern="*.prompt.md", target="files")
  - Missing inline ref: read_file(path)
  - Missing inline ref: patch(path, old_string, new_string)
  - Missing inline ref: write_file(path, content)
  - Missing inline ref: delegate_task(goal, toolsets)
  - Missing inline ref: skill_view(name="acpx-executor")
- `prompts\prompts-strict-template.prompt.md`
  - Missing inline ref: templates/prompts-strict-template/phases.md
  - Missing inline ref: templates/prompts-strict-template/
  - Missing inline ref: phases.md
- `prompts\pytest-coverage.prompt.md`
  - Missing inline ref: templates/pytest-coverage/
  - Missing inline ref: legacy_prompt_details.md
  - Missing inline ref: phases.md
- `prompts\python-mcp-server-generator.prompt.md`
  - Missing inline ref: uv init project-name
  - Missing inline ref: uv add "mcp[cli]"
  - Missing inline ref: templates/python-mcp-server-generator/implementation_details.md
  - Missing inline ref: uv run mcp dev server.py
  - Missing inline ref: uv run mcp install server.py
  - Missing inline ref: stateless_http=True
  - Missing inline ref: json_response=True
  - Missing inline ref: python server.py
  - Missing inline ref: uv run server.py
  - Missing inline ref: python server.py
  - Missing inline ref: uv run mcp dev server.py
  - Missing inline ref: uv run mcp install server.py
  - Missing inline ref: templates/python-mcp-server-generator/
  - Missing inline ref: implementation_details.md
  - Missing inline ref: phases.md
- `prompts\quality-gate-debugger.prompt.md`
  - Missing inline ref: templates/quality-gate-debugger/phase_0_generate_reports.md
  - Missing inline ref: templates/quality-gate-debugger/phase_1_triage.md
  - Missing inline ref: @/
  - Missing inline ref: ui/
  - Missing inline ref: database/
  - Missing inline ref: any
  - Missing inline ref: unknown
  - Missing inline ref:

## Constraints

- **Never skip a report file** — read all that exist.
- **Never introduce new errors** — verify after each batch of fixes.
- **Stay in scope** — only fix issues surfaced by the report files.
- **Document rationale** — for non-obvious fixes, add a brief inline comment.
- **PowerShell-safe** — use
  - Missing inline ref:  instead of
  - Missing inline ref: , use Zod, auth-first, DAL patterns).

## Next action

Run the quality-gate script to generate fresh report files. After that the triage step will parse the report files and produce the triage table.

## Template References

Detailed templates in

- Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\readme-blueprint-generator.prompt.md`
  - Missing inline ref: templates/readme-blueprint-generator/
  - Missing inline ref: legacy_prompt_details.md
  - Missing inline ref: phases.md
- `prompts\refactor-code.prompt.md`
  - Missing inline ref: templates/refactor-code/steps.md
  - Missing inline ref: templates/refactor-code/
  - Missing inline ref: phases.md
  - Missing inline ref: steps.md
- `prompts\refactor-mardown-files.prompt.md`
  - Missing inline ref: AGENTS.md
  - Missing inline ref: .github/copilot-instructions.md
  - Missing inline ref: AGENTS.md
  - Missing inline ref: .cursorrules
  - Missing inline ref: .github/copilot-instructions.md
  - Missing inline ref: AGENTS.md
  - Missing inline ref: .cursorrules
  - Missing inline ref: .github/copilot-instructions.md
  - Missing inline ref: docs/*.md
  - Missing inline ref: *.md
  - Missing inline ref: README.md
  - Missing inline ref: .github/instructions/documentation.instructions.md
  - Missing inline ref: AGENTS.md
  - Missing inline ref: .cursorrules
  - Missing inline ref:

## 4. Output Requirements

- Produce fully rewritten versions of
  - Missing inline ref: ,
  - Missing inline ref:  and
  - Missing inline ref: ,
  - Missing inline ref:  and
  - Missing inline ref: .

## 5. Tool & Capability Requirements

- File system access to read/write
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref: , and reference files.
- Markdown linting and formatting tools (e.g.,
  - Missing inline ref: ).
- Codebase search tools to resolve file paths, section headings, and code samples.
- Date and metadata insertion for “Last Updated” sections.
- Diátaxis and documentation skills, referencing
  - Missing inline ref: ,
  - Missing inline ref:  for validation.
- Load and apply
  - Missing inline ref:  and other relevant instructions.
- Output must be valid markdown, ready for direct commit.

## 7. Quality & Validation Criteria

- All instructions must be clear, concise, and actionable.
- All references must be accurate and up-to-date.
- Output must pass markdown linting and render correctly.
- All required sections must be present and fully populated.
- Run
  - Missing inline ref:  to ensure no regressions.
- Adhere to Banking documentation standards and Diátaxis principles.
- Include “Last Updated” and, if needed, “Migration Notes” sections.
- Output must be peer-reviewed and approved before commit.

## Template References

Detailed templates in

- `prompts\refactor-method-complexity-reduce.prompt.md`
  - Missing inline ref: templates/refactor-method-complexity-reduce/instructions.md
  - Missing inline ref: templates/refactor-method-complexity-reduce/
  - Missing inline ref: instructions.md
- `prompts\refactor-plan.prompt.md`
  - Missing inline ref:

## Template References

Templates in

- Missing inline ref:
-
- `prompts\refresh-agent-inventory.prompt.md`
  - Missing inline ref: templates/refresh-agent-inventory/
  - Missing inline ref: phases.md
- `prompts\remember-interactive-programming.prompt.md`
  - Missing inline ref: templates/remember-interactive-programming/
  - Missing inline ref: phases.md
- `prompts\remember.prompt.md`
  - Missing inline ref: /remember [>domain [scope]] lesson clue
  - Missing inline ref: global
  - Missing inline ref: user
  - Missing inline ref: workspace
  - Missing inline ref: ws
  - Missing inline ref: global
  - Missing inline ref: user
  - Missing inline ref: <global-prompts>
  - Missing inline ref: workspace
  - Missing inline ref: ws
  - Missing inline ref: <workspace-instructions>
  - Missing inline ref: <workspace-root>/.github/instructions/
  - Missing inline ref: <global-prompts>
  - Missing inline ref: <workspace-instructions>
  - Missing inline ref:
/remember [>domain-name [scope]] lesson content

  - Missing inline ref:

-
  - Missing inline ref:  - Optional. Explicitly target a domain (e.g.,
  - Missing inline ref: ,
  - Missing inline ref: )
-
  - Missing inline ref: ,
  - Missing inline ref:  (both mean global),
  - Missing inline ref: , or
  - Missing inline ref: . Defaults to
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:

### Tag Line

Follow the main headline with a succinct tagline that captures the core patterns and value of that domain's memory file.

### Learnings

Each distinct lesson has its own level 2 headline

## Process

> 1. **Parse input** - Extract domain (if
>
- Missing inline ref:  specified) and scope (
- Missing inline ref: templates/remember/process.md
- Missing inline ref: templates/remember/
- Missing inline ref: process.md
- `prompts\repo-management.prompt.md`
  - Missing skill: git-helper
  - Missing skill: repo-research-pipeline
  - Missing skill: web-research-pipeline
  - Missing skill: github-repo-management
  - Missing skill: finishing-a-development-branch
  - Missing skill: workspace-audit
  - Missing reference: git-helper
  - Missing reference: repo-research-pipeline
  - Missing reference: web-research-pipeline
  - Missing reference: github-repo-management
  - Missing reference: finishing-a-development-branch
  - Missing reference: workspace-audit
  - Missing inline ref: development
  - Missing inline ref: production
  - Missing inline ref: .gitignore
  - Missing inline ref: repo-research-pipeline
  - Missing inline ref: development
  - Missing inline ref: production
  - Missing inline ref: production
  - Missing inline ref: bash
git branch | grep -v -E "development|production" | xargs -r git branch -D
git push origin --delete <branch> || true
gh repo edit <owner>/<repo> --default-branch production

  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref:  |
  - Missing inline ref:  for vulns |
| Python |
  - Missing inline ref:  |
  - Missing inline ref:  per repo type (JS/TS uses
  - Missing inline ref: , Python uses
- `prompts\repo-research-pipeline.prompt.md`
  - Missing skill: repo-research-pipeline
  - Missing skill: web-research-pipeline
  - Missing skill: mcp-github
  - Missing skill: mcp-fetch
  - Missing skill: domain-intel
  - Missing reference: repo-research-pipeline
  - Missing reference: web-research-pipeline
  - Missing reference: mcp-github
  - Missing reference: mcp-fetch
  - Missing reference: domain-intel
  - Missing inline ref: repo-research-pipeline
  - Missing inline ref: web-research-pipeline
- `prompts\repo-story-time.prompt.md`
  - Missing skill: code-wiki
  - Missing skill: writing-clearly-and-concisely
  - Missing reference: code-wiki
  - Missing reference: writing-clearly-and-concisely
  - Missing inline ref: bash
git log --oneline --since="1 year ago" | wc -l        # commit count
git shortlog -sn                                       # contributor stats
git diff --stat origin/main..HEAD | tail -3            # recent changes
ls -la projects/<name>/src                             # structure overview

  - Missing inline ref:  | Overview, Architecture, Key Components, Technologies, Data Flow, Team |
|
  - Missing inline ref:  | Year-in-numbers, Contributors, Seasonal Patterns, Themes, Plot Twists, Current Chapter |

## Rules

1. **Be Specific** — Use actual file names, commit messages, and contributor names.
2. **Evidence-Based** — Support observations with actual git data (never fabricate).
3. **Write files, don't print content** — Use

- `prompts\repo.prompt.md`
  - Missing prompt dependency: context-map
  - Missing prompt dependency: update-implementation-plan
  - Missing skill: brainstorming
  - Missing skill: plans-and-specs
  - Missing skill: systematic-debugging
  - Missing skill: context7
  - Missing skill: spike
  - Missing skill: writing-skills
  - Missing skill: content-research-writer
  - Missing prompt dependency: repo-management
  - Missing prompt dependency: repo-story-time
  - Missing prompt dependency: web-research-pipeline
  - Missing prompt dependency: repo-research-pipeline
  - Missing reference: brainstorming
  - Missing reference: plans-and-specs
  - Missing reference: systematic-debugging
  - Missing reference: context7
  - Missing reference: spike
  - Missing reference: writing-skills
  - Missing reference: content-research-writer
  - Missing inline ref: projects/
  - Missing inline ref: RESEARCH_REPORT.md
  - Missing inline ref: RESEARCH_REPORT.md
  - Missing inline ref: ## Report Template
  - Missing inline ref: RESEARCH_REPORT.md
  - Missing inline ref: projects/RESEARCH_INDEX.md
  - Missing inline ref: $HOME/Desktop/SandBox
  - Missing inline ref: context7
  - Missing inline ref: web_search
  - Missing inline ref: dispatching-parallel-agents
  - Missing inline ref: ## Related Projects
  - Missing inline ref: AGENTS.md
  - Missing inline ref: web_search
  - Missing inline ref: pwd
  - Missing inline ref: $HOME/Desktop/SandBox
  - Missing inline ref: find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md' | sort
  - Missing inline ref: web_search
  - Missing inline ref: pwd
  - Missing inline ref:
web_search("Next.js 16 best practices 2026", limit=1)
terminal("pwd")
terminal("find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md' | sort")
terminal("find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md' | wc -l")

  - Missing inline ref: .

> Orchestrator at

- Missing inline ref:  and
- Missing inline ref:  to extract tech stack.

1. Run

- Missing inline ref:  per project using the template in
- Missing inline ref:
read_file("projects/<name>/RESEARCH_REPORT.md")         # if exists — for UPDATE
write_file("projects/<name>/RESEARCH_REPORT.md", content=<report>)
web_extract([url1, url2, url3])                          # verify key links

- Missing inline ref:

1. Rewrite

- Missing inline ref:  — 14 rows, file size, last-updated date.

1. For each report, verify

- Missing inline ref:
terminal("find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md' -exec ls -lh {} \;")
write_file("projects/RESEARCH_INDEX.md", content=<updated index>)

- Missing inline ref:
terminal("find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md' | wc -l")
terminal("for f in projects/*/RESEARCH_REPORT.md; do echo \"=== $f ===\"; grep -c '^## ' \"$f\"; wc -c \"$f\"; done")

- Missing inline ref:

---

## Report Template

Every

- Missing inline ref:  must follow this structure exactly. Do not add or remove
top-level sections. Subsections under
- Missing inline ref:  are tech-specific and variable.

- Missing inline ref:

---

## Acceptance Criteria

| Gate | Condition | Verification Command |
|------|-----------|----------------------|
| All 14 reports exist | count = 14 |

- Missing inline ref:  |
| Each report ≥ 9 sections |
- Missing inline ref:  ≥ 9 | per-report loop |
| No report under 1KB |
- Missing inline ref:  ≥ 1024 | per-report loop |
| No report over 5KB |
- Missing inline ref:  ≤ 5120 | per-report loop |
| 28 URL spot-checks pass |
- Missing inline ref:  non-404 | Phase 4 step 3 |
| RESEARCH_INDEX.md current | 14 rows, size + date correct | read + verify |
| No fabricated findings | every fact traces to
- Missing inline ref:  | manual review |
| Scope respected | no branch/migration work started | agent self-check |
| Sub-prompts accessible |
- Missing inline ref: ](templates/_shared/skills-table-core.md#repo)

| Skill | Phase | Purpose |
|-------|-------|---------|
|

- Missing inline ref:  | 1 | Explore research angles per project |
|
- Missing inline ref:  | 0 | Structure research plan |
|
- Missing inline ref:  | 0, 4 | Detect stale/missing reports |
|
- Missing inline ref:  | 1 | Library API docs and patterns |
|
- Missing inline ref:  | 0 | Prototype report format before batch |
|
- Missing inline ref:  | 2 | Crisp, compact markdown writing |
|
- Missing inline ref:  | 2 | Research synthesis |
|
- Missing inline ref:  | — | Git history analysis and repo narrative |
|
- Missing inline ref:  | 1 | Delegated web search + extraction |
|
- Missing inline ref:  | 1 | Multi-project research orchestrator |

---

## Actions

-
  - Missing inline ref:  — Search for guides, similar projects, cheatsheets
-
  - Missing inline ref:  — Extract content from URLs; verify links before embedding
-
  - Missing inline ref:  — Read project description
-
  - Missing inline ref:  — Read tech stack and setup commands
-
  - Missing inline ref:  — Read existing report for UPDATE
-
  - Missing inline ref:  — Create or update RESEARCH_REPORT.md
-
  - Missing inline ref:  — Count reports
-
  - Missing inline ref:  — Check sizes
-
  - Missing inline ref:  — Verify sections
-
  - Missing inline ref:  — Load research writing skill
-
  - Missing inline ref:  — Load crisp writing skill
-
  - Missing inline ref:  — Delegate per-project research
-
  - Missing inline ref:  — Research 3–4 projects concurrently
-
  - Missing inline ref:  with
  - Missing inline ref:  prompt — Per-project web research
-
  - Missing inline ref:  — Load sub-prompt orchestrator

---

## Secondary Goals

> Execute ONLY after Phase 5 verification passes for all 14 reports.
> Full specifications live in

- Missing inline ref: .

| # | Goal | Priority |
|---|------|----------|
| 1 | Consolidation — comicwise + Django-Scrapy-Selenium + selenium_webdriver → rhixecompany-comics | P1 |
| 2 | Branch normalization —

- Missing inline ref:  +
- Missing inline ref:  only per repo | P2 |
| 3 | Ignore file audit — fix all
- Missing inline ref:  files | P3 |
| 4 | Dependency audit — clean package.json / requirements.txt | P4 |
| 5 | Bun migration — npm/pnpm → bun for JS/TS repos | P5 |
| 6 | CI workflow setup — GitHub Actions for all repos | P6 |

---

## Related Prompts

| Prompt | Location | Purpose |
|--------|----------|---------|
|

- Missing inline ref:  |
- Missing inline ref:  | Script modernization for all 14 projects |
|
- Missing inline ref:  |
- Missing inline ref:  | Workspace-level consolidation |
|
- Missing inline ref:  |
- Missing inline ref:  | Branch norm, Bun migration, CI, consolidation |
|
- Missing inline ref:  |
- Missing inline ref:  | Git history analysis and repo narrative |
|
- Missing inline ref:  |
- Missing inline ref:  | Web search + extraction per project |
|
- Missing inline ref:  |
- Missing inline ref:  | Multi-project research orchestrator |

## Template References

Templates in

- `prompts\review-and-refactor.prompt.md`
  - Missing inline ref: .github/instructions/*.md
  - Missing inline ref: .github/copilot-instructions.md
  - Missing inline ref: templates/review-and-refactor/
  - Missing inline ref: phases.md
- `prompts\ruby-mcp-server-generator.prompt.md`
  - Missing inline ref:
my-mcp-server/
├── Gemfile
├── Rakefile
├── lib/
│   ├── my_mcp_server.rb
│   ├── my_mcp_server/
│   │   ├── server.rb
│   │   ├── tools/
│   │   │   ├── greet_tool.rb
│   │   │   └── calculate_tool.rb
│   │   ├── prompts/
│   │   │   └── code_review_prompt.rb
│   │   └── resources/
│   │       └── example_resource.rb
├── bin/
│   └── mcp-server
├── test/
│   ├── test_helper.rb
│   └── tools/
│       ├── greet_tool_test.rb
│       └── calculate_tool_test.rb
└── README.md

  - Missing inline ref:

## Gemfile Template

- Missing inline ref:

## Rakefile Template

- Missing inline ref:

## lib/my_mcp_server.rb Template

- Missing inline ref:

## bin/mcp-server Template

- Missing inline ref: bash
chmod +x bin/mcp-server

- Missing inline ref:

## test/test_helper.rb Template

- Missing inline ref:

## README.md Template

- Missing inline ref: bash
bundle install

- Missing inline ref:

- Missing inline ref: bash
bundle exec rake test

- Missing inline ref: bash
bundle exec rake rubocop

- Missing inline ref: bash
bundle exec rake

- Missing inline ref:

## Integration with Claude Desktop

Add to

- Missing inline ref:

## Project Structure

- Missing inline ref:
my-mcp-server/
├── Gemfile              # Dependencies
├── Rakefile             # Build tasks
├── lib/                 # Source code
│   ├── my_mcp_server.rb # Main entry point
│   └── my_mcp_server/   # Module namespace
│       ├── server.rb    # Server setup
│       ├── tools/       # Tool implementations
│       ├── prompts/     # Prompt templates
│       └── resources/   # Resource handlers
├── bin/                 # Executables
│   └── mcp-server       # Stdio server
├── test/                # Test suite
│   ├── test_helper.rb   # Test configuration
│   └── tools/           # Tool tests
└── README.md            # This file

- Missing inline ref:

## License

MIT

- Missing inline ref:

## Generation Instructions

1. **Ask for project name and description**
2. **Generate all files** with proper naming and module structure
3. **Use classes for tools and prompts** for better organization
4. **Include input/output schemas** for type safety
5. **Add tool annotations** for behavior hints
6. **Include structured content** in responses
7. **Implement comprehensive tests** for all tools
8. **Follow Ruby conventions** (snake_case, modules, frozen_string_literal)
9. **Add proper error handling** with is_error flag
10. **Provide both stdio and HTTP** usage examples

- Missing inline ref:

## Template References

Detailed templates in

- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\run-session-agentsmd-workflow.prompt.md`
  - Missing inline ref: templates/run-session-agentsmd-workflow/phases.md
  - Missing inline ref: templates/run-session-agentsmd-workflow/
  - Missing inline ref: phases.md
- `prompts\rust-mcp-server-generator.prompt.md`
  - Missing inline ref: rmcp
  - Missing inline ref:
{project-name}/
├── Cargo.toml
├── .gitignore
├── README.md
├── src/
│   ├── main.rs
│   ├── handler.rs
│   ├── tools/
│   │   ├── mod.rs
│   │   └── {tool_name}.rs
│   ├── prompts/
│   │   ├── mod.rs
│   │   └── {prompt_name}.rs
│   ├── resources/
│   │   ├── mod.rs
│   │   └── {resource_name}.rs
│   └── state.rs
└── tests/
    └── integration_test.rs

  - Missing inline ref:

## Installation

- Missing inline ref: bash
cargo build --release

- Missing inline ref:

- Missing inline ref:

## Usage

### Stdio Transport

- Missing inline ref: bash
cargo run

- Missing inline ref:

### SSE Transport

- Missing inline ref: bash
cargo run --features http -- --transport sse

- Missing inline ref:

### HTTP Transport

- Missing inline ref: bash
cargo run --features http -- --transport http

- Missing inline ref: ,
- Missing inline ref: , and
- Missing inline ref:  macros (
- Missing inline ref: ,
- Missing inline ref: ,
- Missing inline ref: ,
- Missing inline ref: bash
cd {project-name}
cargo build
cargo test
cargo run

- Missing inline ref:

Now generate the complete project based on the user's requirements!

## Template References

Detailed templates in

- Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\security.prompt.md`
  - Missing inline ref: templates/security/phases.md
  - Missing inline ref: templates/security/
  - Missing inline ref: phases.md
- `prompts\seed-review-and-create.prompt.md`
  - Missing inline ref: src/scripts/seed/**/*.ts
  - Missing inline ref: src/database/schema.ts
  - Missing inline ref: src/scripts/seed/types.ts
  - Missing inline ref: SeedConfig
  - Missing inline ref: SeedOptions
  - Missing inline ref: LookupCache
  - Missing inline ref: EntityResult
  - Missing inline ref: SeedReport
  - Missing inline ref: src/scripts/seed/seeders/base-seed.ts
  - Missing inline ref: BaseSeeder<T>
  - Missing inline ref: src/scripts/seed/seed-orchestrator.ts
  - Missing inline ref: src/scripts/seed/index.ts
  - Missing inline ref: src/schemas/seed/
  - Missing inline ref:
BaseSeeder<T>.seed() → loadData() → validateData() → processBatches() → insertBatch()

  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref:  and
  - Missing inline ref:

## Template References

Templates in

- `prompts\session-agentsmd-full-workflow.prompt.md`
  - Missing inline ref: templates/session-agentsmd-full-workflow/phases.md
  - Missing inline ref: templates/session-agentsmd-full-workflow/
  - Missing inline ref: phases.md
- `prompts\setup-component.prompt.md`
  - Missing inline ref: templates/setup-component/
  - Missing inline ref: phases.md
- `prompts\setup-enhanced.prompt.md`
  - Missing inline ref:

---

## 2. ✅ Quality Gate (Before Every PR)

- Missing inline ref:

## 8. 🧭 How to Use This Guide

### For New Features

1. Identify which **Phase** (Section 6) your feature belongs to
2. Follow the **Implementation Workflow** (Section 5) step by step
3. Apply **DRY Practices** (Section 4) throughout
4. Run the **Quality Gate** (Section 2) before submitting

### For Bug Fixes

1. Check the **Reference Resolution Hierarchy** (Section 3) to find relevant code
2. Apply the correct pattern from the appropriate reference file
3. Run

- Missing inline ref:  to validate

### For Questions

1. Check the **Reference Resolution Hierarchy** (Section 3) for the right source file
2. Consult

- Missing inline ref:  for expanded technical details

1. Look at existing implementations in

- Missing inline ref:

## 12. 📖 Full Reference Files

| File | Purpose |
| --- | --- |
|

- Missing inline ref:  | Complete developer reference (25 sections) — patterns, code examples, architecture |
|
- Missing inline ref:  | Entity relationship details, constraints, cascade behavior |
|
- Missing inline ref:  | Quick-reference coding rules and conventions |
|
- Missing inline ref:  | File-pattern coding standards (TypeScript, Next.js, security, testing, performance) |
|
- Missing inline ref:  | All 30+ Drizzle tables, enums, relations |
|
- Missing inline ref:  | Abstract
- Missing inline ref:  base class |
|
- Missing inline ref:  |
- Missing inline ref:  type definition |
|
- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\setup-nextjs-frontend-stack.prompt.md`
  - Missing inline ref: src/app
  - Missing inline ref: Comic
  - Missing inline ref: User
  - Missing inline ref: comics
  - Missing inline ref: users
  - Missing inline ref: ${workspaceFolder}
  - Missing inline ref: src/
  - Missing inline ref: ${selection}
  - Missing inline ref: z.infer<typeof schema>
  - Missing inline ref: src/actions
  - Missing inline ref: "use client"
  - Missing inline ref: fields
  - Missing inline ref: src/schemas/<entity>.schema.ts
  - Missing inline ref: EntityCreateDTO
  - Missing inline ref: EntityUpdateDTO
  - Missing inline ref: src/dtos/<entity>.ts
  - Missing inline ref: src/dal/<entity>.ts
  - Missing inline ref: getAll
  - Missing inline ref: getById
  - Missing inline ref: create
  - Missing inline ref: update
  - Missing inline ref: delete
  - Missing inline ref: new Error('Not implemented')
  - Missing inline ref: db
  - Missing inline ref: src/actions/<entity>.ts
  - Missing inline ref: src/app/<plural>/page.tsx
  - Missing inline ref: Create<Entity>Form
  - Missing inline ref: src/components/<entity>/
  - Missing inline ref: tests/<entity>.spec.ts
  - Missing inline ref: page.tsx
  - Missing inline ref: edit
  - Missing inline ref: src/
  - Missing inline ref: fields
  - Missing inline ref: z.infer
  - Missing inline ref: page.tsx
  - Missing inline ref: fields
  - Missing inline ref: ${selection}
  - Missing inline ref: .new.ts
  - Missing inline ref: {entity}.schema.ts
  - Missing inline ref: pnpm lint
  - Missing inline ref: PascalCase.tsx
  - Missing inline ref: kebab-case.ts
  - Missing inline ref: {entity}.schema.ts
  - Missing inline ref: {entity}.ts
  - Missing inline ref: src/types/
  - Missing inline ref: src/components/ui/
  - Missing inline ref: src/utils/
  - Missing inline ref: src/schemas/
  - Missing inline ref: src/schemas/
  - Missing inline ref: src/database/queries/
  - Missing inline ref: src/database/mutations/
  - Missing inline ref: src/actions/
  - Missing inline ref: "use server"
  - Missing inline ref: userDAL.getById()
  - Missing inline ref: ActionResult
  - Missing inline ref: src/types/common.ts
  - Missing inline ref: docs/architecture.md
  - Missing inline ref: buildCommentTree
  - Missing inline ref: deletedAt
  - Missing inline ref: [deleted]
  - Missing inline ref: user
  - Missing inline ref: moderator
  - Missing inline ref: admin
  - Missing inline ref: docs/rbac.md
  - Missing inline ref: verifyAdmin()
  - Missing inline ref: ,
  - Missing inline ref:  or
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref:  (see
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref:  (see
  - Missing inline ref:  for admin-only actions. Return
  - Missing inline ref:  for comments with children, show
  - Missing inline ref:  or
  - Missing inline ref:  and
  - Missing inline ref: )
  1. Use Drizzle ORM in
  - Missing inline ref:  or
  - Missing inline ref:
  1. Be exposed only via server actions in
  - Missing inline ref:  (with
  - Missing inline ref: )
- All API responses must match
  - Missing inline ref: .
- All new files must follow naming conventions and directory structure above.
- All new features must include unit and E2E tests.
- All sensitive actions must be logged to audit table.
- All environment variables must be validated in
  - Missing inline ref: .

---

If anything is ambiguous (naming, folder preference, or the desired implementation style for DAL), ask a focused question before scaffolding files.

## Template References

Detailed templates in

- `prompts\setup.prompt.md`
  - Missing inline ref: templates/setup/1_project_architecture.md
  - Missing inline ref: templates/setup/2_essential_commands.md
  - Missing inline ref: .env.local
  - Missing inline ref: .env.local.example
  - Missing inline ref: templates/setup/3_environment_variables.md
  - Missing inline ref: src/database/schema.ts
  - Missing inline ref: templates/setup/4_database_schema__critical_fa.md
  - Missing inline ref: templates/setup/5_authentication_system.md
  - Missing inline ref: src/dal/base-dal.ts
  - Missing inline ref: templates/setup/6_data_access_layer_dal.md
  - Missing inline ref: src/actions/types.ts
  - Missing inline ref: templates/setup/7_server_actions__primary_muta.md
  - Missing inline ref: BaseSeed<T>
  - Missing inline ref: BaseSeed<T>
  - Missing inline ref: templates/setup/8_seeding_system_cli__rest_api.md
  - Missing inline ref: next.config.ts
  - Missing inline ref:

---

## 10. Provider Stack & Root Layout

### Root Layout (

- Missing inline ref: )

- 7 custom fonts loaded via
  - Missing inline ref:  →
  - Missing inline ref:

### Provider Order (

- Missing inline ref: )

- Missing inline ref:
SessionProvider → QueryClientProvider → ThemeProvider → TooltipProvider → children + lazy Toaster

- Missing inline ref:

-
  - Missing inline ref:  rendered only in development
-
  - Missing inline ref:  lazy-loaded
-
  - Missing inline ref:  receives theme config props

---

## 11. React Query Keys (

- Missing inline ref:

## 12. Middleware (

- Missing inline ref: )

- Missing inline ref:  is actually protected. Despite
- Missing inline ref:  being in the matcher, the function has no
- Missing inline ref:  check — it falls through to
- Missing inline ref: . Additionally, it checks for a cookie named
- Missing inline ref: , not a NextAuth session — this may not integrate with the actual auth system. See §21 (Technical Debt).

---

## 13. TypeScript & Tooling Conventions

### tsconfig.json

-
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref:  →
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref: , etc.
- Next.js plugin enabled, incremental builds

### ESLint (Flat Config —

- Missing inline ref: )

- Extends
  - Missing inline ref:  +
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref:  (ignore
  - Missing inline ref:  prefix),
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref:  are registered but have **no custom rules enabled**. Their built-in recommended configs may still apply through the plugin registration.

### Vitest (

- Missing inline ref: ,
- Missing inline ref: ,
- Missing inline ref:

---

## 14. Unique Project Conventions

> ### React Compiler is ON
>
> **Do NOT** manually add

- Missing inline ref: ,
- Missing inline ref: , or
- Missing inline ref:

## 15. VSCode Configuration

> ### Settings (

- Missing inline ref:

## 18. Key Files Quick Reference

| File | Purpose |
| --- | --- |
|

- Missing inline ref:  | 27 tables, 4 enums, no
- Missing inline ref:  (604 lines) |
|
- Missing inline ref:  | Abstract
- Missing inline ref:  + error normalization |
|
- Missing inline ref:  | Reference DAL with eager loading via
- Missing inline ref:  |
|
- Missing inline ref:  | Reference Server Action with auth + Zod + DAL |
|
- Missing inline ref:  |
- Missing inline ref:  discriminated union |
|
- Missing inline ref:  |
- Missing inline ref: ,
- Missing inline ref:  (bcryptjs) |
|
- Missing inline ref:  | NextAuth init —
- Missing inline ref:  |
|
- Missing inline ref:  | Session strategy, all callbacks (known bugs noted) |
|
- Missing inline ref:  | GitHub + Credentials + Keycloak providers |
|
- Missing inline ref:  | DrizzleAdapter wiring |
|
- Missing inline ref:  | Zod-validated env vars —
- Missing inline ref:  not
- Missing inline ref:  (6 active fields) |
|
- Missing inline ref:  | React Query key factory + singleton |
|
- Missing inline ref:  | SSR-safe Date hook |
|
- Missing inline ref:  | Provider stack order |
|
- Missing inline ref:  | Middleware — protects
- Missing inline ref:  only (⚠
- Missing inline ref:  unguarded) |
|
- Missing inline ref:  | React Compiler, Turbopack, images, security headers |
|
- Missing inline ref:  | Structured config — mostly stubs (see §21) |
|
- Missing inline ref:  | Template method for all seeders |
|
- Missing inline ref:  | Seed dependency resolution + orchestration |
|
- Missing inline ref:  | Seed REST API (5 HTTP methods) |
|
- Missing inline ref:  | Drizzle Kit config (schema path, dialect, pool) |

---

## 19. External Dependencies Map

| Category | Package | Version | Purpose |
| --- | --- | --- | --- |
| **Framework** |

- Missing inline ref:  | 16.1.6 | App Router, Server Components, Turbopack |
| **React** |
- Missing inline ref:  /
- Missing inline ref:  | 19.2.4 | UI rendering, Server Components |
| **ORM** |
- Missing inline ref:  /
- Missing inline ref:  | 0.45.1 | Type-safe SQL, migrations |
| **DB Driver** |
- Missing inline ref:  | — | PostgreSQL client |
| **Auth** |
- Missing inline ref:  | 5.0.0-beta.30 | Authentication, database sessions |
| **Auth Adapter** |
- Missing inline ref:  | — | NextAuth ↔ Drizzle bridge |
| **Validation** |
- Missing inline ref:  | 4.3.6 | Runtime schema validation (⚠ v4 — different API from v3) |
| **State** |
- Missing inline ref:  | 5.0.11 | Client state management |
| **Data Fetching** |
- Missing inline ref:  | 5.x | Client-side caching |
| **UI** |
- Missing inline ref:  | — | Accessible primitives (via shadcn) |
| **Styling** |
- Missing inline ref:  | 4.x | Utility-first CSS |
| **Icons** |
- Missing inline ref:  | — | Icon library |
| **Password** |
- Missing inline ref:  | — | Password hashing |
| **CLI** |
- Missing inline ref:  | 14.0.3 | Seed CLI (devDependency, not runtime) |
| **Monitoring** |
- Missing inline ref:  | — | Error tracking |
| **Testing** |
- Missing inline ref:  | 4.0.18 | Unit tests (jsdom) |
| **E2E Testing** |
- Missing inline ref:  | — | Browser E2E tests |
| **TypeScript** |
- Missing inline ref:  types** — ESLint enforces
- Missing inline ref:
>
> - **No manual memoization** — React Compiler is ON (
>
- Missing inline ref: ,
- Missing inline ref: ,
- Missing inline ref: templates/setup/20_coding_standards_summary.md
- Missing inline ref: proxy.ts
- Missing inline ref: /dashboard
- Missing inline ref: /admin
- Missing inline ref: src/proxy.ts
- Missing inline ref: proxy.ts
- Missing inline ref: "auth-token"
- Missing inline ref: src/proxy.ts
- Missing inline ref: process.env
- Missing inline ref: auth-config.ts
- Missing inline ref: auth-providers.ts
- Missing inline ref: db.ts
- Missing inline ref: env.ts
- Missing inline ref: src/lib/env.ts
- Missing inline ref: relations()
- Missing inline ref: .with()
- Missing inline ref: comment.parentId
- Missing inline ref: src/database/schema.ts
- Missing inline ref: performance.instructions.md
- Missing inline ref: .github/instructions/performance.instructions.md
- Missing inline ref: comment-rating-dal.ts
- Missing inline ref: commentRating
- Missing inline ref: src/dal/comment-rating-dal.ts
- Missing inline ref: comic-schema.ts
- Missing inline ref: comic.schema.ts
- Missing inline ref: src/schemas/
- Missing inline ref: appConfig.ts
- Missing inline ref: database
- Missing inline ref: auth.secret
- Missing inline ref: app
- Missing inline ref: appConfig.ts
- Missing inline ref: src/database/schema.ts
- Missing inline ref: relations()
- Missing inline ref: src/dal/my-entity-dal.ts
- Missing inline ref: BaseDal<typeof myEntity.$inferSelect>
- Missing inline ref: src/schemas/my-entity-schema.ts
- Missing inline ref: createMyEntitySchema
- Missing inline ref: updateMyEntitySchema
- Missing inline ref: src/actions/my-entity.actions.ts
- Missing inline ref: "use server"
- Missing inline ref: auth()
- Missing inline ref: revalidatePath()
- Missing inline ref: ActionResult<T>
- Missing inline ref: src/app/(root)/my-feature/page.tsx
- Missing inline ref: loading.tsx
- Missing inline ref: error.tsx
- Missing inline ref: "use client"
- Missing inline ref: src/tests/
- Missing inline ref: .github/instructions/
- Missing inline ref: code-review.instructions.md
- Missing inline ref: **/*
- Missing inline ref: documentation.instructions.md
- Missing inline ref: **/*.md, **/*.ts,**/*.tsx
- Missing inline ref: nextjs.instructions.md
- Missing inline ref: **/app/**/*.tsx, **/app/**/*.ts
- Missing inline ref: performance.instructions.md
- Missing inline ref: **/*.ts, **/*.tsx,**/*.css
- Missing inline ref: security.instructions.md
- Missing inline ref: **/*.ts, **/*.tsx,**/*.js, **/*.jsx
- Missing inline ref: testing.instructions.md
- Missing inline ref: **/*.test.ts, **/*.test.tsx,**/*.spec.ts
- Missing inline ref: typescript.instructions.md
- Missing inline ref: **/*.ts, **/*.tsx
- Missing inline ref: templates/setup/24_quality_gate_debugger.md
- Missing inline ref: templates/setup/
- Missing inline ref: 1_project_architecture.md
- Missing inline ref: 11_react_query_keys_srclibquer.md
- Missing inline ref: 14_unique_project_conventions.md
- Missing inline ref: 15_vscode_configuration.md
- Missing inline ref: 16_common_tasks__step-by-step.md
- Missing inline ref: 17_testing.md
- Missing inline ref: 2_essential_commands.md
- Missing inline ref: 20_coding_standards_summary.md
- Missing inline ref: 24_quality_gate_debugger.md
- Missing inline ref: 3_environment_variables.md
- Missing inline ref: 4_database_schema__critical_fa.md
- Missing inline ref: 5_authentication_system.md
- Missing inline ref: 6_data_access_layer_dal.md
- Missing inline ref: 7_server_actions__primary_muta.md
- Missing inline ref: 8_seeding_system_cli__rest_api.md
- `prompts\shuffle-json-data.prompt.md`
  - Missing inline ref: Variables
  - Missing inline ref:

## Workflow

1. **Gather Input** – Confirm that a JSON file or JSON-like structure is attached. If not, pause and request the data file.
2. **Review Configuration** – Merge defaults with any supplied variables under the

- Missing inline ref:  header or prompt-level overrides.

1. **Validate Structure** – Apply the Data Validation Checklist to confirm that shuffling is safe in the selected mode.
2. **Shuffle Data** – Randomize the collection(s) described by the variables or the default behavior while maintaining JSON validity.
3. **Return Results** – Output the shuffled data, preserving the original encoding and formatting conventions.

## Requirements for Shuffling Data

- Each request must provide a JSON file or a compatible JSON structure.
- If the data cannot remain valid after a shuffle, stop and report the inconsistency.
- Observe the default state when no overrides are supplied.

## Examples

Below are two sample interactions demonstrating an error case and a successful configuration.

### Missing File

- Missing inline ref: text
[user]

> /shuffle-json-data
[agent]
> Please provide a JSON file to shuffle. Preferably as chat variable or attached context.

- Missing inline ref:

### Custom Configuration

- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\skills-debug-prompt.prompt.md`
  - Missing inline ref: $HOME/AppData/Local/hermes/skills/
  - Missing inline ref: docs/skills-audit-results.json
  - Missing inline ref: docs/plan/skills-debug-plan.md
  - Missing inline ref: docs/skills-debug-context.md
  - Missing inline ref: ## Goal
  - Missing inline ref: templates/skills-debug-prompt/execution_steps.md
  - Missing inline ref: read_file(path)
  - Missing inline ref: patch(path, old_string, new_string)
  - Missing inline ref: write_file(path, content)
  - Missing inline ref: execute_code(code)
  - Missing inline ref: templates/skills-debug-prompt/
  - Missing inline ref: execution_steps.md
- `prompts\skills-fix.prompt.md`
  - Missing prompt dependency: context-map
  - Missing prompt dependency: update-implementation-plan
  - Missing prompt dependency: skills-debug-prompt
  - Missing skill: using-superpowers
  - Missing skill: brainstorming
  - Missing skill: plans-and-specs
  - Missing skill: dispatching-parallel-agents
  - Missing skill: subagent-driven-development
  - Missing skill: systematic-debugging
  - Missing skill: simplify
  - Missing skill: skill-judge
  - Missing skill: skill-creator
  - Missing reference: introspection-only-general
  - Missing reference: no-git-delete
  - Missing reference: no-net-fetch
  - Missing reference: skills-tools-preflight-check
  - Missing inline ref: $HOME/AppData/Local/hermes/skills/
  - Missing inline ref: docs/skills-debug-context.md
  - Missing inline ref: docs/<category>/<skill>/skills-debug-context.md
  - Missing inline ref: docs/plan/skills-debug-plan.md
  - Missing inline ref: prompts/skills-debug-prompt.prompt.md
  - Missing inline ref: hermes skills list
  - Missing inline ref: docs/<category>/<skill>/skills-debug-context.md
  - Missing inline ref: docs/skills-debug-context.md
  - Missing inline ref: docs/plan/skills-debug-plan.md
  - Missing inline ref: prompts/skills-debug-prompt.prompt.md
  - Missing inline ref: docs/skills-debug-context.md
  - Missing inline ref: hermes skills list
  - Missing inline ref: hermes skills update
  - Missing inline ref: patch()
  - Missing inline ref: write_file()
  - Missing inline ref: hermes skills check <name>
  - Missing inline ref: docs/plan/skills-debug-plan.md
  - Missing inline ref: ---
  - Missing inline ref: name
  - Missing inline ref: description
  - Missing inline ref: ## Goal\nUse when Use when <desc>
  - Missing inline ref: ## Goal\nUse when "<desc>" to accomplish...
  - Missing inline ref:  count)                        | Append closing
  - Missing inline ref: ## When to Use
  - Missing inline ref: ## Workflow
  - Missing inline ref: pip install
  - Missing inline ref: npm install -g
  - Missing inline ref: agent-browser
  - Missing inline ref: autonomous-ai-agents/
  - Missing inline ref: algorithmic-art
  - Missing inline ref: creative/
  - Missing inline ref: asdf
  - Missing inline ref: devops/
  - Missing inline ref: banking
  - Missing inline ref: software-development/
  - Missing inline ref: brainstorming
  - Missing inline ref: planning/
  - Missing inline ref: development/brainstorming
  - Missing inline ref: brand-guidelines
  - Missing inline ref: creative/
  - Missing inline ref: canvas-design
  - Missing inline ref: creative/
  - Missing inline ref: validate-memories
  - Missing inline ref: devops/
  - Missing inline ref: watchers
  - Missing inline ref: devops/
  - Missing inline ref: development/brainstorming
  - Missing inline ref: planning/brainstorming
  - Missing inline ref: (root)/dogfood
  - Missing inline ref: qa/dogfood
  - Missing inline ref: (root)/yuanbao
  - Missing inline ref: productivity/yuanbao
  - Missing inline ref: skill_view()
  - Missing inline ref: hermes skills update
  - Missing inline ref: hermes skills list
  - Missing inline ref: find <skills_root> -name 'SKILL.md' | sort
  - Missing inline ref: execute_code
  - Missing inline ref: docs/plan/skills-debug-plan.md
  - Missing inline ref: prompts/skills-debug-prompt.prompt.md
  - Missing inline ref: \n")

  - Missing inline ref:

**C-grade next** — Fix major issues (boilerplate

- Missing inline ref: , missing
- Missing inline ref:

1.

- Missing inline ref:  to review scope

1.

- Missing inline ref:

## Steps

1. Load required skills (

- Missing inline ref: ,
- Missing inline ref: ,
- Missing inline ref: ,
- Missing inline ref: )

1. Run

- Missing inline ref:  — pull official updates

1. Run

- Missing inline ref:  +
- Missing inline ref:  — build live inventory

1. Reorganize misplaced root-level skills; remove duplicates
2. Run audit script in batches of 7 → write per-skill reports + master index
3. Write

- Missing inline ref:  from audit findings

1. Write

- Missing inline ref:  for latest official versions
- [ ] Run
  - Missing inline ref:  and
  - Missing inline ref:  for inventory
- [ ] Reorganize misplaced root-level skills to correct categories
- [ ] Remove confirmed duplicate skills
- [ ] Batch-audit all SKILL.md files in groups of 7
- [ ] Write per-skill reports to
  - Missing inline ref:
- [ ] Write master index to
  - Missing inline ref:
- [ ] Write remediation plan to
  - Missing inline ref:
- [ ] Write execution prompt to
  - Missing inline ref:
- [ ] Fix all F-grade skills (critical issues)
- [ ] Fix all C-grade skills (major issues)
- [ ] Fix B-grade skills in batches of 7
- [ ] Re-run audit and verify F=0, C=0
- [ ] Update plan checklist and commit

## Actions

-
  - Missing inline ref:  — Get live skill inventory
-
  - Missing inline ref:  — Pull latest official skill versions
-
  - Missing inline ref:  — Validate skill format after fix
-
  - Missing inline ref:  — Enumerate all skill files
-
  - Missing inline ref:  — Move misplaced skill to correct category
-
  - Missing inline ref:  — Remove duplicate after verifying canonical exists
-
  - Missing inline ref:  — Run batch audit across all skills
-
  - Missing inline ref:  — Read individual skill for manual review
-
  - Missing inline ref:  — Apply targeted skill fix
-
  - Missing inline ref:  — Write audit reports, plans, or full skill rewrites
-
  - Missing inline ref:  — Review scope before commit
-
- `prompts\sql-code-review.prompt.md`
  - Missing inline ref: templates/sql-code-review/security_analysis.md
  - Missing inline ref: templates/sql-code-review/performance_optimization.md
  - Missing inline ref: templates/sql-code-review/code_quality__maintainability.md
  - Missing inline ref: templates/sql-code-review/database-specific_best_practic.md
  - Missing inline ref: sql
-- Verify referential integrity
SELECT o.user_id
FROM orders o
LEFT JOIN users u ON o.user_id = u.id
WHERE u.id IS NULL;

-- Check for data consistency
SELECT COUNT(*) as inconsistent_records
FROM products
WHERE price < 0 OR stock_quantity < 0;

- Missing inline ref:

## 🎯 Review Output Format

### Issue Template

- Missing inline ref:

## Template References

Detailed templates in

- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\sql-optimization.prompt.md`
  - Missing inline ref: templates/sql-optimization/core_optimization_areas.md
  - Missing inline ref: templates/sql-optimization/performance_tuning_techniques.md
  - Missing inline ref: templates/sql-optimization/query_anti-patterns.md
  - Missing inline ref: templates/sql-optimization/database-agnostic_optimization.md
  - Missing inline ref:

### Partial Index Strategy

- Missing inline ref:

## 📊 Performance Monitoring Queries

### Query Performance Analysis

- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\structured-autonomy-generate.prompt.md`
  - Missing inline ref: plans/{feature-name}/
  - Missing inline ref: runSubagent
  - Missing inline ref: templates/structured-autonomy-generate/step_2_generate_implement.md
  - Missing inline ref: {feature-name}
  - Missing inline ref: templates/structured-autonomy-generate/prerequisites.md
  - Missing inline ref: templates/structured-autonomy-generate/
  - Missing inline ref: phases.md
  - Missing inline ref: prerequisites.md
  - Missing inline ref: step_2_generate_implement.md
- `prompts\structured-autonomy-implement.prompt.md`
  - Missing inline ref: templates/structured-autonomy-implement/
  - Missing inline ref: legacy_prompt_details.md
  - Missing inline ref: phases.md
- `prompts\structured-autonomy-plan.prompt.md`
  - Missing inline ref: [NEEDS CLARIFICATION]
  - Missing inline ref: [NEEDS CLARIFICATION]
  - Missing inline ref: plans/{feature-name}/plan.md
  - Missing inline ref:

## Template References

Templates in

- Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\suggest-awesome-github-copilot-agents.prompt.md`
  - Missing inline ref:  vs local
  - Missing inline ref:  - Update recommended |

## Local Agent Discovery Process

1. List all

- Missing inline ref:  files in
- Missing inline ref:  directory

1. For each discovered file, read front matter to extract

- Missing inline ref:

1. Fetch the remote version using the

- Missing inline ref:  tool to get content from awesome-copilot repository agents folder
- Scan local file system for existing agents in
  - Missing inline ref:  directory

## Template References

Detailed templates in

- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\suggest-awesome-github-copilot-instructions.prompt.md`
  - Missing inline ref:  vs local
  - Missing inline ref:  - Update recommended |

## Local Instructions Discovery Process

1. List all

- Missing inline ref:  files in the
- Missing inline ref:  directory

1. For each discovered file, read front matter to extract

- Missing inline ref:  and
- Missing inline ref:

1. Fetch the remote version using the

- Missing inline ref:  (applies to specific file patterns via
- Missing inline ref:

## Requirements

- Use
  - Missing inline ref:  tool to get content from awesome-copilot repository instructions folder
- Scan local file system for existing instructions in
  - Missing inline ref:  directory
- Read YAML front matter from local instruction files to extract descriptions and
  - Missing inline ref:  directory

## Template References

Detailed templates in

- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\suggest-awesome-github-copilot-prompts.prompt.md`
  - Missing inline ref: prompts/
  - Missing inline ref: templates/suggest-awesome-github-copilot-prompts/process.md
  - Missing inline ref: 'codebase'
  - Missing inline ref: *.prompt.md
  - Missing inline ref: prompts/
  - Missing inline ref: description
  - Missing inline ref: #fetch
  - Missing inline ref: githubRepo
  - Missing inline ref: prompts/
  - Missing inline ref: prompts/
  - Missing inline ref: templates/suggest-awesome-github-copilot-prompts/
  - Missing inline ref: templates/suggest-awesome-github-copilot-prompts/
  - Missing inline ref: context_analysis_criteria.md
  - Missing inline ref: icons_reference.md
  - Missing inline ref: inputs.md
  - Missing inline ref: local_prompts_discovery_p.md
  - Missing inline ref: output_format.md
  - Missing inline ref: phases.md
  - Missing inline ref: process.md
  - Missing inline ref: requirements.md
  - Missing inline ref: rules.md
  - Missing inline ref: update_handling.md
  - Missing inline ref: version_comparison_proces.md
- `prompts\suggest-awesome-github-copilot-skills.prompt.md`
  - Missing inline ref: .github/skills/
  - Missing inline ref: templates/suggest-awesome-github-copilot-skills/local_skills_discovery_pr.md
  - Missing inline ref: .github/skills/
  - Missing inline ref: SKILL.md
  - Missing inline ref: name
  - Missing inline ref: description
  - Missing inline ref: SKILL.md
  - Missing inline ref: #fetch
  - Missing inline ref: SKILL.md
  - Missing inline ref: name
  - Missing inline ref: description
  - Missing inline ref: SKILL.md
  - Missing inline ref: azure-deployment-preflight
  - Missing inline ref: name
  - Missing inline ref: SKILL.md
  - Missing inline ref: SKILL.md
  - Missing inline ref:

## Requirements

- Use
  - Missing inline ref:  tool to get content from awesome-copilot repository skills documentation
- Use
  - Missing inline ref:  tool to get individual skill content for download
- Scan local file system for existing skills in
  - Missing inline ref:  directory
- Read YAML front matter from local
  - Missing inline ref:  directory

1. Ensure all bundled assets are downloaded alongside the updated

- Missing inline ref:

## Template References

Detailed templates in

- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\swift-mcp-server-generator.prompt.md`
  - Missing inline ref:
my-mcp-server/
├── Package.swift
├── Sources/
│   └── MyMCPServer/
│       ├── main.swift
│       ├── Server.swift
│       ├── Tools/
│       │   ├── ToolDefinitions.swift
│       │   └── ToolHandlers.swift
│       ├── Resources/
│       │   ├── ResourceDefinitions.swift
│       │   └── ResourceHandlers.swift
│       └── Prompts/
│           ├── PromptDefinitions.swift
│           └── PromptHandlers.swift
├── Tests/
│   └── MyMCPServerTests/
│       └── ServerTests.swift
└── README.md

  - Missing inline ref:

## Server.swift Template

- Missing inline ref:

## ResourceDefinitions.swift Template

- Missing inline ref:

## PromptDefinitions.swift Template

- Missing inline ref:

## README.md Template

- Missing inline ref: bash
swift build -c release

- Missing inline ref:

- Missing inline ref: bash
swift run

- Missing inline ref: bash
LOG_LEVEL=debug swift run

- Missing inline ref:

## Testing

- Missing inline ref: bash
swift test

- Missing inline ref:  - Entry point with ServiceLifecycle
-
  - Missing inline ref:  - Server configuration
-
  - Missing inline ref:  - Tool definitions and handlers
-
  - Missing inline ref:  - Resource definitions and handlers
-
  - Missing inline ref:  - Prompt definitions and handlers
-
  - Missing inline ref:  - Unit tests

## License

MIT

- Missing inline ref:

## Generation Instructions

1. **Ask for project name and description**
2. **Generate all files** with proper naming
3. **Use actor-based state** for thread safety
4. **Include comprehensive logging** with swift-log
5. **Implement graceful shutdown** with ServiceLifecycle
6. **Add tests** for all handlers
7. **Use modern Swift concurrency** (async/await)
8. **Follow Swift naming conventions** (camelCase, PascalCase)
9. **Include error handling** with proper MCPError usage
10. **Document public APIs** with doc comments

## Build and Run

- Missing inline ref: bash

# Build

swift build

# Run

swift run

# Test

swift test

# Release build

swift build -c release

# Install

swift build -c release
cp .build/release/MyMCPServer /usr/local/bin/

- Missing inline ref:

## Integration with Claude Desktop

Add to

- Missing inline ref:

- Missing inline ref:

## Template References

Detailed templates in

- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\sync-hermes-copilot-codex.prompt.md`
  - Missing skill: using-superpowers
  - Missing skill: user-communication-preferences
  - Missing skill: plans-and-specs
  - Missing reference: using-superpowers
  - Missing reference: user-communication-preferences
  - Missing reference: plans-and-specs
  - Missing inline ref: .github/agents/
  - Missing inline ref: .github/instructions/
  - Missing inline ref: .txt
  - Missing inline ref: ~/AppData/Local/hermes/
  - Missing inline ref: ~/.copilot/
  - Missing inline ref: ~/.codex/
  - Missing inline ref: using-superpowers
  - Missing inline ref: user-communication-preferences
  - Missing inline ref: plans-and-specs
  - Missing inline ref: phases.md
- `prompts\task-implementation.prompt.md`
  - Missing inline ref: templates/task-implementation/phases.md
  - Missing inline ref: templates/task-implementation/
  - Missing inline ref: phases.md
- `prompts\tasksync.prompt.md`
  - Missing inline ref: templates/tasksync/phases.md
  - Missing inline ref: templates/tasksync/
  - Missing inline ref: phases.md
- `prompts\technology-stack-blueprint-generator.prompt.md`
  - Missing inline ref: templates/technology-stack-blueprint-generator/generated_prompt.md
  - Missing inline ref: templates/technology-stack-blueprint-generator/
  - Missing inline ref: generated_prompt.md
- `prompts\test-providers-models.prompt.md`
  - Missing skill: test-providers-models
  - Missing skill: using-superpowers
  - Missing skill: plans-and-specs
  - Missing skill: user-communication-preferences
  - Missing skill: verification-before-completion
  - Missing reference: test-providers-models
  - Missing reference: using-superpowers
  - Missing reference: plans-and-specs
  - Missing reference: user-communication-preferences
  - Missing reference: verification-before-completion
  - Missing inline ref: default
  - Missing inline ref: research-analyst
  - Missing inline ref: code-architect
  - Missing inline ref: code-architect
  - Missing inline ref: research-analyst
  - Missing inline ref: adminbot
  - Missing inline ref: hermes auth list
  - Missing inline ref: hermes auth list
  - Missing inline ref: hermes auth list
  - Missing inline ref: ~/AppData/Local/hermes/scripts/
  - Missing inline ref: docs/test-providers-models‑*
  - Missing inline ref: hermes auth list
  - Missing inline ref: hermes chat -q --provider openrouter
  - Missing inline ref: using-superpowers
  - Missing inline ref: plans-and-specs
  - Missing inline ref: user-communication-preferences
  - Missing inline ref: verification-before-completion
  - Missing inline ref: gh-cli
  - Missing inline ref: provider-reliability-diagnostics
  - Missing inline ref: hermes auth list
  - Missing inline ref: hermes config show
  - Missing inline ref: terminal
  - Missing inline ref: fetch
  - Missing inline ref: web_extract
  - Missing inline ref: execute_code
  - Missing inline ref: memory
  - Missing inline ref: skills
  - Missing inline ref: default
  - Missing inline ref: research-analyst
  - Missing inline ref: code-architect
  - Missing inline ref: code-architect
  - Missing inline ref: research-analyst
  - Missing inline ref: adminbot
  - Missing inline ref: code-architect
  - Missing inline ref: default
  - Missing inline ref: hermes auth list
  - Missing inline ref: research-analyst
  - Missing inline ref: code-architect
  - Missing inline ref: code-architect
  - Missing inline ref: research-analyst
  - Missing inline ref: adminbot
  - Missing inline ref: code-architect
  - Missing inline ref: test_models.py
  - Missing inline ref: hermes auth list
  - Missing inline ref: hermes auth list
  - Missing inline ref: phase_0_auth__provider_invento.md
  - Missing inline ref: phase_1_model_catalog_discover.md
  - Missing inline ref: phase_2_free_model_extraction_.md
  - Missing inline ref: phase_3_provider-by-provider_b.md
  - Missing inline ref: phase_4_cross-provider_compari.md
  - Missing inline ref: phase_5_rate_limit_fallback_c.md
  - Missing inline ref: phase_6_script_creation__autom.md
- `prompts\testing.prompt.md`
  - Missing inline ref: templates/testing/phases.md
  - Missing inline ref: templates/testing/
  - Missing inline ref: phases.md
- `prompts\tldr-prompt.prompt.md`
  - Missing inline ref: tldr
  - Missing inline ref: #file
  - Missing inline ref: tldr
  - Missing inline ref: #fetch
  - Missing inline ref: tldr
  - Missing inline ref: templates/tldr-prompt/url_resolver.md
  - Missing inline ref:  for prompts,
  - Missing inline ref:

  - Missing inline ref:  for .agent.md,
  - Missing inline ref: ,
  - Missing inline ref:  syntax for all user-provided values (e.g.,
  - Missing inline ref: ,
  - Missing inline ref: ,
  - Missing inline ref:  syntax consistently for user-provided values
- ✓ Output is rendered directly in chat, not as a file creation
- ✓ Content accurately reflects the source file's/documentation's purpose and usage
- ✓ Response verbosity is appropriate for chat context (inline chat vs chat view)
- ✓ MCP server content includes setup and tool usage examples when applicable

## Template References

Detailed templates in

- Missing inline ref:
-
- `prompts\typescript-mcp-server-generator.prompt.md`
  - Missing inline ref: npm init
  - Missing inline ref: @modelcontextprotocol/sdk
  - Missing inline ref: zod@3
  - Missing inline ref: templates/typescript-mcp-server-generator/implementation_details.md
  - Missing inline ref: npm start
  - Missing inline ref: bunx tsx server.ts
  - Missing inline ref: npx @modelcontextprotocol/inspector
  - Missing inline ref: templates/typescript-mcp-server-generator/
  - Missing inline ref: implementation_details.md
  - Missing inline ref: phases.md
- `prompts\typescript.prompt.md`
  - Missing inline ref: templates/typescript/phases.md
  - Missing inline ref: templates/typescript/
  - Missing inline ref: phases.md
- `prompts\typespec-api-operations.prompt.md`
  - Missing inline ref: templates/typespec-api-operations/adding_get_operations.md
  - Missing inline ref: templates/typespec-api-operations/adding_post_operations.md
  - Missing inline ref: templates/typespec-api-operations/adding_patch_operations.md
  - Missing inline ref: templates/typespec-api-operations/adding_delete_operations.md
  - Missing inline ref: templates/typespec-api-operations/complete_crud_example.md
  - Missing inline ref: templates/typespec-api-operations/advanced_features.md
  - Missing inline ref: userId
  - Missing inline ref: uid
  - Missing inline ref: templates/typespec-api-operations/best_practices.md
  - Missing inline ref: @query
  - Missing inline ref: @path
  - Missing inline ref: @body
  - Missing inline ref: @card
  - Missing inline ref: @capabilities
  - Missing inline ref: @visibility(Lifecycle.Read)
  - Missing inline ref: templates/typespec-api-operations/
  - Missing inline ref: adding_delete_operations.md
  - Missing inline ref: adding_get_operations.md
  - Missing inline ref: adding_patch_operations.md
  - Missing inline ref: adding_post_operations.md
  - Missing inline ref: advanced_features.md
  - Missing inline ref: best_practices.md
  - Missing inline ref: complete_crud_example.md
- `prompts\typespec-create-agent.prompt.md`
  - Missing inline ref: main.tsp
  - Missing inline ref: templates/typespec-create-agent/requirements.md
  - Missing inline ref: templates/typespec-create-agent/template_structure.md
  - Missing inline ref: templates/typespec-create-agent/
  - Missing inline ref: phases.md
  - Missing inline ref: requirements.md
  - Missing inline ref: template_structure.md
- `prompts\typespec-create-api-plugin.prompt.md`
  - Missing inline ref: templates/typespec-create-api-plugin/requirements.md
  - Missing inline ref: templates/typespec-create-api-plugin/authentication_options.md
  - Missing inline ref: templates/typespec-create-api-plugin/function_capabilities.md
  - Missing inline ref: main.tsp
  - Missing inline ref: actions.tsp
  - Missing inline ref: cards/card.json
  - Missing inline ref: templates/typespec-create-api-plugin/
  - Missing inline ref: authentication_options.md
  - Missing inline ref: function_capabilities.md
  - Missing inline ref: phases.md
  - Missing inline ref: requirements.md
  - Missing inline ref: workflow.md
- `prompts\update-avm-modules-in-bicep.prompt.md`
  - Missing inline ref: ${file}
  - Missing inline ref: avm/res/{service}/{resource}
  - Missing inline ref: #search
  - Missing inline ref: #fetch
  - Missing inline ref: #fetch
  - Missing inline ref: #editFiles
  - Missing inline ref: bicep lint
  - Missing inline ref: bicep build
  - Missing inline ref: #runCommands
  - Missing inline ref: #search
  - Missing inline ref: #searchResults
  - Missing inline ref: #fetch
  - Missing inline ref: #editFiles
  - Missing inline ref: #runCommands
  - Missing inline ref: #todos
  - Missing inline ref: markdown
| Module | Current | Latest | Status | Action | Docs |
| --- | --- | --- | --- | --- | --- |
| avm/res/compute/vm | 0.1.0 | 0.2.0 | 🔄 | Updated | [📖](link) |
| avm/res/storage/account | 0.3.0 | 0.3.0 | ✅ | Current | [📖](link) |

### Summary of Updates

Describe updates made, any manual reviews needed or issues encountered.

- Missing inline ref:

## Icons

- 🔄 Updated
- ✅ Current
- ⚠️ Manual review required
- ❌ Failed
- 📖 Documentation

## Requirements

- Use MCR tags API only for version discovery
- Parse JSON tags array and sort by semantic versioning
- Maintain Bicep file validity and linting compliance

## Template References

Templates in

- `prompts\update-docs-on-code-change.prompt.md`
  - Missing inline ref: templates/update-docs-on-code-change/phases.md
  - Missing inline ref: templates/update-docs-on-code-change/
  - Missing inline ref: phases.md
- `prompts\update-implementation-plan.prompt.md`
  - Missing skill: writing-plans
  - Missing skill: plans-and-specs
  - Missing skill: context-map
  - Missing reference: writing-plans
  - Missing reference: plans-and-specs
  - Missing inline ref: <workspace_root>
  - Missing inline ref: plan/
  - Missing inline ref: <purpose>
  - Missing inline ref: <component>
  - Missing inline ref: <version>
  - Missing inline ref: <workspace_root>/plan/<purpose>-<component>-<version>.md
  - Missing inline ref: <workspace_root>
  - Missing inline ref: $HOME/Desktop/SandBox
  - Missing inline ref: <purpose>
  - Missing inline ref: feature-auth-refactor
  - Missing inline ref: <component>
  - Missing inline ref: database
  - Missing inline ref: <version>
  - Missing inline ref: v1
  - Missing inline ref: v2
  - Missing inline ref: v1
  - Missing inline ref:
<workspace_root>/plan/<purpose>-<component>-<version>.md

  - Missing inline ref:

  - Missing inline ref:

## Outputs

- A complete implementation plan at
  - Missing inline ref: ](templates/_shared/skills-table-core.md#update-implementation-plan)

The skills listed below in the "Skills Required" section mirror the YAML front-matter

- Missing inline ref:  declaration and indicate which Hermes skills must be available for this prompt to execute successfully. The Hermes agent will verify skill availability before running this prompt.

| Skill | Purpose |
| --- | --- |
|

- Missing inline ref:  | Pre-change map of plan-related files and dependencies |
|
- Missing inline ref:  | Author structured implementation plans |
|
- Missing inline ref:

## Actions Summary

1. Read the request and workspace state
2. Determine create vs. update mode
3. Write or update the implementation plan with standard sections
4. Apply the correct status badge
5. Verify all sections are present and accurate

## Template References

Detailed templates in

- Missing inline ref:
-
- `prompts\update-llms.prompt.md`
  - Missing inline ref: llms.txt
  - Missing inline ref: llms.txt
  - Missing inline ref: templates/update-llms/analysis_and_planning_phase.md
  - Missing inline ref: llms.txt
  - Missing inline ref: templates/update-llms/implementation_requirements.md
  - Missing inline ref: llms.txt
  - Missing inline ref: templates/update-llms/execution_steps.md
  - Missing inline ref: /llms.txt
  - Missing inline ref: templates/update-llms/update_strategy.md
  - Missing inline ref:

## Success Criteria

The updated

- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\update-markdown-file-index.prompt.md`
  - Missing inline ref: ${file}
  - Missing inline ref: .md
  - Missing inline ref: .js
  - Missing inline ref: .py
  - Missing inline ref: markdown

## Files in ${folder}

- [filename.ext](path/to/filename.ext) - Description
- [filename2.ext](path/to/filename2.ext) - Description

  - Missing inline ref:
-
- `prompts\update-oo-component-documentation.prompt.md`
  - Missing inline ref: mermaid
[Update diagram to reflect current architecture]

  - Missing inline ref:

  - Missing inline ref: csharp
// Update basic usage example to current API

  - Missing inline ref:

### Advanced Usage

- Missing inline ref: csharp
// Update advanced configuration patterns to current implementation

- Missing inline ref:

- Missing inline ref:

## Template References

Detailed templates in

- `prompts\update-specification.prompt.md`
  - Missing inline ref: templates/update-specification/best_practices_for_ai-rea.md
  - Missing inline ref: templates/update-specification/8_dependencies__external_.md
  - Missing inline ref: code
// Code snippet or data example demonstrating the correct application of the guidelines, including edge cases

  - Missing inline ref:

  - Missing inline ref:

## 10. Validation Criteria

[List the criteria or tests that must be satisfied for compliance with this specification.]

## 11. Related Specifications / Further Reading

[Link to related spec 1] [Link to relevant external documentation]

- Missing inline ref:

- Missing inline ref:

## Template References

Detailed templates in

- Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\web-research-pipeline.prompt.md`
  - Missing skill: web-research-pipeline
  - Missing skill: mcp-fetch
  - Missing skill: firecrawl-scrape
  - Missing skill: domain-intel
  - Missing reference: web-research-pipeline
  - Missing reference: mcp-fetch
  - Missing reference: firecrawl-scrape
  - Missing reference: domain-intel
  - Missing inline ref: mcp_fetch_get_markdown
  - Missing inline ref: firecrawl_scrape
  - Missing inline ref: web_extract
  - Missing inline ref: web-research-pipeline
  - Missing inline ref: firecrawl_search
  - Missing inline ref: web_search
  - Missing inline ref: mcp_fetch_get_markdown
  - Missing inline ref: web_extract
- `prompts\what-context-needed.prompt.md`
  - Missing inline ref: markdown

## Files I Need

> ### Must See (required for accurate answer)
>
> -
>
- Missing inline ref:

## Template References

Templates in

- Missing inline ref:
-
- `prompts\workspace-consolidate.prompt.md`
  - Missing prompt dependency: context-map
  - Missing prompt dependency: update-implementation-plan
  - Missing skill: brainstorming
  - Missing skill: plans-and-specs
  - Missing skill: dispatching-parallel-agents
  - Missing skill: subagent-driven-development
  - Missing skill: systematic-debugging
  - Missing skill: simplify
  - Missing skill: acpx-executor
  - Missing skill: git-patch-management
  - Missing skill: project-consolidation
  - Missing reference: introspection-only-general
  - Missing reference: no-git-delete
  - Missing reference: no-net-fetch
  - Missing reference: skills-tools-preflight-check
  - Missing reference: context-map
  - Missing reference: brainstorming
  - Missing reference: plans-and-specs
  - Missing reference: dispatching-parallel-agents
  - Missing reference: subagent-driven-development
  - Missing reference: systematic-debugging
  - Missing reference: simplify
  - Missing reference: acpx-executor
  - Missing reference: git-patch-management
  - Missing reference: project-consolidation
  - Missing inline ref: projects/Bash/
  - Missing inline ref: projects/Bash/
  - Missing inline ref: tree
Bash/
├── Banking/                          # 34 scripts
│   ├── install.sh
│   ├── install-agents.sh
│   ├── install/lib/00-config.sh → 08-install.sh
│   └── scripts/                      # 23 files (.sh, .ps1, .bat)
├── rhixecompany-comics/               # 0 scripts (pending — new Django + Next.js project)
├── rhixe_scans/                      # 7 scripts
│   ├── docker-clean.sh, git-setup.sh
│   ├── install_chrome.sh, install_firefox.sh
│   ├── prod-dev.sh, prod.sh, setup.sh
├── ecom/                             # 1 script
│   └── install.sh
├── root/                             # 2 scripts
│   ├── analyze-scripts.sh
│   └── sandbox-runtime-commands.ps1
├── src/                              # TypeScript core migration targets
│   ├── cache-clean.ts
│   ├── clean-dep.ts
│   ├── upgrade.ts
│   ├── git-commit-batches.ts
│   ├── core/ (ast-transformer, behavior-test, dry-run, script-runner)
│   ├── lib/ (cli, colors, errors, logging)
│   └── migration/ (templates, ts-morph-helper)
├── docs/                             # Moved from Bash/ root below
│   ├── AGENTS.md
│   ├── ARCHITECTURE.md
│   ├── CODE_STYLE.md
│   ├── README.md
│   ├── bash-scripts-safety-audit.md
│   ├── FINAL-SUMMARY.md
│   ├── MIGRATION-GUIDE.md
│   └── phase5-verification-report.md
├── archive/skills-commit-batches/    # 52 archived batch files (keep as dead code reference)
├── lib/                              # log-rotate.sh, log-rotate.ps1
├── scripts/                          # Auditing/orchestration scripts
├── edits/run-audit.sh.patch          # Patch for run-audit.sh
├── tsconfig.json, package.json, bun.lock, bunfig.toml
├── README.md                         # STUB — links to docs/README.md

  - Missing inline ref:

### Steps

1. **Scan** for any remaining operational scripts outside

- Missing inline ref:  (exclude
   framework seeds,
- Missing inline ref: ,
- Missing inline ref: ,
- Missing inline ref: )

1. **Move** misplaced project docs into

- Missing inline ref:  →

- Missing inline ref:  (update internal references)
    -

- Missing inline ref:  →

- Missing inline ref
    -

- Missing inline ref:  →

- Missing inline ref
    -

- Missing inline ref:  →
- Missing inline ref:  (replace root README with stub)

1. **Create**

- Missing inline ref:  stub that links to
- Missing inline ref:

1. **Verify**

- Missing inline ref:  counts against actual file
   listing

1. **Save** verification report to

- Missing inline ref: , skip with note
  - If
- Missing inline ref:
   file

1. **Validate isolated patches** — verify each applies independently
2. **Dead patch auto-detection** — for each patch classified as

- Missing inline ref:  against EVERY project directory (not just
      prefix-matched)
  - If a supposedly-obsolete patch applies cleanly to a live project, **promote
      it** with corrected target
  - If truly dead (no project found, cookiecutter template, abandoned
      framework), leave in
- Missing inline ref:

1. **Save patch debug report** to

- Missing inline ref:
  - Reference to related docs in
- Missing inline ref:

1. **Ensure portability** — use relative paths, no absolute

- Missing inline ref:  for each applied
   patch

1. **Patch content integrity check** — verify structural integrity beyond

- Missing inline ref: ,
- Missing inline ref: ) — use
- Missing inline ref:  or relative paths
  - All author emails have valid format (
- Missing inline ref:  in
      target project to detect dependency
  - If B's commits contain A's HEAD as ancestor → A must apply first
  - Serialize patches into a DAG-based execution order
  - Save dependency graph to
- Missing inline ref:  as mermaid
      diagram

1. **Save enhanced patches** to

- Missing inline ref:

1. **Save enhancement log** to

- Missing inline ref: ,
- Missing inline ref: )

1. Does it have a known missing feature or bugfix that should be patched?
2. Is documentation out of date compared to the project's actual state?
3. Does

- Missing inline ref: ,
- Missing inline ref: ,
- Missing inline ref:
   where absent

1. **Missing config patches** — add

- Missing inline ref: ,
- Missing inline ref: ,

- Missing inline ref:  for consistency

1. **Consistency patches** — normalize existing files to match

- Missing inline ref:
   conventions

1. **Known bugfix patches** — fix bugs found during Phase 2's

- Missing inline ref:  diagnostics

### Patch Patch Generation

- Missing inline ref: plaintext
patches/
├── enhanced/                     # Enhanced versions of original patches
│   ├── xamehi.patch
│   ├── rhixe-company.patch
│   ├── python-projects.patch
│   └── youtube-downloader.patch
├── new/                          # Newly created patches
│   ├── <project-name>-docs.patch
│   └── <project-name>-config.patch
└── obsolete/                     # Unchanged archive
    ├── django-scrapy-selenium.patch
    ├── xamehi-tv.patch
    └── cookiecutter-django-tailwind.patch

- Missing inline ref: . All project-level docs go under

- Missing inline ref: . All Bash-specific docs go under
- Missing inline ref:

#### Content Standards

| Requirement                           | Why                             | Check                                                  |
| ------------------------------------- | ------------------------------- | ------------------------------------------------------ |
| Clear H1 title                        | Navigation, AI retrieval        | Document starts with

- Missing inline ref:                          |
| 2-3 sentence summary after H1         | Quick human scan, AI snippet    | First paragraph is a summary                           |
| Section headings (H2/H3)              | Scannability, TOC generation    | No walls of text                                       |
| Code blocks with language tags        | Syntax highlighting, AI context | Every code block has
- Missing inline ref: lang
- Missing inline ref: <!-- TOC -->
- Missing inline ref: See [projects/Bash/docs/AGENTS.md](../../Bash/docs/AGENTS.md)
- Missing inline ref: sh,
- Missing inline ref: ts,
- Missing inline ref: $
- Missing inline ref: <!-- like this -->
- Missing inline ref: txt
docs/                                         # Workspace-level reports
├── bash-migration-final-report.md            → verify frontmatter, add tags
├── bash-scripts-audit-results.md             → verify frontmatter, add tags
├── bash-scripts-list-context.md              → verify frontmatter, add tags
├── bash-fix-implementation-plan.md           → verify frontmatter, add tags
├── project-docs/<project>/*.md              → verify each has frontmatter

projects/Bash/docs/                                    # Bash project-specific docs
├── AGENTS.md                                 → add frontmatter, optimize
├── ARCHITECTURE.md                           → add frontmatter, optimize
├── CODE_STYLE.md                             → add frontmatter, optimize
├── README.md                                 → add frontmatter, optimize
├── bash-scripts-safety-audit.md              → add frontmatter, optimize
├── FINAL-SUMMARY.md                          → add frontmatter, optimize
├── MIGRATION-GUIDE.md                        → add frontmatter, optimize
└── phase5-verification-report.md             → add frontmatter, optimize

- Missing inline ref:

### AI-Readiness Scoring Script

Create

- Missing inline ref:  that scores every
- Missing inline ref:  between first 5 lines            |
| Summary paragraph in first 3 lines    | +15                | non-empty paragraph within first 3 lines after H1 |
| Language-tagged code blocks           | +10 each (max +30) | count
- Missing inline ref: lang
- Missing inline ref: test -f
- Missing inline ref: docs/ai-readiness-report.md
- Missing inline ref: repo.prompts.md
- Missing inline ref:

For each project under

- Missing inline ref:
- Flag extra files as
  - Missing inline ref:
- Generate
  - Missing inline ref:
- [ ] Patch dependency graph saved to
  - Missing inline ref:
- [ ] AI-readiness report saved to
  - Missing inline ref:
- [ ] Doc symmetry report saved to
  - Missing inline ref:
- [ ] All active patches pass
  - Missing inline ref:
- [ ] All active patches have enhanced versions in
  - Missing inline ref:
- [ ] All missing patches created in
  - Missing inline ref: , project docs in

  - Missing inline ref: , Bash docs in
  - Missing inline ref:
- [ ] Every
  - Missing inline ref:  file has YAML frontmatter and summary paragraph
- [ ] No dead or misplaced documentation files
- [ ]
  - Missing inline ref:  clean

Generate

- Missing inline ref:  — Find all bash scripts
-
  - Missing inline ref:  — Test patch applicability
-
  - Missing inline ref:  — Detect patch dependencies
-
  - Missing inline ref:  — Write enhanced patches and reports
-
  - Missing inline ref:  — Apply targeted doc fixes
-
  - Missing inline ref:  — Check frontmatter presence
-
  - Missing inline ref:  — Load patch management skill
-
- `prompts\write-coding-standards-from-file.prompt.md`
  - Missing inline ref: boolean
  - Missing inline ref: string[]
  - Missing inline ref: templates/write-coding-standards-from-file/rules_and_configuration.md
  - Missing inline ref: ${fileName}.length > 1 || ${folderName} != undefined
  - Missing inline ref: ${fixInconsistencies}
  - Missing inline ref: templates/write-coding-standards-from-file/variable_and_parameter_configu.md
  - Missing inline ref: ${fetchStyleURL} == true
  - Missing inline ref:

## Coding Standards Templates

###

- Missing inline ref:

- Missing inline ref: text

- Missing inline ref:  or
- Missing inline ref:

- Missing inline ref:

###

- Missing inline ref:

- Missing inline ref: text

- Missing inline ref: markdown

  # Style Guide

    This document defines the style and conventions used in this project.
    All contributions should follow these rules unless otherwise noted.

  ## 1. General Code Style

  - Favor clarity over brevity.
  - Keep functions and methods small and focused.
  - Avoid repeating logic; prefer shared helpers/utilities.
  - Remove unused variables, imports, code paths, and files.

    ## 2. Naming Conventions

    Use descriptive names. Avoid abbreviations unless well-known.

    | Item            | Convention           | Example            |
    |-----------------|----------------------|--------------------|
    | Variables       |
- Missing inline ref:    |
- Missing inline ref:       |
    | Functions       |
- Missing inline ref:  |
- Missing inline ref:       |
    | Constants       |
- Missing inline ref:    |
- Missing inline ref:       |
    | Types/Structs   |
- Missing inline ref:          |
- Missing inline ref:        |
    | File Names      |
- Missing inline ref:    |
- Missing inline ref: c
        if (condition) {
            do_something();
        } else {
            do_something_else();
        }

- Missing inline ref: , not
- Missing inline ref: text
        Short summary (max ~50 chars)
        Optional longer explanation of context and rationale.

- Missing inline ref:

  ### Reviews

  - Keep pull requests reasonably small.
  - Be respectful and constructive in review discussions.
  - Address requested changes or explain if you disagree.

    ## 7. Tests

  - Write tests for new functionality.
  - Tests should be deterministic (no randomness without seeding).
  - Prefer readable test cases over complex test abstraction.

    ## 8. Changes to This Guide

    Style evolves.
    Propose improvements by opening an issue or sending a patch updating this document.

- Missing inline ref:

- Missing inline ref:

## Template References

Detailed templates in

- Missing inline ref:
-
  - Missing inline ref:
-
- `prompts\write-tests.prompt.md`
  - Missing inline ref: templates/write-tests/
  - Missing inline ref: phases.md
- `prompts\zod-schema-generation.prompt.md`
  - Missing skill: prompt-engineering
  - Missing reference: prompt-engineering

### references

- None

---
