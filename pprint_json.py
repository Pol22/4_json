import json
import os
import sys


def load_json_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


# 0 = first, 1 = last
def pretty_print_json(data, number_of_tabs, first_or_last):

    if isinstance(data, list):
        print('[')
        for item in data:
            pretty_print_json(item, number_of_tabs + 1, 1)
            if item != data[len(data)-1]:
                print(',')
            else:
                print()
        print('\t' * (number_of_tabs - 1), ']', end='', sep='')
    elif isinstance(data, dict):
        if first_or_last:
            print('\t' * number_of_tabs, '{')
        else:
            print('{')
        keys = list(data.keys())
        keys.sort()
        number_of_tabs += 1
        for item in keys:
            print('\t' * number_of_tabs, '"', item, '"', ': ', sep='', end='')
            pretty_print_json(data[item], number_of_tabs + 1, 0)
            if item != keys[len(keys)-1]:
                print(',')
            else:
                print('\t' * -1)
        print('\t' * (number_of_tabs - 1), '}', end='')
    elif isinstance(data, str):
        print('"', data, '"', end='', sep='')
    elif data is None or isinstance(data, int):
        print(data, end='', sep='')
    else:
        print('\t' * number_of_tabs, data, end='', sep='')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Input path to the json file second argument")
        exit()
    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        print("Incorrect path")
        exit()
    json_content = load_json_data(filepath)
    pretty_print_json(json_content, 0, 1)
