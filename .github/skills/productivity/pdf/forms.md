---
name: pdf-forms
description: "Pdf Forms"
version: 1.0.0
author: Alexa
---
     1|**CRITICAL: You MUST complete these steps in order. Do not skip ahead to writing code.**
     2|
     3|If you need to fill out a PDF form, first check to see if the PDF has fillable form fields. Run this script from this file's directory: `python scripts/check_fillable_fields <file.pdf>`, and depending on the result go to either the "Fillable fields" or "Non-fillable fields" and follow those instructions.
     4|
     5|# Fillable fields
     6|
     7|If the PDF has fillable form fields:
     8|
     9|- Run this script from this file's directory: `python scripts/extract_form_field_info.py <input.pdf> <field_info.json>`. It will create a JSON file with a list of fields in this format:
    10|
    11|```
    12|[
    13|  {
    14|    "field_id": (unique ID for the field),
    15|    "page": (page number, 1-based),
    16|    "rect": ([left, bottom, right, top] bounding box in PDF coordinates, y=0 is the bottom of the page),
    17|    "type": ("text", "checkbox", "radio_group", or "choice"),
    18|  },
    19|  // Checkboxes have "checked_value" and "unchecked_value" properties:
    20|  {
    21|    "field_id": (unique ID for the field),
    22|    "page": (page number, 1-based),
    23|    "type": "checkbox",
    24|    "checked_value": (Set the field to this value to check the checkbox),
    25|    "unchecked_value": (Set the field to this value to uncheck the checkbox),
    26|  },
    27|  // Radio groups have a "radio_options" list with the possible choices.
    28|  {
    29|    "field_id": (unique ID for the field),
    30|    "page": (page number, 1-based),
    31|    "type": "radio_group",
    32|    "radio_options": [
    33|      {
    34|        "value": (set the field to this value to select this radio option),
    35|        "rect": (bounding box for the radio button for this option)
    36|      },
    37|      // Other radio options
    38|    ]
    39|  },
    40|  // Multiple choice fields have a "choice_options" list with the possible choices:
    41|  {
    42|    "field_id": (unique ID for the field),
    43|    "page": (page number, 1-based),
    44|    "type": "choice",
    45|    "choice_options": [
    46|      {
    47|        "value": (set the field to this value to select this option),
    48|        "text": (display text of the option)
    49|      },
    50|      // Other choice options
    51|    ],
    52|  }
    53|]
    54|```
    55|
    56|- Convert the PDF to PNGs (one image for each page) with this script (run from this file's directory): `python scripts/convert_pdf_to_images.py <file.pdf> <output_directory>` Then analyze the images to determine the purpose of each form field (make sure to convert the bounding box PDF coordinates to image coordinates).
    57|- Create a `field_values.json` file in this format with the values to be entered for each field:
    58|
    59|```
    60|[
    61|  {
    62|    "field_id": "last_name", // Must match the field_id from `extract_form_field_info.py`
    63|    "description": "The user's last name",
    64|    "page": 1, // Must match the "page" value in field_info.json
    65|    "value": "Simpson"
    66|  },
    67|  {
    68|    "field_id": "Checkbox12",
    69|    "description": "Checkbox to be checked if the user is 18 or over",
    70|    "page": 1,
    71|    "value": "/On" // If this is a checkbox, use its "checked_value" value to check it. If it's a radio button group, use one of the "value" values in "radio_options".
    72|  },
    73|  // more fields
    74|]
    75|```
    76|
    77|- Run the `fill_fillable_fields.py` script from this file's directory to create a filled-in PDF: `python scripts/fill_fillable_fields.py <input pdf> <field_values.json> <output pdf>` This script will verify that the field IDs and values you provide are valid; if it prints error messages, correct the appropriate fields and try again.
    78|
    79|# Non-fillable fields
    80|
    81|If the PDF doesn't have fillable form fields, you'll add text annotations. First try to extract coordinates from the PDF structure (more accurate), then fall back to visual estimation if needed.
    82|
    83|## Step 1: Try Structure Extraction First
    84|
    85|Run this script to extract text labels, lines, and checkboxes with their exact PDF coordinates: `python scripts/extract_form_structure.py <input.pdf> form_structure.json`
    86|
    87|This creates a JSON file containing:
    88|
    89|- **labels**: Every text element with exact coordinates (x0, top, x1, bottom in PDF points)
    90|- **lines**: Horizontal lines that define row boundaries
    91|- **checkboxes**: Small square rectangles that are checkboxes (with center coordinates)
    92|- **row_boundaries**: Row top/bottom positions calculated from horizontal lines
    93|
    94|**Check the results**: If `form_structure.json` has meaningful labels (text elements that correspond to form fields), use **Approach A: Structure-Based Coordinates**. If the PDF is scanned/image-based and has few or no labels, use **Approach B: Visual Estimation**.
    95|
    96|---
    97|
    98|## Approach A: Structure-Based Coordinates (Preferred)
    99|
   100|Use this when `extract_form_structure.py` found text labels in the PDF.
   101|
   102|### A.1: Analyze the Structure
   103|
   104|Read form_structure.json and identify:
   105|
   106|1. **Label groups**: Adjacent text elements that form a single label (e.g., "Last" + "Name")
   107|2. **Row structure**: Labels with similar `top` values are in the same row
   108|3. **Field columns**: Entry areas start after label ends (x0 = label.x1 + gap)
   109|4. **Checkboxes**: Use the checkbox coordinates directly from the structure
   110|
   111|**Coordinate system**: PDF coordinates where y=0 is at TOP of page, y increases downward.
   112|
   113|### A.2: Check for Missing Elements
   114|
   115|The structure extraction may not detect all form elements. Common cases:
   116|
   117|- **Circular checkboxes**: Only square rectangles are detected as checkboxes
   118|- **Complex graphics**: Decorative elements or non-standard form controls
   119|- **Faded or light-colored elements**: May not be extracted
   120|
   121|If you see form fields in the PDF images that aren't in form_structure.json, you'll need to use **visual analysis** for those specific fields (see "Hybrid Approach" below).
   122|
   123|### A.3: Create fields.json with PDF Coordinates
   124|
   125|For each field, calculate entry coordinates from the extracted structure:
   126|
   127|**Text fields:**
   128|
   129|- entry x0 = label x1 + 5 (small gap after label)
   130|- entry x1 = next label's x0, or row boundary
   131|- entry top = same as label top
   132|- entry bottom = row boundary line below, or label bottom + row_height
   133|
   134|**Checkboxes:**
   135|
   136|- Use the checkbox rectangle coordinates directly from form_structure.json
   137|- entry_bounding_box = [checkbox.x0, checkbox.top, checkbox.x1, checkbox.bottom]
   138|
   139|Create fields.json using `pdf_width` and `pdf_height` (signals PDF coordinates):
   140|
   141|```json
   142|{
   143|  "form_fields": [
   144|    {
   145|      "page_number": 1,
   146|      "description": "Last name entry field",
   147|      "field_label": "Last Name",
   148|      "label_bounding_box": [43, 63, 87, 73],
   149|      "entry_bounding_box": [92, 63, 260, 79],
   150|      "entry_text": { "text": "Smith", "font_size": 10 }
   151|    },
   152|    {
   153|      "page_number": 1,
   154|      "description": "US Citizen Yes checkbox",
   155|      "field_label": "Yes",
   156|      "label_bounding_box": [260, 200, 280, 210],
   157|      "entry_bounding_box": [285, 197, 292, 205],
   158|      "entry_text": { "text": "X" }
   159|    }
   160|  ],
   161|  "pages": [{ "page_number": 1, "pdf_width": 612, "pdf_height": 792 }]
   162|}
   163|```
   164|
   165|**Important**: Use `pdf_width`/`pdf_height` and coordinates directly from form_structure.json.
   166|
   167|### A.4: Validate Bounding Boxes
   168|
   169|Before filling, check your bounding boxes for errors: `python scripts/check_bounding_boxes.py fields.json`
   170|
   171|This checks for intersecting bounding boxes and entry boxes that are too small for the font size. Fix any reported errors before filling.
   172|
   173|---
   174|
   175|## Approach B: Visual Estimation (Fallback)
   176|
   177|Use this when the PDF is scanned/image-based and structure extraction found no usable text labels (e.g., all text shows as "(cid:X)" patterns).
   178|
   179|### B.1: Convert PDF to Images
   180|
   181|`python scripts/convert_pdf_to_images.py <input.pdf> <images_dir/>`
   182|
   183|### B.2: Initial Field Identification
   184|
   185|Examine each page image to identify form sections and get **rough estimates** of field locations:
   186|
   187|- Form field labels and their approximate positions
   188|- Entry areas (lines, boxes, or blank spaces for text input)
   189|- Checkboxes and their approximate locations
   190|
   191|For each field, note approximate pixel coordinates (they don't need to be precise yet).
   192|
   193|### B.3: Zoom Refinement (CRITICAL for accuracy)
   194|
   195|For each field, crop a region around the estimated position to refine coordinates precisely.
   196|
   197|**Create a zoomed crop using ImageMagick:**
   198|
   199|```bash
   200|magick <page_image> -crop <width>x<height>+<x>+<y> +repage <crop_output.png>
   201|```
   202|
   203|Where:
   204|
   205|- `<x>, <y>` = top-left corner of crop region (use your rough estimate minus padding)
   206|- `<width>, <height>` = size of crop region (field area plus ~50px padding on each side)
   207|
   208|**Example:** To refine a "Name" field estimated around (100, 150):
   209|
   210|```bash
   211|magick images_dir/page_1.png -crop 300x80+50+120 +repage crops/name_field.png
   212|```
   213|
   214|(Note: if the `magick` command isn't available, try `convert` with the same arguments).
   215|
   216|**Examine the cropped image** to determine precise coordinates:
   217|
   218|1. Identify the exact pixel where the entry area begins (after the label)
   219|2. Identify where the entry area ends (before next field or edge)
   220|3. Identify the top and bottom of the entry line/box
   221|
   222|**Convert crop coordinates back to full image coordinates:**
   223|
   224|- full_x = crop_x + crop_offset_x
   225|- full_y = crop_y + crop_offset_y
   226|
   227|Example: If the crop started at (50, 120) and the entry box starts at (52, 18) within the crop:
   228|
   229|- entry_x0 = 52 + 50 = 102
   230|- entry_top = 18 + 120 = 138
   231|
   232|**Repeat for each field**, grouping nearby fields into single crops when possible.
   233|
   234|### B.4: Create fields.json with Refined Coordinates
   235|
   236|Create fields.json using `image_width` and `image_height` (signals image coordinates):
   237|
   238|```json
   239|{
   240|  "form_fields": [
   241|    {
   242|      "page_number": 1,
   243|      "description": "Last name entry field",
   244|      "field_label": "Last Name",
   245|      "label_bounding_box": [120, 175, 242, 198],
   246|      "entry_bounding_box": [255, 175, 720, 218],
   247|      "entry_text": { "text": "Smith", "font_size": 10 }
   248|    }
   249|  ],
   250|  "pages": [
   251|    { "page_number": 1, "image_width": 1700, "image_height": 2200 }
   252|  ]
   253|}
   254|```
   255|
   256|**Important**: Use `image_width`/`image_height` and the refined pixel coordinates from the zoom analysis.
   257|
   258|### B.5: Validate Bounding Boxes
   259|
   260|Before filling, check your bounding boxes for errors: `python scripts/check_bounding_boxes.py fields.json`
   261|
   262|This checks for intersecting bounding boxes and entry boxes that are too small for the font size. Fix any reported errors before filling.
   263|
   264|---
   265|
   266|## Hybrid Approach: Structure + Visual
   267|
   268|Use this when structure extraction works for most fields but misses some elements (e.g., circular checkboxes, unusual form controls).
   269|
   270|1. **Use Approach A** for fields that were detected in form_structure.json
   271|2. **Convert PDF to images** for visual analysis of missing fields
   272|3. **Use zoom refinement** (from Approach B) for the missing fields
   273|4. **Combine coordinates**: For fields from structure extraction, use `pdf_width`/`pdf_height`. For visually-estimated fields, you must convert image coordinates to PDF coordinates:
   274|   - pdf_x = image_x \* (pdf_width / image_width)
   275|   - pdf_y = image_y \* (pdf_height / image_height)
   276|5. **Use a single coordinate system** in fields.json - convert all to PDF coordinates with `pdf_width`/`pdf_height`
   277|
   278|---
   279|
   280|## Step 2: Validate Before Filling
   281|
   282|**Always validate bounding boxes before filling:** `python scripts/check_bounding_boxes.py fields.json`
   283|
   284|This checks for:
   285|
   286|- Intersecting bounding boxes (which would cause overlapping text)
   287|- Entry boxes that are too small for the specified font size
   288|
   289|Fix any reported errors in fields.json before proceeding.
   290|
   291|## Step 3: Fill the Form
   292|
   293|The fill script auto-detects the coordinate system and handles conversion: `python scripts/fill_pdf_form_with_annotations.py <input.pdf> fields.json <output.pdf>`
   294|
   295|## Step 4: Verify Output
   296|
   297|Convert the filled PDF to images and verify text placement: `python scripts/convert_pdf_to_images.py <output.pdf> <verify_images/>`
   298|
   299|If text is mispositioned:
   300|
   301|- **Approach A**: Check that you're using PDF coordinates from form_structure.json with `pdf_width`/`pdf_height`
   302|- **Approach B**: Check that image dimensions match and coordinates are accurate pixels
   303|- **Hybrid**: Ensure coordinate conversions are correct for visually-estimated fields
   304|