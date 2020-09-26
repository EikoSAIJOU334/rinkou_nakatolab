# importするライブラリは冒頭にまとめて記述
import os
# os: 雑多なオペレーティングシステムインタフェース
import sys
# sys: システムパラメータと関数
import argparse
# argparse: プログラム実行時にコマンドラインで引数を受け取る処理を簡単に実装できる標準ライブラリ

# Pandas、及び必要なライブラリのインポート
import pandas as pd

# address.txtの読み込み
# 変数名はadとした
ad = pd.read_csv("address.txt", sep='\t')

# 先頭を表示して読み込みの確認
print('データの先頭を表示')
print(ad.head)

# ファイルの行数をカウント、表示
print('データの行数を表示')
print(len(ad))

# ちなみに119045と表示される

# タブをスペースに置換したファイルを出力する
# address_space.txtというファイル名にした
ad.to_csv('address_space.txt', sep=' ')
