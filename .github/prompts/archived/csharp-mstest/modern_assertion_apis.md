# Modern Assertion APIs

> Extracted from `csharp-mstest.prompt.md`.

## Modern Assertion APIs

MSTest provides three assertion classes: `Assert`, `StringAssert`, and `CollectionAssert`.

### Assert Class - Core Assertions

```csharp
// Equality
Assert.AreEqual(expected, actual);
Assert.AreNotEqual(notExpected, actual);
Assert.AreSame(expectedObject, actualObject);      // Reference equality
Assert.AreNotSame(notExpectedObject, actualObject);

// Null checks
Assert.IsNull(value);
Assert.IsNotNull(value);

// Boolean
Assert.IsTrue(condition);
Assert.IsFalse(condition);

// Fail/Inconclusive
Assert.Fail("Test failed due to...");
Assert.Inconclusive("Test cannot be completed because...");
```

### Exception Testing (Prefer over `[ExpectedException]`)

```csharp
// Assert.Throws - matches TException or derived types
var ex = Assert.Throws<ArgumentException>(() => Method(null));
Assert.AreEqual("Value cannot be null.", ex.Message);

// Assert.ThrowsExactly - matches exact type only
var ex = Assert.ThrowsExactly<InvalidOperationException>(() => Method());

// Async versions
var ex = await Assert.ThrowsAsync<HttpRequestException>(async () => await client.GetAsync(url));
var ex = await Assert.ThrowsExactlyAsync<InvalidOperationException>(async () => await Method());
```

### Collection Assertions (Assert class)

```csharp
Assert.Contains(expectedItem, collection);
Assert.DoesNotContain(unexpectedItem, collection);
Assert.ContainsSingle(collection);  // exactly one element
Assert.HasCount(5, collection);
Assert.IsEmpty(collection);
Assert.IsNotEmpty(collection);
```

### String Assertions (Assert class)

```csharp
Assert.Contains("expected", actualString);
Assert.StartsWith("prefix", actualString);
Assert.EndsWith("suffix", actualString);
Assert.DoesNotStartWith("prefix", actualString);
Assert.DoesNotEndWith("suffix", actualString);
Assert.MatchesRegex(@"\d{3}-\d{4}", phoneNumber);
Assert.DoesNotMatchRegex(@"\d+", textOnly);
```

### Comparison Assertions

```csharp
Assert.IsGreaterThan(lowerBound, actual);
Assert.IsGreaterThanOrEqualTo(lowerBound, actual);
Assert.IsLessThan(upperBound, actual);
Assert.IsLessThanOrEqualTo(upperBound, actual);
Assert.IsInRange(actual, low, high);
Assert.IsPositive(number);
Assert.IsNegative(number);
```

### Type Assertions

```csharp
// MSTest 3.x - uses out parameter
Assert.IsInstanceOfType<MyClass>(obj, out var typed);
typed.DoSomething();

// MSTest 4.x - returns typed result directly
var typed = Assert.IsInstanceOfType<MyClass>(obj);
typed.DoSomething();

Assert.IsNotInstanceOfType<WrongType>(obj);
```

### Assert.That (MSTest 4.0+)

```csharp
Assert.That(result.Count > 0);  // Auto-captures expression in failure message
```

### StringAssert Class

> **Note:** Prefer `Assert` class equivalents when available (e.g., `Assert.Contains("expected", actual)` over `StringAssert.Contains(actual, "expected")`).

```csharp
StringAssert.Contains(actualString, "expected");
StringAssert.StartsWith(actualString, "prefix");
StringAssert.EndsWith(actualString, "suffix");
StringAssert.Matches(actualString, new Regex(@"\d{3}-\d{4}"));
StringAssert.DoesNotMatch(actualString, new Regex(@"\d+"));
```

### CollectionAssert Class

> **Note:** Prefer `Assert` class equivalents when available (e.g., `Assert.Contains`).

```csharp
// Containment
CollectionAssert.Contains(collection, expectedItem);
CollectionAssert.DoesNotContain(collection, unexpectedItem);

// Equality (same elements, same order)
CollectionAssert.AreEqual(expectedCollection, actualCollection);
CollectionAssert.AreNotEqual(unexpectedCollection, actualCollection);

// Equivalence (same elements, any order)
CollectionAssert.AreEquivalent(expectedCollection, actualCollection);
CollectionAssert.AreNotEquivalent(unexpectedCollection, actualCollection);

// Subset checks
CollectionAssert.IsSubsetOf(subset, superset);
CollectionAssert.IsNotSubsetOf(notSubset, collection);

// Element validation
CollectionAssert.AllItemsAreInstancesOfType(collection, typeof(MyClass));
CollectionAssert.AllItemsAreNotNull(collection);
CollectionAssert.AllItemsAreUnique(collection);
```
