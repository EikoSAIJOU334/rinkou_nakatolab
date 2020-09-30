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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="show partial lines of file")
    parser.add_argument("file", help="file path", type=str)
    parser.add_argument("number", help="number of lines", type=int)

    args = parser.parse_args()

    filename = args.file
    nlines = args.number
    print('file: %s' % filename)
    print('number: %d' % nlines)

#     len = count_lines(filename)

#     print('length is {}'.format(len))

    lines = rinkou_1_2.read_file(filename)
# Gina: 他のスクリプトから自作関数を引用するときは、インポートするスクリプトファイルの名前も必要になります。
# Gina: つまり、rinkou_1_2.read_file（）とすることで利用できます。

# SAIJOU: 便利ですね！




# 入力のうち先頭のN行を出力する
    print("先頭の" + str(nlines) + "行は")
    print(lines.head(nlines))

# 入力のうち末尾のN行を出力する
    print("末尾の" + str(nlines) + "行は")
    print(lines.tail(nlines))

# SAIJOU: head, tail関数は作れなかったですが、寝ることにします。。。
