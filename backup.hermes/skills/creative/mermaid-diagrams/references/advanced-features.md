---
name: mermaid-diagrams-advanced-features
description: "Advanced Mermaid Features"
version: 1.0.0
author: Alexa
---
     1|# Advanced Mermaid Features
     2|
     3|Advanced configuration, styling, theming, and other powerful features for creating professional diagrams.
     4|
     5|## Frontmatter Configuration
     6|
     7|Add YAML configuration at the top of diagrams:
     8|
     9|```mermaid
    10|---
    11|config:
    12|  theme: dark
    13|  themeVariables:
    14|    primaryColor: "#ff6b6b"
    15|    primaryTextColor: "#fff"
    16|    primaryBorderColor: "#333"
    17|    lineColor: "#666"
    18|    secondaryColor: "#4ecdc4"
    19|    tertiaryColor: "#ffe66d"
    20|---
    21|flowchart TD
    22|    A --> B
    23|```
    24|
    25|## Themes
    26|
    27|### Built-in Themes
    28|
    29|```mermaid
    30|---
    31|config:
    32|  theme: default
    33|---
    34|```
    35|
    36|**Available themes:**
    37|
    38|- `default` - Standard blue theme
    39|- `forest` - Green earth tones
    40|- `dark` - Dark mode friendly
    41|- `neutral` - Grayscale professional
    42|- `base` - Minimal base theme for customization
    43|
    44|### Theme Examples
    45|
    46|**Default Theme:**
    47|
    48|```mermaid
    49|---
    50|config:
    51|  theme: default
    52|---
    53|flowchart LR
    54|    A[Start] --> B[Process]
    55|    B --> C{Decision}
    56|    C -->|Yes| D[Action 1]
    57|    C -->|No| E[Action 2]
    58|```
    59|
    60|**Dark Theme:**
    61|
    62|```mermaid
    63|---
    64|config:
    65|  theme: dark
    66|---
    67|flowchart LR
    68|    A[Start] --> B[Process]
    69|    B --> C{Decision}
    70|```
    71|
    72|**Forest Theme:**
    73|
    74|```mermaid
    75|---
    76|config:
    77|  theme: forest
    78|---
    79|flowchart LR
    80|    A[Start] --> B[Process]
    81|```
    82|
    83|## Custom Theme Variables
    84|
    85|Override specific colors:
    86|
    87|```mermaid
    88|---
    89|config:
    90|  theme: base
    91|  themeVariables:
    92|    primaryColor: "#ff6b6b"
    93|    primaryTextColor: "#fff"
    94|    primaryBorderColor: "#d63031"
    95|    lineColor: "#74b9ff"
    96|    secondaryColor: "#00b894"
    97|    tertiaryColor: "#fdcb6e"
    98|    background: "#f0f0f0"
    99|    mainBkg: "#ffffff"
   100|    textColor: "#333333"
   101|    nodeBorder: "#333333"
   102|    clusterBkg: "#f9f9f9"
   103|    clusterBorder: "#666666"
   104|---
   105|flowchart TD
   106|    A --> B --> C
   107|```
   108|
   109|## Layout Options
   110|
   111|### Dagre Layout (Default)
   112|
   113|```mermaid
   114|---
   115|config:
   116|  layout: dagre
   117|---
   118|flowchart TD
   119|    A --> B
   120|```
   121|
   122|### ELK Layout (Advanced)
   123|
   124|For complex diagrams with better automatic layout:
   125|
   126|```mermaid
   127|---
   128|config:
   129|  layout: elk
   130|  elk:
   131|    mergeEdges: true
   132|    nodePlacementStrategy: BRANDES_KOEPF
   133|---
   134|flowchart TD
   135|    A --> B
   136|```
   137|
   138|**ELK node placement strategies:**
   139|
   140|- `SIMPLE` - Basic placement
   141|- `NETWORK_SIMPLEX` - Network optimization
   142|- `LINEAR_SEGMENTS` - Linear arrangement
   143|- `BRANDES_KOEPF` - Balanced (default)
   144|
   145|## Look Options
   146|
   147|### Classic Look
   148|
   149|Traditional Mermaid appearance:
   150|
   151|```mermaid
   152|---
   153|config:
   154|  look: classic
   155|---
   156|flowchart LR
   157|    A --> B --> C
   158|```
   159|
   160|### Hand-Drawn Look
   161|
   162|Sketch-like, informal style:
   163|
   164|```mermaid
   165|---
   166|config:
   167|  look: handDrawn
   168|---
   169|flowchart LR
   170|    A --> B --> C
   171|```
   172|
   173|## Complete Configuration Example
   174|
   175|```mermaid
   176|---
   177|config:
   178|  theme: base
   179|  look: handDrawn
   180|  layout: dagre
   181|  themeVariables:
   182|    primaryColor: "#ff6b6b"
   183|    primaryTextColor: "#fff"
   184|    primaryBorderColor: "#d63031"
   185|    lineColor: "#74b9ff"
   186|    secondaryColor: "#00b894"
   187|    tertiaryColor: "#fdcb6e"
   188|---
   189|flowchart TD
   190|    Start([Begin Process]) --> Input[Gather Data]
   191|    Input --> Process{Valid?}
   192|    Process -->|Yes| Store[(Save to DB)]
   193|    Process -->|No| Error[Show Error]
   194|    Store --> Notify[Send Notification]
   195|    Error --> Input
   196|    Notify --> End([Complete])
   197|```
   198|
   199|## Diagram-Specific Styling
   200|
   201|### Flowchart Styling
   202|
   203|**Class-based styling:**
   204|
   205|```mermaid
   206|flowchart TD
   207|    A[Normal]:::success
   208|    B[Warning]:::warning
   209|    C[Error]:::error
   210|
   211|    classDef success fill:#00b894,stroke:#00a383,color:#fff
   212|    classDef warning fill:#fdcb6e,stroke:#e8b923,color:#333
   213|    classDef error fill:#ff6b6b,stroke:#ee5253,color:#fff
   214|
   215|    A --> B --> C
   216|```
   217|
   218|**Node-specific styling:**
   219|
   220|```mermaid
   221|flowchart LR
   222|    A[Node A]
   223|    B[Node B]
   224|    C[Node C]
   225|
   226|    style A fill:#ff6b6b,stroke:#333,stroke-width:4px
   227|    style B fill:#4ecdc4,stroke:#333,stroke-width:2px
   228|    style C fill:#ffe66d,stroke:#333,stroke-width:2px
   229|
   230|    A --> B --> C
   231|```
   232|
   233|**Link styling:**
   234|
   235|```mermaid
   236|flowchart LR
   237|    A --> B
   238|    B --> C
   239|    C --> D
   240|
   241|    linkStyle 0 stroke:#ff6b6b,stroke-width:4px
   242|    linkStyle 1 stroke:#4ecdc4,stroke-width:2px
   243|    linkStyle 2 stroke:#ffe66d,stroke-width:2px
   244|```
   245|
   246|### Sequence Diagram Styling
   247|
   248|```mermaid
   249|sequenceDiagram
   250|    participant A
   251|    participant B
   252|    participant C
   253|
   254|    A->>B: Message 1
   255|    B->>C: Message 2
   256|
   257|    Note over A,C: Styled note
   258|
   259|    %%{init: {'theme':'forest'}}%%
   260|```
   261|
   262|### Class Diagram Styling
   263|
   264|```mermaid
   265|classDiagram
   266|    class User {
   267|        +String name
   268|        +login()
   269|    }
   270|
   271|    class Admin {
   272|        +manageUsers()
   273|    }
   274|
   275|    User <|-- Admin
   276|
   277|    %%{init: {'theme':'dark'}}%%
   278|```
   279|
   280|## Directional Hints
   281|
   282|Control layout direction for specific nodes:
   283|
   284|```mermaid
   285|flowchart TB
   286|    A --> B
   287|    B --> C
   288|    B --> D
   289|    C --> E
   290|    D --> E
   291|
   292|    %% This is a comment - helps organize complex diagrams
   293|```
   294|
   295|## Click Events and Links
   296|
   297|Add interactive elements:
   298|
   299|```mermaid
   300|flowchart LR
   301|    A[GitHub]
   302|    B[Documentation]
   303|    C[Live Demo]
   304|
   305|    click A "https://github.com" "Go to GitHub"
   306|    click B "https://mermaid.js.org" "View Docs"
   307|    click C "https://mermaid.live" "Try Live Editor"
   308|
   309|    A --> B --> C
   310|```
   311|
   312|## Tooltips
   313|
   314|Add hover information:
   315|
   316|```mermaid
   317|flowchart LR
   318|    A[Service A]
   319|    B[Service B]
   320|
   321|    A -.->|REST API| B
   322|
   323|    %% Tooltips are defined with links
   324|    link A: API Documentation @ https://api.example.com
   325|    link B: Service Dashboard @ https://dashboard.example.com
   326|```
   327|
   328|## Subgraph Styling
   329|
   330|```mermaid
   331|flowchart TB
   332|    subgraph Frontend
   333|        A[Web App]
   334|        B[Mobile App]
   335|    end
   336|
   337|    subgraph Backend
   338|        C[API]
   339|        D[Database]
   340|    end
   341|
   342|    A & B --> C
   343|    C --> D
   344|
   345|    style Frontend fill:#e3f2fd,stroke:#2196f3,stroke-width:2px
   346|    style Backend fill:#fff3e0,stroke:#ff9800,stroke-width:2px
   347|```
   348|
   349|## Comments and Documentation
   350|
   351|```mermaid
   352|flowchart TD
   353|    %% This is a single-line comment
   354|
   355|    %% Multi-line comments can be created
   356|    %% by using multiple comment lines
   357|
   358|    A[Start]
   359|    B[Process]
   360|    C[End]
   361|
   362|    %% Define relationships
   363|    A --> B
   364|    B --> C
   365|
   366|    %% Add styling
   367|    style A fill:#90EE90
   368|    style C fill:#FFB6C1
   369|```
   370|
   371|## Complex Styling Example
   372|
   373|```mermaid
   374|flowchart TB
   375|    subgraph production[Production Environment]
   376|        direction LR
   377|        lb[Load Balancer]
   378|
   379|        subgraph servers[Application Servers]
   380|            app1[Server 1]
   381|            app2[Server 2]
   382|            app3[Server 3]
   383|        end
   384|
   385|        cache[(Redis Cache)]
   386|        db[(PostgreSQL)]
   387|    end
   388|
   389|    subgraph monitoring[Monitoring]
   390|        logs[Log Aggregator]
   391|        metrics[Metrics Dashboard]
   392|    end
   393|
   394|    users[Users] --> lb
   395|    lb --> app1 & app2 & app3
   396|    app1 & app2 & app3 --> cache
   397|    app1 & app2 & app3 --> db
   398|    app1 & app2 & app3 --> logs
   399|    logs --> metrics
   400|
   401|    style production fill:#e8f5e9,stroke:#4caf50,stroke-width:3px
   402|    style servers fill:#fff3e0,stroke:#ff9800,stroke-width:2px
   403|    style monitoring fill:#e3f2fd,stroke:#2196f3,stroke-width:2px
   404|
   405|    style lb fill:#ffeb3b,stroke:#fbc02d,stroke-width:2px
   406|    style cache fill:#ce93d8,stroke:#ab47bc,stroke-width:2px
   407|    style db fill:#ce93d8,stroke:#ab47bc,stroke-width:2px
   408|
   409|    classDef serverClass fill:#81c784,stroke:#4caf50,stroke-width:2px,color:#000
   410|    class app1,app2,app3 serverClass
   411|
   412|    linkStyle 0,1,2,3 stroke:#4caf50,stroke-width:2px
   413|    linkStyle 4,5,6,7,8,9 stroke:#ff9800,stroke-width:1px
   414|```
   415|
   416|## Responsive Sizing
   417|
   418|Use CSS to make diagrams responsive:
   419|
   420|```html
   421|<div style="max-width: 100%; overflow: auto;">
   422|  <pre class="mermaid">
   423|        flowchart LR
   424|            A --> B --> C
   425|    </pre
   426|  >
   427|</div>
   428|```
   429|
   430|## SVG Export Options
   431|
   432|When exporting to SVG:
   433|
   434|```bash
   435|# Export with custom dimensions
   436|mmdc -i diagram.mmd -o output.svg -w 1920 -H 1080
   437|
   438|# Export with background color
   439|mmdc -i diagram.mmd -o output.svg -b "#ffffff"
   440|
   441|# Export with transparent background
   442|mmdc -i diagram.mmd -o output.svg -b "transparent"
   443|```
   444|
   445|## Best Practices for Advanced Features
   446|
   447|1. **Use themes consistently** - Pick one theme for related diagrams
   448|2. **Don't over-style** - Too many colors can reduce clarity
   449|3. **Test hand-drawn look** - Some diagrams work better with classic look
   450|4. **Use ELK for complex layouts** - When dagre creates crossed lines
   451|5. **Comment complex configurations** - Explain non-obvious styling choices
   452|6. **Keep it accessible** - Ensure sufficient color contrast
   453|7. **Test exports** - Verify diagrams render correctly in target format
   454|8. **Version control configs** - Track theme changes in your repository
   455|
   456|## Accessibility Considerations
   457|
   458|```mermaid
   459|---
   460|config:
   461|  theme: base
   462|  themeVariables:
   463|    primaryColor: "#0066cc"
   464|    primaryTextColor: "#ffffff"
   465|    primaryBorderColor: "#003d7a"
   466|    lineColor: "#333333"
   467|    background: "#ffffff"
   468|    mainBkg: "#f0f0f0"
   469|---
   470|flowchart TD
   471|    A[High Contrast Text] --> B[Clear Labels]
   472|    B --> C[Meaningful Colors]
   473|```
   474|
   475|**Accessibility tips:**
   476|
   477|- Use high contrast color combinations
   478|- Don't rely solely on color to convey meaning
   479|- Include descriptive text labels
   480|- Test with color blindness simulators
   481|- Consider dark mode alternatives
   482|
   483|## Performance Considerations
   484|
   485|For large diagrams:
   486|
   487|```mermaid
   488|---
   489|config:
   490|  layout: elk
   491|  elk:
   492|    mergeEdges: true
   493|---
   494|flowchart TD
   495|    %% ELK handles complex layouts better
   496|    %% Merge edges reduces visual clutter
   497|```
   498|
   499|**Performance tips:**
   500|
   501|