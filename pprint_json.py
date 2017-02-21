import json
import os
import argparse


def load_json_data(filepath):
    if not os.path.exists(filepath):
        return None

    with open(filepath, 'r', encoding='utf8') as file_handler:
        return json.load(file_handler)


def get_pretty_dict(data, number_tabs):
    return_str = '{\n'
    dict_keys = sorted(data.keys())
    for key in dict_keys:
        return_str += '\t' * number_tabs
        return_str += get_pretty_json(key, number_tabs+1)
        return_str += ': '
        return_str += get_pretty_json(data[key], number_tabs+1)
        if key == dict_keys[-1]:
            return_str += '\n'
        else:
            return_str += ',\n'
    return_str += '\t' * (number_tabs - 1)
    return_str += '}'
    return return_str


def get_pretty_list(data, number_tabs):
    return_str = '[\n'
    for item in data:
        return_str += '\t' * number_tabs
        return_str += get_pretty_json(item, number_tabs+1)
        if item == data[-1]:
            return_str += '\n'
        else:
            return_str += ',\n'
    return_str += '\t' * (number_tabs - 1)
    return_str += ']'
    return return_str


def get_pretty_json(data, number_tabs):
    result_str = ''
    if data is None:
        result_str += 'null'

    if isinstance(data, int) or isinstance(data, float):
        result_str += str(data)

    if isinstance(data, str):
        result_str += "\"" + data + "\""

    if isinstance(data, dict):
        result_str += get_pretty_dict(data, number_tabs)

    if isinstance(data, list):
        result_str += get_pretty_list(data, number_tabs)

    return result_str


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Printing pretty some json')
    parser.add_argument('filepath', metavar='filepath', type=str, nargs=1,
                        help='path to json file')

    args = parser.parse_args()
    filepath = args.filepath[0]

    if not os.path.exists(filepath):
        print("Incorrect path")
        exit(-1)

    json_content = load_json_data(filepath)

    pretty_json = get_pretty_json(json_content, 1)

    print(pretty_json)
