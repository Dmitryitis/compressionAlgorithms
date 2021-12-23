import ast
import codecs
import struct
from decimal import Decimal

DIR_COMPRESSED = 'compressedFiles'

decoder = codecs.getincrementaldecoder('utf-8')()


class FileReader:
    def __init__(self, filename):
        self.file = open(filename, 'rb')

    def _read_int(self, precision):
        return int.from_bytes(self.file.read(precision), byteorder='big')

    def _read_str(self, precision):
        return decoder.decode(self.file.read(precision))

    def _read_symbols_dict(self):
        res_str = ''
        while True:
            symbol = decoder.decode(self.file.read(1))
            res_str += symbol
            if symbol == '\n':
                break
        return res_str

    def _read_code(self):
        res_str = ''
        while True:
            symbol = self._read_int(10)
            print(symbol)
            res_str += str(symbol)
            if symbol == -1:
                break
        return res_str

    def _numbers(self, symbol_count):
        symbols = [self._read_int(1) for _ in range(symbol_count, symbol_count * 2)]
        return symbols

    def bin2float(self, b):
        h = int(b, 2).to_bytes(8, byteorder="big")
        return struct.unpack('>d', h)[0]

    def decodeFileToString(self, read_str):
        decode_line = ''
        for i in range(0, len(read_str)):
            if i == len(read_str) - 2:
                decode_line += f"{(int(read_str[i + 1]) - len(format(read_str[i], 'b'))) * '0'}{format(read_str[i], 'b')}"
            elif i == len(read_str) - 1:
                break
            else:
                decode_line += f"{(8 - len(format(read_str[i], 'b'))) * '0'}{format(read_str[i], 'b')}"
        return decode_line

    def _read_code_float(self):
        res_str = ''
        while True:
            bt = self.file.read(1)
            for sym in bt:
                print(sym)
            print(bt)
            if bt == '-':
                break
        return res_str


    def _read_symbol_length(self):
        res_str = ''
        while True:
            bt = self.file.read(1)
            sym = decoder.decode(bt)
            res_str += sym
            if sym == '\n':
                break
        return res_str

    def _read_dictionary(self):
        res_str = ''
        while True:
            bt = self.file.read(1)
            sym = decoder.decode(bt)
            res_str += sym
            if bt == b'':
                break
        return res_str

    def read(self):
        code_float = self._read_code_float()
        symbol_length = self._read_symbol_length()
        dictionary = self._read_dictionary()
        dictionary = ast.literal_eval(dictionary)
        self.file.close()

        return code_float, dictionary, symbol_length
