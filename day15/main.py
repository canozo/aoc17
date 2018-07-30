def solve(puzzle):
    pairs = 0
    a, b = puzzle
    for num in range(40000000):
        a, b = get_values(a, b)
        if bin(a)[-16:] == bin(b)[-16:]:
            pairs += 1
    return pairs


def solve_v2(puzzle):
    return puzzle


def get_values(a, b):
    factor_a = 16807
    factor_b = 48271
    divide_by = 2147483647

    a = (a * factor_a) % divide_by
    b = (b * factor_b) % divide_by

    return a, b


def process(text):
    gen_a = int(text[0].split('with ')[1])
    gen_b = int(text[1].split('with ')[1])
    return gen_a, gen_b


def main():
    part = int(input('part: '))

    with open('input.txt', 'r') as some:
        puzzle = process(some.readlines())

    if part == 1:
        print(solve(puzzle))
    elif part == 2:
        print(solve_v2(puzzle))


if __name__ == '__main__':
    main()

