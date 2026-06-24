# Configuration Files to Create

> Extracted from `github-copilot-starter.prompt.md`.

## Configuration Files to Create

Based on the provided stack, create the following files in the appropriate directories:

### 1. `.github/copilot-instructions.md`

Main repository instructions that apply to all Copilot interactions.

### 2. `.github/instructions/` Directory

Create specific instruction files:

- `${primaryLanguage}.instructions.md` - Language-specific guidelines
- `testing.instructions.md` - Testing standards and practices
- `documentation.instructions.md` - Documentation requirements
- `security.instructions.md` - Security best practices
- `performance.instructions.md` - Performance optimization guidelines
- `code-review.instructions.md` - Code review standards and GitHub review guidelines

### 3. `.github/prompts/` Directory

Create reusable prompt files:

- `setup-component.prompt.md` - Component/module creation
- `write-tests.prompt.md` - Test generation
- `code-review.prompt.md` - Code review assistance
- `refactor-code.prompt.md` - Code refactoring
- `generate-docs.prompt.md` - Documentation generation
- `debug-issue.prompt.md` - Debugging assistance

### 4. `.github/agents/` Directory

Create specialized chat modes:

- `architect.agent.md` - Architecture planning mode
- `reviewer.agent.md` - Code review mode
- `debugger.agent.md` - Debugging mode

**Chat Mode Attribution**: When using content from awesome-copilot chatmodes, add attribution comments:

```markdown
<!-- Based on/Inspired by: https://github.com/github/awesome-copilot/blob/main/agents/[filename].agent.md -->
```

### 5. `.github/workflows/` Directory

Create Coding Agent workflow file:

- `copilot-setup-steps.yml` - GitHub Actions workflow for Coding Agent environment setup

**CRITICAL**: The workflow MUST follow this exact structure:

- Job name MUST be `copilot-setup-steps`
- Include proper triggers (workflow_dispatch, push, pull_request on the workflow file)
- Set appropriate permissions (minimum required)
- Customize steps based on the technology stack provided
