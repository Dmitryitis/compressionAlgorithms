import sys
from struct import *
from lzw import utils
from lzw.utils import writeDictionary

DIR_COMPRESSED = 'compressedFiles'

def decoder(data, dic):
    compressed_data = []
    next_code = len(dic.keys())
    decompressed_data = ""
    string = ""
    dic = {v: k for k, v in dic.items()}
    for i in data:
        compressed_data.append(i)
    print(dic)
    for code in compressed_data:
        if not (code in dic):
            dic[code] = string + (string[0])
            print(dic[code])
        decompressed_data += dic[code]
        if not (len(string) == 0):
            dic[next_code] = string + dic[code]
            next_code += 1
        string = dic[code]
    print(decompressed_data)


def lzw_coder(data):
    dictionary_size = len(data)
    dictionary = {}
    for i in range(len(data)):
        if not data[i] in dictionary:
            dictionary[data[i]] = i
    string = ''
    compressed_data = []
    maximum_table_size = pow(2, int(len(data)))

    text_dict = writeDictionary(dictionary)
    with open('table.txt', 'w', encoding='utf-8') as f:
        f.write(text_dict)

    for symbol in data:
        string_plus_symbol = string + symbol
        if string_plus_symbol in dictionary:
            string = string_plus_symbol
        else:
            compressed_data.append(dictionary[string])
            if (len(dictionary) <= maximum_table_size):
                dictionary[string_plus_symbol] = dictionary_size
                dictionary_size += 1
            string = symbol

    if string in dictionary:
        compressed_data.append(dictionary[string])

    utils.dirIsExsists(DIR_COMPRESSED)
    output_file = open(DIR_COMPRESSED + "/compressed.txt", "wb")
    for data in compressed_data:
        output_file.write(pack('>H', int(data)))

    output_file.close()

    return compressed_data, dictionary


if __name__ == '__main__':
    path = ''
    flag = True
    print('Для выхода введите команду: exit')
    while flag:
        if len(sys.argv) > 1:
            path = sys.argv[1]
        else:
            path = utils.input_path()
        if path == 'exit':
            flag = False
            break
        read_str = utils.read_file(path)
        if not read_str:
            print("Файл не найден. Введите путь ещё раз.")
            path = utils.input_path()
        else:
            text_from_file = read_str
            compressed_data, dictionary = lzw_coder(text_from_file)
            decoder(compressed_data, dictionary)
            name_file = utils.nameFiles(path)

            print(f'Файл {name_file} был успешно сжат.')
