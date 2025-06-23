# 国会議員の発言傾向可視化アプリ

![demo](https://github.com/yut0takagi/kokkai-analytics/raw/main/src/output.gif)

このアプリは、国会会議録APIを活用して特定の議員の発言を取得し、その傾向をWordCloudで可視化するStreamlitベースのWebアプリです。

## 🔧 機能概要

- 国会会議録APIから議員の発言データを取得
- 発言内容から名詞を抽出してWordCloudを生成
- Streamlitで直感的なインターフェースを提供

## 📦 必要なパッケージ

```bash
pip install streamlit requests beautifulsoup4 janome wordcloud matplotlib lxml
```

## ▶️ 起動方法

```bash
streamlit run app.py
```

## 🗂 ディレクトリ構成

```bash
project/
├── app.py
├── utils/
│   ├── fetch_kokkai.py
│   └── analyzer.py
└── README.md
```

## 📝 備考

- フォントエラーを回避するため、日本語フォント（ヒラギノなど）のパスを環境に応じて設定してください。
- 取得対象の発言数は最大100件までに制限されています（APIの制限による）。
