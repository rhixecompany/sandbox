# Phase 9B: Components (14 new files + 1 root file)

> Extracted from `plan-comicWiseImplementation.prompt.md`.

## Phase 9B: Components (14 new files + 1 root file)

### 9B.1 — `src/app/global-error.tsx`

```tsx
"use client";
import { useEffect } from "react";
import { Button } from "@/components/ui/button";

export default function GlobalError({
  error,
  reset
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    console.error("[GlobalError]", error);
  }, [error]);

  return (
    <html>
      <body>
        <div className="flex min-h-screen flex-col items-center justify-center gap-4">
          <h2 className="text-2xl font-bold">
            Something went wrong!
          </h2>
          <p className="text-muted-foreground">{error.message}</p>
          {error.digest && (
            <p className="text-xs text-muted-foreground">
              Error ID: {error.digest}
            </p>
          )}
          <Button onClick={reset}>Try again</Button>
        </div>
      </body>
    </html>
  );
}
```

### 9B.2 — `src/components/comics/comic-card.tsx`

```tsx
import Image from "next/image";
import Link from "next/link";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";

interface ComicCardProps {
  comic: {
    id: number;
    title: string;
    slug: string;
    coverImage: string | null;
    status: string;
    rating?: number;
  };
}

export function ComicCard({ comic }: ComicCardProps) {
  return (
    <Card className="@container/card overflow-hidden transition-shadow hover:shadow-md">
      <Link href={`/comics/${comic.slug}`}>
        <div className="relative aspect-[2/3] w-full overflow-hidden">
          {comic.coverImage ? (
            <Image
              src={comic.coverImage}
              alt={comic.title}
              fill
              className="object-cover"
              sizes="(max-width: 768px) 50vw, 25vw"
            />
          ) : (
            <div className="flex h-full items-center justify-center bg-muted">
              <span className="text-muted-foreground text-sm">
                No cover
              </span>
            </div>
          )}
          <Badge
            className="absolute right-2 top-2 text-xs"
            variant="secondary"
          >
            {comic.status}
          </Badge>
        </div>
        <CardContent className="p-2">
          <p className="truncate text-sm font-medium">
            {comic.title}
          </p>
          {comic.rating !== undefined && (
            <p className="text-xs text-muted-foreground">
              ★ {comic.rating.toFixed(1)}
            </p>
          )}
        </CardContent>
      </Link>
    </Card>
  );
}
```

### 9B.3 — `src/components/comics/comic-grid.tsx`

```tsx
import { ComicCard } from "./comic-card";

interface ComicGridProps {
  comics: Array<{
    id: number;
    title: string;
    slug: string;
    coverImage: string | null;
    status: string;
    rating?: number;
  }>;
}

export function ComicGrid({ comics }: ComicGridProps) {
  if (comics.length === 0) {
    return (
      <div className="flex min-h-[200px] items-center justify-center">
        <p className="text-muted-foreground">No comics found.</p>
      </div>
    );
  }
  return (
    <div className="grid grid-cols-2 gap-4 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6">
      {comics.map(comic => (
        <ComicCard key={comic.id} comic={comic} />
      ))}
    </div>
  );
}
```

### 9B.4 — `src/components/comics/comic-filter-bar.tsx`

```tsx
"use client";
import { useComicFiltersStore } from "@/stores/use-comic-filters-store";
import { useDebounce } from "@/hooks/use-debounce";
import { Input } from "@/components/ui/input";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { useEffect } from "react";

const STATUSES = [
  "Ongoing",
  "Hiatus",
  "Completed",
  "Dropped",
  "Season End",
  "Coming Soon"
] as const;

export function ComicFilterBar() {
  const { search, status, setSearch, setStatus, reset } =
    useComicFiltersStore();
  const debouncedSearch = useDebounce(search, 300);

  // debouncedSearch can be forwarded to parent or query via prop
  return (
    <div className="flex flex-wrap gap-2">
      <Input
        placeholder="Search comics…"
        value={search}
        onChange={e => setSearch(e.target.value)}
        className="max-w-xs"
      />
      <div className="flex flex-wrap gap-1">
        {STATUSES.map(s => (
          <Badge
            key={s}
            variant={status === s ? "default" : "outline"}
            className="cursor-pointer"
            onClick={() => setStatus(status === s ? "" : s)}
          >
            {s}
          </Badge>
        ))}
      </div>
      <Button variant="ghost" size="sm" onClick={reset}>
        Clear
      </Button>
    </div>
  );
}
```

