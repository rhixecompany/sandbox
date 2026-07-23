# Detailed Review Process

> Extracted from `power-bi-model-design-review.prompt.md`.

## Detailed Review Process

### **Phase 1: Model Architecture Analysis**

#### A. **Schema Design Assessment**

```
Evaluate Model Structure:

Fact Table Analysis:
- Grain definition and consistency
- Appropriate measure columns
- Foreign key completeness
- Size and growth projections
- Historical data management

Dimension Table Analysis:
- Attribute completeness and quality
- Hierarchy design and implementation
- Slowly changing dimension handling
- Surrogate vs. natural key usage
- Reference data management

Relationship Network Analysis:
- Star vs. snowflake patterns
- Relationship complexity assessment
- Filter propagation paths
- Cross-filtering impact evaluation
```

#### B. **Data Quality and Integrity Review**

```
Data Quality Assessment:

Completeness:
□ All required business entities represented
□ No missing critical relationships
□ Comprehensive attribute coverage
□ Proper handling of NULL values

Consistency:
□ Consistent data types across related columns
□ Standardized naming conventions
□ Uniform formatting and encoding
□ Consistent grain across fact tables

Accuracy:
□ Business rule implementation validation
□ Referential integrity verification
□ Data transformation accuracy
□ Calculated field correctness
```

### **Phase 2: Performance and Scalability Review**

#### A. **Model Size and Efficiency Analysis**

```
Size Optimization Assessment:

Data Reduction Opportunities:
- Unnecessary columns identification
- Redundant data elimination
- Historical data archiving needs
- Pre-aggregation possibilities

Compression Efficiency:
- Data type optimization opportunities
- High-cardinality column assessment
- Calculated column vs. measure usage
- Storage mode selection validation

Scalability Considerations:
- Growth projection accommodation
- Refresh performance requirements
- Query performance expectations
- Concurrent user capacity planning
```

#### B. **Query Performance Analysis**

```
Performance Pattern Review:

DAX Optimization:
- Measure efficiency and complexity
- Variable usage in calculations
- Context transition optimization
- Iterator function performance
- Error handling implementation

Relationship Performance:
- Join efficiency assessment
- Cross-filtering impact analysis
- Many-to-many performance implications
- Bidirectional relationship necessity

Indexing and Aggregation:
- DirectQuery indexing requirements
- Aggregation table opportunities
- Composite model optimization
- Cache utilization strategies
```

### **Phase 3: Maintainability and Governance Review**

#### A. **Model Maintainability Assessment**

```
Maintainability Factors:

Documentation Quality:
□ Table and column descriptions
□ Business rule documentation
□ Data source documentation
□ Relationship justification
□ Measure calculation explanations

Code Organization:
□ Logical grouping of related measures
□ Consistent naming conventions
□ Modular design principles
□ Clear separation of concerns
□ Version control considerations

Change Management:
□ Impact assessment procedures
□ Testing and validation processes
□ Deployment and rollback strategies
□ User communication plans
```

#### B. **Security and Compliance Review**

```
Security Implementation:

Row-Level Security:
□ RLS design and implementation
□ Performance impact assessment
□ Testing and validation completeness
□ Role-based access control
□ Dynamic security patterns

Data Protection:
□ Sensitive data handling
□ Compliance requirements adherence
□ Audit trail implementation
□ Data retention policies
□ Privacy protection measures
```
