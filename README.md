# Scraping Practice

※ このプロジェクトは現在準備中です。

Pythonによるスクレイピングのデモサイトです。
スクレイピング練習用サイトはPythonでjsonデータを読み込み、HTMLとして組み立てています。  
BeautifulSoupとSeleniumを使ったスクレイピングコード、およびダミー求人データを元にHTMLを組み立てるコードを含みます。

[スクレイピング練習用サイト](https://nyaataco.github.io/scraping_practice_site/page1.html)
<br><br>

## リポジトリ構成

<pre><code>project_root/
├── scraping_with_beautifulsoup.py  # BeautifulSoupでスクレイピング（準備中）
├── scraping_with_selenium.py       # Seleniumでスクレイピング（準備中）
├── make_site/
│   ├── create_html.py              # jobs.jsonを読み込んでHTMLを組み立てる
│   ├── jobs.json                   # ダミー求人データ
│   ├── style.css                   # 出力HTMLに適用するスタイル
│   ├── base.html                   # HTMLの設計テンプレート（展示用）
│   └── scraping_practice_site/
│       └── page1.htmlなど          # create_html.pyから出力されるHTMLファイル
└── README.md                       # プロジェクトの説明
</code></pre>

<br>

- `make_site`: **Pythonスクレイピングの練習用に自作したダミー求人サイト**を作成するためのデータとスクリプトが入っています。

`jobs.json` 内の架空の求人情報を  
`create_html.py` から読み出して HTML として書き出します。

※ 実在する求人情報ではなく、すべて架空のデータを使っています。

---

## 技術スタック

- Python（BeautifulSoup, Selenium, OpenPyExcel）
- HTML/CSS

---

## 注意

- このサイトに掲載されている求人情報はすべて架空のものです。
- 万が一同じ名前の企業があったとしても、実在する企業・求人情報とは一切関係ありません。
- ダミーデータはAIによって生成されたものです。

---

