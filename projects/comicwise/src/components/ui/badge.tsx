import { cva, type VariantProps } from "class-variance-authority";
import { Slot } from "radix-ui";
import * as React from "react";

import { cn } from "@/lib/utils";

const badgeVariants = cva(
  "inline-flex w-fit shrink-0 items-center justify-center gap-1 overflow-hidden rounded-full border border-transparent px-2 py-0.5 text-xs font-medium whitespace-nowrap transition-[color,box-shadow] focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 aria-invalid:border-destructive aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 [&>svg]:pointer-events-none [&>svg]:size-3 [&>svg]:text-current",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground dark:bg-primary/80 dark:text-primary-foreground",
        secondary: "bg-secondary text-secondary-foreground dark:bg-secondary/70 dark:text-secondary-foreground",
        destructive:
          "bg-destructive dark:bg-destructive/60 dark:text-destructive-foreground [a&]:hover:bg-destructive/90 dark:[a&]:hover:bg-destructive/50 focus-visible:ring-destructive/20 dark:focus-visible:ring-destructive/40 text-white",
        outline:
          "border-border text-foreground dark:border-border dark:text-foreground [a&]:hover:bg-accent dark:[a&]:hover:bg-accent/20 [a&]:hover:text-accent-foreground",
        ghost:
          "text-foreground dark:text-foreground [a&]:hover:bg-accent dark:[a&]:hover:bg-accent/20 [a&]:hover:text-accent-foreground",
        link: "text-primary dark:text-primary dark:[a&]:hover:text-primary/80 underline-offset-4 [a&]:hover:underline",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
);

function Badge({
  className,
  variant = "default",
  asChild = false,
  ...props
}: React.ComponentProps<"span"> & VariantProps<typeof badgeVariants> & { asChild?: boolean }) {
  const Comp = asChild ? Slot.Root : "span";

  return (
    <Comp className={cn(badgeVariants({ variant }), className)} data-slot="badge" data-variant={variant} {...props} />
  );
}

export { Badge, badgeVariants };
