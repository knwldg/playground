import tools


def interpret(command: str) -> str:
    ret = ""

    for i, c in enumerate(command):
        if c == 'G':
            ret += 'G'
        elif c == '(':
            next_val = command[i + 1]
            if next_val == ')':
                ret += 'o'
            elif next_val == 'a':
                ret += 'al'
        else:
            continue

    return ret


def interpret_fast(command: str) -> str:
    return command.replace('()', 'o').replace('(al)', 'al')


if __name__ == '__main__':
    print(tools.time_function_ns(interpret, "G()(al)"))
    print(tools.time_function_ns(interpret, "G()()()()(al)"))
    print(tools.time_function_ns(interpret, "(al)G(al)()()G"))

    print(tools.time_function_ns(interpret_fast, "G()(al)"))
    print(tools.time_function_ns(interpret_fast, "G()()()()(al)"))
    print(tools.time_function_ns(interpret_fast, "(al)G(al)()()G"))
