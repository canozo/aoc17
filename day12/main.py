def solve(pipes, connected_to, grouped=[]):
    if connected_to not in grouped:
        grouped.append(connected_to)

        for line in pipes:
            if connected_to in line:
                for num in line:
                    solve(pipes, num)

    return grouped


def solve_v2(pipes):
    groups = 0
    already_grouped = []

    for num in range(2000):
        if num not in already_grouped:
            already_grouped += solve(pipes, num)
            groups += 1

    return groups


def process_pipes(puzzle):
    result = []
    for line in puzzle:
        pipe, pipes = line.split(' <-> ')
        temp_pipes = [pipe]
        temp_pipes += pipes.split(', ')
        temp_pipes[-1] = temp_pipes[-1].strip()
        result.append(list(map(int, temp_pipes)))
    return result


def main():
    with open('input.txt', 'r') as input_file:
        puzzle = input_file.readlines()

    pipes = process_pipes(puzzle)
    part = int(input('part: '))

    if part == 1:
        print(len(solve(pipes, 0)))
    elif part == 2:
        print(solve_v2(pipes))


if __name__ == '__main__':
    main()

