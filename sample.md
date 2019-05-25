name: inverse
layout: true
class: center, middle, inverse

---

# title

---

class: center, middle
layout:false

# スクレイピング・クローリングって？

---

## スクレイピングって？
> ウェブスクレイピング（英: Web scraping）とは、ウェブサイトから情報を抽出するコンピュータソフトウェア技術のこと。ウェブ・クローラーあるいはウェブ・スパイダーとも呼ばれる。  
> 通常このようなソフトウェアプログラムは低レベルのHTTPを実装することで、もしくはウェブブラウザを埋め込むことによって、WWWのコンテンツを取得する。  
引用： __[wiki](https://ja.wikipedia.org/wiki/ウェブスクレイピング)__

web上のデータを収集すること。  
業務において優先順位としては低め。最後の手段である。

まずは、目的に対し以下を検討する。
1. 必要な物理データがweb上で公開されていないか。
1. APIが公開されていないか。

検討の結果やむを得ない場合、スクレイピングによってデータ収集を行う。

---

## クローリングって？
> クローリングとは、ロボット型検索エンジンにおいて、プログラムがインターネット上のリンクを辿ってWebサイトを巡回し、Webページ上の情報を複製・保存することである。
> クローリングを行うためのプログラムは特に「クローラ」あるいは「スパイダー」と呼ばれている。クローラが複製したデータは、検索エンジンのデータベースに追加される。クローラが定期的にクローリングを行うことで、検索エンジンはWebページに追加・更新された情報も検索することが可能になっている。  
引用：https://www.weblio.jp/content/クローリング

複数ページにわたって巡回し、データを収集するようになったらそれはクローリングと呼ばれたりする。

---

class: center, middle
# 要素の取得

---

## CSS Selector
> セレクタとは、どの要素がそのスタイル規則によって影響されるかを指定するものである。文書の構造とスタイルシート内のスタイル規則の接着剤の役割を担う。上記の例では、h1セレクタによって h1要素が指定されている。文脈やプロパティや内容を考慮した複雑な要素選択を行うセレクタもある。  
https://ja.wikipedia.org/wiki/スタイルシート

CSSセレクタはCSSやjQueryを書きなれたヒトにオススメ。

---

## XML Path Language (XPath)

![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/XPath_example.svg/300px-XPath_example.svg.png)

> XML Path Language （XPath（エックスパス）） は、マークアップ言語 XMLに準拠した文書の特定の部分を指定する言語構文である。  
https://ja.wikipedia.org/wiki/XML_Path_Language

XPathを使うと、より簡潔かつ柔軟に指定ができる（といわれている）。


---

## 例

NCBIから「Single-Cell」検索結果の論文タイトルの取得を例にご紹介。
https://www.ncbi.nlm.nih.gov/pubmed/?term=Single-Cell

**CSSセレクタ**
```css
.title a
```

**XPath**

```css
//*[@id="maincontent"]/div/div[5]/div/div[2]/p/a
```

---

## データの格納先
- RDBに入れるのか、JSONで書き出すのか。
- 標準出力で出すだけで良いのか。
- 1TBを超える場合はHadoopなんかを検討する。

---
class: center, middle

# Pythonでスクレイピング・クローリング
---
## re
正規表現で取ってくるのが一番お手軽。  
Pythonで正規表現を使う時は、みんなお馴染み`re`モジュールを用いる。  

---

## requests
標準的なHTTPライブラリ。
`requests.get(url)`でhttpリクエストを送ることができる。
後述する`lxml`や`BeautifulSoup`と共に使用される。

---
## lxml

インストール
```sh
$ pip install lxml
```

C言語の高速実装な解析器。  
単体で使用する場合、高速。  
libxmlのラッパー。本来はXMLのパースに使用される。  
XPathを使用した要素の取得が可能。  

---
## BeautifulSoup

インストール
```sh
$ pip install beautifulsoup4
```

各種解析器を明示的に指定して使用することができるHTMLパーサー。  
定式化できるような処理の場合結構便利なので静的なHTMLを対象にクローリングする際には使う。  
XPath、CSSセレクタ、要素の属性・ID、タグの中身なんかで要素の取得ができる。

---

## BeautifulSoup使用例
google検索エンジンのタイトルを取ってくる例

```python
import requests
from bs4 import BeautifulSoup
URL = 'https://www.google.com/'
resp = requests.get(URL)
soup = BeautifulSoup(resp.text, features="html.parser")
# titleタグの取得
print(soup.title.text)
```

---

## Selenium

インストール
```sh
$ pip install selenium
```

ブラウザオートメーションツール。  

そもそもは、クロスブラウザ・クロスプラットフォームのUIテストツール。  
Pythonだけでなく、様々な言語でラッパーが存在する。  
ブラウザ及びそれを操作するためのドライバが必要。  
スクロール、クリックする、ウィンドウを開く・閉じる、キャプチャを撮る、タブを切り替える、キー入力等など、ブラウザ上で可能なことは何でもできる。  
参照：https://qiita.com/mochio/items/dc9935ee607895420186

---

## selenium使用例
```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get(URL)
# htmlの表示
print(driver.page_source)
```

---
## Scrapy
![:scale 50%](https://amelieff-esa-bucket.s3-ap-northeast-1.amazonaws.com/uploads/production/attachments/2943/2019/05/17/34115/35c7a6a1-d525-4f1f-af9c-eeb6eb669ddc.png)

https://scrapy.org/

Pythonが誇るスクレイピング・クローリング用フレームワーク。  
めちゃ便利。  
設定ファイルを使用するだけで、色々と良しなに設定してくれる（ログ出力、並列処理関連、robot.txt遵守、ランダムリクエスト、etc...）。  
__[この辺](https://github.com/clemfromspace/scrapy-selenium)__ 使えば、Seleniumと連携もできないこともない。

---

class: center, middle
# 便利な Google拡張

---

## [XPath Helper](https://chrome.google.com/webstore/detail/XPath-helper/hgimnogjllphhhkhlmebbmlgjoejdpjl?hl=ja)
ブラウザ上の要素をクリックすると、その要素を取得するためのXPathとそのXPathで取得できる要素が可視化され、要素名が出力される。

![image.png (323.3 kB)](https://amelieff-esa-bucket.s3-ap-northeast-1.amazonaws.com/uploads/production/attachments/2943/2019/05/17/34115/b69dd2ac-6962-4cd5-a252-940f09c43602.png)
![image.png (32.3 kB)](https://amelieff-esa-bucket.s3-ap-northeast-1.amazonaws.com/uploads/production/attachments/2943/2019/05/17/34115/4f6b1d7b-30f9-4f02-858f-341a830bf2f9.png)

---
## [SelectorGadget](https://chrome.google.com/webstore/detail/selectorgadget/mhjhnkcfbdhnjickkkdbjoemdmbfginb?hl=ja)
ブラウザ上の要素をクリックすると、その要素を取得するためのCSSセレクタとそのCSSセレクタで取得できる要素が可視化される。

![image.png (318.2 kB)](https://amelieff-esa-bucket.s3-ap-northeast-1.amazonaws.com/uploads/production/attachments/2943/2019/05/17/34115/e6c3fedb-51b7-4389-8960-c65f05a33ea4.png)
![image.png (4.5 kB)](https://amelieff-esa-bucket.s3-ap-northeast-1.amazonaws.com/uploads/production/attachments/2943/2019/05/17/34115/0c4b6c4e-f37a-4bfe-a690-15e7940d374a.png)

---

class: center, middle
# スクレイピングの際の注意点

---

## 利用規約や`robot.txt` に配慮する。
利用規約で明示的にスクレイピングが禁止されていることや、robot.txt
などでクローリングが禁止されていることがある。

Twitter
> 本サービスへのクローリングは、robots.txtファイルの定めによる場合は認められていますが、Twitterによる事前の同意がないまま本サービスのスクレイピングをすることは明示的に禁止されています  
https://twitter.com/ja/tos

Instagram
> 不正な方法を用いて、アカウントの作成、情報へのアクセス、または情報の取得を試みることは禁止されています。  
> これには、弊社から明示的な許可を得ることなく、自動化された手段を用いてアカウントを作成したり、情報を取得したりする行為が含まれます。  
https://help.instagram.com/581066165581870


---

## timeoutの指定
timeoutを指定しておかないと、Pythonがフリーズする。  
ゾンビプロセスになってしまう場合がある。

---

## 並列処理

- joblib
- multiprocess
- threading

なんかを使って並列処理するようにする。  
（Scrapyの場合、settingsをいじるだけで並列化対応可能）



---
