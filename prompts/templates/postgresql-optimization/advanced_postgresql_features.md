# 🚀 Advanced PostgreSQL Features

> Extracted from `postgresql-optimization.prompt.md`.

## 🚀 Advanced PostgreSQL Features

### Window Functions
```sql
-- Running totals and rankings
SELECT
    product_id,
    order_date,
    amount,
    SUM(amount) OVER (PARTITION BY product_id ORDER BY order_date) as running_total,
    ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY amount DESC) as rank
FROM sales;
````

### Common Table Expressions (CTEs)

```sql
-- Recursive queries for hierarchical data
WITH RECURSIVE category_tree AS (
    SELECT id, name, parent_id, 1 as level
    FROM categories
    WHERE parent_id IS NULL

    UNION ALL

    SELECT c.id, c.name, c.parent_id, ct.level + 1
    FROM categories c
    JOIN category_tree ct ON c.parent_id = ct.id
)
SELECT * FROM category_tree ORDER BY level, name;
```

Focus on providing specific, actionable PostgreSQL optimizations that improve query performance, security, and maintainability while leveraging PostgreSQL's advanced features.
