---
name: mermaid-diagrams-c4-diagrams
description: "C4 Model Diagrams"
version: 1.0.0
author: Alexa
---
     1|# C4 Model Diagrams
     2|
     3|The C4 model provides a hierarchical way to visualize software architecture at different levels of abstraction: Context, Containers, Components, and Code.
     4|
     5|## C4 Model Levels
     6|
     7|1. **System Context** - Shows the system and its users/external systems
     8|2. **Container** - Shows applications, databases, and services within the system
     9|3. **Component** - Shows internal structure of containers
    10|4. **Code** - Class diagrams showing implementation details (use regular class diagrams)
    11|
    12|## C4 Context Diagram
    13|
    14|Shows the big picture: your system and its relationships with users and external systems.
    15|
    16|### Basic Syntax
    17|
    18|```mermaid
    19|C4Context
    20|    title System Context for Banking System
    21|
    22|    Person(customer, "Customer", "A banking customer")
    23|    System(banking, "Banking System", "Allows customers to manage accounts")
    24|    System_Ext(email, "Email System", "Sends emails")
    25|
    26|    Rel(customer, banking, "Uses")
    27|    Rel(banking, email, "Sends emails via")
    28|```
    29|
    30|### Elements
    31|
    32|**People:**
    33|
    34|```mermaid
    35|C4Context
    36|    Person(user, "User", "Description")
    37|    Person_Ext(external, "External User", "Outside organization")
    38|```
    39|
    40|**Systems:**
    41|
    42|```mermaid
    43|C4Context
    44|    System(internal, "Internal System", "Description")
    45|    System_Ext(external, "External System", "Description")
    46|    SystemDb(database, "Database System", "Description")
    47|    SystemDb_Ext(external_db, "External DB", "Description")
    48|    SystemQueue(queue, "Message Queue", "Description")
    49|    SystemQueue_Ext(external_queue, "External Queue", "Description")
    50|```
    51|
    52|**Relationships:**
    53|
    54|```mermaid
    55|C4Context
    56|    Rel(from, to, "Label")
    57|    Rel(from, to, "Label", "Optional Technology")
    58|    BiRel(system1, system2, "Bidirectional")
    59|```
    60|
    61|### Comprehensive Context Example
    62|
    63|```mermaid
    64|C4Context
    65|    title System Context - E-Commerce Platform
    66|
    67|    Person(customer, "Customer", "Shops online")
    68|    Person(admin, "Administrator", "Manages products and orders")
    69|    Person_Ext(delivery, "Delivery Personnel", "Delivers orders")
    70|
    71|    System(ecommerce, "E-Commerce Platform", "Online shopping platform")
    72|
    73|    System_Ext(payment, "Payment Gateway", "Processes payments")
    74|    System_Ext(email, "Email Service", "Sends notifications")
    75|    System_Ext(sms, "SMS Service", "Sends SMS alerts")
    76|    System_Ext(analytics, "Analytics Platform", "Tracks user behavior")
    77|    SystemQueue_Ext(shipping, "Shipping API", "Calculates shipping rates")
    78|
    79|    Rel(customer, ecommerce, "Browses products, places orders")
    80|    Rel(admin, ecommerce, "Manages catalog, reviews orders")
    81|    Rel(delivery, ecommerce, "Updates delivery status")
    82|
    83|    Rel(ecommerce, payment, "Processes payments via", "HTTPS/REST")
    84|    Rel(ecommerce, email, "Sends emails via", "SMTP")
    85|    Rel(ecommerce, sms, "Sends SMS via", "REST API")
    86|    Rel(ecommerce, analytics, "Tracks events", "JavaScript SDK")
    87|    Rel(ecommerce, shipping, "Gets shipping rates", "REST API")
    88|
    89|    UpdateRelStyle(customer, ecommerce, $offsetX="-50", $offsetY="-30")
    90|    UpdateRelStyle(admin, ecommerce, $offsetX="50", $offsetY="-30")
    91|```
    92|
    93|## C4 Container Diagram
    94|
    95|Zooms into the system to show containers (applications, databases, services).
    96|
    97|### Basic Syntax
    98|
    99|```mermaid
   100|C4Container
   101|    title Container Diagram for Banking System
   102|
   103|    Person(customer, "Customer")
   104|
   105|    Container_Boundary(banking, "Banking System") {
   106|        Container(web, "Web Application", "React", "Delivers static content")
   107|        Container(api, "API Application", "Node.js", "Provides banking API")
   108|        ContainerDb(db, "Database", "PostgreSQL", "Stores account data")
   109|    }
   110|
   111|    Rel(customer, web, "Uses", "HTTPS")
   112|    Rel(web, api, "Makes API calls", "HTTPS/JSON")
   113|    Rel(api, db, "Reads/writes", "SQL/TCP")
   114|```
   115|
   116|### Container Elements
   117|
   118|```mermaid
   119|C4Container
   120|    Container(app, "Application", "Technology", "Description")
   121|    ContainerDb(db, "Database", "PostgreSQL", "Description")
   122|    ContainerQueue(queue, "Queue", "RabbitMQ", "Description")
   123|    Container_Ext(external, "External Service", "Tech", "Description")
   124|```
   125|
   126|### Container Boundaries
   127|
   128|```mermaid
   129|C4Container
   130|    Container_Boundary(boundary_name, "Boundary Label") {
   131|        Container(app1, "App 1", "Tech")
   132|        Container(app2, "App 2", "Tech")
   133|    }
   134|```
   135|
   136|### Comprehensive Container Example
   137|
   138|```mermaid
   139|C4Container
   140|    title Container Diagram - E-Commerce Platform
   141|
   142|    Person(customer, "Customer")
   143|    Person(admin, "Admin")
   144|    System_Ext(payment, "Payment Gateway")
   145|    System_Ext(email, "Email Service")
   146|
   147|    Container_Boundary(frontend, "Frontend") {
   148|        Container(web, "Web App", "React", "Delivers UI")
   149|        Container(mobile, "Mobile App", "React Native", "Mobile UI")
   150|    }
   151|
   152|    Container_Boundary(backend, "Backend Services") {
   153|        Container(api, "API Gateway", "Node.js/Express", "Routes requests")
   154|        Container(auth, "Auth Service", "Node.js", "Handles authentication")
   155|        Container(catalog, "Catalog Service", "Python/FastAPI", "Manages products")
   156|        Container(order, "Order Service", "Java/Spring", "Processes orders")
   157|        Container(notification, "Notification Service", "Node.js", "Sends notifications")
   158|    }
   159|
   160|    Container_Boundary(data, "Data Layer") {
   161|        ContainerDb(postgres, "Main Database", "PostgreSQL", "Stores core data")
   162|        ContainerDb(mongo, "Product DB", "MongoDB", "Product catalog")
   163|        ContainerDb(redis, "Cache", "Redis", "Session & caching")
   164|        ContainerQueue(queue, "Message Queue", "RabbitMQ", "Async processing")
   165|    }
   166|
   167|    Rel(customer, web, "Uses", "HTTPS")
   168|    Rel(customer, mobile, "Uses", "HTTPS")
   169|    Rel(admin, web, "Manages via", "HTTPS")
   170|
   171|    Rel(web, api, "Makes calls", "HTTPS/JSON")
   172|    Rel(mobile, api, "Makes calls", "HTTPS/JSON")
   173|
   174|    Rel(api, auth, "Authenticates", "gRPC")
   175|    Rel(api, catalog, "Gets products", "REST")
   176|    Rel(api, order, "Creates orders", "REST")
   177|
   178|    Rel(auth, postgres, "Reads/writes users", "SQL")
   179|    Rel(catalog, mongo, "Reads/writes products", "MongoDB Protocol")
   180|    Rel(order, postgres, "Reads/writes orders", "SQL")
   181|
   182|    Rel(auth, redis, "Stores sessions", "Redis Protocol")
   183|    Rel(api, redis, "Caches data", "Redis Protocol")
   184|
   185|    Rel(order, queue, "Publishes events", "AMQP")
   186|    Rel(notification, queue, "Consumes events", "AMQP")
   187|    Rel(notification, email, "Sends via", "SMTP")
   188|    Rel(order, payment, "Processes payment", "HTTPS/REST")
   189|```
   190|
   191|## C4 Component Diagram
   192|
   193|Zooms into a container to show its internal components.
   194|
   195|### Basic Syntax
   196|
   197|```mermaid
   198|C4Component
   199|    title Component Diagram for API Application
   200|
   201|    Container(web, "Web App", "React")
   202|    ContainerDb(db, "Database", "PostgreSQL")
   203|    System_Ext(email, "Email System")
   204|
   205|    Container_Boundary(api, "API Application") {
   206|        Component(controller, "Controller", "Express Router", "Handles HTTP")
   207|        Component(service, "Business Logic", "Service Layer", "Core logic")
   208|        Component(repository, "Data Access", "Repository", "DB operations")
   209|        Component(emailClient, "Email Client", "Client", "Sends emails")
   210|    }
   211|
   212|    Rel(web, controller, "Makes requests", "HTTPS")
   213|    Rel(controller, service, "Uses")
   214|    Rel(service, repository, "Uses")
   215|    Rel(repository, db, "Reads/writes", "SQL")
   216|    Rel(service, emailClient, "Sends emails via")
   217|    Rel(emailClient, email, "Sends", "SMTP")
   218|```
   219|
   220|### Comprehensive Component Example
   221|
   222|```mermaid
   223|C4Component
   224|    title Component Diagram - Order Service
   225|
   226|    Container(api_gateway, "API Gateway", "Node.js")
   227|    ContainerDb(postgres, "Database", "PostgreSQL")
   228|    ContainerQueue(queue, "Message Queue", "RabbitMQ")
   229|    System_Ext(payment, "Payment Gateway")
   230|    System_Ext(inventory, "Inventory Service")
   231|
   232|    Container_Boundary(order_service, "Order Service") {
   233|        Component(controller, "REST Controllers", "Spring MVC", "HTTP endpoints")
   234|        Component(order_logic, "Order Manager", "Service", "Order processing logic")
   235|        Component(payment_client, "Payment Client", "REST Client", "Payment integration")
   236|        Component(inventory_client, "Inventory Client", "REST Client", "Inventory integration")
   237|        Component(repository, "Order Repository", "JPA", "Database operations")
   238|        Component(event_publisher, "Event Publisher", "Component", "Publishes domain events")
   239|        Component(validator, "Order Validator", "Component", "Validates orders")
   240|    }
   241|
   242|    Rel(api_gateway, controller, "Routes requests", "HTTPS/REST")
   243|
   244|    Rel(controller, order_logic, "Delegates to")
   245|    Rel(controller, validator, "Validates with")
   246|
   247|    Rel(order_logic, payment_client, "Processes payment")
   248|    Rel(order_logic, inventory_client, "Checks stock")
   249|    Rel(order_logic, repository, "Persists orders")
   250|    Rel(order_logic, event_publisher, "Publishes events")
   251|
   252|    Rel(payment_client, payment, "Calls", "HTTPS/REST")
   253|    Rel(inventory_client, inventory, "Calls", "HTTPS/REST")
   254|    Rel(repository, postgres, "Reads/writes", "JDBC/SQL")
   255|    Rel(event_publisher, queue, "Publishes to", "AMQP")
   256|```
   257|
   258|## Microservices Architecture Example
   259|
   260|```mermaid
   261|C4Container
   262|    title Microservices Architecture - Streaming Platform
   263|
   264|    Person(user, "User", "Platform user")
   265|    Person(creator, "Content Creator", "Uploads videos")
   266|    System_Ext(cdn, "CDN", "Delivers media")
   267|    System_Ext(storage, "Object Storage", "Stores videos")
   268|    System_Ext(transcoding, "Transcoding Service", "Processes videos")
   269|
   270|    Container_Boundary(frontend, "Frontend Layer") {
   271|        Container(web, "Web Application", "Next.js", "Server-rendered UI")
   272|        Container(mobile, "Mobile Apps", "React Native", "iOS/Android apps")
   273|    }
   274|
   275|    Container_Boundary(api_layer, "API Layer") {
   276|        Container(api_gateway, "API Gateway", "Kong", "Routing, auth, rate limiting")
   277|        Container(graphql, "GraphQL Gateway", "Apollo", "Unified API")
   278|    }
   279|
   280|    Container_Boundary(services, "Microservices") {
   281|        Container(auth, "Auth Service", "Go", "Authentication & authorization")
   282|        Container(user, "User Service", "Node.js", "User profiles & preferences")
   283|        Container(video, "Video Service", "Python", "Video metadata & management")
   284|        Container(recommendation, "Recommendation Engine", "Python/ML", "Content recommendations")
   285|        Container(analytics, "Analytics Service", "Go", "View tracking & metrics")
   286|        Container(search, "Search Service", "Elasticsearch", "Content search")
   287|        Container(comment, "Comment Service", "Node.js", "Comments & discussions")
   288|    }
   289|
   290|    Container_Boundary(data, "Data Layer") {
   291|        ContainerDb(user_db, "User Database", "PostgreSQL", "User data")
   292|        ContainerDb(video_db, "Video Database", "MongoDB", "Video metadata")
   293|        ContainerDb(analytics_db, "Analytics DB", "ClickHouse", "Analytics data")
   294|        ContainerDb(cache, "Cache Layer", "Redis Cluster", "Caching & sessions")
   295|        ContainerQueue(event_bus, "Event Bus", "Kafka", "Event streaming")
   296|        ContainerDb(search_index, "Search Index", "Elasticsearch", "Search data")
   297|    }
   298|
   299|    Rel(user, web, "Uses", "HTTPS")
   300|    Rel(creator, web, "Uploads via", "HTTPS")
   301|    Rel(user, mobile, "Uses", "HTTPS")
   302|
   303|    Rel(web, api_gateway, "API calls", "HTTPS/REST")
   304|    Rel(mobile, api_gateway, "API calls", "HTTPS/REST")
   305|    Rel(web, graphql, "Queries", "HTTPS/GraphQL")
   306|
   307|    Rel(api_gateway, auth, "Authenticates", "gRPC")
   308|    Rel(graphql, video, "Gets videos", "gRPC")
   309|    Rel(graphql, user, "Gets users", "gRPC")
   310|    Rel(graphql, recommendation, "Gets recommendations", "gRPC")
   311|
   312|    Rel(video, storage, "Stores videos", "S3 API")
   313|    Rel(video, transcoding, "Sends for transcoding", "REST")
   314|    Rel(video, cdn, "Publishes to", "API")
   315|
   316|    Rel(auth, user_db, "Manages credentials", "SQL")
   317|    Rel(user, user_db, "Stores profiles", "SQL")
   318|    Rel(video, video_db, "Stores metadata", "MongoDB")
   319|    Rel(analytics, analytics_db, "Stores metrics", "SQL")
   320|
   321|    Rel(auth, cache, "Sessions", "Redis")
   322|    Rel(video, cache, "Caches metadata", "Redis")
   323|    Rel(search, search_index, "Indexes & queries", "REST")
   324|
   325|    Rel(video, event_bus, "Publishes VideoUploaded", "Kafka")
   326|    Rel(analytics, event_bus, "Publishes ViewStarted", "Kafka")
   327|    Rel(recommendation, event_bus, "Consumes events", "Kafka")
   328|    Rel(search, event_bus, "Consumes events", "Kafka")
   329|```
   330|
   331|## Best Practices
   332|
   333|1. **Use appropriate level** - Context for stakeholders, Container for architects, Component for developers
   334|2. **Keep it focused** - One system per Context diagram, one container per Component diagram
   335|3. **Show key relationships** - Don't clutter with every possible connection
   336|4. **Use consistent naming** - Same names across all diagram levels
   337|5. **Add technology details** - Specify frameworks, languages, protocols at Container/Component level
   338|6. **Update regularly** - Keep diagrams in sync with architecture
   339|7. **Use boundaries** - Group related containers/components logically
   340|8. **Document protocols** - Show communication methods (REST, gRPC, messaging)
   341|9. **Highlight external systems** - Use \*\_Ext variants for clarity
   342|10. **Start simple** - Begin with Context, drill down as needed
   343|
   344|## Common Architecture Patterns
   345|
   346|### Monolithic Application
   347|
   348|```mermaid
   349|C4Container
   350|    Person(user, "User")
   351|
   352|    Container_Boundary(system, "Application") {
   353|        Container(app, "Web Application", "Ruby on Rails", "Monolithic application")
   354|        ContainerDb(db, "Database", "PostgreSQL", "Application database")
   355|        ContainerDb(cache, "Cache", "Redis", "Session store")
   356|    }
   357|
   358|    Rel(user, app, "Uses", "HTTPS")
   359|    Rel(app, db, "Reads/writes", "SQL")
   360|    Rel(app, cache, "Caches", "Redis Protocol")
   361|```
   362|
   363|### Three-Tier Architecture
   364|
   365|```mermaid
   366|C4Container
   367|    Person(user, "User")
   368|
   369|    Container_Boundary(presentation, "Presentation Tier") {
   370|        Container(web, "Web Server", "Nginx", "Static content")
   371|        Container(app, "App Server", "Node.js", "Application logic")
   372|    }
   373|
   374|    Container_Boundary(business, "Business Tier") {
   375|        Container(api, "API Server", "Java", "Business logic")
   376|    }
   377|
   378|    Container_Boundary(data, "Data Tier") {
   379|        ContainerDb(db, "Database", "MySQL", "Data storage")
   380|    }
   381|
   382|    Rel(user, web, "Uses", "HTTPS")
   383|    Rel(web, app, "Proxies to", "HTTP")
   384|    Rel(app, api, "Calls", "REST")
   385|    Rel(api, db, "Reads/writes", "SQL")
   386|```
   387|
   388|### Event-Driven Architecture
   389|
   390|```mermaid
   391|C4Container
   392|    Person(user, "User")
   393|
   394|    Container(frontend, "Frontend", "React", "User interface")
   395|    Container(api, "API Gateway", "Kong", "API routing")
   396|
   397|    Container_Boundary(services, "Services") {
   398|        Container(order, "Order Service", "Java", "Order processing")
   399|        Container(inventory, "Inventory Service", "Go", "Stock management")
   400|        Container(notification, "Notification Service", "Node.js", "Alerts")
   401|    }
   402|
   403|    ContainerQueue(events, "Event Bus", "Kafka", "Event streaming")
   404|    ContainerDb(db, "Databases", "Various", "Service databases")
   405|
   406|    Rel(user, frontend, "Uses")
   407|    Rel(frontend, api, "Calls")
   408|    Rel(api, order, "Routes to")
   409|
   410|    Rel(order, events, "Publishes OrderCreated")
   411|    Rel(events, inventory, "Consumes events")
   412|    Rel(events, notification, "Consumes events")
   413|
   414|    Rel(order, db, "Persists")
   415|    Rel(inventory, db, "Persists")
   416|```
   417|