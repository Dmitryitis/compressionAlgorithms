import pickle
import sys
from lzw import utils

DIR_RESULT_DECODE = 'decodeFile'


class LZW():
    def __init__(self, text_dict):
        self.text_dict = text_dict

    def decode(self, encoded_string):
        output = ""
        act_string = list(encoded_string)
        dictionary = list(self.text_dict)

        first = True
        while len(act_string) != 0:
            act_element = act_string.pop(0) - 1
            if first:
                first = False
            else:
                dictionary[-1] = dictionary[-1] + dictionary[act_element][0]

            output += dictionary[act_element]
            dictionary.append(dictionary[act_element])

        return output


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
            with open(path, 'rb') as f:
                data = pickle.load(f)
                encoded_string = data['encoded_string']
                dictionary = data['dictionary']
            lzw = LZW(dictionary)
            name_file = utils.nameFiles(path)
            encoded_string = lzw.decode(encoded_string)
            with open('decodeFile/file_decoded.txt', 'w', encoding='utf-8') as f:
                f.write(encoded_string)

            print(f'Файл {name_file} был успешно раскодирован.')

