# 🛠️ Common Query Patterns

> Extracted from `postgresql-optimization.prompt.md`.

## 🛠️ Common Query Patterns

### Pagination

```sql
-- ❌ BAD: OFFSET for large datasets
SELECT * FROM products ORDER BY id OFFSET 10000 LIMIT 20;

-- ✅ GOOD: Cursor-based pagination
SELECT * FROM products
WHERE id > $last_id
ORDER BY id
LIMIT 20;
```

### Aggregation

```sql
-- ❌ BAD: Inefficient grouping
SELECT user_id, COUNT(*)
FROM orders
WHERE order_date >= '2024-01-01'
GROUP BY user_id;

-- ✅ GOOD: Optimized with partial index
CREATE INDEX idx_orders_recent ON orders(user_id)
WHERE order_date >= '2024-01-01';

SELECT user_id, COUNT(*)
FROM orders
WHERE order_date >= '2024-01-01'
GROUP BY user_id;
```

### JSON Queries

```sql
-- ❌ BAD: Inefficient JSON querying
SELECT * FROM users WHERE data::text LIKE '%admin%';

-- ✅ GOOD: JSONB operators and GIN index
CREATE INDEX idx_users_data_gin ON users USING gin(data);

SELECT * FROM users WHERE data @> '{"role": "admin"}';
```
