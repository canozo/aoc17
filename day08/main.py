def solve(puzzle):
    registers = {}
    for line in puzzle:
        process_line(registers, line)
    return max(registers.values())


def solve_mkii(puzzle):
    max_value = 0
    registers = {}
    for line in puzzle:
        process_line(registers, line)
        temp_max = max(registers.values())
        if temp_max > max_value:
            max_value = temp_max
    return max_value


def process_line(registers, line):
    action, condition = line.split(' if ')
    if 'dec' in action:
        # decrement
        register, modify_by = action.split(' dec ')
        execute = dec
    else:
        # increment
        register, modify_by = action.split(' inc ')
        execute = inc

    if register not in registers:
        registers[register] = 0

    if evaluate(registers, condition):
        execute(registers, register, int(modify_by))


def evaluate(registers, condition):
    result = False
    register, operator, value = condition.split()
    value = int(value)

    if register not in registers:
        registers[register] = 0

    if operator == '<':
        result = registers[register] < value
    elif operator == '>':
        result = registers[register] > value
    elif operator == '<=':
        result = registers[register] <= value
    elif operator == '>=':
        result = registers[register] >= value
    elif operator == '==':
        result = registers[register] == value
    elif operator == '!=':
        result = registers[register] != value

    return result


def inc(registers, register, value):
    registers[register] += value


def dec(registers, register, value):
    registers[register] -= value


def main():
    part = int(input('part: '))

    with open('input.txt', 'r') as input_file:
        puzzle = input_file.readlines()

    if part == 1:
        print(solve(puzzle))
    elif part == 2:
        print(solve_mkii(puzzle))


if __name__ == '__main__':
    main()
