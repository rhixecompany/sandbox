---
name: marp-slide-template-dark
description: "Marp Slide Template Dark"
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
     8|@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700&display=swap');
     9|
    10|:root {
    11|  --color-background: #1a1a1a;
    12|  --color-foreground: #e0e0e0;
    13|  --color-heading: #61dafb;
    14|  --color-accent: #bb86fc;
    15|  --color-hr: #61dafb;
    16|  --font-default: 'Noto Sans JP', 'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif;
    17|}
    18|
    19|section {
    20|  background-color: var(--color-background);
    21|  color: var(--color-foreground);
    22|  font-family: var(--font-default);
    23|  font-weight: 400;
    24|  box-sizing: border-box;
    25|  border-bottom: 8px solid var(--color-hr);
    26|  position: relative;
    27|  line-height: 1.7;
    28|  font-size: 22px;
    29|  padding: 56px;
    30|}
    31|
    32|section:last-of-type {
    33|  border-bottom: none;
    34|}
    35|
    36|h1, h2, h3, h4, h5, h6 {
    37|  font-weight: 700;
    38|  color: var(--color-heading);
    39|  margin: 0;
    40|  padding: 0;
    41|}
    42|
    43|h1 {
    44|  font-size: 56px;
    45|  line-height: 1.4;
    46|  text-align: left;
    47|  text-shadow: 0 0 20px rgba(97, 218, 251, 0.3);
    48|}
    49|
    50|h2 {
    51|  position: absolute;
    52|  top: 40px;
    53|  left: 56px;
    54|  right: 56px;
    55|  font-size: 40px;
    56|  padding-top: 0;
    57|  padding-bottom: 16px;
    58|}
    59|
    60|h2::after {
    61|  content: '';
    62|  position: absolute;
    63|  left: 0;
    64|  bottom: 8px;
    65|  width: 60px;
    66|  height: 2px;
    67|  background-color: var(--color-hr);
    68|  box-shadow: 0 0 10px rgba(97, 218, 251, 0.5);
    69|}
    70|
    71|h2 + * {
    72|  margin-top: 112px;
    73|}
    74|
    75|h3 {
    76|  color: var(--color-accent);
    77|  font-size: 28px;
    78|  margin-top: 32px;
    79|  margin-bottom: 12px;
    80|}
    81|
    82|ul, ol {
    83|  padding-left: 32px;
    84|}
    85|
    86|li {
    87|  margin-bottom: 10px;
    88|}
    89|
    90|footer {
    91|  font-size: 0;
    92|  color: transparent;
    93|  position: absolute;
    94|  left: 56px;
    95|  right: 56px;
    96|  bottom: 40px;
    97|  height: 8px;
    98|  background: linear-gradient(90deg, var(--color-heading), var(--color-accent));
    99|  box-shadow: 0 0 20px rgba(97, 218, 251, 0.3);
   100|}
   101|
   102|section.lead {
   103|  border-bottom: 8px solid var(--color-hr);
   104|}
   105|
   106|section.lead footer {
   107|  display: none;
   108|}
   109|
   110|section.lead h1 {
   111|  margin-bottom: 24px;
   112|}
   113|
   114|section.lead p {
   115|  font-size: 24px;
   116|  color: var(--color-foreground);
   117|}
   118|
   119|code {
   120|  background-color: #2d2d2d;
   121|  color: #61dafb;
   122|  padding: 2px 8px;
   123|  border-radius: 4px;
   124|  font-family: 'Consolas', 'Monaco', monospace;
   125|}
   126|
   127|strong {
   128|  color: var(--color-accent);
   129|  font-weight: 700;
   130|}
   131|</style>
   132|
   133|<!-- _class: lead -->
   134|
   135|# プレゼンテーション
   136|
   137|ダークモード
   138|
   139|---
   140|
   141|## アジェンダ
   142|
   143|- トピック1
   144|- トピック2
   145|- トピック3
   146|
   147|---
   148|
   149|## スライド
   150|
   151|- ポイント1
   152|- ポイント2
   153|- ポイント3
   154|