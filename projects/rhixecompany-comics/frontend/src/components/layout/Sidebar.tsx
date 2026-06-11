"use client";

import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Separator } from "@/components/ui/separator";
import { ScrollArea } from "@/components/ui/scroll-area";

interface FilterOption {
  value: string;
  label: string;
}

interface FilterGroup {
  id: string;
  label: string;
  options: FilterOption[];
}

interface SidebarProps {
  filters: FilterGroup[];
  activeFilters: Record<string, string>;
  onFilterChange: (key: string, value: string) => void;
  className?: string;
}

export function Sidebar({ filters, activeFilters, onFilterChange, className }: SidebarProps) {
  return (
    <aside className={cn("w-full border-r bg-background md:w-56 lg:w-64", className)}>
      <ScrollArea className="h-full py-4">
        <div className="px-3">
          <h2 className="mb-2 px-2 text-lg font-semibold tracking-tight">Filters</h2>
          <Separator className="mb-4" />
          {filters.map((group) => (
            <div key={group.id} className="mb-4">
              <h3 className="mb-2 px-2 text-sm font-medium text-muted-foreground">
                {group.label}
              </h3>
              <div className="flex flex-col gap-1">
                <Button
                  variant="ghost"
                  size="sm"
                  className={cn(
                    "justify-start font-normal",
                    !activeFilters[group.id] && "bg-accent",
                  )}
                  onClick={() => onFilterChange(group.id, "")}
                >
                  All
                </Button>
                {group.options.map((option) => (
                  <Button
                    key={option.value}
                    variant="ghost"
                    size="sm"
                    className={cn(
                      "justify-start font-normal",
                      activeFilters[group.id] === option.value && "bg-accent",
                    )}
                    onClick={() => onFilterChange(group.id, option.value)}
                  >
                    {option.label}
                  </Button>
                ))}
              </div>
            </div>
          ))}
        </div>
      </ScrollArea>
    </aside>
  );
}
