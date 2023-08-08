import bitarray
from base64 import b64decode


CHARACTER_FREQ = {
    'e': 12.6,
    't': 9.37,
    'a': 8.34,
    'o': 7.7,
    'n': 6.8,
    'i': 6.71,
    'h': 6.11,
    's': 6.11,
    'r': 5.68,
    'l': 4.24,
    'u': 2.85,
    ' ': 15}


def hamming_distance(first_str, second_str):
    first = bitarray.bitarray()
    first.frombytes(first_str)

    sec = bitarray.bitarray()
    sec.frombytes(second_str)

    first ^= sec
    i = 0
    for bit in first:
        i += bit
    return i


def scoring_key_size(cipher_text):
    size_scores = {}
    score = 0
    for sizeKey in range(2, 41):
        count_slices = len(cipher_text) // (sizeKey * 2)
        for i in range(count_slices):
            slice_1 = slice(i * sizeKey, (i + 1) * sizeKey)
            slice_2 = slice((i + 1) * sizeKey, (i + 2) * sizeKey)

            score += hamming_distance(cipher_text[slice_1], cipher_text[slice_2])
        score /= sizeKey
        score /= count_slices
        size_scores[sizeKey] = score
    return sorted(size_scores, key=size_scores.get)[0]


def scoring(input_bytes):
    score = 0

    for byte in input_bytes:
        score += CHARACTER_FREQ.get(chr(byte).lower(), 0)

    return score


def xor(input_bytes, key_value):
    output = b''

    for char in input_bytes:
        output += bytes([char ^ key_value])

    return output


def xor2(text, key):
    newtext = b''
    i = 0

    for byte in text:
        newtext += bytes([byte ^ key[i]])

        i = i + 1 if (i < len(key) - 1) else 0

    return newtext


def brute_force_key(cipher_block):
    candidates = []

    for candidate in range(256):
        text = xor(cipher_block, candidate)
        score = scoring(text)
        result = {'key': candidate, 'score': score}
        candidates.append(result)

    return sorted(candidates, key=lambda c: c['score'], reverse=True)[0]


def get_blocks(key_size, text):
    key = ""
    message = ""
    for i in range(key_size):
        block = text[i::key_size]
        part = brute_force_key(block)
        key += chr(part['key'])
        message += part['text'].decode()
    print(key)

    print(xor2(bytes(text), bytes(key.encode('utf-8'))))


def main():
    with open('Files/ch_6.txt', 'r', encoding='utf-8') as file:
        text = b64decode(file.read())
        key_size = scoring_key_size(text)
        get_blocks(key_size, text)


if __name__ == "__main__":
    main()
