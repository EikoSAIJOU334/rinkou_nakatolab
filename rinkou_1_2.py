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
    #lines = []
    # Gina: pd.read_csv()によってファイルを読み込むと、pandas.Dataframe型になるので、リストを先に作る必要はないです

#    with open(path, "r", encoding="utf-8") as f:
    lines = pd.read_csv(path, sep='\t', encoding="utf-8", names=['prefecture_city', 'address']) # header=None)
    # Gina: 確認したところ、一行目が自動的にheaderに指定されていました。
    # Gina: header=Noneの代わりに、names=('header1', 'header2')都することで、header名を決められます。
#        lines = f.readlines()
#        lines = [ln.strip(os.linesep) for ln in lines]
    # SAIJOU: names = ['', '']でheaderを追加しました。おおきに～

    return lines

# change this function that uses pandas library
def count_lines(file_path):
    lines = read_file(file_path)
    prefix = os.path.splitext(file_path)[0]
    output = '{}_space.txt'.format(prefix)
    lines.to_csv(output, sep=' ', header=False, index=False)
        # Gina: read_file()から移しました。
        # Gina: ここのoutputのfile名の決め方、流石です！　.format()思いつきませんでした！
        # Gina: 関数の中で変数を一致させるために、filename -> pathにすると良いともいます
        # Gina: また、このままだと、address.txt_space.txtというファイルができているので、
        #       ファイル名と拡張子を分割する、os.path.splitext(path)[0]を.format()のかっこの中に使うと、
        #       address_space.txtという出力ファイルができます。
        #       os.path.splitext(path)では、[".より前のファイル名",".を含んだ拡張子"]を出力します。
        #       今回の例では、["address",".txt"]になります。
        #       os.path.splitext(path)[0]とするとファイル名の文字列を選択できます。

        # Gina: 中戸先生からのコメントとしては、lines.to_csv（）の中身が長いので、分割したほうが行が短くなって見やすいとのことでした
        # Gina: Atomの画面に見えてる縦線が目安となるコードの長さだそうです

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

# 輪読の総括： 一連の作業をしているブロックは、行がたくさんにならないように関数で括り出すとスッキリする。
#           -> 今回はpandasを使うと基本的に行が少なくなる。
#           -> pandasに頼らなくても手動ですることもできる -> 堺谷さん、仲島さんチーム参照
#
#           最終的にはコマンド引数にオプションをつけたときに課題１〜５をそれぞれ実行するようにする。
#           -> 牧野先生、王さんチームのコマンドが参考になります。
#           -> 例えば、$python sample.py address.txt type1 とすると行数を出力するなど。

## 先頭を表示して読み込みの確認
# print('データの先頭を表示')
# print(ad.head)

## ファイルの行数をカウント、表示
# print('データの行数を表示')
# print(len(ad))

## ちなみに119045と表示される
 # SAIJOU: headerで一行取られたために、一行少なく表示されていた

## タブをスペースに置換したファイルを出力する
## address_space.txtというファイル名にした
# lines.to_csv('{}_space.txt'.format(filename), sep=' ', header=False, index=False)
