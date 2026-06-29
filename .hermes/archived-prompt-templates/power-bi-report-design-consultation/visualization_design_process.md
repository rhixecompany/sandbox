# Visualization Design Process

> Extracted from `power-bi-report-design-consultation.prompt.md`.

## Visualization Design Process

### **Phase 1: Information Architecture**

```
Content Prioritization:
1. Critical Metrics: Most important KPIs and measures
2. Supporting Context: Trends, comparisons, breakdowns
3. Detailed Analysis: Drill-down data and specifics
4. Navigation & Filters: User control elements

Layout Strategy:
┌─────────────────────────────────────────┐
│ Header: Title, Key KPIs, Date Range     │
├─────────────────────────────────────────┤
│ Primary Insight Area                    │
│ ┌─────────────┐  ┌─────────────────────┐│
│ │   Main      │  │   Supporting        ││
│ │   Visual    │  │   Context           ││
│ │             │  │   (2-3 smaller      ││
│ │             │  │    visuals)         ││
│ └─────────────┘  └─────────────────────┘│
├─────────────────────────────────────────┤
│ Secondary Analysis (Details/Drill-down) │
├─────────────────────────────────────────┤
│ Filters & Navigation Controls           │
└─────────────────────────────────────────┘
```

### **Phase 2: Visual Design Specifications**

#### **Color Strategy Design**

```
Semantic Color Mapping:
- Green (#2E8B57): Positive performance, on-target, growth
- Red (#DC143C): Negative performance, alerts, below-target
- Blue (#4682B4): Neutral information, base metrics
- Orange (#FF8C00): Warnings, attention needed
- Gray (#708090): Inactive, reference, disabled states

Accessibility Compliance:
✅ Minimum 4.5:1 contrast ratio for text
✅ Colorblind-friendly palette (avoid red-green only distinctions)
✅ Pattern and shape alternatives to color coding
✅ High contrast mode compatibility
✅ Alternative text for screen readers

Brand Integration Guidelines:
- Primary brand color for key metrics and headers
- Secondary palette for data categorization
- Neutral grays for backgrounds and borders
- Accent colors for highlights and interactions
```

#### **Typography Hierarchy**

```
Text Size and Weight Guidelines:
- Report Title: 20-24pt, Bold, Brand Font
- Page Titles: 16-18pt, Semi-bold, Sans-serif
- Section Headers: 14-16pt, Semi-bold
- Visual Titles: 12-14pt, Medium weight
- Data Labels: 10-12pt, Regular
- Footnotes/Captions: 9-10pt, Light

Readability Optimization:
✅ Consistent font family (maximum 2 families)
✅ Sufficient line spacing and letter spacing
✅ Left-aligned text for body content
✅ Centered alignment only for titles
✅ Adequate white space around text elements
```

### **Phase 3: Interactive Design**

#### **Navigation Design Patterns**

```
Tab Navigation:
Best for: Related content areas, different time periods
Implementation:
- Clear tab labels (max 7 tabs)
- Visual indication of active tab
- Consistent content layout across tabs
- Logical ordering by importance or workflow

Drill-through Design:
Best for: Detail exploration, context switching
Implementation:
- Clear visual cues for drill-through availability
- Contextual page design with proper filtering
- Back button for easy return navigation
- Consistent styling between levels

Button Navigation:
Best for: Guided workflows, external links
Implementation:
- Action-oriented button labels
- Consistent styling and sizing
- Appropriate visual hierarchy
- Touch-friendly sizing (minimum 44px)
```

#### **Filter and Slicer Design**

```
Slicer Optimization:
✅ Logical grouping and positioning
✅ Search functionality for high-cardinality fields
✅ Single vs. multi-select based on use case
✅ Clear visual indication of applied filters
✅ Reset/clear all options

Filter Strategy:
- Page-level filters for common scenarios
- Visual-level filters for specific needs
- Report-level filters for global constraints
- Drill-through filters for detailed analysis
```

### **Phase 4: Mobile and Responsive Design**

#### **Mobile Layout Strategy**

```
Mobile-First Considerations:
- Portrait orientation as primary design
- Touch-friendly interaction targets (44px minimum)
- Simplified navigation with hamburger menus
- Stacked layout instead of side-by-side
- Larger fonts and increased spacing

Responsive Visual Selection:
Mobile-Friendly:
✅ Card visuals for KPIs
✅ Simple bar and column charts
✅ Line charts with minimal data points
✅ Large gauge and KPI visuals

Mobile-Challenging:
❌ Dense matrices and tables
❌ Complex scatter plots
❌ Multi-series area charts
❌ Small multiple visuals
```
