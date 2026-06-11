/**
 * Core Web Vitals & Performance Metrics
 * Reference: Google Core Web Vitals, Next.js Performance Best Practices
 *
 * Track and monitor performance metrics for optimization
 */

import { getEnv } from "appConfig";

/**
 * Core Web Vitals thresholds
 * https://web.dev/vitals/
 */
export const CORE_WEB_VITALS_THRESHOLDS = {
  // Largest Contentful Paint: time until largest visual element is visible
  // Good: < 2.5s, Needs improvement: 2.5s-4s, Poor: > 4s
  LCP: {
    GOOD: 2500, // 2.5 seconds
    NEEDS_IMPROVEMENT: 4000, // 4.0 seconds
  },

  // First Input Delay: time from user input to browser response
  // Good: < 100ms, Needs improvement: 100-300ms, Poor: > 300ms
  FID: {
    GOOD: 100, // 100 milliseconds
    NEEDS_IMPROVEMENT: 300, // 300 milliseconds
  },

  // Cumulative Layout Shift: visual stability metric
  // Good: < 0.1, Needs improvement: 0.1-0.25, Poor: > 0.25
  CLS: {
    GOOD: 0.1,
    NEEDS_IMPROVEMENT: 0.25,
  },

  // First Contentful Paint: time until first content is visible
  // Good: < 1.8s, Needs improvement: 1.8-3s, Poor: > 3s
  FCP: {
    GOOD: 1800, // 1.8 seconds
    NEEDS_IMPROVEMENT: 3000, // 3.0 seconds
  },

  // Time to Interactive: when page is fully interactive
  // Good: < 3.8s, Needs improvement: 3.8-7.3s, Poor: > 7.3s
  TTI: {
    GOOD: 3800, // 3.8 seconds
    NEEDS_IMPROVEMENT: 7300, // 7.3 seconds
  },

  // Interaction to Next Paint: responsiveness to user input
  // Good: < 200ms, Needs improvement: 200-500ms, Poor: > 500ms
  INP: {
    GOOD: 200, // 200 milliseconds
    NEEDS_IMPROVEMENT: 500, // 500 milliseconds
  },
} as const;

/**
 * Performance budget for ComicWise application
 * These are targets we aim to achieve and maintain
 */
export const PERFORMANCE_BUDGET = {
  // JavaScript bundle size (gzip)
  jsBundle: {
    main: "200kb", // Main bundle
    vendor: "300kb", // Vendor bundle (Radix, React Query, etc.)
  },

  // CSS bundle size
  cssBundle: "50kb", // Main CSS

  // Image optimization
  images: {
    maxSize: "500kb", // Max size before compression
    formats: ["avif", "webp", "jpeg"],
  },

  // Build time
  buildTime: {
    development: "30s", // Turbopack dev build
    production: "45s", // Full production build
  },

  // Runtime performance
  firstContentfulPaint: "1.8s",
  largestContentfulPaint: "2.5s",
  cumulativeLayoutShift: "0.1",
} as const;

/**
 * Performance monitoring API
 * Client-side measurement of Core Web Vitals
 */
export class PerformanceMonitor {
  private metrics: Map<string, number> = new Map();

  /**
   * Measure Long Tasks (JavaScript execution blocking user input)
   * Triggered when task takes > 50ms
   */
  public measureLongTasks(): void {
    if ("PerformanceObserver" in window) {
      try {
        const observer = new PerformanceObserver((list) => {
          for (const entry of list.getEntries()) {
            console.warn(`Long Task: ${entry.name} took ${entry.duration}ms`, {
              startTime: entry.startTime,
              duration: entry.duration,
            });
          }
        });

        observer.observe({ entryTypes: ["longtask"] });
      } catch (error) {
        console.debug("Long Task API not supported", error);
      }
    }
  }

  /**
   * Measure Resource Timing (network requests)
   * Identifies slow resources affecting page load
   */
  public measureResourceTiming(): void {
    if ("performance" in window && "getEntriesByType" in window.performance) {
      const resources = window.performance.getEntriesByType("resource") as PerformanceResourceTiming[];

      for (const resource of resources) {
        if (resource.duration > 1000) {
          console.warn(`Slow resource: ${resource.name} took ${resource.duration.toFixed(0)}ms`, {
            size: (resource.transferSize || 0) / 1024,
            cached: (resource.transferSize || 0) === 0,
          });
        }
      }
    }
  }

