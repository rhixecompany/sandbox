# Phases

> Extracted from `run-session-agentsmd-workflow.prompt.md`.

## Phases

### Phase 1: Resolve Scope
| Field | Details |
| --- | --- |
| Goal | Resolve argument into concrete target directories. |
| Inputs | User argument, workspace directories. |
| Outputs | Final target list for processing. |
| Validation | Every target exists and is uniquely resolved. |

### Phase 2: Generate AGENTS
| Field | Details |
| --- | --- |
| Goal | Create or update AGENTS.md in each target directory. |
| Inputs | Target files such as README.md, package.json, requirements.txt, pyproject.toml. |
| Outputs | Updated AGENTS.md files with project-specific guidance. |
| Validation | AGENTS.md exists and is lint-valid markdown where diagnostics are available. |

### Phase 3: Commit and Publish
| Field | Details |
| --- | --- |
| Goal | Commit AGENTS.md changes in each repo and publish PR-ready branches. |
| Inputs | Target repos, AGENTS.md diff, branch naming convention. |
| Outputs | Remote branches containing AGENTS commit for each repo. |
| Validation | Remote branch exists and points to expected commit SHA. |

### Phase 4: Reconcile and Report
| Field | Details |
| --- | --- |
| Goal | Normalize branch naming and provide final auditable output. |
| Inputs | Remote refs and per-repo commit SHAs. |
| Outputs | Compact repo-branch-SHA-status table and exception list. |
| Validation | Table includes all targets and accurate statuses. |
