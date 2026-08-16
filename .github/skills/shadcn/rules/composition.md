---
name: shadcn-composition
description: "Shadcn Composition"
version: 1.0.0
author: Alexa
---
     1|---
     2|description: Component composition rules
     3|applyTo: "**/*"
     4|priority: medium
     5|canonicalSource: AGENTS.md
     6|category: development
     7|tags: [shadcn, ui, composition]
     8|date: 2026-05-17
     9|lastReviewed: 2026-05-17
    10|---
    11|
    12|# Component Composition
    13|
    14|## Contents
    15|
    16|- Items always inside their Group component
    17|- Callouts use Alert
    18|- Empty states use Empty component
    19|- Toast notifications use sonner
    20|- Choosing between overlay components
    21|- Dialog, Sheet, and Drawer always need a Title
    22|- Card structure
    23|- Button has no isPending or isLoading prop
    24|- TabsTrigger must be inside TabsList
    25|- Avatar always needs AvatarFallback
    26|- Use Separator instead of raw hr or border divs
    27|- Use Skeleton for loading placeholders
    28|- Use Badge instead of custom styled spans
    29|
    30|---
    31|
    32|## Items always inside their Group component
    33|
    34|Never render items directly inside the content container.
    35|
    36|**Incorrect:**
    37|
    38|```tsx
    39|<SelectContent>
    40|  <SelectItem value="apple">Apple</SelectItem>
    41|  <SelectItem value="banana">Banana</SelectItem>
    42|</SelectContent>
    43|```
    44|
    45|**Correct:**
    46|
    47|```tsx
    48|<SelectContent>
    49|  <SelectGroup>
    50|    <SelectItem value="apple">Apple</SelectItem>
    51|    <SelectItem value="banana">Banana</SelectItem>
    52|  </SelectGroup>
    53|</SelectContent>
    54|```
    55|
    56|This applies to all group-based components:
    57|
    58|| Item | Group |
    59|| --- | --- |
    60|| `SelectItem`, `SelectLabel` | `SelectGroup` |
    61|| `DropdownMenuItem`, `DropdownMenuLabel`, `DropdownMenuSub` | `DropdownMenuGroup` |
    62|| `MenubarItem` | `MenubarGroup` |
    63|| `ContextMenuItem` | `ContextMenuGroup` |
    64|| `CommandItem` | `CommandGroup` |
    65|
    66|---
    67|
    68|## Callouts use Alert
    69|
    70|```tsx
    71|<Alert>
    72|  <AlertTitle>Warning</AlertTitle>
    73|  <AlertDescription>Something needs attention.</AlertDescription>
    74|</Alert>
    75|```
    76|
    77|---
    78|
    79|## Empty states use Empty component
    80|
    81|```tsx
    82|<Empty>
    83|  <EmptyHeader>
    84|    <EmptyMedia variant="icon">
    85|      <FolderIcon />
    86|    </EmptyMedia>
    87|    <EmptyTitle>No projects yet</EmptyTitle>
    88|    <EmptyDescription>
    89|      Get started by creating a new project.
    90|    </EmptyDescription>
    91|  </EmptyHeader>
    92|  <EmptyContent>
    93|    <Button>Create Project</Button>
    94|  </EmptyContent>
    95|</Empty>
    96|```
    97|
    98|---
    99|
   100|## Toast notifications use sonner
   101|
   102|```tsx
   103|import { toast } from "sonner";
   104|
   105|toast.success("Changes saved.");
   106|toast.error("Something went wrong.");
   107|toast("File deleted.", {
   108|  action: { label: "Undo", onClick: () => undoDelete() }
   109|});
   110|```
   111|
   112|---
   113|
   114|## Choosing between overlay components
   115|
   116|| Use case                           | Component     |
   117|| ---------------------------------- | ------------- |
   118|| Focused task that requires input   | `Dialog`      |
   119|| Destructive action confirmation    | `AlertDialog` |
   120|| Side panel with details or filters | `Sheet`       |
   121|| Mobile-first bottom panel          | `Drawer`      |
   122|| Quick info on hover                | `HoverCard`   |
   123|| Small contextual content on click  | `Popover`     |
   124|
   125|---
   126|
   127|## Dialog, Sheet, and Drawer always need a Title
   128|
   129|`DialogTitle`, `SheetTitle`, `DrawerTitle` are required for accessibility. Use `className="sr-only"` if visually hidden.
   130|
   131|```tsx
   132|<DialogContent>
   133|  <DialogHeader>
   134|    <DialogTitle>Edit Profile</DialogTitle>
   135|    <DialogDescription>Update your profile.</DialogDescription>
   136|  </DialogHeader>
   137|  ...
   138|</DialogContent>
   139|```
   140|
   141|---
   142|
   143|## Card structure
   144|
   145|Use full composition — don't dump everything into `CardContent`:
   146|
   147|```tsx
   148|<Card>
   149|  <CardHeader>
   150|    <CardTitle>Team Members</CardTitle>
   151|    <CardDescription>Manage your team.</CardDescription>
   152|  </CardHeader>
   153|  <CardContent>...</CardContent>
   154|  <CardFooter>
   155|    <Button>Invite</Button>
   156|  </CardFooter>
   157|</Card>
   158|```
   159|
   160|---
   161|
   162|## Button has no isPending or isLoading prop
   163|
   164|Compose with `Spinner` + `data-icon` + `disabled`:
   165|
   166|```tsx
   167|<Button disabled>
   168|  <Spinner data-icon="inline-start" />
   169|  Saving...
   170|</Button>
   171|```
   172|
   173|---
   174|
   175|## TabsTrigger must be inside TabsList
   176|
   177|Never render `TabsTrigger` directly inside `Tabs` — always wrap in `TabsList`:
   178|
   179|```tsx
   180|<Tabs defaultValue="account">
   181|  <TabsList>
   182|    <TabsTrigger value="account">Account</TabsTrigger>
   183|    <TabsTrigger value="password">Password</TabsTrigger>
   184|  </TabsList>
   185|  <TabsContent value="account">...</TabsContent>
   186|</Tabs>
   187|```
   188|
   189|---
   190|
   191|## Avatar always needs AvatarFallback
   192|
   193|Always include `AvatarFallback` for when the image fails to load:
   194|
   195|```tsx
   196|<Avatar>
   197|  <AvatarImage src="/avatar.png" alt="User" />
   198|  <AvatarFallback>JD</AvatarFallback>
   199|</Avatar>
   200|```
   201|
   202|---
   203|
   204|## Use existing components instead of custom markup
   205|
   206|| Instead of | Use |
   207|| --- | --- |
   208|| `<hr>` or `<div className="border-t">` | `<Separator />` |
   209|| `<div className="animate-pulse">` with styled divs | `<Skeleton className="h-4 w-3/4" />` |
   210|| `<span className="rounded-full bg-green-100 ...">` | `<Badge variant="secondary">` |
   211|