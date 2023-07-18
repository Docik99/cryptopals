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


def get_score(input_bytes):
    score = 0

    for byte in input_bytes:
        score += CHARACTER_FREQ.get(chr(byte).lower(), 0)

    return score


def xor(input_bytes, key_value):
    output = b''

    for char in input_bytes:
        output += bytes([char ^ key_value])

    return output


def brute_force(secret):
    candidates = []

    for candidate in range(256):
        text = xor(secret, candidate)
        score = get_score(text)

        result = {
            'key': candidate,
            'score': score,
            'text': text
        }

        candidates.append(result)

    return sorted(candidates, key=lambda c: c['score'], reverse=True)


def print_result(results):
    for result in results:
        try:
            print(
                f"{result['text'].decode()}   Score: {int(result['score'])}    Key: {chr(result['key'])}")
        except BaseException:
            print("'utf-8' codec can't decode byte")


def main():
    secret = bytes.fromhex(
        "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    results = brute_force(secret)
    print_result(results)


if __name__ == "__main__":
    main()
