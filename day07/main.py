import re


def solve(puzzle):
    global_parents = []
    global_children = []

    for line in puzzle:
        parent, _, children = line
        if children:
            global_parents.append(parent)
            global_children += children

    for parent in global_parents:
        if parent not in global_children:
            return parent


def solve_v2():
    global_parents = []
    global_children = []

    for line in puzzle:
        parent, weight, children = line
        if children:
            global_parents.append(parent)
            global_children += children

    for parent in global_parents:
        if parent not in global_children:
            return parent


def process_line(line):
    children = []
    temp_line = line.split(' -> ')
    parent, weight = temp_line[0].split(' (')
    weight = int(re.sub('[ )\n]', '', weight))

    if len(temp_line) > 1:
        children = temp_line[1].split(', ')
        children[-1] = children[-1].strip()
    return parent, weight, children


def main():
    puzzle = []
    part = int(input('part: '))

    with open('input.txt', 'r') as input_file:
        for line in input_file.readlines():
            puzzle.append(process_line(line))

    if part == 1:
        print(solve(puzzle))
    elif part == 2:
        print(solve_v2(puzzle))


if __name__ == '__main__':
    main()
