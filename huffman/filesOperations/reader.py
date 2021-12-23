import ast
import codecs

DIR_COMPRESSED = 'compressedFiles'

decoder = codecs.getincrementaldecoder('utf-8')()


class FileReader:
    def __init__(self):
        self.file = open('table.txt', 'rb')

    def _read_str(self, precision):
        return decoder.decode(self.file.read(precision))

    def _read_symbols_dict(self):
        res_str = ''
        while True:
            bt = self.file.read(1)
            sym = decoder.decode(bt)
            res_str += sym
            if bt == b'':
                break
        return res_str

    def read(self):
        dictionary = self._read_symbols_dict()
        dictionary = ast.literal_eval(dictionary)
        self.file.close()

        return dictionary
