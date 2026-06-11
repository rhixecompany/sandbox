"use client";

import { ChevronDown, Filter, X } from "lucide-react";
import { useRouter, useSearchParams } from "next/navigation";
import { useState, useTransition } from "react";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Slider } from "@/components/ui/slider";

import { SearchSuggestionsDropdown } from "./search-suggestions-dropdown";

const COMIC_STATUS = ["Ongoing", "Hiatus", "Completed", "Dropped", "Season End", "Coming Soon"];

const SORT_OPTIONS = [
  { label: "Relevance", value: "relevance" },
  { label: "Rating (High to Low)", value: "rating" },
  { label: "Recently Updated", value: "updated" },
];

interface AdvancedSearchFormProps {
  authors?: Array<{ id: string; name: string }>;
  genres?: Array<{ id: string; name: string }>;
}

export function AdvancedSearchForm({ genres = [], authors = [] }: AdvancedSearchFormProps) {
  const router = useRouter();
  const searchParams = useSearchParams();
  const [isPending, startTransition] = useTransition();

  // Form state from URL params
  const [query, setQuery] = useState(searchParams.get("q") || "");
  const [status, setStatus] = useState(searchParams.get("status") || "all");
  const [sortBy, setSortBy] = useState(searchParams.get("sortBy") || "relevance");
  const [minRating, setMinRating] = useState(parseInt(searchParams.get("minRating") || "0"));
  const [maxRating, setMaxRating] = useState(parseInt(searchParams.get("maxRating") || "5"));
  const [selectedGenres, setSelectedGenres] = useState<string[]>(searchParams.getAll("genres") || []);
  const [selectedAuthors, setSelectedAuthors] = useState<string[]>(searchParams.getAll("authors") || []);
  const [showAdvanced, setShowAdvanced] = useState(false);
  const [dropdownOpen, setDropdownOpen] = useState(false);

  // Handle search form submission
  const handleSearch = () => {
    const params = new URLSearchParams();

    if (query.trim()) params.set("q", query.trim());
    if (status && status !== "all") params.set("status", status);
    if (sortBy !== "relevance") params.set("sortBy", sortBy);
    if (minRating > 0) params.set("minRating", String(minRating));
    if (maxRating < 5) params.set("maxRating", String(maxRating));

    for (const g of selectedGenres) params.append("genres", g);
    for (const a of selectedAuthors) params.append("authors", a);

    params.set("page", "1");

    startTransition(() => {
      router.push(`/search?${params.toString()}`);
    });
  };

  // Handle Enter key in search input
  const handleKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
      setDropdownOpen(false);
      handleSearch();
    } else if (e.key === "Escape") {
      setDropdownOpen(false);
    }
  };

  // Clear all filters
  const handleClearFilters = () => {
    setQuery("");
    setStatus("");
    setSortBy("relevance");
    setMinRating(0);
    setMaxRating(5);
    setSelectedGenres([]);
    setSelectedAuthors([]);
    setShowAdvanced(false);

    startTransition(() => {
      router.push("/search");
    });
  };

  const hasActiveFilters =
    query || status || minRating > 0 || maxRating < 5 || selectedGenres.length > 0 || selectedAuthors.length > 0;

  return (
    <div
      className="w-full space-y-6 rounded-lg border bg-card/50 p-6 backdrop-blur dark:bg-card/50"
      data-testid="advanced-search-form"
      id="search-form"
    >
      {/* Main Search Input */}
      <div className="relative space-y-2">
        <Label className="dark:text-foreground" htmlFor="search-query">
          Search Comics
        </Label>
        <Input
          className="dark:border-border/50 dark:bg-background dark:text-foreground dark:placeholder:text-muted-foreground/70"
          disabled={isPending}
          id="search-query"
          onChange={(e) => {
            setQuery(e.target.value);
            // Auto-open dropdown when query length >= 2
            if (e.target.value.length >= 2) {
              setDropdownOpen(true);
            }
          }}
          onFocus={() => {
            // Open dropdown on focus if query is long enough
            if (query.length >= 2) {
              setDropdownOpen(true);
            }
          }}
          onKeyPress={handleKeyPress}
          placeholder="Search by title, description, author..."
          value={query}
        />
        {/* Search Suggestions Dropdown */}
        <SearchSuggestionsDropdown
          isOpen={dropdownOpen}
          onOpenChange={setDropdownOpen}
          onSelect={(suggestion: string) => {
            setQuery(suggestion);
            setDropdownOpen(false);
          }}
          query={query}
        />
      </div>

      {/* Quick Filters Row */}
      <div className="grid grid-cols-1 gap-4 md:grid-cols-3">
        {/* Status Filter */}
        <div className="space-y-2">
          <Label className="text-sm dark:text-foreground" htmlFor="status-filter">
            Status
          </Label>
          <Select onValueChange={setStatus} value={status}>
            <SelectTrigger className="dark:border-border/50 dark:bg-background dark:text-foreground" id="status-filter">
              <SelectValue placeholder="All statuses" />
            </SelectTrigger>
            <SelectContent className="dark:border-border dark:bg-background">
              <SelectItem value="all">All statuses</SelectItem>
              {COMIC_STATUS.map((s) => (
                <SelectItem key={s} value={s}>
                  {s}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div>

        {/* Sort Order */}
        <div className="space-y-2">
          <Label className="text-sm dark:text-foreground" htmlFor="sort-filter">
            Sort by
          </Label>
          <Select onValueChange={setSortBy} value={sortBy}>
            <SelectTrigger className="dark:border-border/50 dark:bg-background dark:text-foreground" id="sort-filter">
              <SelectValue />
            </SelectTrigger>
            <SelectContent className="dark:border-border dark:bg-background">
              {SORT_OPTIONS.map((opt) => (
                <SelectItem key={opt.value} value={opt.value}>
                  {opt.label}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div>

        {/* Min Rating */}
        <div className="space-y-2">
          <Label className="text-sm dark:text-foreground" htmlFor="min-rating">
            Min Rating: {minRating}★
          </Label>
          <Slider
            className="dark:text-primary"
            id="min-rating"
            max={5}
            min={0}
            onValueChange={(val) => {
              const newMin = val[0];
              if (newMin <= maxRating) {
                setMinRating(newMin);
              }
            }}
            step={0.5}
            value={[minRating]}
          />
        </div>
      </div>

      {/* Advanced Filters Toggle */}
      <Button
        className="w-full gap-2 dark:border-border/50 dark:text-foreground dark:hover:bg-accent/50"
        onClick={() => setShowAdvanced(!showAdvanced)}
        size="sm"
        variant="outline"
      >
        <Filter className="h-4 w-4" />
        {showAdvanced ? "Hide" : "Show"} Advanced Filters
        <ChevronDown className={`ml-auto h-4 w-4 transition-transform ${showAdvanced ? "rotate-180" : ""}`} />
      </Button>

      {/* Advanced Filters Section */}
      {showAdvanced && (
        <div className="space-y-4 border-t pt-4 dark:border-border/50">
          {/* Max Rating */}
          <div className="space-y-2">
            <Label className="text-sm dark:text-foreground" htmlFor="max-rating">
              Max Rating: {maxRating}★
            </Label>
            <Slider
              className="dark:text-primary"
              id="max-rating"
              max={5}
              min={0}
              onValueChange={(val) => {
                const newMax = val[0];
                if (newMax >= minRating) {
                  setMaxRating(newMax);
                }
              }}
              step={0.5}
              value={[maxRating]}
            />
          </div>

          {/* Genres Multi-Select */}
          {genres.length > 0 && (
            <div className="space-y-2">
              <Label className="text-sm dark:text-foreground">Genres</Label>
              <div className="space-y-2 rounded border p-3 dark:border-border/50">
                {genres.map((genre) => (
                  <label className="flex cursor-pointer items-center gap-2 text-sm dark:text-foreground" key={genre.id}>
                    <input
                      checked={selectedGenres.includes(genre.id)}
                      className="h-4 w-4 dark:accent-primary"
                      onChange={(e) => {
                        if (e.target.checked) {
                          setSelectedGenres([...selectedGenres, genre.id]);
                        } else {
                          setSelectedGenres(selectedGenres.filter((g) => g !== genre.id));
                        }
                      }}
                      type="checkbox"
                    />
                    {genre.name}
                  </label>
                ))}
              </div>
            </div>
          )}

          {/* Authors Multi-Select */}
          {authors.length > 0 && (
            <div className="space-y-2">
              <Label className="text-sm dark:text-foreground">Authors</Label>
              <div className="max-h-48 space-y-2 overflow-y-auto rounded border p-3 dark:border-border/50">
                {authors.map((author) => (
                  <label
                    className="flex cursor-pointer items-center gap-2 text-sm dark:text-foreground"
                    key={author.id}
                  >
                    <input
                      checked={selectedAuthors.includes(author.id)}
                      className="h-4 w-4 dark:accent-primary"
                      onChange={(e) => {
                        if (e.target.checked) {
                          setSelectedAuthors([...selectedAuthors, author.id]);
                        } else {
                          setSelectedAuthors(selectedAuthors.filter((a) => a !== author.id));
                        }
                      }}
                      type="checkbox"
                    />
                    {author.name}
                  </label>
                ))}
              </div>
            </div>
          )}
        </div>
      )}

      {/* Action Buttons */}
      <div className="flex gap-2">
        <Button className="flex-1 dark:bg-primary dark:hover:bg-primary/90" disabled={isPending} onClick={handleSearch}>
          {isPending ? "Searching..." : "Search"}
        </Button>
        {hasActiveFilters && (
          <Button
            className="dark:border-border/50 dark:text-foreground dark:hover:bg-accent/50"
            disabled={isPending}
            onClick={handleClearFilters}
            variant="outline"
          >
            <X className="h-4 w-4" />
          </Button>
        )}
      </div>
    </div>
  );
}
