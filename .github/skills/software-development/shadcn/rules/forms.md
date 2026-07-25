---
name: shadcn-forms
description: "Shadcn Forms"
version: 1.0.0
author: Alexa
---
     1|---
     2|description: Forms & inputs composition patterns
     3|applyTo: "**/*"
     4|priority: medium
     5|canonicalSource: AGENTS.md
     6|category: development
     7|tags: [shadcn, ui, forms]
     8|date: 2026-05-17
     9|lastReviewed: 2026-05-17
    10|---
    11|
    12|---
    13|
    14|description: Forms & inputs composition patterns for shadcn/ui components applyTo: "\*_/_" priority: medium canonicalSource: AGENTS.md category: development tags: [shadcn, ui, forms] date: 2026-05-17 lastReviewed: 2026-05-17
    15|
    16|---
    17|
    18|# Forms & Inputs
    19|
    20|## Contents
    21|
    22|- Forms use FieldGroup + Field
    23|- InputGroup requires InputGroupInput/InputGroupTextarea
    24|- Buttons inside inputs use InputGroup + InputGroupAddon
    25|- Option sets (2–7 choices) use ToggleGroup
    26|- FieldSet + FieldLegend for grouping related fields
    27|- Field validation and disabled states
    28|
    29|---
    30|
    31|## Forms use FieldGroup + Field
    32|
    33|Always use `FieldGroup` + `Field` — never raw `div` with `space-y-*`:
    34|
    35|```tsx
    36|<FieldGroup>
    37|  <Field>
    38|    <FieldLabel htmlFor="email">Email</FieldLabel>
    39|    <Input id="email" type="email" />
    40|  </Field>
    41|  <Field>
    42|    <FieldLabel htmlFor="password">Password</FieldLabel>
    43|    <Input id="password" type="password" />
    44|  </Field>
    45|</FieldGroup>
    46|```
    47|
    48|Use `Field orientation="horizontal"` for settings pages. Use `FieldLabel className="sr-only"` for visually hidden labels.
    49|
    50|**Choosing form controls:**
    51|
    52|- Simple text input → `Input`
    53|- Dropdown with predefined options → `Select`
    54|- Searchable dropdown → `Combobox`
    55|- Native HTML select (no JS) → `native-select`
    56|- Boolean toggle → `Switch` (for settings) or `Checkbox` (for forms)
    57|- Single choice from few options → `RadioGroup`
    58|- Toggle between 2–5 options → `ToggleGroup` + `ToggleGroupItem`
    59|- OTP/verification code → `InputOTP`
    60|- Multi-line text → `Textarea`
    61|
    62|---
    63|
    64|## InputGroup requires InputGroupInput/InputGroupTextarea
    65|
    66|Never use raw `Input` or `Textarea` inside an `InputGroup`.
    67|
    68|**Incorrect:**
    69|
    70|```tsx
    71|<InputGroup>
    72|  <Input placeholder="Search..." />
    73|</InputGroup>
    74|```
    75|
    76|**Correct:**
    77|
    78|```tsx
    79|import {
    80|  InputGroup,
    81|  InputGroupInput
    82|} from "@/components/ui/input-group";
    83|
    84|<InputGroup>
    85|  <InputGroupInput placeholder="Search..." />
    86|</InputGroup>;
    87|```
    88|
    89|---
    90|
    91|## Buttons inside inputs use InputGroup + InputGroupAddon
    92|
    93|Never place a `Button` directly inside or adjacent to an `Input` with custom positioning.
    94|
    95|**Incorrect:**
    96|
    97|```tsx
    98|<div className="relative">
    99|  <Input placeholder="Search..." className="pr-10" />
   100|  <Button className="absolute right-0 top-0" size="icon">
   101|    <SearchIcon />
   102|  </Button>
   103|</div>
   104|```
   105|
   106|**Correct:**
   107|
   108|```tsx
   109|import {
   110|  InputGroup,
   111|  InputGroupInput,
   112|  InputGroupAddon
   113|} from "@/components/ui/input-group";
   114|
   115|<InputGroup>
   116|  <InputGroupInput placeholder="Search..." />
   117|  <InputGroupAddon>
   118|    <Button size="icon">
   119|      <SearchIcon data-icon="inline-start" />
   120|    </Button>
   121|  </InputGroupAddon>
   122|</InputGroup>;
   123|```
   124|
   125|---
   126|
   127|## Option sets (2–7 choices) use ToggleGroup
   128|
   129|Don't manually loop `Button` components with active state.
   130|
   131|**Incorrect:**
   132|
   133|```tsx
   134|const [selected, setSelected] = useState("daily")
   135|
   136|<div className="flex gap-2">
   137|  {["daily", "weekly", "monthly"].map((option) => (
   138|    <Button
   139|      key={option}
   140|      variant={selected === option ? "default" : "outline"}
   141|      onClick={() => setSelected(option)}
   142|    >
   143|      {option}
   144|    </Button>
   145|  ))}
   146|</div>
   147|```
   148|
   149|**Correct:**
   150|
   151|```tsx
   152|import {
   153|  ToggleGroup,
   154|  ToggleGroupItem
   155|} from "@/components/ui/toggle-group";
   156|
   157|<ToggleGroup spacing={2}>
   158|  <ToggleGroupItem value="daily">Daily</ToggleGroupItem>
   159|  <ToggleGroupItem value="weekly">Weekly</ToggleGroupItem>
   160|  <ToggleGroupItem value="monthly">Monthly</ToggleGroupItem>
   161|</ToggleGroup>;
   162|```
   163|
   164|Combine with `Field` for labelled toggle groups:
   165|
   166|```tsx
   167|<Field orientation="horizontal">
   168|  <FieldTitle id="theme-label">Theme</FieldTitle>
   169|  <ToggleGroup aria-labelledby="theme-label" spacing={2}>
   170|    <ToggleGroupItem value="light">Light</ToggleGroupItem>
   171|    <ToggleGroupItem value="dark">Dark</ToggleGroupItem>
   172|    <ToggleGroupItem value="system">System</ToggleGroupItem>
   173|  </ToggleGroup>
   174|</Field>
   175|```
   176|
   177|> **Note:** `defaultValue` and `type`/`multiple` props differ between base and radix. See [base-vs-radix.md](./base-vs-radix.md#togglegroup).
   178|
   179|---
   180|
   181|## FieldSet + FieldLegend for grouping related fields
   182|
   183|Use `FieldSet` + `FieldLegend` for related checkboxes, radios, or switches — not `div` with a heading:
   184|
   185|```tsx
   186|<FieldSet>
   187|  <FieldLegend variant="label">Preferences</FieldLegend>
   188|  <FieldDescription>Select all that apply.</FieldDescription>
   189|  <FieldGroup className="gap-3">
   190|    <Field orientation="horizontal">
   191|      <Checkbox id="dark" />
   192|      <FieldLabel htmlFor="dark" className="font-normal">
   193|        Dark mode
   194|      </FieldLabel>
   195|    </Field>
   196|  </FieldGroup>
   197|</FieldSet>
   198|```
   199|
   200|---
   201|
   202|## Field validation and disabled states
   203|
   204|Both attributes are needed — `data-invalid`/`data-disabled` styles the field (label, description), while `aria-invalid`/`disabled` styles the control.
   205|
   206|```tsx
   207|// Invalid.
   208|<Field data-invalid>
   209|  <FieldLabel htmlFor="email">Email</FieldLabel>
   210|  <Input id="email" aria-invalid />
   211|  <FieldDescription>Invalid email address.</FieldDescription>
   212|</Field>
   213|
   214|// Disabled.
   215|<Field data-disabled>
   216|  <FieldLabel htmlFor="email">Email</FieldLabel>
   217|  <Input id="email" disabled />
   218|</Field>
   219|```
   220|
   221|Works for all controls: `Input`, `Textarea`, `Select`, `Checkbox`, `RadioGroupItem`, `Switch`, `Slider`, `NativeSelect`, `InputOTP`.
   222|