---
name: shadcn-base-vs-radix
description: "Shadcn Base Vs Radix"
version: 1.0.0
author: Alexa
---
     1|---
     2|description: API differences between base and radix shadcn versions
     3|applyTo: "**/*"
     4|priority: medium
     5|canonicalSource: AGENTS.md
     6|category: development
     7|tags: [shadcn, ui, base, radix]
     8|date: 2026-05-17
     9|lastReviewed: 2026-05-17
    10|---
    11|
    12|# Base vs Radix
    13|
    14|API differences between `base` and `radix`. Check the `base` field from `npx shadcn@latest info`.
    15|
    16|## Contents
    17|
    18|- Composition: asChild vs render
    19|- Button / trigger as non-button element
    20|- Select (items prop, placeholder, positioning, multiple, object values)
    21|- ToggleGroup (type vs multiple)
    22|- Slider (scalar vs array)
    23|- Accordion (type and defaultValue)
    24|
    25|---
    26|
    27|## Composition: asChild (radix) vs render (base)
    28|
    29|Radix uses `asChild` to replace the default element. Base uses `render`. Don't wrap triggers in extra elements.
    30|
    31|**Incorrect:**
    32|
    33|```tsx
    34|<DialogTrigger>
    35|  <div>
    36|    <Button>Open</Button>
    37|  </div>
    38|</DialogTrigger>
    39|```
    40|
    41|**Correct (radix):**
    42|
    43|```tsx
    44|<DialogTrigger asChild>
    45|  <Button>Open</Button>
    46|</DialogTrigger>
    47|```
    48|
    49|**Correct (base):**
    50|
    51|```tsx
    52|<DialogTrigger render={<Button />}>Open</DialogTrigger>
    53|```
    54|
    55|This applies to all trigger and close components: `DialogTrigger`, `SheetTrigger`, `AlertDialogTrigger`, `DropdownMenuTrigger`, `PopoverTrigger`, `TooltipTrigger`, `CollapsibleTrigger`, `DialogClose`, `SheetClose`, `NavigationMenuLink`, `BreadcrumbLink`, `SidebarMenuButton`, `Badge`, `Item`.
    56|
    57|---
    58|
    59|## Button / trigger as non-button element (base only)
    60|
    61|When `render` changes an element to a non-button (`<a>`, `<span>`), add `nativeButton={false}`.
    62|
    63|**Incorrect (base):** missing `nativeButton={false}`.
    64|
    65|```tsx
    66|<Button render={<a href="/docs" />}>Read the docs</Button>
    67|```
    68|
    69|**Correct (base):**
    70|
    71|```tsx
    72|<Button render={<a href="/docs" />} nativeButton={false}>
    73|  Read the docs
    74|</Button>
    75|```
    76|
    77|**Correct (radix):**
    78|
    79|```tsx
    80|<Button asChild>
    81|  <a href="/docs">Read the docs</a>
    82|</Button>
    83|```
    84|
    85|Same for triggers whose `render` is not a `Button`:
    86|
    87|```tsx
    88|// base.
    89|<PopoverTrigger render={<InputGroupAddon />} nativeButton={false}>
    90|  Pick date
    91|</PopoverTrigger>
    92|```
    93|
    94|---
    95|
    96|## Select
    97|
    98|**items prop (base only).** Base requires an `items` prop on the root. Radix uses inline JSX only.
    99|
   100|**Incorrect (base):**
   101|
   102|```tsx
   103|<Select>
   104|  <SelectTrigger>
   105|    <SelectValue placeholder="Select a fruit" />
   106|  </SelectTrigger>
   107|</Select>
   108|```
   109|
   110|**Correct (base):**
   111|
   112|```tsx
   113|const items = [
   114|  { label: "Select a fruit", value: null },
   115|  { label: "Apple", value: "apple" },
   116|  { label: "Banana", value: "banana" },
   117|]
   118|
   119|<Select items={items}>
   120|  <SelectTrigger>
   121|    <SelectValue />
   122|  </SelectTrigger>
   123|  <SelectContent>
   124|    <SelectGroup>
   125|      {items.map((item) => (
   126|        <SelectItem key={item.value} value={item.value}>{item.label}</SelectItem>
   127|      ))}
   128|    </SelectGroup>
   129|  </SelectContent>
   130|</Select>
   131|```
   132|
   133|**Correct (radix):**
   134|
   135|```tsx
   136|<Select>
   137|  <SelectTrigger>
   138|    <SelectValue placeholder="Select a fruit" />
   139|  </SelectTrigger>
   140|  <SelectContent>
   141|    <SelectGroup>
   142|      <SelectItem value="apple">Apple</SelectItem>
   143|      <SelectItem value="banana">Banana</SelectItem>
   144|    </SelectGroup>
   145|  </SelectContent>
   146|</Select>
   147|```
   148|
   149|**Placeholder.** Base uses a `{ value: null }` item in the items array. Radix uses `<SelectValue placeholder="...">`.
   150|
   151|**Content positioning.** Base uses `alignItemWithTrigger`. Radix uses `position`.
   152|
   153|```tsx
   154|// base.
   155|<SelectContent alignItemWithTrigger={false} side="bottom">
   156|
   157|// radix.
   158|<SelectContent position="popper">
   159|```
   160|
   161|---
   162|
   163|## Select — multiple selection and object values (base only)
   164|
   165|Base supports `multiple`, render-function children on `SelectValue`, and object values with `itemToStringValue`. Radix is single-select with string values only.
   166|
   167|**Correct (base — multiple selection):**
   168|
   169|```tsx
   170|<Select items={items} multiple defaultValue={[]}>
   171|  <SelectTrigger>
   172|    <SelectValue>
   173|      {(value: string[]) =>
   174|        value.length === 0
   175|          ? "Select fruits"
   176|          : `${value.length} selected`
   177|      }
   178|    </SelectValue>
   179|  </SelectTrigger>
   180|  ...
   181|</Select>
   182|```
   183|
   184|**Correct (base — object values):**
   185|
   186|```tsx
   187|<Select defaultValue={plans[0]} itemToStringValue={plan => plan.name}>
   188|  <SelectTrigger>
   189|    <SelectValue>{value => value.name}</SelectValue>
   190|  </SelectTrigger>
   191|  ...
   192|</Select>
   193|```
   194|
   195|---
   196|
   197|## ToggleGroup
   198|
   199|Base uses a `multiple` boolean prop. Radix uses `type="single"` or `type="multiple"`.
   200|
   201|**Incorrect (base):**
   202|
   203|```tsx
   204|<ToggleGroup type="single" defaultValue="daily">
   205|  <ToggleGroupItem value="daily">Daily</ToggleGroupItem>
   206|</ToggleGroup>
   207|```
   208|
   209|**Correct (base):**
   210|
   211|```tsx
   212|// Single (no prop needed), defaultValue is always an array.
   213|<ToggleGroup defaultValue={["daily"]} spacing={2}>
   214|  <ToggleGroupItem value="daily">Daily</ToggleGroupItem>
   215|  <ToggleGroupItem value="weekly">Weekly</ToggleGroupItem>
   216|</ToggleGroup>
   217|
   218|// Multi-selection.
   219|<ToggleGroup multiple>
   220|  <ToggleGroupItem value="bold">Bold</ToggleGroupItem>
   221|  <ToggleGroupItem value="italic">Italic</ToggleGroupItem>
   222|</ToggleGroup>
   223|```
   224|
   225|**Correct (radix):**
   226|
   227|```tsx
   228|// Single, defaultValue is a string.
   229|<ToggleGroup type="single" defaultValue="daily" spacing={2}>
   230|  <ToggleGroupItem value="daily">Daily</ToggleGroupItem>
   231|  <ToggleGroupItem value="weekly">Weekly</ToggleGroupItem>
   232|</ToggleGroup>
   233|
   234|// Multi-selection.
   235|<ToggleGroup type="multiple">
   236|  <ToggleGroupItem value="bold">Bold</ToggleGroupItem>
   237|  <ToggleGroupItem value="italic">Italic</ToggleGroupItem>
   238|</ToggleGroup>
   239|```
   240|
   241|**Controlled single value:**
   242|
   243|```tsx
   244|// base — wrap/unwrap arrays.
   245|const [value, setValue] = React.useState("normal")
   246|<ToggleGroup value={[value]} onValueChange={(v) => setValue(v[0])}>
   247|
   248|// radix — plain string.
   249|const [value, setValue] = React.useState("normal")
   250|<ToggleGroup type="single" value={value} onValueChange={setValue}>
   251|```
   252|
   253|---
   254|
   255|## Slider
   256|
   257|Base accepts a plain number for a single thumb. Radix always requires an array.
   258|
   259|**Incorrect (base):**
   260|
   261|```tsx
   262|<Slider defaultValue={[50]} max={100} step={1} />
   263|```
   264|
   265|**Correct (base):**
   266|
   267|```tsx
   268|<Slider defaultValue={50} max={100} step={1} />
   269|```
   270|
   271|**Correct (radix):**
   272|
   273|```tsx
   274|<Slider defaultValue={[50]} max={100} step={1} />
   275|```
   276|
   277|Both use arrays for range sliders. Controlled `onValueChange` in base may need a cast:
   278|
   279|```tsx
   280|// base.
   281|const [value, setValue] = React.useState([0.3, 0.7])
   282|<Slider value={value} onValueChange={(v) => setValue(v as number[])} />
   283|
   284|// radix.
   285|const [value, setValue] = React.useState([0.3, 0.7])
   286|<Slider value={value} onValueChange={setValue} />
   287|```
   288|
   289|---
   290|
   291|## Accordion
   292|
   293|Radix requires `type="single"` or `type="multiple"` and supports `collapsible`. `defaultValue` is a string. Base uses no `type` prop, uses `multiple` boolean, and `defaultValue` is always an array.
   294|
   295|**Incorrect (base):**
   296|
   297|```tsx
   298|<Accordion type="single" collapsible defaultValue="item-1">
   299|  <AccordionItem value="item-1">...</AccordionItem>
   300|</Accordion>
   301|```
   302|
   303|**Correct (base):**
   304|
   305|```tsx
   306|<Accordion defaultValue={["item-1"]}>
   307|  <AccordionItem value="item-1">...</AccordionItem>
   308|</Accordion>
   309|
   310|// Multi-select.
   311|<Accordion multiple defaultValue={["item-1", "item-2"]}>
   312|  <AccordionItem value="item-1">...</AccordionItem>
   313|  <AccordionItem value="item-2">...</AccordionItem>
   314|</Accordion>
   315|```
   316|
   317|**Correct (radix):**
   318|
   319|```tsx
   320|<Accordion type="single" collapsible defaultValue="item-1">
   321|  <AccordionItem value="item-1">...</AccordionItem>
   322|</Accordion>
   323|```
   324|