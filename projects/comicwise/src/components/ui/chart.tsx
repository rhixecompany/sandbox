"use client";

import * as React from "react";
import * as RechartsPrimitive from "recharts";

import { cn } from "@/lib/utils";

// Minimal, well-typed chart primitives used across the app.
export type ChartConfig = Record<string, { color?: string; icon?: React.ComponentType; label?: React.ReactNode }>;

type ChartContextProps = { config: ChartConfig };
const ChartContext = React.createContext<ChartContextProps | null>(null);

export function useChart() {
  const ctx = React.useContext(ChartContext);
  if (!ctx) throw new Error("useChart must be used within a <ChartContainer />");
  return ctx;
}

export function ChartContainer({
  id,
  className,
  children,
  config,
  ...props
}: React.ComponentProps<"div"> & {
  children?: React.ReactNode;
  config: ChartConfig;
}) {
  const uniqueId = React.useId();
  const chartId = `chart-${String(id ?? uniqueId).replaceAll(":", "")}`;

  // Avoid rendering Recharts' ResponsiveContainer on the server or before the
  // component has mounted. ResponsiveContainer measures its container and can
  // emit warnings like "width(-1) and height(-1) should be greater than 0"
  // during static prerender. Defer actual chart rendering until after mount.
  const [isMounted, setIsMounted] = React.useState(false);
  React.useEffect(() => {
    setIsMounted(true);
  }, []);

  return (
    <ChartContext.Provider value={{ config }}>
      <div className={cn(className)} data-chart={chartId} data-slot="chart" {...props}>
        {isMounted ? <RechartsPrimitive.ResponsiveContainer>{children}</RechartsPrimitive.ResponsiveContainer> : null}
      </div>
    </ChartContext.Provider>
  );
}

export const ChartStyle = ({ id: _id }: { id: string }) => {
  void _id;
  return null;
};

export const ChartTooltip = RechartsPrimitive.Tooltip;
export function ChartTooltipContent(_props: Record<string, unknown>) {
  // Keep this minimal: Recharts provides default tooltip rendering.
  // Use the passed props to avoid unused-variable lint warnings in callers.
  void _props;
  return null;
}

export const ChartLegend = RechartsPrimitive.Legend;
export function ChartLegendContent(_props: Record<string, unknown>) {
  // Avoid unused variable lint warning
  void _props;
  return null;
}

export { ChartContainer as default };
