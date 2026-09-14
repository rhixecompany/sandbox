---
applyTo: src/dal/**/*.ts,src/database/**/*.ts
description: "Database best practices: Drizzle ORM, type-safe queries, schema migrations, N+1 prevention, secure data handling."
---

# Database Best Practices (Drizzle/Postgres)

- Use Drizzle query builders, never raw SQL
- Eager load relations to prevent N+1 queries
- Use type-safe filtering (eq, and, or)
- Document schema changes and migrations
- Secure sensitive data and credentials
- Test queries and migrations before production
