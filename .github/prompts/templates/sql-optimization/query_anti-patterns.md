# 🔍 Query Anti-Patterns

> Extracted from `sql-optimization.prompt.md`.

## 🔍 Query Anti-Patterns

### SELECT Performance Issues

```sql
-- ❌ BAD: SELECT * anti-pattern
SELECT * FROM large_table lt
JOIN another_table at ON lt.id = at.ref_id;

-- ✅ GOOD: Explicit column selection
SELECT lt.id, lt.name, at.value
FROM large_table lt
JOIN another_table at ON lt.id = at.ref_id;
```

### WHERE Clause Optimization

```sql
-- ❌ BAD: Function calls in WHERE clause
SELECT * FROM orders
WHERE UPPER(customer_email) = 'JOHN@EXAMPLE.COM';

-- ✅ GOOD: Index-friendly WHERE clause
SELECT * FROM orders
WHERE customer_email = 'john@example.com';
-- Consider: CREATE INDEX idx_orders_email ON orders(LOWER(customer_email));
```

### OR vs UNION Optimization

```sql
-- ❌ BAD: Complex OR conditions
SELECT * FROM products
WHERE (category = 'electronics' AND price < 1000)
   OR (category = 'books' AND price < 50);

-- ✅ GOOD: UNION approach for better optimization
SELECT * FROM products WHERE category = 'electronics' AND price < 1000
UNION ALL
SELECT * FROM products WHERE category = 'books' AND price < 50;
```