### 9B.5 — `src/components/reading/reader-view.tsx`

```tsx
"use client";
import Image from "next/image";
import { useReaderStore } from "@/stores/use-reader-store";
import { Button } from "@/components/ui/button";
import { ChevronLeft, ChevronRight } from "lucide-react";

interface ReaderViewProps {
  images: Array<{ id: number; imageUrl: string; pageNumber: number }>;
  chapterTitle: string;
}

export function ReaderView({
  images,
  chapterTitle
}: ReaderViewProps) {
  const {
    currentPage,
    totalPages,
    setTotalPages,
    nextPage,
    prevPage
  } = useReaderStore();

  // Set total on mount
  if (totalPages !== images.length) setTotalPages(images.length);

  const current = images[currentPage - 1];

  return (
    <div className="flex flex-col items-center gap-4">
      <div className="flex w-full items-center justify-between px-4">
        <Button
          variant="outline"
          size="icon"
          onClick={prevPage}
          disabled={currentPage === 1}
        >
          <ChevronLeft className="h-4 w-4" />
        </Button>
        <span className="text-sm text-muted-foreground">
          {chapterTitle} — Page {currentPage} / {totalPages}
        </span>
        <Button
          variant="outline"
          size="icon"
          onClick={nextPage}
          disabled={currentPage === totalPages}
        >
          <ChevronRight className="h-4 w-4" />
        </Button>
      </div>
      {current && (
        <div className="relative w-full max-w-2xl">
          <Image
            src={current.imageUrl}
            alt={`Page ${current.pageNumber}`}
            width={800}
            height={1200}
            className="w-full object-contain"
            priority={currentPage <= 2}
          />
        </div>
      )}
    </div>
  );
}
```

### 9B.6 — `src/components/ui/pagination.tsx` (if not already present)

```tsx
import { Button } from "@/components/ui/button";
import { ChevronLeft, ChevronRight } from "lucide-react";

interface PaginationProps {
  page: number;
  totalPages: number;
  onPageChange: (page: number) => void;
}

export function Pagination({
  page,
  totalPages,
  onPageChange
}: PaginationProps) {
  return (
    <div className="flex items-center gap-2">
      <Button
        variant="outline"
        size="icon"
        disabled={page <= 1}
        onClick={() => onPageChange(page - 1)}
      >
        <ChevronLeft className="h-4 w-4" />
      </Button>
      <span className="text-sm">
        {page} / {totalPages}
      </span>
      <Button
        variant="outline"
        size="icon"
        disabled={page >= totalPages}
        onClick={() => onPageChange(page + 1)}
      >
        <ChevronRight className="h-4 w-4" />
      </Button>
    </div>
  );
}
```

### 9B.7 — `src/components/ui/data-table.tsx`

```tsx
"use client";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow
} from "@/components/ui/table";

interface Column<T> {
  key: keyof T | string;
  header: string;
  render?: (row: T) => React.ReactNode;
}

interface DataTableProps<T> {
  columns: Column<T>[];
  data: T[];
  keyExtractor: (row: T) => string | number;
}

export function DataTable<T>({
  columns,
  data,
  keyExtractor
}: DataTableProps<T>) {
  return (
    <Table>
      <TableHeader>
        <TableRow>
          {columns.map(col => (
            <TableHead key={String(col.key)}>{col.header}</TableHead>
          ))}
        </TableRow>
      </TableHeader>
      <TableBody>
        {data.map(row => (
          <TableRow key={keyExtractor(row)}>
            {columns.map(col => (
              <TableCell key={String(col.key)}>
                {col.render
                  ? col.render(row)
                  : String(
                      (row as Record<string, unknown>)[
                        col.key as string
                      ] ?? ""
                    )}
              </TableCell>
            ))}
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}
```

---
