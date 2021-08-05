def run_length_encoding(source: str) -> str:
    vals = [source[0]]
    lengths = [0]

    for c in source:
        if c == vals[len(vals) - 1]:
            lengths[len(lengths) - 1] += 1
        else:
            vals.append(c)
            lengths.append(1)

    return "".join([f"{c}{lengths[i]}" for i, c in enumerate(vals)])


def run_length_decoding(source: str) -> str:
    vals = [c for c in source[::2]]
    lengths = [int(c) for c in source[1::2]]

    return "".join([f"{c * lengths[i]}" for i, c in enumerate(vals)])


if __name__ == '__main__':
    print(run_length_encoding("wwwwaaadexxxxxxwwwwwww"))
    print(run_length_decoding(run_length_encoding("wwwwaaadexxxxxxwwwwwww")))
