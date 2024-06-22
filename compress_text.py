import pickle
from collections import Counter
import heapq


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    freq_dict = Counter(text)
    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]


def build_encoding_table(node, prefix="", table=None):
    if table is None:
        table = {}
    if node.char is not None:
        table[node.char] = prefix
    if node.left is not None:
        build_encoding_table(node.left, prefix + "0", table)
    if node.right is not None:
        build_encoding_table(node.right, prefix + "1", table)
    return table


def compress_text(text, encoding_table):
    encoded_text = "".join(encoding_table[char] for char in text)
    return encoded_text


def compress_and_save(text_file, output_filename):
    with open(text_file, 'r') as file:
        text = file.read()

    if not output_filename.endswith(".pkl"):
        output_filename += ".pkl"
    huffman_tree = build_huffman_tree(text)
    encoding_table = build_encoding_table(huffman_tree)
    encoded_text = compress_text(text, encoding_table)
    with open(output_filename, 'wb') as f:
        pickle.dump((encoding_table, encoded_text), f)
    
    return len(text), len(encoded_text)


if __name__ == "__main__":
    text_file = input("Enter the filename to compress: ")
    output_filename = input("Enter filename to save compressed text: ")
    original_length, compressed_length = compress_and_save(text_file, output_filename)
    
    compression_ratio = (original_length / compressed_length) * 100
    print("The Average of Compression: {:.2f}%".format(compression_ratio))
    print("Total Alphabets before compression:", original_length)
    print("Total Alphabets after compression is:", compressed_length)
