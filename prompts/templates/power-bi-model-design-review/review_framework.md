# Review Framework

> Extracted from `power-bi-model-design-review.prompt.md`.

## Review Framework

### **Comprehensive Model Assessment**

When reviewing a Power BI data model, conduct analysis across these key dimensions:

#### 1. **Schema Architecture Review**

```
Star Schema Compliance:
□ Clear separation of fact and dimension tables
□ Proper grain consistency within fact tables
□ Dimension tables contain descriptive attributes
□ Minimal snowflaking (justified when present)
□ Appropriate use of bridge tables for many-to-many

Table Design Quality:
□ Meaningful table and column names
□ Appropriate data types for all columns
□ Proper primary and foreign key relationships
□ Consistent naming conventions
□ Adequate documentation and descriptions
```

#### 2. **Relationship Design Evaluation**

```
Relationship Quality Assessment:
□ Correct cardinality settings (1:*, *:*, 1:1)
□ Appropriate filter directions (single vs. bidirectional)
□ Referential integrity settings optimized
□ Hidden foreign key columns from report view
□ Minimal circular relationship paths

Performance Considerations:
□ Integer keys preferred over text keys
□ Low-cardinality relationship columns
□ Proper handling of missing/orphaned records
□ Efficient cross-filtering design
□ Minimal many-to-many relationships
```

#### 3. **Storage Mode Strategy Review**

```
Storage Mode Optimization:
□ Import mode used appropriately for small-medium datasets
□ DirectQuery implemented properly for large/real-time data
□ Composite models designed with clear strategy
□ Dual storage mode used effectively for dimensions
□ Hybrid mode applied appropriately for fact tables

Performance Alignment:
□ Storage modes match performance requirements
□ Data freshness needs properly addressed
□ Cross-source relationships optimized
□ Aggregation strategies implemented where beneficial
```
