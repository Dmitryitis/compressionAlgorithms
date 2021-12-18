import heapq
import os
from collections import Counter
from collections import namedtuple
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from huffman import utils


class Node(namedtuple("Node", ["left", "right"])):
    def build(self, code, acc):
        self.left.build(code, acc + "0")
        self.right.build(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def build(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(text):
    huffman_list = []

    for symbol, repetition in Counter(text).items():
        huffman_list.append((repetition, len(huffman_list), Leaf(symbol)))
    heapq.heapify(huffman_list)
    count = len(huffman_list)
    while len(huffman_list) > 1:
        repetition1, count1, left = heapq.heappop(huffman_list)
        repetition2, count2, right = heapq.heappop(huffman_list)

        heapq.heappush(huffman_list, (repetition1 + repetition2, count, Node(left, right)))
        count += 1
    code = {}
    if huffman_list:
        [(_repetition, _count, root)] = huffman_list
        root.build(code, "")
    return code


if __name__ == '__main__':
    path = ''
    flag = True
    while flag:

        if len(sys.argv) > 1:
            path = sys.argv[1]
        else:
            path = utils.input_path()
        read_str = utils.read_file(path)
        if not read_str:
            print("Файл не найден. Введите путь ещё раз.")
            path = utils.input_path()
        else:
            code = huffman_encode(read_str)
            encoded = "".join(code[symbol] for symbol in read_str)
            print(code)
            with open('output.txt', 'wb') as f:
                f.write(utils.toBytesText(encoded))
            flag = False
