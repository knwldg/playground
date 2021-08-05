def roman_to_int(s: str) -> int:
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total, buffer = 0, 0

    for c in s[::-1]:
        value = values[c]
        if value >= buffer:
            total += value
        if value < buffer:
            total -= value
        buffer = value

    return total


if __name__ == '__main__':
    print(roman_to_int("XIV"))
