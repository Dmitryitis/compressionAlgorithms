DIR_COMPRESSED = 'compressedFiles'


class FileWriter:
    def __init__(self):
        self.file = open(f'table.txt', 'wb+')

    def _write_int(self, number_int, precision):
        number_bytes = number_int.to_bytes(precision, byteorder='big', signed=True)
        self.file.write(number_bytes)

    def _write_str(self, symbol):
        number_bytes = symbol.encode('utf-8', 'replace')
        self.file.write(number_bytes)

    def _write_symbols(self, text_dict):
        self._write_str("{")
        for key, value in text_dict.items():
            self._write_str("'")
            self._write_str(key)
            self._write_str("'")
            self._write_str(":")
            self._write_str("'")
            self._write_str(str(value))
            self._write_str("'")
            self._write_str(",")
        self._write_str("}")

    def write(self, code):
        self._write_symbols(code)
        self.file.close()
