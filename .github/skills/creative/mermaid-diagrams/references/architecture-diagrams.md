---
name: mermaid-diagrams-architecture-diagrams
description: "Architecture Diagrams Reference"
version: 1.0.0
author: Alexa
---
     1|# Architecture Diagrams Reference
     2|
     3|Architecture diagrams visualize cloud services, CI/CD deployments, and infrastructure relationships. Introduced in Mermaid v11.1.0.
     4|
     5|## Basic Syntax
     6|
     7|```mermaid
     8|architecture-beta
     9|    group public_api(cloud)[Public API]
    10|    service api1(server)[API Server] in public_api
    11|    service db(database)[Database]
    12|
    13|    api1:R --> L:db
    14|```
    15|
    16|## Building Blocks
    17|
    18|### Groups
    19|
    20|Group related services together:
    21|
    22|```
    23|group {groupId}({icon})[{title}] (in {parentId})?
    24|```
    25|
    26|```mermaid
    27|architecture-beta
    28|    group public_api(cloud)[Public API]
    29|    group private_api(cloud)[Private API] in public_api
    30|```
    31|
    32|### Services
    33|
    34|Declare services (nodes):
    35|
    36|```
    37|service {serviceId}({icon})[{title}] (in {parentId})?
    38|```
    39|
    40|```mermaid
    41|architecture-beta
    42|    service api(server)[API Server]
    43|    service db(database)[Database]
    44|    service cache(redis)[Cache] in api
    45|```
    46|
    47|### Edges
    48|
    49|Connect services with edges:
    50|
    51|```
    52|{serviceId}{{group}}?:{T|B|L|R} {<}?--{>}? {T|B|L|R}:{serviceId}{{group}}?
    53|```
    54|
    55|**Directions:** `T` (top), `B` (bottom), `L` (left), `R` (right)
    56|
    57|**Arrows:** `<` for incoming, `>` for outgoing
    58|
    59|```mermaid
    60|architecture-beta
    61|    service client(browser)[Client]
    62|    service api(server)[API]
    63|    service db(database)[Database]
    64|
    65|    client:B --> T:api
    66|    api:R --> L:db
    67|```
    68|
    69|### Junctions
    70|
    71|Create 4-way splits:
    72|
    73|```
    74|junction {junctionId} (in {parentId})?
    75|```
    76|
    77|```mermaid
    78|architecture-beta
    79|    service input(server)[Input]
    80|    service output1(server)[Output 1]
    81|    service output2(server)[Output 2]
    82|
    83|    junction j1
    84|
    85|    input:R --> L:j1
    86|    j1:T --> B:output1
    87|    j1:B --> T:output2
    88|```
    89|
    90|## Icons
    91|
    92|**Default icons:** `cloud`, `database`, `disk`, `internet`, `server`
    93|
    94|**Custom icons:** Use any of 200,000+ icons from iconify.design:
    95|
    96|```mermaid
    97|architecture-beta
    98|    service web(aws:ec2)[Web Server]
    99|    service storage(aws:s3)[Storage]
   100|```
   101|
   102|### Using @iconify-json Icon Packs
   103|
   104|Use npm icon packs with Mermaid CLI for a wide variety of technology logos:
   105|
   106|```bash
   107|npm install @iconify-json/logos @mermaid-js/mermaid-cli
   108|mmdc --iconPacks @iconify-json/logos -i ./diagram.mmd -o ./output.svg
   109|```
   110|
   111|Use icons with the `logos:` prefix:
   112|
   113|```mermaid
   114|architecture-beta
   115|    service web(logos:docker)[Docker Container]
   116|    service k8s(logos:kubernetes)[Kubernetes Cluster]
   117|    service aws(logos:aws)[AWS Services]
   118|    service github(logos:github)[GitHub Actions]
   119|
   120|    web:R --> L:k8s
   121|    k8s:R --> L:aws
   122|    web:R --> L:github
   123|```
   124|
   125|**Popular icon packs:**
   126|
   127|| Icon Pack | Description | Install |
   128|| --- | --- | --- |
   129|| `@iconify-json/logos` | Technology brands (Docker, AWS, GitHub, etc.) | `npm i @iconify-json/logos` |
   130|| `@iconify-json/bi` | Bootstrap icons | `npm i @iconify-json/bi` |
   131|| `@iconify-json/mdi` | Material Design icons | `npm i @iconify-json/mdi` |
   132|| `@iconify-json/simple-icons` | Simple icons | `npm i @iconify-json/simple-icons` |
   133|
   134|Usage: `pack:icon-name` (e.g., `logos:docker`, `mdi:database`)
   135|
   136|## Complex Example
   137|
   138|```mermaid
   139|architecture-beta
   140|    group internet(cloud)[Internet]
   141|    group private_vpc(cloud)[Private VPC]
   142|
   143|    service lb(load_balancer)[Load Balancer] in internet
   144|    service api1(api)[API Server 1] in private_vpc
   145|    service api2(api)[API Server 2] in private_vpc
   146|    service db(database)[Primary Database] in private_vpc
   147|    service replica(database)[Read Replica] in private_vpc
   148|
   149|    lb:R --> L:api1
   150|    lb:R --> L:api2
   151|    api1:R --> L:db
   152|    api2:R --> L:db
   153|    db:R --> L:replica
   154|```
   155|
   156|## Edge Patterns
   157|
   158|| Pattern              | Description               |
   159|| -------------------- | ------------------------- |
   160|| `A:R -- L:B`         | Horizontal edge           |
   161|| `A:T -- B:B`         | Vertical edge (90 degree) |
   162|| `A:R --> L:B`        | Edge with arrow           |
   163|| `A:R <--> L:B`       | Bidirectional edge        |
   164|| `A{group}:R --> L:B` | Edge from group boundary  |
   165|
   166|## Group Edges
   167|
   168|Connect groups using the `{group}` modifier:
   169|
   170|```mermaid
   171|architecture-beta
   172|    group frontend(cloud)[Frontend]
   173|    group backend(cloud)[Backend]
   174|
   175|    service client(browser)[Client] in frontend
   176|    service api(server)[API] in backend
   177|
   178|    client{group}:B --> T:api{group}
   179|```
   180|
   181|## Best Practices
   182|
   183|1. Group services by environment (public/private) or layer (frontend/backend)
   184|2. Use consistent icons for service types
   185|3. Label edges with protocols (HTTPS, TCP, etc.)
   186|4. Use junctions for fan-out patterns
   187|5. Keep diagrams focused; split complex architectures into multiple views
   188|
   189|## Reference
   190|
   191|- [Official Documentation](https://mermaid.js.org/syntax/architecture.html)
   192|- [Iconify Icons](https://iconify.design)
   193|