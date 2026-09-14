---
name: plugin-install
description: "# asdf Plugin-Specific Installation"
version: 1.0.0
author: Alexa
license: MIT
metadata:
  hermes:
    tags: []
    related_skills: []
---
     1|# asdf Plugin-Specific Installation
     2|
     3|This reference file contains plugin-specific installation requirements that MUST be read before adding certain plugins.
     4|
     5|## Node.js Plugin
     6|
     7|**System dependencies required BEFORE plugin add:**
     8|
     9|```bash
    10|# Ubuntu/Debian
    11|sudo apt install -y coreutils curl git gnupg2 automake autoconf libssl-dev libyaml-dev readline libncurses5 libncurses-dev
    12|
    13|# macOS
    14|brew install coreutils automake autoconf openssl@1.1 yaml readline
    15|```
    16|
    17|**Critical**: Node.js plugin requires `gnupg2` for keyring verification. Install BEFORE running `asdf plugin add nodejs`.
    18|
    19|## Python Plugin
    20|
    21|**System dependencies required:**
    22|
    23|```bash
    24|# Ubuntu/Debian
    25|sudo apt install -y libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev libncurses5 libncurses-dev xz-utils tk-dev liblzma-dev
    26|
    27|# macOS
    28|brew install xz readline sqlite3 tcl-tk
    29|```
    30|
    31|## Erlang Plugin
    32|
    33|**System dependencies (complex):**
    34|
    35|```bash
    36|# Ubuntu/Debian
    37|sudo apt install -y autoconf libncurses-dev openssl libssl-dev wget
    38|
    39|# erlang requires kerl for building - see asdf-erlang documentation
    40|```
    41|
    42|## Common Failure Modes
    43|
    44|- "Missing OpenSSL" → Install libssl-dev before plugin add
    45|- "keyring verify failed" → Install gnupg2 and retry
    46|- "libyaml not found" → Install libyaml-dev
    47|
    48|**Do NOT** attempt plugin installation without first reading these requirements.
    49|