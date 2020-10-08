import os
import sys
import pandas as pd

# こちらに、課題１から課題５までの関数を集約

# Pandasでlinesにaddress.txtを読み込む関数
def read_file(path):
    lines = pd.read_csv(path, sep='\t', encoding="utf-8", names=['city', 'address'])
    return lines

# 課題１、read_file()で読み込んだファイルの行数をカウントする関数
def count_lines(file_path):
    lines = read_file(file_path)
    return len(lines)

# 課題２、read_file()で読み込んだファイルのタブをスペースに置換したファイルを出力する関数
def export_space_file(file_path):
    lines = read_file(file_path)
    prefix = os.path.splitext(file_path)[0]
    output = '{}_space.txt'.format(prefix)
    lines.to_csv(output, sep=' ', header=False, index=False)
    print(output + ' file is saved!')

# 課題３、自然数Nをコマンドライン引数にとり、入力のうち先頭のN行を出力する関数
def print_head_n(file_path, nlines):
    lines = read_file(file_path)
    if nlines > len(lines) or 0 > nlines:
        print('自然数Nの入力が不正です')
        print('1以上' + str(len(lines)) + '以下で数字を入力してください')
        return
    else:
        print("先頭の" + str(nlines) + "行は")
        print(lines.head(nlines))

# 課題4、自然数Nをコマンドライン引数にとり、入力のうち末尾のN行を出力する関数
def print_tail_n(file_path, nlines):
    lines = read_file(file_path)
    if nlines > len(lines) or 0 > nlines:
        print('自然数Nの入力が不正です')
        print('1以上' + str(len(lines)) + '以下で数字を入力してください')
        return
    else:
        print("末尾の" + str(nlines) + "行は")
        print(lines.tail(nlines))

#課題５、１列目の文字列を集計して標準出力に表示する関数
def count_city_number(file_path):
    lines = read_file(file_path)
    lines_city_count = lines["city"].value_counts(sort=True)
    print(lines_city_count)
# Gina: groupbyだとソートができなかったので、堺谷さんたちのグループの.value_counts()を参考にしました。
# Gina: sort=Trueとすると昇順にソートしてくれるようです。

#    lines_groupby = lines.groupby('city')
#    print(lines_groupby.count().sort_values())
