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


def solve_v2(puzzle):
    root = solve(puzzle)
    culprit = find_culprit(root, puzzle)
    _, weight, _ = find(culprit, puzzle)
    return weight + find_weight_difference(culprit, puzzle)


def find_culprit(node, tree):
    parent, weight, children = find(node, tree)
    different = find_different(children, tree)

    if not different:
        return parent
    else:
        return find_culprit(different, tree)


def get_weight(root, tree):
    _, weight, children = find(root, tree)

    if not children:
        return weight
    else:
        for child in children:
            weight += get_weight(child, tree)
    return weight


def get_children(root, tree):
    _, _, children = find(root, tree)
    return children


def find_different(children, tree):
    weights = []
    for child in children:
        weights.append(get_weight(child, tree))

    # see if they are all the same
    if weights.count(weights[0]) == len(weights):
        return

    # find the weight that is different
    for i, weight in enumerate(weights):
        if weights.count(weight) == 1:
            return children[i]


def find_weight_difference(brother, tree):
    weights = []
    for line in tree:
        parent, weight, children = line
        if brother in children:
            for child in children:
                weights.append(get_weight(child, tree))
            normal, different = 0, 0
            for weight in weights:
                if weights.count(weight) > 1:
                    normal = weight
                else:
                    different = weight
            return normal - different


def find(node, tree):
    for line in tree:
        parent, weight, children = line
        if node == parent:
            return parent, weight, children


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
