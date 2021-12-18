import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from huffman import utils
import codecs

if __name__ == '__main__':
    path = ''
    flag = True
    while flag:

        if len(sys.argv) > 1:
            path = sys.argv[1]
        else:
            path = utils.input_path()
        read_str = utils.read_file_decode(path)
        decode_line = ''
        for i in range(0, len(read_str)):
            if i == 0 and len(format(read_str[i], 'b')) != 8:
                decode_line += f"{(8 - len(format(read_str[i], 'b')))*'0'}{format(read_str[i], 'b')}"
            else:

                decode_line += format(read_str[i], 'b')
        print(decode_line)

        flag = False
        if not read_str:
            print("Файл не найден. Введите путь ещё раз.")
            path = utils.input_path()
        else:
            print('re')
