---
name: code-docs-go_google_style
description: "Go Google Style Comments"
version: 1.0.0
author: Alexa
---
     1|# Go Google Style Comments
     2|
     3|Complete reference for Go documentation comments, following Google's Go Style Guide and effective godoc practices.
     4|
     5|## Basic Principles
     6|
     7|- Comments should explain **what** and **why**, not **how** (code shows how)
     8|- Every exported (public) identifier should have a doc comment
     9|- Comments are full sentences with proper punctuation
    10|- First sentence is a summary starting with the declared name
    11|
    12|## Package Comments
    13|
    14|### Basic Package Comment
    15|
    16|Place before the package declaration, typically in a `doc.go` file:
    17|
    18|```go
    19|// Package auth provides authentication and authorization utilities.
    20|//
    21|// This package supports multiple authentication backends including
    22|// OAuth2, API keys, and LDAP. It provides a unified interface for
    23|// validating credentials and managing user sessions.
    24|//
    25|// Basic usage:
    26|//
    27|// authenticator := auth.New(auth.Config{
    28|//  Backend: auth.OAuth2,
    29|//  ClientID: "your-client-id",
    30|// })
    31|// if err := authenticator.Verify(token); err != nil {
    32|//  log.Fatal(err)
    33|// }
    34|package auth
    35|```
    36|
    37|### Package Comment in Main File
    38|
    39|For simple packages without `doc.go`:
    40|
    41|```go
    42|// Package stringutil provides string manipulation utilities.
    43|//
    44|// It includes functions for common string operations like
    45|// reversing, trimming, and case conversion.
    46|package stringutil
    47|
    48|import "strings"
    49|```
    50|
    51|## Function Comments
    52|
    53|### Basic Function
    54|
    55|```go
    56|// Add returns the sum of two integers.
    57|func Add(a, b int) int {
    58| return a + b
    59|}
    60|```
    61|
    62|### Function with Parameters
    63|
    64|```go
    65|// CalculateDistance returns the Euclidean distance between two points.
    66|// The points are represented as (x, y) coordinate pairs.
    67|func CalculateDistance(x1, y1, x2, y2 float64) float64 {
    68| dx := x2 - x1
    69| dy := y2 - y1
    70| return math.Sqrt(dx*dx + dy*dy)
    71|}
    72|```
    73|
    74|### Function with Error Return
    75|
    76|```go
    77|// ReadConfig reads and parses the configuration file at the given path.
    78|//
    79|// It returns an error if the file cannot be read or contains invalid YAML.
    80|// Environment variables in the config file are automatically expanded.
    81|func ReadConfig(path string) (*Config, error) {
    82| data, err := os.ReadFile(path)
    83| if err != nil {
    84|  return nil, fmt.Errorf("read config: %w", err)
    85| }
    86|
    87| var config Config
    88| if err := yaml.Unmarshal(data, &config); err != nil {
    89|  return nil, fmt.Errorf("parse config: %w", err)
    90| }
    91|
    92| return &config, nil
    93|}
    94|```
    95|
    96|### Function with Multiple Return Values
    97|
    98|```go
    99|// Divide returns the quotient and remainder of a divided by b.
   100|//
   101|// It returns an error if b is zero.
   102|func Divide(a, b int) (quotient, remainder int, err error) {
   103| if b == 0 {
   104|  return 0, 0, errors.New("division by zero")
   105| }
   106| return a / b, a % b, nil
   107|}
   108|```
   109|
   110|### Function with Example
   111|
   112|```go
   113|// ParseDuration parses a duration string and returns a time.Duration.
   114|//
   115|// Valid time units are "ns", "us", "ms", "s", "m", "h".
   116|//
   117|// Example usage:
   118|//
   119|// d, err := ParseDuration("1h30m")
   120|// if err != nil {
   121|//  log.Fatal(err)
   122|// }
   123|// fmt.Println(d) // Output: 1h30m0s
   124|func ParseDuration(s string) (time.Duration, error) {
   125| return time.ParseDuration(s)
   126|}
   127|```
   128|
   129|## Type Comments
   130|
   131|### Struct
   132|
   133|```go
   134|// User represents a user account in the system.
   135|//
   136|// Users can have different roles and permissions. The IsActive field
   137|// determines whether the user can log in.
   138|type User struct {
   139| // ID is the unique identifier for the user.
   140| ID int64
   141|
   142| // Username is the user's unique login name.
   143| Username string
   144|
   145| // Email is the user's email address.
   146| Email string
   147|
   148| // IsActive indicates whether the user account is enabled.
   149| IsActive bool
   150|
   151| // CreatedAt is the timestamp when the account was created.
   152| CreatedAt time.Time
   153|}
   154|```
   155|
   156|### Interface
   157|
   158|```go
   159|// Storage defines the interface for data persistence operations.
   160|//
   161|// Implementations must be safe for concurrent use by multiple goroutines.
   162|type Storage interface {
   163| // Get retrieves the value for the given key.
   164| // It returns ErrNotFound if the key doesn't exist.
   165| Get(ctx context.Context, key string) ([]byte, error)
   166|
   167| // Set stores a value with the given key.
   168| // If the key already exists, the value is overwritten.
   169| Set(ctx context.Context, key string, value []byte) error
   170|
   171| // Delete removes the key and its value.
   172| // It returns no error if the key doesn't exist.
   173| Delete(ctx context.Context, key string) error
   174|
   175| // Close releases any resources held by the storage.
   176| Close() error
   177|}
   178|```
   179|
   180|### Type Alias
   181|
   182|```go
   183|// UserID is a unique identifier for a user.
   184|type UserID int64
   185|
   186|// Email represents a validated email address.
   187|type Email string
   188|```
   189|
   190|### Custom Type
   191|
   192|```go
   193|// Status represents the current state of a task.
   194|type Status int
   195|
   196|const (
   197| // StatusPending indicates the task hasn't started.
   198| StatusPending Status = iota
   199|
   200| // StatusRunning indicates the task is currently executing.
   201| StatusRunning
   202|
   203| // StatusCompleted indicates the task finished successfully.
   204| StatusCompleted
   205|
   206| // StatusFailed indicates the task encountered an error.
   207| StatusFailed
   208|)
   209|```
   210|
   211|## Method Comments
   212|
   213|```go
   214|// Config holds database connection configuration.
   215|type Config struct {
   216| Host     string
   217| Port     int
   218| Database string
   219|}
   220|
   221|// DSN returns the data source name for connecting to the database.
   222|//
   223|// The DSN format is "host:port/database".
   224|func (c *Config) DSN() string {
   225| return fmt.Sprintf("%s:%d/%s", c.Host, c.Port, c.Database)
   226|}
   227|
   228|// Validate checks that all required configuration fields are set.
   229|//
   230|// It returns an error if any required field is missing or invalid.
   231|func (c *Config) Validate() error {
   232| if c.Host == "" {
   233|  return errors.New("host is required")
   234| }
   235| if c.Port <= 0 || c.Port > 65535 {
   236|  return errors.New("port must be between 1 and 65535")
   237| }
   238| if c.Database == "" {
   239|  return errors.New("database is required")
   240| }
   241| return nil
   242|}
   243|```
   244|
   245|## Constants and Variables
   246|
   247|### Constants
   248|
   249|```go
   250|// DefaultTimeout is the default request timeout duration.
   251|const DefaultTimeout = 30 * time.Second
   252|
   253|// Maximum allowed values.
   254|const (
   255| // MaxRetries is the maximum number of retry attempts.
   256| MaxRetries = 3
   257|
   258| // MaxConcurrency is the maximum number of concurrent operations.
   259| MaxConcurrency = 100
   260|)
   261|```
   262|
   263|### Variables
   264|
   265|```go
   266|// ErrNotFound is returned when a requested resource doesn't exist.
   267|var ErrNotFound = errors.New("not found")
   268|
   269|// Common error values.
   270|var (
   271| // ErrInvalidInput is returned for invalid input parameters.
   272| ErrInvalidInput = errors.New("invalid input")
   273|
   274| // ErrTimeout is returned when an operation times out.
   275| ErrTimeout = errors.New("operation timed out")
   276|
   277| // ErrUnauthorized is returned for authentication failures.
   278| ErrUnauthorized = errors.New("unauthorized")
   279|)
   280|```
   281|
   282|## Advanced Patterns
   283|
   284|### Constructor Function
   285|
   286|```go
   287|// NewClient creates a new API client with the given configuration.
   288|//
   289|// The client maintains an internal connection pool and is safe for
   290|// concurrent use by multiple goroutines.
   291|//
   292|// Example:
   293|//
   294|// client := NewClient(Config{
   295|//  BaseURL: "https://api.example.com",
   296|//  APIKey:  "your-key",
   297|// })
   298|// defer client.Close()
   299|func NewClient(cfg Config) *Client {
   300| return &Client{
   301|  config: cfg,
   302|  http:   &http.Client{Timeout: 30 * time.Second},
   303| }
   304|}
   305|```
   306|
   307|### Options Pattern
   308|
   309|```go
   310|// Option configures a Client.
   311|type Option func(*Client)
   312|
   313|// WithTimeout returns an Option that sets the request timeout.
   314|func WithTimeout(d time.Duration) Option {
   315| return func(c *Client) {
   316|  c.timeout = d
   317| }
   318|}
   319|
   320|// WithRetries returns an Option that sets the number of retry attempts.
   321|func WithRetries(n int) Option {
   322| return func(c *Client) {
   323|  c.retries = n
   324| }
   325|}
   326|
   327|// NewClient creates a new Client with the given options.
   328|//
   329|// Example:
   330|//
   331|// client := NewClient(
   332|//  WithTimeout(60*time.Second),
   333|//  WithRetries(5),
   334|// )
   335|func NewClient(opts ...Option) *Client {
   336| c := &Client{
   337|  timeout: DefaultTimeout,
   338|  retries: 3,
   339| }
   340| for _, opt := range opts {
   341|  opt(c)
   342| }
   343| return c
   344|}
   345|```
   346|
   347|### Context-Aware Functions
   348|
   349|```go
   350|// FetchUser retrieves user data from the API.
   351|//
   352|// The operation respects the context's deadline and cancellation.
   353|// It returns an error if the context is cancelled or the request fails.
   354|func FetchUser(ctx context.Context, userID int64) (*User, error) {
   355| req, err := http.NewRequestWithContext(
   356|  ctx,
   357|  "GET",
   358|  fmt.Sprintf("/users/%d", userID),
   359|  nil,
   360| )
   361| if err != nil {
   362|  return nil, err
   363| }
   364|
   365| // ... implementation
   366|}
   367|```
   368|
   369|### Generic Functions
   370|
   371|```go
   372|// Map applies a function to each element of a slice and returns a new slice.
   373|//
   374|// The function f is called once for each element in the input slice.
   375|// The order of elements is preserved.
   376|//
   377|// Example:
   378|//
   379|// nums := []int{1, 2, 3}
   380|// doubled := Map(nums, func(n int) int { return n * 2 })
   381|// // doubled is []int{2, 4, 6}
   382|func Map[T, U any](slice []T, f func(T) U) []U {
   383| result := make([]U, len(slice))
   384| for i, v := range slice {
   385|  result[i] = f(v)
   386| }
   387| return result
   388|}
   389|```
   390|
   391|## Error Documentation
   392|
   393|### Custom Error Types
   394|
   395|```go
   396|// ValidationError represents a data validation failure.
   397|//
   398|// It includes the field that failed validation and the reason.
   399|type ValidationError struct {
   400| Field  string
   401| Reason string
   402|}
   403|
   404|// Error returns a string representation of the validation error.
   405|func (e *ValidationError) Error() string {
   406| return fmt.Sprintf("validation failed for field %s: %s", e.Field, e.Reason)
   407|}
   408|```
   409|
   410|### Error Wrapping
   411|
   412|```go
   413|// ProcessFile reads and processes a file.
   414|//
   415|// It returns an error if the file cannot be read, parsed, or processed.
   416|// Errors from lower-level operations are wrapped with additional context.
   417|func ProcessFile(path string) error {
   418| data, err := os.ReadFile(path)
   419| if err != nil {
   420|  return fmt.Errorf("read file %s: %w", path, err)
   421| }
   422|
   423| if err := validate(data); err != nil {
   424|  return fmt.Errorf("validate file %s: %w", path, err)
   425| }
   426|
   427| return nil
   428|}
   429|```
   430|
   431|## Code Examples in Comments
   432|
   433|### Simple Example
   434|
   435|```go
   436|// Reverse returns a reversed copy of the string.
   437|//
   438|// Example:
   439|//
   440|// s := Reverse("hello")
   441|// // s is "olleh"
   442|func Reverse(s string) string {
   443| runes := []rune(s)
   444| for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
   445|  runes[i], runes[j] = runes[j], runes[i]
   446| }
   447| return string(runes)
   448|}
   449|```
   450|
   451|### Multi-line Example
   452|
   453|```go
   454|// Server provides an HTTP server for the API.
   455|//
   456|// Example usage:
   457|//
   458|// srv := &Server{
   459|//  Addr:    ":8080",
   460|//  Handler: handler,
   461|// }
   462|//
   463|// if err := srv.Start(); err != nil {
   464|//  log.Fatal(err)
   465|// }
   466|// defer srv.Shutdown(context.Background())
   467|type Server struct {
   468| Addr    string
   469| Handler http.Handler
   470|}
   471|```
   472|
   473|## Special Sections
   474|
   475|### Deprecated
   476|
   477|```go
   478|// OldFunction is deprecated. Use NewFunction instead.
   479|//
   480|// Deprecated: This function will be removed in version 2.0.
   481|// Use NewFunction which provides better performance and error handling.
   482|func OldFunction() {
   483| // implementation
   484|}
   485|```
   486|
   487|### Experimental
   488|
   489|```go
   490|// ExperimentalFeature provides new functionality.
   491|//
   492|// Warning: This is an experimental API and may change in future versions.
   493|// Do not use in production code.
   494|func ExperimentalFeature() {
   495| // implementation
   496|}
   497|```
   498|
   499|### Internal Details
   500|
   501|