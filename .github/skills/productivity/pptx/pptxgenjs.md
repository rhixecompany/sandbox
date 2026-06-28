---
name: pptx-pptxgenjs
description: "PptxGenJS Tutorial"
version: 1.0.0
author: Alexa
---
     1|# PptxGenJS Tutorial
     2|
     3|## Setup & Basic Structure
     4|
     5|```javascript
     6|const pptxgen = require("pptxgenjs");
     7|
     8|let pres = new pptxgen();
     9|pres.layout = "LAYOUT_16x9"; // or 'LAYOUT_16x10', 'LAYOUT_4x3', 'LAYOUT_WIDE'
    10|pres.author = "Your Name";
    11|pres.title = "Presentation Title";
    12|
    13|let slide = pres.addSlide();
    14|slide.addText("Hello World!", {
    15|  x: 0.5,
    16|  y: 0.5,
    17|  fontSize: 36,
    18|  color: "363636"
    19|});
    20|
    21|pres.writeFile({ fileName: "Presentation.pptx" });
    22|```
    23|
    24|## Layout Dimensions
    25|
    26|Slide dimensions (coordinates in inches):
    27|
    28|- `LAYOUT_16x9`: 10" × 5.625" (default)
    29|- `LAYOUT_16x10`: 10" × 6.25"
    30|- `LAYOUT_4x3`: 10" × 7.5"
    31|- `LAYOUT_WIDE`: 13.3" × 7.5"
    32|
    33|---
    34|
    35|## Text & Formatting
    36|
    37|```javascript
    38|// Basic text
    39|slide.addText("Simple Text", {
    40|  x: 1,
    41|  y: 1,
    42|  w: 8,
    43|  h: 2,
    44|  fontSize: 24,
    45|  fontFace: "Arial",
    46|  color: "363636",
    47|  bold: true,
    48|  align: "center",
    49|  valign: "middle"
    50|});
    51|
    52|// Character spacing (use charSpacing, not letterSpacing which is silently ignored)
    53|slide.addText("SPACED TEXT", {
    54|  x: 1,
    55|  y: 1,
    56|  w: 8,
    57|  h: 1,
    58|  charSpacing: 6
    59|});
    60|
    61|// Rich text arrays
    62|slide.addText(
    63|  [
    64|    { text: "Bold ", options: { bold: true } },
    65|    { text: "Italic ", options: { italic: true } }
    66|  ],
    67|  { x: 1, y: 3, w: 8, h: 1 }
    68|);
    69|
    70|// Multi-line text (requires breakLine: true)
    71|slide.addText(
    72|  [
    73|    { text: "Line 1", options: { breakLine: true } },
    74|    { text: "Line 2", options: { breakLine: true } },
    75|    { text: "Line 3" } // Last item doesn't need breakLine
    76|  ],
    77|  { x: 0.5, y: 0.5, w: 8, h: 2 }
    78|);
    79|
    80|// Text box margin (internal padding)
    81|slide.addText("Title", {
    82|  x: 0.5,
    83|  y: 0.3,
    84|  w: 9,
    85|  h: 0.6,
    86|  margin: 0 // Use 0 when aligning text with other elements like shapes or icons
    87|});
    88|```
    89|
    90|**Tip:** Text boxes have internal margin by default. Set `margin: 0` when you need text to align precisely with shapes, lines, or icons at the same x-position.
    91|
    92|---
    93|
    94|## Lists & Bullets
    95|
    96|```javascript
    97|// ✅ CORRECT: Multiple bullets
    98|slide.addText([
    99|  { text: "First item", options: { bullet: true, breakLine: true } },
   100|  { text: "Second item", options: { bullet: true, breakLine: true } },
   101|  { text: "Third item", options: { bullet: true } }
   102|], { x: 0.5, y: 0.5, w: 8, h: 3 });
   103|
   104|// ❌ WRONG: Never use unicode bullets
   105|slide.addText("• First item", { ... });  // Creates double bullets
   106|
   107|// Sub-items and numbered lists
   108|{ text: "Sub-item", options: { bullet: true, indentLevel: 1 } }
   109|{ text: "First", options: { bullet: { type: "number" }, breakLine: true } }
   110|```
   111|
   112|---
   113|
   114|## Shapes
   115|
   116|```javascript
   117|slide.addShape(pres.shapes.RECTANGLE, {
   118|  x: 0.5,
   119|  y: 0.8,
   120|  w: 1.5,
   121|  h: 3.0,
   122|  fill: { color: "FF0000" },
   123|  line: { color: "000000", width: 2 }
   124|});
   125|
   126|slide.addShape(pres.shapes.OVAL, {
   127|  x: 4,
   128|  y: 1,
   129|  w: 2,
   130|  h: 2,
   131|  fill: { color: "0000FF" }
   132|});
   133|
   134|slide.addShape(pres.shapes.LINE, {
   135|  x: 1,
   136|  y: 3,
   137|  w: 5,
   138|  h: 0,
   139|  line: { color: "FF0000", width: 3, dashType: "dash" }
   140|});
   141|
   142|// With transparency
   143|slide.addShape(pres.shapes.RECTANGLE, {
   144|  x: 1,
   145|  y: 1,
   146|  w: 3,
   147|  h: 2,
   148|  fill: { color: "0088CC", transparency: 50 }
   149|});
   150|
   151|// Rounded rectangle (rectRadius only works with ROUNDED_RECTANGLE, not RECTANGLE)
   152|// ⚠️ Don't pair with rectangular accent overlays — they won't cover rounded corners. Use RECTANGLE instead.
   153|slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
   154|  x: 1,
   155|  y: 1,
   156|  w: 3,
   157|  h: 2,
   158|  fill: { color: "FFFFFF" },
   159|  rectRadius: 0.1
   160|});
   161|
   162|// With shadow
   163|slide.addShape(pres.shapes.RECTANGLE, {
   164|  x: 1,
   165|  y: 1,
   166|  w: 3,
   167|  h: 2,
   168|  fill: { color: "FFFFFF" },
   169|  shadow: {
   170|    type: "outer",
   171|    color: "000000",
   172|    blur: 6,
   173|    offset: 2,
   174|    angle: 135,
   175|    opacity: 0.15
   176|  }
   177|});
   178|```
   179|
   180|Shadow options:
   181|
   182|| Property | Type | Range | Notes |
   183|| --- | --- | --- | --- |
   184|| `type` | string | `"outer"`, `"inner"` |  |
   185|| `color` | string | 6-char hex (e.g. `"000000"`) | No `#` prefix, no 8-char hex — see Common Pitfalls |
   186|| `blur` | number | 0-100 pt |  |
   187|| `offset` | number | 0-200 pt | **Must be non-negative** — negative values corrupt the file |
   188|| `angle` | number | 0-359 degrees | Direction the shadow falls (135 = bottom-right, 270 = upward) |
   189|| `opacity` | number | 0.0-1.0 | Use this for transparency, never encode in color string |
   190|
   191|To cast a shadow upward (e.g. on a footer bar), use `angle: 270` with a positive offset — do **not** use a negative offset.
   192|
   193|**Note**: Gradient fills are not natively supported. Use a gradient image as a background instead.
   194|
   195|---
   196|
   197|## Images
   198|
   199|### Image Sources
   200|
   201|```javascript
   202|// From file path
   203|slide.addImage({ path: "images/chart.png", x: 1, y: 1, w: 5, h: 3 });
   204|
   205|// From URL
   206|slide.addImage({
   207|  path: "https://example.com/image.jpg",
   208|  x: 1,
   209|  y: 1,
   210|  w: 5,
   211|  h: 3
   212|});
   213|
   214|// From base64 (faster, no file I/O)
   215|slide.addImage({
   216|  data: "image/png;base64,iVBORw0KGgo...",
   217|  x: 1,
   218|  y: 1,
   219|  w: 5,
   220|  h: 3
   221|});
   222|```
   223|
   224|### Image Options
   225|
   226|```javascript
   227|slide.addImage({
   228|  path: "image.png",
   229|  x: 1,
   230|  y: 1,
   231|  w: 5,
   232|  h: 3,
   233|  rotate: 45, // 0-359 degrees
   234|  rounding: true, // Circular crop
   235|  transparency: 50, // 0-100
   236|  flipH: true, // Horizontal flip
   237|  flipV: false, // Vertical flip
   238|  altText: "Description", // Accessibility
   239|  hyperlink: { url: "https://example.com" }
   240|});
   241|```
   242|
   243|### Image Sizing Modes
   244|
   245|```javascript
   246|// Contain - fit inside, preserve ratio
   247|{ sizing: { type: 'contain', w: 4, h: 3 } }
   248|
   249|// Cover - fill area, preserve ratio (may crop)
   250|{ sizing: { type: 'cover', w: 4, h: 3 } }
   251|
   252|// Crop - cut specific portion
   253|{ sizing: { type: 'crop', x: 0.5, y: 0.5, w: 2, h: 2 } }
   254|```
   255|
   256|### Calculate Dimensions (preserve aspect ratio)
   257|
   258|```javascript
   259|const origWidth = 1978,
   260|  origHeight = 923,
   261|  maxHeight = 3.0;
   262|const calcWidth = maxHeight * (origWidth / origHeight);
   263|const centerX = (10 - calcWidth) / 2;
   264|
   265|slide.addImage({
   266|  path: "image.png",
   267|  x: centerX,
   268|  y: 1.2,
   269|  w: calcWidth,
   270|  h: maxHeight
   271|});
   272|```
   273|
   274|### Supported Formats
   275|
   276|- **Standard**: PNG, JPG, GIF (animated GIFs work in Microsoft 365)
   277|- **SVG**: Works in modern PowerPoint/Microsoft 365
   278|
   279|---
   280|
   281|## Icons
   282|
   283|Use react-icons to generate SVG icons, then rasterize to PNG for universal compatibility.
   284|
   285|### Setup
   286|
   287|```javascript
   288|const React = require("react");
   289|const ReactDOMServer = require("react-dom/server");
   290|const sharp = require("sharp");
   291|const { FaCheckCircle, FaChartLine } = require("react-icons/fa");
   292|
   293|function renderIconSvg(IconComponent, color = "#000000", size = 256) {
   294|  return ReactDOMServer.renderToStaticMarkup(
   295|    React.createElement(IconComponent, { color, size: String(size) })
   296|  );
   297|}
   298|
   299|async function iconToBase64Png(IconComponent, color, size = 256) {
   300|  const svg = renderIconSvg(IconComponent, color, size);
   301|  const pngBuffer = await sharp(Buffer.from(svg)).png().toBuffer();
   302|  return "image/png;base64," + pngBuffer.toString("base64");
   303|}
   304|```
   305|
   306|### Add Icon to Slide
   307|
   308|```javascript
   309|const iconData = await iconToBase64Png(FaCheckCircle, "#4472C4", 256);
   310|
   311|slide.addImage({
   312|  data: iconData,
   313|  x: 1,
   314|  y: 1,
   315|  w: 0.5,
   316|  h: 0.5 // Size in inches
   317|});
   318|```
   319|
   320|**Note**: Use size 256 or higher for crisp icons. The size parameter controls the rasterization resolution, not the display size on the slide (which is set by `w` and `h` in inches).
   321|
   322|### Icon Libraries
   323|
   324|Install: `npm install -g react-icons react react-dom sharp`
   325|
   326|Popular icon sets in react-icons:
   327|
   328|- `react-icons/fa` - Font Awesome
   329|- `react-icons/md` - Material Design
   330|- `react-icons/hi` - Heroicons
   331|- `react-icons/bi` - Bootstrap Icons
   332|
   333|---
   334|
   335|## Slide Backgrounds
   336|
   337|```javascript
   338|// Solid color
   339|slide.background = { color: "F1F1F1" };
   340|
   341|// Color with transparency
   342|slide.background = { color: "FF3399", transparency: 50 };
   343|
   344|// Image from URL
   345|slide.background = { path: "https://example.com/bg.jpg" };
   346|
   347|// Image from base64
   348|slide.background = { data: "image/png;base64,iVBORw0KGgo..." };
   349|```
   350|
   351|---
   352|
   353|## Tables
   354|
   355|```javascript
   356|slide.addTable(
   357|  [
   358|    ["Header 1", "Header 2"],
   359|    ["Cell 1", "Cell 2"]
   360|  ],
   361|  {
   362|    x: 1,
   363|    y: 1,
   364|    w: 8,
   365|    h: 2,
   366|    border: { pt: 1, color: "999999" },
   367|    fill: { color: "F1F1F1" }
   368|  }
   369|);
   370|
   371|// Advanced with merged cells
   372|let tableData = [
   373|  [
   374|    {
   375|      text: "Header",
   376|      options: {
   377|        fill: { color: "6699CC" },
   378|        color: "FFFFFF",
   379|        bold: true
   380|      }
   381|    },
   382|    "Cell"
   383|  ],
   384|  [{ text: "Merged", options: { colspan: 2 } }]
   385|];
   386|slide.addTable(tableData, { x: 1, y: 3.5, w: 8, colW: [4, 4] });
   387|```
   388|
   389|---
   390|
   391|## Charts
   392|
   393|```javascript
   394|// Bar chart
   395|slide.addChart(
   396|  pres.charts.BAR,
   397|  [
   398|    {
   399|      name: "Sales",
   400|      labels: ["Q1", "Q2", "Q3", "Q4"],
   401|      values: [4500, 5500, 6200, 7100]
   402|    }
   403|  ],
   404|  {
   405|    x: 0.5,
   406|    y: 0.6,
   407|    w: 6,
   408|    h: 3,
   409|    barDir: "col",
   410|    showTitle: true,
   411|    title: "Quarterly Sales"
   412|  }
   413|);
   414|
   415|// Line chart
   416|slide.addChart(
   417|  pres.charts.LINE,
   418|  [
   419|    {
   420|      name: "Temp",
   421|      labels: ["Jan", "Feb", "Mar"],
   422|      values: [32, 35, 42]
   423|    }
   424|  ],
   425|  { x: 0.5, y: 4, w: 6, h: 3, lineSize: 3, lineSmooth: true }
   426|);
   427|
   428|// Pie chart
   429|slide.addChart(
   430|  pres.charts.PIE,
   431|  [
   432|    {
   433|      name: "Share",
   434|      labels: ["A", "B", "Other"],
   435|      values: [35, 45, 20]
   436|    }
   437|  ],
   438|  { x: 7, y: 1, w: 5, h: 4, showPercent: true }
   439|);
   440|```
   441|
   442|### Better-Looking Charts
   443|
   444|Default charts look dated. Apply these options for a modern, clean appearance:
   445|
   446|```javascript
   447|slide.addChart(pres.charts.BAR, chartData, {
   448|  x: 0.5,
   449|  y: 1,
   450|  w: 9,
   451|  h: 4,
   452|  barDir: "col",
   453|
   454|  // Custom colors (match your presentation palette)
   455|  chartColors: ["0D9488", "14B8A6", "5EEAD4"],
   456|
   457|  // Clean background
   458|  chartArea: { fill: { color: "FFFFFF" }, roundedCorners: true },
   459|
   460|  // Muted axis labels
   461|  catAxisLabelColor: "64748B",
   462|  valAxisLabelColor: "64748B",
   463|
   464|  // Subtle grid (value axis only)
   465|  valGridLine: { color: "E2E8F0", size: 0.5 },
   466|  catGridLine: { style: "none" },
   467|
   468|  // Data labels on bars
   469|  showValue: true,
   470|  dataLabelPosition: "outEnd",
   471|  dataLabelColor: "1E293B",
   472|
   473|  // Hide legend for single series
   474|  showLegend: false
   475|});
   476|```
   477|
   478|**Key styling options:**
   479|
   480|- `chartColors: [...]` - hex colors for series/segments
   481|- `chartArea: { fill, border, roundedCorners }` - chart background
   482|- `catGridLine/valGridLine: { color, style, size }` - grid lines (`style: "none"` to hide)
   483|- `lineSmooth: true` - curved lines (line charts)
   484|- `legendPos: "r"` - legend position: "b", "t", "l", "r", "tr"
   485|
   486|---
   487|
   488|## Slide Masters
   489|
   490|```javascript
   491|pres.defineSlideMaster({
   492|  title: "TITLE_SLIDE",
   493|  background: { color: "283A5E" },
   494|  objects: [
   495|    {
   496|      placeholder: {
   497|        options: {
   498|          name: "title",
   499|          type: "title",
   500|          x: 1,
   501|