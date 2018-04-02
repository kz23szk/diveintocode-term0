# coding:utf-8
import csv

def print_format(file_path):
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        print(' '.join(next(reader)))
        address_number_list = []
        print_str_list = []
        for row_list in reader:
            address_number_list.append(int(row_list[1]))
            print_str_list.append(' '.join(row_list))

        for i in range(len(print_str_list)):
            for j in range(i+1, len(print_str_list)):
                if address_number_list[i] > address_number_list[j]:
                    address_number_list[i], address_number_list[j] = address_number_list[j], address_number_list[i]
                    print_str_list[i], print_str_list[j] = print_str_list[j], print_str_list[i]

        for print_str in print_str_list:
            print(print_str)

print_format('./input_data/address_data.csv')
