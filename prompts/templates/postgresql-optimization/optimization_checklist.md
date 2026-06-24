# 📋 Optimization Checklist

> Extracted from `postgresql-optimization.prompt.md`.

## 📋 Optimization Checklist

### Query Analysis

- [ ] Run EXPLAIN ANALYZE for expensive queries
- [ ] Check for sequential scans on large tables
- [ ] Verify appropriate join algorithms
- [ ] Review WHERE clause selectivity
- [ ] Analyze sort and aggregation operations

### Index Strategy

- [ ] Create indexes for frequently queried columns
- [ ] Use composite indexes for multi-column searches
- [ ] Consider partial indexes for filtered queries
- [ ] Remove unused or duplicate indexes
- [ ] Monitor index bloat and fragmentation

### Security Review

- [ ] Use parameterized queries exclusively
- [ ] Implement proper access controls
- [ ] Enable row-level security where needed
- [ ] Audit sensitive data access
- [ ] Use secure connection methods

### Performance Monitoring

- [ ] Set up query performance monitoring
- [ ] Configure appropriate log settings
- [ ] Monitor connection pool usage
- [ ] Track database growth and maintenance needs
- [ ] Set up alerting for performance degradation
