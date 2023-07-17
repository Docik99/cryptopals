import base64

if __name__ == '__main__':
    secret = b"1c0111001f010100061a024b53535009181c"
    secret = secret ^ secret
    print(secret)
