---
name: asdf
title: Asdf
description: "Use when installing or configuring asdf version manager, managing multiple runtime versions (Node.js, Python, Go), or migrating from nvm/pyenv/rbenv."
---

## Description

Universal version manager for multiple runtimes (Node.js, Python, Go, Terraform, etc.). Install, configure, and migrate between version managers.

## When to Use

Use this skill when:

- Installing or configuring asdf
- Managing multiple runtime versions
- Migrating from nvm, pyenv, rbenv
- Setting up .tool-versions files
- Configuring version manager plugins
- Managing development environment

**Triggers**: "Install asdf", "Set up version manager", "Migrate from nvm", "Configure .tool-versions", "Manage Node/Python/Go versions"

## When NOT to Use

- For Docker/container setup (use different approach)
- For CI/CD pipeline configuration (use specific CI tool)
- For system-wide package management (use OS package manager)

## Workflow

### Phase 1: Installation

- Install asdf runtime
- Add to shell configuration
- Verify installation
- Install plugins

### Phase 2: Configuration

- Create .tool-versions file
- Specify runtime versions
- Install specified versions
- Verify installations

### Phase 3: Usage

- Activate version management
- Switch between versions
- Update versions as needed
- Document version requirements

### Phase 4: Maintenance

- Update asdf and plugins
- Clean up old versions
- Backup .tool-versions
- Share with team

## Tools & References

**Related Skills**:

- git-helper - Version control
- task-management - Project management

**Supported Runtimes**:

- Node.js (nodejs)
- Python (python)
- Go (golang)
- Terraform (terraform)
- Ruby (ruby)
- Java (java)
- And 100+ more

## Best Practices

- **Commit .tool-versions**: Share version requirements with team
- **Use Latest Stable**: Keep runtimes up to date
- **Document Versions**: Record why specific versions are needed
- **Test Compatibility**: Verify code works with specified versions
- **Regular Updates**: Check for security updates

