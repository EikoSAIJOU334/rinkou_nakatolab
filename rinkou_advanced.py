# importするライブラリは冒頭にまとめて記述
import os
import sys
import argparse
import pandas as pd

# 自作の関数をモジュールとして読み込む
import utils2

if __name__ == "__main__":
    information='''Type (6~8) of analysis:
            type6: display from m to n lines;
            type7: export non redundant city file;
            type8: display address acording to frequency;'''


    parser = argparse.ArgumentParser(description="show partial lines of file")
    parser.add_argument("mode",help=information,type=str)
    parser.add_argument("file", help="file path", type=str)
    parser.add_argument("mnumber", help="number of mlines", type=int)
    parser.add_argument("nnumber", help="number of nlines", type=int)

    args = parser.parse_args()

    mode = args.mode
    filename = args.file
    mlines = args.mnumber
    nlines = args.nnumber

if mode == 'type6':
    utils2.print_m_to_n_lines(filename, mlines, nlines)

elif mode == 'type7':
    utils2.export_city(filename)

elif mode == 'type8':
    utils2.print_address(filename)

else:
    print(information)
