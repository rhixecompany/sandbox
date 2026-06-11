"use client";

import { Grid, List, Search, X } from "lucide-react";
import { useState } from "react";

import { Button } from "@/components/ui/button";

import type { BookmarkFilter } from "@/types/bookmark";

const BOOKMARK_STATUSES = [
  { value: "", label: "All Statuses" },
  { value: "Reading", label: "Reading" },
  { value: "Plan to Read", label: "Plan to Read" },
  { value: "Completed", label: "Completed" },
  { value: "On Hold", label: "On Hold" },
  { value: "Dropped", label: "Dropped" },
];

const SORT_OPTIONS = [
  { value: "recent", label: "Recently Updated" },
  { value: "progress", label: "Progress" },
  { value: "title", label: "Title" },
  { value: "added", label: "Date Added" },
];

interface BookmarksFilterProps {
  activeFilters?: BookmarkFilter;
  onFilterChange: (filter: BookmarkFilter) => void;
  onViewModeChange: (mode: "grid" | "list") => void;
  viewMode: "grid" | "list";
}

export function BookmarksFilter({
  onFilterChange,
  viewMode,
  onViewModeChange,
  activeFilters = {},
}: BookmarksFilterProps) {
  const [searchQuery, setSearchQuery] = useState(activeFilters.search || "");
  const [selectedStatus, setSelectedStatus] = useState(activeFilters.status || "");
  const [sortBy, setSortBy] = useState<"added" | "progress" | "recent" | "title">(activeFilters.sortBy || "recent");

  const handleSearchChange = (query: string) => {
    setSearchQuery(query);
    onFilterChange({
      search: query,
      status: selectedStatus,
      sortBy,
      view: viewMode,
    });
  };

  const handleStatusChange = (status: string) => {
    setSelectedStatus(status);
    onFilterChange({
      search: searchQuery,
      status: status || undefined,
      sortBy,
      view: viewMode,
    });
  };

  const handleSortChange = (sort: "added" | "progress" | "recent" | "title") => {
    setSortBy(sort);
    onFilterChange({
      search: searchQuery,
      status: selectedStatus,
      sortBy: sort,
      view: viewMode,
    });
  };

  const handleClearFilters = () => {
    setSearchQuery("");
    setSelectedStatus("");
    setSortBy("recent");
    onFilterChange({
      search: "",
      status: undefined,
      sortBy: "recent",
      view: viewMode,
    });
  };

  const hasActiveFilters = searchQuery.length > 0 || selectedStatus.length > 0 || sortBy !== "recent";

  return (
    <div className="space-y-4">
      {/* Search Bar */}
      <div className="relative">
        <Search className="absolute top-1/2 left-3 h-4 w-4 -translate-y-1/2 text-gray-400" />
        <input
          className="w-full rounded-lg border border-gray-200 py-2 pr-4 pl-10 focus:ring-2 focus:ring-blue-500 focus:outline-none dark:border-gray-700 dark:bg-gray-800 dark:text-white"
          onChange={(e) => handleSearchChange(e.target.value)}
          placeholder="Search bookmarks..."
          type="text"
          value={searchQuery}
        />
      </div>

      {/* Filter and Sort Controls */}
      <div className="flex flex-col gap-4 lg:flex-row lg:items-center lg:justify-between">
        <div className="flex flex-wrap gap-2">
          {/* Status Filter */}
          <select
            className="rounded-lg border border-gray-200 bg-white px-3 py-2 text-sm focus:ring-2 focus:ring-blue-500 focus:outline-none dark:border-gray-700 dark:bg-gray-800 dark:text-white"
            onChange={(e) => handleStatusChange(e.target.value)}
            value={selectedStatus}
          >
            {BOOKMARK_STATUSES.map((status) => (
              <option key={status.value} value={status.value}>
                {status.label}
              </option>
            ))}
          </select>

          {/* Sort */}
          <select
            className="rounded-lg border border-gray-200 bg-white px-3 py-2 text-sm focus:ring-2 focus:ring-blue-500 focus:outline-none dark:border-gray-700 dark:bg-gray-800 dark:text-white"
            onChange={(e) => handleSortChange(e.target.value as "added" | "progress" | "recent" | "title")}
            value={sortBy}
          >
            {SORT_OPTIONS.map((option) => (
              <option key={option.value} value={option.value}>
                {option.label}
              </option>
            ))}
          </select>

          {/* Clear Filters */}
          {hasActiveFilters && (
            <Button className="gap-2" onClick={handleClearFilters} size="sm" variant="outline">
              <X className="h-4 w-4" />
              Clear
            </Button>
          )}
        </div>

        {/* View Toggle */}
        <div className="flex gap-1 rounded-lg border border-gray-200 bg-gray-50 p-1 dark:border-gray-700 dark:bg-gray-800">
          <Button
            className="h-8 w-8 p-0"
            onClick={() => onViewModeChange("grid")}
            size="sm"
            title="Grid view"
            variant={viewMode === "grid" ? "default" : "ghost"}
          >
            <Grid className="h-4 w-4" />
          </Button>
          <Button
            className="h-8 w-8 p-0"
            onClick={() => onViewModeChange("list")}
            size="sm"
            title="List view"
            variant={viewMode === "list" ? "default" : "ghost"}
          >
            <List className="h-4 w-4" />
          </Button>
        </div>
      </div>
    </div>
  );
}
