# Workflow Template Structure

> Extracted from `github-copilot-starter.prompt.md`.

## Workflow Template Structure

The `copilot-setup-steps.yml` workflow MUST follow this exact format and KEEP IT SIMPLE:

```yaml
name: "Copilot Setup Steps"
on:
  workflow_dispatch:
  push:
    paths:
      - .github/workflows/copilot-setup-steps.yml
  pull_request:
    paths:
      - .github/workflows/copilot-setup-steps.yml
jobs:
  # The job MUST be called `copilot-setup-steps` or it will not be picked up by Copilot.
  copilot-setup-steps:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - name: Checkout code
        uses: actions/checkout@v5
      # Add ONLY basic technology-specific setup steps here
```

**KEEP WORKFLOWS SIMPLE** - Only include essential steps:

**Node.js/JavaScript:**

```yaml
- name: Set up Node.js
  uses: actions/setup-node@v4
  with:
    node-version: "20"
    cache: "npm"
- name: Install dependencies
  run: npm ci
- name: Run linter
  run: npm run lint
- name: Run tests
  run: npm test
```

**Python:**

```yaml
- name: Set up Python
  uses: actions/setup-python@v4
  with:
    python-version: "3.11"
- name: Install dependencies
  run: pip install -r requirements.txt
- name: Run linter
  run: flake8 .
- name: Run tests
  run: pytest
```

**Java:**

```yaml
- name: Set up JDK
  uses: actions/setup-java@v4
  with:
    java-version: "17"
    distribution: "temurin"
- name: Build with Maven
  run: mvn compile
- name: Run tests
  run: mvn test
````

**AVOID in workflows:**

- ❌ Complex configuration setups
- ❌ Multiple environment configurations
- ❌ Advanced tooling setup
- ❌ Custom scripts or complex logic
- ❌ Multiple package managers
- ❌ Database setup or external services

**INCLUDE only:**

- ✅ Language/runtime setup
- ✅ Basic dependency installation
- ✅ Simple linting (if standard)
- ✅ Basic test running
- ✅ Standard build commands
