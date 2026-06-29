# ⚡ Performance Optimization

> Extracted from `sql-code-review.prompt.md`.

## ⚡ Performance Optimization

### Query Structure Analysis

```sql
-- ❌ BAD: Inefficient query patterns
SELECT DISTINCT u.*
FROM users u, orders o, products p
WHERE u.id = o.user_id
AND o.product_id = p.id
AND YEAR(o.order_date) = 2024;

-- ✅ GOOD: Optimized structure
SELECT u.id, u.name, u.email
FROM users u
INNER JOIN orders o ON u.id = o.user_id
WHERE o.order_date >= '2024-01-01'
AND o.order_date < '2025-01-01';
```

### Index Strategy Review

- **Missing Indexes**: Identify columns that need indexing
- **Over-Indexing**: Find unused or redundant indexes
- **Composite Indexes**: Multi-column indexes for complex queries
- **Index Maintenance**: Check for fragmented or outdated indexes

### Join Optimization

- **Join Types**: Verify appropriate join types (INNER vs LEFT vs EXISTS)
- **Join Order**: Optimize for smaller result sets first
- **Cartesian Products**: Identify and fix missing join conditions
- **Subquery vs JOIN**: Choose the most efficient approach

### Aggregate and Window Functions

```sql
-- ❌ BAD: Inefficient aggregation
SELECT user_id,
       (SELECT COUNT(*) FROM orders o2 WHERE o2.user_id = o1.user_id) as order_count
FROM orders o1
GROUP BY user_id;

-- ✅ GOOD: Efficient aggregation
SELECT user_id, COUNT(*) as order_count
FROM orders
GROUP BY user_id;
```
