# Diagnostic Tools and Techniques

> Extracted from `power-bi-performance-troubleshooting.prompt.md`.

## Diagnostic Tools and Techniques

### **Power BI Desktop Tools**

```
Performance Analyzer:
- Enable and record visual refresh times
- Identify slowest visuals and operations
- Compare DAX query vs. visual rendering time
- Export results for detailed analysis

Usage:
1. Open Performance Analyzer pane
2. Start recording
3. Refresh visuals or interact with report
4. Analyze results by duration
5. Focus on highest duration items first
```

### **DAX Studio Analysis**

```
Advanced DAX Analysis:
- Query execution plans
- Storage engine vs. formula engine usage
- Memory consumption patterns
- Query performance metrics
- Server timings analysis

Key Metrics to Monitor:
- Total duration
- Formula engine duration
- Storage engine duration
- Scan count and efficiency
- Memory usage patterns
```

### **Capacity Monitoring**

```
Fabric Capacity Metrics App:
- CPU and memory utilization trends
- Query volume and patterns
- Refresh performance tracking
- User activity analysis
- Resource bottleneck identification

Premium Capacity Monitoring:
- Capacity utilization dashboards
- Performance threshold alerts
- Historical trend analysis
- Workload distribution assessment
```
