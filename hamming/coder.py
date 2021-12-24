import random
import sys

from hamming import utils

BLOCK_LENGTH = 8
BITS = [i for i in range(1, BLOCK_LENGTH + 1) if not i & (i - 1)]


class Hamming:
    def __init__(self, text):
        self.text = text

    def set_empty_check_bits(self, value_bin):
        for bit in BITS:
            value_bin = value_bin[:bit - 1] + '0' + value_bin[bit - 1:]

        return value_bin

    def set_check_bits(self, value_bin):
        value_bin = self.set_empty_check_bits(value_bin)
        check_bits_data = self.get_bits_check_from_data(value_bin)
        for check_bit, bit_value in check_bits_data.items():
            value_bin = '{0}{1}{2}'.format(
                value_bin[:check_bit - 1], bit_value, value_bin[check_bit:])
        return value_bin

    def exclude_check_bits(self, value_bin):
        clean_value_bin = ''
        for index, char_bin in enumerate(list(value_bin), 1):
            if index not in BITS:
                clean_value_bin += char_bin

        return clean_value_bin

    def check_and_fix_error(self, encoded_block):
        check_bits_encoded = self.check_bits(encoded_block)
        check_item = self.exclude_check_bits(encoded_block)
        check_item = self.set_check_bits(check_item)
        check_bits = self.check_bits(check_item)
        if check_bits_encoded != check_bits:
            invalid_bits = []
            for check_bit_encoded, value in check_bits_encoded.items():
                if check_bits[check_bit_encoded] != value:
                    invalid_bits.append(check_bit_encoded)
            num_bit = sum(invalid_bits)
            encoded_block = '{0}{1}{2}'.format(
                encoded_block[:num_bit - 1],
                int(encoded_block[num_bit - 1]) ^ 1,
                encoded_block[num_bit:])
        return encoded_block

    def check_bits(self, value_bin):
        check_bits = {}
        for index, value in enumerate(value_bin, 1):
            if index in BITS:
                check_bits[index] = int(value)
        return check_bits

    def block_iterator(self, text_bin, block_size=BLOCK_LENGTH):
        for i in range(len(text_bin)):
            if not i % block_size:
                yield text_bin[i:i + block_size]

    def get_bits_check_from_data(self, value_bin):
        check_bits_count_map = {k: 0 for k in BITS}
        for index, value in enumerate(value_bin, 1):
            if int(value):
                bin_char_list = list(bin(index)[2:].zfill(16))
                print(bin_char_list)
                bin_char_list.reverse()
                print(bin_char_list)
                for degree in [2 ** int(i) for i, value in enumerate(bin_char_list) if int(value)]:
                    check_bits_count_map[degree] += 1
        check_bits_value_map = {}
        print(check_bits_count_map)
        for check_bit, count in check_bits_count_map.items():
            check_bits_value_map[check_bit] = 0 if not count % 2 else 1
        return check_bits_value_map

    def encode(self):
        text_in_bin = utils.text_to_bin(self.text)
        print(text_in_bin)
        result = ''
        for block_bin in self.block_iterator(text_in_bin):
            block_bin = self.set_check_bits(block_bin)
            result += block_bin
        return result

    def decode(self, fix_errors=True):
        decoded_value = ''
        fixed_encoded_list = []
        for encoded_block in self.block_iterator(self.text, BLOCK_LENGTH + len(BITS)):
            if fix_errors:
                encoded_block = self.check_and_fix_error(encoded_block)
            fixed_encoded_list.append(encoded_block)

        clean_block_list = []
        for encoded_block in fixed_encoded_list:
            encoded_block = self.exclude_check_bits(encoded_block)
            clean_block_list.append(encoded_block)

        for clean_block in clean_block_list:
            for clean_char in [clean_block[i:i + 16] for i in range(len(clean_block)) if not i % 16]:
                decoded_value += chr(int(clean_char, 2))
        return decoded_value


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
            name_file = utils.nameFiles(path)
            hamming = Hamming(read_str)
            encoded = hamming.encode()
            with open('compressed_file.txt', 'wb') as f:
                f.write(utils.toBytesText(encoded))

            print(f'Файл {name_file} был успешно сжат.')