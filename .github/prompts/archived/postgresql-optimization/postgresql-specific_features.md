# � PostgreSQL-Specific Features

> Extracted from `postgresql-optimization.prompt.md`.

## � PostgreSQL-Specific Features

### JSONB Operations

```sql
-- Advanced JSONB queries
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    data JSONB NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- GIN index for JSONB performance
CREATE INDEX idx_events_data_gin ON events USING gin(data);

-- JSONB containment and path queries
SELECT * FROM events
WHERE data @> '{"type": "login"}'
  AND data #>> '{user,role}' = 'admin';

-- JSONB aggregation
SELECT jsonb_agg(data) FROM events WHERE data ? 'user_id';
```

### Array Operations

```sql
-- PostgreSQL arrays
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    tags TEXT[],
    categories INTEGER[]
);

-- Array queries and operations
SELECT * FROM posts WHERE 'postgresql' = ANY(tags);
SELECT * FROM posts WHERE tags && ARRAY['database', 'sql'];
SELECT * FROM posts WHERE array_length(tags, 1) > 3;

-- Array aggregation
SELECT array_agg(DISTINCT category) FROM posts, unnest(categories) as category;
```

### Window Functions & Analytics

```sql
-- Advanced window functions
SELECT
    product_id,
    sale_date,
    amount,
    -- Running totals
    SUM(amount) OVER (PARTITION BY product_id ORDER BY sale_date) as running_total,
    -- Moving averages
    AVG(amount) OVER (PARTITION BY product_id ORDER BY sale_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as moving_avg,
    -- Rankings
    DENSE_RANK() OVER (PARTITION BY EXTRACT(month FROM sale_date) ORDER BY amount DESC) as monthly_rank,
    -- Lag/Lead for comparisons
    LAG(amount, 1) OVER (PARTITION BY product_id ORDER BY sale_date) as prev_amount
FROM sales;
```

### Full-Text Search

```sql
-- PostgreSQL full-text search
CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT,
    search_vector tsvector
);

-- Update search vector
UPDATE documents
SET search_vector = to_tsvector('english', title || ' ' || content);

-- GIN index for search performance
CREATE INDEX idx_documents_search ON documents USING gin(search_vector);

-- Search queries
SELECT * FROM documents
WHERE search_vector @@ plainto_tsquery('english', 'postgresql database');

-- Ranking results
SELECT *, ts_rank(search_vector, plainto_tsquery('postgresql')) as rank
FROM documents
WHERE search_vector @@ plainto_tsquery('postgresql')
ORDER BY rank DESC;
```
