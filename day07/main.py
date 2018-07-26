def solve(puzzle):
    global_parents = []
    global_children = []

    for line in puzzle:
        parent, children = line
        if children:
            global_parents.append(parent)
            global_children += children

    for parent in global_parents:
        if parent not in global_children:
            return parent


def process_line(line):
    children = []
    temp_line = line.split(' -> ')
    parent = temp_line[0].split(' (')[0]

    if len(temp_line) > 1:
        children = temp_line[1].split(', ')
        children[-1] = children[-1].strip()
    return parent, children


def main():
    puzzle = []
    with open('input.txt', 'r') as input_file:
        for line in input_file.readlines():
            puzzle.append(process_line(line))
    print(solve(puzzle))


if __name__ == '__main__':
    main()
