---
author: Alexa
description: Use when creating automated tests or test harnesses for skills and agent
  behaviors.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: test-skill
tags:
- imported
title: Test Skill
version: 1.0.0

---
# Test Skill

## Description

Use when creating automated tests or test harnesses for skills, workflows, and tools.


## Skills Required

| Skill | Purpose |
|-------|---------|
| `terminal` | CLI commands execution |
| `file` | Read/write files |

## When to Use

Use this skill when:

- Setting up test infrastructure for a project
- Verifying test framework configuration
- Debugging test runner issues
- Checking test coverage
- Validating test environment setup
- Ensuring CI/CD test pipeline works

**Triggers**: "Set up tests", "Configure testing", "Test framework isn't working", "Check test setup", "Verify tests run", "Test infrastructure"

## When NOT to Use

- For writing individual tests (use test-driven-development instead)
- For debugging application code (use systematic-debugging instead)
- For code review (use requesting-code-review instead)
- For test authoring (use test-driven-development instead)

## Distinct Role

**test-skill** focuses on **test infrastructure and tooling** - making sure the testing system works. It answers "Is the test framework set up correctly?"

**test-driven-development** focuses on **writing tests and implementing code** using TDD methodology. It answers "How do I write good tests and implement features?"

**systematic-debugging** focuses on **investigating bugs in application code**. It answers "What's wrong with my code?"

These skills are complementary: use test-skill to set up infrastructure, test-driven-development to write tests, systematic-debugging to fix bugs.

## Workflow

### Phase 1: Verify Test Framework

- Check test framework is installed (Vitest, Jest, pytest, etc.)
- Verify configuration file exists (vitest.config.ts, jest.config.js, etc.)
- Confirm test runner can be invoked
- Check for any configuration errors

### Phase 2: Run Test Suite

- Execute test runner
- Verify tests are discovered
- Check for syntax errors in tests
- Confirm test output is readable

### Phase 3: Check Coverage

- Run coverage report
- Identify uncovered code
- Verify coverage meets project standards
- Document coverage baseline

### Phase 4: Validate CI/CD Integration

- Verify tests run in CI pipeline
- Check test results are reported
- Confirm failures block deployment
- Validate test artifacts are captured

### Phase 5: Document Setup

- Document test framework choice and rationale
- Record configuration details
- Create test running instructions
- Update project README with test commands

## Tools & References

**Related Skills**:

- test-driven-development - Write tests using TDD
- systematic-debugging - Debug application code
- requesting-code-review - Verify test quality

**Testing Frameworks**:

- JavaScript/TypeScript: Vitest, Jest, Mocha, Playwright
- Python: pytest, unittest, coverage
- Go: testing package, go test
- Java: JUnit, TestNG, Gradle

**Coverage Tools**:

- JavaScript: c8, nyc, Istanbul
- Python: coverage.py
- Go: go test -cover
- Java: JaCoCo

## Example Workflow

```plaintext
New project setup
↓
Choose test framework: Vitest
↓
Install: npm install -D vitest
↓
Create vitest.config.ts
↓
Write first test file: src/__tests__/example.test.ts
↓
Run: npm test
↓
Tests discovered and executed ✓
↓
Check coverage: npm test -- --coverage
↓
Coverage report generated ✓
↓
Add to CI/CD pipeline
↓
Tests run on every commit ✓
```

## Best Practices

- **Use standard frameworks**: Vitest, Jest, pytest (don't reinvent)
- **Version lock**: Pin test framework versions
- **Fast feedback**: Tests should run in <30 seconds
- **Parallel execution**: Run tests in parallel when possible
- **Clear output**: Test output should be easy to read
- **Coverage tracking**: Monitor coverage over time
- **CI integration**: Tests must run in CI pipeline

## Overview

Test Skill provides infrastructure and tooling for automated testing across multiple languages and frameworks. Handles framework setup, configuration verification, coverage tracking, and CI/CD integration to ensure reliable test execution.


## Pitfalls

- **Stale cache:** Always re-read files from disk after editing; don't rely on cached context
- **Context limits:** Process in batches; write results after each batch
## Verification Checklist

- [ ] Test framework is installed and configured correctly
- [ ] Test runner discovers and executes all tests
- [ ] Coverage reporting is enabled and meets project thresholds
- [ ] CI/CD pipeline runs tests and blocks on failures
- [ ] Test configuration is documented in project README
