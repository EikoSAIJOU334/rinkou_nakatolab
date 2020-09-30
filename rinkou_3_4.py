# importするライブラリは冒頭にまとめて記述
import os
# os: 雑多なオペレーティングシステムインタフェース
import sys
# sys: システムパラメータと関数
import argparse
# argparse: プログラム実行時にコマンドラインで引数を受け取る処理を簡単に実装できる標準ライブラリ

# Pandas、及び必要なライブラリのインポート
import pandas as pd

import rinkou_1_2
# Gina: rinkou_1_2で作成した関数の引用のため



lines = rinkou_1_2.read_file(filename)
# Gina: 他のスクリプトから自作関数を引用するときは、インポートするスクリプトファイルの名前も必要になります。
# Gina: つまり、rinkou_1_2.read_file（）とすることで利用できます。

# address.txtの読み込み
# 変数名はadとした
ad = pd.read_csv("address.txt", sep='\t', header=None)

# 自然数Nをコマンドライン引数で受け取る。今回は３とした。
N = 3

# 入力のうち先頭のN行を出力する
print("先頭の" + str(N) + "行は")
print(ad.head(N))

# 入力のうち末尾のN行を出力する
print("末尾の" + str(N) + "行は")
print(ad.tail(N))
