import sys
from struct import *
from lzw import utils

DIR_RESULT_DECODE = 'decodeFile'


def lzw_decoder(compressed_data, dictionary):
    next_code = len(dictionary.keys())
    decompressed_data = ""
    string = ""
    print(compressed_data)

    for code in compressed_data:
        if not (code in dictionary):
            dictionary[code] = string + (string[0])
            print(dictionary[code])
        decompressed_data += dictionary[code]
        if not (len(string) == 0):
            dictionary[next_code] = string + dictionary[code]
            next_code += 1
        string = dictionary[code]

    utils.dirIsExsists(DIR_RESULT_DECODE)
    output_file = open(DIR_RESULT_DECODE + "/file_decoded.txt", "w")
    for data in decompressed_data:
        output_file.write(data)

    output_file.close()


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
        read_str = utils.isFile(path)
        if not read_str:
            print("Файл не найден. Введите путь ещё раз.")
            path = utils.input_path()
        else:
            file = open(path, "rb")
            compressed_data = []
            while True:
                rec = file.read(2)
                if len(rec) != 2:
                    break
                (data,) = unpack('>H', rec)
                compressed_data.append(data)

            dictionary = utils.decodeTable()
            dictionary = {v: k for k, v in dictionary.items()}
            print(dictionary)
            name_file = utils.nameFiles(path)
            lzw_decoder(compressed_data, dictionary)

            print(f'Файл {name_file} был успешно раскодирован.')
