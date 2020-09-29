# importするライブラリは冒頭にまとめて記述
import os
# os: 雑多なオペレーティングシステムインタフェース
import sys
# sys: システムパラメータと関数
import argparse
# argparse: プログラム実行時にコマンドラインで引数を受け取る処理を簡単に実装できる標準ライブラリ

# Pandasのインポート
import pandas as pd

# address.txtの読み込み
## 変数名はadとした
## ad = pd.read_csv("address.txt", sep='\t')

def read_file(path):
    lines = []
#    with open(path, "r", encoding="utf-8") as f:
    lines = pd.read_csv(path, sep='\t', encoding="utf-8")
#        lines = f.readlines()
#        lines = [ln.strip(os.linesep) for ln in lines]

    return lines

# change this function that uses pandas library
def count_lines(file_path):
    lines = read_file(file_path)
    return len(lines)

# main関数を定義 (to increase readability)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="show partial lines of file")
    parser.add_argument("file", help="file path", type=str)
    parser.add_argument("number", help="number of lines", type=int)

    args = parser.parse_args()

    filename = args.file
    nlines = args.number
    print('file: %s' % filename)
    print('number: %d' % nlines)

    len = count_lines(filename)

    print('length is {}'.format(len))

## 先頭を表示して読み込みの確認
# print('データの先頭を表示')
# print(ad.head)

## ファイルの行数をカウント、表示
# print('データの行数を表示')
# print(len(ad))

## ちなみに119045と表示される

## タブをスペースに置換したファイルを出力する
## address_space.txtというファイル名にした
# lines.to_csv('{}_space.txt'.format(filename), sep=' ', header=False, index=False)
