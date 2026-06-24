# Troubleshooting Methodology

> Extracted from `power-bi-performance-troubleshooting.prompt.md`.

## Troubleshooting Methodology

### Step 1: **Problem Definition and Scope**

Begin by clearly defining the performance issue:

```
Issue Classification:
□ Model loading/refresh performance
□ Report page loading performance
□ Visual interaction responsiveness
□ Query execution speed
□ Capacity resource constraints
□ Data source connectivity issues

Scope Assessment:
□ Affects all users vs. specific users
□ Occurs at specific times vs. consistently
□ Impacts specific reports vs. all reports
□ Happens with certain data filters vs. all scenarios
```

### Step 2: **Performance Baseline Collection**

Gather current performance metrics:

```
Required Metrics:
- Page load times (target: <10 seconds)
- Visual interaction response (target: <3 seconds)
- Query execution times (target: <30 seconds)
- Model refresh duration (varies by model size)
- Memory and CPU utilization
- Concurrent user load
```

### Step 3: **Systematic Diagnosis**

Use this diagnostic framework:

#### A. **Model Performance Issues**

```
Data Model Analysis:
✓ Model size and complexity
✓ Relationship design and cardinality
✓ Storage mode configuration (Import/DirectQuery/Composite)
✓ Data types and compression efficiency
✓ Calculated columns vs. measures usage
✓ Date table implementation

Common Model Issues:
- Large model size due to unnecessary columns/rows
- Inefficient relationships (many-to-many, bidirectional)
- High-cardinality text columns
- Excessive calculated columns
- Missing or improper date tables
- Poor data type selections
```

#### B. **DAX Performance Issues**

```
DAX Formula Analysis:
✓ Complex calculations without variables
✓ Inefficient aggregation functions
✓ Context transition overhead
✓ Iterator function optimization
✓ Filter context complexity
✓ Error handling patterns

Performance Anti-Patterns:
- Repeated calculations (missing variables)
- FILTER() used as filter argument
- Complex calculated columns in large tables
- Nested CALCULATE functions
- Inefficient time intelligence patterns
```

#### C. **Report Design Issues**

```
Report Performance Analysis:
✓ Number of visuals per page (max 6-8 recommended)
✓ Visual types and complexity
✓ Cross-filtering configuration
✓ Slicer query efficiency
✓ Custom visual performance impact
✓ Mobile layout optimization

Common Report Issues:
- Too many visuals causing resource competition
- Inefficient cross-filtering patterns
- High-cardinality slicers
- Complex custom visuals
- Poorly optimized visual interactions
```

#### D. **Infrastructure and Capacity Issues**

```
Infrastructure Assessment:
✓ Capacity utilization (CPU, memory, query volume)
✓ Network connectivity and bandwidth
✓ Data source performance
✓ Gateway configuration and performance
✓ Concurrent user load patterns
✓ Geographic distribution considerations

Capacity Indicators:
- High CPU utilization (>70% sustained)
- Memory pressure warnings
- Query queuing and timeouts
- Gateway performance bottlenecks
- Network latency issues
```
