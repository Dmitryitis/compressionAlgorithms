import ast
import os


def input_path():
    path_file = input('Введите полный путь до файла: ')
    return path_file


def isFile(file_path):
    if os.access(file_path, os.F_OK):
        return True
    else:
        return False


def read_file(file_path):
    if os.access(file_path, os.F_OK):
        with open(file_path, 'r', encoding='utf-8') as f:
            nums = f.read().splitlines()
        return "".join(nums)
    else:
        return False


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


def read_file_decode(file_path):
    if os.access(file_path, os.F_OK):
        with open(file_path, 'r', encoding='utf-8') as f:
            nums = f.read().splitlines()
        return nums
    else:
        return False


def decodeTable():
    with open('table.txt', 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
    decode_table_dict = ast.literal_eval(lines[0])
    return decode_table_dict


def writeDictionary(text_dict):
    symbol_table = "{"
    for key, value in text_dict.items():
        symbol_table += f"'{key}': {value},"
    symbol_table += "}"

    return symbol_table


def dirIsExsists(path):
    if not os.path.exists(path):
        os.mkdir(path)
