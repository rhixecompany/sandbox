# Phases

> Extracted from `session-agentsmd-full-workflow.prompt.md`.

## Phases

### Phase 1: Intake
| Field | Details |
| --- | --- |
| Goal | Determine scope, targets, and repository boundaries before edits. |
| Inputs | User request, workspace folders, existing AGENTS.md files, project manifests, README files. |
| Outputs | Definitive target list and per-target processing plan. |
| Validation | All requested targets are discovered and mapped to actual directories. |

### Phase 2: Generate AGENTS
| Field | Details |
| --- | --- |
| Goal | Create or update AGENTS.md content per target project with accurate project-specific commands and guidance. |
| Inputs | Target folder, package.json, pyproject.toml, requirements.txt, README.md, workflow files where relevant. |
| Outputs | Updated or created AGENTS.md in each target directory. |
| Validation | File exists, is readable markdown, and reflects actual local command/tooling context. |

### Phase 3: Git Commit and Push
| Field | Details |
| --- | --- |
| Goal | Commit AGENTS.md changes per project repo and push to remote branches safely. |
| Inputs | Project repos under scope, staged AGENTS.md files, branch topology, remote state. |
| Outputs | Pushed commits per repo with trackable branch names. |
| Validation | Commit exists and remote branch contains expected commit SHA. |

### Phase 4: Reconcile and Report
| Field | Details |
| --- | --- |
| Goal | Ensure branch naming consistency and produce final audit-ready table. |
| Inputs | Remote refs, per-repo commit SHAs, branch naming convention. |
| Outputs | Compact repo-branch-SHA table and any exception notes. |
| Validation | Every in-scope repo has a recorded status, branch, and SHA (or explicit blocker). |
