# 📊 PostgreSQL Extensions & Tools

> Extracted from `postgresql-optimization.prompt.md`.

## 📊 PostgreSQL Extensions & Tools

### Useful Extensions

```sql
-- Enable commonly used extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";    -- UUID generation
CREATE EXTENSION IF NOT EXISTS "pgcrypto";     -- Cryptographic functions
CREATE EXTENSION IF NOT EXISTS "unaccent";     -- Remove accents from text
CREATE EXTENSION IF NOT EXISTS "pg_trgm";      -- Trigram matching
CREATE EXTENSION IF NOT EXISTS "btree_gin";    -- GIN indexes for btree types

-- Using extensions
SELECT uuid_generate_v4();                     -- Generate UUIDs
SELECT crypt('password', gen_salt('bf'));      -- Hash passwords
SELECT similarity('postgresql', 'postgersql'); -- Fuzzy matching
```

### Monitoring & Maintenance

```sql
-- Database size and growth
SELECT pg_size_pretty(pg_database_size(current_database())) as db_size;

-- Table and index sizes
SELECT schemaname, tablename,
       pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) as size
FROM pg_tables
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;

-- Index usage statistics
SELECT schemaname, tablename, indexname, idx_scan, idx_tup_read, idx_tup_fetch
FROM pg_stat_user_indexes
WHERE idx_scan = 0;  -- Unused indexes
```

### PostgreSQL-Specific Optimization Tips

- **Use EXPLAIN (ANALYZE, BUFFERS)** for detailed query analysis
- **Configure postgresql.conf** for your workload (OLTP vs OLAP)
- **Use connection pooling** (pgbouncer) for high-concurrency applications
- **Regular VACUUM and ANALYZE** for optimal performance
- **Partition large tables** using PostgreSQL 10+ declarative partitioning
- **Use pg_stat_statements** for query performance monitoring
