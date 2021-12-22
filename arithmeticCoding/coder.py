import decimal
import os
import sys
from decimal import Decimal

from arithmeticCoding import utils
from collections import Counter

from arithmeticCoding.utils import write_result_file

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
decimal.getcontext().prec = 100000
DIR_COMPRESSED = 'compressedFiles'


def arithmetic_coding_encode(text):
    text_length = len(text)
    text_dict = Counter(text)
    segment_dict = utils.segment_list(text_dict, text_length)

    lower_bound = Decimal(0.0)
    upper_bound = Decimal(1.0)

    for symbol in text:
        curr_range = upper_bound - lower_bound
        upper_bound = Decimal(lower_bound + (curr_range * segment_dict.get(symbol)[1]))
        lower_bound = Decimal(lower_bound + (curr_range * segment_dict.get(symbol)[0]))
    result_code = (upper_bound + lower_bound) / 2
    return Decimal(result_code), text_dict, text_length


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
            code, text_dict, symbol_length = arithmetic_coding_encode(read_str)
            print(code)
            utils.dirIsExsists(DIR_COMPRESSED)
            name_file = utils.nameFiles(path)
            print(text_dict)

            res_text = write_result_file(code, text_dict, symbol_length)

            with open(f'{DIR_COMPRESSED}/comp_{name_file}.txt', 'w', encoding='UTF-8') as f:
                f.write(res_text)
            print(f'Файл {name_file} был успешно сжат.')