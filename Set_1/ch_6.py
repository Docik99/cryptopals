import bitarray


def hamming_distance():
    first = bitarray.bitarray()
    first.frombytes('this is a test'.encode('utf-8'))

    sec = bitarray.bitarray()
    sec.frombytes('wokka wokka!!!'.encode('utf-8'))

    first ^= sec
    i = 0
    for bit in first:
        i += bit
    print(i)


def main():
    hamming_distance()


if __name__ == "__main__":
    main()