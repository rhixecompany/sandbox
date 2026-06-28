---
name: code-docs-python_google_style
description: "Python Google Style Docstrings"
version: 1.0.0
author: Alexa
---
     1|# Python Google Style Docstrings
     2|
     3|Complete reference for Google Style Python docstrings, based on the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).
     4|
     5|## Basic Structure
     6|
     7|```python
     8|"""One-line summary (imperative mood, ending with period).
     9|
    10|Extended description (optional). Can span multiple paragraphs.
    11|Use proper grammar and punctuation.
    12|
    13|Attributes:
    14|    attribute_name: Description of the attribute.
    15|
    16|Example:
    17|    >>> code_example()
    18|    expected_output
    19|"""
    20|```
    21|
    22|## Module Docstrings
    23|
    24|Place at the top of the file, after any shebang and before imports:
    25|
    26|```python
    27|#!/usr/bin/env python3
    28|"""Module for handling user authentication.
    29|
    30|This module provides classes and functions for authenticating users
    31|against various backend systems including LDAP, OAuth, and API keys.
    32|
    33|Typical usage example:
    34|
    35|    authenticator = Authenticator(config)
    36|    if authenticator.verify(username, password):
    37|        print("Login successful")
    38|"""
    39|
    40|import os
    41|import sys
    42|```
    43|
    44|## Class Docstrings
    45|
    46|```python
    47|class User:
    48|    """Represents a user in the system.
    49|
    50|    The User class encapsulates user data and provides methods
    51|    for authentication, authorization, and profile management.
    52|
    53|    Attributes:
    54|        username: A string representing the user's unique identifier.
    55|        email: A string containing the user's email address.
    56|        is_active: A boolean indicating if the user account is active.
    57|        created_at: A datetime object with account creation timestamp.
    58|
    59|    Example:
    60|        >>> user = User("john_doe", "john@example.com")
    61|        >>> user.is_active
    62|        True
    63|    """
    64|
    65|    def __init__(self, username: str, email: str):
    66|        """Initialize a new User.
    67|
    68|        Args:
    69|            username: Unique identifier for the user.
    70|            email: User's email address.
    71|
    72|        Raises:
    73|            ValueError: If username is empty or email is invalid.
    74|        """
    75|        self.username = username
    76|        self.email = email
    77|        self.is_active = True
    78|        self.created_at = datetime.now()
    79|```
    80|
    81|## Function/Method Docstrings
    82|
    83|### Basic Function
    84|
    85|```python
    86|def calculate_distance(point1: tuple[float, float],
    87|                       point2: tuple[float, float]) -> float:
    88|    """Calculate Euclidean distance between two points.
    89|
    90|    Args:
    91|        point1: First point as (x, y) coordinates.
    92|        point2: Second point as (x, y) coordinates.
    93|
    94|    Returns:
    95|        The Euclidean distance between the two points.
    96|
    97|    Example:
    98|        >>> calculate_distance((0, 0), (3, 4))
    99|        5.0
   100|    """
   101|    dx = point2[0] - point1[0]
   102|    dy = point2[1] - point1[1]
   103|    return math.sqrt(dx**2 + dy**2)
   104|```
   105|
   106|### Function with Exceptions
   107|
   108|```python
   109|def read_config(path: str) -> dict[str, Any]:
   110|    """Read and parse configuration file.
   111|
   112|    Reads a YAML configuration file and returns the parsed content
   113|    as a dictionary. Supports environment variable expansion.
   114|
   115|    Args:
   116|        path: Path to the configuration file.
   117|
   118|    Returns:
   119|        Dictionary containing parsed configuration data.
   120|
   121|    Raises:
   122|        FileNotFoundError: If the config file doesn't exist.
   123|        yaml.YAMLError: If the file contains invalid YAML.
   124|        PermissionError: If the file cannot be read due to permissions.
   125|
   126|    Example:
   127|        >>> config = read_config("/etc/app/config.yaml")
   128|        >>> config["database"]["host"]
   129|        'localhost'
   130|    """
   131|    with open(path, 'r') as f:
   132|        return yaml.safe_load(f)
   133|```
   134|
   135|### Generator Function
   136|
   137|```python
   138|def fibonacci(n: int) -> Iterator[int]:
   139|    """Generate Fibonacci sequence up to n terms.
   140|
   141|    Args:
   142|        n: Number of terms to generate.
   143|
   144|    Yields:
   145|        Next number in the Fibonacci sequence.
   146|
   147|    Raises:
   148|        ValueError: If n is negative.
   149|
   150|    Example:
   151|        >>> list(fibonacci(5))
   152|        [0, 1, 1, 2, 3]
   153|    """
   154|    if n < 0:
   155|        raise ValueError("n must be non-negative")
   156|
   157|    a, b = 0, 1
   158|    for _ in range(n):
   159|        yield a
   160|        a, b = b, a + b
   161|```
   162|
   163|### Async Function
   164|
   165|```python
   166|async def fetch_user_data(user_id: int) -> dict[str, Any]:
   167|    """Fetch user data from the API asynchronously.
   168|
   169|    Args:
   170|        user_id: Unique identifier of the user.
   171|
   172|    Returns:
   173|        Dictionary containing user data including profile, preferences,
   174|        and activity history.
   175|
   176|    Raises:
   177|        HTTPError: If the API request fails.
   178|        asyncio.TimeoutError: If the request times out.
   179|
   180|    Example:
   181|        >>> data = await fetch_user_data(12345)
   182|        >>> data["username"]
   183|        'john_doe'
   184|    """
   185|    async with aiohttp.ClientSession() as session:
   186|        async with session.get(f"/api/users/{user_id}") as response:
   187|            return await response.json()
   188|```
   189|
   190|## Section Formats
   191|
   192|### Args Section
   193|
   194|```python
   195|def create_user(username: str,
   196|                email: str,
   197|                age: int = None,
   198|                role: str = "user",
   199|                **kwargs) -> User:
   200|    """Create a new user account.
   201|
   202|    Args:
   203|        username: Unique username (3-20 characters, alphanumeric).
   204|        email: Valid email address.
   205|        age: User's age in years. Defaults to None (not specified).
   206|        role: User role (user, admin, moderator). Defaults to "user".
   207|        **kwargs: Additional user attributes.
   208|            tags (list[str]): User tags for categorization.
   209|            metadata (dict): Custom metadata dictionary.
   210|
   211|    Returns:
   212|        Newly created User object.
   213|    """
   214|```
   215|
   216|### Returns Section
   217|
   218|```python
   219|def search_users(query: str) -> list[User]:
   220|    """Search for users matching the query.
   221|
   222|    Args:
   223|        query: Search query string.
   224|
   225|    Returns:
   226|        List of User objects matching the query, sorted by relevance.
   227|        Returns empty list if no matches found.
   228|    """
   229|```
   230|
   231|Multiple return values:
   232|
   233|```python
   234|def divide(a: float, b: float) -> tuple[float, float]:
   235|    """Divide two numbers.
   236|
   237|    Args:
   238|        a: Dividend.
   239|        b: Divisor.
   240|
   241|    Returns:
   242|        A tuple containing:
   243|            - Quotient (a / b)
   244|            - Remainder (a % b)
   245|    """
   246|    return a / b, a % b
   247|```
   248|
   249|### Raises Section
   250|
   251|```python
   252|def validate_email(email: str) -> bool:
   253|    """Validate email address format.
   254|
   255|    Args:
   256|        email: Email address to validate.
   257|
   258|    Returns:
   259|        True if email format is valid, False otherwise.
   260|
   261|    Raises:
   262|        TypeError: If email is not a string.
   263|        ValueError: If email is an empty string.
   264|    """
   265|```
   266|
   267|### Yields Section (Generators)
   268|
   269|```python
   270|def batch_processor(items: list[Any], batch_size: int) -> Iterator[list[Any]]:
   271|    """Process items in batches.
   272|
   273|    Args:
   274|        items: List of items to process.
   275|        batch_size: Number of items per batch.
   276|
   277|    Yields:
   278|        List of items for each batch. Last batch may be smaller than
   279|        batch_size if items don't divide evenly.
   280|
   281|    Example:
   282|        >>> for batch in batch_processor(range(10), 3):
   283|        ...     print(batch)
   284|        [0, 1, 2]
   285|        [3, 4, 5]
   286|        [6, 7, 8]
   287|        [9]
   288|    """
   289|```
   290|
   291|### Example Section
   292|
   293|```python
   294|def merge_dicts(dict1: dict, dict2: dict) -> dict:
   295|    """Merge two dictionaries with dict2 taking precedence.
   296|
   297|    Args:
   298|        dict1: First dictionary.
   299|        dict2: Second dictionary (values override dict1).
   300|
   301|    Returns:
   302|        Merged dictionary.
   303|
   304|    Example:
   305|        >>> d1 = {"a": 1, "b": 2}
   306|        >>> d2 = {"b": 3, "c": 4}
   307|        >>> merge_dicts(d1, d2)
   308|        {"a": 1, "b": 3, "c": 4}
   309|
   310|    Note:
   311|        This function does not modify the input dictionaries.
   312|    """
   313|```
   314|
   315|### Note/Warning Sections
   316|
   317|```python
   318|def cache_data(key: str, value: Any, ttl: int = 3600) -> None:
   319|    """Cache data with expiration.
   320|
   321|    Args:
   322|        key: Cache key.
   323|        value: Value to cache (must be JSON serializable).
   324|        ttl: Time to live in seconds. Defaults to 3600 (1 hour).
   325|
   326|    Note:
   327|        This function uses an in-memory cache. Data will be lost
   328|        when the application restarts.
   329|
   330|    Warning:
   331|        Large values may impact memory usage. Consider using
   332|        external cache for values larger than 1MB.
   333|    """
   334|```
   335|
   336|## Type Hints Integration
   337|
   338|With type hints, you can be more concise:
   339|
   340|```python
   341|def process_order(order_id: int,
   342|                  items: list[str],
   343|                  discount: float = 0.0) -> bool:
   344|    """Process a customer order.
   345|
   346|    Args:
   347|        order_id: Unique order identifier.
   348|        items: List of item SKUs to order.
   349|        discount: Discount percentage (0.0 to 1.0). Defaults to 0.0.
   350|
   351|    Returns:
   352|        True if order processed successfully, False otherwise.
   353|    """
   354|```
   355|
   356|Types are already specified, so Args can focus on semantics, not types.
   357|
   358|## Complex Types
   359|
   360|```python
   361|from typing import Optional, Union, Callable
   362|
   363|def register_callback(
   364|    event: str,
   365|    callback: Callable[[dict[str, Any]], None],
   366|    priority: int = 0
   367|) -> Optional[str]:
   368|    """Register an event callback.
   369|
   370|    Args:
   371|        event: Event name to listen for (e.g., "user.login").
   372|        callback: Function to call when event fires. Must accept
   373|            a single dictionary argument containing event data.
   374|        priority: Callback priority (higher = called first).
   375|            Defaults to 0.
   376|
   377|    Returns:
   378|        Callback ID if registration successful, None if event
   379|        doesn't exist.
   380|
   381|    Example:
   382|        >>> def on_login(data):
   383|        ...     print(f"User {data['username']} logged in")
   384|        >>> callback_id = register_callback("user.login", on_login)
   385|    """
   386|```
   387|
   388|## Property Docstrings
   389|
   390|```python
   391|class Temperature:
   392|    """Temperature with unit conversion."""
   393|
   394|    def __init__(self, celsius: float):
   395|        """Initialize temperature.
   396|
   397|        Args:
   398|            celsius: Temperature in Celsius.
   399|        """
   400|        self._celsius = celsius
   401|
   402|    @property
   403|    def fahrenheit(self) -> float:
   404|        """Temperature in Fahrenheit.
   405|
   406|        Returns:
   407|            Temperature converted to Fahrenheit.
   408|        """
   409|        return self._celsius * 9/5 + 32
   410|
   411|    @fahrenheit.setter
   412|    def fahrenheit(self, value: float) -> None:
   413|        """Set temperature using Fahrenheit.
   414|
   415|        Args:
   416|            value: Temperature in Fahrenheit.
   417|        """
   418|        self._celsius = (value - 32) * 5/9
   419|```
   420|
   421|## Magic Methods
   422|
   423|```python
   424|class Vector:
   425|    """2D vector with mathematical operations."""
   426|
   427|    def __init__(self, x: float, y: float):
   428|        """Initialize vector.
   429|
   430|        Args:
   431|            x: X coordinate.
   432|            y: Y coordinate.
   433|        """
   434|        self.x = x
   435|        self.y = y
   436|
   437|    def __add__(self, other: "Vector") -> "Vector":
   438|        """Add two vectors.
   439|
   440|        Args:
   441|            other: Vector to add.
   442|
   443|        Returns:
   444|            New Vector representing the sum.
   445|
   446|        Example:
   447|            >>> v1 = Vector(1, 2)
   448|            >>> v2 = Vector(3, 4)
   449|            >>> v3 = v1 + v2
   450|            >>> (v3.x, v3.y)
   451|            (4, 6)
   452|        """
   453|        return Vector(self.x + other.x, self.y + other.y)
   454|
   455|    def __repr__(self) -> str:
   456|        """Return string representation.
   457|
   458|        Returns:
   459|            String in format "Vector(x, y)".
   460|        """
   461|        return f"Vector({self.x}, {self.y})"
   462|```
   463|
   464|## Class with Multiple Methods
   465|
   466|```python
   467|class DatabaseConnection:
   468|    """Manages database connections with connection pooling.
   469|
   470|    This class provides a thread-safe connection pool for PostgreSQL
   471|    databases. It handles automatic reconnection and query retries.
   472|
   473|    Attributes:
   474|        host: Database host address.
   475|        port: Database port number.
   476|        database: Database name.
   477|        pool_size: Maximum number of connections in pool.
   478|        is_connected: Boolean indicating connection status.
   479|
   480|    Example:
   481|        >>> db = DatabaseConnection("localhost", 5432, "mydb")
   482|        >>> db.connect()
   483|        >>> result = db.query("SELECT * FROM users")
   484|        >>> db.close()
   485|    """
   486|
   487|    def __init__(self, host: str, port: int, database: str,
   488|                 pool_size: int = 10):
   489|        """Initialize database connection.
   490|
   491|        Args:
   492|            host: Database server hostname or IP.
   493|            port: Database server port.
   494|            database: Name of database to connect to.
   495|            pool_size: Maximum connections in pool. Defaults to 10.
   496|
   497|        Raises:
   498|            ValueError: If pool_size is less than 1.
   499|        """
   500|        if pool_size < 1:
   501|