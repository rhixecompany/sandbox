---
name: code-docs
title: "Code Documentation"
description: "Use when writing Google Style docstrings for Python, Go, or Terraform code, or ensuring consistent documentation standards across projects."
version: 1.0.0
author: "Hermes Agent"
license: MIT
tags: [documentation, docstrings, google-style, python, go, terraform]
metadata:
  hermes:
    tags: [imported]
---
# Code Documentation (Google Style)

## Overview

Write and maintain Google Style docstrings for Python, Go, and Terraform code. Google Style provides a consistent, readable format that works well with documentation generators and IDE tooltips.

## When to Use

- Writing docstrings for Python functions, classes, and modules
- Documenting Go packages, functions, and types
- Creating Terraform module documentation
- Establishing documentation standards across a project
- Adding docstrings to existing undocumented code
- Reviewing code for documentation completeness

## When NOT to Use

- Non-Python/Go/Terraform languages (use language-specific guides)
- General prose documentation (use project-docs)
- API reference generation (use context7)
- Quick inline comments within functions

## Skills Required

| Skill | Purpose |
|-------|---------|
| `project-docs` | Full project documentation |
| `writing-clearly-and-concisely` | Improve prose clarity |

## Workflow

### Phase 1: Understand Google Style Conventions

**Python (Google Style):**
```python
def function_name(param1: int, param2: str = "default") -> bool:
    """One-line summary of the function.

    Extended description of the function's behavior, including any
    important details that the one-line summary didn't cover.

    Args:
        param1: Description of param1.
        param2: Description of param2. Defaults to "default".

    Returns:
        Description of the return value.

    Raises:
        ValueError: When param1 is negative.
        TypeError: When param1 is not an integer.

    Example:
        >>> function_name(5, "test")
        True
        >>> function_name(-1)
        Traceback (most recent call last):
            ...
        ValueError: param1 must be non-negative
    """
```

**Go (Godoc style — Go's equivalent of Google Style):**
```go
// Package auth provides authentication and authorization utilities.
package auth

// User represents an authenticated user in the system.
type User struct {
    ID    string
    Email string
    Role  string
}

// Authenticate validates credentials and returns a User.
// Returns nil and an error if authentication fails.
func Authenticate(token string) (*User, error) {
    // ...
}
```

**Terraform:**
```hcl
# Module: aws-vpc
# Description: Creates a VPC with public and private subnets
# Author: Team Name
# Version: 1.0.0

variable "vpc_cidr" {
  description = "CIDR block for the VPC (e.g., 10.0.0.0/16)"
  type        = string
  default     = "10.0.0.0/16"

  validation {
    condition     = can(cidrhost(var.vpc_cidr, 0))
    error_message = "Must be a valid CIDR block."
  }
}
```

### Phase 2: Write Docstrings

For each public function/class/module:

1. **One-line summary** — Start with imperative mood ("Return X", "Create Y", not "Returns X")
2. **Extended description** — Add detail if the summary isn't sufficient
3. **Args/Parameters** — Document each parameter with type and description
4. **Returns** — Document return value and type
5. **Raises/Errors** — Document exceptions/error conditions
6. **Examples** — Include usage examples for complex functions

### Phase 3: Format Consistently

Rules:
- Use triple double-quotes (`"""`) for Python docstrings
- Start summary on the same line as opening quotes
- Leave blank line between summary and extended description
- Align parameter descriptions
- Use `>>>` for Python doctest examples
- Capitalize first letter of each docstring
- End with closing `"""` on its own line

### Phase 4: Verify & Review

1. Check all public APIs are documented
2. Verify examples actually run (for Python doctests)
3. Ensure parameter types match actual types
4. Review for clarity and completeness
5. Run documentation generator (Sphinx, godoc, terraform-docs) if configured

## Verification Checklist

- [ ] All public functions/classes have docstrings
- [ ] One-line summaries use imperative mood
- [ ] All parameters documented with types
- [ ] Return values documented
- [ ] Exceptions/errors documented
- [ ] Examples provided for complex functions
- [ ] Docstring format is consistent across files
- [ ] Docstrings updated when code changes

## Example: Full Python Module

```python
"""User authentication module.

Provides functions for authenticating users, managing sessions,
and verifying permissions.
"""

from typing import Optional

MAX_LOGIN_ATTEMPTS = 5


def authenticate(username: str, password: str) -> Optional[str]:
    """Authenticate a user and return a session token.

    Validates credentials against the user database and creates
    a new session if authentication succeeds.

    Args:
        username: The user's login name.
        password: The user's plaintext password (hashed internally).

    Returns:
        A session token string if authentication succeeds,
        or None if credentials are invalid.

    Raises:
        AccountLockedError: When max login attempts exceeded.

    Example:
        >>> token = authenticate("admin", "secret")
        >>> token is not None
        True
        >>> authenticate("admin", "wrong") is None
        True
    """
    pass


class AccountLockedError(Exception):
    """Raised when a user exceeds the maximum login attempts."""
    pass
```

## Pitfalls

- **Stale docstrings:** Docstrings that don't match the code are worse than no docstring — update them with every change
- **Over-documenting:** Don't document self-explanatory parameters like `name: str` unless the constraint is non-obvious
- **Under-documenting:** Don't skip edge cases, exceptions, or non-obvious behavior
- **Wrong style:** Stick to one style (Google) per project — don't mix styles
- **Missing examples:** Complex functions need examples — they're worth more than paragraphs of prose
