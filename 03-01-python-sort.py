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
        address_number_list = []
        print_str_list = []
        # それぞれの行の郵便番号とスペース区切りの文字列をリストで格納する
        for row_list in reader:
            address_number_list.append(int(row_list[1]))
            print_str_list.append(' '.join(row_list))

        ＃郵便番号順にソートする
        for i in range(len(print_str_list)):
            for j in range(i+1, len(print_str_list)):
                if address_number_list[i] > address_number_list[j]:
                    address_number_list[i], address_number_list[j] = address_number_list[j], address_number_list[i]
                    print_str_list[i], print_str_list[j] = print_str_list[j], print_str_list[i]

        # さいごにそれぞれの行を順番に表示する
        for print_str in print_str_list:
            print(print_str)

print_format('./input_data/address_data.csv')
