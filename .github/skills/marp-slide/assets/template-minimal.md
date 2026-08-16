---
name: marp-slide-template-minimal
description: "Marp Slide Template Minimal"
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
     8|@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500&display=swap');
     9|
    10|:root {
    11|  --color-background: #ffffff;
    12|  --color-foreground: #2c2c2c;
    13|  --color-heading: #1a1a1a;
    14|  --color-accent: #e0e0e0;
    15|  --font-default: 'Noto Sans JP', 'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif;
    16|}
    17|
    18|section {
    19|  background-color: var(--color-background);
    20|  color: var(--color-foreground);
    21|  font-family: var(--font-default);
    22|  font-weight: 300;
    23|  box-sizing: border-box;
    24|  position: relative;
    25|  line-height: 1.8;
    26|  font-size: 24px;
    27|  padding: 60px 80px;
    28|}
    29|
    30|h1, h2, h3, h4, h5, h6 {
    31|  font-weight: 400;
    32|  color: var(--color-heading);
    33|  margin: 0;
    34|  padding: 0;
    35|}
    36|
    37|h1 {
    38|  font-size: 60px;
    39|  line-height: 1.3;
    40|  text-align: left;
    41|  font-weight: 300;
    42|  letter-spacing: 0.02em;
    43|}
    44|
    45|h2 {
    46|  font-size: 42px;
    47|  margin-bottom: 40px;
    48|  font-weight: 400;
    49|  letter-spacing: 0.01em;
    50|}
    51|
    52|h3 {
    53|  color: var(--color-foreground);
    54|  font-size: 28px;
    55|  margin-top: 32px;
    56|  margin-bottom: 16px;
    57|  font-weight: 400;
    58|}
    59|
    60|ul, ol {
    61|  padding-left: 32px;
    62|}
    63|
    64|li {
    65|  margin-bottom: 14px;
    66|  line-height: 1.7;
    67|}
    68|
    69|footer {
    70|  font-size: 14px;
    71|  color: #999999;
    72|  position: absolute;
    73|  left: 80px;
    74|  right: 80px;
    75|  bottom: 40px;
    76|  text-align: center;
    77|}
    78|
    79|section.lead {
    80|  display: flex;
    81|  flex-direction: column;
    82|  justify-content: center;
    83|  text-align: center;
    84|}
    85|
    86|section.lead h1 {
    87|  margin-bottom: 32px;
    88|  text-align: center;
    89|}
    90|
    91|section.lead p {
    92|  font-size: 24px;
    93|  color: var(--color-foreground);
    94|  font-weight: 300;
    95|}
    96|
    97|hr {
    98|  border: none;
    99|  border-top: 1px solid var(--color-accent);
   100|  margin: 40px 0;
   101|}
   102|</style>
   103|
   104|<!-- _class: lead -->
   105|
   106|# プレゼンテーション
   107|
   108|シンプル＆ミニマル
   109|
   110|---
   111|
   112|## アジェンダ
   113|
   114|- トピック1
   115|- トピック2
   116|- トピック3
   117|
   118|---
   119|
   120|## スライドタイトル
   121|
   122|- ポイント1
   123|- ポイント2
   124|- ポイント3
   125|