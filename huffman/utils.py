import os


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
        with open(file_path, 'rb') as f:
            nums = f.read()
        return nums
    else:
        return False


def toBytesText(data):
    r = []
    for i in range(0, len(data), 8):
        r.append(int(data[i:i + 8], 2))
    return bytes(r)
