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


def brute_force(strings):
    candidates = []

    for string in strings:
        for candidate in range(256):
            text = xor(string, candidate)
            score = get_score(text)

            result = {
                'key': candidate,
                'score': score,
                'text': text
            }

            candidates.append(result)

    return sorted(candidates, key=lambda c: c['score'], reverse=True)[0]


def print_result(result):
    print(
        f"{result['text'].decode().rstrip()}   Score: {int(result['score'])}    Key: {chr(result['key'])}")


def main():
    with open('Files/ch_4.txt', 'r', encoding='utf-8') as f:
        strings = [bytes.fromhex(line.strip()) for line in f if line.strip()]
    results = brute_force(strings)
    print_result(results)


if __name__ == "__main__":
    main()
