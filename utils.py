def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text) + '1111111111111110'

def binary_to_text(binary_data):
    chars = []
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if byte == '11111111':
            break
        chars.append(chr(int(byte, 2)))
    return ''.join(chars)
