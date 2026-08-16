---
name: shadcn-icons
description: "Shadcn Icons"
version: 1.0.0
author: Alexa
---
     1|---
     2|description: Icon usage guidelines and data-icon attribute
     3|applyTo: "**/*"
     4|priority: medium
     5|canonicalSource: AGENTS.md
     6|category: development
     7|tags: [shadcn, ui, icons]
     8|date: 2026-05-17
     9|lastReviewed: 2026-05-17
    10|---
    11|
    12|# Icons
    13|
    14|**Always use the project's configured `iconLibrary` for imports.** Check the `iconLibrary` field from project context: `lucide` → `lucide-react`, `tabler` → `@tabler/icons-react`, etc. Never assume `lucide-react`.
    15|
    16|---
    17|
    18|## Icons in Button use data-icon attribute
    19|
    20|Add `data-icon="inline-start"` (prefix) or `data-icon="inline-end"` (suffix) to the icon. No sizing classes on the icon.
    21|
    22|**Incorrect:**
    23|
    24|```tsx
    25|<Button>
    26|  <SearchIcon className="mr-2 size-4" />
    27|  Search
    28|</Button>
    29|```
    30|
    31|**Correct:**
    32|
    33|```tsx
    34|<Button>
    35|  <SearchIcon data-icon="inline-start"/>
    36|  Search
    37|</Button>
    38|
    39|<Button>
    40|  Next
    41|  <ArrowRightIcon data-icon="inline-end"/>
    42|</Button>
    43|```
    44|
    45|---
    46|
    47|## No sizing classes on icons inside components
    48|
    49|Components handle icon sizing via CSS. Don't add `size-4`, `w-4 h-4`, or other sizing classes to icons inside `Button`, `DropdownMenuItem`, `Alert`, `Sidebar*`, or other shadcn components. Unless the user explicitly asks for custom icon sizes.
    50|
    51|**Incorrect:**
    52|
    53|```tsx
    54|<Button>
    55|  <SearchIcon className="size-4" data-icon="inline-start" />
    56|  Search
    57|</Button>
    58|
    59|<DropdownMenuItem>
    60|  <SettingsIcon className="mr-2 size-4" />
    61|  Settings
    62|</DropdownMenuItem>
    63|```
    64|
    65|**Correct:**
    66|
    67|```tsx
    68|<Button>
    69|  <SearchIcon data-icon="inline-start" />
    70|  Search
    71|</Button>
    72|
    73|<DropdownMenuItem>
    74|  <SettingsIcon />
    75|  Settings
    76|</DropdownMenuItem>
    77|```
    78|
    79|---
    80|
    81|## Pass icons as component objects, not string keys
    82|
    83|Use `icon={CheckIcon}`, not a string key to a lookup map.
    84|
    85|**Incorrect:**
    86|
    87|```tsx
    88|const iconMap = {
    89|  check: CheckIcon,
    90|  alert: AlertIcon
    91|};
    92|
    93|function StatusBadge({ icon }: { icon: string }) {
    94|  const Icon = iconMap[icon];
    95|  return <Icon />;
    96|}
    97|
    98|<StatusBadge icon="check" />;
    99|```
   100|
   101|**Correct:**
   102|
   103|```tsx
   104|// Import from the project's configured iconLibrary (e.g. lucide-react, @tabler/icons-react).
   105|import { CheckIcon } from "lucide-react";
   106|
   107|function StatusBadge({ icon: Icon }: { icon: React.ComponentType }) {
   108|  return <Icon />;
   109|}
   110|
   111|<StatusBadge icon={CheckIcon} />;
   112|```
   113|