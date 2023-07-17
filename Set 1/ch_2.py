def hex_xor(hexdata1, hexdata2):
    dec1 = int(hexdata1, 16)
    dec2 = int(hexdata2, 16)
    xor = dec1 ^ dec2
    return hex(xor)[2:]


if __name__ == '__main__':
    assert hex_xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965") == \
           "746865206b696420646f6e277420706c6179"
    print("Passed")
