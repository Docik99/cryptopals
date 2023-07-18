def hex_xor(hexdata1, hexdata2):
    dec1 = int(hexdata1, 16)
    dec2 = int(hexdata2, 16)
    xor = dec1 ^ dec2
    return hex(xor)[2:]


def main():
    data1 = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"
    hex_xor(data1, key)


if __name__ == "__main__":
    main()
