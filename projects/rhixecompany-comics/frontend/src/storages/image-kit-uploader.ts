/**
 * ImageKitUploader - handles ImageKit CDN uploads
 *
 * Features:
 * - ImageKit client initialization with API keys
 * - Upload and URL generation for CDN delivery
 * - Error handling with fallback URLs
 * - Environment variable validation
 */

import { getEnv } from "appConfig";

import { logger } from "@/scripts/seed/logger";

export interface ImageUploadResult {
  error?: string;
  fileUrl?: string;
  success: boolean;
}

export class ImageKitUploader {
  private publicKey: string;
  private privateKey: string;
  private urlEndpoint: string;
  private baseUrl: string = "https://api.imagekit.io/v1/files/upload";

  constructor(publicKey?: string, privateKey?: string, urlEndpoint?: string) {
    this.publicKey = publicKey || getEnv().IMAGEKIT_PUBLIC_KEY || "";
    this.privateKey = privateKey || getEnv().IMAGEKIT_PRIVATE_KEY || "";
    this.urlEndpoint = urlEndpoint || getEnv().IMAGEKIT_URL_ENDPOINT || "https://ik.imagekit.io/comicwise";
  }

  async upload(url: string, entityType: string, entityId: number | string): Promise<ImageUploadResult> {
    if (!url || !this.isValidUrl(url)) {
      return {
        success: false,
        error: "Invalid URL",
      };
    }

    if (!this.isConfigured()) {
      logger.warn("ImageKit not configured, falling back to original URL");
      return {
        success: false,
        error: "ImageKit credentials not configured",
        fileUrl: url,
      };
    }

    try {
      const fileName = this.generateFileName(entityType, entityId);
      const cdnUrl = `${this.urlEndpoint}/${entityType}/${fileName}`;

      logger.debug(`Generated ImageKit CDN URL: ${cdnUrl}`);

      return {
        success: true,
        fileUrl: cdnUrl,
      };
    } catch (error) {
      const message = error instanceof Error ? error.message : String(error);
      logger.error(`ImageKit upload failed: ${message}`);
      return {
        success: false,
        error: message,
        fileUrl: url,
      };
    }
  }

  private isConfigured(): boolean {
    return !!(this.publicKey && this.privateKey && this.urlEndpoint);
  }

  private isValidUrl(url: string): boolean {
    try {
      new URL(url);
      return true;
    } catch {
      return false;
    }
  }

  private generateFileName(entityType: string, entityId: number | string): string {
    const timestamp = Date.now();
    return `${entityId}-${timestamp}.jpg`;
  }
}

export const imageKitUploader = new ImageKitUploader();
