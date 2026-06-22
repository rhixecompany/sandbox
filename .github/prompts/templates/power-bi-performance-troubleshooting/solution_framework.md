# Solution Framework

> Extracted from `power-bi-performance-troubleshooting.prompt.md`.

## Solution Framework

### **Immediate Performance Fixes**

#### Model Optimization:

```dax
-- Replace inefficient patterns:

❌ Poor Performance:
Sales Growth =
([Total Sales] - CALCULATE([Total Sales], PREVIOUSMONTH('Date'[Date]))) /
CALCULATE([Total Sales], PREVIOUSMONTH('Date'[Date]))

✅ Optimized Version:
Sales Growth =
VAR CurrentMonth = [Total Sales]
VAR PreviousMonth = CALCULATE([Total Sales], PREVIOUSMONTH('Date'[Date]))
RETURN
    DIVIDE(CurrentMonth - PreviousMonth, PreviousMonth)
```

#### Report Optimization:

- Reduce visuals per page to 6-8 maximum
- Implement drill-through instead of showing all details
- Use bookmarks for different views instead of multiple visuals
- Apply filters early to reduce data volume
- Optimize slicer selections and cross-filtering

#### Data Model Optimization:

- Remove unused columns and tables
- Optimize data types (integers vs. text, dates vs. datetime)
- Replace calculated columns with measures where possible
- Implement proper star schema relationships
- Use incremental refresh for large datasets

### **Advanced Performance Solutions**

#### Storage Mode Optimization:

```
Import Mode Optimization:
- Data reduction techniques
- Pre-aggregation strategies
- Incremental refresh implementation
- Compression optimization

DirectQuery Optimization:
- Database index optimization
- Query folding maximization
- Aggregation table implementation
- Connection pooling configuration

Composite Model Strategy:
- Strategic storage mode selection
- Cross-source relationship optimization
- Dual mode dimension implementation
- Performance monitoring setup
```

#### Infrastructure Scaling:

```
Capacity Scaling Considerations:
- Vertical scaling (more powerful capacity)
- Horizontal scaling (distributed workload)
- Geographic distribution optimization
- Load balancing implementation

Gateway Optimization:
- Dedicated gateway clusters
- Load balancing configuration
- Connection optimization
- Performance monitoring setup
```
