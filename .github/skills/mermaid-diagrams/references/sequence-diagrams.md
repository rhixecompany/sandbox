---
name: mermaid-diagrams-sequence-diagrams
description: "Sequence Diagrams"
version: 1.0.0
author: Alexa
---
     1|# Sequence Diagrams
     2|
     3|Sequence diagrams show interactions between participants over time. They're ideal for API flows, authentication sequences, and system component interactions.
     4|
     5|## Basic Syntax
     6|
     7|```mermaid
     8|sequenceDiagram
     9|    participant A
    10|    participant B
    11|    A->>B: Message
    12|```
    13|
    14|## Participants and Actors
    15|
    16|```mermaid
    17|sequenceDiagram
    18|    actor User
    19|    participant Frontend
    20|    participant API
    21|    participant Database
    22|
    23|    User->>Frontend: Click button
    24|    Frontend->>API: POST /data
    25|```
    26|
    27|**Difference:**
    28|
    29|- `participant` - System components (services, classes, databases)
    30|- `actor` - External entities (users, external systems)
    31|
    32|## Message Types
    33|
    34|### Solid Arrow (Synchronous)
    35|
    36|```mermaid
    37|sequenceDiagram
    38|    Client->>Server: Request
    39|    Server-->>Client: Response
    40|```
    41|
    42|- `->>` Solid arrow (request)
    43|- `-->>` Dotted arrow (response/return)
    44|
    45|### Open Arrow (Asynchronous)
    46|
    47|```mermaid
    48|sequenceDiagram
    49|    Client-)Server: Async message
    50|    Server--)Client: Async response
    51|```
    52|
    53|- `-)` Solid open arrow
    54|- `--)` Dotted open arrow
    55|
    56|### Cross/X (Delete)
    57|
    58|```mermaid
    59|sequenceDiagram
    60|    Client-xServer: Delete
    61|```
    62|
    63|## Activations
    64|
    65|Show when a participant is actively processing:
    66|
    67|```mermaid
    68|sequenceDiagram
    69|    Client->>+Server: Request
    70|    Server->>+Database: Query
    71|    Database-->>-Server: Data
    72|    Server-->>-Client: Response
    73|```
    74|
    75|- `+` after arrow activates
    76|- `-` before arrow deactivates
    77|
    78|## Alt/Else (Conditional Logic)
    79|
    80|```mermaid
    81|sequenceDiagram
    82|    User->>API: POST /login
    83|    API->>Database: Query user
    84|    Database-->>API: User data
    85|
    86|    alt Valid credentials
    87|        API-->>User: 200 OK + Token
    88|    else Invalid credentials
    89|        API-->>User: 401 Unauthorized
    90|    else Account locked
    91|        API-->>User: 403 Forbidden
    92|    end
    93|```
    94|
    95|## Opt (Optional)
    96|
    97|```mermaid
    98|sequenceDiagram
    99|    User->>API: POST /order
   100|    API->>PaymentService: Process payment
   101|
   102|    opt Payment successful
   103|        API->>EmailService: Send confirmation
   104|    end
   105|
   106|    API-->>User: Order result
   107|```
   108|
   109|## Par (Parallel)
   110|
   111|Show concurrent operations:
   112|
   113|```mermaid
   114|sequenceDiagram
   115|    API->>Service: Process order
   116|
   117|    par Send email
   118|        Service->>EmailService: Send confirmation
   119|    and Update inventory
   120|        Service->>InventoryService: Reduce stock
   121|    and Log event
   122|        Service->>LogService: Log order
   123|    end
   124|
   125|    Service-->>API: Complete
   126|```
   127|
   128|## Loop
   129|
   130|```mermaid
   131|sequenceDiagram
   132|    Client->>Server: Request batch
   133|
   134|    loop For each item
   135|        Server->>Database: Process item
   136|        Database-->>Server: Result
   137|    end
   138|
   139|    Server-->>Client: All results
   140|```
   141|
   142|**Loop with condition:**
   143|
   144|```mermaid
   145|sequenceDiagram
   146|    loop Every 5 seconds
   147|        Monitor->>API: Health check
   148|        API-->>Monitor: Status
   149|    end
   150|```
   151|
   152|## Break (Early Exit)
   153|
   154|```mermaid
   155|sequenceDiagram
   156|    User->>API: Submit form
   157|    API->>Validator: Validate input
   158|
   159|    break Input invalid
   160|        API-->>User: 400 Bad Request
   161|    end
   162|
   163|    API->>Database: Save data
   164|    Database-->>API: Success
   165|    API-->>User: 200 OK
   166|```
   167|
   168|## Notes
   169|
   170|### Note over single participant
   171|
   172|```mermaid
   173|sequenceDiagram
   174|    User->>API: Request
   175|    Note over API: Validates JWT token
   176|    API-->>User: Response
   177|```
   178|
   179|### Note spanning participants
   180|
   181|```mermaid
   182|sequenceDiagram
   183|    Frontend->>API: Request
   184|    Note over Frontend,API: HTTPS encrypted
   185|    API-->>Frontend: Response
   186|```
   187|
   188|### Right/Left notes
   189|
   190|```mermaid
   191|sequenceDiagram
   192|    User->>System: Action
   193|    Note right of System: Logs to database
   194|    System-->>User: Response
   195|    Note left of User: Updates UI
   196|```
   197|
   198|## Sequence Numbers
   199|
   200|Automatically number messages:
   201|
   202|```mermaid
   203|sequenceDiagram
   204|    autonumber
   205|
   206|    User->>Frontend: Login
   207|    Frontend->>API: Authenticate
   208|    API->>Database: Verify credentials
   209|    Database-->>API: User data
   210|    API-->>Frontend: JWT token
   211|    Frontend-->>User: Success
   212|```
   213|
   214|## Links and Tooltips
   215|
   216|Add clickable links:
   217|
   218|```mermaid
   219|sequenceDiagram
   220|    participant A as Service A
   221|    link A: Dashboard @ https://dashboard.example.com
   222|    link A: API Docs @ https://docs.example.com
   223|
   224|    A->>B: Message
   225|```
   226|
   227|## Comprehensive Example: User Authentication Flow
   228|
   229|```mermaid
   230|sequenceDiagram
   231|    autonumber
   232|    actor User
   233|    participant Frontend
   234|    participant AuthAPI
   235|    participant Database
   236|    participant Redis
   237|    participant EmailService
   238|
   239|    User->>+Frontend: Enter credentials
   240|    Frontend->>+AuthAPI: POST /auth/login
   241|
   242|    AuthAPI->>+Database: Query user by email
   243|    Database-->>-AuthAPI: User record
   244|
   245|    alt User not found
   246|        AuthAPI-->>Frontend: 404 User not found
   247|        Frontend-->>User: Show error
   248|    else User found
   249|        AuthAPI->>AuthAPI: Verify password hash
   250|
   251|        alt Invalid password
   252|            AuthAPI->>Database: Increment failed attempts
   253|
   254|            opt Failed attempts > 5
   255|                AuthAPI->>Database: Lock account
   256|                AuthAPI->>EmailService: Send security alert
   257|            end
   258|
   259|            AuthAPI-->>Frontend: 401 Invalid credentials
   260|            Frontend-->>User: Show error
   261|        else Valid password
   262|            AuthAPI->>AuthAPI: Generate JWT token
   263|            AuthAPI->>+Redis: Store session
   264|            Redis-->>-AuthAPI: Confirm
   265|
   266|            par Update login metadata
   267|                AuthAPI->>Database: Update last_login
   268|            and Track analytics
   269|                AuthAPI->>Database: Log login event
   270|            end
   271|
   272|            AuthAPI-->>-Frontend: 200 OK + JWT token
   273|            Frontend->>Frontend: Store token in localStorage
   274|            Frontend-->>-User: Redirect to dashboard
   275|
   276|            opt First login
   277|                EmailService->>User: Welcome email
   278|            end
   279|        end
   280|    end
   281|```
   282|
   283|## API Request/Response Example
   284|
   285|```mermaid
   286|sequenceDiagram
   287|    autonumber
   288|    participant Client
   289|    participant Gateway
   290|    participant AuthService
   291|    participant UserService
   292|    participant Database
   293|
   294|    Client->>+Gateway: GET /api/users/123
   295|    Note over Gateway: Rate limiting check
   296|
   297|    Gateway->>+AuthService: Validate JWT
   298|    AuthService->>AuthService: Verify signature
   299|
   300|    alt Token invalid or expired
   301|        AuthService-->>Gateway: 401 Unauthorized
   302|        Gateway-->>Client: 401 Unauthorized
   303|    else Token valid
   304|        AuthService-->>-Gateway: User context
   305|
   306|        Gateway->>+UserService: GET /users/123
   307|        UserService->>+Database: SELECT * FROM users WHERE id=123
   308|        Database-->>-UserService: User record
   309|
   310|        alt User not found
   311|            UserService-->>Gateway: 404 Not Found
   312|            Gateway-->>Client: 404 Not Found
   313|        else User found
   314|            UserService-->>-Gateway: 200 OK + User data
   315|            Gateway-->>-Client: 200 OK + User data
   316|        end
   317|    end
   318|```
   319|
   320|## Microservices Communication
   321|
   322|```mermaid
   323|sequenceDiagram
   324|    actor User
   325|    participant Gateway
   326|    participant OrderService
   327|    participant PaymentService
   328|    participant InventoryService
   329|    participant NotificationService
   330|    participant MessageQueue
   331|
   332|    User->>+Gateway: POST /orders
   333|    Gateway->>+OrderService: Create order
   334|
   335|    OrderService->>+InventoryService: Check stock
   336|    InventoryService-->>-OrderService: Stock available
   337|
   338|    break Insufficient stock
   339|        OrderService-->>Gateway: 400 Out of stock
   340|        Gateway-->>User: Error message
   341|    end
   342|
   343|    OrderService->>OrderService: Reserve order
   344|    OrderService->>+PaymentService: Charge customer
   345|
   346|    alt Payment successful
   347|        PaymentService-->>-OrderService: Payment confirmed
   348|        OrderService->>MessageQueue: Publish OrderConfirmed event
   349|
   350|        par Async processing
   351|            MessageQueue->>InventoryService: Reduce stock
   352|        and
   353|            MessageQueue->>NotificationService: Send confirmation
   354|            NotificationService->>User: Email confirmation
   355|        end
   356|
   357|        OrderService-->>-Gateway: 201 Created
   358|        Gateway-->>User: Order confirmed
   359|    else Payment failed
   360|        PaymentService-->>OrderService: Payment declined
   361|        OrderService->>OrderService: Release reservation
   362|        OrderService-->>Gateway: 402 Payment Required
   363|        Gateway-->>User: Payment failed
   364|    end
   365|```
   366|
   367|## Best Practices
   368|
   369|1. **Order participants logically** - Typically: User → Frontend → Backend → Database
   370|2. **Use activations** - Shows when components are actively processing
   371|3. **Group related logic** - Use alt/opt/par to organize conditional flows
   372|4. **Add descriptive notes** - Explain complex logic or important details
   373|5. **Keep diagrams focused** - One scenario per diagram
   374|6. **Number messages** - Use autonumber for complex flows
   375|7. **Show error paths** - Document failure scenarios with alt/else
   376|8. **Indicate async operations** - Use open arrows for fire-and-forget messages
   377|
   378|## Common Use Cases
   379|
   380|### Authentication
   381|
   382|- Login flows
   383|- OAuth/SSO flows
   384|- Token refresh
   385|- Password reset
   386|
   387|### API Operations
   388|
   389|- CRUD operations
   390|- Search and filtering
   391|- Batch processing
   392|- Webhook handling
   393|
   394|### System Integration
   395|
   396|- Microservice communication
   397|- Third-party API calls
   398|- Message queue processing
   399|- Event-driven architecture
   400|
   401|### Business Processes
   402|
   403|- Order fulfillment
   404|- Payment processing
   405|- Approval workflows
   406|- Notification chains
   407|