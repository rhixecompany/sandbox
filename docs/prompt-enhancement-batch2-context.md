# Prompt Enhancement Batch 2 - Context & Dependency Catalog

## Batch 2: Next 5 Most Recently Updated Prompts

| #   | Path                                            | Name                  | Title                                                      | Timestamp  |
| --- | ----------------------------------------------- | --------------------- | ---------------------------------------------------------- | ---------- |
| 1   | .github/prompts/cosmosdb-datamodeling.prompt.md | cosmosdb-datamodeling | Azure Cosmos DB NoSQL Data Modeling Expert System Prompt   | 1785892726 |
| 2   | .github/prompts/oh-my-openagent-setup.prompt.md | oh-my-openagent-setup | Oh My OpenAgent Setup                                      | 1785892349 |
| 3   | .github/prompts/disk-space-cleanup.prompt.md    | disk-space-cleanup    | Disk Space Cleanup                                         | 1785892349 |
| 4   | .github/prompts/pl.prompt.md                    | pl                    | Pl (Batch Fix Errors/Warnings/Deprecations)                | 1785563322 |
| 5   | .github/prompts/model-recommendation.prompt.md  | model-recommendation  | AI Model Recommendation for Copilot Chat Modes and Prompts | 1785561707 |

## Prompt 1: cosmosdb-datamodeling.prompt.md

- **Tags**: architecture, azure, data, database, frontend, ml, prompts, sql, typescript
- **Skills**: [] (empty - but references using-superpowers, systematic-debugging, git-patch-management, executing-plans, verification-before-completion in body)
- **Toolsets**: file, terminal
- **Dependencies**: [] (empty)
- **Trigger**: /cosmosdb-datamodeling
- **Plan**: None (references templates/cosmosdb-datamodeling/ directory)
- **Lines**: 304, Size: 14420 bytes
- **Issues**: Frontmatter contains empty lines with blank values (lines 2, 4, 6, 9, 12, 15, 21, 23, 25, 27, 29, 32, 35, 38, 41, 44, 47, 50, 53, 55)

## Prompt 2: oh-my-openagent-setup.prompt.md

- **Tags**: hermes, opencode, setup, ops, workflow
- **Skills**: using-superpowers, user-communication-preferences, verification-before-completion, oh-my-openagent-setup
- **Toolsets**: file, terminal
- **Scripts**: ~/Desktop/SandBox/scripts/omo_doctor.py
- **Dependencies**: skill:using-superpowers, skill:user-communication-preferences, skill:verification-before-completion, skill:oh-my-openagent-setup
- **Trigger**: /oh-my-openagent-setup
- **Plan**: None
- **Lines**: 80, Size: 2772 bytes
- **Status**: ✅ Clean - no issues found

## Prompt 3: disk-space-cleanup.prompt.md

- **Tags**: cleanup, disk, hermes, ops, workflow
- **Skills**: using-superpowers, user-communication-preferences, verification-before-completion, disk-space-cleanup
- **Toolsets**: clarify, file, terminal
- **Scripts**: ~/Desktop/SandBox/scripts/cleanup_disk.py
- **Dependencies**: skill:using-superpowers, skill:user-communication-preferences, skill:verification-before-completion, skill:disk-space-cleanup
- **Trigger**: /disk-space-cleanup
- **Plan**: None
- **Lines**: 79, Size: 2906 bytes
- **Status**: ✅ Clean - no issues found

## Prompt 4: pl.prompt.md

- **Tags**: documentation, fix, frontend, linting, markdown, ml, prompts, specification, testing, typescript, errors, warnings, deprecations, batch-fix, build
- **Skills**: [] (empty - but references using-superpowers, systematic-debugging, git-patch-management, executing-plans, verification-before-completion in body)
- **Toolsets**: web, terminal, file, code_execution, session_search
- **Dependencies**: [] (empty)
- **Trigger**: /pl
- **Plan**: plans/2026-06-29_144500-awesome-hermes-agent-implementation.md
- **Lines**: 244, Size: 9001 bytes
- **Issues**: Frontmatter contains empty lines with blank values (lines 2, 4, 7, 9, 11, 14, 16, 19, 22, 25, 28, 31, 34, 37)

## Prompt 5: model-recommendation.prompt.md

- **Tags**: ai-assistant, frontend, ml, prompts, specification, typescript
- **Skills**: [] (empty - but references using-superpowers, systematic-debugging, git-patch-management, executing-plans, verification-before-completion in body)
- **Toolsets**: file, terminal
- **Dependencies**: [] (empty)
- **Trigger**: /model-recommendation
- **Plan**: None (references templates/model-recommendation/ directory)
- **Lines**: 343, Size: 14040 bytes
- **Issues**: Frontmatter contains empty lines with blank values (lines 2, 4, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48)

## Cross-Prompt Dependencies

- **cosmosdb-datamodeling** → references templates/cosmosdb-datamodeling/ directory
- **oh-my-openagent-setup** → uses oh-my-openagent-setup skill
- **disk-space-cleanup** → uses disk-space-cleanup skill
- **pl** → references plans/2026-06-29_144500-awesome-hermes-agent-implementation.md
- **model-recommendation** → references templates/model-recommendation/ directory

## Common Template References

All prompts reference shared templates in `templates/_shared/`:

- rules-core.md
- personas.md
- personality.md
- best-practices.md
- deps-core.md
- skills-table-core.md
