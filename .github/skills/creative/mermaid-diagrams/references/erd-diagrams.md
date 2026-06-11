---
name: mermaid-diagrams-erd-diagrams
description: "Entity Relationship Diagrams (ERD)"
version: 1.0.0
author: Alexa
---
     1|# Entity Relationship Diagrams (ERD)
     2|
     3|ERDs model database schemas, showing tables (entities), their columns (attributes), and relationships between tables. Essential for database design and documentation.
     4|
     5|## Basic Syntax
     6|
     7|```mermaid
     8|erDiagram
     9|    CUSTOMER ||--o{ ORDER : places
    10|```
    11|
    12|## Defining Entities
    13|
    14|```mermaid
    15|erDiagram
    16|    CUSTOMER
    17|    ORDER
    18|    PRODUCT
    19|```
    20|
    21|## Entity Attributes
    22|
    23|Define columns with type and constraints:
    24|
    25|```mermaid
    26|erDiagram
    27|    CUSTOMER {
    28|        int id PK
    29|        string email UK
    30|        string name
    31|        string phone
    32|        datetime created_at
    33|    }
    34|```
    35|
    36|**Attribute format:** `type name constraints`
    37|
    38|**Common constraints:**
    39|
    40|- `PK` - Primary Key
    41|- `FK` - Foreign Key
    42|- `UK` - Unique Key
    43|- `NN` - Not Null
    44|
    45|## Relationships
    46|
    47|### Relationship Symbols
    48|
    49|**Cardinality indicators:**
    50|
    51|- `||` - Exactly one
    52|- `|o` - Zero or one
    53|- `}{` - One or many
    54|- `}o` - Zero or many
    55|
    56|**Relationship line:**
    57|
    58|- `--` - Non-identifying relationship
    59|- `..` - Identifying relationship (rare in practice)
    60|
    61|### Common Relationships
    62|
    63|```mermaid
    64|erDiagram
    65|    %% One-to-One
    66|    USER ||--|| PROFILE : has
    67|
    68|    %% One-to-Many
    69|    CUSTOMER ||--o{ ORDER : places
    70|
    71|    %% Many-to-Many (with junction table)
    72|    STUDENT }o--o{ COURSE : enrolls
    73|    STUDENT ||--o{ ENROLLMENT : has
    74|    COURSE ||--o{ ENROLLMENT : includes
    75|
    76|    %% Optional Relationships
    77|    EMPLOYEE |o--o{ DEPARTMENT : manages
    78|```
    79|
    80|### Relationship with Labels
    81|
    82|```mermaid
    83|erDiagram
    84|    AUTHOR ||--o{ BOOK : writes
    85|    BOOK }o--|| PUBLISHER : "published by"
    86|    READER }o--o{ BOOK : reads
    87|```
    88|
    89|## Data Types
    90|
    91|Use standard database types:
    92|
    93|- `int`, `bigint`, `smallint`
    94|- `varchar`, `text`, `char`
    95|- `decimal`, `float`, `double`
    96|- `boolean`, `bool`
    97|- `date`, `datetime`, `timestamp`
    98|- `json`, `jsonb`
    99|- `uuid`
   100|- `blob`, `bytea`
   101|
   102|## Comprehensive Example: E-Commerce Database
   103|
   104|```mermaid
   105|erDiagram
   106|    CUSTOMER ||--o{ ORDER : places
   107|    CUSTOMER ||--o{ REVIEW : writes
   108|    CUSTOMER ||--o{ ADDRESS : has
   109|    ORDER ||--|{ LINE_ITEM : contains
   110|    PRODUCT ||--o{ LINE_ITEM : "ordered in"
   111|    PRODUCT }o--|| CATEGORY : "belongs to"
   112|    PRODUCT ||--o{ REVIEW : receives
   113|    PRODUCT ||--o{ INVENTORY : tracks
   114|    ORDER ||--|| PAYMENT : "paid by"
   115|    ORDER ||--o| SHIPMENT : "shipped via"
   116|
   117|    CUSTOMER {
   118|        uuid id PK
   119|        varchar email UK "NOT NULL"
   120|        varchar name "NOT NULL"
   121|        varchar phone
   122|        timestamp created_at "DEFAULT NOW()"
   123|        timestamp updated_at
   124|    }
   125|
   126|    ADDRESS {
   127|        uuid id PK
   128|        uuid customer_id FK
   129|        varchar street "NOT NULL"
   130|        varchar city "NOT NULL"
   131|        varchar state
   132|        varchar postal_code
   133|        varchar country "NOT NULL"
   134|        boolean is_default
   135|    }
   136|
   137|    ORDER {
   138|        uuid id PK
   139|        uuid customer_id FK "NOT NULL"
   140|        decimal total "NOT NULL"
   141|        varchar status "NOT NULL"
   142|        timestamp order_date "DEFAULT NOW()"
   143|        timestamp shipped_date
   144|        timestamp delivered_date
   145|    }
   146|
   147|    LINE_ITEM {
   148|        uuid id PK
   149|        uuid order_id FK "NOT NULL"
   150|        uuid product_id FK "NOT NULL"
   151|        int quantity "NOT NULL"
   152|        decimal price_per_unit "NOT NULL"
   153|        decimal subtotal "COMPUTED"
   154|    }
   155|
   156|    PRODUCT {
   157|        uuid id PK
   158|        varchar sku UK "NOT NULL"
   159|        varchar name "NOT NULL"
   160|        text description
   161|        decimal price "NOT NULL"
   162|        uuid category_id FK
   163|        boolean is_active "DEFAULT TRUE"
   164|        timestamp created_at "DEFAULT NOW()"
   165|    }
   166|
   167|    CATEGORY {
   168|        uuid id PK
   169|        varchar name UK "NOT NULL"
   170|        text description
   171|        uuid parent_category_id FK
   172|    }
   173|
   174|    INVENTORY {
   175|        uuid id PK
   176|        uuid product_id FK "NOT NULL"
   177|        int quantity "DEFAULT 0"
   178|        varchar warehouse_location
   179|        timestamp last_updated
   180|    }
   181|
   182|    REVIEW {
   183|        uuid id PK
   184|        uuid customer_id FK "NOT NULL"
   185|        uuid product_id FK "NOT NULL"
   186|        int rating "CHECK 1-5"
   187|        text comment
   188|        timestamp created_at "DEFAULT NOW()"
   189|    }
   190|
   191|    PAYMENT {
   192|        uuid id PK
   193|        uuid order_id FK "NOT NULL"
   194|        varchar payment_method "NOT NULL"
   195|        decimal amount "NOT NULL"
   196|        varchar status "NOT NULL"
   197|        varchar transaction_id UK
   198|        timestamp processed_at
   199|    }
   200|
   201|    SHIPMENT {
   202|        uuid id PK
   203|        uuid order_id FK "NOT NULL"
   204|        varchar carrier
   205|        varchar tracking_number
   206|        timestamp shipped_date
   207|        timestamp estimated_delivery
   208|        timestamp actual_delivery
   209|    }
   210|```
   211|
   212|## Blog Platform Schema
   213|
   214|```mermaid
   215|erDiagram
   216|    USER ||--o{ POST : creates
   217|    USER ||--o{ COMMENT : writes
   218|    POST ||--o{ COMMENT : receives
   219|    POST }o--o{ TAG : tagged_with
   220|    POST ||--o{ POST_TAG : has
   221|    TAG ||--o{ POST_TAG : applied_to
   222|    POST }o--|| CATEGORY : "belongs to"
   223|    USER ||--o{ LIKE : gives
   224|    POST ||--o{ LIKE : receives
   225|    COMMENT ||--o{ LIKE : receives
   226|
   227|    USER {
   228|        bigint id PK "AUTO_INCREMENT"
   229|        varchar email UK "NOT NULL"
   230|        varchar username UK "NOT NULL"
   231|        varchar password_hash "NOT NULL"
   232|        varchar display_name
   233|        text bio
   234|        varchar avatar_url
   235|        timestamp created_at "DEFAULT NOW()"
   236|        timestamp last_login
   237|    }
   238|
   239|    POST {
   240|        bigint id PK "AUTO_INCREMENT"
   241|        bigint user_id FK "NOT NULL"
   242|        bigint category_id FK
   243|        varchar title "NOT NULL"
   244|        varchar slug UK "NOT NULL"
   245|        text content "NOT NULL"
   246|        text excerpt
   247|        varchar featured_image_url
   248|        varchar status "NOT NULL DEFAULT 'draft'"
   249|        int view_count "DEFAULT 0"
   250|        timestamp published_at
   251|        timestamp created_at "DEFAULT NOW()"
   252|        timestamp updated_at
   253|    }
   254|
   255|    COMMENT {
   256|        bigint id PK "AUTO_INCREMENT"
   257|        bigint user_id FK "NOT NULL"
   258|        bigint post_id FK "NOT NULL"
   259|        bigint parent_comment_id FK "NULL"
   260|        text content "NOT NULL"
   261|        varchar status "DEFAULT 'pending'"
   262|        timestamp created_at "DEFAULT NOW()"
   263|    }
   264|
   265|    CATEGORY {
   266|        bigint id PK "AUTO_INCREMENT"
   267|        varchar name UK "NOT NULL"
   268|        varchar slug UK "NOT NULL"
   269|        text description
   270|        bigint parent_id FK
   271|    }
   272|
   273|    TAG {
   274|        bigint id PK "AUTO_INCREMENT"
   275|        varchar name UK "NOT NULL"
   276|        varchar slug UK "NOT NULL"
   277|    }
   278|
   279|    POST_TAG {
   280|        bigint post_id FK "NOT NULL"
   281|        bigint tag_id FK "NOT NULL"
   282|    }
   283|
   284|    LIKE {
   285|        bigint id PK "AUTO_INCREMENT"
   286|        bigint user_id FK "NOT NULL"
   287|        varchar likeable_type "NOT NULL"
   288|        bigint likeable_id "NOT NULL"
   289|        timestamp created_at "DEFAULT NOW()"
   290|    }
   291|```
   292|
   293|## Social Media Schema
   294|
   295|```mermaid
   296|erDiagram
   297|    USER ||--o{ POST : creates
   298|    USER ||--o{ FOLLOW : follows
   299|    USER ||--o{ FOLLOW : "followed by"
   300|    POST ||--o{ LIKE : receives
   301|    POST ||--o{ COMMENT : has
   302|    USER ||--o{ LIKE : gives
   303|    USER ||--o{ COMMENT : makes
   304|    USER ||--o{ NOTIFICATION : receives
   305|    POST ||--o{ POST_MEDIA : contains
   306|    USER }o--o{ GROUP : "member of"
   307|    USER ||--o{ MESSAGE : sends
   308|    USER ||--o{ MESSAGE : receives
   309|
   310|    USER {
   311|        uuid id PK
   312|        varchar username UK "NOT NULL"
   313|        varchar email UK "NOT NULL"
   314|        varchar password_hash "NOT NULL"
   315|        varchar full_name
   316|        text bio
   317|        varchar profile_picture_url
   318|        varchar cover_photo_url
   319|        boolean is_verified "DEFAULT FALSE"
   320|        boolean is_private "DEFAULT FALSE"
   321|        timestamp created_at "DEFAULT NOW()"
   322|    }
   323|
   324|    POST {
   325|        uuid id PK
   326|        uuid user_id FK "NOT NULL"
   327|        text content
   328|        varchar visibility "DEFAULT 'public'"
   329|        int likes_count "DEFAULT 0"
   330|        int comments_count "DEFAULT 0"
   331|        int shares_count "DEFAULT 0"
   332|        timestamp created_at "DEFAULT NOW()"
   333|        timestamp edited_at
   334|    }
   335|
   336|    POST_MEDIA {
   337|        uuid id PK
   338|        uuid post_id FK "NOT NULL"
   339|        varchar media_type "NOT NULL"
   340|        varchar media_url "NOT NULL"
   341|        int display_order
   342|    }
   343|
   344|    FOLLOW {
   345|        uuid id PK
   346|        uuid follower_id FK "NOT NULL"
   347|        uuid following_id FK "NOT NULL"
   348|        timestamp created_at "DEFAULT NOW()"
   349|    }
   350|
   351|    LIKE {
   352|        uuid id PK
   353|        uuid user_id FK "NOT NULL"
   354|        uuid post_id FK "NOT NULL"
   355|        timestamp created_at "DEFAULT NOW()"
   356|    }
   357|
   358|    COMMENT {
   359|        uuid id PK
   360|        uuid user_id FK "NOT NULL"
   361|        uuid post_id FK "NOT NULL"
   362|        uuid parent_comment_id FK
   363|        text content "NOT NULL"
   364|        int likes_count "DEFAULT 0"
   365|        timestamp created_at "DEFAULT NOW()"
   366|    }
   367|
   368|    MESSAGE {
   369|        uuid id PK
   370|        uuid sender_id FK "NOT NULL"
   371|        uuid receiver_id FK "NOT NULL"
   372|        text content "NOT NULL"
   373|        boolean is_read "DEFAULT FALSE"
   374|        timestamp created_at "DEFAULT NOW()"
   375|        timestamp read_at
   376|    }
   377|
   378|    NOTIFICATION {
   379|        uuid id PK
   380|        uuid user_id FK "NOT NULL"
   381|        varchar notification_type "NOT NULL"
   382|        text content "NOT NULL"
   383|        boolean is_read "DEFAULT FALSE"
   384|        varchar related_entity_type
   385|        uuid related_entity_id
   386|        timestamp created_at "DEFAULT NOW()"
   387|    }
   388|
   389|    GROUP {
   390|        uuid id PK
   391|        varchar name "NOT NULL"
   392|        text description
   393|        uuid created_by FK "NOT NULL"
   394|        boolean is_private "DEFAULT FALSE"
   395|        timestamp created_at "DEFAULT NOW()"
   396|    }
   397|```
   398|
   399|## Best Practices
   400|
   401|1. **Name entities in UPPERCASE** - Convention for clarity
   402|2. **Use singular names** - `USER` not `USERS`, `ORDER` not `ORDERS`
   403|3. **Define all constraints** - Document PKs, FKs, UKs, NOT NULL
   404|4. **Show cardinality accurately** - Be precise about one-to-many vs many-to-many
   405|5. **Include timestamps** - created_at, updated_at for auditing
   406|6. **Document computed columns** - Mark calculated/derived values
   407|7. **Add meaningful comments** - Use quotes for constraints and descriptions
   408|8. **Consider junction tables** - Explicitly model many-to-many relationships
   409|9. **Use appropriate types** - Match database-specific types
   410|10. **Show indexes** - Document UK (unique keys) beyond PKs
   411|
   412|## Common Patterns
   413|
   414|### Self-Referencing (Hierarchical)
   415|
   416|```mermaid
   417|erDiagram
   418|    CATEGORY ||--o{ CATEGORY : "parent of"
   419|
   420|    CATEGORY {
   421|        uuid id PK
   422|        varchar name "NOT NULL"
   423|        uuid parent_id FK "NULLABLE"
   424|    }
   425|```
   426|
   427|### Junction Table (Many-to-Many)
   428|
   429|```mermaid
   430|erDiagram
   431|    STUDENT }o--o{ COURSE : enrolls
   432|    STUDENT ||--o{ ENROLLMENT : has
   433|    COURSE ||--o{ ENROLLMENT : includes
   434|
   435|    STUDENT {
   436|        uuid id PK
   437|        varchar name "NOT NULL"
   438|    }
   439|
   440|    ENROLLMENT {
   441|        uuid student_id FK PK
   442|        uuid course_id FK PK
   443|        date enrolled_date
   444|        varchar grade
   445|    }
   446|
   447|    COURSE {
   448|        uuid id PK
   449|        varchar title "NOT NULL"
   450|    }
   451|```
   452|
   453|### Polymorphic Relationship
   454|
   455|```mermaid
   456|erDiagram
   457|    COMMENT {
   458|        uuid id PK
   459|        uuid user_id FK
   460|        varchar commentable_type "NOT NULL"
   461|        uuid commentable_id "NOT NULL"
   462|        text content
   463|    }
   464|
   465|    POST {
   466|        uuid id PK
   467|        varchar title
   468|    }
   469|
   470|    VIDEO {
   471|        uuid id PK
   472|        varchar title
   473|    }
   474|```
   475|
   476|### Soft Deletes
   477|
   478|```mermaid
   479|erDiagram
   480|    USER {
   481|        uuid id PK
   482|        varchar email UK
   483|        varchar name
   484|        timestamp deleted_at "NULLABLE"
   485|    }
   486|```
   487|
   488|### Audit Trail
   489|
   490|```mermaid
   491|erDiagram
   492|    DOCUMENT ||--o{ DOCUMENT_VERSION : has
   493|
   494|    DOCUMENT {
   495|        uuid id PK
   496|        varchar title "NOT NULL"
   497|        int current_version "DEFAULT 1"
   498|    }
   499|
   500|    DOCUMENT_VERSION {
   501|