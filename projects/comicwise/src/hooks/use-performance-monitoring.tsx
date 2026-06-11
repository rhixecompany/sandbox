"use client";

/**
 * usePerformanceMonitoring Hook
 * Measures Core Web Vitals and reports metrics in client components
 *
 * Reference: Next.js 16 Performance Optimization
 */

import { useEffect, useState } from "react";

import { CORE_WEB_VITALS_THRESHOLDS, PerformanceMonitor } from "@/lib/performance-metrics";

interface UsePerformanceMonitoringOptions {
  debug?: boolean;
  onMetrics?: (metrics: Record<string, number>) => void;
}

/**
 * Hook to measure and monitor Core Web Vitals
 *
 * @param options Configuration options
 * @returns Object with metrics and monitoring status
 *
 * @example
 * ```tsx
 * export function RootLayout({ children }: { children: React.ReactNode }) {
 *   usePerformanceMonitoring({ debug: true });
 *   return <>{children}</>;
 * }
 * ```
 */
export function usePerformanceMonitoring(options: UsePerformanceMonitoringOptions = {}): {
  getHealthStatus: () => "critical" | "good" | "warning";
  isMonitoring: boolean;
  metrics: Record<string, number>;
} {
  const { onMetrics, debug = false } = options;
  const [metrics, setMetrics] = useState<Record<string, number>>({});

  useEffect(() => {
    // Initialize monitor once
    const monitor = new PerformanceMonitor();

    // Measure metrics when component mounts
    const timeoutId = setTimeout(() => {
      monitor.measureAllMetrics();

      // Also measure resource timing to identify slow assets
      monitor.measureResourceTiming();

      // Also identify long tasks blocking main thread
      monitor.measureLongTasks();

      // Store metrics
      const newMetrics = monitor.getMetrics();
      setMetrics(newMetrics);

      // Report to callback if provided
      if (onMetrics) {
        onMetrics(newMetrics);
      }

      if (debug) {
        console.log("📊 Performance Metrics:", newMetrics);
      }
    }, 100); // Wait 100ms for initial metrics to populate

    return () => clearTimeout(timeoutId);
  }, [onMetrics, debug]);

  /**
   * Determine overall health status based on Core Web Vitals
   */
  function getHealthStatus(): "critical" | "good" | "warning" {
    let warningCount = 0;
    let criticalCount = 0;

    // Check LCP
    if (metrics.LCP) {
      if (metrics.LCP <= CORE_WEB_VITALS_THRESHOLDS.LCP.GOOD) {
        // good
      } else if (metrics.LCP <= CORE_WEB_VITALS_THRESHOLDS.LCP.NEEDS_IMPROVEMENT) {
        warningCount++;
      } else {
        criticalCount++;
      }
    }

    // Check FID
    if (metrics.FID) {
      if (metrics.FID <= CORE_WEB_VITALS_THRESHOLDS.FID.GOOD) {
        // good
      } else if (metrics.FID <= CORE_WEB_VITALS_THRESHOLDS.FID.NEEDS_IMPROVEMENT) {
        warningCount++;
      } else {
        criticalCount++;
      }
    }

    // Check CLS
    if (metrics.CLS) {
      if (metrics.CLS <= CORE_WEB_VITALS_THRESHOLDS.CLS.GOOD) {
        // good
      } else if (metrics.CLS <= CORE_WEB_VITALS_THRESHOLDS.CLS.NEEDS_IMPROVEMENT) {
        warningCount++;
      } else {
        criticalCount++;
      }
    }

    // Determine status
    if (criticalCount > 0) return "critical";
    if (warningCount > 1) return "warning";
    return "good";
  }

  return {
    isMonitoring: true,
    metrics,
    getHealthStatus,
  };
}

/**
 * useLoadingPerformance Hook
 * Measures loading time for specific operations (data fetching, etc.)
 *
 * @example
 * ```tsx
 * function MyComponent() {
 *   const { startMeasure, endMeasure } = useLoadingPerformance('fetch-comics');
 *
 *   const handleFetch = async () => {
 *     startMeasure();
 *     const data = await fetchComics();
 *     const duration = endMeasure();
 *     console.log(`Fetch took ${duration}ms`);
 *   };
 * }
 * ```
 */
export function useLoadingPerformance(label: string): {
  endMeasure: () => number;
  startMeasure: () => void;
} {
  const startTimeRef = { current: null as null | number };

  const startMeasure = () => {
    startTimeRef.current = performance.now();
  };

  const endMeasure = (): number => {
    if (!startTimeRef.current) {
      console.warn("startMeasure not called before endMeasure");
      return 0;
    }

    const duration = performance.now() - startTimeRef.current;

    if (process.env.NODE_ENV === "development") {
      console.log(`⏱️  ${label} took ${duration.toFixed(2)}ms`);
    }

    return duration;
  };

  return { startMeasure, endMeasure };
}

/**
 * useLayoutShiftMonitor Hook
 * Monitors Cumulative Layout Shift to prevent janky UI
 *
 * @example
 * ```tsx
 * function DialogWithStableHeight() {
 *   useLayoutShiftMonitor(); // Logs any CLS > 0.1
 *   return <Dialog>...</Dialog>;
 * }
 * ```
 */
export function useLayoutShiftMonitor(): void {
  useEffect(() => {
    if (typeof window === "undefined") return;

    let clsValue = 0;

    const observer = new PerformanceObserver((list) => {
      for (const entry of list.getEntries()) {
        const layoutShift = entry as unknown as {
          hadRecentInput?: boolean;
          value?: number;
        };
        if (!layoutShift.hadRecentInput) {
          clsValue += layoutShift.value ?? 0;

          if (process.env.NODE_ENV === "development" && clsValue > 0.1) {
            console.warn(`⚠️  Cumulative Layout Shift detected: ${clsValue.toFixed(3)}`);
          }
        }
      }
    });

    try {
      observer.observe({ entryTypes: ["layout-shift"] });
    } catch {
      // LayoutShift not supported
    }

    return () => observer.disconnect();
  }, []);
}
