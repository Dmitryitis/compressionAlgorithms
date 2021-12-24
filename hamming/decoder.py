import sys

from hamming import utils
from hamming.coder import Hamming

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
            name_file = utils.nameFiles(path)
            with open(path, 'rb') as f:
                text = f.read()
            decode_text_from_file = utils.decodeFileToString(text)
            hamming = Hamming(decode_text_from_file)
            decoded = hamming.decode()

            with open('final_file.txt', 'w', encoding='utf-8') as f:
                f.write(decoded)

            print(f'Файл {name_file} был успешно раскодирован.')