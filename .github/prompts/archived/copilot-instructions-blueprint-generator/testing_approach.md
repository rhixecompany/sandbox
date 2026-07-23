# Testing Approach

> Extracted from `copilot-instructions-blueprint-generator.prompt.md`.

## Testing Approach

${TESTING_REQUIREMENTS.includes("Unit") || TESTING_REQUIREMENTS == "All" ? `### Unit Testing

- Match the exact structure and style of existing unit tests
- Follow the same naming conventions for test classes and methods
- Use the same assertion patterns found in existing tests
- Apply the same mocking approach used in the codebase
- Follow existing patterns for test isolation` : ""}

${TESTING_REQUIREMENTS.includes("Integration") || TESTING_REQUIREMENTS == "All" ? `### Integration Testing

- Follow the same integration test patterns found in the codebase
- Match existing patterns for test data setup and teardown
- Use the same approach for testing component interactions
- Follow existing patterns for verifying system behavior` : ""}

${TESTING_REQUIREMENTS.includes("E2E") || TESTING_REQUIREMENTS == "All" ? `### End-to-End Testing

- Match the existing E2E test structure and patterns
- Follow established patterns for UI testing
- Apply the same approach for verifying user journeys` : ""}

${TESTING_REQUIREMENTS.includes("TDD") || TESTING_REQUIREMENTS == "All" ? `### Test-Driven Development

- Follow TDD patterns evident in the codebase
- Match the progression of test cases seen in existing code
- Apply the same refactoring patterns after tests pass` : ""}

${TESTING_REQUIREMENTS.includes("BDD") || TESTING_REQUIREMENTS == "All" ? `### Behavior-Driven Development

- Match the existing Given-When-Then structure in tests
- Follow the same patterns for behavior descriptions
- Apply the same level of business focus in test cases` : ""}
