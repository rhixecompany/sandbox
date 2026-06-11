/**
 * Search Input Component
 * Client component with debounced search input
 */

"use client";

import { Search, X } from "lucide-react";
import { useRouter, useSearchParams } from "next/navigation";
import { useTransition } from "react";

import { Input } from "@/components/ui/input";

interface SearchInputProps {
  initialQuery?: string;
}

export default function SearchInput({ initialQuery = "" }: SearchInputProps) {
  const router = useRouter();
  const searchParams = useSearchParams();
  const [isPending, startTransition] = useTransition();

  const handleSearch = (query: string) => {
    const params = new URLSearchParams(searchParams);

    if (query.trim()) {
      params.set("q", query.trim());
      params.set("page", "0");
    } else {
      params.delete("q");
    }

    startTransition(() => {
      router.push(`/search?${params.toString()}`);
    });
  };

  const handleClear = () => {
    handleSearch("");
  };

  return (
    <div className="relative">
      <Search className="absolute top-3 left-3 h-5 w-5 text-muted-foreground dark:text-muted-foreground/70" />
      <Input
        className="pr-10 pl-10 dark:border-border/50 dark:bg-background dark:placeholder:text-muted-foreground/70"
        defaultValue={initialQuery}
        disabled={isPending}
        onChange={(e) => handleSearch(e.target.value)}
        placeholder="Search by title, description, author..."
        type="search"
      />
      {initialQuery && (
        <button
          aria-label="Clear search"
          className="absolute top-3 right-3 text-muted-foreground hover:text-foreground dark:text-muted-foreground/70 dark:hover:text-foreground"
          onClick={handleClear}
        >
          <X className="h-5 w-5" />
        </button>
      )}
    </div>
  );
}
