---
name: pdf-reference
description: "PDF Processing Advanced Reference"
version: 1.0.0
author: Alexa
---
     1|# PDF Processing Advanced Reference
     2|
     3|This document contains advanced PDF processing features, detailed examples, and additional libraries not covered in the main skill instructions.
     4|
     5|## pypdfium2 Library (Apache/BSD License)
     6|
     7|### Overview
     8|
     9|pypdfium2 is a Python binding for PDFium (Chromium's PDF library). It's excellent for fast PDF rendering, image generation, and serves as a PyMuPDF replacement.
    10|
    11|### Render PDF to Images
    12|
    13|```python
    14|import pypdfium2 as pdfium
    15|from PIL import Image
    16|
    17|# Load PDF
    18|pdf = pdfium.PdfDocument("document.pdf")
    19|
    20|# Render page to image
    21|page = pdf[0]  # First page
    22|bitmap = page.render(
    23|    scale=2.0,  # Higher resolution
    24|    rotation=0  # No rotation
    25|)
    26|
    27|# Convert to PIL Image
    28|img = bitmap.to_pil()
    29|img.save("page_1.png", "PNG")
    30|
    31|# Process multiple pages
    32|for i, page in enumerate(pdf):
    33|    bitmap = page.render(scale=1.5)
    34|    img = bitmap.to_pil()
    35|    img.save(f"page_{i+1}.jpg", "JPEG", quality=90)
    36|```
    37|
    38|### Extract Text with pypdfium2
    39|
    40|```python
    41|import pypdfium2 as pdfium
    42|
    43|pdf = pdfium.PdfDocument("document.pdf")
    44|for i, page in enumerate(pdf):
    45|    text = page.get_text()
    46|    print(f"Page {i+1} text length: {len(text)} chars")
    47|```
    48|
    49|## JavaScript Libraries
    50|
    51|### pdf-lib (MIT License)
    52|
    53|pdf-lib is a powerful JavaScript library for creating and modifying PDF documents in any JavaScript environment.
    54|
    55|#### Load and Manipulate Existing PDF
    56|
    57|```javascript
    58|import { PDFDocument } from "pdf-lib";
    59|import fs from "fs";
    60|
    61|async function manipulatePDF() {
    62|  // Load existing PDF
    63|  const existingPdfBytes = fs.readFileSync("input.pdf");
    64|  const pdfDoc = await PDFDocument.load(existingPdfBytes);
    65|
    66|  // Get page count
    67|  const pageCount = pdfDoc.getPageCount();
    68|  console.log(`Document has ${pageCount} pages`);
    69|
    70|  // Add new page
    71|  const newPage = pdfDoc.addPage([600, 400]);
    72|  newPage.drawText("Added by pdf-lib", {
    73|    x: 100,
    74|    y: 300,
    75|    size: 16
    76|  });
    77|
    78|  // Save modified PDF
    79|  const pdfBytes = await pdfDoc.save();
    80|  fs.writeFileSync("modified.pdf", pdfBytes);
    81|}
    82|```
    83|
    84|#### Create Complex PDFs from Scratch
    85|
    86|```javascript
    87|import { PDFDocument, rgb, StandardFonts } from "pdf-lib";
    88|import fs from "fs";
    89|
    90|async function createPDF() {
    91|  const pdfDoc = await PDFDocument.create();
    92|
    93|  // Add fonts
    94|  const helveticaFont = await pdfDoc.embedFont(
    95|    StandardFonts.Helvetica
    96|  );
    97|  const helveticaBold = await pdfDoc.embedFont(
    98|    StandardFonts.HelveticaBold
    99|  );
   100|
   101|  // Add page
   102|  const page = pdfDoc.addPage([595, 842]); // A4 size
   103|  const { width, height } = page.getSize();
   104|
   105|  // Add text with styling
   106|  page.drawText("Invoice #12345", {
   107|    x: 50,
   108|    y: height - 50,
   109|    size: 18,
   110|    font: helveticaBold,
   111|    color: rgb(0.2, 0.2, 0.8)
   112|  });
   113|
   114|  // Add rectangle (header background)
   115|  page.drawRectangle({
   116|    x: 40,
   117|    y: height - 100,
   118|    width: width - 80,
   119|    height: 30,
   120|    color: rgb(0.9, 0.9, 0.9)
   121|  });
   122|
   123|  // Add table-like content
   124|  const items = [
   125|    ["Item", "Qty", "Price", "Total"],
   126|    ["Widget", "2", "$50", "$100"],
   127|    ["Gadget", "1", "$75", "$75"]
   128|  ];
   129|
   130|  let yPos = height - 150;
   131|  items.forEach(row => {
   132|    let xPos = 50;
   133|    row.forEach(cell => {
   134|      page.drawText(cell, {
   135|        x: xPos,
   136|        y: yPos,
   137|        size: 12,
   138|        font: helveticaFont
   139|      });
   140|      xPos += 120;
   141|    });
   142|    yPos -= 25;
   143|  });
   144|
   145|  const pdfBytes = await pdfDoc.save();
   146|  fs.writeFileSync("created.pdf", pdfBytes);
   147|}
   148|```
   149|
   150|#### Advanced Merge and Split Operations
   151|
   152|```javascript
   153|import { PDFDocument } from "pdf-lib";
   154|import fs from "fs";
   155|
   156|async function mergePDFs() {
   157|  // Create new document
   158|  const mergedPdf = await PDFDocument.create();
   159|
   160|  // Load source PDFs
   161|  const pdf1Bytes = fs.readFileSync("doc1.pdf");
   162|  const pdf2Bytes = fs.readFileSync("doc2.pdf");
   163|
   164|  const pdf1 = await PDFDocument.load(pdf1Bytes);
   165|  const pdf2 = await PDFDocument.load(pdf2Bytes);
   166|
   167|  // Copy pages from first PDF
   168|  const pdf1Pages = await mergedPdf.copyPages(
   169|    pdf1,
   170|    pdf1.getPageIndices()
   171|  );
   172|  pdf1Pages.forEach(page => mergedPdf.addPage(page));
   173|
   174|  // Copy specific pages from second PDF (pages 0, 2, 4)
   175|  const pdf2Pages = await mergedPdf.copyPages(pdf2, [0, 2, 4]);
   176|  pdf2Pages.forEach(page => mergedPdf.addPage(page));
   177|
   178|  const mergedPdfBytes = await mergedPdf.save();
   179|  fs.writeFileSync("merged.pdf", mergedPdfBytes);
   180|}
   181|```
   182|
   183|### pdfjs-dist (Apache License)
   184|
   185|PDF.js is Mozilla's JavaScript library for rendering PDFs in the browser.
   186|
   187|#### Basic PDF Loading and Rendering
   188|
   189|```javascript
   190|import * as pdfjsLib from "pdfjs-dist";
   191|
   192|// Configure worker (important for performance)
   193|pdfjsLib.GlobalWorkerOptions.workerSrc = "./pdf.worker.js";
   194|
   195|async function renderPDF() {
   196|  // Load PDF
   197|  const loadingTask = pdfjsLib.getDocument("document.pdf");
   198|  const pdf = await loadingTask.promise;
   199|
   200|  console.log(`Loaded PDF with ${pdf.numPages} pages`);
   201|
   202|  // Get first page
   203|  const page = await pdf.getPage(1);
   204|  const viewport = page.getViewport({ scale: 1.5 });
   205|
   206|  // Render to canvas
   207|  const canvas = document.createElement("canvas");
   208|  const context = canvas.getContext("2d");
   209|  canvas.height = viewport.height;
   210|  canvas.width = viewport.width;
   211|
   212|  const renderContext = {
   213|    canvasContext: context,
   214|    viewport: viewport
   215|  };
   216|
   217|  await page.render(renderContext).promise;
   218|  document.body.appendChild(canvas);
   219|}
   220|```
   221|
   222|#### Extract Text with Coordinates
   223|
   224|```javascript
   225|import * as pdfjsLib from "pdfjs-dist";
   226|
   227|async function extractText() {
   228|  const loadingTask = pdfjsLib.getDocument("document.pdf");
   229|  const pdf = await loadingTask.promise;
   230|
   231|  let fullText = "";
   232|
   233|  // Extract text from all pages
   234|  for (let i = 1; i <= pdf.numPages; i++) {
   235|    const page = await pdf.getPage(i);
   236|    const textContent = await page.getTextContent();
   237|
   238|    const pageText = textContent.items
   239|      .map(item => item.str)
   240|      .join(" ");
   241|
   242|    fullText += `\n--- Page ${i} ---\n${pageText}`;
   243|
   244|    // Get text with coordinates for advanced processing
   245|    const textWithCoords = textContent.items.map(item => ({
   246|      text: item.str,
   247|      x: item.transform[4],
   248|      y: item.transform[5],
   249|      width: item.width,
   250|      height: item.height
   251|    }));
   252|  }
   253|
   254|  console.log(fullText);
   255|  return fullText;
   256|}
   257|```
   258|
   259|#### Extract Annotations and Forms
   260|
   261|```javascript
   262|import * as pdfjsLib from "pdfjs-dist";
   263|
   264|async function extractAnnotations() {
   265|  const loadingTask = pdfjsLib.getDocument("annotated.pdf");
   266|  const pdf = await loadingTask.promise;
   267|
   268|  for (let i = 1; i <= pdf.numPages; i++) {
   269|    const page = await pdf.getPage(i);
   270|    const annotations = await page.getAnnotations();
   271|
   272|    annotations.forEach(annotation => {
   273|      console.log(`Annotation type: ${annotation.subtype}`);
   274|      console.log(`Content: ${annotation.contents}`);
   275|      console.log(`Coordinates: ${JSON.stringify(annotation.rect)}`);
   276|    });
   277|  }
   278|}
   279|```
   280|
   281|## Advanced Command-Line Operations
   282|
   283|### poppler-utils Advanced Features
   284|
   285|#### Extract Text with Bounding Box Coordinates
   286|
   287|```bash
   288|# Extract text with bounding box coordinates (essential for structured data)
   289|pdftotext -bbox-layout document.pdf output.xml
   290|
   291|# The XML output contains precise coordinates for each text element
   292|```
   293|
   294|#### Advanced Image Conversion
   295|
   296|```bash
   297|# Convert to PNG images with specific resolution
   298|pdftoppm -png -r 300 document.pdf output_prefix
   299|
   300|# Convert specific page range with high resolution
   301|pdftoppm -png -r 600 -f 1 -l 3 document.pdf high_res_pages
   302|
   303|# Convert to JPEG with quality setting
   304|pdftoppm -jpeg -jpegopt quality=85 -r 200 document.pdf jpeg_output
   305|```
   306|
   307|#### Extract Embedded Images
   308|
   309|```bash
   310|# Extract all embedded images with metadata
   311|pdfimages -j -p document.pdf page_images
   312|
   313|# List image info without extracting
   314|pdfimages -list document.pdf
   315|
   316|# Extract images in their original format
   317|pdfimages -all document.pdf images/img
   318|```
   319|
   320|### qpdf Advanced Features
   321|
   322|#### Complex Page Manipulation
   323|
   324|```bash
   325|# Split PDF into groups of pages
   326|qpdf --split-pages=3 input.pdf output_group_%02d.pdf
   327|
   328|# Extract specific pages with complex ranges
   329|qpdf input.pdf --pages input.pdf 1,3-5,8,10-end -- extracted.pdf
   330|
   331|# Merge specific pages from multiple PDFs
   332|qpdf --empty --pages doc1.pdf 1-3 doc2.pdf 5-7 doc3.pdf 2,4 -- combined.pdf
   333|```
   334|
   335|#### PDF Optimization and Repair
   336|
   337|```bash
   338|# Optimize PDF for web (linearize for streaming)
   339|qpdf --linearize input.pdf optimized.pdf
   340|
   341|# Remove unused objects and compress
   342|qpdf --optimize-level=all input.pdf compressed.pdf
   343|
   344|# Attempt to repair corrupted PDF structure
   345|qpdf --check input.pdf
   346|qpdf --fix-qdf damaged.pdf repaired.pdf
   347|
   348|# Show detailed PDF structure for debugging
   349|qpdf --show-all-pages input.pdf > structure.txt
   350|```
   351|
   352|#### Advanced Encryption
   353|
   354|```bash
   355|# Add password protection with specific permissions
   356|qpdf --encrypt user_pass owner_pass 256 --print=none --modify=none -- input.pdf encrypted.pdf
   357|
   358|# Check encryption status
   359|qpdf --show-encryption encrypted.pdf
   360|
   361|# Remove password protection (requires password)
   362|qpdf --password=secret123 --decrypt encrypted.pdf decrypted.pdf
   363|```
   364|
   365|## Advanced Python Techniques
   366|
   367|### pdfplumber Advanced Features
   368|
   369|#### Extract Text with Precise Coordinates
   370|
   371|```python
   372|import pdfplumber
   373|
   374|with pdfplumber.open("document.pdf") as pdf:
   375|    page = pdf.pages[0]
   376|
   377|    # Extract all text with coordinates
   378|    chars = page.chars
   379|    for char in chars[:10]:  # First 10 characters
   380|        print(f"Char: '{char['text']}' at x:{char['x0']:.1f} y:{char['y0']:.1f}")
   381|
   382|    # Extract text by bounding box (left, top, right, bottom)
   383|    bbox_text = page.within_bbox((100, 100, 400, 200)).extract_text()
   384|```
   385|
   386|#### Advanced Table Extraction with Custom Settings
   387|
   388|```python
   389|import pdfplumber
   390|import pandas as pd
   391|
   392|with pdfplumber.open("complex_table.pdf") as pdf:
   393|    page = pdf.pages[0]
   394|
   395|    # Extract tables with custom settings for complex layouts
   396|    table_settings = {
   397|        "vertical_strategy": "lines",
   398|        "horizontal_strategy": "lines",
   399|        "snap_tolerance": 3,
   400|        "intersection_tolerance": 15
   401|    }
   402|    tables = page.extract_tables(table_settings)
   403|
   404|    # Visual debugging for table extraction
   405|    img = page.to_image(resolution=150)
   406|    img.save("debug_layout.png")
   407|```
   408|
   409|### reportlab Advanced Features
   410|
   411|#### Create Professional Reports with Tables
   412|
   413|```python
   414|from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
   415|from reportlab.lib.styles import getSampleStyleSheet
   416|from reportlab.lib import colors
   417|
   418|# Sample data
   419|data = [
   420|    ['Product', 'Q1', 'Q2', 'Q3', 'Q4'],
   421|    ['Widgets', '120', '135', '142', '158'],
   422|    ['Gadgets', '85', '92', '98', '105']
   423|]
   424|
   425|# Create PDF with table
   426|doc = SimpleDocTemplate("report.pdf")
   427|elements = []
   428|
   429|# Add title
   430|styles = getSampleStyleSheet()
   431|title = Paragraph("Quarterly Sales Report", styles['Title'])
   432|elements.append(title)
   433|
   434|# Add table with advanced styling
   435|table = Table(data)
   436|table.setStyle(TableStyle([
   437|    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
   438|    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
   439|    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
   440|    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
   441|    ('FONTSIZE', (0, 0), (-1, 0), 14),
   442|    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
   443|    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
   444|    ('GRID', (0, 0), (-1, -1), 1, colors.black)
   445|]))
   446|elements.append(table)
   447|
   448|doc.build(elements)
   449|```
   450|
   451|## Complex Workflows
   452|
   453|### Extract Figures/Images from PDF
   454|
   455|#### Method 1: Using pdfimages (fastest)
   456|
   457|```bash
   458|# Extract all images with original quality
   459|pdfimages -all document.pdf images/img
   460|```
   461|
   462|#### Method 2: Using pypdfium2 + Image Processing
   463|
   464|```python
   465|import pypdfium2 as pdfium
   466|from PIL import Image
   467|import numpy as np
   468|
   469|def extract_figures(pdf_path, output_dir):
   470|    pdf = pdfium.PdfDocument(pdf_path)
   471|
   472|    for page_num, page in enumerate(pdf):
   473|        # Render high-resolution page
   474|        bitmap = page.render(scale=3.0)
   475|        img = bitmap.to_pil()
   476|
   477|        # Convert to numpy for processing
   478|        img_array = np.array(img)
   479|
   480|        # Simple figure detection (non-white regions)
   481|        mask = np.any(img_array != [255, 255, 255], axis=2)
   482|
   483|        # Find contours and extract bounding boxes
   484|        # (This is simplified - real implementation would need more sophisticated detection)
   485|
   486|        # Save detected figures
   487|        # ... implementation depends on specific needs
   488|```
   489|
   490|### Batch PDF Processing with Error Handling
   491|
   492|```python
   493|import os
   494|import glob
   495|from pypdf import PdfReader, PdfWriter
   496|import logging
   497|
   498|logging.basicConfig(level=logging.INFO)
   499|logger = logging.getLogger(__name__)
   500|
   501|