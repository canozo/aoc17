def solve(puzzle):
    remove_me = []
    global_parents = []
    global_children = []

    for line in puzzle:
        parent, children = line
        if not children:
            # do nothing
            global_children.append(parent)
            continue

        global_children += children

        if parent in global_children:
            # not add it to parents
            continue

        # ok, it's a parent (for now)
        global_parents.append(parent)

        # check if any global parents are children
        for node in global_parents:
            if node in global_children and node not in remove_me:
                remove_me.append(node)

    for node in remove_me:
        global_parents.remove(node)

    return global_parents


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
