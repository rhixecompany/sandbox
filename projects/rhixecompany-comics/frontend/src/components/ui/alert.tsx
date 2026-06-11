import { cva, type VariantProps } from "class-variance-authority";
import * as React from "react";

import { cn } from "@/lib/utils";

const alertVariants = cva(
  "relative grid w-full grid-cols-[0_1fr] items-start gap-y-0.5 rounded-lg border px-4 py-3 text-sm transition-colors has-[>svg]:grid-cols-[calc(var(--spacing)*4)_1fr] has-[>svg]:gap-x-3 [&>svg]:size-4 [&>svg]:translate-y-0.5 [&>svg]:text-current",
  {
    variants: {
      variant: {
        default: "bg-card dark:bg-card border-border dark:border-border text-card-foreground dark:text-card-foreground",
        destructive:
          "bg-destructive/10 dark:bg-destructive/20 border-destructive/50 dark:border-destructive/60 text-destructive dark:text-destructive-foreground *:data-[slot=alert-description]:text-destructive/90 dark:*:data-[slot=alert-description]:text-destructive-foreground/90 [&>svg]:text-destructive dark:[&>svg]:text-destructive-foreground",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
);

function Alert({ className, variant, ...props }: React.ComponentProps<"div"> & VariantProps<typeof alertVariants>) {
  return <div className={cn(alertVariants({ variant }), className)} data-slot="alert" role="alert" {...props} />;
}

function AlertTitle({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      className={cn("col-start-2 line-clamp-1 min-h-4 font-medium tracking-tight", className)}
      data-slot="alert-title"
      {...props}
    />
  );
}

function AlertDescription({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      className={cn(
        "col-start-2 grid justify-items-start gap-1 text-sm text-muted-foreground [&_p]:leading-relaxed",
        className
      )}
      data-slot="alert-description"
      {...props}
    />
  );
}

export { Alert, AlertDescription, AlertTitle };
