# importするライブラリは冒頭にまとめて記述
import os
import sys
import argparse
import pandas as pd
# 自作の関数をモジュールとして読み込む
import utils

if __name__ == "__main__":

    information='''Type (1~5) of analysis:
            type1: display the number of lines;
            type2: export file as space-limited file;
            type3: export the initial "n" lines;
            type4: exprot the last "n" lines;
            type5: Count the first column & display string/counts;'''

    parser = argparse.ArgumentParser(description="show partial lines of file")
    parser.add_argument("mode",help=information,type=str)
    parser.add_argument("file", help="file path", type=str)
    parser.add_argument("number", help="number of lines", type=int)

    args = parser.parse_args()

    mode = args.mode
    filename = args.file
    nlines = args.number

if mode == 'type1':
    print('length is {}'.format(utils.count_lines(filename)))

elif mode == 'type2':
    utils.export_space_file(filename)

elif mode == 'type3':
    utils.print_head_n(filename, nlines)

elif mode == 'type4':
    utils.print_tail_n(filename, nlines)

elif mode == 'type5':
    utils.count_city_number(filename)
    
else:
    print(information)
