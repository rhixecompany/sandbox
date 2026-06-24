---
agent: "agent"
description: "Find GitHub Copilot skills that add coverage the repo lacks and flag local duplicates or outdated copies."
tools:
  [
    "edit",
    "search",
    "runCommands",
    "runTasks",
    "think",
    "changes",
    "testFailure",
    "openSimpleBrowser",
    "web/fetch",
    "githubRepo",
    "todos",
    "search"
  ]
---

## Goal

Suggest GitHub Copilot skills that add coverage the repo lacks, and flag local duplicates or outdated copies.

## Context

Use when you need to work on the current workspace or task.

## Inputs

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs

- A complete result that matches the prompt's purpose.
- A concise verification note when the task benefits from one.

## Rules

- Follow the prompt literally and prefer evidence from the current workspace.
- Keep the response structured, deterministic, and easy to act on.
- Avoid changing unrelated files or adding unnecessary scope.
- If something is unclear, state the assumption instead of guessing.

## Phases

### Phase 1: Intake
- Read the request and identify the exact scope.
- Locate the relevant files, diffs, or references.

### Phase 2: Execute
- Perform the requested work with the smallest safe change set.
- Keep the steps explicit and reproducible.

### Phase 3: Verify
- Check the result against the goal, rules, and inputs.
- Confirm the output is usable and complete.

### Phase 4: Hand off
- Return the final artifact or findings clearly.
- Stop once the requested result is delivered.

## Legacy Prompt Details
# Suggest Awesome GitHub Copilot Skills

Analyze current repository context and suggest relevant Agent Skills from the [GitHub awesome-copilot repository](https://github.com/github/awesome-copilot/blob/main/docs/README.skills.md) that are not already available in this repository. Agent Skills are self-contained folders located in the [skills](https://github.com/github/awesome-copilot/tree/main/skills) folder of the awesome-copilot repository, each containing a `SKILL.md` file with instructions and optional bundled assets.

## Process

> 1. **Fetch Available Skills**: Extract skills list and descriptions from [awesom
> 2. **Scan Local Skills**: Discover existing skill folders in `.github/skills/` f

> **Full content:** `templates/suggest-awesome-github-copilot-skills/local_skills_discovery_pr.md`

## Context Analysis Criteria

🔍 **Repository Patterns**:

- Programming languages used (.cs, .js, .py, .ts, etc.)
- Framework indicators (ASP.NET, React, Azure, Next.js, etc.)
- Project types (web apps, APIs, libraries, tools, infrastructure)
- Development workflow requirements (testing, CI/CD, deployment)
- Infrastructure and cloud providers (Azure, AWS, GCP)

🗨️ **Chat History Context**:

- Recent discussions and pain points
- Feature requests or implementation needs
- Code review patterns
- Development workflow requirements
- Specialized task needs (diagramming, evaluation, deployment)

## Output Format

Display analysis results in structured table comparing awesome-copilot skills with existing repository skills:

| Awesome-Copilot Skill | Description | Bundled Assets | Already Installed | Similar Local Skill | Suggestion Rationale |
| --- | --- | --- | --- | --- | --- |
| [gh-cli](https://github.com/github/awesome-copilot/tree/main/skills/gh-cli) | GitHub CLI skill for managing repositories and workflows | None | ❌ No | None | Would enhance GitHub workflow automation capabilities |
| [aspire](https://github.com/github/awesome-copilot/tree/main/skills/aspire) | Aspire skill for distributed application development | 9 reference files | ✅ Yes | aspire | Already covered by existing Aspire skill |
| [terraform-azurerm-set-diff-analyzer](https://github.com/github/awesome-copilot/tree/main/skills/terraform-azurerm-set-diff-analyzer) | Analyze Terraform AzureRM provider changes | Reference files | ⚠️ Outdated | terraform-azurerm-set-diff-analyzer | Instructions updated with new validation patterns - Update recommended |

## Local Skills Discovery Process

1. List all folders in `.github/skills/` directory
2. For each folder, read `SKILL.md` front matter to extract `name` and `description`
3. List any bundled assets within each skill folder
4. Build comprehensive inventory of existing skills with their capabilities
5. Use this inventory to avoid suggesting duplicates

## Version Comparison Process

1. For each local skill folder, construct the raw GitHub URL to fetch the remote `SKILL.md`:
   - Pattern: `https://raw.githubusercontent.com/github/awesome-copilot/main/skills/<skill-name>/SKILL.md`
2. Fetch the remote version using the `#fetch` tool
3. Compare entire file content (including front matter and body)
4. Identify specific differences:
   - **Front matter changes** (name, description)
   - **Instruction updates** (guidelines, examples, best practices)
   - **Bundled asset changes** (new, removed, or modified assets)
5. Document key differences for outdated skills
6. Calculate similarity to determine if update is needed

## Skill Structure Requirements

Based on the Agent Skills specification, each skill is a folder containing:

- **`SKILL.md`**: Main instruction file with front matter (`name`, `description`) and detailed instructions
- **Optional bundled assets**: Scripts, templates, reference data, and other files referenced from `SKILL.md`
- **Folder naming**: Lowercase with hyphens (e.g., `azure-deployment-preflight`)
- **Name matching**: The `name` field in `SKILL.md` front matter must match the folder name

## Front Matter Structure

Skills in awesome-copilot use this front matter format in `SKILL.md`:

```markdown
---
name: "skill-name"
description: "Brief description of what this skill provides and when to use it"
---
```

## Requirements

- Use `fetch` tool to get content from awesome-copilot repository skills documentation
- Use `githubRepo` tool to get individual skill content for download
- Scan local file system for existing skills in `.github/skills/` directory
- Read YAML front matter from local `SKILL.md` files to extract names and descriptions
- Compare local skills with remote versions to detect outdated skills
- Compare against existing skills in this repository to avoid duplicates
- Focus on gaps in current skill library coverage
- Validate that suggested skills align with repository's purpose and technology stack
- Provide clear rationale for each suggestion
- Include links to both awesome-copilot skills and similar local skills
- Clearly identify outdated skills with specific differences noted
- Consider bundled asset requirements and compatibility
- Don't provide any additional information or context beyond the table and the analysis

## Icons Reference

- ✅ Already installed and up-to-date
- ⚠️ Installed but outdated (update available)
- ❌ Not installed in repo

## Update Handling

When outdated skills are identified:

1. Include them in the output table with ⚠️ status
2. Document specific differences in the "Suggestion Rationale" column
3. Provide recommendation to update with key changes noted
4. When user requests update, replace entire local skill folder with remote version
5. Preserve folder location in `.github/skills/` directory
6. Ensure all bundled assets are downloaded alongside the updated `SKILL.md`


## Template References

Detailed templates in `templates/suggest-awesome-github-copilot-skills/`:


## Template References

Templates in `templates/suggest-awesome-github-copilot-skills/`:
- `context_analysis_criteria.md`
- `front_matter_structure.md`
- `icons_reference.md`
- `inputs.md`
- `local_skills_discovery_pr.md`
- `output_format.md`
- `phases.md`
- `process.md`
- `requirements.md`
- `rules.md`
- `skill_structure_requireme.md`
- `update_handling.md`
- `version_comparison_proces.md`
