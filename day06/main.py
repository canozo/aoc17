def solve(puzzle):
    seen = []
    steps = 0
    while to_string(puzzle) not in seen:
        seen.append(to_string(puzzle))
        balance(puzzle)
        steps += 1
    return steps


def debugging(puzzle):
    seen = []
    while to_string(puzzle) not in seen:
        seen.append(to_string(puzzle))
        balance(puzzle)

    seen = []
    cycles = 0
    while to_string(puzzle) not in seen:
        seen.append(to_string(puzzle))
        balance(puzzle)
        cycles += 1
    return cycles


def balance(mem_banks):
    size = len(mem_banks)
    value = max(mem_banks)
    index = mem_banks.index(value)
    mem_banks[index] = 0

    index += 1
    while value > 0:
        mem_banks[index % size] += 1
        index += 1
        value -= 1


def to_string(the_list):
    return ''.join(map(str, the_list))


def main():
    part = int(input('part: '))
    _input = '0	5	10	0	11	14	13	4	11	8	8	7	1	4	12	11'
    mem_banks = [int(x) for x in _input.split('\t')]
    if part == 1:
        print(solve(mem_banks))
    elif part == 2:
        print(debugging(mem_banks))


if __name__ == '__main__':
    main()
