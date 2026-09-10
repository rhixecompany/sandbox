# Actions for Create Feature

## Task T-1: Analyze requirements from spec
### Action 1.1
```bash
read_file .hermes/specs/create-feature-spec.md
```
- **Expected Output**: Requirements extracted
- **Verification**: Requirements list matches spec

## Task T-2: Create implementation plan
### Action 2.1
```bash
hermes create-plan --spec .hermes/specs/create-feature-spec.md
```
- **Expected Output**: Plan created
- **Verification**: Plan file exists with all phases

## Task T-3: Write failing tests (TDD)
### Action 3.1
```bash
pytest tests/ -v --tb=short
```
- **Expected Output**: Tests failing (RED)
- **Verification**: All new tests fail as expected
