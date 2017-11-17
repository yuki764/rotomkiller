# Rotom Killer

## 概要

ポケモン公式LINEアカウントのロトムが仕掛けてくる「しりとりバトル」に勝つためのスクリプトです。

## 使い方
Python 3がインストールされた環境でご使用ください。
`--auto` オプションを付けると、次に答えるべきポケモンをランダムに選択します。
付けなかった場合は、一覧が表示されるので好きなポケモンを選んで入力してください。

```bash
python3 shiritori.py [--auto|-a]
```

## 実行例
```
$ python3 shiritori.py
Rotom: アーボ
* ボスゴドラ
* ボーマンダ
* ボルトロス
* ボクレー
You: イーブイ
error: This isn't a name of Pokemon and in a candidates list.
You: ボーマンダ
Rotom: ダークライ
* イシツブテ
* イワーク
* イーブイ
* イトマル
* イノムー
* イルミーゼ
* イシズマイ
* イワパレス
* イベルタル
* イワンコ
You: surrender
You lose...
```
