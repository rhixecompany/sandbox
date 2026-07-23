# File Structure and Content Guidelines

> Extracted from `create-agentsmd.prompt.md`.

## File Structure and Content Guidelines

### 1. Required Setup

- Create the file as `AGENTS.md` in the repository root
- Use standard Markdown formatting
- No required fields - flexible structure based on project needs

### 2. Essential Sections to Include

#### Project Overview

- Brief description of what the project does
- Architecture overview if complex
- Key technologies and frameworks used

#### Setup Commands

- Installation instructions
- Environment setup steps
- Dependency management commands
- Database setup if applicable

#### Development Workflow

- How to start development server
- Build commands
- Watch/hot-reload setup
- Package manager specifics (npm, pnpm, yarn, etc.)

#### Testing Instructions

- How to run tests (unit, integration, e2e)
- Test file locations and naming conventions
- Coverage requirements
- Specific test patterns or frameworks used
- How to run subset of tests or focus on specific areas

#### Code Style Guidelines

- Language-specific conventions
- Linting and formatting rules
- File organization patterns
- Naming conventions
- Import/export patterns

#### Build and Deployment

- Build commands and outputs
- Environment configurations
- Deployment steps and requirements
- CI/CD pipeline information

### 3. Optional but Recommended Sections

#### Security Considerations

- Security testing requirements
- Secrets management
- Authentication patterns
- Permission models

#### Monorepo Instructions (if applicable)

- How to work with multiple packages
- Cross-package dependencies
- Selective building/testing
- Package-specific commands

#### Pull Request Guidelines

- Title format requirements
- Required checks before submission
- Review process
- Commit message conventions

#### Debugging and Troubleshooting

- Common issues and solutions
- Logging patterns
- Debug configuration
- Performance considerations
