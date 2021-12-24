import pickle
import sys
from lzw import utils

DIR_COMPRESSED = 'compressedFiles'


def write_file(encoded_string, dictionary, output_file):
    data = dict(encoded_string=encoded_string, dictionary=dictionary)
    with open(output_file, 'wb') as f:
        pickle.dump(data, f)


class LZW():
    def __init__(self, text_dict):
        self.text_dict = text_dict

    def _longest_prefix_match(self, string, list):
        max_idx = 0
        max_value = 0
        for i in range(len(list)):
            prefix_len = 0
            for j in range(len(string)):
                if j < len(list[i]) and list[i][j] == string[j]:
                    prefix_len += 1
                else:
                    break
            if prefix_len > max_value:
                max_value = prefix_len
                max_idx = i
        return max_idx

    def encode(self, input_string):
        output = []
        act_string = str(input_string)

        dictionary = list(self.text_dict)

        while act_string != "":
            idx = self._longest_prefix_match(act_string, dictionary)

            act_string = act_string[len(dictionary[idx]):]
            if act_string != "":
                dictionary.append(dictionary[idx] + act_string[0])

            output.append(idx + 1)
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
        read_str = utils.read_file(path)
        if not read_str:
            print("Файл не найден. Введите путь ещё раз.")
            path = utils.input_path()
        else:
            text_from_file = read_str
            dictionary = list(sorted(set(list(text_from_file))))

            lzw = LZW(dictionary)
            encoded_string = lzw.encode(text_from_file)
            name_file = utils.nameFiles(path)

            write_file(encoded_string,dictionary, 'compressedFiles/compressed.txt')

            print(f'Файл {name_file} был успешно сжат.')
