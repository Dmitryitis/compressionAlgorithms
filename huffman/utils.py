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


def decodeFileToString(read_str):
    decode_line = ''
    for i in range(0, len(read_str)):
        if i == 0 and len(format(read_str[i], 'b')) != 8:
            decode_line += f"{(8 - len(format(read_str[i], 'b'))) * '0'}{format(read_str[i], 'b')}"
        else:

            decode_line += format(read_str[i], 'b')
    return decode_line


def decodeTable():
    with open('table.txt', 'r') as f:
        lines = f.read().splitlines()
    decode_table_dict = {}
    for line in lines:
        line_value = line.split(', ')
        decode_table_dict[line_value[0]] = line_value[1]
    return decode_table_dict
