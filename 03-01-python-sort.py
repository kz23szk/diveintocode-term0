# coding:utf-8
import csv


def print_format(file_path):
    '''
    file_pathのcsvファイルを読み込み、
    郵便番号順にスペース区切りでデータを表示する
    '''
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        # 項目名は先に表示する
        print(' '.join(next(reader)))
        # 郵便番号順で並び替える
        sorted_address = sorted(reader, key=lambda x: x[1]) 
        for print_str in sorted_ddress:
            print(' '.join(print_str))


print_format('./address_data.csv')
