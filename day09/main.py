def solve(puzzle):
    pos = 0
    depth = 0
    score = 0
    garbage = False

    while pos < len(puzzle):
        char = puzzle[pos]
        if char == '{' and not garbage:
            depth += 1
            score += depth
            pos += 1
        elif char == '}' and not garbage:
            depth -= 1
            pos += 1
        elif char == '<' and not garbage:
            garbage = True
            pos += 1
        elif char == '>' and garbage:
            garbage = False
            pos += 1
        elif char == '!' and garbage:
            pos += 2
        else:
            pos += 1
    return score


def solve_v2(puzzle):
    pos = 0
    depth = 0
    score = 0
    garbage = False

    while pos < len(puzzle):
        char = puzzle[pos]
        if char == '{' and not garbage:
            depth += 1
            pos += 1
        elif char == '}' and not garbage:
            depth -= 1
            pos += 1
        elif char == '<' and not garbage:
            garbage = True
            pos += 1
        elif char == '>' and garbage:
            garbage = False
            pos += 1
        elif char == '!' and garbage:
            pos += 2
        elif garbage:
            score += 1
            pos += 1
        else:
            pos += 1
    return score


def main():
    part = int(input('part: '))

    with open('input.txt', 'r') as some:
        puzzle = some.read()

    if part == 1:
        print(solve(puzzle))
    elif part == 2:
        print(solve_v2(puzzle))


if __name__ == '__main__':
    main()

