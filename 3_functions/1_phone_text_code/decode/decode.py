def decode_numbers(numbers: str) -> str | None:
    keypad = {
        '1': '.,?!:;',
        '2': 'абвг',
        '3': 'дежз',
        '4': 'ийкл',
        '5': 'мноп',
        '6': 'рсту',
        '7': 'фхцч',
        '8': 'шщъы',
        '9': 'ьэюя',
        '0': ' '
    }

    sequences = numbers.split()
    result = []

    for seq in sequences:
        if not seq or seq[0] not in keypad:
            return None

        key = seq[0]

        if any(char != key for char in seq):
            return None

        press_count = len(seq)

        if press_count > len(keypad[key]):
            return None

        result.append(keypad[key][press_count - 1])

    result = ''.join(result)

    return result
