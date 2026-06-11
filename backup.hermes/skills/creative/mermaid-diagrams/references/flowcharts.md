---
name: mermaid-diagrams-flowcharts
description: "Flowcharts"
version: 1.0.0
author: Alexa
---
     1|# Flowcharts
     2|
     3|Flowcharts visualize processes, algorithms, decision trees, and user journeys. They show step-by-step progression through a system or workflow.
     4|
     5|## Basic Syntax
     6|
     7|```mermaid
     8|flowchart TD
     9|    A --> B
    10|```
    11|
    12|**Directions:**
    13|
    14|- `TD` or `TB` - Top to Bottom (default)
    15|- `BT` - Bottom to Top
    16|- `LR` - Left to Right
    17|- `RL` - Right to Left
    18|
    19|## Node Shapes
    20|
    21|### Rectangle (default)
    22|
    23|```mermaid
    24|flowchart LR
    25|    A[Process step]
    26|```
    27|
    28|### Rounded Rectangle
    29|
    30|```mermaid
    31|flowchart LR
    32|    B([Rounded process])
    33|```
    34|
    35|### Stadium/Pill Shape
    36|
    37|```mermaid
    38|flowchart LR
    39|    C(Start or End)
    40|```
    41|
    42|### Subroutine (Double Border)
    43|
    44|```mermaid
    45|flowchart LR
    46|    D[[Subroutine]]
    47|```
    48|
    49|### Cylindrical (Database)
    50|
    51|```mermaid
    52|flowchart LR
    53|    E[(Database)]
    54|```
    55|
    56|### Circle
    57|
    58|```mermaid
    59|flowchart LR
    60|    F((Circle node))
    61|```
    62|
    63|### Asymmetric/Flag
    64|
    65|```mermaid
    66|flowchart LR
    67|    G>Flag node]
    68|```
    69|
    70|### Rhombus (Decision)
    71|
    72|```mermaid
    73|flowchart LR
    74|    H{Decision?}
    75|```
    76|
    77|### Hexagon
    78|
    79|```mermaid
    80|flowchart LR
    81|    I{{Hexagon}}
    82|```
    83|
    84|### Parallelogram (Input/Output)
    85|
    86|```mermaid
    87|flowchart LR
    88|    J[/Input or Output/]
    89|    K[\Alternative IO\]
    90|```
    91|
    92|### Trapezoid
    93|
    94|```mermaid
    95|flowchart LR
    96|    L[/Trapezoid\]
    97|    M[\Alt trapezoid/]
    98|```
    99|
   100|## Connections
   101|
   102|### Basic Arrow
   103|
   104|```mermaid
   105|flowchart LR
   106|    A --> B
   107|```
   108|
   109|### Open Link (No Arrow)
   110|
   111|```mermaid
   112|flowchart LR
   113|    A --- B
   114|```
   115|
   116|### Text on Links
   117|
   118|```mermaid
   119|flowchart LR
   120|    A -->|Label text| B
   121|    C ---|"Text with spaces"| D
   122|```
   123|
   124|### Dotted Links
   125|
   126|```mermaid
   127|flowchart LR
   128|    A -.-> B
   129|    C -.- D
   130|    E -.Label.-> F
   131|```
   132|
   133|### Thick Links
   134|
   135|```mermaid
   136|flowchart LR
   137|    A ==> B
   138|    C === D
   139|    E ==Label==> F
   140|```
   141|
   142|### Chaining
   143|
   144|```mermaid
   145|flowchart LR
   146|    A --> B --> C --> D
   147|    E --> F & G --> H
   148|```
   149|
   150|### Multi-directional
   151|
   152|```mermaid
   153|flowchart LR
   154|    A --> B & C & D
   155|    B & C & D --> E
   156|```
   157|
   158|## Subgraphs
   159|
   160|Group related nodes:
   161|
   162|```mermaid
   163|flowchart TB
   164|    A[Start]
   165|
   166|    subgraph Processing
   167|        B[Step 1]
   168|        C[Step 2]
   169|        D[Step 3]
   170|    end
   171|
   172|    E[End]
   173|
   174|    A --> B
   175|    D --> E
   176|```
   177|
   178|### Nested Subgraphs
   179|
   180|```mermaid
   181|flowchart TB
   182|    subgraph Outer
   183|        A[Node A]
   184|
   185|        subgraph Inner
   186|            B[Node B]
   187|            C[Node C]
   188|        end
   189|    end
   190|```
   191|
   192|### Subgraph Direction
   193|
   194|```mermaid
   195|flowchart LR
   196|    subgraph one
   197|        direction TB
   198|        A1 --> A2
   199|    end
   200|
   201|    subgraph two
   202|        direction TB
   203|        B1 --> B2
   204|    end
   205|
   206|    one --> two
   207|```
   208|
   209|## Styling
   210|
   211|### Individual Node Styling
   212|
   213|```mermaid
   214|flowchart LR
   215|    A[Normal]
   216|    B[Styled]
   217|
   218|    style B fill:#ff6b6b,stroke:#333,stroke-width:4px,color:#fff
   219|```
   220|
   221|### Class-based Styling
   222|
   223|```mermaid
   224|flowchart LR
   225|    A[Node 1]:::className
   226|    B[Node 2]:::className
   227|    C[Node 3]
   228|
   229|    classDef className fill:#f9f,stroke:#333,stroke-width:2px
   230|```
   231|
   232|### Link Styling
   233|
   234|```mermaid
   235|flowchart LR
   236|    A --> B
   237|    linkStyle 0 stroke:#ff3,stroke-width:4px,color:red
   238|```
   239|
   240|## Comprehensive Example: User Registration Flow
   241|
   242|```mermaid
   243|flowchart TD
   244|    Start([User visits registration page]) --> Form[Show registration form]
   245|    Form --> Input[User enters details]
   246|    Input --> Validate{Valid input?}
   247|
   248|    Validate -->|No| ShowError[Show validation errors]
   249|    ShowError --> Form
   250|
   251|    Validate -->|Yes| CheckEmail{Email exists?}
   252|
   253|    CheckEmail -->|Yes| EmailError[Show 'Email already registered']
   254|    EmailError --> Form
   255|
   256|    CheckEmail -->|No| CreateAccount[Create user account]
   257|    CreateAccount --> Hash[Hash password]
   258|    Hash --> SaveDB[(Save to database)]
   259|    SaveDB --> GenerateToken[Generate verification token]
   260|    GenerateToken --> SendEmail[Send verification email]
   261|    SendEmail --> ShowSuccess[Show success message]
   262|    ShowSuccess --> End([Redirect to login])
   263|
   264|    style Start fill:#90EE90,stroke:#333,stroke-width:2px
   265|    style End fill:#90EE90,stroke:#333,stroke-width:2px
   266|    style CreateAccount fill:#87CEEB,stroke:#333,stroke-width:2px
   267|    style SaveDB fill:#FFD700,stroke:#333,stroke-width:2px
   268|```
   269|
   270|## Algorithm Example: Binary Search
   271|
   272|```mermaid
   273|flowchart TD
   274|    Start([Start Binary Search]) --> Init[Set low = 0, high = array.length - 1]
   275|    Init --> Check{low <= high?}
   276|
   277|    Check -->|No| NotFound[Return -1: Not found]
   278|    NotFound --> End([End])
   279|
   280|    Check -->|Yes| CalcMid[mid = low + (high - low) / 2]
   281|    CalcMid --> Compare{array[mid] == target?}
   282|
   283|    Compare -->|Yes| Found[Return mid: Found]
   284|    Found --> End
   285|
   286|    Compare -->|No| CheckLess{array[mid] < target?}
   287|
   288|    CheckLess -->|Yes| MoveLow[low = mid + 1]
   289|    MoveLow --> Check
   290|
   291|    CheckLess -->|No| MoveHigh[high = mid - 1]
   292|    MoveHigh --> Check
   293|
   294|    style Start fill:#90EE90
   295|    style End fill:#90EE90
   296|    style Found fill:#FFD700
   297|    style NotFound fill:#FF6B6B
   298|```
   299|
   300|## CI/CD Pipeline
   301|
   302|```mermaid
   303|flowchart LR
   304|    subgraph Development
   305|        Commit[Developer commits code] --> Push[Push to repository]
   306|    end
   307|
   308|    subgraph CI
   309|        Push --> Trigger[Trigger CI pipeline]
   310|        Trigger --> Checkout[Checkout code]
   311|        Checkout --> Install[Install dependencies]
   312|        Install --> Lint[Run linters]
   313|        Lint --> Test[Run tests]
   314|        Test --> Build[Build application]
   315|    end
   316|
   317|    subgraph QA
   318|        Build --> DeployStaging[Deploy to staging]
   319|        DeployStaging --> E2E[Run E2E tests]
   320|        E2E --> ManualQA{Manual QA approval?}
   321|    end
   322|
   323|    subgraph Production
   324|        ManualQA -->|Approved| DeployProd[Deploy to production]
   325|        DeployProd --> HealthCheck{Health check passed?}
   326|        HealthCheck -->|Yes| Success([Deployment successful])
   327|        HealthCheck -->|No| Rollback[Rollback deployment]
   328|        Rollback --> Alert[Alert team]
   329|    end
   330|
   331|    ManualQA -->|Rejected| FixIssues[Fix issues]
   332|    FixIssues --> Development
   333|
   334|    Test -->|Failed| NotifyDev[Notify developer]
   335|    NotifyDev --> FixIssues
   336|```
   337|
   338|## E-Commerce Checkout Flow
   339|
   340|```mermaid
   341|flowchart TD
   342|    Start([User clicks Checkout]) --> Auth{Authenticated?}
   343|
   344|    Auth -->|No| Login[Redirect to login]
   345|    Login --> Auth
   346|
   347|    Auth -->|Yes| Cart{Cart empty?}
   348|    Cart -->|Yes| EmptyCart[Show empty cart message]
   349|    EmptyCart --> Browse[Redirect to products]
   350|
   351|    Cart -->|No| Address[Show shipping address form]
   352|    Address --> ValidateAddr{Valid address?}
   353|    ValidateAddr -->|No| Address
   354|    ValidateAddr -->|Yes| Shipping[Select shipping method]
   355|
   356|    Shipping --> Payment[Enter payment details]
   357|    Payment --> ValidatePayment{Valid payment info?}
   358|    ValidatePayment -->|No| Payment
   359|
   360|    ValidatePayment -->|Yes| Review[Show order review]
   361|    Review --> Confirm{Confirm order?}
   362|
   363|    Confirm -->|No| Edit{Edit what?}
   364|    Edit -->|Address| Address
   365|    Edit -->|Shipping| Shipping
   366|    Edit -->|Payment| Payment
   367|
   368|    Confirm -->|Yes| ProcessPayment[Process payment]
   369|    ProcessPayment --> PaymentResult{Payment successful?}
   370|
   371|    PaymentResult -->|No| PaymentError[Show payment error]
   372|    PaymentError --> RetryPayment{Retry?}
   373|    RetryPayment -->|Yes| Payment
   374|    RetryPayment -->|No| Cancel([Order cancelled])
   375|
   376|    PaymentResult -->|Yes| CreateOrder[(Create order record)]
   377|    CreateOrder --> ReduceStock[Reduce inventory]
   378|    ReduceStock --> SendConfirmation[Send confirmation email]
   379|    SendConfirmation --> Success([Order complete - Show confirmation])
   380|
   381|    style Start fill:#90EE90
   382|    style Success fill:#90EE90
   383|    style Cancel fill:#FF6B6B
   384|    style CreateOrder fill:#FFD700
   385|```
   386|
   387|## Decision Matrix Example
   388|
   389|```mermaid
   390|flowchart TD
   391|    Start([Select deployment strategy]) --> Env{Environment?}
   392|
   393|    Env -->|Development| DevDecision{Automated tests?}
   394|    DevDecision -->|Pass| DevDeploy[Auto-deploy to dev]
   395|    DevDecision -->|Fail| Block[Block deployment]
   396|
   397|    Env -->|Staging| StageDecision{All checks pass?}
   398|    StageDecision -->|Yes| StageDeploy[Deploy to staging]
   399|    StageDecision -->|No| Block
   400|
   401|    Env -->|Production| ProdDecision{Change type?}
   402|
   403|    ProdDecision -->|Hotfix| Urgent{Critical bug?}
   404|    Urgent -->|Yes| FastTrack[Emergency approval + deploy]
   405|    Urgent -->|No| NormalProcess
   406|
   407|    ProdDecision -->|Feature| NormalProcess{Approval status?}
   408|    NormalProcess -->|Approved| Schedule{Deploy window?}
   409|    NormalProcess -->|Pending| Wait[Wait for approval]
   410|    NormalProcess -->|Rejected| Block
   411|
   412|    Schedule -->|Now| ImmediateDeploy[Deploy immediately]
   413|    Schedule -->|Scheduled| QueueDeploy[Queue for deploy window]
   414|
   415|    DevDeploy --> Monitor[Monitor metrics]
   416|    StageDeploy --> Monitor
   417|    FastTrack --> Monitor
   418|    ImmediateDeploy --> Monitor
   419|    QueueDeploy --> Monitor
   420|
   421|    Monitor --> End([Deployment complete])
   422|    Block --> End
   423|    Wait --> End
   424|```
   425|
   426|## Best Practices
   427|
   428|1. **Use meaningful labels** - Node text should be clear and action-oriented
   429|2. **Consistent node shapes** - Same shapes for same types of actions
   430|3. **Decision nodes as diamonds** - Standard convention for yes/no decisions
   431|4. **Flow top-to-bottom or left-to-right** - Natural reading direction
   432|5. **Start and end nodes** - Use stadium/pill shapes to mark entry/exit
   433|6. **Group related steps** - Use subgraphs for logical groupings
   434|7. **Color code** - Use colors to highlight different types of actions
   435|8. **Minimize crossing lines** - Reorganize for clarity
   436|9. **Keep it focused** - One process per diagram
   437|
   438|## Common Patterns
   439|
   440|### Simple Linear Flow
   441|
   442|```mermaid
   443|flowchart LR
   444|    A[Step 1] --> B[Step 2] --> C[Step 3] --> D[Step 4]
   445|```
   446|
   447|### Branching Decision
   448|
   449|```mermaid
   450|flowchart TD
   451|    A[Input] --> B{Condition?}
   452|    B -->|True| C[Path 1]
   453|    B -->|False| D[Path 2]
   454|    C --> E[Merge]
   455|    D --> E
   456|```
   457|
   458|### Loop Pattern
   459|
   460|```mermaid
   461|flowchart TD
   462|    A[Initialize] --> B[Process]
   463|    B --> C{Continue?}
   464|    C -->|Yes| B
   465|    C -->|No| D[Exit]
   466|```
   467|
   468|### Error Handling
   469|
   470|```mermaid
   471|flowchart TD
   472|    A[Try operation] --> B{Success?}
   473|    B -->|Yes| C[Continue]
   474|    B -->|No| D[Handle error]
   475|    D --> E{Retry?}
   476|    E -->|Yes| A
   477|    E -->|No| F[Abort]
   478|```
   479|