import { BookOpen } from "lucide-react";
import Link from "next/link";

import { Button } from "@/components/ui/button";

interface EmptyStateProps {
  action?: {
    href?: string;
    label: string;
    onClick?: () => void;
  };
  description?: string;
  icon?: React.ReactNode;
  title?: string;
}

/**
 * Empty state component
 * Displays helpful message when no content is available
 */
export function EmptyState({
  title = "No comics found",
  description = "Try adjusting your filters or search terms",
  icon,
  action,
}: EmptyStateProps) {
  return (
    <div className="flex min-h-[300px] flex-col items-center justify-center rounded-lg border border-dashed p-8 text-center">
      {icon ? <div className="mb-4">{icon}</div> : <BookOpen className="mb-4 h-12 w-12 text-muted-foreground" />}
      <h3 className="mb-2 text-lg font-semibold">{title}</h3>
      <p className="mb-6 max-w-sm text-sm text-muted-foreground">{description}</p>
      {action &&
        (action.href ? (
          <Button asChild>
            <Link href={action.href as never}>{action.label}</Link>
          </Button>
        ) : (
          <Button onClick={action.onClick}>{action.label}</Button>
        ))}
    </div>
  );
}
