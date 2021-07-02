def array_strings_are_equal(word1, word2):
    full1 = ""
    full2 = ""

    for part in word1:
        full1 += part

    for part in word2:
        full2 += part

    return full1 == full2


if __name__ == '__main__':
    print(array_strings_are_equal(["ab", "c"], ["a", "bc"]))
