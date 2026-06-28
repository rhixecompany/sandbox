---
name: marp-slide-template-colorful
description: "Marp Slide Template Colorful"
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
     8|@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700;900&display=swap');
     9|
    10|:root {
    11|  --color-background: #fff5f7;
    12|  --color-foreground: #2d2d2d;
    13|  --color-heading: #ff6b9d;
    14|  --color-accent-1: #ffd93d;
    15|  --color-accent-2: #6bcf7f;
    16|  --color-accent-3: #4d96ff;
    17|  --font-default: 'Noto Sans JP', 'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif;
    18|}
    19|
    20|section {
    21|  background: linear-gradient(135deg, var(--color-background) 0%, #ffe5ec 100%);
    22|  color: var(--color-foreground);
    23|  font-family: var(--font-default);
    24|  font-weight: 400;
    25|  box-sizing: border-box;
    26|  border-bottom: 10px solid var(--color-accent-1);
    27|  position: relative;
    28|  line-height: 1.7;
    29|  font-size: 24px;
    30|  padding: 56px;
    31|}
    32|
    33|section:last-of-type {
    34|  border-bottom: none;
    35|}
    36|
    37|h1, h2, h3, h4, h5, h6 {
    38|  font-weight: 900;
    39|  color: var(--color-heading);
    40|  margin: 0;
    41|  padding: 0;
    42|}
    43|
    44|h1 {
    45|  font-size: 64px;
    46|  line-height: 1.3;
    47|  text-align: left;
    48|  background: linear-gradient(135deg, var(--color-heading), var(--color-accent-3));
    49|  -webkit-background-clip: text;
    50|  -webkit-text-fill-color: transparent;
    51|  background-clip: text;
    52|}
    53|
    54|h2 {
    55|  position: absolute;
    56|  top: 40px;
    57|  left: 56px;
    58|  right: 56px;
    59|  font-size: 44px;
    60|  padding-top: 0;
    61|  padding-bottom: 20px;
    62|  background: linear-gradient(90deg, var(--color-heading), var(--color-accent-3));
    63|  -webkit-background-clip: text;
    64|  -webkit-text-fill-color: transparent;
    65|  background-clip: text;
    66|}
    67|
    68|h2::after {
    69|  content: '';
    70|  position: absolute;
    71|  left: 0;
    72|  bottom: 8px;
    73|  width: 80px;
    74|  height: 4px;
    75|  background: linear-gradient(90deg, var(--color-accent-1), var(--color-accent-2), var(--color-accent-3));
    76|  border-radius: 2px;
    77|}
    78|
    79|h2 + * {
    80|  margin-top: 120px;
    81|}
    82|
    83|h3 {
    84|  color: var(--color-accent-3);
    85|  font-size: 30px;
    86|  margin-top: 32px;
    87|  margin-bottom: 12px;
    88|}
    89|
    90|ul, ol {
    91|  padding-left: 32px;
    92|}
    93|
    94|li {
    95|  margin-bottom: 12px;
    96|}
    97|
    98|footer {
    99|  font-size: 0;
   100|  color: transparent;
   101|  position: absolute;
   102|  left: 56px;
   103|  right: 56px;
   104|  bottom: 40px;
   105|  height: 10px;
   106|  background: linear-gradient(90deg, var(--color-accent-1), var(--color-accent-2), var(--color-accent-3));
   107|  border-radius: 5px;
   108|}
   109|
   110|section.lead {
   111|  border-bottom: 10px solid var(--color-accent-1);
   112|  background: linear-gradient(135deg, #fff5f7 0%, #ffe5ec 50%, #ffd5e0 100%);
   113|}
   114|
   115|section.lead footer {
   116|  display: none;
   117|}
   118|
   119|section.lead h1 {
   120|  margin-bottom: 24px;
   121|}
   122|
   123|section.lead p {
   124|  font-size: 26px;
   125|  color: var(--color-foreground);
   126|  font-weight: 700;
   127|}
   128|
   129|strong {
   130|  color: var(--color-heading);
   131|  font-weight: 900;
   132|}
   133|</style>
   134|
   135|<!-- _class: lead -->
   136|
   137|# プレゼンテーション
   138|
   139|カラフル＆ポップ
   140|
   141|---
   142|
   143|## アジェンダ
   144|
   145|- トピック1
   146|- トピック2
   147|- トピック3
   148|
   149|---
   150|
   151|## スライド
   152|
   153|- ポイント1
   154|- ポイント2
   155|- ポイント3
   156|