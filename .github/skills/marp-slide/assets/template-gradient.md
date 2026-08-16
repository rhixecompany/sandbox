---
name: marp-slide-template-gradient
description: "Marp Slide Template Gradient"
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
    11|  --color-foreground: #ffffff;
    12|  --color-heading: #ffffff;
    13|  --color-accent: #ffd700;
    14|  --font-default: 'Noto Sans JP', 'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif;
    15|}
    16|
    17|section {
    18|  background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
    19|  color: var(--color-foreground);
    20|  font-family: var(--font-default);
    21|  font-weight: 400;
    22|  box-sizing: border-box;
    23|  position: relative;
    24|  line-height: 1.7;
    25|  font-size: 22px;
    26|  padding: 56px;
    27|}
    28|
    29|section:nth-child(2n) {
    30|  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    31|}
    32|
    33|section:nth-child(3n) {
    34|  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    35|}
    36|
    37|section:nth-child(4n) {
    38|  background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    39|}
    40|
    41|section:nth-child(5n) {
    42|  background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
    43|}
    44|
    45|h1, h2, h3, h4, h5, h6 {
    46|  font-weight: 700;
    47|  color: var(--color-heading);
    48|  margin: 0;
    49|  padding: 0;
    50|  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
    51|}
    52|
    53|h1 {
    54|  font-size: 56px;
    55|  line-height: 1.4;
    56|  text-align: left;
    57|}
    58|
    59|h2 {
    60|  position: absolute;
    61|  top: 40px;
    62|  left: 56px;
    63|  right: 56px;
    64|  font-size: 40px;
    65|  padding-top: 0;
    66|  padding-bottom: 16px;
    67|}
    68|
    69|h2::after {
    70|  content: '';
    71|  position: absolute;
    72|  left: 0;
    73|  bottom: 8px;
    74|  width: 80px;
    75|  height: 3px;
    76|  background-color: var(--color-accent);
    77|  box-shadow: 0 2px 10px rgba(255, 215, 0, 0.5);
    78|}
    79|
    80|h2 + * {
    81|  margin-top: 112px;
    82|}
    83|
    84|h3 {
    85|  color: var(--color-accent);
    86|  font-size: 28px;
    87|  margin-top: 32px;
    88|  margin-bottom: 12px;
    89|  text-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
    90|}
    91|
    92|ul, ol {
    93|  padding-left: 32px;
    94|}
    95|
    96|li {
    97|  margin-bottom: 10px;
    98|  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
    99|}
   100|
   101|footer {
   102|  font-size: 16px;
   103|  color: rgba(255, 255, 255, 0.7);
   104|  position: absolute;
   105|  left: 56px;
   106|  right: 56px;
   107|  bottom: 40px;
   108|  text-align: center;
   109|  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
   110|}
   111|
   112|section.lead {
   113|  background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
   114|  display: flex;
   115|  flex-direction: column;
   116|  justify-content: center;
   117|  align-items: center;
   118|  text-align: center;
   119|}
   120|
   121|section.lead h1 {
   122|  margin-bottom: 24px;
   123|  text-align: center;
   124|}
   125|
   126|section.lead p {
   127|  font-size: 24px;
   128|  color: var(--color-foreground);
   129|  text-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
   130|}
   131|
   132|strong {
   133|  color: var(--color-accent);
   134|  font-weight: 700;
   135|  text-shadow: 0 1px 5px rgba(0, 0, 0, 0.3);
   136|}
   137|</style>
   138|
   139|<!-- _class: lead -->
   140|
   141|# プレゼンテーション
   142|
   143|グラデーション背景
   144|
   145|---
   146|
   147|## アジェンダ
   148|
   149|- トピック1
   150|- トピック2
   151|- トピック3
   152|
   153|---
   154|
   155|## スライド
   156|
   157|- ポイント1
   158|- ポイント2
   159|- ポイント3
   160|