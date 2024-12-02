# python-gui-for-ai

LangGraphを利用したアプリケーション旨のGUI

## Getting Started

- [uv](https://docs.astral.sh/uv/)使ってください

```bash
# 必要なパッケージを仮想環境にインストール
uv sync
# アプリケーションを起動
uv run .\src\app.py
```

## Format・Lint

```bash
uv run ruff check
```

## Build

以下コマンドを実行すると、distフォルダ配下にexeファイルが出力されます

```bash
uv run pyinstaller .\src\app.py --onefile
```
