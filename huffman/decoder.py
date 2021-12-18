import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from huffman import utils
DIR_RESULT_DECODE = 'decodeFile'

def huffman_decode(encoded, code):
    decode_text = []
    enc_symbol = ''
    for symbol in encoded:
        enc_symbol += symbol
        for dec_ch in code:
            if code.get(dec_ch) == enc_symbol:
                decode_text.append(dec_ch)
                enc_symbol = ''
                break
    return "".join(decode_text)


if __name__ == '__main__':
    path = ''
    flag = True
    while flag:
        if len(sys.argv) > 1:
            path = sys.argv[1]
        else:
            path = utils.input_path()
        read_str = utils.read_file_decode(path)

        if not read_str:
            print("Файл не найден. Введите путь ещё раз.")
            path = utils.input_path()
        else:
            decode_line = utils.decodeFileToString(read_str)
            decode_table = utils.decodeTable()
            utils.dirIsExsists(DIR_RESULT_DECODE)
            name_file = utils.nameFiles(path)
            result = huffman_decode(decode_line, decode_table)
            with open(f'{DIR_RESULT_DECODE}/resultDecode.txt', 'w') as f:
                f.write(result)
            print(f'Файл {name_file} был успешно раскодирован.')
            flag = False
