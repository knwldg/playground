def check_pangram(sentence) -> bool:
    az = [chr(i) for i in range(97, 123)]

    d = {letter: False for letter in az}

    for c in sentence:
        d[c] = True

    return all(d.values())


def check_fast(sentence):
    a = set(sentence)
    b = set([chr(i) for i in range(97, 123)])

    return len(a & b) == 26


if __name__ == '__main__':
    print(check_fast(
        "cspduleznlxgqqhohsvvxdoloranhqvirefamevwuxjjnjwmwzodsbxocxbojrphonvwkdnpaibajcgntvaiuwfhwcgbjvlwhvmszivogcxvzxwjjjgeekplruvlcftudtceaqddufknmojbwgwisvgowqfppmaqhkhrbqomijhjitgxkpragvgsjxnomnx"))
    print(check_fast("thequickbrownfoxjumpsoverthelazydog"))