  /**
   * Report metric to analytics
   * Send Core Web Vitals to monitoring service
   */
  public reportMetric(name: string, value: number, rating: string): void {
    // Log to console in development
    if (getEnv().NODE_ENV === "development") {
      console.log(`📊 ${name}: ${value.toFixed(0)}`, { rating });
    }

    // TODO: Send to analytics service (Sentry, Vercel Analytics, etc.)
    // This would be implemented once error tracking is configured
  }

  /**
   * Get metric rating based on thresholds
   */
  private getRating(
    metricName: keyof typeof CORE_WEB_VITALS_THRESHOLDS,
    value: number
  ): "good" | "needs-improvement" | "poor" {
    const thresholds = CORE_WEB_VITALS_THRESHOLDS[metricName as never] as Record<string, number>;

    if (value <= thresholds.GOOD) return "good";
    if (value <= thresholds.NEEDS_IMPROVEMENT) return "needs-improvement";
    return "poor";
  }

  /**
   * Measure and report all Core Web Vitals
   * Should be called after page load completes
   */
  public measureAllMetrics(): void {
    // LCP (Largest Contentful Paint)
    if ("PerformanceObserver" in window) {
      try {
        const lcpObserver = new PerformanceObserver((list) => {
          const entries = list.getEntries();
          const lastEntry = entries[entries.length - 1] as unknown as {
            loadTime?: number;
            renderTime?: number;
            startTime: number;
          };
          const value = (lastEntry.renderTime || lastEntry.loadTime) ?? lastEntry.startTime;
          this.metrics.set("LCP", value);
          this.reportMetric("LCP", value, this.getRating("LCP", value));
        });

        lcpObserver.observe({ entryTypes: ["largest-contentful-paint"] });
      } catch (error) {
        console.debug("LCP measurement not available", error);
      }
    }

    // FID/INP (Input Delay)
    if ("PerformanceObserver" in window) {
      try {
        const fidObserver = new PerformanceObserver((list) => {
          const entries = list.getEntries();
          if (entries.length > 0) {
            const firstEntry = entries[0] as PerformanceEntryWithProcessingDuration;
            const value = firstEntry.processingDuration;
            this.metrics.set("FID", value);
            this.reportMetric("FID", value, this.getRating("FID", value));
          }
        });

        fidObserver.observe({ entryTypes: ["first-input", "pointer"] });
      } catch (error) {
        console.debug("FID measurement not available", error);
      }
    }

    // CLS (Cumulative Layout Shift)
    if ("PerformanceObserver" in window) {
      try {
        let clsValue = 0;
        const clsObserver = new PerformanceObserver((list) => {
          for (const entry of list.getEntries()) {
            if (!(entry as LayoutShift).hadRecentInput) {
              clsValue += (entry as LayoutShift).value;
              this.metrics.set("CLS", clsValue);
              this.reportMetric("CLS", clsValue, this.getRating("CLS", clsValue));
            }
          }
        });

        clsObserver.observe({ entryTypes: ["layout-shift"] });
      } catch (error) {
        console.debug("CLS measurement not available", error);
      }
    }

    // FCP (First Contentful Paint)
    if ("performance" in window && "getEntriesByName" in window.performance) {
      const fcpEntry = window.performance.getEntriesByName("first-contentful-paint")[0] as
        | PerformanceEntryWithStartTime
        | undefined;
      if (fcpEntry) {
        const value = fcpEntry.startTime;
        this.metrics.set("FCP", value);
        this.reportMetric("FCP", value, this.getRating("FCP", value));
      }
    }
  }

  /**
   * Get all collected metrics
   */
  public getMetrics(): Record<string, number> {
    return Object.fromEntries(this.metrics);
  }
}

// Types for Performance API
interface LayoutShift extends PerformanceEntry {
  hadRecentInput: boolean;
  value: number;
}

interface PerformanceEntryWithProcessingDuration extends PerformanceEntry {
  processingDuration: number;
}

interface PerformanceEntryWithStartTime extends PerformanceEntry {
  startTime: number;
}

/**
 * Initialize performance monitoring
 * Call this once on app load to start tracking metrics
 */
export function initializePerformanceMonitoring(): void {
  if (typeof window === "undefined") return;

  const monitor = new PerformanceMonitor();

  // Measure metrics once page is fully loaded
  if (document.readyState === "complete") {
    monitor.measureAllMetrics();
    monitor.measureLongTasks();
    monitor.measureResourceTiming();
  } else {
    window.addEventListener("load", () => {
      monitor.measureAllMetrics();
      monitor.measureLongTasks();
      monitor.measureResourceTiming();
    });
  }
}
