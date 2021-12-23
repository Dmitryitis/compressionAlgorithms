import struct

DIR_COMPRESSED = 'compressedFiles'


class Data:
    def __init__(self, code, dictionary, symbols):
        self.code = code
        self.dictionary = dictionary
        self.symbols = symbols


class FileWriter:
    def __init__(self, filename):
        self.file = open(f'{DIR_COMPRESSED}/compress_{filename}.txt', 'wb')
        self.fileData = open(f'{DIR_COMPRESSED}/compressed_{filename}.txt', 'wb')

    def _write_int(self, number_int, precision):
        number_bytes = number_int.to_bytes(precision, byteorder='letter', signed=True)
        self.file.write(number_bytes)

    def _write_str(self, symbol):
        number_bytes = symbol.encode('utf-8', 'replace')
        self.file.write(number_bytes)

    def float2bin(self, f):
        [d] = struct.unpack(">Q", struct.pack(">d", f))
        return f'{d:064b}'

    def _write_toBytesText(self, data):
        r = []

        for i in range(0, len(data), 8):
            r.append(int(data[i:i + 8], 2))
            if i + 8 >= len(data):
                r.append(int(len(data) - i))
        return self.file.write(bytes(r))

    def _write_symbols(self, text_dict):
        self._write_str("{")
        for key, value in text_dict.items():
            self._write_str("'")
            self._write_str(key)
            self._write_str("'")
            self._write_str(":")
            self._write_str(str(value))
            self._write_str(",")
        self._write_str("}")
        self._write_str("\n")

    def write(self, code, text_dict, symbol_length):
        cod = self.float2bin(code)
        self._write_toBytesText(cod)
        self._write_str('\n')
        self._write_str(str(symbol_length))
        self._write_str('\n')
        self._write_symbols(text_dict)
        self.file.close()
