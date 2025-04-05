# FizzBuzz Project

このプロジェクトは、FizzBuzz問題を解決するためのPythonプログラムを含んでいます。

## FizzBuzzとは

FizzBuzzは、1から指定された数までの整数を順に出力するプログラムです。ただし、以下のルールに従います：
- 数が3で割り切れる場合は、"Fizz"と出力します。
- 数が5で割り切れる場合は、"Buzz"と出力します。
- 数が3と5の両方で割り切れる場合は、"FizzBuzz"と出力します。
- それ以外の場合は、数をそのまま出力します。

## ファイル構成

- `src/fizzbuzz.py`: FizzBuzz関数の実装。
- `tests/test_fizzbuzz.py`: FizzBuzz関数のテストコード。

## 実行方法

1. 仮想環境を有効化します。
2. `uv run pytest`を実行して、テストを確認します。

## 必要なパッケージ

- `pytest`: テストフレームワーク

## インストール

以下のコマンドで必要なパッケージをインストールできます：

```bash
uv add pytest
```