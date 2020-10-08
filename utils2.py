import os
import sys
import pandas as pd

# こちらに、課題6から課題8までの関数を集約

# Pandasでlinesにaddress.txtを読み込む関数
def read_file(path):
    lines = pd.read_csv(path, sep='\t', encoding="utf-8", names=['city', 'address'])
    return lines

# 課題６、自然数M, Nをコマンドライン引数にとり、入力のうちM行目からN行目を出力する関数
def print_m_to_n_lines(file_path, mlines, nlines):
    lines = read_file(file_path)
    if mlines >= nlines:
        print('２つ目の数字は１つ目よりも大きい値を入力してください')
        return
    elif mlines < 0:
        print('0以上の値を入力してください')
        return
    elif mlines > len(lines) or nlines > len(lines):
        print(str(len(lines)) + 'よりも小さい値を入力してください')
        return
    else:
        print(lines[mlines:nlines])

# 課題７、１列目だけファイルに出力する（重複行は除去する、順番は任意）関数
def export_city(file_path):
    lines = read_file(file_path)
    prefix = os.path.splitext(file_path)[0]
    output = '{}_city.txt'.format(prefix)
    lines_groupby_city = lines.groupby('city') # cityごとにグループ化
    lines2 = lines_groupby_city.first() # グループごとに最初の１行を抽出
    lines2.to_csv(output, header=False, index=False)
    print(output + ' file is saved!')

# 課題８、各行の２列目の文字列の出現頻度を求め、出現頻度の高い順にソートして標準出力に表示する関数
def print_address(file_path):
    lines = read_file(file_path)
    lines_groupby_address = lines.groupby('address') # addressごとにグループ化
    lines_size_address = lines_groupby_address.size() # グループごとに数をカウント
    lines_size_address_s = lines_size_address.sort_values('size')
    print(lines_size_address_s['address'])
