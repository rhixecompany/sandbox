# Example Subagent-Driven Development Plan

## Goal
Demonstrate full subagent-driven-development workflow with 3 granular tasks.

## Tasks

### Task 1: Create Hello World Module
- **File**: `src/hello.py`
- **Spec**: Create a `hello()` function that returns "Hello, World!" with a `name` parameter defaulting to "World"
- **Test**: `tests/test_hello.py` with pytest, test default and custom name
- **TDD**: Write test first (fail), implement (pass), verify no regressions

### Task 2: Add Greeting Formatter
- **File**: `src/greeting.py`
- **Spec**: Create `format_greeting(name: str, style: str = "casual") -> str` function
  - Styles: "casual" → "Hey {name}!", "formal" → "Greetings, {name}."
  - Default: "casual"
- **Test**: `tests/test_greeting.py` with tests for both styles
- **TDD**: Write test first (fail), implement (pass)

### Task 3: Create CLI Entry Point
- **File**: `src/cli.py`
- **Spec**: Create `main()` function using argparse
  - `--name` argument (default: "World")
  - `--style` argument (choices: casual, formal, default: casual)
  - Prints formatted greeting
- **Test**: `tests/test_cli.py` with subprocess tests
- **Integration**: Import and use `hello()` and `format_greeting()`

## Dependencies
- Task 1 must complete before Task 2 (greeting uses hello)
- Task 2 must complete before Task 3 (CLI uses both)

## Acceptance Criteria (per task)
- [ ] Test written first and fails
- [ ] Implementation passes test
- [ ] All tests pass (no regressions)
- [ ] Spec compliance review PASS
- [ ] Code quality review APPROVED
- [ ] Committed with conventional commit message

## Project Conventions
- Python 3.11, pytest for testing
- Type hints required
- Ruff for linting (if available)
- File structure: `src/`, `tests/`
- Commit format: `type: description` (feat, fix, test, refactor)