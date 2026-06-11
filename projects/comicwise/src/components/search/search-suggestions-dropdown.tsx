"use client";

import { useEffect, useRef, useState, useTransition } from "react";

import { getSearchSuggestionsAction } from "@/actions/search.actions";
import { Popover, PopoverContent } from "@/components/ui/popover";
import { Spinner } from "@/components/ui/spinner";

interface SearchSuggestionsDropdownProps {
  isOpen: boolean;
  onOpenChange: (open: boolean) => void;
  onSelect: (suggestion: string) => void;
  query: string;
}

export function SearchSuggestionsDropdown({ query, onSelect, isOpen, onOpenChange }: SearchSuggestionsDropdownProps) {
  const [suggestions, setSuggestions] = useState<string[]>([]);
  const [isLoading, startTransition] = useTransition();
  const [selectedIndex, setSelectedIndex] = useState(-1);
  const suggestionsRef = useRef<HTMLDivElement>(null);

  // Fetch suggestions when query changes
  useEffect(() => {
    if (!query || query.length < 2) {
      return;
    }

    startTransition(async () => {
      const result = await getSearchSuggestionsAction({
        q: query,
        limit: 10,
      });

      if (result.ok && result.data) {
        setSuggestions(result.data);
        setSelectedIndex(-1);
      } else {
        setSuggestions([]);
      }
    });
  }, [query]);

  // Handle keyboard navigation
  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (!isOpen || suggestions.length === 0) return;

    switch (e.key) {
      case "ArrowDown":
        e.preventDefault();
        setSelectedIndex((prev) => (prev < suggestions.length - 1 ? prev + 1 : prev));
        break;
      case "ArrowUp":
        e.preventDefault();
        setSelectedIndex((prev) => (prev > 0 ? prev - 1 : -1));
        break;
      case "Enter":
        e.preventDefault();
        if (selectedIndex >= 0) {
          onSelect(suggestions[selectedIndex]);
          onOpenChange(false);
        }
        break;
      case "Escape":
        e.preventDefault();
        onOpenChange(false);
        setSelectedIndex(-1);
        break;
      default:
        break;
    }
  };

  // Auto-scroll selected item into view
  useEffect(() => {
    if (selectedIndex >= 0 && suggestionsRef.current) {
      const selectedElement = suggestionsRef.current.querySelector(`[data-index="${selectedIndex}"]`) as HTMLElement;

      if (selectedElement) {
        selectedElement.scrollIntoView({ block: "nearest" });
      }
    }
  }, [selectedIndex]);

  if (!isOpen || !query || query.length < 2) {
    return null;
  }

  return (
    <Popover onOpenChange={onOpenChange} open={isOpen}>
      <PopoverContent
        align="start"
        className="w-64 p-0 dark:border-border dark:bg-background"
        onKeyDown={handleKeyDown}
      >
        <div className="max-h-48 overflow-y-auto rounded-md border dark:border-border/50" ref={suggestionsRef}>
          {isLoading ? (
            <div className="flex items-center justify-center py-4 dark:text-foreground">
              <Spinner className="h-4 w-4" />
            </div>
          ) : suggestions.length === 0 ? (
            <div className="px-4 py-2 text-center text-sm dark:text-muted-foreground">No suggestions found</div>
          ) : (
            <div className="space-y-1 p-1">
              {suggestions.map((suggestion, index) => (
                <button
                  className={`w-full rounded px-3 py-2 text-left text-sm transition-colors dark:text-foreground dark:hover:bg-accent/50 ${
                    selectedIndex === index ? "dark:bg-accent bg-accent" : "hover:bg-accent/30"
                  }`}
                  data-index={index}
                  key={`${suggestion}-${index}`}
                  onClick={() => {
                    onSelect(suggestion);
                    onOpenChange(false);
                  }}
                  onMouseEnter={() => setSelectedIndex(index)}
                >
                  {suggestion}
                </button>
              ))}
            </div>
          )}
        </div>
      </PopoverContent>
    </Popover>
  );
}
