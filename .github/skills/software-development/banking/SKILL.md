---
author: Alexa
description: Use when building and testing banking-domain examples, reference patterns,
  and prompts.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: banking
tags:
- imported
title: Banking
version: 1.0.0

---
# Banking

## Description

Use when building and testing banking-domain examples, including account operations and transaction processing.

## When to Use

Use this skill when:

- Developing banking/fintech features
- Fixing bugs in banking app
- Performing code reviews
- Working with wallet/transfer functionality
- Integrating Plaid or Dwolla
- Managing ACH transfers
- Implementing idempotency
- Using soft-delete patterns

**Triggers**: "Build banking feature", "Fix wallet bug", "Review banking code", "Integrate Plaid", "Handle ACH transfer", "Implement idempotency"

## When NOT to Use

- For non-banking applications
- For general Next.js questions (use context7 instead)
- For database questions unrelated to Drizzle (use general DB resources)
- For authentication unrelated to NextAuth v4

## Workflow

### Phase 1: Understand Requirements

- Review feature requirements
- Check existing patterns
- Identify dependencies
- Plan implementation

### Phase 2: Implementation

- Write database migrations
- Implement API routes
- Add business logic
- Integrate external services

### Phase 3: Testing

- Write unit tests
- Test integrations
- Verify idempotency
- Check error handling

### Phase 4: Review & Deploy

- Code review
- Security audit
- Performance check
- Deploy to production

## Tools & References

**Related Skills**:

- test-driven-development - Write tests first
- requesting-code-review - Get code reviewed
- systematic-debugging - Debug issues

**Tech Stack**:

- Next.js 16
- PostgreSQL
- Drizzle ORM
- NextAuth v4
- Plaid API
- Dwolla API

## Best Practices

- **Idempotency**: All operations must be idempotent
- **Soft Deletes**: Use soft-delete for audit trails
- **Transaction Safety**: Wrap multi-step operations in transactions
- **Error Handling**: Handle payment failures gracefully
- **Security**: Validate all inputs, use HTTPS
- **Logging**: Log all financial transactions

## Skills Required

| Skill | Purpose |
|-------|---------|
| `test-driven-development` | Write tests for banking operations |
| `requesting-code-review` | Get code reviewed before merge |
| `systematic-debugging` | Debug payment and transaction issues |

## Verification Checklist

- [ ] All banking operations are idempotent
- [ ] All financial transactions are logged
- [ ] Error handling covers payment failures gracefully
- [ ] Security validation is applied to all inputs
- [ ] Integration tests cover all external service calls

## Pitfalls

- Non-idempotent payment operations can cause duplicate charges
- Missing soft-delete patterns break audit trail requirements
- Not wrapping multi-step operations in transactions risks data inconsistency
- Insufficient error handling on payment failures leads to lost funds
- Skipping input validation opens security vulnerabilities
