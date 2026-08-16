---
name: marp-slide-template-basic
description: "Marp Slide Template Basic"
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
    11|  --color-background: #f8f8f4;
    12|  --color-foreground: #3a3b5a;
    13|  --color-heading: #4f86c6;
    14|  --color-hr: #000000;
    15|  --font-default: 'Noto Sans JP', 'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif;
    16|}
    17|
    18|section {
    19|  background-color: var(--color-background);
    20|  color: var(--color-foreground);
    21|  font-family: var(--font-default);
    22|  font-weight: 400;
    23|  box-sizing: border-box;
    24|  border-bottom: 8px solid var(--color-hr);
    25|  position: relative;
    26|  line-height: 1.7;
    27|  font-size: 22px;
    28|  padding: 56px;
    29|}
    30|
    31|section:last-of-type {
    32|  border-bottom: none;
    33|}
    34|
    35|h1, h2, h3, h4, h5, h6 {
    36|  font-weight: 700;
    37|  color: var(--color-heading);
    38|  margin: 0;
    39|  padding: 0;
    40|}
    41|
    42|h1 {
    43|  font-size: 56px;
    44|  line-height: 1.4;
    45|  text-align: left;
    46|}
    47|
    48|h2 {
    49|  position: absolute;
    50|  top: 40px;
    51|  left: 56px;
    52|  right: 56px;
    53|  font-size: 40px;
    54|  padding-top: 0;
    55|  padding-bottom: 16px;
    56|}
    57|
    58|h2::after {
    59|  content: '';
    60|  position: absolute;
    61|  left: 0;
    62|  bottom: 8px;
    63|  width: 60px;
    64|  height: 2px;
    65|  background-color: var(--color-hr);
    66|}
    67|
    68|h2 + * {
    69|  margin-top: 112px;
    70|}
    71|
    72|h3 {
    73|  color: var(--color-foreground);
    74|  font-size: 28px;
    75|  margin-top: 32px;
    76|  margin-bottom: 12px;
    77|}
    78|
    79|ul, ol {
    80|  padding-left: 32px;
    81|}
    82|
    83|li {
    84|  margin-bottom: 10px;
    85|}
    86|
    87|footer {
    88|  font-size: 0;
    89|  color: transparent;
    90|  position: absolute;
    91|  left: 56px;
    92|  right: 56px;
    93|  bottom: 40px;
    94|  height: 8px;
    95|  background-color: var(--color-heading);
    96|}
    97|
    98|section.lead {
    99|  border-bottom: 8px solid var(--color-hr);
   100|}
   101|
   102|section.lead footer {
   103|  display: none;
   104|}
   105|
   106|section.lead h1 {
   107|  margin-bottom: 24px;
   108|}
   109|
   110|section.lead p {
   111|  font-size: 24px;
   112|  color: var(--color-foreground);
   113|}
   114|</style>
   115|
   116|<!-- _class: lead -->
   117|
   118|# プレゼンテーションタイトル
   119|
   120|あなたの名前2024年XX月XX日
   121|
   122|---
   123|
   124|## アジェンダ
   125|
   126|- トピック1
   127|- トピック2
   128|- トピック3
   129|- トピック4
   130|
   131|---
   132|
   133|## スライドタイトル
   134|
   135|- ポイント1
   136|- ポイント2
   137|- ポイント3
   138|
   139|---
   140|
   141|## まとめ
   142|
   143|- 要点1
   144|- 要点2
   145|- ご清聴ありがとうございました
   146|