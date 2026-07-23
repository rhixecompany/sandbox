# Design Consultation Framework

> Extracted from `power-bi-report-design-consultation.prompt.md`.

## Design Consultation Framework

### **Initial Requirements Gathering**

Before recommending visualizations, understand the context:

```
Business Context Assessment:
□ What business problem are you trying to solve?
□ Who is the target audience (executives, analysts, operators)?
□ What decisions will this report support?
□ What are the key performance indicators?
□ How will the report be accessed (desktop, mobile, presentation)?

Data Context Analysis:
□ What data types are involved (categorical, numerical, temporal)?
□ What is the data volume and granularity?
□ Are there hierarchical relationships in the data?
□ What are the most important comparisons or trends?
□ Are there specific drill-down requirements?

Technical Requirements:
□ Performance constraints and expected load
□ Accessibility requirements
□ Brand guidelines and color restrictions
□ Mobile and responsive design needs
□ Integration with other systems or reports
```

### **Chart Selection Methodology**

#### **Data Relationship Analysis**

```
Comparison Analysis:
✅ Bar/Column Charts: Comparing categories, ranking items
✅ Horizontal Bars: Long category names, space constraints
✅ Bullet Charts: Performance against targets
✅ Dot Plots: Precise value comparison with minimal ink

Trend Analysis:
✅ Line Charts: Continuous time series, multiple metrics
✅ Area Charts: Cumulative values, composition over time
✅ Stepped Lines: Discrete changes, status transitions
✅ Sparklines: Inline trend indicators

Composition Analysis:
✅ Stacked Bars: Parts of whole with comparison
✅ Donut/Pie Charts: Simple composition (max 5-7 categories)
✅ Treemaps: Hierarchical composition, space-efficient
✅ Waterfall: Sequential changes, bridge analysis

Distribution Analysis:
✅ Histograms: Frequency distribution
✅ Box Plots: Statistical distribution summary
✅ Scatter Plots: Correlation, outlier identification
✅ Heat Maps: Two-dimensional patterns
```

#### **Audience-Specific Design Patterns**

```
Executive Dashboard Design:
- High-level KPIs prominently displayed
- Exception-based highlighting (red/yellow/green)
- Trend indicators with clear direction arrows
- Minimal text, maximum insight density
- Clean, uncluttered design with plenty of white space

Analytical Report Design:
- Multiple levels of detail with drill-down capability
- Comparative analysis tools (period-over-period)
- Interactive filtering and exploration options
- Detailed data tables when needed
- Comprehensive legends and context information

Operational Report Design:
- Real-time or near real-time data display
- Action-oriented design with clear status indicators
- Exception-based alerts and notifications
- Mobile-optimized for field use
- Quick refresh and update capabilities
```
