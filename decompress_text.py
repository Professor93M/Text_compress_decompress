import pickle


def load_and_decompress(input_filename):
    if not input_filename.endswith(".pkl"):
        input_filename += ".pkl"
    with open(input_filename, 'rb') as f:
        encoding_table, encoded_text = pickle.load(f)

    decoding_table = {code: char for char, code in encoding_table.items()}
    decoded_text = ""
    code = ""
    for bit in encoded_text:
        code += bit
        if code in decoding_table:
            decoded_text += decoding_table[code]
            code = ""
    
    # Extracting the original text to a new file
    output_filename = input_filename.replace(".pkl", "_decompressed.txt")
    with open(output_filename, 'w') as f:
        f.write(decoded_text)
    
    return decoded_text


if __name__ == "__main__":
    input_filename = input("Enter filename to decompress: ")
    decompressed_text = load_and_decompress(input_filename)
    print("Decompressed text:")
    print(decompressed_text)
