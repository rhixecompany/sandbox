---
name: marp-slide-template-business
description: "Marp Slide Template Business"
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
     8|@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&display=swap');
     9|
    10|:root {
    11|  --color-background: #ffffff;
    12|  --color-foreground: #1f2937;
    13|  --color-heading: #1e40af;
    14|  --color-accent: #3b82f6;
    15|  --color-border: #d1d5db;
    16|  --font-default: 'Noto Sans JP', 'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif;
    17|}
    18|
    19|section {
    20|  background-color: var(--color-background);
    21|  color: var(--color-foreground);
    22|  font-family: var(--font-default);
    23|  font-weight: 400;
    24|  box-sizing: border-box;
    25|  border-top: 8px solid var(--color-heading);
    26|  position: relative;
    27|  line-height: 1.7;
    28|  font-size: 22px;
    29|  padding: 56px;
    30|}
    31|
    32|h1, h2, h3, h4, h5, h6 {
    33|  font-weight: 700;
    34|  color: var(--color-heading);
    35|  margin: 0;
    36|  padding: 0;
    37|}
    38|
    39|h1 {
    40|  font-size: 54px;
    41|  line-height: 1.3;
    42|  text-align: left;
    43|  font-weight: 700;
    44|  letter-spacing: -0.02em;
    45|}
    46|
    47|h2 {
    48|  position: absolute;
    49|  top: 40px;
    50|  left: 56px;
    51|  right: 56px;
    52|  font-size: 38px;
    53|  padding-top: 0;
    54|  padding-bottom: 16px;
    55|  border-bottom: 3px solid var(--color-accent);
    56|}
    57|
    58|h2 + * {
    59|  margin-top: 112px;
    60|}
    61|
    62|h3 {
    63|  color: var(--color-accent);
    64|  font-size: 26px;
    65|  margin-top: 32px;
    66|  margin-bottom: 12px;
    67|  font-weight: 600;
    68|}
    69|
    70|ul, ol {
    71|  padding-left: 32px;
    72|}
    73|
    74|li {
    75|  margin-bottom: 10px;
    76|  line-height: 1.7;
    77|}
    78|
    79|footer {
    80|  font-size: 16px;
    81|  color: #6b7280;
    82|  position: absolute;
    83|  left: 56px;
    84|  right: 56px;
    85|  bottom: 40px;
    86|  display: flex;
    87|  justify-content: space-between;
    88|  align-items: center;
    89|}
    90|
    91|footer::before {
    92|  content: '';
    93|  flex: 1;
    94|  height: 2px;
    95|  background-color: var(--color-border);
    96|  margin-right: 20px;
    97|}
    98|
    99|section.lead {
   100|  border-top: 8px solid var(--color-heading);
   101|  display: flex;
   102|  flex-direction: column;
   103|  justify-content: center;
   104|  background: linear-gradient(135deg, #ffffff 0%, #f3f4f6 100%);
   105|}
   106|
   107|section.lead footer {
   108|  display: none;
   109|}
   110|
   111|section.lead h1 {
   112|  margin-bottom: 32px;
   113|  color: var(--color-heading);
   114|}
   115|
   116|section.lead p {
   117|  font-size: 24px;
   118|  color: var(--color-foreground);
   119|  font-weight: 500;
   120|}
   121|
   122|table {
   123|  border-collapse: collapse;
   124|  width: 100%;
   125|  margin: 20px 0;
   126|  font-size: 18px;
   127|}
   128|
   129|th, td {
   130|  border: 1px solid var(--color-border);
   131|  padding: 12px;
   132|  text-align: left;
   133|}
   134|
   135|th {
   136|  background-color: var(--color-heading);
   137|  color: #ffffff;
   138|  font-weight: 700;
   139|}
   140|
   141|tr:nth-child(even) {
   142|  background-color: #f9fafb;
   143|}
   144|
   145|strong {
   146|  color: var(--color-heading);
   147|  font-weight: 700;
   148|}
   149|
   150|code {
   151|  background-color: #f3f4f6;
   152|  color: var(--color-heading);
   153|  padding: 2px 6px;
   154|  border-radius: 3px;
   155|  font-family: 'Consolas', 'Monaco', monospace;
   156|  font-size: 0.9em;
   157|}
   158|</style>
   159|
   160|<!-- _class: lead -->
   161|
   162|# プレゼンテーション
   163|
   164|ビジネスライク
   165|
   166|---
   167|
   168|## アジェンダ
   169|
   170|- トピック1
   171|- トピック2
   172|- トピック3
   173|
   174|---
   175|
   176|## スライド
   177|
   178|- ポイント1
   179|- ポイント2
   180|- ポイント3
   181|