# 🎯 PostgreSQL Code Quality Checklist

> Extracted from `postgresql-code-review.prompt.md`.

## 🎯 PostgreSQL Code Quality Checklist

### Schema Design

- [ ] Using appropriate PostgreSQL data types (CITEXT, JSONB, arrays)
- [ ] Leveraging ENUM types for constrained values
- [ ] Implementing proper CHECK constraints
- [ ] Using TIMESTAMPTZ instead of TIMESTAMP
- [ ] Defining custom domains for reusable constraints

### Performance Considerations

- [ ] Appropriate index types (GIN for JSONB/arrays, GiST for ranges)
- [ ] JSONB queries using containment operators (@>, ?)
- [ ] Array operations using PostgreSQL-specific operators
- [ ] Proper use of window functions and CTEs
- [ ] Efficient use of PostgreSQL-specific functions

### PostgreSQL Features Utilization

- [ ] Using extensions where appropriate
- [ ] Implementing stored procedures in PL/pgSQL when beneficial
- [ ] Leveraging PostgreSQL's advanced SQL features
- [ ] Using PostgreSQL-specific optimization techniques
- [ ] Implementing proper error handling in functions

### Security and Compliance

- [ ] Row Level Security (RLS) implementation where needed
- [ ] Proper role and privilege management
- [ ] Using PostgreSQL's built-in encryption functions
- [ ] Implementing audit trails with PostgreSQL features
