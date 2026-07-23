# 📋 SQL Review Checklist

> Extracted from `sql-code-review.prompt.md`.

## 📋 SQL Review Checklist

### Security

- [ ] All user inputs are parameterized
- [ ] No dynamic SQL construction with string concatenation
- [ ] Appropriate access controls and permissions
- [ ] Sensitive data is properly protected
- [ ] SQL injection attack vectors are eliminated

### Performance

- [ ] Indexes exist for frequently queried columns
- [ ] No unnecessary SELECT \* statements
- [ ] JOINs are optimized and use appropriate types
- [ ] WHERE clauses are selective and use indexes
- [ ] Subqueries are optimized or converted to JOINs

### Code Quality

- [ ] Consistent naming conventions
- [ ] Proper formatting and indentation
- [ ] Meaningful comments for complex logic
- [ ] Appropriate data types are used
- [ ] Error handling is implemented

### Schema Design

- [ ] Tables are properly normalized
- [ ] Constraints enforce data integrity
- [ ] Indexes support query patterns
- [ ] Foreign key relationships are defined
- [ ] Default values are appropriate
