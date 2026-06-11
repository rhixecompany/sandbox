---
description: "Best practices for writing JavaScript/TypeScript tests using Jest, including mocking strategies, test structure, and common patterns."
agent: "agent"
---

## Goal

Best practices for writing JavaScript/TypeScript tests using Jest, including mocking strategies, test structure, and common patterns.

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
### Test Structure

- Name test files with `.test.ts` or `.test.js` suffix
- Place test files next to the code they test or in a dedicated `__tests__` directory
- Use descriptive test names that explain the expected behavior
- Use nested describe blocks to organize related tests
- Follow the pattern: `describe('Component/Function/Class', () => { it('should do something', () => {}) })`

### Effective Mocking

- Mock external dependencies (APIs, databases, etc.) to isolate your tests
- Use `jest.mock()` for module-level mocks
- Use `jest.spyOn()` for specific function mocks
- Use `mockImplementation()` or `mockReturnValue()` to define mock behavior
- Reset mocks between tests with `jest.resetAllMocks()` in `afterEach`

### Testing Async Code

- Always return promises or use async/await syntax in tests
- Use `resolves`/`rejects` matchers for promises
- Set appropriate timeouts for slow tests with `jest.setTimeout()`

### Snapshot Testing

- Use snapshot tests for UI components or complex objects that change infrequently
- Keep snapshots small and focused
- Review snapshot changes carefully before committing

### Testing React Components

- Use React Testing Library over Enzyme for testing components
- Test user behavior and component accessibility
- Query elements by accessibility roles, labels, or text content
- Use `userEvent` over `fireEvent` for more realistic user interactions

## Common Jest Matchers

- Basic: `expect(value).toBe(expected)`, `expect(value).toEqual(expected)`
- Truthiness: `expect(value).toBeTruthy()`, `expect(value).toBeFalsy()`
- Numbers: `expect(value).toBeGreaterThan(3)`, `expect(value).toBeLessThanOrEqual(3)`
- Strings: `expect(value).toMatch(/pattern/)`, `expect(value).toContain('substring')`
- Arrays: `expect(array).toContain(item)`, `expect(array).toHaveLength(3)`
- Objects: `expect(object).toHaveProperty('key', value)`
- Exceptions: `expect(fn).toThrow()`, `expect(fn).toThrow(Error)`
- Mock functions: `expect(mockFn).toHaveBeenCalled()`, `expect(mockFn).toHaveBeenCalledWith(arg1, arg2)`
