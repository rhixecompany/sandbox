---
name: marp-slide-template-tech
description: "Marp Slide Template Tech"
version: 1.0.0
author: Alexa
---
     1|---
     2|marp: true
     3|theme: default
     4|paginate: true
     5|---
     6|
     7|<style>
     8|@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700&family=Fira+Code:wght@400;500;700&display=swap');
     9|
    10|:root {
    11|  --color-background: #0d1117;
    12|  --color-foreground: #c9d1d9;
    13|  --color-heading: #58a6ff;
    14|  --color-accent: #7ee787;
    15|  --color-code-bg: #161b22;
    16|  --color-border: #30363d;
    17|  --font-default: 'Noto Sans JP', 'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif;
    18|  --font-code: 'Fira Code', 'Consolas', 'Monaco', monospace;
    19|}
    20|
    21|section {
    22|  background-color: var(--color-background);
    23|  color: var(--color-foreground);
    24|  font-family: var(--font-default);
    25|  font-weight: 400;
    26|  box-sizing: border-box;
    27|  border-left: 4px solid var(--color-accent);
    28|  position: relative;
    29|  line-height: 1.6;
    30|  font-size: 20px;
    31|  padding: 56px;
    32|}
    33|
    34|h1, h2, h3, h4, h5, h6 {
    35|  font-weight: 700;
    36|  color: var(--color-heading);
    37|  margin: 0;
    38|  padding: 0;
    39|  font-family: var(--font-code);
    40|}
    41|
    42|h1 {
    43|  font-size: 52px;
    44|  line-height: 1.3;
    45|  text-align: left;
    46|}
    47|
    48|h1::before {
    49|  content: '# ';
    50|  color: var(--color-accent);
    51|}
    52|
    53|h2 {
    54|  font-size: 38px;
    55|  margin-bottom: 40px;
    56|  padding-bottom: 12px;
    57|  border-bottom: 2px solid var(--color-border);
    58|}
    59|
    60|h2::before {
    61|  content: '## ';
    62|  color: var(--color-accent);
    63|}
    64|
    65|h3 {
    66|  color: var(--color-foreground);
    67|  font-size: 26px;
    68|  margin-top: 32px;
    69|  margin-bottom: 12px;
    70|}
    71|
    72|h3::before {
    73|  content: '### ';
    74|  color: var(--color-accent);
    75|}
    76|
    77|ul, ol {
    78|  padding-left: 32px;
    79|}
    80|
    81|li {
    82|  margin-bottom: 10px;
    83|}
    84|
    85|li::marker {
    86|  color: var(--color-accent);
    87|}
    88|
    89|pre {
    90|  background-color: var(--color-code-bg);
    91|  border: 1px solid var(--color-border);
    92|  border-radius: 6px;
    93|  padding: 16px;
    94|  overflow-x: auto;
    95|  font-family: var(--font-code);
    96|  font-size: 16px;
    97|  line-height: 1.5;
    98|}
    99|
   100|code {
   101|  background-color: var(--color-code-bg);
   102|  color: var(--color-accent);
   103|  padding: 2px 6px;
   104|  border-radius: 3px;
   105|  font-family: var(--font-code);
   106|  font-size: 0.9em;
   107|}
   108|
   109|pre code {
   110|  background-color: transparent;
   111|  padding: 0;
   112|  color: var(--color-foreground);
   113|}
   114|
   115|footer {
   116|  font-size: 14px;
   117|  color: #8b949e;
   118|  font-family: var(--font-code);
   119|  position: absolute;
   120|  left: 56px;
   121|  right: 56px;
   122|  bottom: 40px;
   123|  text-align: right;
   124|}
   125|
   126|footer::before {
   127|  content: '// ';
   128|  color: var(--color-accent);
   129|}
   130|
   131|section.lead {
   132|  border-left: 4px solid var(--color-accent);
   133|  display: flex;
   134|  flex-direction: column;
   135|  justify-content: center;
   136|}
   137|
   138|section.lead h1 {
   139|  margin-bottom: 24px;
   140|}
   141|
   142|section.lead p {
   143|  font-size: 22px;
   144|  color: var(--color-foreground);
   145|  font-family: var(--font-code);
   146|}
   147|
   148|strong {
   149|  color: var(--color-accent);
   150|  font-weight: 700;
   151|}
   152|</style>
   153|
   154|<!-- _class: lead -->
   155|
   156|# プレゼンテーション
   157|
   158|技術系（コード向け）
   159|
   160|---
   161|
   162|## アジェンダ
   163|
   164|- トピック1
   165|- トピック2
   166|- トピック3
   167|
   168|---
   169|
   170|## スライド
   171|
   172|- ポイント1
   173|- ポイント2
   174|- ポイント3
   175|