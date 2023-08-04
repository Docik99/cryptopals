import bitarray


def hamming_distance(first_str, second_str):
    first = bitarray.bitarray()
    first.frombytes(first_str.encode('utf-8'))

    sec = bitarray.bitarray()
    sec.frombytes(second_str.encode('utf-8'))

    first ^= sec
    i = 0
    for bit in first:
        i += bit
    print(i)


def main():
    hamming_distance('this is a test', 'wokka wokka!!!')


if __name__ == "__main__":
    main()