import { cn } from "@/lib/utils";

function Skeleton({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      aria-busy="true"
      aria-label="Loading content"
      className={cn("animate-pulse rounded-md bg-accent dark:bg-accent/60", className)}
      data-slot="skeleton"
      role="status"
      {...props}
    />
  );
}

export { Skeleton };
