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


def text_to_bin(text):
    symbol_bins = [bin(ord(symbol))[2:].zfill(16) for symbol in text]
    return ''.join(symbol_bins)


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


def toBytesText(data):
    r = []
    for i in range(0, len(data), 8):
        r.append(int(data[i:i + 8], 2))
        if i + 8 >= len(data):
            r.append(int(len(data) - i))
    return bytes(r)


def decodeFileToString(read_str):
    decode_line = ''
    for i in range(0, len(read_str)):
        if i == len(read_str) - 2:
            decode_line += f"{(int(read_str[i + 1]) - len(format(read_str[i], 'b'))) * '0'}{format(read_str[i], 'b')}"
        elif i == len(read_str) - 1:
            break
        else:
            decode_line += f"{(8 - len(format(read_str[i], 'b'))) * '0'}{format(read_str[i], 'b')}"
    return decode_line
