---
name: mermaid-diagrams-class-diagrams
description: "Class Diagrams"
version: 1.0.0
author: Alexa
---
     1|# Class Diagrams
     2|
     3|Class diagrams model object-oriented designs and domain models. They show entities (classes), their attributes/methods, and relationships.
     4|
     5|## Basic Syntax
     6|
     7|```mermaid
     8|classDiagram
     9|    ClassName
    10|```
    11|
    12|## Defining Classes with Members
    13|
    14|```mermaid
    15|classDiagram
    16|    class BankAccount {
    17|        +String owner
    18|        +Decimal balance
    19|        -String accountNumber
    20|        +deposit(amount)
    21|        +withdraw(amount)
    22|        +getBalance() Decimal
    23|    }
    24|```
    25|
    26|**Visibility modifiers:**
    27|
    28|- `+` Public
    29|- `-` Private
    30|- `#` Protected
    31|- `~` Package/Internal
    32|
    33|**Member syntax:**
    34|
    35|- `+type attribute` - Attribute with type
    36|- `+method(params) ReturnType` - Method with parameters and return type
    37|
    38|## Relationships
    39|
    40|### Association (`--`)
    41|
    42|Loose relationship where entities use each other but exist independently.
    43|
    44|```mermaid
    45|classDiagram
    46|    Title -- Genre
    47|```
    48|
    49|### Composition (`*--`)
    50|
    51|Strong ownership - child cannot exist without parent. When parent is deleted, children are deleted.
    52|
    53|```mermaid
    54|classDiagram
    55|    Order *-- LineItem
    56|    House *-- Room
    57|```
    58|
    59|### Aggregation (`o--`)
    60|
    61|Weaker ownership - child can exist independently. Represents "has-a" relationship.
    62|
    63|```mermaid
    64|classDiagram
    65|    Department o-- Employee
    66|    Playlist o-- Song
    67|```
    68|
    69|### Inheritance (`<|--`)
    70|
    71|"Is-a" relationship. Child class inherits from parent class.
    72|
    73|```mermaid
    74|classDiagram
    75|    Animal <|-- Dog
    76|    Animal <|-- Cat
    77|
    78|    class Animal {
    79|        +String name
    80|        +makeSound()
    81|    }
    82|
    83|    class Dog {
    84|        +bark()
    85|    }
    86|```
    87|
    88|### Dependency (`<..`)
    89|
    90|One class depends on another, often as a parameter or local variable.
    91|
    92|```mermaid
    93|classDiagram
    94|    OrderProcessor <.. PaymentGateway
    95|```
    96|
    97|### Realization/Implementation (`<|..`)
    98|
    99|Class implements an interface.
   100|
   101|```mermaid
   102|classDiagram
   103|    class Drawable {
   104|        <<interface>>
   105|        +draw()
   106|    }
   107|    Drawable <|.. Circle
   108|    Drawable <|.. Rectangle
   109|```
   110|
   111|## Multiplicity
   112|
   113|Show how many instances participate in a relationship:
   114|
   115|```mermaid
   116|classDiagram
   117|    Customer "1" --> "0..*" Order : places
   118|    Order "1" *-- "1..*" LineItem : contains
   119|    Author "1..*" -- "1..*" Book : writes
   120|```
   121|
   122|**Common multiplicities:**
   123|
   124|- `1` - Exactly one
   125|- `0..1` - Zero or one
   126|- `0..*` or `*` - Zero or many
   127|- `1..*` - One or many
   128|- `m..n` - Between m and n
   129|
   130|## Relationship Labels
   131|
   132|```mermaid
   133|classDiagram
   134|    Customer --> Order : places
   135|    Order --> Product : contains
   136|    Driver --> Vehicle : drives
   137|```
   138|
   139|## Class Stereotypes
   140|
   141|Mark special class types:
   142|
   143|```mermaid
   144|classDiagram
   145|    class IRepository {
   146|        <<interface>>
   147|        +save(entity)
   148|        +findById(id)
   149|    }
   150|
   151|    class UserService {
   152|        <<service>>
   153|        +createUser()
   154|    }
   155|
   156|    class UserDTO {
   157|        <<dataclass>>
   158|        +String name
   159|        +String email
   160|    }
   161|```
   162|
   163|## Abstract Classes and Methods
   164|
   165|```mermaid
   166|classDiagram
   167|    class Shape {
   168|        <<abstract>>
   169|        +int x
   170|        +int y
   171|        +draw()* abstract
   172|        +move(x, y)
   173|    }
   174|
   175|    Shape <|-- Circle
   176|    Shape <|-- Rectangle
   177|```
   178|
   179|## Generic Classes
   180|
   181|```mermaid
   182|classDiagram
   183|    class List~T~ {
   184|        +add(item: T)
   185|        +get(index: int) T
   186|    }
   187|
   188|    List~String~ <-- StringProcessor
   189|```
   190|
   191|## Comprehensive Example: E-Commerce Domain
   192|
   193|```mermaid
   194|classDiagram
   195|    %% Core entities
   196|    class Customer {
   197|        +UUID id
   198|        +String email
   199|        +String name
   200|        +Address shippingAddress
   201|        +placeOrder(cart: Cart) Order
   202|        +getOrderHistory() List~Order~
   203|    }
   204|
   205|    class Order {
   206|        +UUID id
   207|        +DateTime orderDate
   208|        +OrderStatus status
   209|        +Decimal total
   210|        +calculateTotal() Decimal
   211|        +ship()
   212|        +cancel()
   213|    }
   214|
   215|    class LineItem {
   216|        +int quantity
   217|        +Decimal pricePerUnit
   218|        +getSubtotal() Decimal
   219|    }
   220|
   221|    class Product {
   222|        +UUID id
   223|        +String name
   224|        +String description
   225|        +Decimal price
   226|        +int stockQuantity
   227|        +reduceStock(quantity: int)
   228|        +isAvailable() bool
   229|    }
   230|
   231|    class Category {
   232|        +String name
   233|        +String description
   234|    }
   235|
   236|    class Cart {
   237|        +addItem(product: Product, quantity: int)
   238|        +removeItem(product: Product)
   239|        +getTotal() Decimal
   240|        +clear()
   241|    }
   242|
   243|    %% Relationships
   244|    Customer "1" --> "0..*" Order : places
   245|    Customer "1" --> "1" Cart : has
   246|    Order "1" *-- "1..*" LineItem : contains
   247|    LineItem "1" --> "1" Product : references
   248|    Product "0..*" --> "1" Category : belongs to
   249|    Cart "1" o-- "0..*" Product : contains
   250|
   251|    %% Enums
   252|    class OrderStatus {
   253|        <<enumeration>>
   254|        PENDING
   255|        PAID
   256|        SHIPPED
   257|        DELIVERED
   258|        CANCELLED
   259|    }
   260|
   261|    Order --> OrderStatus
   262|```
   263|
   264|## Domain-Driven Design Patterns
   265|
   266|### Entities
   267|
   268|```mermaid
   269|classDiagram
   270|    class User {
   271|        <<entity>>
   272|        -UUID id
   273|        +String email
   274|        +String name
   275|    }
   276|```
   277|
   278|### Value Objects
   279|
   280|```mermaid
   281|classDiagram
   282|    class Money {
   283|        <<value object>>
   284|        +Decimal amount
   285|        +String currency
   286|        +add(other: Money) Money
   287|    }
   288|
   289|    class Address {
   290|        <<value object>>
   291|        +String street
   292|        +String city
   293|        +String postalCode
   294|    }
   295|```
   296|
   297|### Aggregates
   298|
   299|```mermaid
   300|classDiagram
   301|    class Order {
   302|        <<aggregate root>>
   303|        -UUID id
   304|        +addLineItem(item)
   305|        +removeLineItem(item)
   306|    }
   307|
   308|    Order *-- LineItem
   309|```
   310|
   311|## Tips for Effective Class Diagrams
   312|
   313|1. **Start with core entities** - Add attributes and methods incrementally
   314|2. **Show only relevant details** - Omit obvious getters/setters unless important
   315|3. **Use appropriate relationships** - Choose between association, aggregation, and composition carefully
   316|4. **Add multiplicity** - Clarifies how many instances participate
   317|5. **Group related classes** - Use notes or visual proximity
   318|6. **Document invariants** - Use notes to explain business rules
   319|
   320|## Common Patterns
   321|
   322|### Repository Pattern
   323|
   324|```mermaid
   325|classDiagram
   326|    class IRepository~T~ {
   327|        <<interface>>
   328|        +save(entity: T)
   329|        +findById(id: UUID) T
   330|        +delete(entity: T)
   331|    }
   332|
   333|    class UserRepository {
   334|        +findByEmail(email: String) User
   335|    }
   336|
   337|    IRepository~User~ <|.. UserRepository
   338|```
   339|
   340|### Factory Pattern
   341|
   342|```mermaid
   343|classDiagram
   344|    class ShapeFactory {
   345|        +createShape(type: String) Shape
   346|    }
   347|
   348|    class Shape {
   349|        <<abstract>>
   350|        +draw()*
   351|    }
   352|
   353|    ShapeFactory ..> Shape : creates
   354|    Shape <|-- Circle
   355|    Shape <|-- Rectangle
   356|```
   357|
   358|### Strategy Pattern
   359|
   360|```mermaid
   361|classDiagram
   362|    class PaymentProcessor {
   363|        -PaymentStrategy strategy
   364|        +setStrategy(strategy: PaymentStrategy)
   365|        +processPayment(amount: Decimal)
   366|    }
   367|
   368|    class PaymentStrategy {
   369|        <<interface>>
   370|        +pay(amount: Decimal)*
   371|    }
   372|
   373|    PaymentStrategy <|.. CreditCardPayment
   374|    PaymentStrategy <|.. PayPalPayment
   375|    PaymentProcessor --> PaymentStrategy
   376|```
   377|