import decimal
import sys
from decimal import Decimal

from arithmeticCoding import utils
from arithmeticCoding.filesOperations.reader import FileReader

decimal.getcontext().prec = 100000
DIR_RESULT_DECODE = 'decodeFile'


def arithmetic_coding_decode(code, text_dict, text_length):
    decoded_str = ""
    code_el = code

    segment_dict = utils.segment_list(text_dict, text_length)

    while text_length != len(decoded_str):
        for key, value in sorted(segment_dict.items()):

            if segment_dict.get(key)[0] <= code_el < segment_dict.get(key)[1]:
                decoded_str += key
                code_el = Decimal(code_el - segment_dict.get(key)[0]) / Decimal(
                    segment_dict.get(key)[1] - segment_dict.get(key)[0])
                if text_length == len(decoded_str):
                    break

    return decoded_str


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
        read_str = utils.read_file_decode(path)

        if not read_str:
            print("Файл не найден. Введите путь ещё раз.")
            path = utils.input_path()
        else:
            code, text_dict, symbol_length = utils.read_decode_file(path)
            utils.dirIsExsists(DIR_RESULT_DECODE)
            name_file = utils.nameFiles(path)
            result = arithmetic_coding_decode(Decimal(code), text_dict, int(symbol_length))
            with open(f'{DIR_RESULT_DECODE}/resultDecode.txt', 'w') as f:
                f.write(result)
            print(f'Файл {name_file} был успешно раскодирован.')
