---
name: "documentation"
description: "Documentation standards for this repository"
applyTo: "**/*.md,**/*.ts,**/*.tsx"
---


# Code Documentation Standards

- **Priority Tiers:** Required (must exist before merge): TSDoc Comments, Component Props, API Documentation (endpoints). Recommended (must exist before release): README Standards, Architecture Documentation. Optional (add when relevant): Inline Documentation items.

- **TSDoc Comments:** Use TSDoc syntax for function and class documentation
- **Type Documentation:** Document types and interfaces that have more than 3 properties, use generics, or represent domain concepts (e.g., not primitives or simple aliases).
- **Component Props:** Document React component props with clear descriptions
- **API Documentation:** Document all API endpoints with parameters and responses
- **Hook Documentation:** Document custom hook usage and dependencies

## README Standards

- **Project Overview:** Provide clear project description and purpose
- **Setup Instructions:** Include complete development environment setup
- **Usage Examples:** Provide practical usage examples and code snippets
- **Public API Overview:** Document public APIs and integration patterns, and link to full endpoint documentation instead of duplicating endpoint parameter/response tables.
- **Contributing Guidelines:** Include contribution workflow and standards

## Architecture Documentation

- **System Design:** Document major architectural decisions
- **Data Flow:** Explain data flow patterns and state management
- **Database Schema:** Maintain up-to-date schema documentation
- **Authentication Flow:** Document authentication and authorization patterns
- **Environment Variables:** Maintain a `.env.example` file with every required variable listed, a non-sensitive default or placeholder value, and a one-line comment describing its purpose and where to obtain the value.
- **Deployment:** Document deployment processes and requirements

## Inline Documentation

- **Complex Logic:** Add inline comments for any algorithm with cyclomatic complexity > 5, non-obvious O(n²) or worse operations, or logic that encodes a non-obvious business rule.
- **Configuration:** Document configuration options and their effects
- **Workarounds:** Explain temporary fixes and their reasons
- **Dependencies:** Document external dependency choices and alternatives
- **Performance Considerations:** Note performance implications of code decisions

## Documentation Maintenance

- **Version Control:** Update all affected TSDoc comments, README sections, and architecture docs in the same PR as the code change. PRs with API changes must not be merged without corresponding documentation updates.
- **Regular Reviews:** Review and update documentation on every PR that changes public APIs, and run a full documentation audit at the start of each sprint.
- **Link Validation:** Ensure all internal links remain valid
- **Example Updates:** Keep code examples current with latest practices
- **Accessibility:** Ensure documentation is accessible to all team members
