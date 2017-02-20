import json
import os
import sys


def load_json_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def pretty_print(data, number_tabs):
    if isinstance(data, int) or isinstance(data, float):
        print(data, end='', sep='')

    if isinstance(data, str):
        print("\""+data+"\"", end='', sep='')

    if isinstance(data, dict):
        print('{')
        dict_keys = sorted(data.keys())
        for key in dict_keys:
            print('\t'*number_tabs, end='')
            pretty_print(key, number_tabs+1)
            print(': ', end='')
            pretty_print(data[key], number_tabs+1)
            if key == dict_keys[-1]:
                print('')
            else:
                print(',')
        print('\t'*(number_tabs-1), end='')
        print('}', end='')

    if isinstance(data, list):
        print('[')
        for item in data:
            print('\t'*number_tabs, end='')
            pretty_print(item, number_tabs+1)
            if item == data[-1]:
                print('')
            else:
                print(',')
        print('\t'*(number_tabs-1), end='')
        print(']', end='')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Input path to the json file second argument")
        exit()
    filepath = sys.argv[1]

    if not os.path.exists(filepath):
        print("Incorrect path")
        exit()

    json_content = load_json_data(filepath)

    pretty_print(json_content, 1)
