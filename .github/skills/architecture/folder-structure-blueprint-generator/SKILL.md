---
name: folder-structure-blueprint-generator
title: "Folder Structure Blueprint Generator"
description: "Use when analyzing and documenting project folder structures. Auto-detects project types (.NET, Java, React, Angular, Python, Node.js, Flutter), generates detailed blueprints with visualization options, naming conventions, and file placement patterns."
version: 1.1.0
author: "Hermes Agent"
license: MIT
tags: [architecture, documentation, folder-structure, blueprint]
metadata:
  hermes:
    tags: [imported]
---
# Folder Structure Blueprint Generator

## Overview

Analyze a project's folder structure and generate a comprehensive blueprint document that serves as a definitive guide for maintaining consistent code organization. The blueprint includes directory visualization, naming conventions, file placement patterns, and extension templates.

## When to Use

- Documenting folder structure for a new or existing project
- Onboarding team members to a codebase's organization
- Establishing folder conventions for a new project
- Reviewing and improving existing folder organization

## When NOT TO USE

- Generating architecture diagrams (use architecture-blueprint-generator)
- Documenting technology stack (use technology-stack-blueprint-generator)
- Small projects with <5 directories

## Skills Required

| Skill | Purpose |
|-------|---------|
| `codemap` | Generate component hierarchy |
| `project-docs` | Full documentation set |
| `architecture-blueprint-generator` | Full architecture blueprint |

## Workflow

### Phase 1: Auto-Detect Project Type

Scan the project for technology signatures:
- `.sln`, `.csproj` → .NET
- `pom.xml`, `build.gradle` → Java
- `package.json` with React/Angular/Vue → JavaScript framework
- `requirements.txt`, `pyproject.toml` → Python
- `pubspec.yaml` → Flutter

### Phase 2: Analyze Structure

1. Map the directory tree to the configured depth level
2. Identify organizational principles (by feature, by layer, by domain)
3. Document naming conventions for files and folders
4. Note file placement patterns by type

### Phase 3: Generate Blueprint

Use the template at `templates/blueprint-template.md` to generate a comprehensive document including:
- Structural overview
- Directory visualization (ASCII tree, Markdown list, or table)
- Key directory analysis
- File placement patterns
- Naming conventions
- Extension templates

### Phase 4: Save Output

Save the blueprint to `docs/Project_Folders_Structure_Blueprint.md`

## Verification Checklist

- [ ] Project type auto-detected correctly
- [ ] Directory tree mapped to configured depth
- [ ] Naming conventions documented
- [ ] File placement patterns identified
- [ ] Blueprint saved to docs/ folder

## Pitfalls

- **Too much detail:** Focus on patterns, not every file
- **Missing generated folders:** Decide whether to include `node_modules/`, `dist/`, etc.
- **Outdated blueprints:** Update when folder structure changes significantly
