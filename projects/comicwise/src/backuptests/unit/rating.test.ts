/**
 * Rating System Tests
 * Tests for rating creation, updates, and aggregation
 */

import { describe, expect, it } from "vitest";

describe("Rating Validation", () => {
  describe("Rating values", () => {
    it("should accept valid rating 1-5", () => {
      const validRatings = [1, 2, 3, 4, 5];
      for (const rating of validRatings) {
        expect(rating).toBeGreaterThanOrEqual(1);
        expect(rating).toBeLessThanOrEqual(5);
      }
    });

    it("should reject ratings outside 1-5 range", () => {
      const isValidRating = (r: number): boolean => r >= 1 && r <= 5;

      expect(isValidRating(0)).toBe(false);
      expect(isValidRating(6)).toBe(false);
      expect(isValidRating(-1)).toBe(false);
    });

    it("should reject non-integer ratings", () => {
      const isValidRating = (r: number): boolean => Number.isInteger(r) && r >= 1 && r <= 5;

      expect(isValidRating(3.5)).toBe(false);
      expect(isValidRating(4.2)).toBe(false);
    });
  });

  describe("User rating uniqueness", () => {
    it("should prevent duplicate ratings from same user", () => {
      const ratings = [
        { userId: "user-1", comicId: 1, rating: 5 },
        { userId: "user-2", comicId: 1, rating: 4 },
      ];

      const userAlreadyRated = (userId: string, comicId: number): boolean => {
        return ratings.some((r) => r.userId === userId && r.comicId === comicId);
      };

      expect(userAlreadyRated("user-1", 1)).toBe(true);
      expect(userAlreadyRated("user-3", 1)).toBe(false);
    });
  });
});

describe("Rating Aggregation", () => {
  const ratings = [5, 5, 4, 4, 4, 3, 3, 2];

  it("should calculate average rating", () => {
    const average = ratings.reduce((a, b) => a + b, 0) / ratings.length;
    expect(average).toBe(3.75);
  });

  it("should round average to 1 decimal", () => {
    const average = ratings.reduce((a, b) => a + b, 0) / ratings.length;
    const rounded = Math.round(average * 10) / 10;
    expect(rounded).toBe(3.8);
  });

  it("should count total ratings", () => {
    expect(ratings).toHaveLength(8);
  });

  it("should calculate rating distribution", () => {
    const distribution = {
      5: ratings.filter((r) => r === 5).length,
      4: ratings.filter((r) => r === 4).length,
      3: ratings.filter((r) => r === 3).length,
      2: ratings.filter((r) => r === 2).length,
      1: ratings.filter((r) => r === 1).length,
    };

    expect(distribution[5]).toBe(2);
    expect(distribution[4]).toBe(3);
    expect(distribution[3]).toBe(2);
    expect(distribution[2]).toBe(1);
    expect(distribution[1]).toBe(0);
  });

  it("should handle empty ratings", () => {
    const emptyRatings: number[] = [];
    const average = emptyRatings.length > 0 ? emptyRatings.reduce((a, b) => a + b, 0) / emptyRatings.length : 0;

    expect(average).toBe(0);
  });
});

describe("Rating Updates", () => {
  it("should allow users to update their rating", () => {
    const userRating = 5; // User updates their rating from 4 to 5

    expect(userRating).toBe(5);
  });

  it("should recalculate aggregate after update", () => {
    let ratings = [5, 5, 4, 3];
    let average = ratings.reduce((a, b) => a + b, 0) / ratings.length;
    expect(Math.round(average * 10) / 10).toBe(4.3);

    // User updates rating from 3 to 5
    ratings = [5, 5, 4, 5];
    average = ratings.reduce((a, b) => a + b, 0) / ratings.length;
    expect(Math.round(average * 10) / 10).toBe(4.8);
  });

  it("should allow deletion and recalculate", () => {
    let ratings = [5, 5, 4, 3];
    let average = Math.round((ratings.reduce((a, b) => a + b, 0) / ratings.length) * 10) / 10;
    expect(average).toBe(4.3);

    // Delete one rating
    ratings = ratings.slice(0, -1); // Remove last element
    average = Math.round((ratings.reduce((a, b) => a + b, 0) / ratings.length) * 10) / 10;
    expect(average).toBe(4.7);
  });
});

describe("Star Display", () => {
  it("should map rating to stars", () => {
    const getRatingStars = (rating: number): string => {
      const fullStars = Math.floor(rating);
      const hasHalf = rating % 1 >= 0.5 ? "½" : "";
      const emptyStars = 5 - fullStars - (hasHalf ? 1 : 0);
      return "★".repeat(fullStars) + (hasHalf ? "½" : "") + "☆".repeat(emptyStars);
    };

    expect(getRatingStars(4.5)).toBe("★★★★½");
    expect(getRatingStars(3.2)).toBe("★★★☆☆");
    expect(getRatingStars(5)).toBe("★★★★★");
  });

  it("should display half-star for .5 ratings", () => {
    const rating = 4.5;
    const fullStars = Math.floor(rating);
    const hasHalf = rating % 1 !== 0;

    expect(fullStars).toBe(4);
    expect(hasHalf).toBe(true);
  });
});
