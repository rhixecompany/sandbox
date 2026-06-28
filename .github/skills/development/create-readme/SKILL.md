---
author: Hermes Agent
description: Use when creating a README.md file for a project. Generates a comprehensive,
  well-structured README based on project analysis.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: create-readme
tags:
- documentation
- readme
- project-setup
title: Create README
version: 1.0.0

---
# Create README

## Overview

Generate a comprehensive, well-structured README.md file for a project. This skill analyzes the entire project and creates documentation that is appealing, informative, and easy to read.

## When to Use

- Creating a README for a new project
- Updating an existing README that's outdated
- Standardizing README format across multiple projects
- Generating README after major project changes

## When NOT TO USE

- Projects that already have a comprehensive README
- Non-Markdown documentation (use project-docs)
- API reference documentation (use context7)

## Skills Required

| Skill | Purpose |
|-------|---------|
| `project-docs` | Full project documentation |
| `writing-clearly-and-concisely` | Clear, concise writing |

## Workflow

### Phase 1: Analyze Project

1. Review the entire project structure:
   ```bash
   ls -la
   cat package.json  # or equivalent manifest
   find src/ -name "*.ts" -o -name "*.py" | head -20
   ls tests/ docs/ examples/ 2>/dev/null
   ```

2. Identify key information:
   - Project name and purpose
   - Tech stack and dependencies
   - Entry points and main files
   - Available scripts (build, test, deploy)
   - Configuration requirements
   - Environment variables needed

3. Check for existing documentation:
   ```bash
   ls *.md docs/ 2>/dev/null
   cat CONTRIBUTING.md CHANGELOG.md LICENSE 2>/dev/null
   ```

### Phase 2: Generate README Structure

Create README.md with these sections:

```markdown
# Project Name

> One-line description of what this project does.

## Overview

2-3 sentences explaining the project's purpose and key features.

## Features

- Feature 1
- Feature 2
- Feature 3

## Prerequisites

- Node.js 20+ / Python 3.11+ / etc.
- Any required tools or services

## Installation

```bash
# Clone the repository
git clone https://github.com/user/repo.git
cd repo

# Install dependencies
npm install
# or
pip install -r requirements.txt
```

## Usage

```bash
# Start development server
npm run dev

# Run tests
npm test

# Build for production
npm run build
```

## Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `API_URL` | Backend API endpoint | `http://localhost:3000` |
| `DEBUG` | Enable debug mode | `false` |

## Project Structure

```
src/
├── index.ts          # Entry point
├── routes/           # API routes
├── models/           # Data models
└── utils/            # Shared utilities
tests/                # Test suite
docs/                 # Documentation
```

## Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server |
| `npm test` | Run test suite |
| `npm run build` | Build for production |
| `npm run lint` | Run linter |

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## License

[MIT](LICENSE) — see LICENSE file for details.
```

### Phase 3: Customize Content

1. Replace placeholders with actual project information
2. Add project-specific sections (Architecture, API Reference, Deployment, etc.)
3. Include badges if applicable (build status, coverage, version)
4. Add screenshots or diagrams for visual projects
5. Reference existing documentation files

### Phase 4: Verify

1. Check all links work
2. Verify code blocks are correct
3. Ensure installation steps actually work
4. Check formatting renders correctly on GitHub

## Verification Checklist

- [ ] Project name and description at top
- [ ] Installation instructions with copy-paste commands
- [ ] Usage examples
- [ ] Configuration/environment variables documented
- [ ] Project structure overview
- [ ] Available scripts documented
- [ ] Prerequisites listed
- [ ] License section present
- [ ] No LICENSE/CONTRIBUTING/CHANGELOG sections (those are separate files)
- [ ] GFM formatting used correctly
- [ ] GitHub admonition syntax for notes/warnings

## Pitfalls

- **Overuse of emojis:** Keep it professional — emojis are fine in moderation
- **Outdated instructions:** Test all commands before documenting
- **Missing prerequisites:** List all required tools, versions, and services
- **Too much detail:** Link to detailed docs instead of putting everything in README
- **Missing structure:** Use consistent heading hierarchy (H1 → H2 → H3)
