---
toolsets: ["codebase", "edit/editFiles", "search/codebase"]
license: MIT
author: Hermes Agent
version: 1.0.0
title: Generate Application from OpenAPI Spec
name: openapi-to-application-code
description: "Generate a complete, production-ready application from an OpenAPI specification"
tags:
  - api
  - generator
  - ml
  - prompts
  - specification
  - typescript
  - api
  - documentation
  - planning
  - specification
metadata:
  hermes:
    related_skills: []
    tags:
    - openapi-to-application-code.prompt

trigger: openapi-to-application-code

---


## Actions

- Follow the prompt workflow as specified.
- Produce the requested deliverable(s) in the exact structure requested.
- Validate output against acceptance criteria before finishing.
metadata:
  hermes:
    related_skills: []
    tags:
    - openapi-to-application-code.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - openapi-to-application-code.prompt

## Goal

Generate a complete, production-ready application from an OpenAPI specification.

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
> Core rules: [`prompts/templates/_shared/rules-core.md`](../templates/_shared/rules-core.md)


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

## Input Requirements

1. **OpenAPI Specification**: Provide either:
   - A URL to the OpenAPI spec (e.g., `https://api.example.com/openapi.json`)
   - A local file path to the OpenAPI spec
   - The full OpenAPI specification content pasted directly

2. **Project Details** (if not in spec):
   - Project name and description
   - Target framework and version
   - Package/namespace naming conventions
   - Authentication method (if not specified in OpenAPI)

## Generation Process

> ### Step 1: Analyze the OpenAPI Specification
> - Validate the OpenAPI spec for completeness and correctness

> **Full content:** `templates/openapi-to-application-code/generation_process.md`

## Output Structure

The generated application will include:

```
project-name/
├── README.md                      # Setup and usage instructions
├── [build-config]                 # Framework-specific build files (pom.xml, build.gradle, package.json, etc.)
├── src/
│   ├── main/
│   │   ├── [language]/
│   │   │   ├── controllers/       # HTTP endpoint handlers
│   │   │   ├── services/          # Business logic
│   │   │   ├── models/            # Data models and DTOs
│   │   │   ├── repositories/      # Data access (if applicable)
│   │   │   └── config/            # Application configuration
│   │   └── resources/             # Configuration files
│   └── test/
│       ├── [language]/
│       │   ├── controllers/       # Controller tests
│       │   └── services/          # Service tests
│       └── resources/             # Test configuration
├── .gitignore
├── .env.example                   # Environment variables template
└── docker-compose.yml             # Optional: Docker setup (if applicable)
```

## Best Practices Applied

- **Framework Conventions**: Follows framework-specific naming, structure, and patterns
- **Separation of Concerns**: Clear layers with controllers, services, and repositories
- **Error Handling**: Comprehensive error handling with meaningful responses
- **Validation**: Input validation and schema validation throughout
- **Logging**: Structured logging for debugging and monitoring
- **Testing**: Unit tests for services and controllers
- **Documentation**: Inline code documentation and setup instructions
- **Security**: Implements authentication/authorization from OpenAPI spec
- **Scalability**: Design patterns support growth and maintenance

## Next Steps

After generation:

1. Review the generated code structure and make customizations as needed
2. Install dependencies according to framework requirements
3. Configure environment variables and database connections
4. Run tests to verify generated code
5. Start the development server
6. Test endpoints using the provided examples

## Questions to Ask if Needed

- Should the application include database/ORM setup, or just in-memory/mock data?
- Do you want Docker configuration for containerization?
- Should authentication be JWT, OAuth2, API keys, or basic auth?
- Do you need integration tests or just unit tests?
- Any specific database technology preferences?
- Should the API include pagination, filtering, and sorting examples?


## Template References

Detailed templates in `templates/openapi-to-application-code/`:
- `generation_process.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
