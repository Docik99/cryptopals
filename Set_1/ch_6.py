import bitarray
from base64 import b64decode


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
    print(size_scores)
    print(sorted(size_scores, key=size_scores.get))


def xor(text, key):
    newtext = b''
    i = 0

    for byte in text:
        newtext += bytes([byte ^ key[i]])

        i = i + 1 if (i < len(key) - 1) else 0

    return newtext.hex()


def main():
    with open('Files/ch_6.txt', 'r', encoding='utf-8') as file:
        text = b64decode(file.read())
        scoring_key_size(text)


if __name__ == "__main__":
    main()
