import ast
import os
from decimal import Decimal


def input_path():
    path_file = input('Введите полный путь до файла: ')
    return path_file


def read_file(file_path):
    if os.access(file_path, os.F_OK):
        with open(file_path, 'r', encoding='utf-8') as f:
            nums = f.read().splitlines()
        return "".join(nums)
    else:
        return False


def read_file_decode(file_path):
    if os.access(file_path, os.F_OK):
        with open(file_path, 'r', encoding='utf-8') as f:
            nums = f.read().splitlines()
        return nums
    else:
        return False


def dirIsExsists(path):
    if not os.path.exists(path):
        os.mkdir(path)


def nameFiles(path):
    if path.find(chr(92)):
        path_split = path.split(chr(92))
        name_file = path_split[-1]
    elif path.find("/"):
        path_split = path.split('/')
        name_file = path_split[-1]
    else:
        name_file = path
    return name_file


def write_result_file(code, text_dict, symbol_length):
    symbol_table = "{"
    for key, value in text_dict.items():
        symbol_table += f"'{key}': {value},"
    symbol_table += "}"

    return f"{code}\n{symbol_table}\n{symbol_length}"


def decodeFileToString(lines):
    code = Decimal(lines[0])
    symbol_length = int(lines[2])
    text_dict = ast.literal_eval(lines[1])
    return code, text_dict, symbol_length


def segment_list(text_dict, text_length):
    segment_dict = dict.fromkeys(text_dict.keys(), [])
    sorted_items = sorted(text_dict.items())
    low = Decimal(0.0)

    for key, value in sorted_items:
        segment_dict[key] = []
        segment_dict[key].append(low)
        high = low + Decimal(text_dict[key] / text_length)
        segment_dict[key].append(high)
        low = high
    return segment_dict
