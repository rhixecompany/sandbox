import { Loader2Icon } from "lucide-react";

import { cn } from "@/lib/utils";

function Spinner({ className, ...props }: React.ComponentProps<"svg">) {
  return (
    <Loader2Icon
      aria-busy="true"
      aria-label="Loading"
      className={cn("size-4 animate-spin text-primary dark:text-primary-foreground", className)}
      role="status"
      {...props}
    />
  );
}

export { Spinner };
