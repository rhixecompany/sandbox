/**
 * System Information Resource
 *
 * Exposes OS, platform, memory, CPU, and runtime details as a
 * read-only MCP resource under mcp://system/info.
 */

import { hostname, platform, release, type, arch, totalmem, freemem, uptime, cpus as osCpus } from "os";
import { version as nodeVersion } from "process";

/**
 * Collect system information with defensive fallbacks.
 */
function gatherSystemInfo(): Record<string, unknown> {
  const cpuInfo = osCpus();
  return {
    hostname: hostname(),
    platform: platform(),
    osType: type(),
    osRelease: release(),
    architecture: arch(),
    nodeVersion,
    uptimeSeconds: uptime(),
    memory: {
      totalBytes: totalmem(),
      freeBytes: freemem(),
      usedBytes: totalmem() - freemem(),
      freePercent: Math.round((freemem() / totalmem()) * 100),
    },
    cpu: {
      model: cpuInfo.length > 0 ? cpuInfo[0].model : "unknown",
      cores: cpuInfo.length,
      speedMHz: cpuInfo.length > 0 ? cpuInfo[0].speed : 0,
    },
    timestamp: new Date().toISOString(),
  };
}

/**
 * Resource read handler.
 */
export async function systemInfoRead(
  uri: string,
): Promise<{ contents: Array<{ uri: string; mimeType?: string; text: string }>; isError?: boolean }> {
  const info = gatherSystemInfo();

  return {
    contents: [
      {
        uri,
        mimeType: "application/json",
        text: JSON.stringify(info, null, 2),
      },
    ],
  };
}

/** Static resource definition metadata (also exported for registration). */
export const systemInfoResource = {
  uri: "mcp://system/info",
  name: "System Information",
  description:
    "Current system and runtime information including platform, memory, and CPU details",
  mimeType: "application/json",
};
