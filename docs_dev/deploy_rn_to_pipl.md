# README to publish

📖 [Pythonスクリプトってどうやってパブリッシュするんだぜ（＾～＾）？](https://crieit.net/drafts/61a3496b73b42)  

## Step O1o0

👇 ソースは、 `src` ディレクトリーを作って、その中に入れてほしい  

```plaintext
👉  └── 📂 src
        └── 📂 パッケージ名
            └── 📄 __init__.py
```

## Step O2o0

👇 （していなければ）pipを更新  

```shell
python -m pip install --upgrade pip
```

## Step O3o0

👇 （していなければ）buildパッケージをインストール  

```shell
python.exe -m pip install --upgrade build
```

## Step O4o0

👇 （していなければ）以下のファイルを新規作成  

```plaintext
    ├── 📂 src
    │   └── 📂 パッケージ名
    │       └── 📄 __init__.py
👉  ├── 📄 setup.cfg  
👉  └── 📄 setup.py  
```

## Step O5o0

２回目以降のアップロードでは、 `setup.cfg`, `setup.py` ファイルの中のバージョン番号を上げてほしい  

## Step O6o0

（必要ないかもしれないが build をする前に） Git Hub などのリポジトリ―を利用しているなら、コミットしていないファイルがあればコミットしておくといいかもしれない  

## Step O7o0

👇 buildを実行  

```shell
python.exe -m build
```

👇 dist ディレクトリーが自動生成される  

```plaintext
    ├── 📂 dist
👉  │       ├── 📄 パッケージ名-バージョン-py3-none-any.whl
👉  │       └── 📄 パッケージ名-バージョン.tar.gz
    ├── 📂 src
    │   └── 📂 パッケージ名
    │       └── 📄 __init__.py
    ├── 📄 setup.cfg  
    └── 📄 setup.py  
```

## Step O8o0

👇 まず、テスト環境へのアップロードを試します  
PyPi へログインするためのユーザー名とパスワードの入力が求められます  

```shell
python.exe -m twine upload --repository testpypi dist/* --verbose
```

ログインに成功すると、アップロードが行われ、 URL が出てくるのでアクセスしてください  

## Step O9o0

👇 本番です  

```shell
python.exe -m twine upload dist/*
```

ログインに成功すると、アップロードが行われ、 URL が出てくるのでアクセスしてください  
